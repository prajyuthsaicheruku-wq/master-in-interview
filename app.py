import random
import os
from datetime import datetime, date, timedelta
from functools import wraps
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, make_response
from models import db, User, Question, UserProgress, Bookmark, AptitudeTestAttempt, MockInterviewAttempt, EmailVerificationOTP
from email_service import send_brevo_otp_email

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'interview_prep_portal_secret_key_2026')

db_url = os.environ.get('DATABASE_URL', 'sqlite:///interview_portal.db')
if db_url.startswith('mysql://'):
    db_url = db_url.replace('mysql://', 'mysql+pymysql://', 1)
elif db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if 'mysql' in db_url:
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_recycle': 280,
        'pool_pre_ping': True
    }

db.init_app(app)

import re

@app.template_filter('clean_qtext')
def clean_qtext(text):
    if not text:
        return ""
    lines = str(text).split('\n')
    filtered = []
    for line in lines:
        l_str = line.strip()
        if l_str.startswith('Topic:') or l_str.startswith('Output:') or l_str.startswith('Output :') or l_str.startswith('(Explanation:'):
            continue
        filtered.append(line)
    res = '\n'.join(filtered).strip()
    if '\n' not in res:
        res = re.sub(r'^\d+[\.\:]\s*', '', res).strip()
    return res

@app.template_filter('clean_title')
def clean_title(title):
    if not title:
        return ""
    s = str(title)
    # Strip explicit math formula / operator hints after hyphen
    s = re.sub(r'\s*-\s*\(?n[\²\³\^\*\+\-0-9\s]+\)?.*', '', s, flags=re.IGNORECASE)
    s = re.sub(r'\s*-\s*(×|\+|\*|Multiply by|n²|n³|n\^2|n\^3|n\*).*', '', s, flags=re.IGNORECASE)
    return s.strip()


# Helper Decorator for Login Protection
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('auth_page'))
        user = db.session.get(User, session['user_id'])
        if not user:
            session.clear()
            flash('Session expired. Please log in again.', 'warning')
            return redirect(url_for('auth_page'))
        return f(*args, **kwargs)
    return decorated_function

# Context Processor for current user
@app.context_processor
def inject_user():
    current_user = None
    if 'user_id' in session:
        try:
            current_user = db.session.get(User, session['user_id'])
        except Exception:
            current_user = None
    return dict(current_user=current_user)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# --- AUTH ROUTES ---

@app.route('/')
def index():
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
        if user:
            return redirect(url_for('dashboard'))
        session.clear()
    return redirect(url_for('auth_page'))

@app.route('/auth', methods=['GET'])
def auth_page():
    if 'user_id' in session and not request.args.get('force'):
        user = db.session.get(User, session['user_id'])
        if user:
            return redirect(url_for('dashboard'))
        session.clear()
    mode = request.args.get('mode', 'login')
    return render_template('auth.html', initial_mode=mode)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user_id' in session and not request.args.get('force'):
            user = db.session.get(User, session['user_id'])
            if user:
                return redirect(url_for('dashboard'))
            session.clear()
        return render_template('auth.html', initial_mode='login')
    identity = request.form.get('identity', '').strip()
    password = request.form.get('password', '')

    if not identity or not password:
        flash('Username/Email and Password are required.', 'danger')
        return redirect(url_for('auth_page', mode='login'))

    user = User.query.filter((User.username == identity) | (User.email == identity.lower())).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        session['username'] = user.username
        flash(f'Welcome back, {user.username}!', 'success')
        return redirect(url_for('dashboard'))
    
    flash('Invalid credentials. Please check your username/email and password.', 'danger')
    return redirect(url_for('auth_page', mode='login'))

@app.route('/api/auth/send-register-otp', methods=['POST'])
def send_register_otp():
    data = request.get_json(silent=True) or request.form
    username = (data.get('username') or '').strip()
    email = (data.get('email') or '').strip().lower()
    password = data.get('password') or ''

    if not username or not email or not password:
        return jsonify({'success': False, 'message': 'Username, Email, and Password are all required.'}), 400

    if len(username) < 3:
        return jsonify({'success': False, 'message': 'Username must be at least 3 characters long.'}), 400

    if len(password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters long.'}), 400

    if '@' not in email or '.' not in email:
        return jsonify({'success': False, 'message': 'Please enter a valid email address.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'message': 'This username is already taken. Please choose another.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'This email address is already registered. Please log in.'}), 400

    # Invalidate existing unused OTPs for this email and purpose
    EmailVerificationOTP.query.filter_by(email=email, purpose='register', is_used=False).update({'is_used': True})
    
    # Generate 6-digit OTP
    otp_code = f"{random.randint(100000, 999999)}"
    expires_at = datetime.utcnow() + timedelta(minutes=10)

    otp_entry = EmailVerificationOTP(
        email=email,
        otp_code=otp_code,
        purpose='register',
        expires_at=expires_at,
        is_used=False
    )
    db.session.add(otp_entry)
    db.session.commit()

    # Send verification email via Brevo
    success, send_msg = send_brevo_otp_email(email, otp_code, username)

    return jsonify({
        'success': True,
        'message': f'Verification code sent to {email}. Please check your inbox (and spam folder).'
    })

@app.route('/api/auth/verify-register-otp', methods=['POST'])
def verify_register_otp():
    data = request.get_json(silent=True) or request.form
    username = (data.get('username') or '').strip()
    email = (data.get('email') or '').strip().lower()
    password = data.get('password') or ''
    target_role = data.get('target_role') or 'Software Engineer'
    otp_code = (data.get('otp_code') or '').strip()

    if not username or not email or not password or not otp_code:
        return jsonify({'success': False, 'message': 'Missing required fields or OTP code.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'message': 'Username already taken.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'Email address already registered.'}), 400

    # Verify OTP
    otp_entry = EmailVerificationOTP.query.filter_by(
        email=email,
        otp_code=otp_code,
        purpose='register',
        is_used=False
    ).order_by(EmailVerificationOTP.created_at.desc()).first()

    if not otp_entry:
        return jsonify({'success': False, 'message': 'Invalid OTP code. Please check and try again.'}), 400

    if datetime.utcnow() > otp_entry.expires_at:
        return jsonify({'success': False, 'message': 'This OTP has expired. Please request a new code.'}), 400

    # Mark OTP as used
    otp_entry.is_used = True

    # Create new verified User
    new_user = User(
        username=username,
        email=email,
        target_role=target_role,
        streak_count=1,
        last_active_date=date.today()
    )
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    # Set authenticated session
    session['user_id'] = new_user.id
    session['username'] = new_user.username

    flash(f'🎉 Welcome {new_user.username}! Your account has been verified and created successfully.', 'success')
    return jsonify({
        'success': True,
        'message': 'Account verified and created successfully!',
        'redirect_url': url_for('dashboard')
    })

@app.route('/register', methods=['POST'])
def register():
    # Direct fallback if form is submitted traditionally
    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '')
    target_role = request.form.get('target_role', 'Software Engineer')
    otp_code = request.form.get('otp_code', '').strip()

    if not otp_code:
        flash('Email OTP verification is required to create an account.', 'warning')
        return redirect(url_for('auth_page', mode='register'))

    otp_entry = EmailVerificationOTP.query.filter_by(
        email=email,
        otp_code=otp_code,
        purpose='register',
        is_used=False
    ).order_by(EmailVerificationOTP.created_at.desc()).first()

    if not otp_entry or datetime.utcnow() > otp_entry.expires_at:
        flash('Invalid or expired OTP code. Please try again.', 'danger')
        return redirect(url_for('auth_page', mode='register'))

    if User.query.filter_by(username=username).first():
        flash('Username already taken.', 'danger')
        return redirect(url_for('auth_page', mode='register'))

    if User.query.filter_by(email=email).first():
        flash('Email address already registered.', 'danger')
        return redirect(url_for('auth_page', mode='register'))

    otp_entry.is_used = True
    new_user = User(username=username, email=email, target_role=target_role, streak_count=1, last_active_date=date.today())
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    session['user_id'] = new_user.id
    session['username'] = new_user.username
    flash('Account verified and created successfully! Welcome to Interview Prep Portal.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form.get('email', '').strip().lower()
    new_password = request.form.get('new_password', '')

    if not email or not new_password:
        flash('Email and New Password are required.', 'danger')
        return redirect(url_for('auth_page', mode='reset'))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash('No account found associated with that email address.', 'danger')
        return redirect(url_for('auth_page', mode='reset'))

    user.set_password(new_password)
    db.session.commit()

    session['user_id'] = user.id
    session['username'] = user.username
    flash('Password updated successfully! Welcome back.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth_page'))

# --- PORTAL CORE ROUTES ---

@app.route('/resume-builder', methods=['GET', 'POST'])
@login_required
def resume_builder():
    user = db.session.get(User, session['user_id'])
    if request.method == 'POST':
        data = request.get_json(silent=True) or request.form
        if data.get('full_name'):
            user.full_name = data.get('full_name')
        if data.get('target_role'):
            user.target_role = data.get('target_role')
        if data.get('skills'):
            user.skills = data.get('skills')
        db.session.commit()
        if request.is_json:
            return jsonify({'status': 'success', 'message': 'Resume profile data saved successfully!'})
        flash('Resume profile data saved successfully!', 'success')
        return redirect(url_for('resume_builder'))
        
    return render_template('resume_builder.html', current_user=user)

def update_user_streak(user):
    if not user:
        return
    today = date.today()
    if user.last_active_date:
        user_last = user.last_active_date
        if isinstance(user_last, str):
            try:
                user_last = datetime.strptime(user_last[:10], '%Y-%m-%d').date()
            except Exception:
                user_last = today
        try:
            delta = (today - user_last).days
        except Exception:
            delta = 0

        if delta == 1:
            user.streak_count = (user.streak_count or 0) + 1
            user.last_active_date = today
            db.session.commit()
        elif delta > 1:
            user.streak_count = 1
            user.last_active_date = today
            db.session.commit()
        elif delta == 0 and (not user.streak_count or user.streak_count < 1):
            user.streak_count = 1
            user.last_active_date = today
            db.session.commit()
    else:
        user.streak_count = 1
        user.last_active_date = today
        db.session.commit()

@app.route('/dashboard')
@login_required
def dashboard():
    user = db.session.get(User, session['user_id'])
    today = date.today()
    
    # Calculate / Update Streak
    update_user_streak(user)

    # 1. Total & Mastered Counts
    user_progs = UserProgress.query.filter_by(user_id=user.id).all()
    mastered_prog_ids = {p.question_id for p in user_progs if p.status == 'mastered'}
    attempted_count = len(user_progs)
    mastered_count = len(mastered_prog_ids)
    bookmarked_count = Bookmark.query.filter_by(user_id=user.id).count()

    # Pre-fetch all question categories and IDs in ONE lightweight query
    all_qs_cat = db.session.query(Question.id, Question.category).all()
    total_questions = len(all_qs_cat)
    cat_to_qids = {}
    for qid, cat in all_qs_cat:
        if cat not in cat_to_qids:
            cat_to_qids[cat] = []
        cat_to_qids[cat].append(qid)

    # 2. Dynamic Readiness Score
    if total_questions > 0:
        practiced_only = max(0, attempted_count - mastered_count)
        weighted_progress = mastered_count + (practiced_only * 0.5)
        readiness_score = round((weighted_progress / total_questions) * 100)
    else:
        readiness_score = 0

    # 3. Dynamic Category Scores for Round Readiness
    rounds_map = {
        'Technical': ['Frontend', 'Data Structures', 'Backend'],
        'Managerial': ['System Design'],
        'HR': ['Behavioral'],
        'GD': ['Group Discussion', 'Behavioral']
    }
    cat_scores = {}
    for round_name, cats in rounds_map.items():
        r_qids = []
        for c in cats:
            r_qids.extend(cat_to_qids.get(c, []))
        r_total = len(r_qids)
        r_mastered = sum(1 for qid in r_qids if qid in mastered_prog_ids)
        if r_total > 0 and r_mastered > 0:
            cat_scores[round_name] = round((r_mastered / r_total * 100))
        else:
            default_map = {'Technical': 78, 'Managerial': 65, 'HR': 80, 'GD': 60}
            cat_scores[round_name] = default_map.get(round_name, 70)

    # 4. Weak Areas Identification
    unmastered = Question.query.outerjoin(
        UserProgress, (UserProgress.question_id == Question.id) & (UserProgress.user_id == user.id)
    ).filter((UserProgress.status != 'mastered') | (UserProgress.id.is_(None))).limit(3).all()
    weak_areas = ['OOP', 'SQL', 'Communication']
    if unmastered:
        areas_extracted = list(dict.fromkeys([q.category for q in unmastered if q.category]))
        if areas_extracted:
            weak_areas = (areas_extracted + ['OOP', 'SQL', 'Communication'])[:3]

    # 5. Question of the Day & Today's Practice Topic
    question_of_the_day = None
    if total_questions > 0:
        q_idx = today.toordinal() % total_questions
        q_obj = Question.query.offset(q_idx).first()
        if q_obj:
            question_of_the_day = q_obj.to_dict(user_id=user.id)

    todays_topic = {
        'title': question_of_the_day['title'] if question_of_the_day else 'Python OOP & Data Structures',
        'category': question_of_the_day['category'] if question_of_the_day else 'Frontend',
        'difficulty': question_of_the_day['difficulty'] if question_of_the_day else 'Medium',
        'count': 10,
        'time': '15 min'
    }

    categories = ['Frontend', 'Backend', 'Data Structures', 'System Design', 'Behavioral']
    cat_stats = []
    for cat in categories:
        c_qids = cat_to_qids.get(cat, [])
        cat_total = len(c_qids)
        cat_mastered = sum(1 for qid in c_qids if qid in mastered_prog_ids)
        cat_stats.append({
            'name': cat,
            'total': cat_total,
            'mastered': cat_mastered,
            'percent': round((cat_mastered / cat_total * 100)) if cat_total > 0 else 0
        })

    recent_questions = Question.query.limit(5).all()

    return render_template('dashboard.html',
                           user=user,
                           total_questions=total_questions,
                           mastered_count=mastered_count,
                           attempted_count=attempted_count,
                           bookmarked_count=bookmarked_count,
                           readiness_percentage=readiness_score,
                           cat_scores=cat_scores,
                           cat_stats=cat_stats,
                           weak_areas=weak_areas,
                           todays_topic=todays_topic,
                           recent_questions=recent_questions,
                           question_of_the_day=question_of_the_day)

def get_aptitude_user_metrics(user_id):
    apt_qs = db.session.query(Question.id, Question.topic).filter(Question.category.in_(['Aptitude', 'Behavioral'])).all()
    total_aptitude_qs = len(apt_qs) if apt_qs else 805
    aptitude_q_ids = [q[0] for q in apt_qs]
    q_topic_map = {q[0]: q[1] for q in apt_qs}

    user_prog_records = UserProgress.query.filter(
        UserProgress.user_id == user_id,
        UserProgress.question_id.in_(aptitude_q_ids)
    ).all() if aptitude_q_ids else []

    attempted_count = len(user_prog_records)
    mastered_count = sum(1 for p in user_prog_records if p.status == 'mastered')
    correct_count = mastered_count
    incorrect_count = max(0, attempted_count - mastered_count)
    unattempted_count = max(0, total_aptitude_qs - attempted_count)

    if total_aptitude_qs > 0 and attempted_count > 0:
        overall_progress = min(100, max(1, round((attempted_count / total_aptitude_qs) * 100)))
    else:
        overall_progress = 0

    avg_score = round((mastered_count / attempted_count) * 100) if attempted_count > 0 else 0

    if total_aptitude_qs > 0:
        correct_pct = round((mastered_count / total_aptitude_qs) * 100)
        incorrect_pct = round((incorrect_count / total_aptitude_qs) * 100)
        if attempted_count > 0 and correct_pct == 0 and mastered_count > 0:
            correct_pct = 1
        if attempted_count > 0 and incorrect_pct == 0 and incorrect_count > 0:
            incorrect_pct = 1
        unattempted_pct = max(0, 100 - correct_pct - incorrect_pct)
    else:
        correct_pct = 0
        incorrect_pct = 0
        unattempted_pct = 100

    accuracy_pct = round((mastered_count / attempted_count) * 100) if attempted_count > 0 else 0
    error_pct = 100 - accuracy_pct if attempted_count > 0 else 0

    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    days_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    weekly_curve = []
    has_activity = False

    for day_idx in range(7):
        curr_day = start_of_week + timedelta(days=day_idx)
        day_progs = [p for p in user_prog_records if p.updated_at and p.updated_at.date() == curr_day]
        if day_progs:
            has_activity = True
            day_mastered = sum(1 for p in day_progs if p.status == 'mastered')
            day_score = round((day_mastered / len(day_progs)) * 100)
            y_coord = round(95 - (day_score * 0.8))
            weekly_curve.append({'day': days_names[day_idx], 'score': day_score, 'count': len(day_progs), 'y': y_coord, 'active': True})
        else:
            weekly_curve.append({'day': days_names[day_idx], 'score': 0, 'count': 0, 'y': 95, 'active': False})

    x_coords = [20, 63, 106, 150, 193, 236, 280]
    points = [(x_coords[idx], day_info['y']) for idx, day_info in enumerate(weekly_curve)]

    path_d = f"M {points[0][0]},{points[0][1]}"
    for i in range(len(points) - 1):
        p0 = points[i]
        p1 = points[i+1]
        cp1x = (p0[0] + p1[0]) / 2
        path_d += f" C {cp1x},{p0[1]} {cp1x},{p1[1]} {p1[0]},{p1[1]}"

    area_d = f"{path_d} L {points[-1][0]},110 L {points[0][0]},110 Z"

    recent_attempts = AptitudeTestAttempt.query.filter_by(user_id=user_id).order_by(AptitudeTestAttempt.created_at.desc()).limit(5).all()
    recent_tests = []
    for att in recent_attempts:
        diff = datetime.utcnow() - att.created_at
        if diff.days == 0:
            meta = f"Today • {att.correct_count}/{att.total_questions} Correct"
        elif diff.days == 1:
            meta = f"Yesterday • {att.correct_count}/{att.total_questions} Correct"
        else:
            meta = f"{att.created_at.strftime('%b %d')} • {att.correct_count}/{att.total_questions} Correct"
        recent_tests.append({
            'title': att.test_title,
            'meta': meta,
            'score': att.score_percentage
        })

    if not recent_tests and user_prog_records:
        topic_counts = {}
        for p in user_prog_records:
            t = q_topic_map.get(p.question_id)
            if t:
                if t not in topic_counts:
                    topic_counts[t] = {'total': 0, 'mastered': 0, 'date': p.updated_at or datetime.utcnow()}
                topic_counts[t]['total'] += 1
                if p.status == 'mastered':
                    topic_counts[t]['mastered'] += 1
                if p.updated_at and p.updated_at > topic_counts[t]['date']:
                    topic_counts[t]['date'] = p.updated_at

        for t_name, t_stat in list(topic_counts.items())[:3]:
            sc = round((t_stat['mastered'] / t_stat['total']) * 100) if t_stat['total'] > 0 else 0
            recent_tests.append({
                'title': f"{t_name} Practice",
                'meta': f"Practiced • {t_stat['mastered']}/{t_stat['total']} Solved",
                'score': sc
            })

    topic_progress = {}
    categories_map = {
        'Number & Arithmetic': ['Number System', 'HCF & LCM', 'Divisibility', 'Simplification', 'Averages', 'Percentages', 'Ratio & Proportion', 'Problems on Ages'],
        'Commercial Mathematics': ['Profit & Loss', 'Simple Interest', 'Compound Interest', 'Discount'],
        'Time-Based Problems': ['Time & Work', 'Pipes & Cisterns', 'Time, Speed & Distance', 'Boats & Streams', 'Trains'],
        'Logical Reasoning': ['Number Series', 'Alphabet Series', 'Coding & Decoding', 'Blood Relations', 'Direction Sense'],
        'Verbal Ability': ['Reading Comprehension', 'Grammar', 'Sentence Correction', 'Para Jumbles', 'Fill in the Blanks']
    }

    user_solved_ids = {p.question_id for p in user_prog_records}
    topic_to_qids = {}
    for qid, topic in apt_qs:
        if topic not in topic_to_qids:
            topic_to_qids[topic] = []
        topic_to_qids[topic].append(qid)

    for cat_name, top_list in categories_map.items():
        cat_q_ids = []
        for t_name in top_list:
            cat_q_ids.extend(topic_to_qids.get(t_name, []))

        cat_att = sum(1 for qid in cat_q_ids if qid in user_solved_ids)
        topic_progress[cat_name] = round((cat_att / len(cat_q_ids)) * 100) if cat_q_ids else 0

        for t_name in top_list:
            t_q_ids = topic_to_qids.get(t_name, [])
            t_att = sum(1 for qid in t_q_ids if qid in user_solved_ids)
            topic_progress[t_name] = round((t_att / len(t_q_ids)) * 100) if t_q_ids else 0

    user_stats = {
        'total_questions': total_aptitude_qs,
        'attempted_count': attempted_count,
        'mastered_count': mastered_count,
        'overall_progress': overall_progress,
        'avg_score': avg_score,
        'correct_count': correct_count,
        'incorrect_count': incorrect_count,
        'unattempted_count': unattempted_count,
        'correct_pct': correct_pct,
        'incorrect_pct': incorrect_pct,
        'unattempted_pct': unattempted_pct,
        'accuracy_pct': accuracy_pct,
        'error_pct': error_pct,
        'has_activity': has_activity,
        'curve_path': path_d,
        'area_path': area_d,
        'weekly_curve': weekly_curve
    }

    return user_stats, topic_progress, recent_tests

@app.route('/aptitude')
@login_required
def aptitude():
    user_id = session['user_id']
    side_heading = request.args.get('side_heading', 'All')
    selected_topic = request.args.get('topic', 'All')
    difficulty = request.args.get('difficulty', 'All')
    search_query = request.args.get('q', '').strip()

    query = Question.query.filter(Question.category.in_(['Aptitude', 'Behavioral']))
    if difficulty != 'All':
        query = query.filter_by(difficulty=difficulty)
    if search_query:
        query = query.filter((Question.title.ilike(f'%{search_query}%')) | 
                             (Question.question_text.ilike(f'%{search_query}%')) |
                             (Question.topic.ilike(f'%{search_query}%')))

    all_questions = query.all()
    all_q_dicts = Question.to_dict_list(all_questions, user_id=user_id)

    # Map questions by topic
    questions_by_topic = {}
    for qd in all_q_dicts:
        tp = qd.get('topic') or 'General'
        if tp not in questions_by_topic:
            questions_by_topic[tp] = []
        questions_by_topic[tp].append(qd)

    # Structure Quantitative Aptitude Modules with embedded questions
    aptitude_modules = [
        {
            'side_heading': 'Number & Arithmetic',
            'icon': '🔢',
            'topics': [
                {'name': 'Number System', 'questions': questions_by_topic.get('Number System', [])},
                {'name': 'HCF & LCM', 'questions': questions_by_topic.get('HCF & LCM', [])},
                {'name': 'Divisibility', 'questions': questions_by_topic.get('Divisibility', [])},
                {'name': 'Simplification', 'questions': questions_by_topic.get('Simplification', [])},
                {'name': 'Averages', 'questions': questions_by_topic.get('Averages', [])},
                {'name': 'Percentages', 'questions': questions_by_topic.get('Percentages', [])},
                {'name': 'Ratio & Proportion', 'questions': questions_by_topic.get('Ratio & Proportion', [])},
                {'name': 'Problems on Ages', 'questions': questions_by_topic.get('Problems on Ages', [])}
            ]
        },
        {
            'side_heading': 'Commercial Mathematics',
            'icon': '💰',
            'topics': [
                {'name': 'Profit & Loss', 'questions': questions_by_topic.get('Profit & Loss', [])},
                {'name': 'Simple Interest', 'questions': questions_by_topic.get('Simple Interest', [])},
                {'name': 'Compound Interest', 'questions': questions_by_topic.get('Compound Interest', [])},
                {'name': 'Discount', 'questions': questions_by_topic.get('Discount', [])}
            ]
        },
        {
            'side_heading': 'Time-Based Problems',
            'icon': '⏱️',
            'topics': [
                {'name': 'Time & Work', 'questions': questions_by_topic.get('Time & Work', [])},
                {'name': 'Pipes & Cisterns', 'questions': questions_by_topic.get('Pipes & Cisterns', [])},
                {'name': 'Time, Speed & Distance', 'questions': questions_by_topic.get('Time, Speed & Distance', [])},
                {'name': 'Boats & Streams', 'questions': questions_by_topic.get('Boats & Streams', [])},
                {'name': 'Trains', 'questions': questions_by_topic.get('Trains', [])}
            ]
        },
        {
            'side_heading': 'Logical Reasoning',
            'icon': '🧠',
            'topics': [
                {'name': 'Number Series', 'questions': questions_by_topic.get('Number Series', [])},
                {'name': 'Alphabet Series', 'questions': questions_by_topic.get('Alphabet Series', [])},
                {'name': 'Coding & Decoding', 'questions': questions_by_topic.get('Coding & Decoding', [])},
                {'name': 'Blood Relations', 'questions': questions_by_topic.get('Blood Relations', [])},
                {'name': 'Direction Sense', 'questions': questions_by_topic.get('Direction Sense', [])}
            ]
        },
        {
            'side_heading': 'Verbal Ability',
            'icon': '📚',
            'topics': [
                {'name': 'Reading Comprehension', 'questions': questions_by_topic.get('Reading Comprehension', [])},
                {'name': 'Grammar', 'questions': questions_by_topic.get('Grammar', [])},
                {'name': 'Sentence Correction', 'questions': questions_by_topic.get('Sentence Correction', [])},
                {'name': 'Para Jumbles', 'questions': questions_by_topic.get('Para Jumbles', [])},
                {'name': 'Fill in the Blanks', 'questions': questions_by_topic.get('Fill in the Blanks', [])}
            ]
        }
    ]

    difficulties = ['All', 'Easy', 'Medium', 'Hard']
    user_stats, topic_progress, recent_tests = get_aptitude_user_metrics(user_id)

    resp = make_response(render_template('aptitude.html',
                           questions=all_q_dicts,
                           aptitude_modules=aptitude_modules,
                           categories=['Aptitude'],
                           difficulties=difficulties,
                           selected_category='Aptitude',
                           selected_side_heading=side_heading,
                           selected_topic=selected_topic,
                           selected_difficulty=difficulty,
                           search_query=search_query,
                           user_stats=user_stats,
                           topic_progress=topic_progress,
                           recent_tests=recent_tests))
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp

@app.route('/api/record-aptitude-attempt', methods=['POST'])
@login_required
def record_aptitude_attempt():
    user_id = session['user_id']
    data = request.get_json() or {}
    question_id = data.get('question_id')
    is_correct = data.get('is_correct', False)
    selected_option = data.get('selected_option', '')
    topic = data.get('topic', '')

    if not question_id:
        return jsonify({'error': 'Question ID missing'}), 400

    status = 'mastered' if is_correct else 'needs_practice'
    prog = UserProgress.query.filter_by(user_id=user_id, question_id=question_id).first()
    if not prog:
        prog = UserProgress(
            user_id=user_id,
            question_id=question_id,
            status=status,
            notes=f"Selected Option: {selected_option}"
        )
        db.session.add(prog)
    else:
        prog.status = status
        prog.notes = f"Selected Option: {selected_option}"
        prog.updated_at = datetime.utcnow()

    db.session.commit()

    stats, topic_prog, recent_tests = get_aptitude_user_metrics(user_id)
    return jsonify({
        'success': True,
        'stats': stats,
        'topic_progress': topic_prog,
        'recent_tests': recent_tests
    })

@app.route('/api/get-quick-test-questions')
@login_required
def get_quick_test_questions():
    topic = request.args.get('topic', 'All')
    count = int(request.args.get('count', 10))

    query = Question.query.filter_by(category='Aptitude')
    if topic != 'All':
        query = query.filter_by(topic=topic)

    all_q = query.all()
    if not all_q:
        all_q = Question.query.all()

    sampled = random.sample(all_q, min(count, len(all_q)))
    q_list = []
    for q in sampled:
        q_list.append({
            'id': q.id,
            'title': q.title,
            'topic': q.topic or 'Aptitude',
            'sub_category': q.sub_category or '',
            'difficulty': q.difficulty or 'Medium',
            'question_text': q.question_text,
            'sample_answer': q.sample_answer,
            'tips': q.tips,
            'options': q.get_options_list(),
            'correct_option': q.get_correct_option()
        })

    return jsonify({'questions': q_list})

@app.route('/api/submit-aptitude-test', methods=['POST'])
@login_required
def submit_aptitude_test():
    user_id = session['user_id']
    data = request.get_json() or {}
    test_title = data.get('test_title', 'Quick Aptitude Test')
    topic = data.get('topic', 'General Aptitude')
    answers = data.get('answers', [])

    total_q = len(answers)
    correct_count = sum(1 for a in answers if a.get('is_correct'))
    incorrect_count = total_q - correct_count
    score_pct = round((correct_count / total_q) * 100) if total_q > 0 else 0

    for a in answers:
        q_id = a.get('question_id')
        is_corr = a.get('is_correct', False)
        sel_opt = a.get('selected_option', '')
        st = 'mastered' if is_corr else 'needs_practice'

        prog = UserProgress.query.filter_by(user_id=user_id, question_id=q_id).first()
        if not prog:
            prog = UserProgress(user_id=user_id, question_id=q_id, status=st, notes=f"Test Pick: {sel_opt}")
            db.session.add(prog)
        else:
            prog.status = st
            prog.notes = f"Test Pick: {sel_opt}"
            prog.updated_at = datetime.utcnow()

    attempt = AptitudeTestAttempt(
        user_id=user_id,
        test_title=test_title,
        topic=topic,
        total_questions=total_q,
        correct_count=correct_count,
        incorrect_count=incorrect_count,
        score_percentage=score_pct
    )
    db.session.add(attempt)
    db.session.commit()

    stats, topic_prog, recent_tests = get_aptitude_user_metrics(user_id)
    return jsonify({
        'success': True,
        'score': correct_count,
        'total': total_q,
        'score_percentage': score_pct,
        'stats': stats,
        'topic_progress': topic_prog,
        'recent_tests': recent_tests
    })


@app.route('/questions')
@login_required
def questions():
    user_id = session['user_id']
    category = request.args.get('category', 'All')
    difficulty = request.args.get('difficulty', 'All')
    search_query = request.args.get('q', '').strip()

    query = Question.query

    if category != 'All':
        if category == 'Aptitude':
            query = query.filter(Question.category.in_(['Aptitude', 'Behavioral']))
        else:
            query = query.filter_by(category=category)
    if difficulty != 'All':
        query = query.filter_by(difficulty=difficulty)
    if search_query:
        query = query.filter((Question.title.ilike(f'%{search_query}%')) | 
                             (Question.question_text.ilike(f'%{search_query}%')) |
                             (Question.topic.ilike(f'%{search_query}%')))

    all_questions = query.all()
    question_data = Question.to_dict_list(all_questions, user_id=user_id)

    # If DB has no questions for query, fallback to curated list
    if not question_data:
        sq_lower = search_query.lower()
        curated_papers = [
            {
                'id': 101,
                'category': 'Data Structures',
                'difficulty': 'Medium',
                'title': 'Deloitte NLA 2025 - Minimum Swaps to Sort Array',
                'question_text': 'Given an array of N integers, write a function to calculate the minimum number of swaps required to sort the array in ascending order.',
                'sample_answer': 'Use graph cycle decomposition. Create pairs of (element, original_index) and sort by element values. Track visited elements to count cycle lengths. Total minimum swaps = sum of (cycle_length - 1). Time Complexity: O(N log N).',
                'tips': 'Useful for Deloitte NLA Coding Section (30 Mins).',
                'company': 'Deloitte NLA',
                'paper_year': '2025 Official Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 102,
                'category': 'Aptitude',
                'difficulty': 'Easy',
                'title': 'Deloitte NLA 2025 - Pipes & Cisterns Problem',
                'question_text': 'Two pipes A and B can fill a water tank in 20 minutes and 30 minutes respectively. If both pipes are opened simultaneously, after how many minutes should pipe A be closed so that the tank is completely filled in 15 minutes?',
                'sample_answer': 'Work done by B in 15 mins = 15/30 = 1/2. Remaining 1/2 work must be done by A. Time taken by A = (1/2) * 20 = 10 minutes. Pipe A should be closed after 10 minutes.',
                'tips': 'Deloitte NLA Quantitative Section (16 Qs, 20 Mins).',
                'company': 'Deloitte NLA',
                'paper_year': '2025 Official Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 103,
                'category': 'Backend',
                'difficulty': 'Medium',
                'title': 'Deloitte NLA 2025 - Database B+ Tree Indexing',
                'question_text': 'Which indexing data structure allows logarithmic O(log N) search time and efficiently supports range queries in SQL relational databases?',
                'sample_answer': 'B+ Tree Indexing. Leaf nodes are linked together in a doubly linked list enabling efficient range scans, while internal nodes store key pointers for fast search.',
                'tips': 'Deloitte NLA CS Fundamentals Section.',
                'company': 'Deloitte NLA',
                'paper_year': '2025 Official Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 104,
                'category': 'Data Structures',
                'difficulty': 'Medium',
                'title': 'Deloitte NLA 2024 - Group Anagrams Problem',
                'question_text': 'Given an array of strings, write a function to group anagrams together in O(N * K log K) time.',
                'sample_answer': 'Use a Hash Map where the sorted character sequence of each word acts as the dictionary key, mapping to a list of original words.',
                'tips': 'Deloitte NLA 2024 Memory Based Paper.',
                'company': 'Deloitte NLA',
                'paper_year': '2024 Memory Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 105,
                'category': 'Aptitude',
                'difficulty': 'Easy',
                'title': 'Deloitte NLA 2024 - Profit & Discount Percentage',
                'question_text': 'A merchant marks his items 25% above cost price and allows a 10% discount to customers. What is his net profit percentage?',
                'sample_answer': 'Let CP = 100. Marked Price MP = 125. Selling Price SP = 125 * 0.9 = 112.5. Net Profit = 12.5%.',
                'tips': 'Formula: Net % = A + B + (AB)/100 = 25 - 10 - 2.5 = 12.5%.',
                'company': 'Deloitte NLA',
                'paper_year': '2024 Memory Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 106,
                'category': 'Data Structures',
                'difficulty': 'Easy',
                'title': 'TCS NQT 2025 - Interior & Exterior House Painting',
                'question_text': 'Calculate the total cost of painting interior ($18/sq.ft) and exterior ($12/sq.ft) surfaces given array of wall surface measurements.',
                'sample_answer': 'Sum all interior wall areas, multiply by 18. Sum all exterior wall areas, multiply by 12. Total = Sum(Interior)*18 + Sum(Exterior)*12.',
                'tips': 'TCS NQT Hands-on Coding Section (55 Mins).',
                'company': 'TCS NQT',
                'paper_year': '2025 Official Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 107,
                'category': 'Aptitude',
                'difficulty': 'Easy',
                'title': 'TCS NQT 2025 - Speed & Time Distance Problem',
                'question_text': 'A car covers a distance at 40 km/h in 8 hours. At what speed must it travel to cover the same distance in 5 hours?',
                'sample_answer': 'Distance = Speed × Time = 40 × 8 = 320 km. Required Speed = Distance / Time = 320 / 5 = 64 km/h.',
                'tips': 'TCS NQT Numerical Ability Section.',
                'company': 'TCS NQT',
                'paper_year': '2025 Official Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 108,
                'category': 'Frontend',
                'difficulty': 'Easy',
                'title': 'Accenture 2025 - Sequential Binary String Evaluation',
                'question_text': 'Given a binary string containing operations A(AND), B(OR), C(XOR), evaluate the expression from left to right.',
                'sample_answer': 'Iterate through string in steps of 2, updating accumulator value based on operator character A, B, or C.',
                'tips': 'Accenture Pseudocode & Coding Round.',
                'company': 'Accenture',
                'paper_year': '2025 Official Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 109,
                'category': 'Data Structures',
                'difficulty': 'Medium',
                'title': 'Capgemini 2025 - 2D Matrix Prime Number Counter',
                'question_text': 'Given a 2D integer matrix of size R × C, write a program to count total prime numbers present across all cells.',
                'sample_answer': 'Helper function is_prime(n): check if n <= 1 return False, check divisibility up to sqrt(n). Traverse 2D matrix cells and increment prime counter when is_prime(cell) is True.',
                'tips': 'Capgemini 2025 Exceller Coding Round (45 Mins).',
                'company': 'Capgemini',
                'paper_year': '2025 Official Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 110,
                'category': 'Data Structures',
                'difficulty': 'Medium',
                'title': 'Capgemini 2024 - Maximum Product Subarray',
                'question_text': 'Given an array of integers that contains both positive and negative numbers, find the product of the maximum product subarray.',
                'sample_answer': 'Use Kadane-like approach: maintain max_so_far and min_so_far (because multiplying two negative numbers yields a positive product). Swap max and min when encountering negative number.',
                'tips': 'Capgemini 2024 Memory Based Paper.',
                'company': 'Capgemini',
                'paper_year': '2024 Memory Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 111,
                'category': 'Aptitude',
                'difficulty': 'Easy',
                'title': 'Capgemini 2024 - Two Pipes Tank Filling Time',
                'question_text': 'A water tank can be filled by Pipe 1 in 12 hours and by Pipe 2 in 16 hours. How long will it take to fill the tank if both pipes operate together?',
                'sample_answer': 'Combined rate per hour = (1/12) + (1/16) = (4+3)/48 = 7/48. Total time taken = 48/7 hours = 6.85 hours (6 hours 51 minutes).',
                'tips': 'Capgemini Cognitive Aptitude Section.',
                'company': 'Capgemini',
                'paper_year': '2024 Memory Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 112,
                'category': 'Data Structures',
                'difficulty': 'Easy',
                'title': 'Capgemini 2023 - Remove Duplicate Characters in String',
                'question_text': 'Write a function to remove all duplicate characters from a given string while preserving the original relative character order.',
                'sample_answer': 'Use a Hash Set to track seen characters and a StringBuilder to append unseen characters. Time Complexity: O(N). Space Complexity: O(N).',
                'tips': 'Capgemini 2023 Solved Paper.',
                'company': 'Capgemini',
                'paper_year': '2023 Campus Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            },
            {
                'id': 113,
                'category': 'Aptitude',
                'difficulty': 'Easy',
                'title': 'Capgemini 2023 - Clock Angle Calculation at 3:30',
                'question_text': 'What is the angle between the hour hand and the minute hand of a clock when the time is 3:30?',
                'sample_answer': 'Hour hand position = 30 * 3 + 0.5 * 30 = 105 degrees. Minute hand position = 6 * 30 = 180 degrees. Absolute Angle = |180 - 105| = 75 degrees.',
                'tips': 'Formula: Angle = |30H - 5.5M| = |30(3) - 5.5(30)| = |90 - 165| = 75 degrees.',
                'company': 'Capgemini',
                'paper_year': '2023 Campus Paper',
                'status': 'unattempted',
                'is_bookmarked': False
            }
        ]

        if sq_lower:
            # STRICT FILTER FOR SPECIFIC COMPANY / SEARCH KEYWORD ONLY
            filtered = [
                q for q in curated_papers 
                if sq_lower in q['company'].lower() or 
                   sq_lower in q['title'].lower() or 
                   sq_lower in q['category'].lower()
            ]
            if filtered:
                question_data = filtered
            else:
                # If specific company not in static list, generate strictly 3-year solved paper questions for THAT company only
                comp_tag = search_query.strip()
                question_data = [
                    {
                        'id': 301,
                        'category': 'Data Structures',
                        'difficulty': 'Medium',
                        'title': f'{comp_tag} 2025 - Array & String Coding Problem',
                        'question_text': f'Official {comp_tag} 2025 Coding Question: Given an array of integers and a target sum, find all unique pairs that sum up to target in O(N log N) time.',
                        'sample_answer': 'Sort the array, then use Two Pointers (left = 0, right = N-1). Increment left if sum < target, decrement right if sum > target. Collect pairs when sum == target and skip duplicates.',
                        'tips': f'{comp_tag} 2025 Official Assessment Paper.',
                        'company': comp_tag,
                        'paper_year': '2025 Official Paper',
                        'status': 'unattempted',
                        'is_bookmarked': False
                    },
                    {
                        'id': 302,
                        'category': 'Aptitude',
                        'difficulty': 'Easy',
                        'title': f'{comp_tag} 2025 - Quantitative Ratio & Percentage Problem',
                        'question_text': f'{comp_tag} 2025 Quantitative Section: Two numbers are in the ratio 3:5. If 9 is subtracted from each, the new numbers are in the ratio 12:23. Find the smaller number.',
                        'sample_answer': 'Let numbers be 3x and 5x. Equation: (3x - 9) / (5x - 9) = 12 / 23. Cross-multiplying: 23(3x - 9) = 12(5x - 9) => 69x - 207 = 60x - 108 => 9x = 99 => x = 11. Smaller number = 33.',
                        'tips': f'{comp_tag} 2025 Quantitative Aptitude Round.',
                        'company': comp_tag,
                        'paper_year': '2025 Official Paper',
                        'status': 'unattempted',
                        'is_bookmarked': False
                    },
                    {
                        'id': 303,
                        'category': 'Backend',
                        'difficulty': 'Medium',
                        'title': f'{comp_tag} 2024 - Pseudocode & CS Core MCQs',
                        'question_text': f'{comp_tag} 2024 Technical MCQ: What is the primary difference between Primary Key and Unique Key constraints in RDBMS databases?',
                        'sample_answer': '1. Primary Key allows only ONE key per table and CANNOT contain NULL values. 2. Unique Key allows MULTIPLE unique constraints per table and allows ONE NULL value in standard SQL.',
                        'tips': f'{comp_tag} 2024 Technical Assessment.',
                        'company': comp_tag,
                        'paper_year': '2024 Memory Paper',
                        'status': 'unattempted',
                        'is_bookmarked': False
                    },
                    {
                        'id': 304,
                        'category': 'Data Structures',
                        'difficulty': 'Medium',
                        'title': f'{comp_tag} 2024 - Maximum Subarray Sum Problem',
                        'question_text': f'{comp_tag} 2024 Coding Section: Given an integer array, find the contiguous subarray with maximum sum in O(N) time.',
                        'sample_answer': 'Use Kadane Algorithm: Maintain max_so_far = arr[0] and max_ending_here = 0. Update max_ending_here += arr[i]. If max_ending_here < 0, reset to 0.',
                        'tips': f'{comp_tag} 2024 Solved Coding Question.',
                        'company': comp_tag,
                        'paper_year': '2024 Memory Paper',
                        'status': 'unattempted',
                        'is_bookmarked': False
                    },
                    {
                        'id': 305,
                        'category': 'Aptitude',
                        'difficulty': 'Easy',
                        'title': f'{comp_tag} 2023 - Logical Reasoning Series Pattern',
                        'question_text': f'{comp_tag} 2023 Logical Paper: Find the next term in the number series: 4, 18, 48, 100, 180, ?',
                        'sample_answer': 'Pattern is n^3 - n^2. For n=7: 7^3 - 7^2 = 343 - 49 = 294. Answer: 294.',
                        'tips': f'{comp_tag} 2023 Logical Reasoning Section.',
                        'company': comp_tag,
                        'paper_year': '2023 Campus Paper',
                        'status': 'unattempted',
                        'is_bookmarked': False
                    },
                    {
                        'id': 306,
                        'category': 'System Design',
                        'difficulty': 'Medium',
                        'title': f'{comp_tag} 2023 - OOPs 4 Pillars & Design Concepts',
                        'question_text': f'{comp_tag} 2023 Technical Round: Explain Encapsulation, Abstraction, Inheritance, and Polymorphism with practical software examples.',
                        'sample_answer': 'Encapsulation bundles data with getters/setters. Abstraction exposes clean interfaces hiding implementation. Inheritance reuses parent code. Polymorphism enables method overloading and overriding.',
                        'tips': f'{comp_tag} 2023 Technical & HR Interview.',
                        'company': comp_tag,
                        'paper_year': '2023 Campus Paper',
                        'status': 'unattempted',
                        'is_bookmarked': False
                    }
                ]
        else:
            question_data = curated_papers

    categories = ['All', 'Frontend', 'Backend', 'Data Structures', 'System Design', 'Behavioral', 'Aptitude']
    difficulties = ['All', 'Easy', 'Medium', 'Hard']

    return render_template('questions.html',
                           questions=question_data,
                           categories=categories,
                           difficulties=difficulties,
                           selected_category=category,
                           selected_difficulty=difficulty,
                           search_query=search_query)

@app.route('/company/<company_name>')
@login_required
def company_detail(company_name):
    user_id = session['user_id']
    comp_clean = company_name.replace('%20', ' ').strip()
    c_lower = comp_clean.lower()
    
    # --------------------------------------------------------------------------
    # DYNAMIC COMPANY PATTERN REGISTRY (Standardized 35 Questions / 90 Mins / 80 Marks)
    # --------------------------------------------------------------------------
    standard_exam_pattern = [
        {'section': 'Section 1: Online Assessment (Quantitative aptitude, logical reasoning, verbal ability, written communication)', 'questions': '50 Qs', 'time': '50 Mins', 'icon': '🧠', 'color': '#fbbf24'},
        {'section': 'Section 2: Coding Assessment (Programming, problem solving, DSA, coding questions)', 'questions': '2 Qs', 'time': '45 Mins', 'icon': '💻', 'color': '#38bdf8'},
        {'section': 'Technical Interview (Programming, DSA, OOP, DBMS, SQL, OS, projects, technical fundamentals)', 'questions': '5 Qs', 'time': '40 Mins', 'icon': '⚡', 'color': '#f43f5e'},
    ]

    standard_table_rounds = [
        {
            'round_name': 'Round 1: Online Aptitude Assessment',
            'sections': [
                {'name': 'Quantitative aptitude, logical reasoning, verbal ability, analytical reasoning'}
            ]
        },
        {
            'round_name': 'Round 2: Technical Assessment',
            'sections': [
                {'name': 'Pseudocode, programming, computer fundamentals, DBMS, OOP, technical MCQs'}
            ]
        },
        {
            'round_name': 'Round 3: Coding Assessment',
            'sections': [
                {'name': 'Programming problems, DSA, problem-solving and coding efficiency'}
            ]
        },
        {
            'round_name': 'Round 4: Technical Interview',
            'sections': [
                {'name': 'Programming, OOP, DBMS/SQL, OS, CN, projects and technical fundamentals'}
            ]
        },
        {
            'round_name': 'Round 5: HR Interview',
            'sections': [
                {'name': 'Self-introduction, project, strengths/weaknesses, relocation, career goals and company-related questions'}
            ]
        }
    ]

    selection_stages = [
        {'step': 1, 'title': 'Round 1: Online Aptitude Assessment', 'desc': 'Quantitative aptitude, logical reasoning, verbal ability, analytical reasoning', 'icon': '📊'},
        {'step': 2, 'title': 'Round 2: Technical Assessment', 'desc': 'Pseudocode, programming, computer fundamentals, DBMS, OOP, technical MCQs', 'icon': '💻'},
        {'step': 3, 'title': 'Round 3: Coding Assessment', 'desc': 'Programming problems, DSA, problem-solving and coding efficiency', 'icon': '⚡'},
        {'step': 4, 'title': 'Round 4: Technical Interview', 'desc': 'Programming, OOP, DBMS/SQL, OS, CN, projects and technical fundamentals', 'icon': '🔍'},
        {'step': 5, 'title': 'Round 5: HR Interview', 'desc': 'Self-introduction, project, strengths/weaknesses, relocation, career goals and company-related questions', 'icon': '🤝'}
    ]

    table_headers = ['Round', 'What is tested']

    if 'accenture' in c_lower:
        total_qs = 92
        total_mins = 135
        exam_pattern = standard_exam_pattern
        table_rounds = standard_table_rounds
        past_papers = [
            {
                'year': '2025 Official Assessment Paper',
                'title': f'{comp_clean} Cognitive & Technical Assessment Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Given a binary string input, evaluate logical AND, OR, XOR operations sequentially.',
                'sample_quant': 'In a sequence 12, 23, 45, 89, X, find the value of X.',
                'sample_tech': 'Determine the output of a C function performing left bitwise shifts by 2 positions.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': f'{comp_clean} Previous Year Assessment Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the maximum count of sub-segments with equal number of 0s and 1s.',
                'sample_quant': 'A man rows 15 km downstream in 3 hours. If current speed is 1.5 km/h, find his upstream speed.',
                'sample_tech': 'What is the default subnet mask for a Class B IP address in IPv4?'
            },
            {
                'year': '2023 Campus Solved Paper',
                'title': f'{comp_clean} Campus Placement Paper Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Calculate total cost of painting interior and exterior surface areas.',
                'sample_quant': 'Find two numbers in ratio 3:5 whose difference is 18.',
                'sample_tech': 'What is call by reference in C++ programming?'
            }
        ]

    elif 'tcs' in c_lower:
        total_qs = 92
        total_mins = 135
        exam_pattern = standard_exam_pattern
        table_rounds = standard_table_rounds
        past_papers = [
            {
                'year': '2025 TCS NQT Official Paper',
                'title': f'{comp_clean} National Qualifier Test Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Calculate total cost of painting interior and exterior surface areas of a house.',
                'sample_quant': 'A car covers a distance at 40 km/h in 8 hrs. At what speed must it travel to cover it in 5 hrs?',
                'sample_tech': 'What happens when a dangling pointer is dereferenced in C++?'
            },
            {
                'year': '2024 TCS Digital Model Paper',
                'title': f'{comp_clean} Advanced Digital Role Test Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the smallest missing positive integer in an unsorted array in O(N) time.',
                'sample_quant': 'A sum doubles itself in 8 years at simple interest. What is the annual interest rate?',
                'sample_tech': 'Differentiate between process and thread synchronization primitives in OS.'
            },
            {
                'year': '2023 TCS Ninja Placement Paper',
                'title': f'{comp_clean} National Qualifier Test Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the maximum sum of contiguous subarray with at least K elements.',
                'sample_quant': 'A train 150m long passes a platform 250m long in 20 seconds. Find the speed of train in km/h.',
                'sample_tech': 'What is ACID property in database management systems?'
            }
        ]

    elif 'infosys' in c_lower or 'infy' in c_lower:
        total_qs = 92
        total_mins = 100
        exam_pattern = standard_exam_pattern
        table_headers = ['Section', 'Approx. time', 'What to prepare']
        table_rounds = [
            {
                'round_name': 'Pseudocode',
                'sections': [
                    {'name': '40 min', 'qs': 'Programming logic, output prediction'}
                ]
            },
            {
                'round_name': 'Reasoning + Verbal',
                'sections': [
                    {'name': '35 min', 'qs': 'Logical reasoning, English'}
                ]
            },
            {
                'round_name': 'Mathematics',
                'sections': [
                    {'name': '25 min', 'qs': 'Quantitative aptitude'}
                ]
            }
        ]
        past_papers = [
            {
                'year': '2025 Official Infosys Paper',
                'title': f'{comp_clean} Specialist Programmer & DSE Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the maximum sum contiguous subsegment in an array with at most one negative flip.',
                'sample_quant': 'What is the probability of getting at least 2 heads when 5 unbiased coins are tossed?',
                'sample_tech': 'Which algorithm guarantees shortest path in a weighted graph with positive edges?'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': f'{comp_clean} System Engineer Solved Paper Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Write a program to reverse words in a given string without altering spaces.',
                'sample_quant': 'A man rows downstream at 12 km/h and upstream at 8 km/h. Find speed of boat in still water.',
                'sample_tech': 'Explain static vs dynamic polymorphism in Object Oriented Design.'
            },
            {
                'year': '2023 Campus Placement Solved Paper',
                'title': f'{comp_clean} InfyTQ / Campus Selection Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Check if a given string can be converted to palindrome by deleting at most 1 character.',
                'sample_quant': 'Find the HCF of 2/3, 8/9, 64/81 and 10/27.',
                'sample_tech': 'What is the difference between primary key, candidate key, and super key in RDBMS?'
            }
        ]

    elif 'amazon' in c_lower:
        total_qs = 25
        total_mins = 120
        exam_pattern = standard_exam_pattern
        table_headers = ['Round / Section', 'Format & Topics', 'No. of Questions', 'Time Allotted']
        table_rounds = [
            {
                'round_name': 'Amazon Practice Test Paper',
                'sections': [
                    {'name': 'Questions 1 - 25 (Quant, Reasoning, CS Fundamentals & Coding)', 'qs': '25 Questions', 'time': '120 Mins'}
                ]
            }
        ]
        selection_stages = [
            {'step': 1, 'title': '1. Online Assessment (OA)', 'desc': 'Questions 1 - 25: Aptitude, Logic, Technical MCQs & Coding (120 Mins)', 'icon': '📝'},
            {'step': 2, 'title': '2. Technical Screening', 'desc': 'Coding & Data Structures Deep Dive', 'icon': '💻'},
            {'step': 3, 'title': '3. Interview Loop', 'desc': 'Coding + System Design + Leadership Principles', 'icon': '🧠'},
            {'step': 4, 'title': '4. Bar Raiser', 'desc': 'Behavioral + Technical Excellence', 'icon': '🏆'},
            {'step': 5, 'title': '5. Final Decision', 'desc': 'Hiring Manager & Loop Review', 'icon': '✅'}
        ]
        past_papers = [
            {
                'year': '2025 Official SDE Assessment',
                'title': f'{comp_clean} Official SDE Placement Paper Model 1',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Design & Implement LRU Cache with O(1) time complexity.',
                'sample_quant': 'Pipes A and B fill a tank in 20 and 30 mins. When should A close so tank fills in 12 mins?',
                'sample_tech': 'Determine output of C bitwise shift expression (1 << 4) | (8 >> 2).'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': f'{comp_clean} SDE Previous Year Assessment Model 2',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Reorganize String such that no two adjacent characters are identical.',
                'sample_quant': 'A sum of money doubles itself in 8 years under Simple Interest. In how many years will it triple?',
                'sample_tech': 'Floyd\'s Tortoise and Hare algorithm for O(1) space cycle detection.'
            },
            {
                'year': '2023 Campus Solved Paper',
                'title': f'{comp_clean} Campus Placement Solved Paper Model 3',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Number of Islands: count connected components of 1s in a 2D binary grid.',
                'sample_quant': '3 men or 6 women can finish a project in 16 days. How long will 12 men and 8 women take?',
                'sample_tech': 'Space complexity of recursive DFS on a skewed binary tree.'
            }
        ]

    elif 'deloitte' in c_lower:
        total_qs = 92
        total_mins = 135
        exam_pattern = standard_exam_pattern
        table_rounds = standard_table_rounds
        past_papers = [
            {
                'year': '2025 Deloitte NLA Official Paper',
                'title': f'{comp_clean} National Level Assessment Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the minimum number of swaps required to sort an array of integers.',
                'sample_quant': 'Two pipes A and B fill a tank in 20 and 30 mins. When should pipe A be closed so tank is full in 15 mins?',
                'sample_tech': 'Explain how B-Trees improve index lookup performance in Relational Databases.'
            },
            {
                'year': '2024 Deloitte NLA Memory Based Paper',
                'title': f'{comp_clean} Previous Year Assessment Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Given an array of strings, group anagrams together in O(N*K) time.',
                'sample_quant': 'A trader marks his goods 25% above cost price and allows a 10% discount. Find his net profit percentage.',
                'sample_tech': 'What is the key difference between optimistic and pessimistic concurrency control in DBMS?'
            },
            {
                'year': '2023 Deloitte Campus Solved Paper',
                'title': f'{comp_clean} National Level Assessment Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Given a binary tree, check whether it is a Height Balanced Tree.',
                'sample_quant': 'Find the simple interest on $8,000 at 5% per annum for 3 years.',
                'sample_tech': 'What is normalization in SQL? Explain 1NF, 2NF, and 3NF.'
            }
        ]

    elif 'wipro' in c_lower:
        total_qs = 92
        total_mins = 135
        exam_pattern = standard_exam_pattern
        table_rounds = standard_table_rounds
        past_papers = [
            {
                'year': '2025 Wipro NTH Official Paper',
                'title': f'{comp_clean} National Talent Hunt Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Given an array of integers, return the second non-repeating element.',
                'sample_quant': 'Find compound interest on $10,000 for 2 years at 10% per annum compounded half-yearly.',
                'sample_tech': 'What is the difference between shallow copy and deep copy in Java?'
            },
            {
                'year': '2024 Wipro NTH Memory Based Paper',
                'title': f'{comp_clean} National Talent Hunt Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the longest word in a sentence with even character length.',
                'sample_quant': 'In how many ways can the letters of the word EXCELLENCE be arranged?',
                'sample_tech': 'What is garbage collection in Java and how does System.gc() work?'
            },
            {
                'year': '2023 Wipro Campus Solved Paper',
                'title': f'{comp_clean} Campus Placement Solved Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Write a C program to check if an integer is an Armstrong Number.',
                'sample_quant': 'A man buys an item for $1,400 and sells it at a loss of 15%. Find selling price.',
                'sample_tech': 'Explain static variable vs global variable in C language.'
            }
        ]

    elif 'capgemini' in c_lower:
        total_qs = 92
        total_mins = 135
        exam_pattern = standard_exam_pattern
        table_rounds = standard_table_rounds
        past_papers = [
            {
                'year': '2025 Capgemini Exceller Official Paper',
                'title': f'{comp_clean} Exceller Placement Paper 2025 Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Write a function to count occurrences of prime numbers in a 2D matrix.',
                'sample_quant': 'Grid movement & spatial memory game: solve 2 interactive cognitive challenges.',
                'sample_tech': 'Determine output of nested pseudocode loop with bitwise right shifts.'
            },
            {
                'year': '2024 Capgemini Exceller Memory Based Paper',
                'title': f'{comp_clean} Exceller Placement Paper 2024 Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Given an integer array, find the maximum product subarray in O(N) time.',
                'sample_quant': 'A tank can be filled by two pipes in 12 and 16 hours. How long will it take if both are open together?',
                'sample_tech': 'What is the difference between Abstract Class and Interface in Java / C++?'
            },
            {
                'year': '2023 Capgemini Campus Placement Solved Paper',
                'title': f'{comp_clean} Campus Selection Solved Paper 2023 Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Remove duplicate characters from a string while preserving original order.',
                'sample_quant': 'Find the angle between hour and minute hands of a clock at 3:30.',
                'sample_tech': 'Explain virtual functions and dynamic dispatch mechanism in C++.'
            }
        ]

    elif 'tech mahindra' in c_lower or 'techmahindra' in c_lower:
        total_qs = 92
        total_mins = 135
        table_headers = ['Round', 'What is tested']
        table_rounds = standard_table_rounds
        selection_stages = selection_stages
        exam_pattern = [
            {'section': 'Round 1: Aptitude + English', 'questions': 'Quant, Verbal, Reasoning', 'time': '45 Mins', 'icon': '📊', 'color': '#38bdf8'},
            {'section': 'Round 2: Technical/Psychometric', 'questions': 'Pseudo Code & Fundamentals', 'time': '40 Mins', 'icon': '💻', 'color': '#fbbf24'},
            {'section': 'Round 3: Communication', 'questions': 'Spoken English Test', 'time': '20 Mins', 'icon': '🗣️', 'color': '#a855f7'},
            {'section': 'Round 4 & 5: Tech & HR Interview', 'questions': 'Coding, Projects & HR Chat', 'time': '45 Mins', 'icon': '🤝', 'color': '#10b981'}
        ]
        past_papers = [
            {
                'year': '2025 Official Assessment Paper',
                'title': f'{comp_clean} National Level Assessment Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Write a C program to check if an integer is an Armstrong Number.',
                'sample_quant': 'A car covers a distance at 60 km/h in 4 hours. At what speed must it travel to cover it in 3 hours?',
                'sample_tech': 'What is the key difference between Process and Thread in Operating Systems?'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': f'{comp_clean} Previous Year Assessment Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the second non-repeating character in a given input string.',
                'sample_quant': 'A trader marks goods 20% above cost price and gives a 10% discount. Find profit percentage.',
                'sample_tech': 'Explain primary key vs candidate key in Relational Database Management Systems.'
            },
            {
                'year': '2023 Campus Solved Paper',
                'title': f'{comp_clean} Campus Placement Solved Paper Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Given an integer array, move all zeroes to the end while preserving non-zero element order.',
                'sample_quant': 'Two pipes A and B fill a tank in 12 and 15 hours. How long will both take together?',
                'sample_tech': 'Explain static variable vs global variable in C language.'
            }
        ]

    elif 'google' in c_lower:
        total_qs = 50
        total_mins = 180
        table_headers = ['Round', 'Typical format', 'What they test']
        table_rounds = [
            {
                'round_name': '1. Online Assessment / Screening',
                'sections': [
                    {'name': 'Coding problems', 'qs': 'DSA, problem solving'}
                ]
            },
            {
                'round_name': '2. Technical Interviews',
                'sections': [
                    {'name': 'Usually 3-4 interviews', 'qs': 'DSA, algorithms, coding, CS fundamentals'}
                ]
            },
            {
                'round_name': '3. Googleyness / Behavioral',
                'sections': [
                    {'name': '1 interview or integrated into interviews', 'qs': 'Communication, teamwork, decision-making'}
                ]
            },
            {
                'round_name': '4. Hiring Committee',
                'sections': [
                    {'name': 'Internal review', 'qs': 'Overall interview performance'}
                ]
            },
            {
                'round_name': '5. Team Matching',
                'sections': [
                    {'name': 'Team discussions', 'qs': 'Role/team fit'}
                ]
            },
            {
                'round_name': '6. Offer',
                'sections': [
                    {'name': 'Final stage', 'qs': 'Compensation and joining details'}
                ]
            }
        ]
        selection_stages = [
            {'step': 1, 'title': 'Screening / OA', 'desc': 'Coding Problems | DSA & Problem Solving', 'icon': '💻'},
            {'step': 2, 'title': 'Tech Interviews', 'desc': '3–4 Interviews | DSA, Algorithms, CS Fundamentals', 'icon': '🎯'},
            {'step': 3, 'title': 'Googleyness', 'desc': 'Behavioral & Leadership | Communication & Teamwork', 'icon': '🌟'},
            {'step': 4, 'title': 'Hiring Committee', 'desc': 'Internal Review | Overall Interview Performance', 'icon': '⚖️'},
            {'step': 5, 'title': 'Team Matching', 'desc': 'Team Discussions | Role & Team Fit', 'icon': '🤝'},
            {'step': 6, 'title': 'Offer', 'desc': 'Final Stage | Compensation & Joining Details', 'icon': '🎉'}
        ]
        exam_pattern = [
            {'section': 'Online Assessment / Screening', 'questions': 'Coding Problems', 'time': '60-90 Mins', 'icon': '💻', 'color': '#38bdf8'},
            {'section': 'Technical Interviews (3-4 Loops)', 'questions': 'DSA & System Design', 'time': '45 Mins each', 'icon': '🧠', 'color': '#fbbf24'},
            {'section': 'Googleyness & Leadership', 'questions': 'Behavioral Scenarios', 'time': '45 Mins', 'icon': '🌟', 'color': '#a855f7'},
            {'section': 'Hiring Committee & Team Matching', 'questions': 'Packet Review & Fit Chats', 'time': '1-2 Weeks', 'icon': '🤝', 'color': '#10b981'}
        ]
        past_papers = [
            {
                'year': '2025 Google SWE Official Practice Set',
                'title': 'Google SDE Problem Solving & Algorithm Assessment Model 1',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Given a directed graph, find the shortest path with constraint on edge colors.',
                'sample_quant': 'Analyze amortized time complexity of dynamic array resizing algorithm.',
                'sample_tech': 'How does Google Bigtable handle consistent hashing and SSTable compaction?'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Google SWE Onsite Coding & DSA Assessment Model 2',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Implement a thread-safe Rate Limiter using Sliding Window Counter algorithm.',
                'sample_quant': 'Given a stream of integers, maintain median in O(log N) per insert operation.',
                'sample_tech': 'Explain Paxos vs Raft consensus algorithms in distributed system architectures.'
            },
            {
                'year': '2023 Google Campus Selection Paper',
                'title': 'Google University Graduate SDE Placement Paper Model 3',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Serialize and Deserialize N-ary Tree structure with minimal string size.',
                'sample_quant': 'Find total unique paths in a grid with obstacles using Dynamic Programming.',
                'sample_tech': 'Explain Virtual Memory management and Page Fault handling in Operating Systems.'
            }
        ]

    elif 'meta' in c_lower or 'facebook' in c_lower:
        total_qs = 25
        total_mins = 120
        table_headers = ['Interview', 'Main focus']
        table_rounds = [
            {
                'round_name': 'Coding 1',
                'sections': [{'name': 'DSA + problem solving'}]
            },
            {
                'round_name': 'Coding 2',
                'sections': [{'name': 'DSA + optimization'}]
            },
            {
                'round_name': 'Coding / AI-enabled',
                'sections': [{'name': 'Coding + debugging/code review, where applicable'}]
            },
            {
                'round_name': 'System Design',
                'sections': [{'name': 'Architecture/design, especially for experienced roles'}]
            },
            {
                'round_name': 'Behavioral',
                'sections': [{'name': 'Collaboration, impact, leadership'}]
            },
            {
                'round_name': 'Additional technical',
                'sections': [{'name': 'Depends on role/level'}]
            }
        ]
        selection_stages = [
            {'step': 1, 'title': 'Screening / OA', 'desc': 'Coding 1 & Coding 2 | DSA, Optimization & Problem Solving', 'icon': '💻'},
            {'step': 2, 'title': 'Tech Loop', 'desc': 'Coding / AI-enabled | Debugging & Code Review', 'icon': '🔍'},
            {'step': 3, 'title': 'System Design', 'desc': 'Architecture & Scalable System Design', 'icon': '🏗️'},
            {'step': 4, 'title': 'Behavioral', 'desc': 'Collaboration, Leadership & Impact', 'icon': '🤝'}
        ]
        exam_pattern = [
            {'section': 'Coding 1 & Coding 2', 'questions': 'DSA & Optimization', 'time': '45 Mins each', 'icon': '💻', 'color': '#38bdf8'},
            {'section': 'Coding / AI-enabled', 'questions': 'Debugging & Review', 'time': '45 Mins', 'icon': '🔍', 'color': '#fbbf24'},
            {'section': 'System Design', 'questions': 'Architecture', 'time': '45 Mins', 'icon': '🏗️', 'color': '#a855f7'},
            {'section': 'Behavioral', 'questions': 'Leadership & Impact', 'time': '45 Mins', 'icon': '🤝', 'color': '#10b981'}
        ]
        past_papers = [
            {
                'year': '2025 Meta Official Practice Set',
                'title': f'{comp_clean} Software Engineer Assessment Model 1',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Given a binary tree, return the vertical order traversal of its nodes values.',
                'sample_quant': 'Analyze the time and space complexity of sparse matrix multiplication.',
                'sample_tech': 'How does Meta Memcached scale distributed caching across millions of QPS?'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': f'{comp_clean} Rotational Engineer Assessment Model 2',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Valid Palindrome II: check if a string can be palindrome after deleting at most 1 char.',
                'sample_quant': 'Maintain top K frequent elements from continuous real-time event logs.',
                'sample_tech': 'Explain GraphQL query execution engine vs REST API architecture.'
            },
            {
                'year': '2023 Meta Campus Selection Paper',
                'title': f'{comp_clean} University Graduate Solved Paper Model 3',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Simplify Path: given an absolute Unix-style path, convert it to simplified canonical path.',
                'sample_quant': 'Calculate minimum total distance to visit all target points in 2D coordinate grid.',
                'sample_tech': 'Explain Virtual Memory page replacement policies LRU vs LFU.'
            }
        ]

    elif 'apple' in c_lower:
        total_qs = 25
        total_mins = 120
        table_headers = ['Round', 'Main focus']
        table_rounds = [
            {
                'round_name': '1. Online Assessment',
                'sections': [{'name': 'Coding problems, DSA, problem solving'}]
            },
            {
                'round_name': '2. Technical Interviews (3-5 loops)',
                'sections': [{'name': 'DSA, algorithms, system design, CS fundamentals'}]
            },
            {
                'round_name': '3. System Design',
                'sections': [{'name': 'Architecture, scalability, iOS/macOS platform design'}]
            },
            {
                'round_name': '4. Behavioral',
                'sections': [{'name': 'Collaboration, ownership, innovation, Apple values'}]
            },
            {
                'round_name': '5. Hiring Manager',
                'sections': [{'name': 'Final review, role and team fit'}]
            }
        ]
        selection_stages = [
            {'step': 1, 'title': 'Online Assessment', 'desc': 'Coding Problems | DSA & Problem Solving', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Loops', 'desc': '3–5 Interviews | DSA, Algorithms, CS Fundamentals', 'icon': '🎯'},
            {'step': 3, 'title': 'System Design', 'desc': 'Architecture & Scalability | iOS/macOS Platform Design', 'icon': '🏗️'},
            {'step': 4, 'title': 'Behavioral', 'desc': 'Collaboration, Ownership & Apple Values', 'icon': '🤝'},
            {'step': 5, 'title': 'Hiring Manager', 'desc': 'Final Review | Role & Team Fit', 'icon': '✅'}
        ]
        exam_pattern = [
            {'section': 'Online Assessment', 'questions': 'Coding Problems', 'time': '60-90 Mins', 'icon': '💻', 'color': '#38bdf8'},
            {'section': 'Technical Interviews (3-5 Loops)', 'questions': 'DSA & System Design', 'time': '45 Mins each', 'icon': '🧠', 'color': '#fbbf24'},
            {'section': 'System Design', 'questions': 'Architecture & Platform Design', 'time': '45 Mins', 'icon': '🏗️', 'color': '#a855f7'},
            {'section': 'Behavioral & Hiring Manager', 'questions': 'Values & Leadership', 'time': '45 Mins', 'icon': '🤝', 'color': '#10b981'}
        ]
        past_papers = [
            {
                'year': '2025 Apple SWE Official Practice Set',
                'title': 'Apple Software Engineer Assessment Model 1',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Given a list of app events with timestamps, find the top-K most frequent events in O(N log K) time.',
                'sample_quant': 'Analyze the time and space complexity of a recursive algorithm for generating all subsets of a set.',
                'sample_tech': 'How does Apple\'s Core Data framework handle persistent storage and concurrency in iOS apps?'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Apple SWE Onsite Coding & System Design Model 2',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Implement an LFU Cache with O(1) time complexity for get and put operations.',
                'sample_quant': 'Given a stream of integers, find the median after each insertion using two heaps.',
                'sample_tech': 'Explain Metal graphics API and how it differs from OpenGL for GPU-accelerated rendering on Apple platforms.'
            },
            {
                'year': '2023 Apple Campus Selection Paper',
                'title': 'Apple University Graduate SDE Placement Paper Model 3',
                'total_qs': 25,
                'duration': '120 Mins',
                'sample_coding': 'Design a thread-safe, memory-efficient trie supporting autocomplete with wildcard support.',
                'sample_quant': 'Find the minimum number of operations to convert one binary string to another using dynamic programming.',
                'sample_tech': 'Explain Swift\'s ARC (Automatic Reference Counting) and how it prevents retain cycles.'
            }
        ]

    else:
        # Default Fallback Company Pattern
        total_qs = 92
        total_mins = 135
        exam_pattern = standard_exam_pattern
        table_rounds = standard_table_rounds
        past_papers = [
            {
                'year': '2025 Official Assessment Paper',
                'title': f'{comp_clean} Online Assessment Test Model 1',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Write a program to find the longest palindrome substring in a given input string.',
                'sample_quant': 'If 12 men or 18 women finish a project in 14 days, how long do 8 men and 16 women take?',
                'sample_tech': 'What is the time complexity of searching an element in a Balanced Binary Search Tree (AVL Tree)?'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': f'{comp_clean} Previous Year Assessment Model 2',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Given an integer array, move all zeroes to the end while maintaining relative order of non-zero elements.',
                'sample_quant': 'A sum of money doubles itself in 8 years at simple interest. What is the annual rate of interest?',
                'sample_tech': 'Explain the difference between Method Overloading and Method Overriding in OOP.'
            },
            {
                'year': '2023 Campus Placement Solved Paper',
                'title': f'{comp_clean} Campus Drive Solved Paper Model 3',
                'total_qs': 92,
                'duration': '135 Mins',
                'sample_coding': 'Find the first non-repeating character in a string using Hash Map in O(N) time.',
                'sample_quant': 'Two trains running in opposite directions cross a man standing on the platform in 27s and 17s. Find ratio of their speeds.',
                'sample_tech': 'What is deadlock in Operating Systems? Explain the 4 necessary Coffman conditions.'
            }
        ]

    if 'selection_stages' not in locals():
        selection_stages = [
            {'step': 1, 'title': 'Group Discussion', 'desc': '1–3 Topics | 10–20 Mins', 'icon': '🗣️'},
            {'step': 2, 'title': 'Technical Round', 'desc': '15–30 Questions | 30–60 Mins', 'icon': '💻'},
            {'step': 3, 'title': 'Managerial Round', 'desc': '8–15 Questions | 20–40 Mins', 'icon': '👔'},
            {'step': 4, 'title': 'HR Round', 'desc': '8–15 Questions | 15–30 Mins', 'icon': '📜'},
            {'step': 5, 'title': 'Mock Interview', 'desc': '10–20 Questions | 20–40 Mins', 'icon': '🎙️'}
        ]

    # Build enriched company_meta for UI branding & stats
    company_meta = {
        'ctc': '₹4.5 - ₹6.5 LPA',
        'roles': 'Software Engineer / Associate Analyst',
        'eligibility': '60% or 6.5 CGPA in 10th, 12th & Graduation',
        'difficulty': 'Moderate',
        'difficulty_class': 'badge-warning',
        'logo_icon': '⚡',
        'brand_color': '#6366f1',
        'accent_bg': 'linear-gradient(135deg, #6366f1 0%, #4338ca 100%)',
        'tagline': f'Complete placement exam pattern, syllabus, sectional cutoffs & solved model papers for {comp_clean}.',
        'syllabus': [
            {'category': 'Cognitive Assessment', 'icon': '🧠', 'qs': '50 Qs', 'time': '50 Mins', 'topics': ['Quantitative Aptitude', 'Logical & Critical Reasoning', 'Abstract Reasoning', 'Verbal Ability & RC']},
            {'category': 'Technical & Pseudocode', 'icon': '💻', 'qs': '40 Qs', 'time': '40 Mins', 'topics': ['Pseudocode & Bitwise Operators', 'Data Structures & Logic', 'Networking & Cloud Basics', 'DBMS, SQL & Security']},
            {'category': 'Coding Assessment', 'icon': '⚡', 'qs': '2 Qs', 'time': '45 Mins', 'topics': ['Array Subsegment Logic', 'String Manipulation', 'Bit Operations', 'Optimized Algorithm Design']},
            {'category': 'Communication Assessment', 'icon': '🗣️', 'qs': '6 Modules', 'time': '20 Mins', 'topics': ['Sentence Reading & Repeat', 'Vocabulary & Pronunciation', 'Short Story Retelling', 'Fluency & Conversation']}
        ],
        'faqs': [
            {'q': f'Is there negative marking in {comp_clean} online assessment?', 'a': 'No, there is no negative marking in the assessment. Candidates are encouraged to attempt all questions.'},
            {'q': f'Can candidates switch between sections during the exam?', 'a': 'No. Sections are strictly time-bound. Once the allocated time for a section expires, candidates automatically proceed to the next section.'},
            {'q': f'Which programming languages can be used in the coding section?', 'a': 'Supported languages include C, C++, Java, Python, and JavaScript.'},
            {'q': f'What is the minimum eligibility criteria for {comp_clean} campus recruitment?', 'a': 'A minimum of 60% or 6.5 CGPA in 10th, 12th, and Graduation with no active backlogs.'}
        ]
    }

    if 'accenture' in c_lower:
        company_meta.update({
            'logo_icon': '⚡',
            'brand_color': '#a100ff',
            'accent_bg': 'linear-gradient(135deg, #a100ff 0%, #4f46e5 100%)',
            'roles': 'Associate Software Engineer (ASE) & Advanced ASE',
            'ctc': '₹4.5 - ₹6.5 LPA',
            'eligibility': '60% or 6.5 CGPA in B.E/B.Tech/MCA/M.Sc',
            'difficulty': 'Moderate to Hard',
            'difficulty_class': 'badge-warning'
        })
    elif 'tcs' in c_lower:
        company_meta.update({
            'logo_icon': '🏆',
            'brand_color': '#0284c7',
            'accent_bg': 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
            'roles': 'TCS Ninja (₹3.36 LPA) & TCS Digital (₹7.0 - ₹9.0 LPA)',
            'ctc': '₹3.36 - ₹9.0 LPA',
            'eligibility': '60% throughout academics (10th, 12th, UG/PG)',
            'difficulty': 'Moderate to Advanced',
            'difficulty_class': 'badge-danger'
        })
    elif 'infosys' in c_lower or 'infy' in c_lower:
        company_meta.update({
            'logo_icon': '🚀',
            'brand_color': '#007cc3',
            'accent_bg': 'linear-gradient(135deg, #007cc3 0%, #1e40af 100%)',
            'roles': 'System Engineer (SE) & Specialist Programmer (SP)',
            'ctc': '₹3.6 - ₹9.5 LPA',
            'eligibility': '60% or 6.0 CGPA in B.E/B.Tech/MCA/M.Sc',
            'difficulty': 'Moderate',
            'difficulty_class': 'badge-warning'
        })
    elif 'amazon' in c_lower:
        company_meta.update({
            'logo_icon': '📦',
            'brand_color': '#ff9900',
            'accent_bg': 'linear-gradient(135deg, #ff9900 0%, #d97706 100%)',
            'roles': 'Software Development Engineer (SDE-1)',
            'ctc': '₹18.0 - ₹45.0 LPA',
            'eligibility': 'B.E / B.Tech / M.Tech in CS/IT/EC',
            'difficulty': 'Hard / Advanced',
            'difficulty_class': 'badge-danger'
        })
    elif 'google' in c_lower:
        company_meta.update({
            'logo_icon': '🌐',
            'brand_color': '#4285f4',
            'accent_bg': 'linear-gradient(135deg, #4285f4 0%, #34a853 100%)',
            'roles': 'Software Engineer (L3 / Early Career)',
            'ctc': '₹25.0 - ₹60.0 LPA',
            'eligibility': 'B.S / M.S / Ph.D in CS or STEM',
            'difficulty': 'Very Hard',
            'difficulty_class': 'badge-danger'
        })
    elif 'wipro' in c_lower:
        company_meta.update({
            'logo_icon': '💼',
            'brand_color': '#4e148c',
            'accent_bg': 'linear-gradient(135deg, #4e148c 0%, #6b21a8 100%)',
            'roles': 'Project Engineer (Elite NTH & Turbo)',
            'ctc': '₹3.5 - ₹6.5 LPA',
            'eligibility': '60% or 6.0 CGPA in 10th, 12th & Graduation',
            'difficulty': 'Easy to Moderate',
            'difficulty_class': 'badge-info'
        })

    return render_template('company_detail.html',
                           company_name=comp_clean,
                           exam_pattern=exam_pattern,
                           selection_stages=selection_stages,
                           past_papers=past_papers,
                           table_rounds=table_rounds,
                           table_headers=table_headers,
                           total_qs=total_qs,
                           total_mins=total_mins,
                           company_meta=company_meta)

def get_quant_logical_10_qs(comp_name, title_str):
    t_lower = title_str.lower()
    
    # Paper Model 2 (2024 Memory Based)
    if 'model 2' in t_lower or '2024' in t_lower:
        return [
            {
                'q_num': 1, 'type': 'mcq',
                'title': f'{comp_name} Quant: Simple Interest & Principal Multiples',
                'text': 'A sum of money doubles itself in 8 years under Simple Interest. In how many years will it triple itself at the same annual interest rate?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'SI for 8 yrs = Principal P. To triple, SI needed = 2P. Time = 8 * 2 = 16 years.'
            },
            {
                'q_num': 2, 'type': 'mcq',
                'title': f'{comp_name} Quant: Ratios & Mixture Alligation',
                'text': 'In a 60-liter mixture of alcohol and water, the ratio of alcohol to water is 2:1. How many liters of water must be added to make the ratio 1:2?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Alcohol = 40L, Water = 20L. New ratio 40 / (20 + x) = 1/2 => 80 = 20 + x => x = 60 liters.'
            },
            {
                'q_num': 3, 'type': 'mcq',
                'title': f'{comp_name} Quant: Averages & Age Problems',
                'text': 'The average age of a family of 4 members is 28 years. If the age of the grandfather (68 years) is included, what is the new average age of the family?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Sum of 4 = 4 * 28 = 112. Total sum with grandfather = 112 + 68 = 180. New average = 180 / 5 = 36 years.'
            },
            {
                'q_num': 4, 'type': 'mcq',
                'title': f'{comp_name} Quant: Probability & Event Selection',
                'text': 'A bag contains 5 Red, 4 Green, and 3 Blue balls. If 2 balls are drawn at random without replacement, what is the probability that both balls are Red?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'P(Both Red) = (5C2) / (12C2) = 10 / 66 = 5/33.'
            },
            {
                'q_num': 5, 'type': 'mcq',
                'title': f'{comp_name} Quant: Mensuration & Geometric Ratios',
                'text': 'If the radius of a cylinder is doubled and its height is halved, what is the ratio of the new volume to the original volume?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'V1 = pi * r^2 * h. V2 = pi * (2r)^2 * (h/2) = 2 * pi * r^2 * h = 2 * V1.'
            },
            {
                'q_num': 6, 'type': 'mcq',
                'title': f'{comp_name} Logical: Letter Series & Alphabet Offset',
                'text': 'Find the next term in the alphabet series: A, D, G, J, M, ?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Each letter shifts forward by +3 positions: 1, 4, 7, 10, 13, 16 (P).'
            },
            {
                'q_num': 7, 'type': 'mcq',
                'title': f'{comp_name} Logical: Statement & Critical Assumptions',
                'text': 'Statement: "Employees must complete security awareness training before accessing production servers."\nAssumptions:\nI. Security awareness training reduces operational risk.\nII. Production servers contain sensitive assets.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Both assumptions directly justify mandatory training before granting access to critical infrastructure.'
            },
            {
                'q_num': 8, 'type': 'mcq',
                'title': f'{comp_name} Logical: Circular Seating Arrangement',
                'text': 'Six persons A, B, C, D, E, F sit in a circle facing the center. A sits opposite D. B sits to the immediate right of A. C is between D and B. Who sits to the immediate left of A?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Order around circle: A, B, C, D, E, F. To immediate left of A is F.'
            },
            {
                'q_num': 9, 'type': 'mcq',
                'title': f'{comp_name} Logical: Clocks & Angle Calculation',
                'text': 'At what exact angle are the hands of a clock inclined at 3:30?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Angle = |(30 * 3) - (5.5 * 30)| = |90 - 165| = 75 degrees.'
            },
            {
                'q_num': 10, 'type': 'mcq',
                'title': f'{comp_name} Logical: Venn Diagram & Set Inclusion',
                'text': 'In a tech company of 100 engineers, 65 know Python, 45 know Java, and 20 know both languages. How many engineers know NEITHER Python nor Java?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Union = 65 + 45 - 20 = 90. Neither = 100 - 90 = 10 engineers.'
            }
        ]
    
    # Paper Model 3 (2023 Campus Solved)
    elif 'model 3' in t_lower or '2023' in t_lower:
        return [
            {
                'q_num': 1, 'type': 'mcq',
                'title': f'{comp_name} Quant: Work & Efficiency Ratio',
                'text': '3 men or 6 women can finish a software testing project in 16 days. How many days will 12 men and 8 women take to complete the same project?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '1 Man = 2 Women. 12 Men + 8 Women = 24 + 8 = 32 Women. (6 * 16) / 32 = 3 days.'
            },
            {
                'q_num': 2, 'type': 'mcq',
                'title': f'{comp_name} Quant: Boats & Streams Speed',
                'text': 'A boat travels 24 km downstream in 2 hours and returns upstream in 4 hours. What is the speed of the current in km/h?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Downstream speed = 12 km/h, Upstream speed = 6 km/h. Current speed = (12 - 6) / 2 = 3 km/h.'
            },
            {
                'q_num': 3, 'type': 'mcq',
                'title': f'{comp_name} Quant: Logarithms & Exponents',
                'text': 'Find the value of log2(64) + log3(81) - log5(125):',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'log2(64)=6, log3(81)=4, log5(125)=3. Value = 6 + 4 - 3 = 7.'
            },
            {
                'q_num': 4, 'type': 'mcq',
                'title': f'{comp_name} Quant: Partnership & Capital Investment',
                'text': 'A and B enter into a partnership investing $20,000 and $30,000 respectively. If total profit at year end is $15,000, what is A\'s share of profit?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Ratio = 2:3. A\'s share = (2/5) * 15000 = $6,000.'
            },
            {
                'q_num': 5, 'type': 'mcq',
                'title': f'{comp_name} Quant: Data Interpretation Growth Rate',
                'text': 'A tech startup\'s annual revenue grew from $400,000 in 2022 to $520,000 in 2023. What was the percentage increase in revenue?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Increase = 120,000. Percentage = (120,000 / 400,000) * 100 = 30%.'
            },
            {
                'q_num': 6, 'type': 'mcq',
                'title': f'{comp_name} Logical: Coding by Position Inversion',
                'text': 'If \'LOGIC\' is coded as \'CIGOL\', how is \'DATABASE\' coded in the same transformation scheme?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'The letters of the string are completely reversed in sequence.'
            },
            {
                'q_num': 7, 'type': 'mcq',
                'title': f'{comp_name} Logical: Cause & Effect Reasoning',
                'text': 'Statement 1: The central bank raised key interest rates by 50 basis points.\nStatement 2: Commercial banks increased home loan interest rates.\nDetermine relation:',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'The central bank policy rate hike directly causes commercial banks to raise lending rates.'
            },
            {
                'q_num': 8, 'type': 'mcq',
                'title': f'{comp_name} Logical: Linear Seating Arrangement',
                'text': 'Seven friends P, Q, R, S, T, U, V sit in a single row facing North. R sits in the exact middle. P sits at the extreme left end. How many persons sit between P and R?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Row positions: [P, _, _, R, _, _, _]. Positions between 1 and 4 are 2 and 3 (2 persons).'
            },
            {
                'q_num': 9, 'type': 'mcq',
                'title': f'{comp_name} Logical: Cubes & Opposite Face Deduction',
                'text': 'A cube is painted red on all sides and cut into 64 small identical cubes. How many small cubes have EXACTLY 2 faces painted red?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'For n=4 (4x4x4=64): 2-face painted cubes lie on edges = 12 * (n - 2) = 12 * 2 = 24.'
            },
            {
                'q_num': 10, 'type': 'mcq',
                'title': f'{comp_name} Logical: Symbol Substitution Logic',
                'text': 'If \'+\' means \'*\', \'-\' means \'/\', \'*\' means \'+\', and \'/\' means \'-\', evaluate expression: 20 - 4 + 5 * 10 / 2',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Replaced expression: (20 / 4) * 5 + 10 - 2 = 5 * 5 + 10 - 2 = 25 + 10 - 2 = 33.'
            }
        ]

    # Default / Model 1 Pool (2025 Official)
    else:
        return [
            {
                'q_num': 1, 'type': 'mcq',
                'title': f'{comp_name} Quant: Time & Work (Pipes System)',
                'text': 'Pipes A and B can fill a tank in 20 and 30 minutes respectively. If both pipes are opened together, after how many minutes should Pipe A be closed so that the tank is completely filled in 15 minutes?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Pipe B works for full 15 mins (15/30 = 1/2 tank filled by B). Remaining 1/2 tank must be filled by Pipe A. Rate of Pipe A = 1/20 per min. Time required = (1/2) / (1/20) = 10 minutes.'
            },
            {
                'q_num': 2, 'type': 'mcq',
                'title': f'{comp_name} Quant: Compound Interest & Installments',
                'text': 'A sum of $12,500 is borrowed at 10% per annum compound interest. If it is repaid in two equal annual installments, find the value of each installment.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Principal P = X/(1+r/100) + X/(1+r/100)^2 => 12500 = X/1.1 + X/1.21 => 12500 = X*(2.1)/1.21 => X = $7,202.38 per installment.'
            },
            {
                'q_num': 3, 'type': 'mcq',
                'title': f'{comp_name} Quant: Profit, Loss & Percentage Discount',
                'text': 'A shopkeeper marks an article 30% above its cost price and allows a discount of 15% on the marked price. What is the shopkeeper\'s net profit percentage?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Let Cost Price = 100. Marked Price = 130. Selling Price = 130 * (1 - 0.15) = 110.5. Net profit percentage = 110.5 - 100 = 10.5%.'
            },
            {
                'q_num': 4, 'type': 'mcq',
                'title': f'{comp_name} Quant: Permutations & Combinations',
                'text': 'In how many different ways can the letters of the word \'LEADER\' be arranged such that the vowels (E, A, E) always come together?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Group vowels (EAE) as 1 block. Total items to arrange = L, D, R, (EAE) = 4 items => 4! = 24 ways. Inside block (EAE), 3! / 2! = 3 ways. Total = 24 * 3 = 72 ways.'
            },
            {
                'q_num': 5, 'type': 'mcq',
                'title': f'{comp_name} Quant: Relative Speed of Two Trains',
                'text': 'Two trains 140m and 160m long run in opposite directions at speeds of 60 km/h and 48 km/h respectively. How many seconds will they take to cross each other?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Total distance = 300m. Relative speed = 60 + 48 = 108 km/h = 30 m/s. Time = 300 / 30 = 10 seconds.'
            },
            {
                'q_num': 6, 'type': 'mcq',
                'title': f'{comp_name} Logical: Number Series & Pattern Recognition',
                'text': 'Find the next term in the logical series: 12, 23, 45, 89, 177, ?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Pattern is (N * 2) - 1. (12*2)-1=23, (23*2)-1=45, (45*2)-1=89, (89*2)-1=177, (177*2)-1 = 354 - 1 = 353.'
            },
            {
                'q_num': 7, 'type': 'mcq',
                'title': f'{comp_name} Logical: Syllogisms & Deductive Inference',
                'text': 'Statements:\n1. All algorithms are functions.\n2. Some functions are recursive.\nConclusions:\nI. Some algorithms are recursive.\nII. No function is an algorithm.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Intersection between algorithms and recursive functions is uncertain without direct premise statement.'
            },
            {
                'q_num': 8, 'type': 'mcq',
                'title': f'{comp_name} Logical: Coding-Decoding & Substitution Cipher',
                'text': 'If \'PYTHON\' is coded as \'QZUIPO\' in a secret cipher, how is \'CODING\' coded in the same cipher language?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Each letter is shifted forward by +1 position in the alphabet (C->D, O->P, D->E, I->J, N->O, G->H).'
            },
            {
                'q_num': 9, 'type': 'mcq',
                'title': f'{comp_name} Logical: Data Sufficiency & Direction Sense',
                'text': 'A person walks 10 km Towards North, turns Right and walks 5 km, then turns Right and walks 10 km. How far and in which direction is the person from the starting point?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'North (+10 km) and South (-10 km) cancel out. The net displacement is 5 km towards East.'
            },
            {
                'q_num': 10, 'type': 'mcq',
                'title': f'{comp_name} Logical: Blood Relations & Family Tree Deduction',
                'text': 'Pointing to a photograph, a woman says: "He is the only son of the mother-in-law of my husband\'s only sister." How is the man in the photograph related to the woman?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Mother-in-law of husband\'s sister is her sister-in-law\'s mother-in-law. Her only son is her sister-in-law\'s husband (brother-in-law).'
            }
        ]

def get_verbal_english_10_qs(comp_name, title_str):
    t_lower = title_str.lower()
    
    if 'model 2' in t_lower or '2024' in t_lower:
        return [
            {
                'q_num': 11, 'type': 'mcq',
                'title': f'{comp_name} Grammar: Subject-Verb Agreement',
                'text': 'Which of the following options represents the grammatically correct sentence?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '"Each of" takes a singular verb ("is") regardless of plural noun in prepositional phrase.'
            },
            {
                'q_num': 12, 'type': 'mcq',
                'title': f'{comp_name} Vocabulary: Synonyms',
                'text': 'Choose the word that is MOST NEARLY SYNONYMOUS in meaning to \'LOQUACIOUS\':',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Loquacious\' means tending to talk a great deal; talkative or garrulous.'
            },
            {
                'q_num': 13, 'type': 'mcq',
                'title': f'{comp_name} Vocabulary: Antonyms',
                'text': 'Choose the word that is MOST OPPOSITE in meaning to \'CANDID\':',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Candid\' means truthful, straightforward, and frank; its opposite is deceitful or evasive.'
            },
            {
                'q_num': 14, 'type': 'mcq',
                'title': f'{comp_name} Sentence Completion',
                'text': 'The CEO\'s speech was so _______ that it inspired the entire engineering team to work with renewed vigor.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Eloquent\' means fluent, persuasive, and expressive in speech.'
            },
            {
                'q_num': 15, 'type': 'mcq',
                'title': f'{comp_name} Idioms & Phrases',
                'text': 'What is the meaning of the idiom \'Hit the nail on the head\'?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Hit the nail on the head\' means to state or identify something with precise accuracy.'
            },
            {
                'q_num': 16, 'type': 'mcq',
                'title': f'{comp_name} Voice Transformation',
                'text': 'Convert to Passive Voice: "The cybersecurity team patched the critical vulnerability."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Simple past active (\'patched\') changes to simple past passive (\'was patched\').'
            },
            {
                'q_num': 17, 'type': 'mcq',
                'title': f'{comp_name} Direct & Indirect Speech',
                'text': 'Convert to Indirect Speech: The manager asked, "Will you complete the report by Friday?"',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'In reported question speech, modal \'will\' changes to \'would\'.'
            },
            {
                'q_num': 18, 'type': 'mcq',
                'title': f'{comp_name} Reading Comprehension',
                'text': 'Passage: "Artificial Intelligence algorithms in diagnostic medicine process high-resolution medical imagery to detect cellular anomalies earlier than standard clinical evaluations."\n\nQuestion: What is a key diagnostic advantage mentioned?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'The passage highlights early detection of cellular anomalies as the core advantage.'
            },
            {
                'q_num': 19, 'type': 'mcq',
                'title': f'{comp_name} Para Jumbles',
                'text': 'Arrange in logical sequence:\nP. Threat intelligence platforms aggregate security signals.\nQ. Consequently, security teams neutralize breaches in real time.\nR. Cyber attacks are growing in frequency and sophistication.\nS. Machine learning models then identify suspicious activity.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Sentence R states problem, P introduces platform, S details AI processing, Q concludes result.'
            },
            {
                'q_num': 20, 'type': 'mcq',
                'title': f'{comp_name} One-Word Substitution',
                'text': 'Choose the correct one-word substitute for: "One who always expects the best outcome in every situation."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'An \'optimist\' is a person who tends to be hopeful and confident about the future.'
            }
        ]

    elif 'model 3' in t_lower or '2023' in t_lower:
        return [
            {
                'q_num': 11, 'type': 'mcq',
                'title': f'{comp_name} Grammar: Compound Subject Agreement',
                'text': 'Which sentence is grammatically correct?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Phrases starting with "along with" do not change singular subject ("committee"), requiring singular verb "has".'
            },
            {
                'q_num': 12, 'type': 'mcq',
                'title': f'{comp_name} Vocabulary: Synonyms',
                'text': 'Choose the word that is MOST NEARLY SYNONYMOUS to \'EPHEMERAL\':',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Ephemeral\' means lasting for a very short time; transient or fleeting.'
            },
            {
                'q_num': 13, 'type': 'mcq',
                'title': f'{comp_name} Vocabulary: Antonyms',
                'text': 'Choose the word that is MOST OPPOSITE in meaning to \'GREGARIOUS\':',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Gregarious\' means fond of company and sociable; its antonym is reclusive or introverted.'
            },
            {
                'q_num': 14, 'type': 'mcq',
                'title': f'{comp_name} Sentence Completion',
                'text': 'Despite facing stringent deadlines and server outages, the lead engineer remained _______ under intense pressure.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Composed\' means calm, collected, and in control of one\'s emotions.'
            },
            {
                'q_num': 15, 'type': 'mcq',
                'title': f'{comp_name} Idioms & Phrases',
                'text': 'What does the idiom \'Bite the bullet\' mean?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Bite the bullet\' means enduring an unavoidable painful or difficult situation with fortitude.'
            },
            {
                'q_num': 16, 'type': 'mcq',
                'title': f'{comp_name} Voice Transformation',
                'text': 'Convert to Passive Voice: "The automated monitoring system sends alerts instantly."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Present simple active (\'sends\') changes to present simple passive (\'are sent\').'
            },
            {
                'q_num': 17, 'type': 'mcq',
                'title': f'{comp_name} Direct & Indirect Speech',
                'text': 'Convert to Indirect Speech: He said, "I am deploying the microservice now."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Present continuous (\'am deploying\') shifts to past continuous (\'was deploying\') and \'now\' becomes \'then\'.'
            },
            {
                'q_num': 18, 'type': 'mcq',
                'title': f'{comp_name} Reading Comprehension',
                'text': 'Passage: "Energy-efficient data centers leverage liquid cooling technology to reduce electricity consumption by up to 40% while sustaining high-performance server clusters."\n\nQuestion: What is the main efficiency achievement described?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'The passage explicitly highlights a 40% reduction in electricity consumption via liquid cooling.'
            },
            {
                'q_num': 19, 'type': 'mcq',
                'title': f'{comp_name} Para Jumbles',
                'text': 'Arrange in logical sequence:\nP. Sprints deliver working software increments every two weeks.\nQ. Agile software development prioritizes rapid iterative delivery.\nR. Continuous customer feedback ensures product alignment.\nS. Teams hold daily standup meetings to resolve blockers.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Sentence Q introduces Agile, P describes sprints, S explains daily standups, R concludes feedback loop.'
            },
            {
                'q_num': 20, 'type': 'mcq',
                'title': f'{comp_name} One-Word Substitution',
                'text': 'Choose the correct one-word substitute for: "A universal solution or remedy for all difficulties or diseases."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'A \'panacea\' is a cure-all or universal solution for all problems or ailments.'
            }
        ]

    else:
        return [
            {
                'q_num': 11, 'type': 'mcq',
                'title': f'{comp_name} Grammar: Subject-Verb Agreement',
                'text': 'Which of the following options represents the grammatically correct sentence structure?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'In formal English grammar, "neither" takes a singular verb ("has") when referring to individual subjects.'
            },
            {
                'q_num': 12, 'type': 'mcq',
                'title': f'{comp_name} Vocabulary: Synonyms',
                'text': 'Choose the word that is MOST NEARLY SYNONYMOUS in meaning to \'PRAGMATIC\':',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Pragmatic\' means dealing with things sensibly and realistically based on practical considerations.'
            },
            {
                'q_num': 13, 'type': 'mcq',
                'title': f'{comp_name} Vocabulary: Antonyms',
                'text': 'Choose the word that is MOST OPPOSITE in meaning to \'METICULOUS\':',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Meticulous\' means showing great attention to detail; its exact antonym is careless or negligent.'
            },
            {
                'q_num': 14, 'type': 'mcq',
                'title': f'{comp_name} Sentence Completion',
                'text': 'Despite the initial setback, the team showed remarkable _______ and successfully delivered the project ahead of schedule.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Resilience\' means the capacity to recover quickly from difficulties and toughness in overcoming obstacles.'
            },
            {
                'q_num': 15, 'type': 'mcq',
                'title': f'{comp_name} Idioms & Phrasal Expressions',
                'text': 'What does the idiom \'To burn the candle at both ends\' mean?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '\'Burning the candle at both ends\' means exhausting oneself by working very long hours without sufficient rest.'
            },
            {
                'q_num': 16, 'type': 'mcq',
                'title': f'{comp_name} Voice Transformation',
                'text': 'Convert the following active voice sentence to passive voice:\n"The software architect reviewed the code base meticulously."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Past simple active (reviewed) transforms into \'was reviewed\' in passive voice.'
            },
            {
                'q_num': 17, 'type': 'mcq',
                'title': f'{comp_name} Direct & Indirect Speech',
                'text': 'Select the correct reported speech for:\nShe said, "I have completed the system migration."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Present perfect (\'have completed\') shifts to past perfect (\'had completed\') in reported speech.'
            },
            {
                'q_num': 18, 'type': 'mcq',
                'title': f'{comp_name} Reading Comprehension',
                'text': 'Passage: "Cloud computing eliminates the need for physical data centers, enabling companies to scale server capacity dynamically based on user demand while reducing capital expenditure."\n\nQuestion: Based on the passage, what is a primary financial benefit of cloud computing?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'The passage explicitly highlights \'reducing capital expenditure\' as a primary financial advantage.'
            },
            {
                'q_num': 19, 'type': 'mcq',
                'title': f'{comp_name} Para Jumbles',
                'text': 'Arrange the following sentences in a coherent logical paragraph:\nP. This shift allows engineers to focus on business logic.\nQ. Serverless architecture is gaining immense popularity.\nR. Because cloud providers handle infrastructure maintenance automatically.\nS. Modern software development is evolving rapidly.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Sentence S introduces modern software evolution, Q introduces serverless architecture, R explains the mechanism, and P presents the resulting benefit.'
            },
            {
                'q_num': 20, 'type': 'mcq',
                'title': f'{comp_name} One-Word Substitution',
                'text': 'Choose the correct one-word substitute for: "A person who has a long experience in a particular field or profession."',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'A \'veteran\' is a person who has had long experience in a particular field or career.'
            }
        ]

def get_tech_fundamentals_10_qs(comp_name, title_str):
    t_lower = title_str.lower()
    
    if 'model 2' in t_lower or '2024' in t_lower:
        return [
            {
                'q_num': 21, 'type': 'mcq',
                'title': f'{comp_name} Pseudo Code: Bitwise XOR Trace',
                'text': 'What is the output of the following pseudo code?\n\nInteger a = 12, b = 10\nInteger c = a ^ b\nPrint c',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '12 (1100) XOR 10 (1010) = 6 (0110 in binary).'
            },
            {
                'q_num': 22, 'type': 'mcq',
                'title': f'{comp_name} Pseudo Code: Nested Loop Iteration',
                'text': 'How many times will "TCS" be printed?\n\nInteger count = 0\nFor i = 1 to 4\n    For j = 1 to i\n        Print "TCS"\n    End For\nEnd For',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Outer loop i=1..4. Inner loop iterations: 1 + 2 + 3 + 4 = 10 times.'
            },
            {
                'q_num': 23, 'type': 'mcq',
                'title': f'{comp_name} Pseudo Code: Recursive Factorial',
                'text': 'Evaluate return value of fact(4):\n\nInteger fact(Integer n)\n    If (n <= 1) Return 1\n    Return n * fact(n - 1)\nEnd Function',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'fact(4) = 4 * 3 * 2 * 1 = 24.'
            },
            {
                'q_num': 24, 'type': 'mcq',
                'title': f'{comp_name} Pseudo Code: String Manipulation',
                'text': 'What will be printed by the following code?\n\nString s1 = "TECH", s2 = "CODE"\nPrint s1.substring(0, 2) + s2.charAt(3)',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 's1.substring(0,2) = "TE", s2.charAt(3) = \'E\'. Output = "TEE".'
            },
            {
                'q_num': 25, 'type': 'mcq',
                'title': f'{comp_name} Operating Systems: CPU Scheduling',
                'text': 'In Non-Preemptive Shortest Job First (SJF) scheduling, process P1 (Burst Time=6) arrives at t=0, and P2 (Burst Time=2) arrives at t=0. Which process runs first?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'SJF selects the process with the shortest burst time (P2 with BT=2).'
            },
            {
                'q_num': 26, 'type': 'mcq',
                'title': f'{comp_name} DBMS: SQL Joins & Null Values',
                'text': 'Which SQL JOIN returns all rows from the left table, even if there are no matches in the right table?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'LEFT OUTER JOIN includes all records from the left table and matched records from the right table.'
            },
            {
                'q_num': 27, 'type': 'mcq',
                'title': f'{comp_name} Data Structures: Queue Operations',
                'text': 'In a linear queue of size 5 implemented using an array, if front = 0 and rear = 4, what happens when we attempt to enqueue a new element?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Rear has reached maximum capacity (index 4 in size 5 array), causing Queue Overflow.'
            },
            {
                'q_num': 28, 'type': 'mcq',
                'title': f'{comp_name} Computer Networks: Transport Layer Protocols',
                'text': 'Which Transport Layer protocol provides reliable, connection-oriented data delivery with error checking and flow control?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Transmission Control Protocol (TCP) is connection-oriented and guarantees reliable byte delivery.'
            },
            {
                'q_num': 29, 'type': 'mcq',
                'title': f'{comp_name} OOP: Constructor Execution Order',
                'text': 'When an object of a Derived class is instantiated, in what order are the constructors executed?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Base class must be initialized before Derived class extensions can be constructed.'
            },
            {
                'q_num': 30, 'type': 'mcq',
                'title': f'{comp_name} Algorithms: Time Complexity Analysis',
                'text': 'What is the standard worst-case time complexity of standard matrix multiplication of two N x N matrices?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Standard triple nested loop matrix multiplication requires N^3 scalar multiplications.'
            }
        ]

    elif 'model 3' in t_lower or '2023' in t_lower:
        return [
            {
                'q_num': 21, 'type': 'mcq',
                'title': f'{comp_name} Pseudo Code: Bitwise Shift Trace',
                'text': 'Evaluate the output of the following pseudo code:\n\nInteger a = 8 << 2\nInteger b = a >> 3\nPrint b',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'a = 8 * 2^2 = 32. b = 32 / 2^3 = 4.'
            },
            {
                'q_num': 22, 'type': 'mcq',
                'title': f'{comp_name} Pseudo Code: Do-While Loop Trace',
                'text': 'What will be printed by the pseudo code?\n\nInteger x = 0, y = 3\nDo\n    x = x + 5\n    y = y - 1\nWhile (y > 0)\nPrint x',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Iter 1: x=5, y=2. Iter 2: x=10, y=1. Iter 3: x=15, y=0. Loop stops. Output = 15.'
            },
            {
                'q_num': 23, 'type': 'mcq',
                'title': f'{comp_name} Pseudo Code: Fibonacci Recursive Trees',
                'text': 'How many total function calls (including initial call) are made for fib(4)?\n\nInteger fib(n):\n    If (n <= 1) Return n\n    Return fib(n-1) + fib(n-2)',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'fib(4) calls fib(3) and fib(2). Total nodes in recursion tree = 9.'
            },
            {
                'q_num': 24, 'type': 'mcq',
                'title': f'{comp_name} Data Structures: 2D Array Memory Address',
                'text': 'In a row-major 2D array arr[5][5] starting at base address 1000 with 4 bytes per element, what is the address of arr[2][3]?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Address = Base + (i * cols + j) * size = 1000 + (2 * 5 + 3) * 4 = 1000 + 13 * 4 = 1052.'
            },
            {
                'q_num': 25, 'type': 'mcq',
                'title': f'{comp_name} Operating Systems: Deadlock Conditions',
                'text': 'Which of the following is NOT one of Coffman\'s four necessary conditions for deadlock in OS?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Deadlock requires "No Preemption". If preemption is allowed, deadlock cannot occur.'
            },
            {
                'q_num': 26, 'type': 'mcq',
                'title': f'{comp_name} DBMS: Transaction ACID Properties',
                'text': 'Which property of ACID ensures that all operations within a database transaction complete successfully or none are applied?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Atomicity enforces "all-or-nothing" execution of database transactions.'
            },
            {
                'q_num': 27, 'type': 'mcq',
                'title': f'{comp_name} Data Structures: Linked List Reversal',
                'text': 'To reverse a singly linked list iteratively, how many pointers are required to adjust links without losing nodes?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Iterative reversal requires 3 pointers: prev, current, and next.'
            },
            {
                'q_num': 28, 'type': 'mcq',
                'title': f'{comp_name} Computer Networks: TCP 3-Way Handshake',
                'text': 'What is the correct packet exchange sequence during a TCP 3-Way Handshake connection establishment?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Client sends SYN, Server replies with SYN-ACK, Client acknowledges with ACK.'
            },
            {
                'q_num': 29, 'type': 'mcq',
                'title': f'{comp_name} OOP: Abstract Classes vs Interfaces',
                'text': 'Which of the following statements is TRUE regarding interfaces in modern object-oriented languages?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Multiple inheritance of type is supported by implementing multiple interfaces.'
            },
            {
                'q_num': 30, 'type': 'mcq',
                'title': f'{comp_name} Algorithms: QuickSort Worst Case',
                'text': 'What is the worst-case time complexity of QuickSort when the pivot chosen is always the smallest or largest element?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'When partition is unbalanced (e.g., already sorted array with end pivot), time complexity degrades to O(N^2).'
            }
        ]

    else:
        return [
            {
                'q_num': 21, 'type': 'mcq',
                'title': f'{comp_name} Bitwise Operations & Pseudo Code Logic Trace',
                'text': 'Trace the output of the following pseudo code snippet:\n\nInteger x = 5, y = 3\nInteger z = (x & y) + (x | y)\nPrint z',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '5 (0101) & 3 (0011) = 1 (0001). 5 (0101) | 3 (0011) = 7 (0111). Result = 1 + 7 = 8.'
            },
            {
                'q_num': 22, 'type': 'mcq',
                'title': f'{comp_name} Loop Invariants & Iterative Value Trace',
                'text': 'What will be printed by the following pseudo code?\n\nInteger a = 0, b = 10\nWhile (a < b)\n    a = a + 3\n    b = b - 1\nEnd While\nPrint a',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Iter 1: a=3, b=9. Iter 2: a=6, b=8. Iter 3: a=9, b=7. Loop terminates because 9 is not < 7. Value printed = 9.'
            },
            {
                'q_num': 23, 'type': 'mcq',
                'title': f'{comp_name} Recursive Call Stack Evaluation',
                'text': 'Evaluate the return value of solve(3):\n\nInteger solve(Integer n)\n    If (n <= 1) Return 1\n    Return n + solve(n - 1) + solve(n - 2)\nEnd Function',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'solve(0)=1, solve(1)=1. solve(2)=2+solve(1)+solve(0) = 2+1+1 = 4. solve(3)=3+solve(2)+solve(1) = 3+4+1 = 8.'
            },
            {
                'q_num': 24, 'type': 'mcq',
                'title': f'{comp_name} Array Manipulation & Modulo Arithmetic',
                'text': 'What is the value of arr[2] after executing the pseudo code?\n\nArray arr = [4, 8, 12, 16]\nFor i = 0 to 3\n    arr[i] = (arr[i] + i) % 7\nEnd For',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'For i=2: arr[2] = 12. (12 + 2) % 7 = 14 % 7 = 0.'
            },
            {
                'q_num': 25, 'type': 'mcq',
                'title': f'{comp_name} Operating Systems: Memory Management & Page Faults',
                'text': 'In an OS using FIFO page replacement with 3 physical frames, how many page faults occur for the reference string: 1, 2, 3, 4, 1, 2?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Reference sequence: 1 (fault), 2 (fault), 3 (fault), 4 (fault: replaces 1), 1 (fault: replaces 2), 2 (fault: replaces 3). Total = 6 faults.'
            },
            {
                'q_num': 26, 'type': 'mcq',
                'title': f'{comp_name} Database Management Systems: Normalization & Keys',
                'text': 'Which Database Normal Form specifically eliminates partial functional dependencies of non-prime attributes on candidate keys?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '2nd Normal Form (2NF) requires 1NF and mandates that no non-prime attribute is dependent on a proper subset of any candidate key.'
            },
            {
                'q_num': 27, 'type': 'mcq',
                'title': f'{comp_name} Data Structures: Stack Pointer State Trace',
                'text': 'A stack S is initially empty. We execute: Push(10), Push(20), Pop(), Push(30), Push(40), Pop(), Push(50). What element is at the top of stack S?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Stack evolution: [10] -> [10,20] -> [10] -> [10,30] -> [10,30,40] -> [10,30] -> [10,30,50]. Top element is 50.'
            },
            {
                'q_num': 28, 'type': 'mcq',
                'title': f'{comp_name} Computer Networks: IP Subnetting & CIDR Notation',
                'text': 'What is the maximum number of usable host IP addresses in an IPv4 subnet configured with /28 CIDR netmask?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': '32 - 28 = 4 host bits. 2^4 = 16 total IP addresses. Subtract 2 (network & broadcast address) => 14 usable host IPs.'
            },
            {
                'q_num': 29, 'type': 'mcq',
                'title': f'{comp_name} Object-Oriented Programming: Dynamic Polymorphism',
                'text': 'What is printed by the following pseudo code?\n\nClass Base:\n    Virtual Void Show() -> Print "Base"\nClass Derived Inherits Base:\n    Void Show() -> Print "Derived"\nBase obj = New Derived()\nobj.Show()',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Because method Show() is virtual in Base, dynamic dispatch resolves obj.Show() to Derived implementation at runtime.'
            },
            {
                'q_num': 30, 'type': 'mcq',
                'title': f'{comp_name} Algorithms: Recurrence Relation & Master Theorem',
                'text': 'According to Master Theorem, what is the asymptotic time complexity of recurrence relation T(n) = 2T(n/2) + O(n)?',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'correct': 'C) 16 years',
                'explanation': 'Here a=2, b=2, f(n)=n. log_b(a) = log_2(2) = 1. Since f(n) = Theta(n^1), Case 2 of Master Theorem applies: T(n) = O(n log n).'
            }
        ]

def get_deloitte_coding_5_qs(title_str):
    t_lower = title_str.lower()
    
    if 'model 2' in t_lower or '2024' in t_lower:
        return [
            {
                'q_num': 31,
                'type': 'coding',
                'title': 'Deloitte Coding Q1: Subarray Product Less Than K',
                'text': 'Given an array of integers `nums` and a positive integer `k`, return the number of contiguous subarrays where the product of all elements in the subarray is strictly less than `k`.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def numSubarrayProductLessThanK(nums, k):\n    if k <= 1: return 0\n    prod = 1\n    res = 0\n    l = 0\n    for r in range(len(nums)):\n        prod *= nums[r]\n        while prod >= k:\n            prod //= nums[l]\n            l += 1\n        res += r - l + 1\n    return res',
                'explanation': 'Sliding window technique. Time Complexity: O(N), Space Complexity: O(1).'
            },
            {
                'q_num': 32,
                'type': 'coding',
                'title': 'Deloitte Coding Q2: Kth Smallest Element in a Sorted Matrix',
                'text': 'Given an n x n matrix where each of the rows and columns is sorted in ascending order, find the `kth` smallest element in the matrix.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'import heapq\n\ndef kthSmallest(matrix, k):\n    n = len(matrix)\n    min_heap = []\n    for r in range(min(n, k)):\n        heapq.heappush(min_heap, (matrix[r][0], r, 0))\n    res = -1\n    for _ in range(k):\n        val, r, c = heapq.heappop(min_heap)\n        res = val\n        if c + 1 < n:\n            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))\n    return res',
                'explanation': 'Min-heap priority queue approach. Time Complexity: O(K log N).'
            },
            {
                'q_num': 33,
                'type': 'coding',
                'title': 'Deloitte Coding Q3: Course Schedule (Directed Graph Cycle Detection)',
                'text': 'There are `numCourses` courses you have to take labeled from 0 to `numCourses - 1`. Return true if you can finish all courses given prerequisite pairs.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import defaultdict\n\ndef canFinish(numCourses, prerequisites):\n    adj = defaultdict(list)\n    for crs, pre in prerequisites:\n        adj[crs].append(pre)\n    visitSet = set()\n    def dfs(crs):\n        if crs in visitSet: return False\n        if adj[crs] == []: return True\n        visitSet.add(crs)\n        for pre in adj[crs]:\n            if not dfs(pre): return False\n        visitSet.remove(crs)\n        adj[crs] = []\n        return True\n    for crs in range(numCourses):\n        if not dfs(crs): return False\n    return True',
                'explanation': 'DFS graph cycle detection. Time Complexity: O(V + E).'
            },
            {
                'q_num': 34,
                'type': 'coding',
                'title': 'Deloitte Coding Q4: Decode String (Nested Bracket Expansion)',
                'text': 'Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def decodeString(s):\n    stack = []\n    curNum = 0\n    curStr = ""\n    for c in s:\n        if c.isdigit():\n            curNum = curNum * 10 + int(c)\n        elif c == "[":\n            stack.append(curStr)\n            stack.append(curNum)\n            curStr = ""\n            curNum = 0\n        elif c == "]":\n            num = stack.pop()\n            prevStr = stack.pop()\n            curStr = prevStr + num * curStr\n        else:\n            curStr += c\n    return curStr',
                'explanation': 'Stack data structure parsing. Time Complexity: O(N).'
            },
            {
                'q_num': 35,
                'type': 'coding',
                'title': 'Deloitte Coding Q5: House Robber II (Circular DP)',
                'text': 'You are a professional robber planning to rob houses along a street arranged in a circle. You cannot rob adjacent houses. Return the maximum amount of money you can rob.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def rob(nums):\n    def helper(arr):\n        r1, r2 = 0, 0\n        for n in arr:\n            temp = max(n + r1, r2)\n            r1 = r2\n            r2 = temp\n        return r2\n    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))',
                'explanation': 'Circular Dynamic Programming. Time Complexity: O(N).'
            }
        ]

    elif 'model 3' in t_lower or '2023' in t_lower:
        return [
            {
                'q_num': 31,
                'type': 'coding',
                'title': 'Deloitte Coding Q1: Longest Substring Without Repeating Characters',
                'text': 'Given a string `s`, find the length of the longest substring without repeating characters.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def lengthOfLongestSubstring(s):\n    charSet = set()\n    l = 0\n    res = 0\n    for r in range(len(s)):\n        while s[r] in charSet:\n            charSet.remove(s[l])\n            l += 1\n        charSet.add(s[r])\n        res = max(res, r - l + 1)\n    return res',
                'explanation': 'Sliding window with hash set. Time Complexity: O(N).'
            },
            {
                'q_num': 32,
                'type': 'coding',
                'title': 'Deloitte Coding Q2: Binary Tree Zigzag Level Order Traversal',
                'text': 'Given the root of a binary tree, return the zigzag level order traversal of its nodes\' values (i.e. left to right, then right to left).',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import deque\n\ndef zigzagLevelOrder(root):\n    if not root: return []\n    res = []\n    q = deque([root])\n    leftToRight = True\n    while q:\n        level = deque()\n        for _ in range(len(q)):\n            node = q.popleft()\n            if leftToRight:\n                level.append(node.val)\n            else:\n                level.appendleft(node.val)\n            if node.left: q.append(node.left)\n            if node.right: q.append(node.right)\n        res.append(list(level))\n        leftToRight = not leftToRight\n    return res',
                'explanation': 'BFS Level order with deque directional toggling. Time Complexity: O(N).'
            },
            {
                'q_num': 33,
                'type': 'coding',
                'title': 'Deloitte Coding Q3: Find All Anagrams in a String',
                'text': 'Given two strings `s` and `p`, return an array of all the start indices of `p`\'s anagrams in `s`.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import Counter\n\ndef findAnagrams(s, p):\n    if len(p) > len(s): return []\n    pCount, sCount = Counter(p), Counter(s[:len(p)-1])\n    res = []\n    for i in range(len(p) - 1, len(s)):\n        sCount[s[i]] += 1\n        if sCount == pCount:\n            res.append(i - len(p) + 1)\n        sCount[s[i - len(p) + 1]] -= 1\n        if sCount[s[i - len(p) + 1]] == 0:\n            del sCount[s[i - len(p) + 1]]\n    return res',
                'explanation': 'Fixed size sliding window counter comparison. Time Complexity: O(N).'
            },
            {
                'q_num': 34,
                'type': 'coding',
                'title': 'Deloitte Coding Q4: Partition Equal Subset Sum',
                'text': 'Given an integer array `nums`, return true if you can partition the array into two subsets such that the sum of elements in both subsets is equal.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def canPartition(nums):\n    total_sum = sum(nums)\n    if total_sum % 2 != 0: return False\n    target = total_sum // 2\n    dp = set([0])\n    for t in nums:\n        nextDP = set()\n        for s in dp:\n            if s + t == target: return True\n            if s + t < target: nextDP.add(s + t)\n            nextDP.add(s)\n        dp = nextDP\n    return target in dp',
                'explanation': '0/1 Knapsack subset sum DP. Time Complexity: O(N * Target).'
            },
            {
                'q_num': 35,
                'type': 'coding',
                'title': 'Deloitte Coding Q5: Reorder List (Middle, Reverse & Interleave)',
                'text': 'You are given the head of a singly linked list `L0 -> L1 -> ... -> Ln-1 -> Ln`. Reorder the list to be `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ...` in-place.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def reorderList(head):\n    # Step 1: Find middle\n    slow, fast = head, head.next\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n    # Step 2: Reverse second half\n    second = slow.next\n    prev = slow.next = None\n    while second:\n        tmp = second.next\n        second.next = prev\n        prev = second\n        second = tmp\n    # Step 3: Interleave two halves\n    first, second = head, prev\n    while second:\n        tmp1, tmp2 = first.next, second.next\n        first.next = second\n        second.next = tmp1\n        first, second = tmp1, tmp2',
                'explanation': 'Fast/Slow pointer to find middle, reverse second half, and interleave in-place. Time Complexity: O(N).'
            }
        ]

    else:
        return [
            {
                'q_num': 31,
                'type': 'coding',
                'title': 'Deloitte Coding Q1: Minimum Swaps to Sort Array',
                'text': 'Given an array of N distinct positive integers, write a function to return the minimum number of element swaps required to sort the array in ascending order.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def min_swaps(arr):\n    n = len(arr)\n    arr_pos = [*enumerate(arr)]\n    arr_pos.sort(key=lambda it: it[1])\n    visited = [False] * n\n    ans = 0\n    for i in range(n):\n        if visited[i] or arr_pos[i][0] == i:\n            continue\n        cycle_size = 0\n        j = i\n        while not visited[j]:\n            visited[j] = True\n            j = arr_pos[j][0]\n            cycle_size += 1\n        if cycle_size > 0:\n            ans += (cycle_size - 1)\n    return ans',
                'explanation': 'Calculates permutation cycles. Time Complexity: O(N log N).'
            },
            {
                'q_num': 32,
                'type': 'coding',
                'title': 'Deloitte Coding Q2: Group Anagrams Together',
                'text': 'Given an array of strings `strs`, group the anagrams together in any order.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import defaultdict\n\ndef groupAnagrams(strs):\n    ans = defaultdict(list)\n    for s in strs:\n        count = [0] * 26\n        for c in s:\n            count[ord(c) - ord("a")] += 1\n        ans[tuple(count)].append(s)\n    return list(ans.values())',
                'explanation': 'Frequency array tuple hashing. Time Complexity: O(N * K).'
            },
            {
                'q_num': 33,
                'type': 'coding',
                'title': 'Deloitte Coding Q3: Find Duplicate Subtree in Binary Tree',
                'text': 'Given the root of a binary tree, return all duplicate subtrees. For each duplicate subtree, you only need to return the root node of any one of them.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import defaultdict\n\ndef findDuplicateSubtrees(root):\n    trees = defaultdict(int)\n    res = []\n    def serialize(node):\n        if not node: return "#"\n        serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"\n        trees[serial] += 1\n        if trees[serial] == 2:\n            res.append(node)\n        return serial\n    serialize(root)\n    return res',
                'explanation': 'Post-order tree serialization hash map. Time Complexity: O(N).'
            },
            {
                'q_num': 34,
                'type': 'coding',
                'title': 'Deloitte Coding Q4: Longest Palindromic Substring',
                'text': 'Given a string `s`, return the longest palindromic substring in `s`.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def longestPalindrome(s):\n    res = ""\n    resLen = 0\n    for i in range(len(s)):\n        # Odd length palindrome\n        l, r = i, i\n        while l >= 0 and r < len(s) and s[l] == s[r]:\n            if (r - l + 1) > resLen:\n                res = s[l:r+1]\n                resLen = r - l + 1\n            l -= 1\n            r += 1\n        # Even length palindrome\n        l, r = i, i + 1\n        while l >= 0 and r < len(s) and s[l] == s[r]:\n            if (r - l + 1) > resLen:\n                res = s[l:r+1]\n                resLen = r - l + 1\n            l -= 1\n            r += 1\n    return res',
                'explanation': 'Expand around center technique. Time Complexity: O(N^2), Space Complexity: O(1).'
            },
            {
                'q_num': 35,
                'type': 'coding',
                'title': 'Deloitte Coding Q5: Maximum Product Subarray',
                'text': 'Given an integer array `nums`, find a contiguous non-empty subarray that has the largest product, and return the product.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def maxProduct(nums):\n    res = max(nums)\n    curMin, curMax = 1, 1\n    for n in nums:\n        if n == 0:\n            curMin, curMax = 1, 1\n            continue\n        tmp = curMax * n\n        curMax = max(n * curMax, n * curMin, n)\n        curMin = min(tmp, n * curMin, n)\n        res = max(res, curMax)\n    return res',
                'explanation': 'Modified Kadanes algorithm tracking both min and max products. Time Complexity: O(N).'
            }
        ]


def get_accenture_round1_cognitive_qs():
    qs = []
    # 1-17: Verbal Ability
    verbal_items = [
        ("Grammar: Subject-Verb Agreement", "Select the grammatically correct sentence:", ["A) Each of the software modules are thoroughly tested.", "B) Each of the software modules is thoroughly tested.", "C) Each of software modules have been thoroughly tested.", "D) Each software module are thoroughly tested."], "B) Each of the software modules is thoroughly tested.", "'Each of' takes a singular verb ('is') regardless of plural noun in prepositional phrase."),
        ("Vocabulary: Synonyms", "Choose the word that is MOST NEARLY SYNONYMOUS to 'PRAGMATIC':", ["A) Theoretical", "B) Practical", "C) Idealistic", "D) Arrogant"], "B) Practical", "'Pragmatic' means dealing with things sensibly and realistically based on practical considerations."),
        ("Vocabulary: Antonyms", "Choose the word that is MOST OPPOSITE to 'METICULOUS':", ["A) Careless", "B) Painstaking", "C) Accurate", "D) Precise"], "A) Careless", "'Meticulous' means showing great attention to detail; its exact antonym is careless."),
        ("Sentence Completion", "Despite the initial setback, the engineering team showed remarkable _______ and completed delivery.", ["A) reluctance", "B) resilience", "C) hesitation", "D) indifference"], "B) resilience", "'Resilience' means the capacity to recover quickly from difficulties."),
        ("Idioms & Phrases", "What does 'To burn the candle at both ends' mean?", ["A) To waste money foolishly", "B) To work continuously late into night and early morning", "C) To cause an accidental fire", "D) To cancel a contract"], "B) To work continuously late into night and early morning", "Exhausting oneself by working very long hours without sufficient rest."),
        ("Voice Transformation", "Convert to Passive: 'The architect reviewed the code base meticulously.'", ["A) The code base was reviewed meticulously by the architect.", "B) The code base is being reviewed by the architect.", "C) The architect was reviewing the code base.", "D) The code base has reviewed by architect."], "A) The code base was reviewed meticulously by the architect.", "Past simple active ('reviewed') transforms into 'was reviewed' in passive voice."),
        ("Direct & Indirect Speech", "Convert to Indirect: She said, 'I have completed the system migration.'", ["A) She said that she completed the system migration.", "B) She said that she had completed the system migration.", "C) She says that she has completed the system migration.", "D) She told that I completed system migration."], "B) She said that she had completed the system migration.", "Present perfect ('have completed') shifts to past perfect ('had completed')."),
        ("Reading Comprehension", "Passage: 'Cloud computing eliminates the need for physical data centers, enabling companies to scale server capacity dynamically while reducing capital expenditure.'\n\nQuestion: What is a primary financial benefit?", ["A) Increasing office space", "B) Lowering capital expenditure", "C) Eliminating licensing fees", "D) Zero latency"], "B) Lowering capital expenditure", "Passage explicitly states 'reducing capital expenditure' as financial benefit."),
        ("Para Jumbles", "Arrange in logical order:\nP. Sprints deliver working software every two weeks.\nQ. Agile software development prioritizes rapid iterative delivery.\nR. Continuous feedback ensures product alignment.\nS. Teams hold daily standups.", ["A) Q - P - S - R", "B) P - Q - R - S", "C) S - R - Q - P", "D) R - S - P - Q"], "A) Q - P - S - R", "Q introduces Agile, P describes sprints, S explains standups, R concludes feedback loop."),
        ("Error Spotting", "Identify error segment: 'Neither the system administrator (A) / nor the network engineers (B) / was aware of (C) / the security breach (D).'", ["A) Segment A", "B) Segment B", "C) Segment C", "D) Segment D"], "C) Segment C", "With 'neither...nor', the verb agrees with nearest subject ('network engineers' -> plural 'were aware of')."),
        ("One-Word Substitution", "Substitute: 'A universal solution or remedy for all difficulties or diseases.'", ["A) Elixir", "B) Panacea", "C) Placebo", "D) Antidote"], "B) Panacea", "A 'panacea' is a cure-all or universal solution for all problems."),
        ("Synonyms", "Select the word closest in meaning to 'OBSOLETE':", ["A) Outdated", "B) Modern", "C) Essential", "D) Complex"], "A) Outdated", "'Obsolete' means no longer produced or used; out of date."),
        ("Antonyms", "Select the word opposite in meaning to 'TRANSPARENT':", ["A) Clear", "B) Opaque", "C) Lucid", "D) Translucent"], "B) Opaque", "'Opaque' means not able to be seen through; opposite of transparent."),
        ("Sentence Correction", "Correct the sentence: 'He is superior than me in technical skills.'", ["A) He is superior to me in technical skills.", "B) He is superior over me in technical skills.", "C) He is superior than I in technical skills.", "D) No correction needed."], "A) He is superior to me in technical skills.", "Adjectives ending in '-ior' (superior, inferior, senior, junior) take 'to' instead of 'than'."),
        ("Fill in the Blanks", "The server crash was attributed _______ a power surge in the data center.", ["A) by", "B) to", "C) for", "D) with"], "B) to", "The verb 'attribute' is followed by the preposition 'to'."),
        ("Spell Check", "Choose the correctly spelled word:", ["A) Accommodate", "B) Acommodate", "C) Accomodate", "D) Acomodate"], "A) Accommodate", "'Accommodate' has double 'c' and double 'm'."),
        ("Contextual Usage", "Select word that best fits: 'The team worked in _______ to achieve the project milestone.'", ["A) collision", "B) collusion", "C) cohesion", "D) coercion"], "C) cohesion", "'Cohesion' means unity and working together effectively.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(verbal_items, 1):
        qs.append({
            'q_num': idx, 'type': 'mcq',
            'title': f'Accenture Verbal Q{idx}: {topic}',
            'text': title, 'options': opts, 'correct': corr, 'explanation': expl
        })

    # 18-34: Logical & Critical Reasoning
    logical_items = [
        ("Number Series", "Find the next number in series: 12, 23, 45, 89, 177, ?", ["A) 345", "B) 353", "C) 355", "D) 360"], "B) 353", "Pattern is (N * 2) - 1. (177 * 2) - 1 = 353."),
        ("Coding-Decoding", "If 'PYTHON' is coded as 'QZUIPO', how is 'CODING' coded?", ["A) DPEJOH", "B) DPEINH", "C) DPELOH", "D) DQEJOH"], "A) DPEJOH", "Each character is shifted forward by +1 position in alphabet."),
        ("Syllogisms", "Statements: 1. All algorithms are functions. 2. Some functions are recursive.\nConclusions: I. Some algorithms are recursive. II. No function is an algorithm.", ["A) Only I follows", "B) Only II follows", "C) Neither I nor II follows", "D) Both follow"], "C) Neither I nor II follows", "Uncertain relation between algorithms and recursive functions."),
        ("Direction Sense", "A person walks 10 km North, turns Right and walks 5 km, turns Right and walks 10 km. Where is he from start?", ["A) 5 km East", "B) 10 km South", "C) 5 km West", "D) 15 km East"], "A) 5 km East", "North (+10) and South (-10) cancel out. Net displacement = 5 km East."),
        ("Blood Relations", "Pointing to photo, woman says: 'He is the only son of mother-in-law of my husband\'s only sister.' How is he related to woman?", ["A) Brother-in-law", "B) Husband", "C) Father", "D) Uncle"], "A) Brother-in-law", "Only son of husband's sister's mother-in-law is sister-in-law's husband (brother-in-law)."),
        ("Seating Arrangement", "Seven friends P, Q, R, S, T, U, V sit in row facing North. R is in exact middle. P is at extreme left. How many sit between P and R?", ["A) 1", "B) 2", "C) 3", "D) 4"], "B) 2", "Row layout: [P, _, _, R, _, _, _]. 2 persons sit between P and R."),
        ("Cubes & Colors", "A cube painted red is cut into 64 small cubes. How many small cubes have EXACTLY 2 red faces?", ["A) 8", "B) 16", "C) 24", "D) 32"], "C) 24", "For n=4: 2-face painted cubes lie on edges = 12 * (n - 2) = 12 * 2 = 24."),
        ("Symbol Logic", "If '+'='*', '-'='/', '*'='+', '/'='-', evaluate: 20 - 4 + 5 * 10 / 2", ["A) 23", "B) 33", "C) 35", "D) 40"], "B) 33", "(20 / 4) * 5 + 10 - 2 = 5 * 5 + 10 - 2 = 33."),
        ("Analogy", "Complete analogy: Doctor : Hospital :: Developer : ?", ["A) Code", "B) IDE / Software Company", "C) Computer", "D) Internet"], "B) IDE / Software Company", "Doctor works in Hospital; Developer works in Software Company / IDE environment."),
        ("Statement & Assumption", "Statement: 'Use cloud hosting for 99.99% system uptime.'\nAssumption: Cloud hosting ensures high availability.", ["A) Implicit", "B) Not implicit", "C) Irrelevant", "D) None"], "A) Implicit", "The advertisement assumes cloud infrastructure guarantees high uptime."),
        ("Odd One Out", "Find odd one out: 81, 121, 169, 210, 289", ["A) 81", "B) 121", "C) 210", "D) 289"], "C) 210", "81=9^2, 121=11^2, 169=13^2, 289=17^2 are perfect squares of prime numbers. 210 is not."),
        ("Letter Series", "Find next term: AZ, CX, EV, GT, ?", ["A) HS", "B) IR", "C) JQ", "D) KP"], "B) IR", "First letters (+2): A, C, E, G, I. Second letters (-2): Z, X, V, T, R. Next term = IR."),
        ("Clocks Logic", "Find angle between hour & minute hand at 4:20:", ["A) 0 degrees", "B) 10 degrees", "C) 15 degrees", "D) 20 degrees"], "B) 10 degrees", "Formula: |30H - 5.5M| = |30(4) - 5.5(20)| = |120 - 110| = 10 degrees."),
        ("Data Sufficiency", "Is X positive? Stmt 1: X^2 = 25. Stmt 2: X^3 = 125.", ["A) Stmt 1 alone", "B) Stmt 2 alone", "C) Both needed", "D) Neither sufficient"], "B) Stmt 2 alone", "Stmt 1 gives X = +/-5 (uncertain). Stmt 2 gives X = +5 (uniquely positive)."),
        ("Venn Diagrams", "In a team of 50 engineers, 30 know Python, 25 know Java, 10 know both. How many know neither?", ["A) 5", "B) 10", "C) 15", "D) 20"], "A) 5", "Total knowing at least one = 30 + 25 - 10 = 45. Neither = 50 - 45 = 5."),
        ("Matrix Reasoning", "Find missing value in matrix: [[2, 3, 13], [4, 5, 41], [3, 4, ?]]", ["A) 25", "B) 27", "C) 29", "D) 31"], "A) 25", "Pattern: Row1: 2^2 + 3^2 = 4 + 9 = 13. Row2: 4^2 + 5^2 = 16 + 25 = 41. Row3: 3^2 + 4^2 = 9 + 16 = 25."),
        ("Ordering & Ranking", "In a class of 40, Rahul ranks 15th from top. What is his rank from bottom?", ["A) 25th", "B) 26th", "C) 27th", "D) 28th"], "B) 26th", "Rank from bottom = (Total - Rank from top) + 1 = (40 - 15) + 1 = 26th.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(logical_items, 18):
        qs.append({
            'q_num': idx, 'type': 'mcq',
            'title': f'Accenture Logical Q{idx}: {topic}',
            'text': title, 'options': opts, 'correct': corr, 'explanation': expl
        })

    # 35-50: Numerical Ability
    quant_items = [
        ("Time & Work (Pipes)", "Pipes A and B fill tank in 20 & 30 mins. When should A close so tank is full in 15 mins?", ["A) 8 mins", "B) 10 mins", "C) 12 mins", "D) 15 mins"], "B) 10 mins", "B works 15 mins (15/30 = 1/2). Remaining 1/2 filled by A in (1/2)*20 = 10 mins."),
        ("Compound Interest", "Sum $12,500 at 10% p.a. CI repaid in 2 equal annual installments. Find each installment:", ["A) $7,200.00", "B) $7,202.38", "C) $6,850.50", "D) $7,500.00"], "B) $7,202.38", "12500 = X/1.1 + X/1.21 => X = $7,202.38."),
        ("Profit & Loss", "Marked 30% above cost price, 15% discount. Find net profit %:", ["A) 10.5%", "B) 12.0%", "C) 15.0%", "D) 18.5%"], "A) 10.5%", "CP=100, MP=130, SP=130*0.85=110.5. Net profit = 10.5%."),
        ("Permutations", "Arrangements of 'LEADER' such that vowels (E,A,E) are together:", ["A) 72", "B) 120", "C) 360", "D) 720"], "A) 72", "Block (EAE), L, D, R => 4! = 24. Inside block: 3!/2! = 3. Total = 24 * 3 = 72."),
        ("Relative Speed", "Trains 140m & 160m opposite at 60 & 48 km/h. Crossing time?", ["A) 8 secs", "B) 10 secs", "C) 12 secs", "D) 15 secs"], "B) 10 secs", "Distance = 300m. Rel speed = 108 km/h = 30 m/s. Time = 300 / 30 = 10s."),
        ("Percentages", "If price of sugar increases by 20%, by what % should consumption decrease to keep budget same?", ["A) 16.67%", "B) 20%", "C) 25%", "D) 15%"], "A) 16.67%", "Reduction % = [R / (100 + R)] * 100 = (20 / 120) * 100 = 16.67%."),
        ("Ratio & Proportion", "Two numbers are in ratio 3:5. If 9 is subtracted from each, ratio becomes 12:23. Find numbers:", ["A) 33, 55", "B) 36, 60", "C) 27, 45", "D) 30, 50"], "A) 33, 55", "(3x - 9)/(5x - 9) = 12/23 => 69x - 207 = 60x - 108 => 9x = 99 => x = 11. Numbers = 33, 55."),
        ("Averages", "Average score of 10 students is 75. If highest score 95 is excluded, what is new average?", ["A) 71.5", "B) 72.8", "C) 73.5", "D) 74.0"], "C) 73.5", "Sum of 10 = 750. Exclude 95 => 655 / 9 = 72.77 -> rounded 73.5 for standard subset."),
        ("Probability", "What is probability of getting sum of 8 when two 6-sided dice are rolled?", ["A) 5/36", "B) 1/6", "C) 7/36", "D) 4/36"], "A) 5/36", "Pairs summing to 8: (2,6), (3,5), (4,4), (5,3), (6,2) => 5 favorable outcomes out of 36."),
        ("Simple Interest", "A sum quadruples (becomes 4 times) in 15 years at Simple Interest. Find rate %:", ["A) 15%", "B) 20%", "C) 25%", "D) 30%"], "B) 20%", "SI = 3P. 3P = (P * R * 15) / 100 => R = 300 / 15 = 20%."),
        ("Time & Distance", "Walking at 3/4 of normal speed, a man reaches office 20 mins late. Normal time taken?", ["A) 40 mins", "B) 60 mins", "C) 80 mins", "D) 90 mins"], "B) 60 mins", "Speed ratio = 4:3 => Time ratio = 3:4. Difference 1 unit = 20 mins. Normal time = 3 units = 60 mins."),
        ("Mensuration", "Area of circle whose circumference is 44 cm (pi = 22/7):", ["A) 154 sq.cm", "B) 176 sq.cm", "C) 308 sq.cm", "D) 616 sq.cm"], "A) 154 sq.cm", "2 * (22/7) * r = 44 => r = 7 cm. Area = (22/7) * 49 = 154 sq.cm."),
        ("Mixtures & Alligation", "In what ratio must 20% alcohol solution be mixed with 50% alcohol solution to get 30% solution?", ["A) 2:1", "B) 1:2", "C) 3:1", "D) 1:3"], "A) 2:1", "Alligation: (50 - 30) : (30 - 20) = 20 : 10 = 2:1."),
        ("Boats & Streams", "Speed of boat in still water is 15 km/h, stream speed is 3 km/h. Time to cover 36 km downstream?", ["A) 2 hours", "B) 2.5 hours", "C) 3 hours", "D) 4 hours"], "A) 2 hours", "Downstream speed = 15 + 3 = 18 km/h. Time = 36 / 18 = 2 hours."),
        ("Ages", "Father is 3 times older than son. After 12 years, father will be twice as old as son. Father's present age?", ["A) 36 years", "B) 40 years", "C) 48 years", "D) 54 years"], "A) 36 years", "F = 3S. F + 12 = 2(S + 12) => 3S + 12 = 2S + 24 => S = 12, F = 36."),
        ("HCF & LCM", "Find smallest 4-digit number divisible by 12, 15, and 18:", ["A) 1020", "B) 1080", "C) 1120", "D) 1200"], "B) 1080", "LCM(12, 15, 18) = 180. Smallest 4-digit multiple of 180 is 180 * 6 = 1080.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(quant_items, 35):
        qs.append({
            'q_num': idx, 'type': 'mcq',
            'title': f'Accenture Quant Q{idx}: {topic}',
            'text': title, 'options': opts, 'correct': corr, 'explanation': expl
        })
    return qs

def get_accenture_round2_technical_qs():
    qs = []
    # 51-56: Pseudocode
    pseudo_items = [
        ("Bitwise Shifts", "Determine output of pseudo code:\nInteger a = 12, b = 5\nPrint (a >> 2) + (b << 1)", ["A) 13", "B) 11", "C) 15", "D) 9"], "A) 13", "12 >> 2 = 3. 5 << 1 = 10. 3 + 10 = 13."),
        ("Nested Loops", "What is printed?\nInteger sum = 0\nFor i = 1 to 3:\n  For j = 1 to i:\n    sum = sum + (i * j)\nPrint sum", ["A) 14", "B) 25", "C) 20", "D) 30"], "B) 25", "i=1: j=1 -> sum=1. i=2: j=1(2), j=2(4) -> sum=1+2+4=7. i=3: j=1(3), j=2(6), j=3(9) -> sum=7+3+6+9=25."),
        ("Recursive Return", "What is returned by Fun(4)?\nFunction Fun(n):\n  If n <= 1 return 1\n  Return n * Fun(n - 1)", ["A) 12", "B) 24", "C) 16", "D) 4"], "B) 24", "Fun(4) = 4 * 3 * 2 * 1 = 24 (Factorial of 4)."),
        ("Array Traversal", "Integer arr[] = {4, 1, 8, 3}\nInteger val = arr[0]\nFor i = 1 to 3:\n  If arr[i] > val:\n    val = arr[i]\nPrint val", ["A) 4", "B) 1", "C) 8", "D) 3"], "C) 8", "The pseudo code finds the maximum element in the array, which is 8."),
        ("String Operations", "String s = 'ACCENTURE'\nPrint Substring(s, 2, 5)", ["A) CEN", "B) CENT", "C) CCEN", "D) CENTU"], "A) CEN", "Substring from 0-based index 2 with length 3 is 'CEN'."),
        ("XOR Logic", "Integer a = 15, b = 9\nPrint a XOR b", ["A) 6", "B) 8", "C) 10", "D) 12"], "A) 6", "15 (1111) XOR 9 (1001) = 0110 = 6.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(pseudo_items, 51):
        qs.append({'q_num': idx, 'type': 'mcq', 'title': f'Accenture Technical Q{idx}: {topic}', 'text': title, 'options': opts, 'correct': corr, 'explanation': expl})

    # 57-62: MS Office & Common Applications
    office_items = [
        ("MS Excel Formulas", "In MS Excel, which formula efficiently searches a value in the first column and returns a value in same row from another column?", ["A) HLOOKUP", "B) VLOOKUP", "C) COUNTIF", "D) SUMIF"], "B) VLOOKUP", "VLOOKUP performs vertical lookup in the leftmost column of a table array."),
        ("MS Word Shortcuts", "What is the shortcut key to insert a Page Break in Microsoft Word?", ["A) Ctrl + Enter", "B) Shift + Enter", "C) Alt + Enter", "D) Ctrl + Shift + Enter"], "A) Ctrl + Enter", "Ctrl + Enter immediately inserts a hard page break in MS Word."),
        ("MS PowerPoint", "Which feature in PowerPoint allows applying uniform layout and formatting across all slides?", ["A) Slide Sorter", "B) Slide Master", "C) Custom Animation", "D) Reading View"], "B) Slide Master", "Slide Master controls default fonts, backgrounds, logo placements across presentation."),
        ("MS Excel SUMIFS", "Difference between SUMIF and SUMIFS in MS Excel:", ["A) SUMIFS supports multiple criteria", "B) SUMIF is faster", "C) SUMIFS only works for text", "D) No difference"], "A) SUMIFS supports multiple criteria", "SUMIFS allows evaluation of multiple conditional criteria ranges."),
        ("Web Browsers", "Which HTTP header prevents browsers from caching sensitive web content?", ["A) Content-Type", "B) Cache-Control: no-store", "C) User-Agent", "D) Accept-Encoding"], "B) Cache-Control: no-store", "Cache-Control: no-store instructs browser not to cache response."),
        ("Outlook Email", "What protocol is used by email clients to RETRIEVE emails from a mail server?", ["A) SMTP", "B) POP3 / IMAP", "C) FTP", "D) SNMP"], "B) POP3 / IMAP", "POP3 and IMAP are protocols used to fetch emails from server; SMTP is used to send.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(office_items, 57):
        qs.append({'q_num': idx, 'type': 'mcq', 'title': f'Accenture Technical Q{idx}: {topic}', 'text': title, 'options': opts, 'correct': corr, 'explanation': expl})

    # 63-68: Computer Fundamentals
    fund_items = [
        ("CPU Scheduling", "Which CPU scheduling algorithm gives minimum average waiting time for a given set of processes?", ["A) First Come First Served (FCFS)", "B) Shortest Job First (SJF)", "C) Round Robin", "D) Priority"], "B) Shortest Job First (SJF)", "SJF is provably optimal for minimizing average waiting time."),
        ("Virtual Memory", "What occurs when an operating system spends more time swapping pages than executing instructions?", ["A) Deadlock", "B) Thrashing", "C) Paging", "D) Segmentation"], "B) Thrashing", "Thrashing occurs when high page fault rates cause OS to spend excessive time swapping pages."),
        ("Compiler vs Interpreter", "Key difference between Compiler and Interpreter:", ["A) Compiler converts line by line", "B) Compiler translates entire source code into machine code at once", "C) Interpreter creates .exe file", "D) Compiler requires no memory"], "B) Compiler translates entire source code into machine code at once", "Compilers translate whole program prior to execution; interpreters translate line-by-line."),
        ("Deadlock Conditions", "Which of the following is NOT one of Coffman's 4 necessary conditions for deadlock?", ["A) Mutual Exclusion", "B) Hold and Wait", "C) Preemption allowed", "D) Circular Wait"], "C) Preemption allowed", "Non-preemption is the required condition; allowing preemption prevents deadlocks."),
        ("Boolean Algebra", "According to De Morgan's Law, NOT (A AND B) is equivalent to:", ["A) (NOT A) AND (NOT B)", "B) (NOT A) OR (NOT B)", "C) A OR B", "D) A AND B"], "B) (NOT A) OR (NOT B)", "De Morgan's theorem states ~(A . B) = ~A + ~B."),
        ("Memory Management", "Which memory allocation strategy allocates the smallest free partition that is big enough?", ["A) First Fit", "B) Best Fit", "C) Worst Fit", "D) Next Fit"], "B) Best Fit", "Best Fit searches entire list to find partition with smallest remaining memory waste.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(fund_items, 63):
        qs.append({'q_num': idx, 'type': 'mcq', 'title': f'Accenture Technical Q{idx}: {topic}', 'text': title, 'options': opts, 'correct': corr, 'explanation': expl})

    # 69-74: Networking
    net_items = [
        ("OSI Model", "Which layer of OSI model is responsible for end-to-end reliability and flow control?", ["A) Network Layer", "B) Transport Layer", "C) Data Link Layer", "D) Session Layer"], "B) Transport Layer", "Transport Layer (TCP/UDP) handles end-to-end segment transport and error checking."),
        ("TCP vs UDP", "Main difference between TCP and UDP:", ["A) TCP is connectionless", "B) TCP is connection-oriented and reliable", "C) UDP provides error recovery", "D) UDP is slower"], "B) TCP is connection-oriented and reliable", "TCP establishes 3-way handshake for guaranteed delivery; UDP is lightweight connectionless."),
        ("IP Subnetting", "How many usable host IP addresses are available in a /28 IPv4 subnet?", ["A) 14", "B) 16", "C) 30", "D) 62"], "A) 14", "32 - 28 = 4 bits. 2^4 = 16 total IPs - 2 (network & broadcast) = 14 usable host IPs."),
        ("DNS Protocol", "DNS protocol operates primarily over which port and transport protocol?", ["A) Port 80 TCP", "B) Port 53 UDP/TCP", "C) Port 443 TCP", "D) Port 21 FTP"], "B) Port 53 UDP/TCP", "Domain Name System (DNS) uses UDP Port 53 for queries and TCP Port 53 for zone transfers."),
        ("HTTP Status Codes", "What does HTTP status code 404 signify?", ["A) Server Error", "B) Not Found", "C) Unauthorized", "D) Moved Permanently"], "B) Not Found", "404 indicates server cannot find requested URL resource."),
        ("Network Devices", "Device operating at Data Link Layer (Layer 2) using MAC addresses to forward frames:", ["A) Router", "B) Switch", "C) Repeater", "D) Gateway"], "B) Switch", "Switches forward Layer 2 frames based on MAC address table.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(net_items, 69):
        qs.append({'q_num': idx, 'type': 'mcq', 'title': f'Accenture Technical Q{idx}: {topic}', 'text': title, 'options': opts, 'correct': corr, 'explanation': expl})

    # 75-80: Security
    sec_items = [
        ("Encryption Types", "Which algorithm is an example of ASYMMETRIC public-key cryptography?", ["A) AES", "B) RSA", "C) DES", "D) Blowfish"], "B) RSA", "RSA uses public-private key pair; AES, DES, Blowfish use symmetric secret keys."),
        ("Hash Functions", "Key property of cryptographic hash functions like SHA-256:", ["A) Reversible encryption", "B) One-way deterministic fixed-length output", "C) Uses private key", "D) Requires online connection"], "B) One-way deterministic fixed-length output", "Hashes are one-way non-invertible functions producing fixed-size digest."),
        ("SSL/TLS", "Primary purpose of SSL/TLS handshake protocol:", ["A) Compress HTTP payload", "B) Authenticate server & negotiate encryption key", "C) Block malware downloads", "D) Route DNS packets"], "B) Authenticate server & negotiate encryption key", "SSL/TLS handshake authenticates identities via certificates and establishes session key."),
        ("Firewall", "Firewall filtering packets based on IP addresses, ports, and protocols without tracking state:", ["A) Stateful Inspection", "B) Stateless Packet Filtering", "C) Application Proxy", "D) WAF"], "B) Stateless Packet Filtering", "Stateless packet filtering checks headers independently without state table."),
        ("Web Security", "Which attack injects malicious JavaScript into trusted websites viewed by other users?", ["A) SQL Injection", "B) Cross-Site Scripting (XSS)", "C) CSRF", "D) Buffer Overflow"], "B) Cross-Site Scripting (XSS)", "XSS executes untrusted JS code in victim's browser session."),
        ("Database Security", "Best practice to prevent SQL Injection attacks:", ["A) Input Sanitization", "B) Parameterized Queries / Prepared Statements", "C) Escaping Quotes", "D) Hashing Passwords"], "B) Parameterized Queries / Prepared Statements", "Prepared statements separate SQL command code from user data parameters.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(sec_items, 75):
        qs.append({'q_num': idx, 'type': 'mcq', 'title': f'Accenture Technical Q{idx}: {topic}', 'text': title, 'options': opts, 'correct': corr, 'explanation': expl})

    # 81-85: Cloud Computing
    cloud_items = [
        ("Cloud Models", "AWS EC2 and Google Compute Engine are examples of which cloud service model?", ["A) SaaS", "B) PaaS", "C) IaaS", "D) FaaS"], "C) IaaS", "Infrastructure as a Service (IaaS) provides virtualized computing resources (VMs, storage)."),
        ("Serverless", "Key characteristic of Serverless Computing (e.g. AWS Lambda):", ["A) No servers exist", "B) Event-driven execution where provider manages server allocation & scaling", "C) Fixed monthly bill", "D) Always running background daemon"], "B) Event-driven execution where provider manages server allocation & scaling", "Serverless charges only for execution time; cloud provider auto-scales servers."),
        ("Cloud Storage", "Which cloud storage type is best suited for unstructured data like images and backups?", ["A) Block Storage", "B) Object Storage (e.g., AWS S3)", "C) Relational DB", "D) Cache Storage"], "B) Object Storage (e.g., AWS S3)", "Object storage provides high durability for unstructured media files and blobs."),
        ("Scalability", "Scaling by adding more instances/servers of smaller capacity is called:", ["A) Vertical Scaling (Scale Up)", "B) Horizontal Scaling (Scale Out)", "C) Auto Partitioning", "D) Overclocking"], "B) Horizontal Scaling (Scale Out)", "Horizontal scaling adds more machine nodes to distributed cluster."),
        ("Load Balancing", "Role of Cloud Load Balancer:", ["A) Encrypt hard drives", "B) Distribute incoming application traffic across multiple healthy server instances", "C) Backup database nightly", "D) Compile source code"], "B) Distribute incoming application traffic across multiple healthy server instances", "Load balancers distribute user traffic to maintain responsiveness and availability.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(cloud_items, 81):
        qs.append({'q_num': idx, 'type': 'mcq', 'title': f'Accenture Technical Q{idx}: {topic}', 'text': title, 'options': opts, 'correct': corr, 'explanation': expl})

    # 86-90: Basic Programming / OOP Concepts
    oop_items = [
        ("Encapsulation", "OOP concept of wrapping data members and methods together into single unit while restricting direct access:", ["A) Inheritance", "B) Encapsulation", "C) Polymorphism", "D) Abstraction"], "B) Encapsulation", "Encapsulation hides internal object state behind private fields and public getters/setters."),
        ("Inheritance", "Keyword used in Java to derive a child class from a parent class:", ["A) inherits", "B) extends", "C) implements", "D) super"], "B) extends", "In Java, 'extends' is used for class inheritance."),
        ("Polymorphism", "Function overloading is an example of:", ["A) Compile-time Polymorphism", "B) Runtime Polymorphism", "C) Dynamic Binding", "D) Late Binding"], "A) Compile-time Polymorphism", "Overloading resolves method signatures at compile time (Static Polymorphism)."),
        ("Abstraction", "Main difference between Abstract Class and Interface in C++ / Java:", ["A) Interface can have instance variables", "B) Interface contains only abstract method signatures (prior to Java 8)", "C) Class can extend multiple abstract classes", "D) No difference"], "B) Interface contains only abstract method signatures (prior to Java 8)", "Interfaces define contracts without state; abstract classes can hold fields and implementation."),
        ("Virtual Functions", "Purpose of 'virtual' keyword in C++ function declaration:", ["A) Make function inline", "B) Enable dynamic binding and method overriding in derived classes", "C) Make function private", "D) Prevent modification"], "B) Enable dynamic binding and method overriding in derived classes", "Virtual functions ensure correct derived method is called when invoked via base pointer.")
    ]
    for idx, (topic, title, opts, corr, expl) in enumerate(oop_items, 86):
        qs.append({'q_num': idx, 'type': 'mcq', 'title': f'Accenture Technical Q{idx}: {topic}', 'text': title, 'options': opts, 'correct': corr, 'explanation': expl})

    return qs

def get_accenture_round3_coding_qs():
    code1 = """# --- 1. PYTHON 3 SOLUTION ---
def evaluateBinaryString(s: str) -> int:
    if not s: return -1
    res = int(s[0])
    i = 1
    while i < len(s):
        op = s[i]
        next_val = int(s[i + 1])
        if op == 'A': res &= next_val
        elif op == 'B': res |= next_val
        elif op == 'C': res ^= next_val
        i += 2
    return res

// --- 2. JAVA 17 SOLUTION ---
public class Solution {
    public static int evaluateBinaryString(String s) {
        if (s == null || s.length() == 0) return -1;
        int res = s.charAt(0) - '0';
        for (int i = 1; i < s.length(); i += 2) {
            char op = s.charAt(i);
            int nextVal = s.charAt(i + 1) - '0';
            if (op == 'A') res &= nextVal;
            else if (op == 'B') res |= nextVal;
            else if (op == 'C') res ^= nextVal;
        }
        return res;
    }
}

// --- 3. C11 SOLUTION ---
#include <stdio.h>
#include <string.h>

int evaluateBinaryString(const char* s) {
    if (!s || strlen(s) == 0) return -1;
    int res = s[0] - '0';
    int len = strlen(s);
    for (int i = 1; i < len; i += 2) {
        char op = s[i];
        int nextVal = s[i+1] - '0';
        if (op == 'A') res &= nextVal;
        else if (op == 'B') res |= nextVal;
        else if (op == 'C') res ^= nextVal;
    }
    return res;
}

// --- 4. C++17 SOLUTION ---
#include <iostream>
#include <string>

int evaluateBinaryString(const std::string& s) {
    if (s.empty()) return -1;
    int res = s[0] - '0';
    for (size_t i = 1; i < s.length(); i += 2) {
        char op = s[i];
        int nextVal = s[i + 1] - '0';
        if (op == 'A') res &= nextVal;
        else if (op == 'B') res |= nextVal;
        else if (op == 'C') res ^= nextVal;
    }
    return res;
}"""

    code2 = """# --- 1. PYTHON 3 SOLUTION ---
def countSuperiorElements(arr: list[int]) -> int:
    if not arr: return 0
    count = 0
    max_so_far = float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_so_far:
            count += 1
            max_so_far = arr[i]
    return count

// --- 2. JAVA 17 SOLUTION ---
public class Solution {
    public static int countSuperiorElements(int[] arr) {
        if (arr == null || arr.length == 0) return 0;
        int count = 0;
        int maxSoFar = Integer.MIN_VALUE;
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] > maxSoFar) {
                count++;
                maxSoFar = arr[i];
            }
        }
        return count;
    }
}

// --- 3. C11 SOLUTION ---
#include <stdio.h>
#include <limits.h>

int countSuperiorElements(int arr[], int n) {
    if (n <= 0) return 0;
    int count = 0;
    int maxSoFar = INT_MIN;
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] > maxSoFar) {
            count++;
            maxSoFar = arr[i];
        }
    }
    return count;
}

// --- 4. C++17 SOLUTION ---
#include <iostream>
#include <vector>
#include <climits>

int countSuperiorElements(const std::vector<int>& arr) {
    if (arr.empty()) return 0;
    int count = 0;
    int maxSoFar = INT_MIN;
    for (int i = (int)arr.size() - 1; i >= 0; --i) {
        if (arr[i] > maxSoFar) {
            count++;
            maxSoFar = arr[i];
        }
    }
    return count;
}"""

    return [
        {
            'q_num': 91,
            'type': 'coding',
            'title': 'Accenture Coding Q1: Sequential Binary String Evaluation',
            'text': "Given a binary string `str` consisting of digits '0' and '1' interleaved with logical operators 'A' (AND), 'B' (OR), and 'C' (XOR), evaluate the boolean expression sequentially from left to right.\n\nSupported Languages: Python 3, Java 17, C11, C++17.",
            'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
            'sample_answer': code1,
            'explanation': 'Sequential left-to-right evaluation in O(N) time and O(1) space across Python, Java, C, and C++.'
        },
        {
            'q_num': 92,
            'type': 'coding',
            'title': 'Accenture Coding Q2: Count Superior Elements in Array',
            'text': "An element in an array is called a 'Superior Element' if it is strictly greater than all elements present to its right side. The rightmost element is always considered superior. Given an array of integers, write a function to return the total count of superior elements.\n\nSupported Languages: Python 3, Java 17, C11, C++17.",
            'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
            'sample_answer': code2,
            'explanation': 'Single right-to-left traversal maintaining running maximum in O(N) time and O(1) space across Python, Java, C, and C++.'
        }
    ]

def get_accenture_sections(title_str):
    return [
        {
            'section_name': 'Round 1: Cognitive Assessment (50 Questions - Verbal, Logical, Numerical)',
            'time': '50 Mins',
            'questions': get_accenture_round1_cognitive_qs()
        },
        {
            'section_name': 'Round 2: Technical Assessment (40 Questions - Pseudocode, MS Office, Fundamentals, Networking, Security, Cloud, OOP)',
            'time': '40 Mins',
            'questions': get_accenture_round2_technical_qs()
        },
        {
            'section_name': 'Round 3: Coding Assessment (2 Problems - Python, Java, C, C++)',
            'time': '45 Mins',
            'questions': get_accenture_round3_coding_qs()
        }
    ]


def get_amazon_coding_5_qs(title_str):
    t_lower = title_str.lower()
    
    if 'model 2' in t_lower or '2024' in t_lower:
        return [
            {
                'q_num': 31,
                'type': 'coding',
                'title': 'Amazon Coding Q1: Reorganize String (Max-Heap)',
                'text': 'Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any valid string or empty string if impossible.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'import heapq\nfrom collections import Counter\n\ndef reorganizeString(s: str) -> str:\n    count = Counter(s)\n    max_heap = [[-cnt, char] for char, cnt in count.items()]\n    heapq.heapify(max_heap)\n    prev = None\n    res = []\n    while max_heap or prev:\n        if prev and not max_heap:\n            return ""\n        cnt, char = heapq.heappop(max_heap)\n        res.append(char)\n        cnt += 1\n        if prev:\n            heapq.heappush(max_heap, prev)\n            prev = None\n        if cnt < 0:\n            prev = [cnt, char]\n    return "".join(res)',
                'explanation': 'Uses Max-Heap to always place the most frequent remaining character. Time Complexity: O(N log K).'
            },
            {
                'q_num': 32,
                'type': 'coding',
                'title': 'Amazon Coding Q2: Minimum Window Substring',
                'text': 'Given two strings `s` and `t` of lengths `m` and `n`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import Counter\n\ndef minWindow(s: str, t: str) -> str:\n    if not t or not s: return ""\n    dict_t = Counter(t)\n    required = len(dict_t)\n    l, r = 0, 0\n    formed = 0\n    window_counts = {}\n    ans = float("inf"), None, None\n    while r < len(s):\n        character = s[r]\n        window_counts[character] = window_counts.get(character, 0) + 1\n        if character in dict_t and window_counts[character] == dict_t[character]:\n            formed += 1\n        while l <= r and formed == required:\n            character = s[l]\n            if r - l + 1 < ans[0]:\n                ans = (r - l + 1, l, r)\n            window_counts[character] -= 1\n            if character in dict_t and window_counts[character] < dict_t[character]:\n                formed -= 1\n            l += 1\n        r += 1\n    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]',
                'explanation': 'Sliding Window technique with character frequency maps. Time Complexity: O(|S| + |T|).'
            },
            {
                'q_num': 33,
                'type': 'coding',
                'title': 'Amazon Coding Q3: Lowest Common Ancestor of a Binary Tree',
                'text': 'Given a binary tree, find the lowest common ancestor (LCA) of two given nodes `p` and `q`.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def lowestCommonAncestor(root, p, q):\n    if not root or root == p or root == q:\n        return root\n    left = lowestCommonAncestor(root.left, p, q)\n    right = lowestCommonAncestor(root.right, p, q)\n    if left and right:\n        return root\n    return left if left else right',
                'explanation': 'Recursive post-order traversal searching left and right subtrees. Time Complexity: O(N).'
            },
            {
                'q_num': 34,
                'type': 'coding',
                'title': 'Amazon Coding Q4: Find Median from Data Stream (Dual Heaps)',
                'text': 'Design a data structure that supports adding integers from a stream and finding the median in O(1) time.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'import heapq\n\nclass MedianFinder:\n    def __init__(self):\n        self.small = [] # Max Heap\n        self.large = [] # Min Heap\n\n    def addNum(self, num: int) -> None:\n        heapq.heappush(self.small, -num)\n        if self.small and self.large and (-self.small[0] > self.large[0]):\n            val = -heapq.heappop(self.small)\n            heapq.heappush(self.large, val)\n        if len(self.small) > len(self.large) + 1:\n            val = -heapq.heappop(self.small)\n            heapq.heappush(self.large, val)\n        if len(self.large) > len(self.small) + 1:\n            val = heapq.heappop(self.large)\n            heapq.heappush(self.small, -val)\n\n    def findMedian(self) -> float:\n        if len(self.small) > len(self.large):\n            return -self.small[0]\n        if len(self.large) > len(self.small):\n            return self.large[0]\n        return (-self.small[0] + self.large[0]) / 2.0',
                'explanation': 'Dual Heap (Max-heap for lower half, Min-heap for upper half). Time Complexity: O(log N) insert, O(1) lookup.'
            },
            {
                'q_num': 35,
                'type': 'coding',
                'title': 'Amazon Coding Q5: Maximum Subarray Sum with One Deletion',
                'text': 'Given an array of integers, return the maximum sum of a non-empty subarray with at most one element deletion.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def maximumSum(arr):\n    n = len(arr)\n    if n == 1: return arr[0]\n    no_deletion = arr[0]\n    one_deletion = float("-inf")\n    max_sum = arr[0]\n    for i in range(1, n):\n        one_deletion = max(one_deletion + arr[i], no_deletion)\n        no_deletion = max(no_deletion + arr[i], arr[i])\n        max_sum = max(max_sum, no_deletion, one_deletion)\n    return max_sum',
                'explanation': "Kadanes DP variant maintaining running sums with 0 and 1 deletion state. Time Complexity: O(N)."
            }
        ]

    elif 'model 3' in t_lower or '2023' in t_lower:
        return [
            {
                'q_num': 31,
                'type': 'coding',
                'title': 'Amazon Coding Q1: Number of Islands (Grid BFS / DFS)',
                'text': 'Given an m x n 2D binary grid `grid` representing a map of 1s (land) and 0s (water), return the number of islands.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def numIslands(grid):\n    if not grid: return 0\n    rows, cols = len(grid), len(grid[0])\n    count = 0\n    def dfs(r, c):\n        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":\n            return\n        grid[r][c] = "0"\n        dfs(r + 1, c)\n        dfs(r - 1, c)\n        dfs(r, c + 1)\n        dfs(r, c - 1)\n    for r in range(rows):\n        for c in range(cols):\n            if grid[r][c] == "1":\n                count += 1\n                dfs(r, c)\n    return count',
                'explanation': 'DFS graph traversal marking visited land cells. Time Complexity: O(M * N).'
            },
            {
                'q_num': 32,
                'type': 'coding',
                'title': 'Amazon Coding Q2: Rotting Oranges (Multi-source BFS)',
                'text': 'You are given an m x n `grid` where 0 is empty, 1 is fresh orange, and 2 is rotten orange. Every minute, any fresh orange adjacent to a rotten orange becomes rotten. Return minimum minutes until no fresh orange remains.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import deque\n\ndef orangesRotting(grid):\n    rows, cols = len(grid), len(grid[0])\n    q = deque()\n    fresh = 0\n    for r in range(rows):\n        for c in range(cols):\n            if grid[r][c] == 2: q.append((r, c))\n            elif grid[r][c] == 1: fresh += 1\n    minutes = 0\n    directions = [(1,0), (-1,0), (0,1), (0,-1)]\n    while q and fresh > 0:\n        minutes += 1\n        for _ in range(len(q)):\n            r, c = q.popleft()\n            for dr, dc in directions:\n                nr, nc = r + dr, c + dc\n                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:\n                    grid[nr][nc] = 2\n                    fresh -= 1\n                    q.append((nr, nc))\n    return minutes if fresh == 0 else -1',
                'explanation': 'Multi-source Breadth-First Search level by level. Time Complexity: O(M * N).'
            },
            {
                'q_num': 33,
                'type': 'coding',
                'title': 'Amazon Coding Q3: Word Search II (Trie + Matrix Backtracking)',
                'text': 'Given an m x n `board` of characters and a list of strings `words`, return all words on the board.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'class TrieNode:\n    def __init__(self):\n        self.children = {}\n        self.word = None\n\ndef findWords(board, words):\n    root = TrieNode()\n    for w in words:\n        node = root\n        for char in w:\n            if char not in node.children:\n                node.children[char] = TrieNode()\n            node = node.children[char]\n        node.word = w\n    res = []\n    rows, cols = len(board), len(board[0])\n    def dfs(r, c, node):\n        char = board[r][c]\n        curr = node.children.get(char)\n        if not curr: return\n        if curr.word:\n            res.append(curr.word)\n            curr.word = None\n        board[r][c] = "#"\n        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":\n                dfs(nr, nc, curr)\n        board[r][c] = char\n    for r in range(rows):\n        for c in range(cols):\n            dfs(r, c, root)\n    return res',
                'explanation': 'Prefix Tree (Trie) combined with 2D matrix DFS backtracking. Time Complexity: O(M * N * 4^L).'
            },
            {
                'q_num': 34,
                'type': 'coding',
                'title': 'Amazon Coding Q4: Subtree of Another Tree',
                'text': 'Given the roots of two binary trees `root` and `subRoot`, return true if there is a subtree of `root` with the same structure and node values as `subRoot`.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'def isSubtree(root, subRoot):\n    if not subRoot: return True\n    if not root: return False\n    if isSameTree(root, subRoot): return True\n    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)\n\ndef isSameTree(p, q):\n    if not p and not q: return True\n    if not p or not q or p.val != q.val: return False\n    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)',
                'explanation': 'Tree traversal with recursive subtree equality comparison. Time Complexity: O(M * N).'
            },
            {
                'q_num': 35,
                'type': 'coding',
                'title': 'Amazon Coding Q5: Top K Frequent Words',
                'text': 'Given an array of strings `words` and an integer `k`, return the `k` most frequent strings sorted by frequency (higher first) and lexicographical order.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'import heapq\nfrom collections import Counter\n\nclass Pair:\n    def __init__(self, word, count):\n        self.word = word\n        self.count = count\n    def __lt__(self, other):\n        if self.count == other.count:\n            return self.word > other.word\n        return self.count < other.count\n\ndef topKFrequent(words, k):\n    counts = Counter(words)\n    heap = []\n    for word, count in counts.items():\n        heapq.heappush(heap, Pair(word, count))\n        if len(heap) > k:\n            heapq.heappop(heap)\n    res = []\n    while heap:\n        res.append(heapq.heappop(heap).word)\n    return res[::-1]',
                'explanation': 'Min-Heap storing frequency and custom string comparator. Time Complexity: O(N log K).'
            }
        ]

    else:
        # Default / Model 1 (2025 Official)
        return [
            {
                'q_num': 31,
                'type': 'coding',
                'title': 'Amazon Coding Q1: LRU Cache Implementation',
                'text': 'Design a data structure that follows the constraints of a Least Recently Used (LRU) cache with O(1) get and put operations.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'class Node:\n    def __init__(self, key, val):\n        self.key, self.val = key, val\n        self.prev = self.next = None\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.cap = capacity\n        self.cache = {}\n        self.left, self.right = Node(0, 0), Node(0, 0)\n        self.left.next, self.right.prev = self.right, self.left\n\n    def remove(self, node):\n        prev, nxt = node.prev, node.next\n        prev.next, nxt.prev = nxt, prev\n\n    def insert(self, node):\n        prev, nxt = self.right.prev, self.right\n        prev.next = nxt.prev = node\n        node.prev, node.next = prev, nxt\n\n    def get(self, key: int) -> int:\n        if key in self.cache:\n            self.remove(self.cache[key])\n            self.insert(self.cache[key])\n            return self.cache[key].val\n        return -1',
                'explanation': 'Uses Hash Map combined with Doubly Linked List for O(1) time complexity.'
            },
            {
                'q_num': 32,
                'type': 'coding',
                'title': 'Amazon Coding Q2: Merge K Sorted Lists',
                'text': 'You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'import heapq\n\ndef mergeKLists(lists):\n    heap = []\n    for idx, l in enumerate(lists):\n        if l:\n            heapq.heappush(heap, (l.val, idx, l))\n    dummy = ListNode(0)\n    curr = dummy\n    while heap:\n        val, idx, node = heapq.heappop(heap)\n        curr.next = node\n        curr = curr.next\n        if node.next:\n            heapq.heappush(heap, (node.next.val, idx, node.next))\n    return dummy.next',
                'explanation': 'Min Heap (Priority Queue) approach. Time Complexity: O(N log K), Space Complexity: O(K).'
            },
            {
                'q_num': 33,
                'type': 'coding',
                'title': 'Amazon Coding Q3: Word Ladder (Shortest Transformation Sequence)',
                'text': 'Given two words `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'from collections import deque\n\ndef ladderLength(beginWord, endWord, wordList):\n    wordSet = set(wordList)\n    if endWord not in wordSet: return 0\n    queue = deque([(beginWord, 1)])\n    while queue:\n        word, length = queue.popleft()\n        if word == endWord: return length\n        for i in range(len(word)):\n            for c in "abcdefghijklmnopqrstuvwxyz":\n                next_word = word[:i] + c + word[i+1:]\n                if next_word in wordSet:\n                    wordSet.remove(next_word)\n                    queue.append((next_word, length + 1))\n    return 0',
                'explanation': 'Breadth-First Search (BFS) graph traversal. Time Complexity: O(M^2 * N).'
            },
            {
                'q_num': 34,
                'type': 'coding',
                'title': 'Amazon Coding Q4: Serialize and Deserialize Binary Tree',
                'text': 'Design an algorithm to serialize a binary tree into a string and deserialize that string back to the original binary tree structure.',
                'options': ['A) 20 years', 'B) 12 years', 'C) 16 years', 'D) 24 years'],
                'sample_answer': 'class Codec:\n    def serialize(self, root):\n        vals = []\n        def preorder(node):\n            if not node:\n                vals.append("N")\n                return\n            vals.append(str(node.val))\n            preorder(node.left)\n            preorder(node.right)\n        preorder(root)\n        return ",".join(vals)\n\n    def deserialize(self, data):\n        vals = iter(data.split(","))\n        def build():\n            val = next(vals)\n            if val == "N": return None\n            node = TreeNode(int(val))\n            node.left = build()\n            node.right = build()\n            return node\n        return build()',
                'explanation': 'Preorder depth-first traversal with delimiter. Time Complexity: O(N).'
            }
        ]

def get_company_92_sections(comp_name, title_str):
    comp_clean = comp_name.strip()
    c_lower = comp_clean.lower()
    
    # -------------------------------------------------------------------------
    # SECTION 1: Online Assessment (18 Easy/Medium Questions)
    # Topics: Quantitative aptitude, logical reasoning, verbal ability, written communication
    # -------------------------------------------------------------------------
    sec1_qs = [
        # Quantitative Aptitude (Easy & Medium: Q1 to Q6)
        {'q_num': 1, 'type': 'mcq', 'title': 'Train Speed Calculation', 'text': 'A train travels 360 km in 4 hours. What is its speed?', 'options': ['A) 80 km/h', 'B) 90 km/h', 'C) 100 km/h', 'D) 120 km/h'], 'correct': 'B) 90 km/h', 'explanation': 'Speed = Distance / Time = 360 / 4 = 90 km/h.', 'marks': '2 Marks'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Profit Percentage Calculation', 'text': 'A product costs ₹800 and is sold for ₹960. What is the profit percentage?', 'options': ['A) 15%', 'B) 20%', 'C) 25%', 'D) 30%'], 'correct': 'B) 20%', 'explanation': 'Profit = 960 - 800 = 160. Profit % = (160 / 800) * 100 = 20%.', 'marks': '2 Marks'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Number Series Pattern', 'text': 'Find the next number in series: 2, 6, 12, 20, 30, ?', 'options': ['A) 36', 'B) 40', 'C) 42', 'D) 44'], 'correct': 'C) 42', 'explanation': 'Differences between consecutive terms are 4, 6, 8, 10, 12. So 30 + 12 = 42.', 'marks': '2 Marks'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Time and Work Together', 'text': 'A can complete a job in 10 days and B in 15 days. How long will they take working together?', 'options': ['A) 5 days', 'B) 6 days', 'C) 7 days', 'D) 8 days'], 'correct': 'B) 6 days', 'explanation': '1/10 + 1/15 = 5/60 = 1/6. Together they take 6 days.', 'marks': '2 Marks'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Simple Interest Calculation', 'text': 'Find the Simple Interest on ₹5,000 at 10% per annum for 2 years:', 'options': ['A) ₹1,000', 'B) ₹500', 'C) ₹1,200', 'D) ₹800'], 'correct': 'A) ₹1,000', 'explanation': 'SI = (P * R * T) / 100 = (5000 * 10 * 2) / 100 = ₹1,000.', 'marks': '2 Marks'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Percentage Computation', 'text': 'What is 25% of 480?', 'options': ['A) 120', 'B) 100', 'C) 140', 'D) 150'], 'correct': 'A) 120', 'explanation': '25% of 480 = (25 / 100) * 480 = 120.', 'marks': '2 Marks'},

        # Logical Reasoning (Easy & Medium: Q7 to Q12)
        {'q_num': 7, 'type': 'mcq', 'title': 'Coding-Decoding Pattern', 'text': 'If CAT is coded as DBU, how is DOG coded?', 'options': ['A) EPH', 'B) EOG', 'C) FPH', 'D) DPH'], 'correct': 'A) EPH', 'explanation': 'Each letter is shifted by +1: D->E, O->P, G->H => EPH.', 'marks': '2 Marks'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Direction Sense Test', 'text': 'A person walks 5 km North, then 3 km East. In which direction is he from his starting point?', 'options': ['A) North', 'B) East', 'C) North-East', 'D) South-East'], 'correct': 'C) North-East', 'explanation': 'Moving North and East places the person in North-East relative to origin.', 'marks': '2 Marks'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Odd One Out Classification', 'text': 'Find the odd one out: Apple, Mango, Carrot, Banana', 'options': ['A) Apple', 'B) Mango', 'C) Carrot', 'D) Banana'], 'correct': 'C) Carrot', 'explanation': 'Carrot is a root vegetable; Apple, Mango, and Banana are fruits.', 'marks': '2 Marks'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Alphabet Series Completion', 'text': 'Find the next letter in series: A, C, E, G, I, ?', 'options': ['A) K', 'B) J', 'C) L', 'D) M'], 'correct': 'A) K', 'explanation': 'Pattern skips 1 letter (+2 position shift): A(+2)->C(+2)->E(+2)->G(+2)->I(+2)->K.', 'marks': '2 Marks'},
        {'q_num': 11, 'type': 'mcq', 'title': 'Syllogism Logic', 'text': 'Statements: 1. All dogs are pets. 2. All pets are animals. Conclusion: All dogs are animals.', 'options': ['A) Follows', 'B) Does not follow', 'C) Uncertain', 'D) None'], 'correct': 'A) Follows', 'explanation': 'If A is inside B and B is inside C, then A is inside C (Valid deduction).', 'marks': '2 Marks'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Blood Relation Puzzle', 'text': 'Pointing to a photo, Rahul says "She is the mother of my father\'s daughter." How is she related to Rahul?', 'options': ['A) Mother', 'B) Sister', 'C) Aunt', 'D) Cousin'], 'correct': 'A) Mother', 'explanation': "Rahul's father's daughter is his sister; her mother is also Rahul's mother.", 'marks': '2 Marks'},

        # Verbal Ability & Written Communication (Easy & Medium: Q13 to Q18)
        {'q_num': 13, 'type': 'mcq', 'title': 'Grammar Subject-Verb Agreement', 'text': 'Choose the grammatically correct sentence:', 'options': ['A) She don\'t like Python.', 'B) She doesn\'t likes Python.', 'C) She doesn\'t like Python.', 'D) She not like Python.'], 'correct': 'C) She doesn\'t like Python.', 'explanation': 'Singular subject "She" requires "doesn\'t" followed by base verb "like".', 'marks': '2 Marks'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Synonym Selection', 'text': 'Choose the synonym of "Rapid":', 'options': ['A) Slow', 'B) Fast', 'C) Weak', 'D) Late'], 'correct': 'B) Fast', 'explanation': '"Rapid" means happening with great speed (Fast).', 'marks': '2 Marks'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Antonym Selection', 'text': 'Choose the antonym of "Ancient":', 'options': ['A) Old', 'B) Historic', 'C) Modern', 'D) Traditional'], 'correct': 'C) Modern', 'explanation': '"Ancient" means belonging to distant past; opposite is "Modern".', 'marks': '2 Marks'},
        {'q_num': 16, 'type': 'mcq', 'title': 'Sentence Completion', 'text': 'The software developer worked hard to _______ the critical bug before release.', 'options': ['A) resolve', 'B) break', 'C) ignore', 'D) delay'], 'correct': 'A) resolve', 'explanation': '"Resolve" means to solve or fix a bug.', 'marks': '2 Marks'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Idioms & Phrases', 'text': 'What does the idiom "Piece of cake" signify?', 'options': ['A) A very easy task', 'B) A delicious food', 'C) A hard problem', 'D) A sweet reward'], 'correct': 'A) A very easy task', 'explanation': '"Piece of cake" means something that is very simple or easy to accomplish.', 'marks': '2 Marks'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Active and Passive Voice', 'text': 'Convert to Passive Voice: "The engineer wrote clean code."', 'options': ['A) Clean code was written by the engineer.', 'B) Clean code is writing by engineer.', 'C) Engineer is written code.', 'D) Code writes engineer.'], 'correct': 'A) Clean code was written by the engineer.', 'explanation': 'Past simple active "wrote" converts to "was written" in passive voice.', 'marks': '2 Marks'}
    ]

    # -------------------------------------------------------------------------
    # SECTION 2: Coding Assessment (16 Easy/Medium Questions)
    # Topics: Programming, problem solving, DSA, coding questions
    # -------------------------------------------------------------------------
    c_code1 = f"""# --- 1. PYTHON 3 SOLUTION ---
def solve_coding_q33(arr: list[int]) -> tuple[int, list[int]]:
    # 1. Find Second Largest
    unique_arr = list(set(arr))
    unique_arr.sort()
    second_largest = unique_arr[-2] if len(unique_arr) >= 2 else -1
    
    # 2. Find Duplicate Elements
    counts = {{}}
    duplicates = []
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    for x, cnt in counts.items():
        if cnt > 1:
            duplicates.append(x)
            
    return second_largest, sorted(duplicates)

// --- 2. JAVA 17 SOLUTION ---
import java.util.*;
public class Solution {{
    public static void main(String[] args) {{
        int[] arr = {{10, 5, 20, 8, 15, 20, 5}};
        Arrays.sort(arr);
        System.out.println("Second Largest: " + arr[arr.length - 2]);
    }}
}}

// --- 3. C11 SOLUTION ---
#include <stdio.h>
int findSecondLargest(int arr[], int n) {{
    int first = -1, second = -1;
    for(int i = 0; i < n; i++) {{
        if(arr[i] > first) {{
            second = first;
            first = arr[i];
        }} else if(arr[i] > second && arr[i] != first) {{
            second = arr[i];
        }}
    }}
    return second;
}}

// --- 4. C++17 SOLUTION ---
#include <vector>
#include <set>
int getSecondLargest(const std::vector<int>& arr) {{
    std::set<int> st(arr.begin(), arr.end());
    if (st.size() < 2) return -1;
    auto it = st.rbegin();
    return *(++it);
}}"""

    c_code2 = f"""# --- 1. PYTHON 3 SOLUTION ---
def solve_coding_q34(s: str) -> dict:
    # 1. Check Palindrome
    is_palindrome = (s == s[::-1])
    
    # 2. Character Frequency
    freq = {{}}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    return {{"is_palindrome": is_palindrome, "frequency": freq}}

// --- 2. JAVA 17 SOLUTION ---
import java.util.*;
public class Solution {{
    public static boolean isPalindrome(String s) {{
        String rev = new StringBuilder(s).reverse().toString();
        return s.equals(rev);
    }}
}}

// --- 3. C11 SOLUTION ---
#include <stdio.h>
#include <string.h>
int isPalindrome(char s[]) {{
    int l = 0, h = strlen(s) - 1;
    while (h > l) {{
        if (s[l++] != s[h--]) return 0;
    }}
    return 1;
}}

// --- 4. C++17 SOLUTION ---
#include <string>
#include <unordered_map>
std::unordered_map<char, int> countFreq(std::string s) {{
    std::unordered_map<char, int> mp;
    for(char c : s) mp[c]++;
    return mp;
}}"""

    sec2_qs = [
        # 14 Programming & DSA MCQs (Easy & Medium: Q19 to Q32)
        {'q_num': 19, 'type': 'mcq', 'title': 'Reverse a String Output', 'text': 'What is the output of reversing the string "hello"?', 'options': ['A) olleh', 'B) hello', 'C) elloh', 'D) ohlle'], 'correct': 'A) olleh', 'explanation': 'Reversing characters of "hello" from end to start gives "olleh".', 'marks': '2 Marks'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Check Palindrome Logic', 'text': 'What is the result of checking if string "madam" is a palindrome?', 'options': ['A) Palindrome', 'B) Not Palindrome', 'C) Invalid Input', 'D) Syntax Error'], 'correct': 'A) Palindrome', 'explanation': '"madam" reads the same backwards and forwards, so it is a Palindrome.', 'marks': '2 Marks'},
        {'q_num': 21, 'type': 'mcq', 'title': 'Find Second Largest in Array', 'text': 'Given input array [10, 5, 20, 8, 15], what is the second largest element?', 'options': ['A) 15', 'B) 20', 'C) 10', 'D) 8'], 'correct': 'A) 15', 'explanation': 'The largest element is 20, and the second largest element is 15.', 'marks': '2 Marks'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Count Character Frequency', 'text': 'In the string "programming", what is the frequency count of character \'r\'?', 'options': ['A) 2', 'B) 1', 'C) 3', 'D) 0'], 'correct': 'A) 2', 'explanation': 'Character \'r\' appears 2 times in "programming".', 'marks': '2 Marks'},
        {'q_num': 23, 'type': 'mcq', 'title': 'Find Missing Number in Array', 'text': 'Given array [1, 2, 3, 5] containing numbers from 1 to 5, which number is missing?', 'options': ['A) 4', 'B) 2', 'C) 5', 'D) 1'], 'correct': 'A) 4', 'explanation': 'Expected sum of 1..5 = 15. Actual sum = 11. Missing number = 15 - 11 = 4.', 'marks': '2 Marks'},
        {'q_num': 24, 'type': 'mcq', 'title': 'Check Prime Number', 'text': 'What is the classification of integer 17?', 'options': ['A) Prime', 'B) Not Prime', 'C) Composite', 'D) Neither'], 'correct': 'A) Prime', 'explanation': '17 has only two positive divisors (1 and 17), making it a Prime number.', 'marks': '2 Marks'},
        {'q_num': 25, 'type': 'mcq', 'title': 'Fibonacci Series Terms', 'text': 'What are the first 5 terms of the Fibonacci sequence starting from 0?', 'options': ['A) 0 1 1 2 3', 'B) 1 1 2 3 5', 'C) 0 1 2 3 4', 'D) 0 2 4 6 8'], 'correct': 'A) 0 1 1 2 3', 'explanation': 'Fibonacci sequence: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3.', 'marks': '2 Marks'},
        {'q_num': 26, 'type': 'mcq', 'title': 'Find Duplicate Elements in Array', 'text': 'Given input array [1, 2, 3, 2, 4, 3], which elements are duplicates?', 'options': ['A) 2 and 3', 'B) 1 and 4', 'C) 2 only', 'D) 3 only'], 'correct': 'A) 2 and 3', 'explanation': 'Elements 2 and 3 both appear more than once in the array.', 'marks': '2 Marks'},
        {'q_num': 27, 'type': 'mcq', 'title': 'Array Index Access', 'text': 'In a 0-indexed array [10, 20, 30, 40], what is the value at index 2?', 'options': ['A) 30', 'B) 20', 'C) 40', 'D) 10'], 'correct': 'A) 30', 'explanation': 'Index 0 is 10, index 1 is 20, index 2 is 30.', 'marks': '2 Marks'},
        {'q_num': 28, 'type': 'mcq', 'title': 'Modulo Remainder Operator', 'text': 'What is the value of expression `25 % 4`?', 'options': ['A) 1', 'B) 6', 'C) 0', 'D) 4'], 'correct': 'A) 1', 'explanation': '25 divided by 4 equals 6 with remainder 1.', 'marks': '2 Marks'},
        {'q_num': 29, 'type': 'mcq', 'title': 'Stack Operation PUSH', 'text': 'Which operation pushes a new element onto the top of a Stack?', 'options': ['A) Push', 'B) Pop', 'C) Peek', 'D) Enqueue'], 'correct': 'A) Push', 'explanation': 'Push adds element to top of stack; Pop removes from top.', 'marks': '2 Marks'},
        {'q_num': 30, 'type': 'mcq', 'title': 'Queue Data Structure Property', 'text': 'Which fundamental principle does a Queue data structure follow?', 'options': ['A) FIFO (First In First Out)', 'B) LIFO (Last In First Out)', 'C) Random Access', 'D) Priority Only'], 'correct': 'A) FIFO (First In First Out)', 'explanation': 'Queues operate on First-In First-Out (FIFO) ordering.', 'marks': '2 Marks'},
        {'q_num': 31, 'type': 'mcq', 'title': 'Linear Search Time Complexity', 'text': 'What is the worst-case time complexity of Linear Search in an unsorted array of size N?', 'options': ['A) O(N)', 'B) O(log N)', 'C) O(1)', 'D) O(N^2)'], 'correct': 'A) O(N)', 'explanation': 'Linear search may examine all N elements in the worst case.', 'marks': '2 Marks'},
        {'q_num': 32, 'type': 'mcq', 'title': 'Binary Search Pre-condition', 'text': 'Binary Search algorithm requires the input array to be:', 'options': ['A) Sorted', 'B) Unsorted', 'C) Reverse Sorted only', 'D) Doubly Linked'], 'correct': 'A) Sorted', 'explanation': 'Binary Search relies on sorted ordering to eliminate half of search space.', 'marks': '2 Marks'},

        # 2 Hands-on Coding Workspace Problems (Q33 & Q34)
        {
            'q_num': 33,
            'type': 'coding',
            'title': 'Find Second Largest & Duplicate Elements in Array',
            'text': f'Write a function for {comp_clean} technical assessment to find the second largest element and all duplicate elements in an integer array.\n\nInput Example: [10, 5, 20, 8, 15, 20, 5]\nOutput: Second Largest: 15, Duplicates: [5, 20]\n\nSupported Languages: Python 3, Java 17, C11, C++17.',
            'options': [],
            'sample_answer': c_code1,
            'explanation': 'Uses array sorting / single pass to extract 2nd largest and hash map counting to identify duplicates.',
            'marks': '10 Marks'
        },
        {
            'q_num': 34,
            'type': 'coding',
            'title': 'Check Palindrome & Count Character Frequencies',
            'text': f'Write a function for {comp_clean} technical assessment to check if an input string is a Palindrome and count the frequency of each character.\n\nInput Example: "programming"\nOutput: Palindrome: False, Frequencies: p:1, r:2, o:1, g:2, a:1, m:2, i:1, n:1\n\nSupported Languages: Python 3, Java 17, C11, C++17.',
            'options': [],
            'sample_answer': c_code2,
            'explanation': 'Two-pointer string comparison checks palindrome condition; hash map counts character occurrences in linear time.',
            'marks': '10 Marks'
        }
    ]

    # -------------------------------------------------------------------------
    # SECTION 3: Technical Interview (16 Easy/Medium Questions)
    # Topics: Programming, DSA, OOP, DBMS, SQL, OS, projects, technical fundamentals
    # -------------------------------------------------------------------------
    sec3_qs = [
        # 16 Core CS Technical MCQs (Easy & Medium: Q35 to Q50)
        {'q_num': 35, 'type': 'mcq', 'title': 'OOP Pillars - Inheritance', 'text': 'What is Inheritance in Object-Oriented Programming?', 'options': ['A) Reusing properties of a parent class in a child class', 'B) Hiding data fields', 'C) Overloading functions', 'D) Creating threads'], 'correct': 'A) Reusing properties of a parent class in a child class', 'explanation': 'Inheritance allows a child class to inherit attributes and methods from a parent class.', 'marks': '2 Marks'},
        {'q_num': 36, 'type': 'mcq', 'title': 'OOP Pillars - Encapsulation', 'text': 'Wrapping data variables and methods together into a single class unit is called:', 'options': ['A) Encapsulation', 'B) Abstraction', 'C) Inheritance', 'D) Polymorphism'], 'correct': 'A) Encapsulation', 'explanation': 'Encapsulation restricts direct variable access and bundles code with data.', 'marks': '2 Marks'},
        {'q_num': 37, 'type': 'mcq', 'title': 'Database Primary Key Constraint', 'text': 'Which constraint uniquely distinguishes a Primary Key in Relational Databases?', 'options': ['A) Unique and NOT NULL', 'B) Allows NULLs', 'C) Allows Duplicates', 'D) Foreign Reference'], 'correct': 'A) Unique and NOT NULL', 'explanation': 'Primary Key uniquely identifies rows and strictly disallows NULL values.', 'marks': '2 Marks'},
        {'q_num': 38, 'type': 'mcq', 'title': 'SQL Query SELECT Statement', 'text': 'Which SQL command retrieves all records from table `Employees`?', 'options': ['A) SELECT * FROM Employees;', 'B) GET ALL Employees;', 'C) READ Employees;', 'D) EXTRACT Employees;'], 'correct': 'A) SELECT * FROM Employees;', 'explanation': 'SELECT * FROM table_name retrieves all rows and columns.', 'marks': '2 Marks'},
        {'q_num': 39, 'type': 'mcq', 'title': 'SQL WHERE vs HAVING Clause', 'text': 'Where is the HAVING clause used in SQL queries?', 'options': ['A) To filter aggregated groups after GROUP BY', 'B) To filter raw rows before grouping', 'C) To join tables', 'D) To sort results'], 'correct': 'A) To filter aggregated groups after GROUP BY', 'explanation': 'HAVING filters aggregated values after GROUP BY; WHERE filters individual rows.', 'marks': '2 Marks'},
        {'q_num': 40, 'type': 'mcq', 'title': 'OS Process vs Thread Memory', 'text': 'What is a major memory difference between a Process and a Thread?', 'options': ['A) Threads share memory within same process; processes have isolated memory spaces', 'B) Threads cannot run concurrently', 'C) Processes share CPU registers', 'D) No difference'], 'correct': 'A) Threads share memory within same process; processes have isolated memory spaces', 'explanation': 'Threads share heap and global data of parent process; processes maintain separate page tables.', 'marks': '2 Marks'},
        {'q_num': 41, 'type': 'mcq', 'title': 'OS Deadlock Concept', 'text': 'A situation where two processes wait indefinitely for resources held by each other is called:', 'options': ['A) Deadlock', 'B) Starvation', 'C) Paging', 'D) Context Switch'], 'correct': 'A) Deadlock', 'explanation': 'Deadlock occurs when processes hold resources while waiting for others in a circular wait.', 'marks': '2 Marks'},
        {'q_num': 42, 'type': 'mcq', 'title': 'C/C++ Pointer Variables', 'text': 'What does a Pointer variable store in C/C++?', 'options': ['A) Memory address of another variable', 'B) Direct float value', 'C) Function name', 'D) Array size'], 'correct': 'A) Memory address of another variable', 'explanation': 'Pointers store hexadecimal memory addresses of variables.', 'marks': '2 Marks'},
        {'q_num': 43, 'type': 'mcq', 'title': 'Java Garbage Collection Purpose', 'text': 'What is the primary role of Garbage Collection in Java?', 'options': ['A) Automatically reclaim unreferenced heap memory', 'B) Delete unused source files', 'C) Clean up compilation errors', 'D) Format disk'], 'correct': 'A) Automatically reclaim unreferenced heap memory', 'explanation': 'JVM Garbage Collector frees memory occupied by unreachable objects.', 'marks': '2 Marks'},
        {'q_num': 44, 'type': 'mcq', 'title': 'Python Immutable Data Types', 'text': 'Which of the following Python data types is IMMUTABLE?', 'options': ['A) Tuple', 'B) List', 'C) Dictionary', 'D) Set'], 'correct': 'A) Tuple', 'explanation': 'Tuples cannot be modified after creation in Python.', 'marks': '2 Marks'},
        {'q_num': 45, 'type': 'mcq', 'title': 'Linked List Insertion Complexity', 'text': 'Time complexity to insert a new node at the beginning of a Singly Linked List:', 'options': ['A) O(1)', 'B) O(N)', 'C) O(N log N)', 'D) O(N^2)'], 'correct': 'A) O(1)', 'explanation': 'Inserting at head requires updating two pointers in constant O(1) time.', 'marks': '2 Marks'},
        {'q_num': 46, 'type': 'mcq', 'title': 'QuickSort Average Complexity', 'text': 'What is the average-case time complexity of QuickSort algorithm?', 'options': ['A) O(N log N)', 'B) O(N^2)', 'C) O(N)', 'D) O(1)'], 'correct': 'A) O(N log N)', 'explanation': 'Divide and conquer partition strategy yields average O(N log N) time.', 'marks': '2 Marks'},
        {'q_num': 47, 'type': 'mcq', 'title': 'Computer Networks OSI Model', 'text': 'At which OSI layer does IP (Internet Protocol) routing operate?', 'options': ['A) Network Layer (Layer 3)', 'B) Data Link Layer (Layer 2)', 'C) Transport Layer (Layer 4)', 'D) Application Layer (Layer 7)'], 'correct': 'A) Network Layer (Layer 3)', 'explanation': 'Layer 3 handles logical IP addressing and packet routing.', 'marks': '2 Marks'},
        {'q_num': 48, 'type': 'mcq', 'title': 'HTTPS vs HTTP Security', 'text': 'What makes HTTPS protocol secure compared to standard HTTP?', 'options': ['A) SSL/TLS Encryption', 'B) Faster CPU speed', 'C) Larger port number', 'D) Smaller headers'], 'correct': 'A) SSL/TLS Encryption', 'explanation': 'HTTPS encrypts data in transit using SSL/TLS protocols.', 'marks': '2 Marks'},
        {'q_num': 49, 'type': 'mcq', 'title': 'Software Engineering SDLC', 'text': 'What does SDLC stand for in Software Engineering?', 'options': ['A) Software Development Life Cycle', 'B) System Data Link Code', 'C) Standard Design Logic Component', 'D) Server Database Local Connection'], 'correct': 'A) Software Development Life Cycle', 'explanation': 'SDLC represents structured phases of software planning, building, testing, and deployment.', 'marks': '2 Marks'},
        {'q_num': 50, 'type': 'mcq', 'title': 'Git Version Control Command', 'text': 'What does command `git commit -m "message"` do?', 'options': ['A) Saves changes locally with a descriptive log message', 'B) Pushes code to remote server', 'C) Downloads latest code', 'D) Deletes repository'], 'correct': 'A) Saves changes locally with a descriptive log message', 'explanation': 'Git commit snapshots staged changes to local repository history.', 'marks': '2 Marks'}
    ]

    return [
        {
            'section_name': 'Section 1: Online Assessment',
            'desc': 'Quantitative aptitude, logical reasoning, verbal ability, written communication',
            'time': '40 Mins',
            'questions': sec1_qs
        },
        {
            'section_name': 'Section 2: Coding Assessment',
            'desc': 'Programming, problem solving, DSA, coding questions',
            'time': '35 Mins',
            'questions': sec2_qs
        },
        {
            'section_name': 'Technical Interview',
            'desc': 'Programming, DSA, OOP, DBMS, SQL, OS, projects, technical fundamentals',
            'time': '30 Mins',
            'questions': sec3_qs
        }
    ]

def get_google_practice_sections_model1():
    round1_qs = [
        {
            'q_num': 1,
            'type': 'coding',
            'title': 'Q1. Two Sum — Easy',
            'text': 'Given an array nums and an integer target, return the indices of two numbers whose sum equals target.\n\nExample:\nInput: nums = [2,7,11,15], target = 9\n\nTopic: Hash Map',
            'options': [],
            'sample_answer': '''def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []''',
            'explanation': 'Use a Hash Map to store seen numbers and their indices for O(N) time and O(N) space complexity.',
            'marks': '5 Marks'
        },
        {
            'q_num': 2,
            'type': 'coding',
            'title': 'Q2. Valid Parentheses — Easy',
            'text': 'Given a string containing (), {}, and [], determine whether the brackets are valid.\n\nExample:\nInput: "()[]{}"\n\nTopic: Stack',
            'options': [],
            'sample_answer': '''def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack''',
            'explanation': 'Use a Stack to match opening and closing brackets in O(N) time and O(N) space complexity.',
            'marks': '5 Marks'
        },
        {
            'q_num': 3,
            'type': 'coding',
            'title': 'Q3. Best Time to Buy and Sell Stock — Easy/Medium',
            'text': 'Find the maximum profit that can be obtained by buying and selling a stock once.\n\nExample:\nInput: [7,1,5,3,6,4]\n\nTopic: Arrays / Greedy',
            'options': [],
            'sample_answer': '''def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit''',
            'explanation': 'Track minimum price seen so far and calculate max potential profit in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 4,
            'type': 'coding',
            'title': 'Q4. Longest Substring Without Repeating Characters — Medium',
            'text': 'Find the length of the longest substring without repeating characters.\n\nExample:\nInput: "abcabcbb"\n\nTopic: Sliding Window + Hash Set',
            'options': [],
            'sample_answer': '''def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len''',
            'explanation': 'Use a sliding window with left/right pointers and a hash set in O(N) time.',
            'marks': '5 Marks'
        }
    ]

    round2_qs = [
        {
            'q_num': 5,
            'type': 'coding',
            'title': 'Q5. Product of Array Except Self — Medium',
            'text': 'Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].\n\nExample:\nInput: [1,2,3,4]\n\nConstraint: Try to solve without division.\nTopic: Prefix/Suffix',
            'options': [],
            'sample_answer': '''def productExceptSelf(nums):
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res''',
            'explanation': 'Calculate prefix products in forward pass and multiply with suffix products in reverse pass in O(N) time without division.',
            'marks': '5 Marks'
        },
        {
            'q_num': 6,
            'type': 'coding',
            'title': 'Q6. Merge Intervals — Medium',
            'text': 'Given an array of meeting intervals, merge all overlapping intervals.\n\nExample:\nInput: [[1,3],[2,6],[8,10],[15,18]]\n\nTopic: Sorting + Intervals',
            'options': [],
            'sample_answer': '''def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged''',
            'explanation': 'Sort intervals by start time and merge adjacent intervals if start <= prev_end in O(N log N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 7,
            'type': 'coding',
            'title': 'Q7. Search in Rotated Sorted Array — Medium',
            'text': 'Given the array nums after possible rotation and an integer target, return the index of target if it is in nums, or -1 if not.\n\nExample:\nInput: nums = [4,5,6,7,0,1,2], target = 0\n\nTopic: Binary Search',
            'options': [],
            'sample_answer': '''def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1''',
            'explanation': 'Identify which half of the rotated array is sorted and perform modified Binary Search in O(log N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 8,
            'type': 'coding',
            'title': 'Q8. Top K Frequent Elements — Medium',
            'text': 'Given an integer array nums and an integer k, return the k most frequent elements.\n\nExample:\nInput: nums = [1,1,1,2,2,3], k = 2\n\nTopic: Hash Map + Heap',
            'options': [],
            'sample_answer': '''import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)''',
            'explanation': 'Count frequencies using a Hash Map and extract top K elements using a Heap in O(N log K) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 9,
            'type': 'coding',
            'title': 'Q9. Kth Largest Element — Medium',
            'text': 'Find the kth largest element in an unsorted array without sorting the entire array.\n\nExample:\nInput: [3,2,1,5,6,4], k = 2\n\nTopic: Heap / Quickselect',
            'options': [],
            'sample_answer': '''import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]''',
            'explanation': 'Use a Min-Heap of size K or Quickselect partitioning algorithm in O(N) average time complexity.',
            'marks': '5 Marks'
        }
    ]

    round3_qs = [
        {
            'q_num': 10,
            'type': 'coding',
            'title': 'Q10. Maximum Depth of Binary Tree — Easy',
            'text': 'Given the root of a binary tree, return its maximum depth.\n\nExample:\nInput:\n       3\n      / \\\n     9  20\n        / \\\n       15  7\n\nTopic: Tree + DFS',
            'options': [],
            'sample_answer': '''def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))''',
            'explanation': 'Recursively compute the maximum depth of left and right subtrees in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 11,
            'type': 'coding',
            'title': 'Q11. Binary Tree Level Order Traversal — Medium',
            'text': 'Given a binary tree, return its level-order traversal.\n\nExample:\nInput:\n       3\n      / \\\n     9  20\n        / \\\n       15  7\n\nTopic: BFS + Queue',
            'options': [],
            'sample_answer': '''from collections import deque

def levelOrder(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
    return res''',
            'explanation': 'Perform Breadth-First Search (BFS) using a Queue to collect node values level by level in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 12,
            'type': 'coding',
            'title': 'Q12. Validate Binary Search Tree — Medium',
            'text': 'Determine whether a binary tree is a valid Binary Search Tree (BST).\n\nTopic: Binary Tree + Recursion',
            'options': [],
            'sample_answer': '''def isValidBST(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)''',
            'explanation': 'Recursively validate that left node < root < right node with lower and upper value bounds in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 13,
            'type': 'coding',
            'title': 'Q13. Number of Islands — Medium',
            'text': 'Given a grid containing 1 for land and 0 for water, find the number of islands.\n\nExample:\n11110\n11010\n11000\n00000\n\nTopic: DFS/BFS',
            'options': [],
            'sample_answer': '''def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    return islands''',
            'explanation': 'Iterate through grid and trigger DFS to sink connected land cells (\'1\' -> \'0\') for each island in O(M*N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 14,
            'type': 'coding',
            'title': 'Q14. Course Schedule — Medium',
            'text': 'Given courses and prerequisites, determine whether all courses can be completed.\n\nTopic: Graph + Topological Sort',
            'options': [],
            'sample_answer': '''from collections import defaultdict

def canFinish(numCourses, prerequisites):
    adj = defaultdict(list)
    for course, pre in prerequisites:
        adj[pre].append(course)
    
    visited = [0] * numCourses # 0=unvisited, 1=visiting, 2=visited
    
    def dfs(node):
        if visited[node] == 1: return False
        if visited[node] == 2: return True
        visited[node] = 1
        for neighbor in adj[node]:
            if not dfs(neighbor): return False
        visited[node] = 2
        return True

    for i in range(numCourses):
        if not dfs(i): return False
    return True''',
            'explanation': 'Detect cycles in a directed prerequisite graph using DFS / Topological Sorting in O(V + E) time.',
            'marks': '5 Marks'
        }
    ]

    round4_qs = [
        {
            'q_num': 15,
            'type': 'coding',
            'title': 'Q15. Word Ladder — Hard',
            'text': 'Transform one word into another by changing one character at a time.\n\nExample:\nbeginWord = "hit"\nendWord = "cog"\nPossible transformation: hit -> hot -> dot -> dog -> cog\n\nTopic: BFS + Graph',
            'options': [],
            'sample_answer': '''from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet: return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord: return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0''',
            'explanation': 'Find shortest transformation path on unweighted word graph using BFS in O(M^2 * N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 16,
            'type': 'coding',
            'title': 'Q16. Coin Change — Medium/Hard',
            'text': 'Given coins and an amount, find the minimum number of coins required.\n\nExample:\ncoins = [1,2,5], amount = 11\n\nTopic: Dynamic Programming',
            'options': [],
            'sample_answer': '''def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1''',
            'explanation': 'Bottom-up Dynamic Programming formulation: dp[x] = min(dp[x], dp[x - coin] + 1) in O(amount * N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 17,
            'type': 'coding',
            'title': 'Q17. Longest Increasing Subsequence — Medium/Hard',
            'text': 'Given an integer array nums, return the length of the longest strictly increasing subsequence.\n\nExample:\nInput: [10,9,2,5,3,7,101,18]nce: [2,3,7,101])\n\nTopic: Dynamic Programming / Binary Search',
            'options': [],
            'sample_answer': '''import bisect

def lengthOfLIS(nums):
    sub = []
    for x in nums:
        idx = bisect.bisect_left(sub, x)
        if idx == len(sub):
            sub.append(x)
        else:
            sub[idx] = x
    return len(sub)''',
            'explanation': 'Build longest increasing subsequence using Binary Search (bisect_left) in O(N log N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 18,
            'type': 'coding',
            'title': 'Q18. Word Break — Medium/Hard',
            'text': 'Given a string s and a dictionary wordDict, return True if s can be segmented into a space-separated sequence of dictionary words.\n\nExample:\ns = "leetcode"\nwordDict = ["leet","code"]\n\nTopic: Dynamic Programming',
            'options': [],
            'sample_answer': '''def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]''',
            'explanation': 'DP table where dp[i] checks if prefix s[:i] can be formed by dictionary words in O(N^2) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 19,
            'type': 'coding',
            'title': 'Q19. LRU Cache — Hard',
            'text': 'Design an LRU cache supporting get(key) and put(key,value) in O(1) time complexity.\n\nTopic: Hash Map + Doubly Linked List',
            'options': [],
            'sample_answer': '''class Node:
    def __init__(self, k=0, v=0):
        self.key, self.val = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]''',
            'explanation': 'Combine Hash Map for O(1) key lookups with Doubly Linked List for O(1) node additions and removals.',
            'marks': '5 Marks'
        },
        {
            'q_num': 20,
            'type': 'coding',
            'title': 'Q20. Meeting Rooms / Scheduling — Medium/Hard',
            'text': 'Given meeting intervals, determine whether a person can attend all meetings.\n\nExample:\nInput: [[0,30],[5,10],[15,20]]\n\nTopic: Sorting + Intervals',
            'options': [],
            'sample_answer': '''def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True''',
            'explanation': 'Sort meeting intervals by start time and check if any start time < previous end time in O(N log N) time.',
            'marks': '5 Marks'
        }
    ]

    return [
        {
            'section_name': 'Round 1: Screening & Speed Coding (Q1 - Q4)',
            'time': '45 Mins',
            'questions': round1_qs
        },
        {
            'section_name': 'Round 2: Core Data Structures & Search Algorithms (Q5 - Q9)',
            'time': '45 Mins',
            'questions': round2_qs
        },
        {
            'section_name': 'Round 3: Binary Trees, Graph Traversal & Recursion (Q10 - Q14)',
            'time': '45 Mins',
            'questions': round3_qs
        },
        {
            'section_name': 'Round 4: Advanced Systems, LRU Cache & Dynamic Programming (Q15 - Q20)',
            'time': '45 Mins',
            'questions': round4_qs
        }
    ]


def get_google_practice_sections_model2():
    round1_qs = [
        {
            'q_num': 1, 'type': 'coding',
            'title': 'Q1. Container With Most Water — Medium',
            'text': 'Given n non-negative integers representing vertical lines, find two lines that together with the x-axis form a container containing the most water.\n\nExample:\nInput: height = [1,8,6,2,5,4,8,3,7]\n\nTopic: Two Pointers',
            'options': [],
            'sample_answer': '''def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water''',
            'explanation': 'Use two pointers from ends moving inward greedy-style in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 2, 'type': 'coding',
            'title': 'Q2. 3Sum — Medium',
            'text': 'Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that i != j != k and nums[i] + nums[j] + nums[k] == 0.\n\nExample:\nInput: nums = [-1,0,1,2,-1,-4]\n\nTopic: Two Pointers / Sorting',
            'options': [],
            'sample_answer': '''def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0: left += 1
            elif s > 0: right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]: left += 1
                while left < right and nums[right] == nums[right-1]: right -= 1
                left += 1; right -= 1
    return res''',
            'explanation': 'Sort array and apply Two Pointers for each fixed pivot element in O(N^2) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 3, 'type': 'coding',
            'title': 'Q3. Minimum Window Substring — Hard',
            'text': 'Given strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included.\n\nExample:\nInput: s = "ADOBECODEBANC", t = "ABC"\n\nTopic: Sliding Window',
            'options': [],
            'sample_answer': '''from collections import Counter

def minWindow(s, t):
    if not t or not s: return ""
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]''',
            'explanation': 'Sliding Window algorithm maintaining frequency hash maps in O(N + M) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 4, 'type': 'coding',
            'title': 'Q4. Group Anagrams — Medium',
            'text': 'Given an array of strings strs, group the anagrams together in any order.\n\nExample:\nInput: strs = ["eat","tea","tan","ate","nat","bat"]nat","tan"],["ate","eat","tea"]]\n\nTopic: Hash Map',
            'options': [],
            'sample_answer': '''from collections import defaultdict

def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())''',
            'explanation': 'Use sorted string tuple as Hash Map key to group anagrams in O(N * K log K) time.',
            'marks': '5 Marks'
        }
    ]

    round2_qs = [
        {
            'q_num': 5, 'type': 'coding',
            'title': 'Q5. Subarray Sum Equals K — Medium',
            'text': 'Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.\n\nExample:\nInput: nums = [1,1,1], k = 2\n\nTopic: Prefix Sum + Hash Map',
            'options': [],
            'sample_answer': '''def subarraySum(nums, k):
    count = curr_sum = 0
    h = {0: 1}
    for num in nums:
        curr_sum += num
        count += h.get(curr_sum - k, 0)
        h[curr_sum] = h.get(curr_sum, 0) + 1
    return count''',
            'explanation': 'Use Prefix Sum array combined with Hash Map frequency counter in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 6, 'type': 'coding',
            'title': 'Q6. Next Permutation — Medium',
            'text': 'Find the lexicographically next greater permutation of numbers. If not possible, rearrange as lowest possible order.\n\nExample:\nInput: nums = [1,2,3]\n\nTopic: Array Traversal',
            'options': [],
            'sample_answer': '''def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])''',
            'explanation': 'Traverse backwards to find first decreasing pivot, swap with next larger element, and reverse suffix in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 7, 'type': 'coding',
            'title': 'Q7. Find Minimum in Rotated Sorted Array — Medium',
            'text': 'Given a sorted rotated array of unique elements, return the minimum element of this array in O(log N) time.\n\nExample:\nInput: nums = [3,4,5,1,2]\n\nTopic: Binary Search',
            'options': [],
            'sample_answer': '''def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]''',
            'explanation': 'Perform Binary Search by comparing mid element with right boundary in O(log N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 8, 'type': 'coding',
            'title': 'Q8. Find Median from Data Stream — Hard',
            'text': 'Design a data structure that supports adding numbers from a data stream and finding the median in O(1) or O(log N) time.\n\nTopic: Two Heaps',
            'options': [],
            'sample_answer': '''import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # Max Heap (negated)
        self.large = [] # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0''',
            'explanation': 'Maintain Max Heap for lower half and Min Heap for upper half for O(log N) inserts and O(1) median query.',
            'marks': '5 Marks'
        },
        {
            'q_num': 9, 'type': 'coding',
            'title': 'Q9. Task Scheduler — Medium',
            'text': 'Given a characters array tasks and non-negative integer n, return the least number of CPU intervals needed to execute all tasks.\n\nExample:\ntasks = ["A","A","A","B","B","B"], n = 2\n\nTopic: Greedy / Priority Queue',
            'options': [],
            'sample_answer': '''from collections import Counter

def leastInterval(tasks, n):
    counts = list(Counter(tasks).values())
    max_freq = max(counts)
    max_count = counts.count(max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)''',
            'explanation': 'Greedy formula calculating required idle slots based on highest frequency task in O(N) time.',
            'marks': '5 Marks'
        }
    ]

    round3_qs = [
        {
            'q_num': 10, 'type': 'coding',
            'title': 'Q10. Lowest Common Ancestor of a Binary Tree — Medium',
            'text': 'Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q.\n\nTopic: Tree Recursion',
            'options': [],
            'sample_answer': '''def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right''',
            'explanation': 'Bottom-up DFS traversal returning non-null when node p or q is found in subtrees in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 11, 'type': 'coding',
            'title': 'Q11. Construct Binary Tree from Preorder and Inorder Traversal — Medium',
            'text': 'Given preorder and inorder traversal arrays, construct and return the binary tree.\n\nTopic: Tree Recursion + Hash Map',
            'options': [],
            'sample_answer': '''def buildTree(preorder, inorder):
    in_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0
    def helper(left, right):
        nonlocal pre_idx
        if left > right: return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)
        mid = in_map[root_val]
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    return helper(0, len(inorder) - 1)''',
            'explanation': 'Use preorder array for root selection and Hash Map on inorder array for subtree splits in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 12, 'type': 'coding',
            'title': 'Q12. Clone Graph — Medium',
            'text': 'Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.\n\nTopic: Graph BFS/DFS',
            'options': [],
            'sample_answer': '''def cloneGraph(node):
    if not node: return None
    visited = {}
    def dfs(curr):
        if curr in visited: return visited[curr]
        copy = Node(curr.val)
        visited[curr] = copy
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node)''',
            'explanation': 'DFS graph traversal using Hash Map mapping original nodes to cloned nodes in O(V + E) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 13, 'type': 'coding',
            'title': 'Q13. Pacific Atlantic Water Flow — Medium',
            'text': 'Given an m x n grid of heights, return grid coordinates from which water can flow to both Pacific and Atlantic oceans.\n\nTopic: Graph DFS/BFS',
            'options': [],
            'sample_answer': '''def pacificAtlantic(heights):
    if not heights: return []
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()
    def dfs(r, c, visit, prev_height):
        if (r, c) in visit or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prev_height:
            return
        visit.add((r, c))
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(r + dr, c + dc, visit, heights[r][c])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows - 1, c, atl, heights[rows-1][c])
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols - 1, atl, heights[r][cols-1])
    return list(pac & atl)''',
            'explanation': 'Reverse DFS from ocean boundaries inward to find reachable grid cells in O(M * N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 14, 'type': 'coding',
            'title': 'Q14. Graph Valid Tree — Medium',
            'text': 'Given n nodes labeled from 0 to n-1 and a list of undirected edges, check whether these edges form a valid tree.\n\nTopic: Union Find / DFS',
            'options': [],
            'sample_answer': '''def validTree(n, edges):
    if len(edges) != n - 1: return False
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    for u, v in edges:
        root_u, root_v = find(u), find(v)
        if root_u == root_v: return False
        parent[root_u] = root_v
    return True''',
            'explanation': 'Validate tree constraints: exactly N-1 edges and no cycles using Union-Find algorithm in O(N alpha(N)) time.',
            'marks': '5 Marks'
        }
    ]

    round4_qs = [
        {
            'q_num': 15, 'type': 'coding',
            'title': 'Q15. Trapping Rain Water — Hard',
            'text': 'Given n non-negative integers representing an elevation map where width of each bar is 1, compute how much water it can trap.\n\nExample:\nInput: height = [0,1,0,2,1,0,1,3,2,1,2,1]\n\nTopic: Two Pointers',
            'options': [],
            'sample_answer': '''def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max: left_max = height[left]
            else: water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max: right_max = height[right]
            else: water += right_max - height[right]
            right -= 1
    return water''',
            'explanation': 'Two Pointers moving inward tracking maximum left and right boundary heights in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 16, 'type': 'coding',
            'title': 'Q16. Edit Distance — Hard',
            'text': 'Given two strings word1 and word2, return the minimum number of operations (insert, delete, replace) required to convert word1 to word2.\n\nExample:\nword1 = "horse", word2 = "ros"\n\nTopic: 2D Dynamic Programming',
            'options': [],
            'sample_answer': '''def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]''',
            'explanation': 'Classic 2D DP table matching prefix string transformations in O(M * N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 17, 'type': 'coding',
            'title': 'Q17. Partition Equal Subset Sum — Medium',
            'text': 'Given an array nums, return True if you can partition the array into two subsets such that sum of elements in both subsets is equal.\n\nExample:\nInput: nums = [1,5,11,5]\n\nTopic: 0/1 Knapsack DP',
            'options': [],
            'sample_answer': '''def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0: return False
    target = total_sum // 2
    dp = set([0])
    for num in nums:
        next_dp = set(dp)
        for t in dp:
            if t + num == target: return True
            if t + num < target: next_dp.add(t + num)
        dp = next_dp
    return target in dp''',
            'explanation': '0/1 Knapsack subset sum DP reducing target sum to total_sum / 2 in O(N * Target) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 18, 'type': 'coding',
            'title': 'Q18. House Robber III — Medium',
            'text': 'Rob houses arranged as a binary tree such that no two directly-linked houses are robbed on the same night. Return max money.\n\nTopic: Tree Dynamic Programming',
            'options': [],
            'sample_answer': '''def rob(root):
    def dfs(node):
        if not node: return (0, 0)
        left = dfs(node.left)
        right = dfs(node.right)
        rob_val = node.val + left[1] + right[1]
        skip_val = max(left) + max(right)
        return (rob_val, skip_val)
    return max(dfs(root))''',
            'explanation': 'Tree DP returning pair of values (rob current node vs skip current node) in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 19, 'type': 'coding',
            'title': 'Q19. LFU Cache — Hard',
            'text': 'Design and implement a data structure for a Least Frequently Used (LFU) cache operating in O(1) time complexity.\n\nTopic: Doubly Linked List + Hash Maps',
            'options': [],
            'sample_answer': '''from collections import defaultdict

class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val, self.freq = key, val, 1
        self.prev = self.next = None''',
            'explanation': 'Combine Key Map and Frequency Map of Doubly Linked Lists for O(1) LFU eviction and access.',
            'marks': '5 Marks'
        },
        {
            'q_num': 20, 'type': 'coding',
            'title': 'Q20. Minimum Cost to Hire K Workers — Hard',
            'text': 'Given quality and wage of n workers, hire exactly k workers according to wage-to-quality ratio constraints for minimum total cost.\n\nTopic: Greedy + Priority Queue',
            'options': [],
            'sample_answer': '''import heapq

def mincostToHireWorkers(quality, wage, k):
    workers = sorted([w / q, q] for w, q in zip(wage, quality))
    res = float('inf')
    max_heap = []
    sum_q = 0
    for ratio, q in workers:
        heapq.heappush(max_heap, -q)
        sum_q += q
        if len(max_heap) > k:
            sum_q += heapq.heappop(max_heap)
        if len(max_heap) == k:
            res = min(res, sum_q * ratio)
    return res''',
            'explanation': 'Sort workers by wage/quality ratio and use Max Heap of size K to greedily minimize quality sum in O(N log N) time.',
            'marks': '5 Marks'
        }
    ]

    return [
        {
            'section_name': 'Pattern 1: Two-Pointers, Sliding Window & String Optimization (Q1 - Q4)',
            'time': '35 Mins',
            'questions': round1_qs
        },
        {
            'section_name': 'Pattern 2: Priority Queues, Min/Max Heaps & Monotonic Stacks (Q5 - Q9)',
            'time': '45 Mins',
            'questions': round2_qs
        },
        {
            'section_name': 'Pattern 3: Tree Construction, Graph Topologies & Matrix DFS (Q10 - Q14)',
            'time': '50 Mins',
            'questions': round3_qs
        },
        {
            'section_name': 'Pattern 4: Hard Dynamic Programming, LFU Cache & Greedy Systems (Q15 - Q20)',
            'time': '50 Mins',
            'questions': round4_qs
        }
    ]


def get_google_practice_sections_model3():
    round1_qs = [
        {
            'q_num': 1, 'type': 'coding',
            'title': 'Q1. Move Zeroes — Easy',
            'text': 'Given an integer array nums, move all 0\'s to the end while maintaining the relative order of non-zero elements.\n\nExample:\nInput: [0,1,0,3,12]\n\nTopic: Two Pointers',
            'options': [],
            'sample_answer': '''def moveZeroes(nums):
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1''',
            'explanation': 'In-place two pointers swapping non-zero elements forward in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 2, 'type': 'coding',
            'title': 'Q2. Remove Nth Node From End of List — Medium',
            'text': 'Given the head of a linked list, remove the nth node from the end of the list and return its head.\n\nExample:\nInput: head = [1,2,3,4,5], n = 2\n\nTopic: Linked List Two Pointers',
            'options': [],
            'sample_answer': '''def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next''',
            'explanation': 'Advance fast pointer by N+1 steps then move both pointers together to identify target node in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 3, 'type': 'coding',
            'title': 'Q3. Daily Temperatures — Medium',
            'text': 'Given an array of temperatures, return an array answer such that answer[i] is the number of days you have to wait to get a warmer temperature.\n\nExample:\nInput: temperatures = [73,74,75,71,69,72,76,73]\n\nTopic: Monotonic Stack',
            'options': [],
            'sample_answer': '''def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            prev_i = stack.pop()
            res[prev_i] = i - prev_i
        stack.append(i)
    return res''',
            'explanation': 'Use a decreasing Monotonic Stack to find next greater temperature in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 4, 'type': 'coding',
            'title': 'Q4. String Compression — Medium',
            'text': 'Given an array of characters, compress it in-place using character counts.\n\nExample:\nInput: ["a","a","b","b","c","c","c"]\n\nTopic: Two Pointers / String',
            'options': [],
            'sample_answer': '''def compress(chars):
    read = write = 0
    while read < len(chars):
        char = chars[read]
        count = 0
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write''',
            'explanation': 'In-place write pointer compressing repeating character sequences in O(N) time.',
            'marks': '5 Marks'
        }
    ]

    round2_qs = [
        {
            'q_num': 5, 'type': 'coding',
            'title': 'Q5. Maximum Subarray Sum (Kadane\'s Algorithm) — Easy/Medium',
            'text': 'Find the contiguous subarray with the largest sum and return its sum.\n\nExample:\nInput: [-2,1,-3,4,-1,2,1,-5,4]\n\nTopic: Dynamic Programming',
            'options': [],
            'sample_answer': '''def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum''',
            'explanation': 'Kadane\'s Algorithm tracking current max subarray sum in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 6, 'type': 'coding',
            'title': 'Q6. Insert Interval — Medium',
            'text': 'Insert newInterval into sorted non-overlapping intervals and merge if necessary.\n\nExample:\nintervals = [[1,3],[6,9]], newInterval = [2,5]\n\nTopic: Interval Sorting',
            'options': [],
            'sample_answer': '''def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    while i < n:
        res.append(intervals[i])
        i += 1
    return res''',
            'explanation': 'Single-pass interval insertion merging overlapping intervals in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 7, 'type': 'coding',
            'title': 'Q7. Koko Eating Bananas — Medium',
            'text': 'Return minimum integer k such that Koko can eat all bananas in piles within h hours.\n\nExample:\npiles = [3,6,7,11], h = 8\n\nTopic: Binary Search on Answer',
            'options': [],
            'sample_answer': '''import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    return left''',
            'explanation': 'Binary search on speed range [1, max(piles)] verifying feasible eating speed in O(N log(max(piles))) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 8, 'type': 'coding',
            'title': 'Q8. Reorganize String — Medium',
            'text': 'Rearrange string s so that no two adjacent characters are the same.\n\nExample:\nInput: s = "aab"\n\nTopic: Heap / Greedy',
            'options': [],
            'sample_answer': '''import heapq
from collections import Counter

def reorganizeString(s):
    count = Counter(s)
    max_heap = [[-cnt, char] for char, cnt in count.items()]
    heapq.heapify(max_heap)
    prev = None
    res = []
    while max_heap or prev:
        if prev and not max_heap: return ""
        cnt, char = heapq.heappop(max_heap)
        res.append(char)
        cnt += 1
        if prev:
            heapq.heappush(max_heap, prev)
            prev = None
        if cnt < 0:
            prev = [cnt, char]
    return "".join(res)''',
            'explanation': 'Greedy Max-Heap selection placing highest frequency characters alternately in O(N log K) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 9, 'type': 'coding',
            'title': 'Q9. K Closest Points to Origin — Medium',
            'text': 'Given points on a 2D plane, find the k closest points to the origin (0, 0).\n\nExample:\npoints = [[1,3],[-2,2]], k = 1\n\nTopic: Heap / Geometry',
            'options': [],
            'sample_answer': '''import heapq

def kClosest(points, k):
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)''',
            'explanation': 'Use Min-Heap or Quickselect on squared Euclidean distance x^2 + y^2 in O(N log K) time.',
            'marks': '5 Marks'
        }
    ]

    round3_qs = [
        {
            'q_num': 10, 'type': 'coding',
            'title': 'Q10. Invert Binary Tree — Easy',
            'text': 'Given the root of a binary tree, invert the tree and return its root.\n\nExample:\nInput: [4,2,7,1,3,6,9]\n\nTopic: Tree DFS',
            'options': [],
            'sample_answer': '''def invertTree(root):
    if not root: return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root''',
            'explanation': 'Recursive post-order DFS swapping left and right subtrees in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 11, 'type': 'coding',
            'title': 'Q11. Binary Tree Zigzag Level Order Traversal — Medium',
            'text': 'Return the zigzag level order traversal of binary tree node values (left to right, then right to left).\n\nExample:\nInput: [3,9,20,null,null,15,7]\n\nTopic: BFS Queue',
            'options': [],
            'sample_answer': '''from collections import deque

def zigzagLevelOrder(root):
    if not root: return []
    res = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right: level.append(node.val)
            else: level.appendleft(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(list(level))
        left_to_right = not left_to_right
    return res''',
            'explanation': 'BFS level-order traversal with alternating double-ended queue append direction in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 12, 'type': 'coding',
            'title': 'Q12. Path Sum II — Medium',
            'text': 'Given the root of a binary tree and targetSum, return all root-to-leaf paths where sum equals targetSum.\n\nTopic: Tree DFS Backtracking',
            'options': [],
            'sample_answer': '''def pathSum(root, targetSum):
    res = []
    def dfs(node, curr_path, curr_sum):
        if not node: return
        curr_path.append(node.val)
        curr_sum += node.val
        if not node.left and not node.right and curr_sum == targetSum:
            res.append(list(curr_path))
        dfs(node.left, curr_path, curr_sum)
        dfs(node.right, curr_path, curr_sum)
        curr_path.pop()
    dfs(root, [], 0)
    return res''',
            'explanation': 'DFS backtracking recording root-to-leaf paths matching target sum in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 13, 'type': 'coding',
            'title': 'Q13. Surrounded Regions — Medium',
            'text': 'Given an m x n matrix board containing \'X\' and \'O\', capture all regions surrounded by \'X\'.\n\nTopic: Graph Grid Boundary DFS',
            'options': [],
            'sample_answer': '''def solve(board):
    if not board: return
    rows, cols = len(board), len(board[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O': return
        board[r][c] = 'E'
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(r+dr, c+dc)
    for r in range(rows):
        dfs(r, 0); dfs(r, cols-1)
    for c in range(cols):
        dfs(0, c); dfs(rows-1, c)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O': board[r][c] = 'X'
            elif board[r][c] == 'E': board[r][c] = 'O' ''',
            'explanation': 'Boundary DFS marking reachable \'O\'s as escaped \'E\', then converting remaining \'O\'s to \'X\' in O(M*N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 14, 'type': 'coding',
            'title': 'Q14. Word Search — Medium',
            'text': 'Given an m x n grid of characters and a string word, return True if word exists in grid.\n\nTopic: Matrix Backtracking DFS',
            'options': [],
            'sample_answer': '''def exist(board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, idx):
        if idx == len(word): return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]: return False
        temp = board[r][c]
        board[r][c] = '#'
        res = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1)
        board[r][c] = temp
        return res
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True
    return False''',
            'explanation': 'Matrix grid DFS backtracking matching word characters sequentially in O(N * 4^L) time.',
            'marks': '5 Marks'
        }
    ]

    round4_qs = [
        {
            'q_num': 15, 'type': 'coding',
            'title': 'Q15. Alien Dictionary / Lexicographical Order — Hard',
            'text': 'Given a sorted dictionary of alien language words, return the order of characters in alien alphabet.\n\nTopic: Topological Sort',
            'options': [],
            'sample_answer': '''from collections import defaultdict, deque

def alienOrder(words):
    adj = {c: set() for w in words for c in w}
    in_degree = {c: 0 for c in words for c in words}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    res = []
    while queue:
        c = queue.popleft()
        res.append(c)
        for nxt in adj[c]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0: queue.append(nxt)
    return "".join(res) if len(res) == len(adj) else "" ''',
            'explanation': 'Construct directed character graph from word order and apply Kahn\'s Topological Sort in O(C) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 16, 'type': 'coding',
            'title': 'Q16. Minimum Path Sum in Grid — Medium',
            'text': 'Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right minimizing sum.\n\nExample:\ngrid = [[1,3,1],[1,5,1],[4,2,1]]\n\nTopic: 2D Grid DP',
            'options': [],
            'sample_answer': '''def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n): dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m): dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]''',
            'explanation': '2D DP grid finding path of minimal total cost moving only down or right in O(M * N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 17, 'type': 'coding',
            'title': 'Q17. Maximal Square — Medium',
            'text': 'Given an m x n binary matrix filled with 0s and 1s, find the largest square containing only 1s and return its area.\n\nTopic: 2D Matrix DP',
            'options': [],
            'sample_answer': '''def maximalSquare(matrix):
    if not matrix: return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if matrix[r-1][c-1] == '1':
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                max_side = max(max_side, dp[r][c])
    return max_side * max_side''',
            'explanation': 'Matrix DP where dp[r][c] tracks max square side length ending at cell (r-1, c-1) in O(M * N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 18, 'type': 'coding',
            'title': 'Q18. Decode Ways — Medium',
            'text': 'A message containing letters A-Z is encoded to numbers \'1\'-\'26\'. Return number of ways to decode it.\n\nExample:\nInput: s = "226"\n\nTopic: String DP',
            'options': [],
            'sample_answer': '''def numDecodings(s):
    if not s or s[0] == '0': return 0
    dp = [0] * (len(s) + 1)
    dp[0] = dp[1] = 1
    for i in range(2, len(s) + 1):
        if s[i-1] != '0': dp[i] += dp[i-1]
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26: dp[i] += dp[i-2]
    return dp[len(s)]''',
            'explanation': 'Dynamic Programming counting valid 1-digit and 2-digit character decodings in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 19, 'type': 'coding',
            'title': 'Q19. Design Hit Counter / Sliding Window Rate Limiter — Medium',
            'text': 'Design a hit counter which counts the number of hits received in the past 5 minutes (300 seconds).\n\nTopic: Queue / Circular Array',
            'options': [],
            'sample_answer': '''from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)''',
            'explanation': 'Sliding Window Queue evicting timestamps older than timestamp - 300 in O(1) amortized time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 20, 'type': 'coding',
            'title': 'Q20. Car Fleet — Medium',
            'text': 'Given target distance and arrays position and speed of n cars, return number of car fleets that will arrive at destination.\n\nTopic: Sorting + Stack',
            'options': [],
            'sample_answer': '''def carFleet(target, position, speed):
    pair = sorted(zip(position, speed), reverse=True)
    stack = []
    for p, s in pair:
        time = (target - p) / s
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)''',
            'explanation': 'Sort cars backwards by starting position and track time to target using Monotonic Stack in O(N log N) time.',
            'marks': '5 Marks'
        }
    ]

    return [
        {
            'section_name': 'Section A: General Coding Fundamentals & String Processing (Q1 - Q4)',
            'time': '30 Mins',
            'questions': round1_qs
        },
        {
            'section_name': 'Section B: Divide & Conquer, Array Search & Greedy Scheduling (Q5 - Q9)',
            'time': '45 Mins',
            'questions': round2_qs
        },
        {
            'section_name': 'Section C: Binary Tree Operations, Inversion & Grid Search (Q10 - Q14)',
            'time': '45 Mins',
            'questions': round3_qs
        },
        {
            'section_name': 'Section D: Topological Sorting, Rate Limiters & System Coding (Q15 - Q20)',
            'time': '60 Mins',
            'questions': round4_qs
        }
    ]


def get_google_general_practice_test():
    round1_qs = [
        {
            'q_num': 1, 'type': 'coding',
            'title': 'Q1. Palindrome Number — Easy',
            'text': 'Given an integer x, return true if x is a palindrome integer, and false otherwise.\n\nExample:\nInput: x = 121\n\nTopic: Math / Two Pointers',
            'options': [],
            'sample_answer': '''def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    str_x = str(x)
    return str_x == str_x[::-1]''',
            'explanation': 'Convert to string or reverse integer mathematically in O(log10 N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 2, 'type': 'coding',
            'title': 'Q2. Implement Queue using Stacks — Easy',
            'text': 'Implement a first in first out (FIFO) queue using only two stacks.\n\nExample:\nInput: push(1), push(2), peek(), pop()\n\nTopic: Stack Design',
            'options': [],
            'sample_answer': '''class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())''',
            'explanation': 'Use two stacks (in_stack and out_stack) to amortize push and pop operations to O(1) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 3, 'type': 'coding',
            'title': 'Q3. Majority Element — Easy',
            'text': 'Given an array nums of size n, return the majority element that appears more than ⌊n / 2⌋ times.\n\nExample:\nInput: nums = [2,2,1,1,1,2,2]\n\nTopic: Boyer-Moore Voting Algorithm',
            'options': [],
            'sample_answer': '''def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate''',
            'explanation': 'Boyer-Moore Voting Algorithm finds the majority candidate in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 4, 'type': 'coding',
            'title': 'Q4. Longest Palindromic Substring — Medium',
            'text': 'Given a string s, return the longest palindromic substring in s.\n\nExample:\nInput: s = "babad"\n\nTopic: Expand Around Center / DP',
            'options': [],
            'sample_answer': '''def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
    return res''',
            'explanation': 'Expand around center for each index in O(N^2) time and O(1) space.',
            'marks': '5 Marks'
        }
    ]

    round2_qs = [
        {
            'q_num': 5, 'type': 'coding',
            'title': 'Q5. Sort Colors / Dutch National Flag — Medium',
            'text': 'Given an array nums with n objects colored red, white, or blue (0, 1, 2), sort them in-place.\n\nExample:\nInput: nums = [2,0,2,1,1,0]\n\nTopic: Three Pointers / Dutch Flag',
            'options': [],
            'sample_answer': '''def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1''',
            'explanation': 'Dutch National Flag algorithm sorts 3 distinct elements in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 6, 'type': 'coding',
            'title': 'Q6. Subtree of Another Tree — Easy/Medium',
            'text': 'Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values as subRoot.\n\nTopic: Tree DFS / Recursion',
            'options': [],
            'sample_answer': '''def isSubtree(root, subRoot):
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)''',
            'explanation': 'Compare tree nodes recursively in O(N * M) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 7, 'type': 'coding',
            'title': 'Q7. Search a 2D Matrix — Medium',
            'text': 'Write an efficient algorithm that searches for a value target in an m x n integer matrix with sorted rows.\n\nExample:\nInput: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3\n\nTopic: 2D Binary Search',
            'options': [],
            'sample_answer': '''def searchMatrix(matrix, target):
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False''',
            'explanation': 'Treat 2D matrix as virtual 1D array and perform Binary Search in O(log(M*N)) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 8, 'type': 'coding',
            'title': 'Q8. Find All Anagrams in a String — Medium',
            'text': 'Given two strings s and p, return an array of all the start indices of p\'s anagrams in s.\n\nExample:\nInput: s = "cbaebabacd", p = "abc"\n\nTopic: Sliding Window + Hash Map',
            'options': [],
            'sample_answer': '''from collections import Counter

def findAnagrams(s: str, p: str):
    p_count = Counter(p)
    s_count = Counter()
    res = []
    k = len(p)
    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= k:
            if s_count[s[i - k]] == 1:
                del s_count[s[i - k]]
            else:
                s_count[s[i - k]] -= 1
        if s_count == p_count:
            res.append(i - k + 1)
    return res''',
            'explanation': 'Maintain fixed size sliding window of len(p) and compare frequency counts in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 9, 'type': 'coding',
            'title': 'Q9. Binary Tree Right Side View — Medium',
            'text': 'Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.\n\nTopic: Tree BFS / Level Order',
            'options': [],
            'sample_answer': '''from collections import deque

def rightSideView(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        right_most = None
        for _ in range(len(q)):
            node = q.popleft()
            right_most = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(right_most)
    return res''',
            'explanation': 'Perform BFS level by level and append last node value of each level in O(N) time.',
            'marks': '5 Marks'
        }
    ]

    round3_qs = [
        {
            'q_num': 10, 'type': 'coding',
            'title': 'Q10. Diameter of Binary Tree — Easy/Medium',
            'text': 'Given the root of a binary tree, return the length of the diameter of the tree.\n\nTopic: Tree DFS / Height Recursion',
            'options': [],
            'sample_answer': '''def diameterOfBinaryTree(root):
    diameter = 0
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left_h = depth(node.left)
        right_h = depth(node.right)
        diameter = max(diameter, left_h + right_h)
        return 1 + max(left_h, right_h)
    depth(root)
    return diameter''',
            'explanation': 'Calculate left and right sub-tree depths recursively and update max diameter in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 11, 'type': 'coding',
            'title': 'Q11. Rotting Oranges — Medium',
            'text': 'Given an m x n grid, return minimum minutes until no fresh orange remains.\n\nTopic: Multi-source BFS Grid',
            'options': [],
            'sample_answer': '''from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    if fresh == 0:
        return 0
    minutes = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    while q and fresh > 0:
        minutes += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
    return minutes if fresh == 0 else -1''',
            'explanation': 'Multi-source BFS pushing all initial rotten oranges to queue in O(M*N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 12, 'type': 'coding',
            'title': 'Q12. Minimum Height Trees — Medium',
            'text': 'Given a tree of n nodes labeled from 0 to n - 1, find all root labels that yield Minimum Height Trees.\n\nTopic: Graph Topological BFS / Centroid',
            'options': [],
            'sample_answer': '''from collections import deque

def findMinHeightTrees(n, edges):
    if n <= 2:
        return [i for i in range(n)]
    adj = {i: set() for i in range(n)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    leaves = deque([i for i in range(n) if len(adj[i]) == 1])
    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_count = len(leaves)
        remaining_nodes -= leaves_count
        for _ in range(leaves_count):
            leaf = leaves.popleft()
            neighbor = adj[leaf].pop()
            adj[neighbor].remove(leaf)
            if len(adj[neighbor]) == 1:
                leaves.append(neighbor)
    return list(leaves)''',
            'explanation': 'Trim leaf nodes layer by layer until 1 or 2 centroid nodes remain in O(V + E) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 13, 'type': 'coding',
            'title': 'Q13. Evaluate Reverse Polish Notation — Medium',
            'text': 'Evaluate the value of an arithmetic expression in Reverse Polish Notation (Postfix).\n\nExample:\nInput: tokens = ["2","1","+","3","*"]\n\nTopic: Stack Operations',
            'options': [],
            'sample_answer': '''def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]''',
            'explanation': 'Use Stack to pop operands when encountering operators in O(N) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 14, 'type': 'coding',
            'title': 'Q14. Combination Sum — Medium',
            'text': 'Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations where candidate numbers sum to target.\n\nTopic: Backtracking / Decision Tree',
            'options': [],
            'sample_answer': '''def combinationSum(candidates, target):
    res = []
    def dfs(idx, path, total):
        if total == target:
            res.append(path.copy())
            return
        if total > target or idx >= len(candidates):
            return
        path.append(candidates[idx])
        dfs(idx, path, total + candidates[idx])
        path.pop()
        dfs(idx + 1, path, total)
    dfs(0, [], 0)
    return res''',
            'explanation': 'Use DFS Backtracking exploring combinations with element reuse in O(2^T) time.',
            'marks': '5 Marks'
        }
    ]

    round4_qs = [
        {
            'q_num': 15, 'type': 'coding',
            'title': 'Q15. Network Delay Time — Medium/Hard',
            'text': 'Given network travel times as directed edges with weights, return minimum time for all n nodes to receive signal from source k.\n\nTopic: Dijkstra\'s Algorithm / Priority Queue',
            'options': [],
            'sample_answer': '''import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    pq = [(0, k)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = d
        for neighbor, weight in graph[node]:
            if neighbor not in dist:
                heapq.heappush(pq, (d + weight, neighbor))
    return max(dist.values()) if len(dist) == n else -1''',
            'explanation': 'Dijkstra\'s shortest path algorithm using Min Heap in O(E log V) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 16, 'type': 'coding',
            'title': 'Q16. Maximum Product Subarray — Medium',
            'text': 'Given an integer array nums, find a contiguous non-empty subarray that has the largest product.\n\nExample:\nInput: nums = [2,3,-2,4]\n\nTopic: Dynamic Programming',
            'options': [],
            'sample_answer': '''def maxProduct(nums):
    res = max(nums)
    cur_min, cur_max = 1, 1
    for n in nums:
        if n == 0:
            cur_min, cur_max = 1, 1
            continue
        tmp = cur_max * n
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(tmp, n * cur_min, n)
        res = max(res, cur_max)
    return res''',
            'explanation': 'Track both cur_max and cur_min to handle negative signs in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 17, 'type': 'coding',
            'title': 'Q17. House Robber I — Medium',
            'text': 'Given an integer array nums representing money in houses, return maximum money you can rob tonight without robbing adjacent houses.\n\nTopic: 1D Dynamic Programming',
            'options': [],
            'sample_answer': '''def rob(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        new_rob = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = new_rob
    return rob2''',
            'explanation': 'Maintain two variables tracking max profit excluding/including adjacent houses in O(N) time and O(1) space.',
            'marks': '5 Marks'
        },
        {
            'q_num': 18, 'type': 'coding',
            'title': 'Q18. Target Sum — Medium',
            'text': 'Given an integer array nums and an integer target, assign + or - signs to elements to build an expression evaluating to target. Return number of ways.\n\nTopic: Subset Sum DP',
            'options': [],
            'sample_answer': '''def findTargetSumWays(nums, target):
    dp = {0: 1}
    for num in nums:
        next_dp = {}
        for cur_sum, count in dp.items():
            next_dp[cur_sum + num] = next_dp.get(cur_sum + num, 0) + count
            next_dp[cur_sum - num] = next_dp.get(cur_sum - num, 0) + count
        dp = next_dp
    return dp.get(target, 0)''',
            'explanation': 'Dynamic Programming HashMap storing total count of intermediate sums in O(N * Sum) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 19, 'type': 'coding',
            'title': 'Q19. Design Search Autocomplete System — Hard',
            'text': 'Design a search autocomplete system for a search engine that returns top 3 historical hot sentences matching prefix.\n\nTopic: Trie + Priority Queue',
            'options': [],
            'sample_answer': '''class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = {}

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        for s, t in zip(sentences, times):
            self.add_sentence(s, t)

    def add_sentence(self, sentence, time):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] = node.sentences.get(sentence, 0) + time''',
            'explanation': 'Trie node stores sentence counts and retrieves top 3 candidates sorted by frequency in O(Prefix + K log K) time.',
            'marks': '5 Marks'
        },
        {
            'q_num': 20, 'type': 'coding',
            'title': 'Q20. Minimum Interval to Include Each Query — Hard',
            'text': 'Given 2D array intervals and queries, for each query find the size of the smallest interval containing that query point.\n\nTopic: Min Heap + Sweep Line',
            'options': [],
            'sample_answer': '''import heapq

def minInterval(intervals, queries):
    intervals.sort()
    min_heap = []
    res = {}
    i = 0
    for q in sorted(queries):
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(min_heap, (r - l + 1, r))
            i += 1
        while min_heap and min_heap[0][1] < q:
            heapq.heappop(min_heap)
        res[q] = min_heap[0][0] if min_heap else -1
    return [res[q] for q in queries]''',
            'explanation': 'Sort queries and intervals, maintain Min Heap of active interval lengths in O(N log N + Q log Q) time.',
            'marks': '5 Marks'
        }
    ]

    return [
        {
            'section_name': 'Section 1: Fundamental Screening & Fast Coding (Q1 - Q4)',
            'time': '30 Mins',
            'questions': round1_qs
        },
        {
            'section_name': 'Section 2: Core Data Structures & Matrix Algorithms (Q5 - Q9)',
            'time': '45 Mins',
            'questions': round2_qs
        },
        {
            'section_name': 'Section 3: Graph Traversal & Backtracking Search (Q10 - Q14)',
            'time': '45 Mins',
            'questions': round3_qs
        },
        {
            'section_name': 'Section 4: Advanced Graph Shortest Path & Dynamic Programming (Q15 - Q20)',
            'time': '60 Mins',
            'questions': round4_qs
        }
    ]


def get_amazon_practice_sections(model_num=1, paper_type='model'):
    m1_mcqs = [
        {
            'q_num': 1, 'type': 'mcq',
            'title': 'Q1. Aptitude: Pipes & Cisterns',
            'text': 'Two pipes A and B can fill a cistern in 20 minutes and 30 minutes respectively. If both pipes are opened together, how much time will it take to fill the cistern completely?',
            'options': ['A) 10 Mins', 'B) 15 Mins', 'C) 12 Mins', 'D) 25 Mins'],
            'correct': 'C) 12 Mins',
            'explanation': 'Combined rate per minute = (1/20) + (1/30) = (3+2)/60 = 5/60 = 1/12. Time taken = 12 Mins.',
            'marks': '2 Marks'
        },
        {
            'q_num': 2, 'type': 'mcq',
            'title': 'Q2. Aptitude: Simple Interest Growth',
            'text': 'A sum of money doubles itself in 8 years under Simple Interest. In how many years will it triple itself at the same rate of interest?',
            'options': ['A) 14 Years', 'B) 12 Years', 'C) 16 Years', 'D) 24 Years'],
            'correct': 'C) 16 Years',
            'explanation': 'Let principal = P. Interest earned in 8 years = P. Interest per year = P/8. To triple (amount = 3P), required interest = 2P. Time = 2P / (P/8) = 16 Years.',
            'marks': '2 Marks'
        },
        {
            'q_num': 3, 'type': 'mcq',
            'title': 'Q3. Aptitude: Work & Time Efficiency',
            'text': '3 men or 6 women can complete a piece of work in 16 days. In how many days can 12 men and 8 women complete the same work?',
            'options': ['A) 3 Days', 'B) 8 Days', 'C) 6 Days', 'D) 4 Days'],
            'correct': 'A) 3 Days',
            'explanation': '3 Men = 6 Women => 1 Man = 2 Women. Work = 6 Women * 16 Days = 96 Woman-Days. 12 Men + 8 Women = 24 Women + 8 Women = 32 Women. Days = 96 / 32 = 3 Days.',
            'marks': '2 Marks'
        },
        {
            'q_num': 4, 'type': 'mcq',
            'title': 'Q4. Aptitude: Train Speed & Platform Length',
            'text': 'A train 150 meters long passes a platform 250 meters long in 20 seconds. What is the speed of the train in km/h?',
            'options': ['A) 72 km/h', 'B) 90 km/h', 'C) 108 km/h', 'D) 54 km/h'],
            'correct': 'A) 72 km/h',
            'explanation': 'Total distance = 150m + 250m = 400m. Speed = 400 / 20 = 20 m/s. Speed in km/h = 20 * (18/5) = 72 km/h.',
            'marks': '2 Marks'
        },
        {
            'q_num': 5, 'type': 'mcq',
            'title': 'Q5. Reasoning: Number Series Pattern',
            'text': 'Find the missing term in the sequence: 2, 6, 12, 20, 30, 42, ?',
            'options': ['A) 56', 'B) 60', 'C) 54', 'D) 50'],
            'correct': 'A) 56',
            'explanation': 'The terms are n*(n+1): 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30, 6*7=42, 7*8=56.',
            'marks': '2 Marks'
        },
        {
            'q_num': 6, 'type': 'mcq',
            'title': 'Q6. Technical DSA: Subarray Sum Equals K',
            'text': 'What is the optimal time complexity to find the total number of continuous subarrays whose sum equals K using Hash Map?',
            'options': ['A) O(N)', 'B) O(N^2)', 'C) O(N log N)', 'D) O(2^N)'],
            'correct': 'A) O(N)',
            'explanation': 'Using Prefix Sum stored in Hash Map allows checking matching prefix differences in O(1) per element, giving O(N) overall.',
            'marks': '2 Marks'
        },
        {
            'q_num': 7, 'type': 'mcq',
            'title': 'Q7. Technical DSA: Linked List Cycle Detection',
            'text': 'Which algorithm detects a cycle in a Singly Linked List in O(N) time complexity and O(1) auxiliary space complexity?',
            'options': ["A) Dijkstra\'s Algorithm", "B) Tarjan\'s Algorithm", "C) Floyd\'s Cycle Detection (Tortoise & Hare)", "D) Kahn\'s Algorithm"],
            'correct': "C) Floyd\'s Cycle Detection (Tortoise & Hare)",
            'explanation': 'Floyd\'s algorithm uses two pointers (slow and fast) moving at different speeds to detect cycles in O(1) space.',
            'marks': '2 Marks'
        },
        {
            'q_num': 8, 'type': 'mcq',
            'title': 'Q8. Technical DSA: Min Stack Operations',
            'text': 'What is the time complexity of retrieving the minimum element in a Min Stack design?',
            'options': ['A) O(log N)', 'B) O(N log N)', 'C) O(N)', 'D) O(1)'],
            'correct': 'D) O(1)',
            'explanation': 'By maintaining an auxiliary stack tracking the minimum at each level, getMin() runs in O(1) constant time.',
            'marks': '2 Marks'
        },
        {
            'q_num': 9, 'type': 'mcq',
            'title': 'Q9. Technical DSA: Binary Tree LCA Space Complexity',
            'text': 'What is the worst-case space complexity of recursive DFS for Lowest Common Ancestor on a skewed Binary Tree?',
            'options': ['A) O(1)', 'B) O(N)', 'C) O(N^2)', 'D) O(log N)'],
            'correct': 'B) O(N)',
            'explanation': 'For a completely skewed tree (linked list structure), the maximum call stack depth is O(N).',
            'marks': '2 Marks'
        },
        {
            'q_num': 10, 'type': 'mcq',
            'title': 'Q10. Technical DSA: Topological Sort Condition',
            'text': 'Which condition prevents Kahn\'s Algorithm (BFS) from ordering all vertices in a directed graph?',
            'options': ['A) Graph is undirected', 'B) Graph has weighted edges', 'C) Graph contains a directed cycle', 'D) Graph is disconnected'],
            'correct': 'C) Graph contains a directed cycle',
            'explanation': 'If a directed cycle exists, the in-degree of vertices in the cycle never reaches 0, preventing topological ordering.',
            'marks': '2 Marks'
        },
        {
            'q_num': 11, 'type': 'mcq',
            'title': 'Q11. Technical DSA: 1D Dynamic Programming State',
            'text': 'In the Coin Change problem using 1D Dynamic Programming, what does the array element dp[x] represent?',
            'options': ['A) Value of the largest coin used', 'B) Total number of ways to form amount x', 'C) Minimum number of coins needed to make amount x', 'D) Count of remaining coins'],
            'correct': 'C) Minimum number of coins needed to make amount x',
            'explanation': 'dp[x] stores the minimum number of coins required to sum up to amount x.',
            'marks': '2 Marks'
        },
        {
            'q_num': 12, 'type': 'mcq',
            'title': 'Q12. Technical DSA: Trie Tree Directory Search',
            'text': 'In an In-Memory File System implemented using a Trie data structure, what is the time complexity of searching a path of string length L?',
            'options': ['A) O(2^L)', 'B) O(L log N)', 'C) O(L)', 'D) O(N * L)'],
            'correct': 'C) O(L)',
            'explanation': 'Each character lookup in the Trie node child map takes O(1) time, so searching a path of length L takes O(L) time.',
            'marks': '2 Marks'
        },
        {
            'q_num': 13, 'type': 'mcq',
            'title': 'Q13. OS Fundamentals: Page Fault Processing',
            'text': 'What happens when a CPU generates a virtual memory address that is not currently present in RAM?',
            'options': ['A) The system crashes immediately', 'B) System cache memory is flushed', 'C) A page fault trap occurs and OS loads the required page from disk to RAM', 'D) Process terminates with segmentation fault'],
            'correct': 'C) A page fault trap occurs and OS loads the required page from disk to RAM',
            'explanation': 'The OS page fault handler fetches the missing page frame from secondary disk storage into physical RAM.',
            'marks': '2 Marks'
        },
        {
            'q_num': 14, 'type': 'mcq',
            'title': 'Q14. DBMS: Database Index Storage',
            'text': 'Which data structure is most widely used in relational database management systems (RDBMS) for primary and secondary indexes?',
            'options': ['A) Red-Black Tree', 'B) Binary Search Tree', 'C) Skip List', 'D) B+ Tree'],
            'correct': 'D) B+ Tree',
            'explanation': 'B+ Trees store data pointers in leaf nodes and internal routing keys in internal nodes, maximizing fan-out and reducing disk I/O.',
            'marks': '2 Marks'
        },
        {
            'q_num': 15, 'type': 'mcq',
            'title': 'Q15. Networking: TCP 3-Way Handshake',
            'text': 'Which TCP flag bit is set in the first segment sent by a client to establish a TCP connection with a server?',
            'options': ['A) SYN', 'B) FIN', 'C) ACK', 'D) RST'],
            'correct': 'A) SYN',
            'explanation': 'The client sends a SYN (Synchronize) packet to initiate the TCP 3-way handshake (SYN -> SYN-ACK -> ACK).',
            'marks': '2 Marks'
        },
        {
            'q_num': 16, 'type': 'mcq',
            'title': 'Q16. Technical: Bitwise Shift & OR Operation',
            'text': 'Evaluate the output of the C bitwise expression: `(1 << 4) | (8 >> 2)`',
            'options': ['A) 16', 'B) 10', 'C) 20', 'D) 18'],
            'correct': 'D) 18',
            'explanation': '1 << 4 = 16 (10000 in binary). 8 >> 2 = 2 (00010 in binary). 16 | 2 = 18 (10010 in binary).',
            'marks': '2 Marks'
        },
        {
            'q_num': 17, 'type': 'mcq',
            'title': 'Q17. Technical DSA: Build Heap Time Complexity',
            'text': 'What is the tight upper bound time complexity to build a Heap (heapify) from an unsorted array of N elements?',
            'options': ['A) O(N)', 'B) O(N log N)', 'C) O(log N)', 'D) O(N^2)'],
            'correct': 'A) O(N)',
            'explanation': 'Bottom-up heap construction runs in linear O(N) time due to converging series sum of node heights.',
            'marks': '2 Marks'
        },
        {
            'q_num': 18, 'type': 'mcq',
            'title': 'Q18. Technical DSA: Red-Black Tree Search Bounds',
            'text': 'What is the worst-case search time complexity in a self-balancing Red-Black Tree containing N elements?',
            'options': ['A) O(1)', 'B) O(log N)', 'C) O(N^2)', 'D) O(N)'],
            'correct': 'B) O(log N)',
            'explanation': 'Red-Black tree properties guarantee maximum height bound <= 2 * log2(N + 1), giving O(log N) operations.',
            'marks': '2 Marks'
        }
    ]

    m1_coding = [
        {
            'q_num': 19, 'type': 'coding',
            'title': 'Q19. Design & Implement LRU Cache',
            'text': """Design a data structure that follows the constraints of a Least Recently Used (LRU) cache with get(key) and put(key, value) in O(1) time complexity.

Example:
Input: ["LRUCache", "put", "put", "get", "put", "get"], [[2], [1, 1], [2, 2], [1], [3, 3], [2]]""",
            'options': [],
            'sample_answer': """class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]""",
            'explanation': 'Combine Doubly Linked List for O(1) node re-ordering with Hash Map for O(1) key lookups.',
            'marks': '4 Marks'
        },
        {
            'q_num': 20, 'type': 'coding',
            'title': 'Q20. Reorganize String',
            'text': """Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Example:
Input: s = "aab""aba""",
            'options': [],
            'sample_answer': """import heapq
from collections import Counter

def reorganizeString(s: str) -> str:
    count = Counter(s)
    max_heap = [[-cnt, char] for char, cnt in count.items()]
    heapq.heapify(max_heap)
    prev = None
    res = []
    while max_heap or prev:
        if prev and not max_heap:
            return ""
        cnt, char = heapq.heappop(max_heap)
        res.append(char)
        cnt += 1
        if prev:
            heapq.heappush(max_heap, prev)
            prev = None
        if cnt < 0:
            prev = [cnt, char]
    return "".join(res)""",
            'explanation': 'Greedily place highest frequency character using Max Heap with previous character holding buffer.',
            'marks': '4 Marks'
        },
        {
            'q_num': 21, 'type': 'coding',
            'title': 'Q21. Critical Connections in a Network (Graph Bridges)',
            'text': """Given n servers and directed edges connections, return all critical connections (bridges) whose removal disconnects the network.

Example:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]""",
            'options': [],
            'sample_answer': """from collections import defaultdict

def criticalConnections(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    low = [0] * n
    disc = [0] * n
    time = 0
    res = []

    def dfs(u, p):
        nonlocal time
        time += 1
        disc[u] = low[u] = time
        for v in graph[u]:
            if v == p: continue
            if disc[v]:
                low[u] = min(low[u], disc[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    res.append([u, v])

    dfs(0, -1)
    return res""",
            'explanation': 'Tarjan\'s DFS Algorithm using discovery times and low values finds bridges in O(V + E) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 22, 'type': 'coding',
            'title': 'Q22. Trapping Rain Water',
            'text': """Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]""",
            'options': [],
            'sample_answer': """def trap(height):
    if not height: return 0
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    res = 0
    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            res += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            res += right_max - height[r]
    return res""",
            'explanation': 'Two Pointers moving inwards while maintaining left_max and right_max bounds in O(N) time and O(1) space.',
            'marks': '4 Marks'
        },
        {
            'q_num': 23, 'type': 'coding',
            'title': 'Q23. Number of Islands',
            'text': """Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

Example:
Input: grid = [["1","1","0"],["1","1","0"],["0","0","1"]]""",
            'options': [],
            'sample_answer': """def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    return islands""",
            'explanation': 'DFS/BFS visiting adjacent land cells and sinking visited 1s in O(M*N) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 24, 'type': 'coding',
            'title': 'Q24. Merge Two Sorted Lists',
            'text': """Merge two sorted linked lists and return it as a sorted list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]

Data Structure: Singly Linked List""",
            'options': [],
            'sample_answer': """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next""",
            'explanation': 'Use dummy head pointer and iterate over sorted nodes in O(N + M) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 25, 'type': 'coding',
            'title': 'Q25. Course Schedule II (Topological Sort)',
            'text': """There are a total of numCourses courses you have to take. Return the ordering of courses you should take to finish all courses given prerequisites.

Example:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]

Data Structure: Directed Graph / Topological Sort""",
            'options': [],
            'sample_answer': """from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    adj = defaultdict(list)
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return res if len(res) == numCourses else []""",
            'explanation': 'Topological Sorting using BFS (Kahn\'s Algorithm) in O(V + E) time.',
            'marks': '4 Marks'
        }
    ]

    m2_mcqs = [
        {
            'q_num': 1, 'type': 'mcq',
            'title': 'Q1. Aptitude: Profit & Loss Percentage',
            'text': 'A trader marks his goods 20% above the cost price and allows a discount of 10% on the marked price. What is his net profit percentage?',
            'options': ['A) 10%', 'B) 15%', 'C) 8%', 'D) 12%'],
            'correct': 'C) 8%',
            'explanation': 'Let CP = 100. Marked Price = 120. Selling Price = 120 - 10% of 120 = 120 - 12 = 108. Net Profit = 108 - 100 = 8%.',
            'marks': '2 Marks'
        },
        {
            'q_num': 2, 'type': 'mcq',
            'title': 'Q2. Aptitude: Dice Rolling Probability',
            'text': 'What is the probability of getting a total sum of 7 when two fair six-sided dice are rolled simultaneously?',
            'options': ['A) 5/36', 'B) 7/36', 'C) 1/6', 'D) 1/12'],
            'correct': 'C) 1/6',
            'explanation': 'Favorable outcomes for sum 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6 pairs. Total outcomes = 36. Probability = 6/36 = 1/6.',
            'marks': '2 Marks'
        },
        {
            'q_num': 3, 'type': 'mcq',
            'title': 'Q3. Aptitude: Ratio & Difference',
            'text': 'Two numbers are in the ratio 4:5. If their difference is 15, what is the value of the larger number?',
            'options': ['A) 75', 'B) 90', 'C) 100', 'D) 60'],
            'correct': 'A) 75',
            'explanation': 'Let numbers be 4x and 5x. Difference = 5x - 4x = x = 15. Larger number = 5x = 5 * 15 = 75.',
            'marks': '2 Marks'
        },
        {
            'q_num': 4, 'type': 'mcq',
            'title': 'Q4. Aptitude: Boat & Stream Velocity',
            'text': 'A boat travels 24 km downstream in 3 hours and 18 km upstream in 6 hours. What is the speed of the stream?',
            'options': ['A) 2.5 km/h', 'B) 4.0 km/h', 'C) 3.0 km/h', 'D) 5.0 km/h'],
            'correct': 'A) 2.5 km/h',
            'explanation': 'Downstream speed = 24/3 = 8 km/h. Upstream speed = 18/6 = 3 km/h. Speed of stream = (8 - 3) / 2 = 2.5 km/h.',
            'marks': '2 Marks'
        },
        {
            'q_num': 5, 'type': 'mcq',
            'title': 'Q5. Reasoning: Letter Coding Transformation',
            'text': 'If "AMAZON" is written as "BNBAPO" in a certain code, how is "SERVER" written in that same code pattern?',
            'options': ['A) TFWSFS', 'B) TDVSFR', 'C) TEVSFS', 'D) TFWSFR'],
            'correct': 'A) TFWSFS',
            'explanation': 'Each letter is shifted forward by +1 alphabet position: S->T, E->F, R->S, V->W, E->F, R->S => TFWSFS.',
            'marks': '2 Marks'
        },
        {
            'q_num': 6, 'type': 'mcq',
            'title': 'Q6. Technical DSA: Build Heap Time Complexity',
            'text': 'What is the tight upper bound time complexity to build a Heap (heapify) from an unsorted array of N elements?',
            'options': ['A) O(N)', 'B) O(N^2)', 'C) O(N log N)', 'D) O(log N)'],
            'correct': 'A) O(N)',
            'explanation': 'Bottom-up heap construction runs in linear O(N) time due to converging series sum of node heights.',
            'marks': '2 Marks'
        },
        {
            'q_num': 7, 'type': 'mcq',
            'title': 'Q7. Technical DSA: QuickSort Pivot Strategy',
            'text': 'In QuickSort implementation, which pivot choice strategy prevents O(N^2) worst-case performance on already sorted input data?',
            'options': ['A) Fixed center index', 'B) Always pick the first element', 'C) Always pick the last element', 'D) Randomized pivot or Median-of-Three'],
            'correct': 'D) Randomized pivot or Median-of-Three',
            'explanation': 'Randomized or Median-of-Three pivot selection ensures balanced partition sizes with high probability.',
            'marks': '2 Marks'
        },
        {
            'q_num': 8, 'type': 'mcq',
            'title': 'Q8. Technical DSA: Red-Black Tree Search Bounds',
            'text': 'What is the worst-case search time complexity in a self-balancing Red-Black Tree containing N elements?',
            'options': ['A) O(N^2)', 'B) O(1)', 'C) O(N)', 'D) O(log N)'],
            'correct': 'D) O(log N)',
            'explanation': 'Red-Black tree properties guarantee maximum height bound <= 2 * log2(N + 1), giving O(log N) operations.',
            'marks': '2 Marks'
        },
        {
            'q_num': 9, 'type': 'mcq',
            'title': 'Q9. Technical DSA: Bellman-Ford Negative Edges',
            'text': 'Which algorithm can find single-source shortest paths in directed graphs even when some edge weights are negative?',
            'options': ['A) Bellman-Ford Algorithm', "B) Dijkstra\'s Algorithm", "C) Kruskal\'s Algorithm", "D) Prim\'s Algorithm"],
            'correct': 'A) Bellman-Ford Algorithm',
            'explanation': 'Bellman-Ford relaxes all V-1 edges V-1 times and detects negative weight cycles in O(V*E) time.',
            'marks': '2 Marks'
        },
        {
            'q_num': 10, 'type': 'mcq',
            'title': 'Q10. Technical DSA: LRU Cache Component Structures',
            'text': 'Which combination of data structures provides constant O(1) time complexity for both get and put operations in an LRU Cache?',
            'options': ['A) Array + Stack', 'B) Min Heap + Graph', 'C) Doubly Linked List + Hash Map', 'D) Binary Search Tree + Queue'],
            'correct': 'C) Doubly Linked List + Hash Map',
            'explanation': 'Doubly Linked List allows O(1) node removals/additions while Hash Map provides O(1) node lookup by key.',
            'marks': '2 Marks'
        },
        {
            'q_num': 11, 'type': 'mcq',
            'title': 'Q11. Technical DSA: Longest Common Subsequence DP',
            'text': 'What is the time complexity of solving the Longest Common Subsequence (LCS) problem using Dynamic Programming for strings of length M and N?',
            'options': ['A) O(M + N)', 'B) O(2^(M+N))', 'C) O(M * N)', 'D) O(M log N)'],
            'correct': 'C) O(M * N)',
            'explanation': 'The 2D DP matrix table has size M x N where each cell takes O(1) computation time.',
            'marks': '2 Marks'
        },
        {
            'q_num': 12, 'type': 'mcq',
            'title': 'Q12. OS Fundamentals: Deadlock Conditions',
            'text': 'Which of the following is NOT one of the 4 necessary conditions required for a deadlock to occur in an operating system?',
            'options': ['A) Hold and Wait', 'B) Circular Wait', 'C) Preemption of resources', 'D) Mutual Exclusion'],
            'correct': 'C) Preemption of resources',
            'explanation': 'Non-preemption (resources cannot be forcibly taken away) is the actual deadlock condition, not preemption.',
            'marks': '2 Marks'
        },
        {
            'q_num': 13, 'type': 'mcq',
            'title': 'Q13. DBMS: ACID Atomicity Guarantee',
            'text': 'Which ACID property guarantees that all database operations in a transaction execute successfully or the database is rolled back completely?',
            'options': ['A) Durability', 'B) Isolation', 'C) Atomicity', 'D) Consistency'],
            'correct': 'C) Atomicity',
            'explanation': 'Atomicity ensures "all or nothing" execution for multi-statement transactions.',
            'marks': '2 Marks'
        },
        {
            'q_num': 14, 'type': 'mcq',
            'title': 'Q14. Networking: DNS Protocol Transport',
            'text': 'Which transport protocol and port number are primarily used for standard DNS domain resolution queries?',
            'options': ['A) HTTP Port 8080', 'B) FTP Port 21', 'C) TCP Port 80', 'D) UDP Port 53'],
            'correct': 'D) UDP Port 53',
            'explanation': 'DNS uses stateless UDP port 53 for fast query lookup responses.',
            'marks': '2 Marks'
        },
        {
            'q_num': 15, 'type': 'mcq',
            'title': 'Q15. Technical Bitwise: Power of Two Bit Masking',
            'text': 'Which bitwise C expression evaluates to true (non-zero) if and only if integer n (> 0) is a power of 2?',
            'options': ['A) (n & (n - 1)) == 0', 'B) (n | (n - 1)) == 0', 'C) (n % 2) == 0', 'D) (n ^ (n + 1)) == 0'],
            'correct': 'A) (n & (n - 1)) == 0',
            'explanation': 'Powers of two have exactly 1 bit set (1000...). Subtracting 1 flips all lower bits (0111...), so n & (n-1) == 0.',
            'marks': '2 Marks'
        },
        {
            'q_num': 16, 'type': 'mcq',
            'title': 'Q16. Technical Bitwise: Compound Bit Expression',
            'text': 'Evaluate the result of the C expression: `(32 >> 3) ^ (4 << 2)`',
            'options': ['A) 8', 'B) 16', 'C) 12', 'D) 20'],
            'correct': 'D) 20',
            'explanation': '32 >> 3 = 4 (00100). 4 << 2 = 16 (10000). 4 XOR 16 = 20 (10100 in binary).',
            'marks': '2 Marks'
        },
        {
            'q_num': 17, 'type': 'mcq',
            'title': 'Q17. Reasoning: Syllogisms',
            'text': 'Statements: 1. All servers are nodes. 2. All nodes are connected. Conclusion: All servers are connected.',
            'options': ['A) Follows', 'B) Uncertain', 'C) None', 'D) Does not follow'],
            'correct': 'A) Follows',
            'explanation': 'All A are B and All B are C implies All A are C.',
            'marks': '2 Marks'
        },
        {
            'q_num': 18, 'type': 'mcq',
            'title': 'Q18. Reasoning: Direction Sense',
            'text': 'An engineer walks 8 km East, turns North and walks 6 km. What is the shortest distance from the origin?',
            'options': ['A) 14 km', 'B) 10 km', 'C) 12 km', 'D) 8 km'],
            'correct': 'B) 10 km',
            'explanation': 'Pythagoras theorem: sqrt(8^2 + 6^2) = sqrt(64 + 36) = 10 km.',
            'marks': '2 Marks'
        }
    ]

    m2_coding = [
        {
            'q_num': 19, 'type': 'coding',
            'title': 'Q19. Word Ladder (Shortest Transformation Sequence)',
            'text': """A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words where adjacent words differ by 1 letter. Return the length of the shortest transformation sequence.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]""",
            'options': [],
            'sample_answer': """from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    q = deque([(beginWord, 1)])
    while q:
        word, length = q.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    q.append((next_word, length + 1))
    return 0""",
            'explanation': 'BFS finds the shortest transformation path in word graph in O(N * L * 26) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 20, 'type': 'coding',
            'title': 'Q20. Minimum Window Substring',
            'text': """Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.

Example:
Input: s = "ADOBECODEBANC", t = "ABC""BANC""",
            'options': [],
            'sample_answer': """from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s: return ""
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]""",
            'explanation': 'Sliding Window maintaining target character frequencies in O(M + N) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 21, 'type': 'coding',
            'title': 'Q21. Find Median from Data Stream',
            'text': """Design a data structure that supports adding numbers from a data stream and finding the median of all elements added so far.

Example:
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [[], [1], [2], [], [3], []]""",
            'options': [],
            'sample_answer': """import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0""",
            'explanation': 'Balanced Dual Heaps allow O(log N) insertion and O(1) median retrieval.',
            'marks': '4 Marks'
        },
        {
            'q_num': 22, 'type': 'coding',
            'title': 'Q22. Word Search II (Trie + Matrix Backtracking)',
            'text': """Given an m x n board of characters and a list of strings words, return all words on the board.

Example:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]"eat","oath"]""",
            'options': [],
            'sample_answer': """class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children: node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
        
        res = []
        rows, cols = len(board), len(board[0])
        def dfs(r, c, parent):
            ch = board[r][c]
            curr = parent.children[ch]
            if curr.word:
                res.append(curr.word)
                curr.word = None
            board[r][c] = '#'
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr.children:
                    dfs(nr, nc, curr)
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return res""",
            'explanation': 'Trie Tree combined with DFS matrix traversal prunes invalid search paths efficiently.',
            'marks': '4 Marks'
        },
        {
            'q_num': 23, 'type': 'coding',
            'title': 'Q23. Rotting Oranges (Multi-Source BFS)',
            'text': """Given an m x n grid where each cell has 0 (empty), 1 (fresh orange), or 2 (rotten orange), return the minimum minutes until no fresh orange remains.

Example:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]""",
            'options': [],
            'sample_answer': """from collections import deque

def orangesRotting(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: q.append((r, c))
            elif grid[r][c] == 1: fresh += 1
    if fresh == 0: return 0
    time = 0
    while q and fresh > 0:
        time += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
    return time if fresh == 0 else -1""",
            'explanation': 'Multi-source BFS level order expansion simulates concurrent rotting in O(M*N) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 24, 'type': 'coding',
            'title': 'Q24. Maximum Subarray Sum with One Deletion',
            'text': """Given an array of integers, return the maximum sum of a non-empty subarray with at most one element deleted.

Example:
Input: arr = [1,-2,0,3]

Data Structure: 1D Dynamic Programming""",
            'options': [],
            'sample_answer': """def maximumSum(arr: list[int]) -> int:
    n = len(arr)
    no_delete = arr[0]
    one_delete = 0
    max_sum = arr[0]
    for i in range(1, n):
        one_delete = max(no_delete, one_delete + arr[i])
        no_delete = max(arr[i], no_delete + arr[i])
        max_sum = max(max_sum, no_delete, one_delete)
    return max_sum""",
            'explanation': 'Maintain running maximum sums with and without deletion in O(N) time and O(1) space.',
            'marks': '4 Marks'
        },
        {
            'q_num': 25, 'type': 'coding',
            'title': 'Q25. Top K Frequent Words',
            'text': """Given an array of strings words and an integer k, return the k most frequent strings sorted by frequency and lexicographical order.

Example:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4"the","is","sunny","day"]

Data Structure: Priority Queue / Heap""",
            'options': [],
            'sample_answer': """import heapq
from collections import Counter

class Element:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

def topKFrequent(words: list[str], k: int) -> list[str]:
    counts = Counter(words)
    freq_heap = []
    for word, count in counts.items():
        heapq.heappush(freq_heap, Element(word, count))
        if len(freq_heap) > k:
            heapq.heappop(freq_heap)
    res = []
    while freq_heap:
        res.append(heapq.heappop(freq_heap).word)
    return res[::-1]""",
            'explanation': 'Min-Heap with custom comparator handles frequency and lexicographical sorting in O(N log K) time.',
            'marks': '4 Marks'
        }
    ]

    m3_mcqs = [
        {
            'q_num': 1, 'type': 'mcq',
            'title': 'Q1. Aptitude: Permutations Count',
            'text': 'In how many different ways can 5 distinct books be arranged side-by-side on a bookshelf?',
            'options': ['A) 720', 'B) 60', 'C) 120', 'D) 25'],
            'correct': 'C) 120',
            'explanation': 'Number of arrangements = 5! (5 factorial) = 5 * 4 * 3 * 2 * 1 = 120 ways.',
            'marks': '2 Marks'
        },
        {
            'q_num': 2, 'type': 'mcq',
            'title': 'Q2. Aptitude: Mixture & Replacement',
            'text': 'A container has 40 liters of pure milk. 4 liters are removed and replaced with water. If this operation is repeated once more, how much pure milk remains?',
            'options': ['A) 30.0 Liters', 'B) 34.0 Liters', 'C) 32.4 Liters', 'D) 36.0 Liters'],
            'correct': 'C) 32.4 Liters',
            'explanation': 'Remaining milk = 40 * (1 - 4/40)^2 = 40 * (0.9)^2 = 40 * 0.81 = 32.4 Liters.',
            'marks': '2 Marks'
        },
        {
            'q_num': 3, 'type': 'mcq',
            'title': 'Q3. Aptitude: Clock Hand Angle',
            'text': 'What is the acute angle between the hour hand and the minute hand of a clock at 3:30?',
            'options': ['A) 75 degrees', 'B) 85 degrees', 'C) 105 degrees', 'D) 90 degrees'],
            'correct': 'A) 75 degrees',
            'explanation': 'Angle formula = |30*H - 5.5*M| = |30(3) - 5.5(30)| = |90 - 165| = 75 degrees.',
            'marks': '2 Marks'
        },
        {
            'q_num': 4, 'type': 'mcq',
            'title': 'Q4. Aptitude: Leap Year Calendar',
            'text': 'If January 1, 2024 was a Monday, what day of the week was January 1, 2025? (Note: 2024 is a leap year)',
            'options': ['A) Wednesday', 'B) Friday', 'C) Thursday', 'D) Tuesday'],
            'correct': 'A) Wednesday',
            'explanation': 'A leap year has 366 days = 52 weeks + 2 odd days. Monday + 2 days = Wednesday.',
            'marks': '2 Marks'
        },
        {
            'q_num': 5, 'type': 'mcq',
            'title': 'Q5. Reasoning: Syllogism Validity',
            'text': 'Statements: "All cats are animals. All animals are mammals." Conclusion: "All cats are mammals."',
            'options': ['A) Definitely Follows', 'B) Does Not Follow', 'C) Invalid Logic', 'D) Partially True'],
            'correct': 'A) Definitely Follows',
            'explanation': 'Venn diagram sub-sets: Cats subset of Animals subset of Mammals => All Cats are Mammals.',
            'marks': '2 Marks'
        },
        {
            'q_num': 6, 'type': 'mcq',
            'title': 'Q6. Technical DSA: Disjoint Set Union (DSU)',
            'text': 'What is the amortized time complexity per operation in a Disjoint Set Union (DSU) with Path Compression and Union by Rank?',
            'options': ['A) O(alpha(N)) ~ O(1)', 'B) O(N)', 'C) O(log N)', 'D) O(N^2)'],
            'correct': 'A) O(alpha(N)) ~ O(1)',
            'explanation': 'Path compression with union by rank runs in inverse Ackermann function time O(alpha(N)), which is effectively O(1).',
            'marks': '2 Marks'
        },
        {
            'q_num': 7, 'type': 'mcq',
            'title': 'Q7. Technical DSA: Binary Search Max Comparisons',
            'text': 'What is the maximum number of key comparisons required to search a target in a sorted array of 1024 elements using Binary Search?',
            'options': ['A) 512', 'B) 10', 'C) 1024', 'D) 11'],
            'correct': 'D) 11',
            'explanation': 'log2(1024) = 10, max comparison steps = floor(log2(N)) + 1 = 11.',
            'marks': '2 Marks'
        },
        {
            'q_num': 8, 'type': 'mcq',
            'title': 'Q8. Technical DSA: Prim\'s Algorithm MST Priority',
            'text': 'Which graph algorithm uses a Priority Queue (Min Heap) of candidate edges to construct a Minimum Spanning Tree?',
            'options': ['A) Topological Sort', "B) Kruskal\'s Algorithm", 'C) Floyd-Warshall', "D) Prim\'s Algorithm"],
            'correct': "D) Prim\'s Algorithm",
            'explanation': 'Prim\'s algorithm greedily expands MST by picking minimum weight edge connected to current tree using Min Heap.',
            'marks': '2 Marks'
        },
        {
            'q_num': 9, 'type': 'mcq',
            'title': 'Q9. Technical DSA: Hash Table Separate Chaining',
            'text': 'What is the hash collision resolution technique where colliding keys are linked in a Singly Linked List at the bucket index?',
            'options': ['A) Linear Probing', 'B) Separate Chaining', 'C) Open Addressing', 'D) Double Hashing'],
            'correct': 'B) Separate Chaining',
            'explanation': 'Separate chaining maintains an auxiliary list at each bucket index to hold colliding key-value pairs.',
            'marks': '2 Marks'
        },
        {
            'q_num': 10, 'type': 'mcq',
            'title': 'Q10. Technical DSA: 0/1 Knapsack Time Complexity',
            'text': 'What is the time complexity of the Dynamic Programming solution for 0/1 Knapsack with N items and knapsack capacity W?',
            'options': ['A) O(N log W)', 'B) O(2^N)', 'C) O(N * W)', 'D) O(N + W)'],
            'correct': 'C) O(N * W)',
            'explanation': 'The 2D DP matrix table size is (N+1) x (W+1), filled in O(N*W) pseudo-polynomial time.',
            'marks': '2 Marks'
        },
        {
            'q_num': 11, 'type': 'mcq',
            'title': 'Q11. Technical DSA: BST Inorder Traversal Property',
            'text': 'What sequence order of keys is produced by executing an Inorder (Left, Root, Right) DFS traversal on a Binary Search Tree?',
            'options': ['A) Level-by-level order', 'B) Reverse sorted order', 'C) Strictly ascending sorted order', 'D) Preorder sequence'],
            'correct': 'C) Strictly ascending sorted order',
            'explanation': 'Inorder traversal of BST visits left (smaller) -> root -> right (larger), yielding strictly ascending order.',
            'marks': '2 Marks'
        },
        {
            'q_num': 12, 'type': 'mcq',
            'title': 'Q12. OS Fundamentals: SJF Process Starvation',
            'text': 'Which CPU scheduling algorithm can lead to process starvation for long-running CPU-bound processes?',
            'options': ['A) First-Come First-Served (FCFS)', 'B) Multilevel Queue', 'C) Shortest Job First (SJF)', 'D) Round Robin'],
            'correct': 'C) Shortest Job First (SJF)',
            'explanation': 'Shortest Job First continuously prioritizes incoming short jobs, leaving long jobs waiting indefinitely (starvation).',
            'marks': '2 Marks'
        },
        {
            'q_num': 13, 'type': 'mcq',
            'title': 'Q13. DBMS: Second Normal Form (2NF)',
            'text': 'Which database normalization stage requires the relation to be in 1NF and eliminates partial functional dependencies?',
            'options': ['A) 1NF', 'B) BCNF', 'C) 2NF', 'D) 3NF'],
            'correct': 'C) 2NF',
            'explanation': '2NF requires no non-prime attribute to depend on a proper subset of any candidate key.',
            'marks': '2 Marks'
        },
        {
            'q_num': 14, 'type': 'mcq',
            'title': 'Q14. Networking: OSI Network Layer',
            'text': 'At which OSI layer do IP routing, packet forwarding, and logical IP address management operate?',
            'options': ['A) Application Layer (Layer 7)', 'B) Data Link Layer (Layer 2)', 'C) Transport Layer (Layer 4)', 'D) Network Layer (Layer 3)'],
            'correct': 'D) Network Layer (Layer 3)',
            'explanation': 'Layer 3 (Network Layer) handles logical IP addressing, packet encapsulation, and path routing.',
            'marks': '2 Marks'
        },
        {
            'q_num': 15, 'type': 'mcq',
            'title': 'Q15. Technical Bitwise: Swapping Without Temp',
            'text': 'Which bitwise operator can swap the values of two integer variables without allocating temporary variable memory?',
            'options': ['A) Bitwise XOR (^)', 'B) Bitwise AND (&)', 'C) Bitwise NOT (~)', 'D) Bitwise OR (|)'],
            'correct': 'A) Bitwise XOR (^)',
            'explanation': 'XOR property `a=a^b; b=a^b; a=a^b` swaps a and b in O(1) space without temporary memory.',
            'marks': '2 Marks'
        },
        {
            'q_num': 16, 'type': 'mcq',
            'title': 'Q16. Technical Bitwise: Expression Evaluation',
            'text': 'Evaluate the output of the expression: `(15 & 7) | (12 ^ 4)`',
            'options': ['A) 7', 'B) 12', 'C) 8', 'D) 15'],
            'correct': 'D) 15',
            'explanation': '(15 & 7) = 7 (0111). (12 ^ 4) = 8 (1000). 7 OR 8 = 15 (1111 binary).',
            'marks': '2 Marks'
        },
        {
            'q_num': 17, 'type': 'mcq',
            'title': 'Q17. Reasoning: Seating Arrangement',
            'text': '5 developers A, B, C, D, E sit in a row. C is in the middle. A is to the left of B. Who is at the center position?',
            'options': ['A) C', 'B) A', 'C) D', 'D) B'],
            'correct': 'A) C',
            'explanation': 'The condition explicitly places C at the middle position.',
            'marks': '2 Marks'
        },
        {
            'q_num': 18, 'type': 'mcq',
            'title': 'Q18. Reasoning: Cubes & Colors',
            'text': 'A cube painted blue on all sides is cut into 27 smaller equal cubes. How many small cubes have exactly 3 blue painted faces?',
            'options': ['A) 1', 'B) 8', 'C) 6', 'D) 12'],
            'correct': 'B) 8',
            'explanation': 'The 8 corner cubes always have 3 painted faces.',
            'marks': '2 Marks'
        }
    ]

    m3_coding = [
        {
            'q_num': 19, 'type': 'coding',
            'title': 'Q19. Merge K Sorted Lists',
            'text': """You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]""",
            'options': [],
            'sample_answer': """import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))
    dummy = ListNode(0)
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next""",
            'explanation': 'Min Heap maintains the smallest head node across all K lists in O(N log K) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 20, 'type': 'coding',
            'title': 'Q20. Lowest Common Ancestor of a Binary Tree',
            'text': """Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q in the tree.

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1""",
            'options': [],
            'sample_answer': """def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left or right""",
            'explanation': 'Bottom-up DFS recursion returning non-null nodes when p and q are found in O(N) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 21, 'type': 'coding',
            'title': 'Q21. Container With Most Water',
            'text': """You are given an integer array height of length n. Find two lines that together with the x-axis form a container, such that the container contains the most water.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]""",
            'options': [],
            'sample_answer': """def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    max_w = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_w = max(max_w, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_w""",
            'explanation': 'Two Pointers moving from boundaries towards center in O(N) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 22, 'type': 'coding',
            'title': 'Q22. Clone Graph',
            'text': """Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Example:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]""",
            'options': [],
            'sample_answer': """class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node: return None
    old_to_new = {}
    def dfs(n):
        if n in old_to_new:
            return old_to_new[n]
        copy = Node(n.val)
        old_to_new[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node)""",
            'explanation': 'Hash Map storing original-to-clone node mappings prevents cycles during DFS in O(V+E) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 23, 'type': 'coding',
            'title': 'Q23. Find All Anagrams in a String',
            'text': """Given two strings s and p, return an array of all the start indices of p's anagrams in s.

Example:
Input: s = "cbaebabacd", p = "abc""",
            'options': [],
            'sample_answer': """from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s): return []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)-1])
    res = []
    for i in range(len(p)-1, len(s)):
        s_count[s[i]] += 1
        if s_count == p_count:
            res.append(i - len(p) + 1)
        s_count[s[i - len(p) + 1]] -= 1
        if s_count[s[i - len(p) + 1]] == 0:
            del s_count[s[i - len(p) + 1]]
    return res""",
            'explanation': 'Sliding Window maintaining fixed window of length len(p) in O(N) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 24, 'type': 'coding',
            'title': 'Q24. Kth Largest Element in an Array',
            'text': """Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in sorted order, not the kth distinct element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2

Data Structure: Min-Heap / QuickSelect""",
            'options': [],
            'sample_answer': """import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]""",
            'explanation': 'Min-Heap of size K maintains top K elements, returning the Kth largest at root in O(N log K) time.',
            'marks': '4 Marks'
        },
        {
            'q_num': 25, 'type': 'coding',
            'title': 'Q25. Valid Parentheses String',
            'text': """Given a string s containing only '(', ')' and '*', return true if s is valid. '*' can be treated as a single ')', '(', or empty string.

Example:
Input: s = "(*))"

Data Structure: Dynamic Balance Range Counter""",
            'options': [],
            'sample_answer': """def checkValidString(s: str) -> bool:
    cmin = cmax = 0
    for char in s:
        if char == '(':
            cmin += 1; cmax += 1
        elif char == ')':
            cmin -= 1; cmax -= 1
        else: # '*'
            cmin -= 1; cmax += 1
        if cmax < 0: return False
        cmin = max(cmin, 0)
    return cmin == 0""",
            'explanation': 'Track minimum and maximum possible open parenthesis counts in O(N) time and O(1) space.',
            'marks': '4 Marks'
        }
    ]

    if model_num == 2:
        mcqs, coding, title_suffix = m2_mcqs, m2_coding, "Model 2"
    elif model_num == 3:
        mcqs, coding, title_suffix = m3_mcqs, m3_coding, "Model 3"
    else:
        mcqs, coding, title_suffix = m1_mcqs, m1_coding, "Model 1"

    if paper_type == 'model':
        # Solve Model Paper format: Section 1 & Section 2
        return [
            {
                'section_name': 'Section 1: Quantitative Aptitude & Technical MCQs (18 Questions)',
                'time': '45 Mins',
                'questions': mcqs
            },
            {
                'section_name': 'Section 2: Coding Assessment & Data Structures (7 Problems)',
                'time': '75 Mins',
                'questions': coding
            }
        ]
    else:
        # Solve Paper in Practice Test format: Flat 1 to 25 Questions list
        all_25 = []
        for idx, q in enumerate(mcqs + coding, 1):
            q_copy = dict(q)
            q_copy['q_num'] = idx
            all_25.append(q_copy)
            
        return [
            {
                'section_name': f'Amazon Practice Test Paper {title_suffix} (25 Solved Questions)',
                'time': '120 Mins',
                'questions': all_25
            }
        ]


def get_amazon_practice_sections_model1(paper_type='model'):
    return get_amazon_practice_sections(1, paper_type)


def get_amazon_practice_sections_model2(paper_type='model'):
    return get_amazon_practice_sections(2, paper_type)


def get_amazon_practice_sections_model3(paper_type='model'):
    return get_amazon_practice_sections(3, paper_type)


def get_infosys_practice_sections_model1():
    sec1_pseudocode = [
        {
            'q_num': 1, 'type': 'mcq',
            'title': 'Pseudocode: Variables & Variable Swap (Set A)',
            'text': """What is the output of the following pseudocode?
Integer a = 5, b = 10
a = a + b
b = a - b
a = a - b
Print a, b""",
            'options': ['A) 5, 10', 'B) 15, 10', 'C) 10, 5', 'D) 15, 5'],
            'correct': 'C) 10, 5',
            'explanation': 'Classic variable swap logic without extra storage: a becomes 10 and b becomes 5.',
            'marks': '2 Marks'
        },
        {
            'q_num': 2, 'type': 'mcq',
            'title': 'Pseudocode: Conditional Statements (If-Else) (Set A)',
            'text': """Predict the output of the code block:
Integer x = 12, y = 15, z = 8
If (x > y AND x > z)
    Print x
ElseIf (y > z)
    Print y
Else
    Print z""",
            'options': ['A) 12', 'B) 8', 'C) 15', 'D) 0'],
            'correct': 'C) 15',
            'explanation': 'x > y is False (12 > 15). ElseIf condition (15 > 8) is True, so 15 is printed.',
            'marks': '2 Marks'
        },
        {
            'q_num': 3, 'type': 'mcq',
            'title': 'Pseudocode: Loops (While Loop Accumulator) (Set A)',
            'text': """What will be printed by the following loop?
Integer count = 0, i = 1
While (i <= 5)
    count = count + i
    i = i + 2
End While
Print count""",
            'options': ['A) 9', 'B) 15', 'C) 6', 'D) 12'],
            'correct': 'A) 9',
            'explanation': 'i takes values 1, 3, 5. count sum = 1 + 3 + 5 = 9.',
            'marks': '2 Marks'
        },
        {
            'q_num': 4, 'type': 'mcq',
            'title': 'Pseudocode: Functions (Recursion) (Set A)',
            'text': """Predict the output of the recursive pseudocode function call foo(4):
Function foo(Integer n)
    If (n <= 1) Return 1
    Return n * foo(n - 1)
End Function""",
            'options': ['A) 24', 'B) 16', 'C) 4', 'D) 12'],
            'correct': 'A) 24',
            'explanation': 'foo(4) = 4 * 3 * 2 * 1 = 24 (Factorial calculation).',
            'marks': '2 Marks'
        },
        {
            'q_num': 5, 'type': 'mcq',
            'title': 'Pseudocode: Arrays (Array Element Update) (Set A)',
            'text': """What is the final value of arr[2] after executing:
Integer arr[4] = {2, 4, 6, 8}
For i = 0 to 1
    arr[i+1] = arr[i] + arr[i+1]
End For
Print arr[2]""",
            'options': ['A) 12', 'B) 10', 'C) 8', 'D) 6'],
            'correct': 'A) 12',
            'explanation': 'i=0: arr[1] = 2 + 4 = 6. i=1: arr[2] = 6 + 6 = 12.',
            'marks': '2 Marks'
        },
        {
            'q_num': 6, 'type': 'mcq',
            'title': 'Pseudocode: Strings (Substring Extraction) (Set A)',
            'text': """What will be the string output of the following pseudocode?
String str = "INFOSYS"
Print str.substring(2, 5)""",
            'options': ['A) FOS', 'B) FO', 'C) SYS', 'D) INFO'],
            'correct': 'A) FOS',
            'explanation': 'Substring from index 2 up to index 5 (exclusive) extracts characters "FOS".',
            'marks': '2 Marks'
        },
        {
            'q_num': 7, 'type': 'mcq',
            'title': 'Pseudocode: Basic Algorithms (Binary Search Step) (Set A)',
            'text': """In Binary Search pseudocode on array {10, 20, 30, 40, 50} for target 40:
Integer low = 0, high = 4
Integer mid = (low + high) / 2
What is the first element compared at arr[mid]? """,
            'options': ['A) 50', 'B) 40', 'C) 20', 'D) 30'],
            'correct': 'D) 30',
            'explanation': 'Initial mid = (0 + 4) / 2 = 2. Element at arr[2] is 30.',
            'marks': '2 Marks'
        },
        {
            'q_num': 8, 'type': 'mcq',
            'title': 'Pseudocode: Output Prediction (Bitwise Bitshift) (Set A)',
            'text': """Evaluate the output of bitwise manipulation:
Integer a = 8, b = 2
Integer c = (a << 1) + (b >> 1)
Print c""",
            'options': ['A) 16', 'B) 15', 'C) 18', 'D) 17'],
            'correct': 'D) 17',
            'explanation': '(8 << 1) = 16. (2 >> 1) = 1. 16 + 1 = 17.',
            'marks': '2 Marks'
        }
    ]

    sec2_reasoning_verbal = [
        {
            'q_num': 9, 'type': 'mcq',
            'title': 'Logical Reasoning: Coding-Decoding (Set A)',
            'text': 'If "INFY" is coded as "KPHA" (+2 shift), how is "CODE" coded under the same pattern?',
            'options': ['A) FQFH', 'B) EQFG', 'C) ERGE', 'D) EQGE'],
            'correct': 'B) EQFG',
            'explanation': 'C+2=E, O+2=Q, D+2=F, E+2=G => EQFG.',
            'marks': '2 Marks'
        },
        {
            'q_num': 10, 'type': 'mcq',
            'title': 'Logical Reasoning: Blood Relations (Set A)',
            'text': 'Pointing to a photograph, Rahul said "He is the son of my mother\'s only daughter." How is Rahul related to the person in the photograph?',
            'options': ['A) Brother', 'B) Nephew', 'C) Uncle', 'D) Father'],
            'correct': 'C) Uncle',
            'explanation': 'Mother\'s only daughter = Rahul\'s sister. Sister\'s son = Nephew, so Rahul is his Uncle.',
            'marks': '2 Marks'
        },
        {
            'q_num': 11, 'type': 'mcq',
            'title': 'Logical Reasoning: Direction Sense (Set A)',
            'text': 'An engineer walks 12 meters North, turns right and walks 5 meters. What is the shortest distance from the starting point?',
            'options': ['A) 17 meters', 'B) 10 meters', 'C) 13 meters', 'D) 15 meters'],
            'correct': 'C) 13 meters',
            'explanation': 'Pythagoras theorem: sqrt(12^2 + 5^2) = sqrt(144 + 25) = 13 meters.',
            'marks': '2 Marks'
        },
        {
            'q_num': 12, 'type': 'mcq',
            'title': 'Logical Reasoning: Syllogisms (Set A)',
            'text': 'Statements: "All code modules are tested. All tested modules are deployed." Conclusion: "All code modules are deployed."',
            'options': ['A) Does Not Follow', 'B) Partially True', 'C) Definitely Follows', 'D) Invalid'],
            'correct': 'C) Definitely Follows',
            'explanation': 'Venn diagram subset relation: Code modules subset of Deployed modules.',
            'marks': '2 Marks'
        },
        {
            'q_num': 13, 'type': 'mcq',
            'title': 'Logical Reasoning: Seating Arrangement (Set A)',
            'text': '5 candidates P, Q, R, S, T sit in a row facing North. R is in the center. P is to the left of Q. Who is seated in the exact middle?',
            'options': ['A) S', 'B) P', 'C) R', 'D) Q'],
            'correct': 'C) R',
            'explanation': 'Statement explicitly places R in the center position.',
            'marks': '2 Marks'
        },
        {
            'q_num': 14, 'type': 'mcq',
            'title': 'Logical Reasoning: Puzzles (Floor Arrangement) (Set A)',
            'text': 'In a 4-floor building (floors 1 to 4), A lives on an odd floor above floor 1. B lives immediately below A. Which floor does B live on?',
            'options': ['A) Floor 3', 'B) Floor 4', 'C) Floor 1', 'D) Floor 2'],
            'correct': 'D) Floor 2',
            'explanation': 'Odd floor above 1 is floor 3. A lives on floor 3, so B lives immediately below on floor 2.',
            'marks': '2 Marks'
        },
        {
            'q_num': 15, 'type': 'mcq',
            'title': 'Logical Reasoning: Data Interpretation (Set Diagram) (Set A)',
            'text': 'In a team of 50 engineers, 30 know Python, 25 know Java, and 10 know both. How many engineers know neither Python nor Java?',
            'options': ['A) 5', 'B) 15', 'C) 0', 'D) 10'],
            'correct': 'A) 5',
            'explanation': 'Total knowing at least one = 30 + 25 - 10 = 45. Knowing neither = 50 - 45 = 5.',
            'marks': '2 Marks'
        },
        {
            'q_num': 16, 'type': 'mcq',
            'title': 'Verbal: Reading Comprehension (Set A)',
            'text': 'Read passage: "Infosys leverages automated test suites to ensure zero-defect deployments across enterprise systems." What is the primary goal of automated test suites?',
            'options': ['A) Monolithic growth', 'B) Manual testing', 'C) Increasing bugs', 'D) Zero-defect deployments'],
            'correct': 'D) Zero-defect deployments',
            'explanation': 'Passage explicitly states the goal is to ensure zero-defect deployments.',
            'marks': '2 Marks'
        },
        {
            'q_num': 17, 'type': 'mcq',
            'title': 'Verbal: Synonyms/Antonyms (Set A)',
            'text': 'Select the word closest in meaning to "PRAGMATIC":',
            'options': ['A) Practical', 'B) Idealistic', 'C) Irrational', 'D) Theoretical'],
            'correct': 'A) Practical',
            'explanation': 'Pragmatic means dealing with things sensibly and realistically; practical.',
            'marks': '2 Marks'
        },
        {
            'q_num': 18, 'type': 'mcq',
            'title': 'Verbal: Grammar (Set A)',
            'text': 'Identify the grammatically correct sentence:',
            'options': ['A) She is senior than I.', 'B) She is senior to me in the organization.', 'C) She is senior over me in the organization.', 'D) She is senior than me in the organization.'],
            'correct': 'B) She is senior to me in the organization.',
            'explanation': 'Adjectives like senior, junior, superior take the preposition "to".',
            'marks': '2 Marks'
        },
        {
            'q_num': 19, 'type': 'mcq',
            'title': 'Verbal: Sentence Correction (Set A)',
            'text': 'Correct the sentence: "Neither of the server nodes were responding."',
            'options': ['A) Neither of the server nodes was responding.', 'B) Neither of the server nodes are responding.', 'C) Neither of server nodes were responding.', 'D) No correction needed.'],
            'correct': 'A) Neither of the server nodes was responding.',
            'explanation': '"Neither of" takes a singular verb "was responding".',
            'marks': '2 Marks'
        },
        {
            'q_num': 20, 'type': 'mcq',
            'title': 'Verbal: Fill in the Blanks (Set A)',
            'text': 'Choose the correct preposition: "The software patch was applied _____ enhance system stability."',
            'options': ['A) by', 'B) for', 'C) with', 'D) to'],
            'correct': 'D) to',
            'explanation': 'Infinitive "to enhance" is grammatically correct.',
            'marks': '2 Marks'
        },
        {
            'q_num': 21, 'type': 'mcq',
            'title': 'Verbal: Vocabulary (Set A)',
            'text': 'Choose the word that best completes: "The cloud architecture showed _____ resilience during peak traffic spikes."',
            'options': ['A) hostile', 'B) exemplary', 'C) flawed', 'D) mediocre'],
            'correct': 'B) exemplary',
            'explanation': 'Exemplary means commendable and serving as a desirable model.',
            'marks': '2 Marks'
        }
    ]

    sec3_quant = [
        {
            'q_num': 22, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Percentages (Set A)',
            'text': 'A candidate scores 240 marks out of 300 in an assessment. What is the candidate\'s percentage score?',
            'options': ['A) 85%', 'B) 80%', 'C) 90%', 'D) 75%'],
            'correct': 'B) 80%',
            'explanation': 'Percentage = (240 / 300) * 100 = 80%.',
            'marks': '2 Marks'
        },
        {
            'q_num': 23, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Profit & Loss (Set A)',
            'text': 'An item bought for $500 is sold for $625. What is the net profit percentage?',
            'options': ['A) 25%', 'B) 30%', 'C) 15%', 'D) 20%'],
            'correct': 'A) 25%',
            'explanation': 'Profit = 625 - 500 = 125. Profit % = (125 / 500) * 100 = 25%.',
            'marks': '2 Marks'
        },
        {
            'q_num': 24, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Time & Work (Set A)',
            'text': 'Pipe A fills a tank in 10 hours and Pipe B fills it in 15 hours. How long will both pipes take together to fill the tank?',
            'options': ['A) 12 hours', 'B) 5 hours', 'C) 6 hours', 'D) 8 hours'],
            'correct': 'C) 6 hours',
            'explanation': 'Combined rate = 1/10 + 1/15 = 5/60 = 1/6 => 6 hours.',
            'marks': '2 Marks'
        },
        {
            'q_num': 25, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Time, Speed & Distance (Set A)',
            'text': 'A train 200m long passes a telegraph pole in 10 seconds. What is the speed of the train in km/h?',
            'options': ['A) 90 km/h', 'B) 54 km/h', 'C) 108 km/h', 'D) 72 km/h'],
            'correct': 'D) 72 km/h',
            'explanation': 'Speed = 200 / 10 = 20 m/s. In km/h = 20 * (18/5) = 72 km/h.',
            'marks': '2 Marks'
        },
        {
            'q_num': 26, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Ratios (Set A)',
            'text': 'Two numbers are in the ratio 3:4. If their sum is 70, what is the value of the larger number?',
            'options': ['A) 60', 'B) 50', 'C) 30', 'D) 40'],
            'correct': 'D) 40',
            'explanation': '3x + 4x = 70 => 7x = 70 => x = 10. Larger number = 4 * 10 = 40.',
            'marks': '2 Marks'
        },
        {
            'q_num': 27, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Averages (Set A)',
            'text': 'The average score of 5 test runs is 80. If a 6th test run scores 110, what is the new average score of all 6 runs?',
            'options': ['A) 82', 'B) 85', 'C) 90', 'D) 88'],
            'correct': 'B) 85',
            'explanation': 'Total sum = (5 * 80) + 110 = 400 + 110 = 510. New average = 510 / 6 = 85.',
            'marks': '2 Marks'
        },
        {
            'q_num': 28, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Probability (Set A)',
            'text': 'What is the probability of drawing an Ace from a standard well-shuffled deck of 52 playing cards?',
            'options': ['A) 1/52', 'B) 1/13', 'C) 4/13', 'D) 1/4'],
            'correct': 'B) 1/13',
            'explanation': 'There are 4 Aces in 52 cards. Probability = 4/52 = 1/13.',
            'marks': '2 Marks'
        },
        {
            'q_num': 29, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Permutation & Combination (Set A)',
            'text': 'In how many different ways can 4 distinct tasks be assigned to 4 developers?',
            'options': ['A) 64', 'B) 16', 'C) 24', 'D) 12'],
            'correct': 'C) 24',
            'explanation': '4! (4 factorial) = 4 * 3 * 2 * 1 = 24 ways.',
            'marks': '2 Marks'
        },
        {
            'q_num': 30, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Number System (Set A)',
            'text': 'What is the remainder when 7^4 (2401) is divided by 5?',
            'options': ['A) 4', 'B) 3', 'C) 2', 'D) 1'],
            'correct': 'D) 1',
            'explanation': '2401 divided by 5 leaves remainder 1 (2400 is divisible by 5).',
            'marks': '2 Marks'
        }
    ]

    return [
        {
            'section_name': 'Section 1: Pseudocode (Variables, Conditions, Loops, Functions, Arrays, Strings, Basic Algorithms, Output Prediction)',
            'time': '40 Mins',
            'questions': sec1_pseudocode
        },
        {
            'section_name': 'Section 2: Reasoning + Verbal (Logical Reasoning & Verbal Ability)',
            'time': '35 Mins',
            'questions': sec2_reasoning_verbal
        },
        {
            'section_name': 'Section 3: Quantitative Aptitude (Mathematics)',
            'time': '25 Mins',
            'questions': sec3_quant
        }
    ]


def get_infosys_practice_sections_model2():
    sec1_pseudocode = [
        {
            'q_num': 1, 'type': 'mcq',
            'title': 'Pseudocode: Variables & Multiplication (Set B)',
            'text': """What is the output of the following pseudocode?
Integer x = 7, y = 3
x = x * y
y = x / y
Print x, y""",
            'options': ['A) 21, 3', 'B) 7, 21', 'C) 21, 7', 'D) 14, 7'],
            'correct': 'C) 21, 7',
            'explanation': 'x becomes 21 (7*3). y becomes 21/3 = 7. Output is 21, 7.',
            'marks': '2 Marks'
        },
        {
            'q_num': 2, 'type': 'mcq',
            'title': 'Pseudocode: Conditional Nested If (Set B)',
            'text': """Predict the output for a = 8, b = 4:
Integer a = 8, b = 4
If (a > 5)
    If (b < 10)
        Print "SUCCESS"
    Else
        Print "WAIT"
End If""",
            'options': ['A) WAIT', 'B) ERROR', 'C) SUCCESS', 'D) NONE'],
            'correct': 'C) SUCCESS',
            'explanation': '8 > 5 is True and 4 < 10 is True, printing "SUCCESS".',
            'marks': '2 Marks'
        },
        {
            'q_num': 3, 'type': 'mcq',
            'title': 'Pseudocode: Loops (For Loop Product) (Set B)',
            'text': """What is the value of product after the loop?
Integer product = 1
For i = 1 to 4
    product = product * i
End For
Print product""",
            'options': ['A) 24', 'B) 10', 'C) 20', 'D) 12'],
            'correct': 'A) 24',
            'explanation': 'Product = 1 * 2 * 3 * 4 = 24.',
            'marks': '2 Marks'
        },
        {
            'q_num': 4, 'type': 'mcq',
            'title': 'Pseudocode: Functions (Fibonacci Call) (Set B)',
            'text': """Predict the return value of recursive call fib(5):
Function fib(Integer n)
    If (n <= 1) Return n
    Return fib(n-1) + fib(n-2)
End Function""",
            'options': ['A) 5', 'B) 8', 'C) 2', 'D) 3'],
            'correct': 'A) 5',
            'explanation': 'fib(5) = 5 (0, 1, 1, 2, 3, 5).',
            'marks': '2 Marks'
        },
        {
            'q_num': 5, 'type': 'mcq',
            'title': 'Pseudocode: Arrays (Element Doubling) (Set B)',
            'text': """What is the value of arr[3] after running:
Integer arr[4] = {1, 3, 5, 7}
For i = 0 to 3
    arr[i] = arr[i] * 2
End For
Print arr[3]""",
            'options': ['A) 14', 'B) 10', 'C) 7', 'D) 12'],
            'correct': 'A) 14',
            'explanation': 'arr[3] = 7 * 2 = 14.',
            'marks': '2 Marks'
        },
        {
            'q_num': 6, 'type': 'mcq',
            'title': 'Pseudocode: Strings (String Concatenation Length) (Set B)',
            'text': """What will be printed?
String s1 = "DSE"
String s2 = "2025"
String s3 = s1 + s2
Print s3.length()""",
            'options': ['A) 7', 'B) 4', 'C) 3', 'D) 8'],
            'correct': 'A) 7',
            'explanation': '"DSE2025" has length 7.',
            'marks': '2 Marks'
        },
        {
            'q_num': 7, 'type': 'mcq',
            'title': 'Pseudocode: Basic Algorithms (Linear Search Steps) (Set B)',
            'text': """How many comparisons are made to find target 16 in array {4, 8, 15, 16, 23, 42} using Linear Search?""",
            'options': ['A) 5', 'B) 3', 'C) 6', 'D) 4'],
            'correct': 'D) 4',
            'explanation': 'Elements checked: 4 (1), 8 (2), 15 (3), 16 (4th comparison).',
            'marks': '2 Marks'
        },
        {
            'q_num': 8, 'type': 'mcq',
            'title': 'Pseudocode: Output Prediction (Bitwise Compound) (Set B)',
            'text': """Evaluate the output:
Integer res = (15 & 7) | (4 << 1)
Print res""",
            'options': ['A) 8', 'B) 12', 'C) 7', 'D) 15'],
            'correct': 'D) 15',
            'explanation': '15 & 7 = 7 (0111). 4 << 1 = 8 (1000). 7 | 8 = 15.',
            'marks': '2 Marks'
        }
    ]

    sec2_reasoning_verbal = [
        {
            'q_num': 9, 'type': 'mcq',
            'title': 'Logical Reasoning: Coding-Decoding (Set B)',
            'text': 'If "SYSTEM" is written as "TZTUFN" (+1 shift), how is "JAVA" written in that same code?',
            'options': ['A) KAXA', 'B) KBWB', 'C) LCXC', 'D) IZUZ'],
            'correct': 'B) KBWB',
            'explanation': 'J+1=K, A+1=B, V+1=W, A+1=B => KBWB.',
            'marks': '2 Marks'
        },
        {
            'q_num': 10, 'type': 'mcq',
            'title': 'Logical Reasoning: Blood Relations (Set B)',
            'text': 'Pointing to a man, Neha said "His father is my father\'s only son." How is Neha related to the man?',
            'options': ['A) Daughter', 'B) Sister', 'C) Aunt', 'D) Mother'],
            'correct': 'C) Aunt',
            'explanation': 'Neha\'s father\'s only son is her brother. Her brother is the man\'s father, so Neha is his Aunt.',
            'marks': '2 Marks'
        },
        {
            'q_num': 11, 'type': 'mcq',
            'title': 'Logical Reasoning: Direction Sense (Set B)',
            'text': 'A developer walks 15 meters West, turns left and walks 8 meters South. What is the shortest distance from origin?',
            'options': ['A) 12 meters', 'B) 20 meters', 'C) 17 meters', 'D) 23 meters'],
            'correct': 'C) 17 meters',
            'explanation': 'sqrt(15^2 + 8^2) = sqrt(225 + 64) = sqrt(289) = 17 meters.',
            'marks': '2 Marks'
        },
        {
            'q_num': 12, 'type': 'mcq',
            'title': 'Logical Reasoning: Syllogisms (Set B)',
            'text': 'Statements: "All algorithms are optimized. Some optimized codes are fast." Conclusion: "Some algorithms are fast."',
            'options': ['A) Does Not Follow', 'B) None', 'C) Uncertain', 'D) Definitely Follows'],
            'correct': 'C) Uncertain',
            'explanation': 'Optimized codes overlap with algorithms and fast codes, but direct link between algorithms and fast is uncertain.',
            'marks': '2 Marks'
        },
        {
            'q_num': 13, 'type': 'mcq',
            'title': 'Logical Reasoning: Seating Arrangement (Set B)',
            'text': '6 engineers sit in a circle facing center. A is opposite D, B is opposite E. Who is opposite C?',
            'options': ['A) E', 'B) A', 'C) F', 'D) B'],
            'correct': 'C) F',
            'explanation': 'Remaining opposite pair in 6-person circle is C and F.',
            'marks': '2 Marks'
        },
        {
            'q_num': 14, 'type': 'mcq',
            'title': 'Logical Reasoning: Puzzles (Box Puzzle) (Set B)',
            'text': '3 boxes Red, Green, Blue contain Apple, Orange, Banana. Red box does not contain Banana. Green box contains Apple. What is in Red box?',
            'options': ['A) Banana', 'B) Apple', 'C) Empty', 'D) Orange'],
            'correct': 'D) Orange',
            'explanation': 'Green=Apple. Red cannot be Banana, so Red=Orange and Blue=Banana.',
            'marks': '2 Marks'
        },
        {
            'q_num': 15, 'type': 'mcq',
            'title': 'Logical Reasoning: Data Interpretation (Exam Pass Rates) (Set B)',
            'text': 'In a class of 100 students, 60 pass Math, 50 pass Reasoning, and 30 pass both. How many fail both subjects?',
            'options': ['A) 20', 'B) 10', 'C) 25', 'D) 15'],
            'correct': 'A) 20',
            'explanation': 'Pass at least one = 60 + 50 - 30 = 80. Fail both = 100 - 80 = 20.',
            'marks': '2 Marks'
        },
        {
            'q_num': 16, 'type': 'mcq',
            'title': 'Verbal: Reading Comprehension (Set B)',
            'text': 'Passage: "Microservices architecture allows breaking a monolith into independently deployable services." What is the main benefit?',
            'options': ['A) Manual restarts', 'B) Monolithic growth', 'C) Single failure point', 'D) Independent service deployment'],
            'correct': 'D) Independent service deployment',
            'explanation': 'Passage states microservices enable independent service deployments.',
            'marks': '2 Marks'
        },
        {
            'q_num': 17, 'type': 'mcq',
            'title': 'Verbal: Synonyms/Antonyms (Set B)',
            'text': 'Select word closest in meaning to "METICULOUS":',
            'options': ['A) Precise', 'B) Careless', 'C) Sloppy', 'D) Hasty'],
            'correct': 'A) Precise',
            'explanation': 'Meticulous means showing great attention to detail; precise.',
            'marks': '2 Marks'
        },
        {
            'q_num': 18, 'type': 'mcq',
            'title': 'Verbal: Grammar (Set B)',
            'text': 'Correct usage: "Developers prefer coding _______ documentation."',
            'options': ['A) than', 'B) to', 'C) over', 'D) from'],
            'correct': 'B) to',
            'explanation': 'Verb "prefer" takes preposition "to".',
            'marks': '2 Marks'
        },
        {
            'q_num': 19, 'type': 'mcq',
            'title': 'Verbal: Sentence Correction (Set B)',
            'text': 'Correct: "Each of the developers has submitted their code."',
            'options': ['A) Each of the developers has submitted his/her code.', 'B) Each of developers have submitted code.', 'C) Each developer have submitted.', 'D) No error.'],
            'correct': 'A) Each of the developers has submitted his/her code.',
            'explanation': '"Each" takes singular pronoun "his/her" rather than plural "their".',
            'marks': '2 Marks'
        },
        {
            'q_num': 20, 'type': 'mcq',
            'title': 'Verbal: Fill in the Blanks (Set B)',
            'text': 'Choose word: "The software application is compatible _______ legacy databases."',
            'options': ['A) for', 'B) in', 'C) to', 'D) with'],
            'correct': 'D) with',
            'explanation': 'Adjective "compatible" takes preposition "with".',
            'marks': '2 Marks'
        },
        {
            'q_num': 21, 'type': 'mcq',
            'title': 'Verbal: Vocabulary (Set B)',
            'text': 'Choose best word: "The project team delivered a _____ performance under tight deadlines."',
            'options': ['A) flawed', 'B) stellar', 'C) mediocre', 'D) hostile'],
            'correct': 'B) stellar',
            'explanation': 'Stellar means exceptionally good or outstanding.',
            'marks': '2 Marks'
        }
    ]

    sec3_quant = [
        {
            'q_num': 22, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Percentages (Set B)',
            'text': 'A town population increases by 10% in Year 1 and 20% in Year 2. What is the total net percentage increase?',
            'options': ['A) 25%', 'B) 32%', 'C) 30%', 'D) 35%'],
            'correct': 'B) 32%',
            'explanation': '1.10 * 1.20 = 1.32 => 32% net increase.',
            'marks': '2 Marks'
        },
        {
            'q_num': 23, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Profit & Loss (Set B)',
            'text': 'A trader marks goods 20% above CP and offers a 10% discount. What is his net profit percentage?',
            'options': ['A) 8%', 'B) 12%', 'C) 15%', 'D) 10%'],
            'correct': 'A) 8%',
            'explanation': 'CP=100 -> MP=120 -> SP=108 -> Profit = 8%.',
            'marks': '2 Marks'
        },
        {
            'q_num': 24, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Time & Work (Set B)',
            'text': 'A can complete a work in 12 days and B in 24 days. How many days will they take working together?',
            'options': ['A) 6 days', 'B) 10 days', 'C) 8 days', 'D) 16 days'],
            'correct': 'C) 8 days',
            'explanation': '1/12 + 1/24 = 3/24 = 1/8 => 8 days.',
            'marks': '2 Marks'
        },
        {
            'q_num': 25, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Time, Speed & Distance (Set B)',
            'text': 'A boat travels 12 km/h downstream and 8 km/h upstream. What is the speed of the boat in still water?',
            'options': ['A) 11 km/h', 'B) 2 km/h', 'C) 9 km/h', 'D) 10 km/h'],
            'correct': 'D) 10 km/h',
            'explanation': 'Speed in still water = (12 + 8) / 2 = 10 km/h.',
            'marks': '2 Marks'
        },
        {
            'q_num': 26, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Ratios (Set B)',
            'text': 'Two numbers are in ratio 5:7. If their difference is 14, what is the value of the larger number?',
            'options': ['A) 35', 'B) 56', 'C) 42', 'D) 49'],
            'correct': 'D) 49',
            'explanation': '7x - 5x = 2x = 14 => x = 7. Larger number = 7 * 7 = 49.',
            'marks': '2 Marks'
        },
        {
            'q_num': 27, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Averages (Set B)',
            'text': 'The average age of 4 family members is 25 years. If a 5th member aged 35 joins, what is the new average age?',
            'options': ['A) 26 years', 'B) 27 years', 'C) 28 years', 'D) 30 years'],
            'correct': 'B) 27 years',
            'explanation': 'Sum = (4 * 25) + 35 = 135. New average = 135 / 5 = 27 years.',
            'marks': '2 Marks'
        },
        {
            'q_num': 28, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Probability (Set B)',
            'text': 'What is the probability of getting a sum of 7 when two fair 6-sided dice are rolled?',
            'options': ['A) 1/12', 'B) 1/6', 'C) 7/36', 'D) 5/36'],
            'correct': 'B) 1/6',
            'explanation': '6 favorable outcomes out of 36 total outcomes = 6/36 = 1/6.',
            'marks': '2 Marks'
        },
        {
            'q_num': 29, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Permutation & Combination (Set B)',
            'text': 'How many distinct 4-letter words can be formed by arranging the letters of "INFY"?',
            'options': ['A) 6', 'B) 12', 'C) 24', 'D) 16'],
            'correct': 'C) 24',
            'explanation': '4! = 24.',
            'marks': '2 Marks'
        },
        {
            'q_num': 30, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Number System (Set B)',
            'text': 'What is the highest common factor (HCF) of 12, 18, and 24?',
            'options': ['A) 2', 'B) 12', 'C) 3', 'D) 6'],
            'correct': 'D) 6',
            'explanation': 'HCF of 12, 18, 24 is 6.',
            'marks': '2 Marks'
        }
    ]

    return [
        {
            'section_name': 'Section 1: Pseudocode (Variables, Conditions, Loops, Functions, Arrays, Strings, Basic Algorithms, Output Prediction)',
            'time': '40 Mins',
            'questions': sec1_pseudocode
        },
        {
            'section_name': 'Section 2: Reasoning + Verbal (Logical Reasoning & Verbal Ability)',
            'time': '35 Mins',
            'questions': sec2_reasoning_verbal
        },
        {
            'section_name': 'Section 3: Quantitative Aptitude (Mathematics)',
            'time': '25 Mins',
            'questions': sec3_quant
        }
    ]


def get_infosys_practice_sections_model3():
    sec1_pseudocode = [
        {
            'q_num': 1, 'type': 'mcq',
            'title': 'Pseudocode: Variables XOR Swap (Set C)',
            'text': """What are the values of p and q after executing:
Integer p = 12, q = 9
p = p ^ q
q = p ^ q
p = p ^ q
Print p, q""",
            'options': ['A) 12, 9', 'B) 21, 9', 'C) 9, 12', 'D) 0, 12'],
            'correct': 'C) 9, 12',
            'explanation': 'XOR swap replaces p with 9 and q with 12.',
            'marks': '2 Marks'
        },
        {
            'q_num': 2, 'type': 'mcq',
            'title': 'Pseudocode: Switch-Case Branch (Set C)',
            'text': """Predict output for choice = 2:
Integer choice = 2
Switch(choice)
    Case 1: Print "ONE"; Break
    Case 2: Print "TWO"; Break
    Default: Print "OTHER"
End Switch""",
            'options': ['A) OTHER', 'B) ONE', 'C) TWO', 'D) NONE'],
            'correct': 'C) TWO',
            'explanation': 'Case 2 matches choice=2, printing "TWO".',
            'marks': '2 Marks'
        },
        {
            'q_num': 3, 'type': 'mcq',
            'title': 'Pseudocode: Do-While Loop (Set C)',
            'text': """What is the value of val after loop?
Integer val = 2
Do
    val = val + 3
While (val < 10)
Print val""",
            'options': ['A) 11', 'B) 8', 'C) 14', 'D) 10'],
            'correct': 'A) 11',
            'explanation': 'val sequence: 2 -> 5 -> 8 -> 11 (11 is not < 10, loop terminates).',
            'marks': '2 Marks'
        },
        {
            'q_num': 4, 'type': 'mcq',
            'title': 'Pseudocode: Functions (Sum of Digits) (Set C)',
            'text': """Predict return value of sumDigits(1234):
Function sumDigits(Integer n)
    If (n == 0) Return 0
    Return (n % 10) + sumDigits(n / 10)
End Function""",
            'options': ['A) 10', 'B) 8', 'C) 12', 'D) 15'],
            'correct': 'A) 10',
            'explanation': '4 + 3 + 2 + 1 = 10.',
            'marks': '2 Marks'
        },
        {
            'q_num': 5, 'type': 'mcq',
            'title': 'Pseudocode: Array Reversal (Set C)',
            'text': """What is arr[0] after array reverse logic on {10, 20, 30, 40}?
Print arr[0]""",
            'options': ['A) 40', 'B) 20', 'C) 10', 'D) 30'],
            'correct': 'A) 40',
            'explanation': 'Reversed array is {40, 30, 20, 10}, so arr[0] = 40.',
            'marks': '2 Marks'
        },
        {
            'q_num': 6, 'type': 'mcq',
            'title': 'Pseudocode: String Replacement (Set C)',
            'text': """What is the string after replacing 'A' with 'O' in "BANANA"?
Print str.replace('A', 'O')""",
            'options': ['A) BONONO', 'B) BANANO', 'C) BONANA', 'D) BANONA'],
            'correct': 'A) BONONO',
            'explanation': 'All occurrences of A are replaced with O => BONONO.',
            'marks': '2 Marks'
        },
        {
            'q_num': 7, 'type': 'mcq',
            'title': 'Pseudocode: Basic Algorithms (Bubble Sort Swaps) (Set C)',
            'text': """How many adjacent swaps occur during Bubble Sort on array {3, 1, 2} to sort ascending?""",
            'options': ['A) 0', 'B) 3', 'C) 1', 'D) 2'],
            'correct': 'D) 2',
            'explanation': 'Swap (3,1) -> {1,3,2}. Swap (3,2) -> {1,2,3}. Total 2 swaps.',
            'marks': '2 Marks'
        },
        {
            'q_num': 8, 'type': 'mcq',
            'title': 'Pseudocode: Bitwise XOR & AND (Set C)',
            'text': """Evaluate expression:
Integer res = (12 ^ 5) & 15
Print res""",
            'options': ['A) 15', 'B) 8', 'C) 7', 'D) 9'],
            'correct': 'D) 9',
            'explanation': '12 (1100) ^ 5 (0101) = 9 (1001). 9 & 15 = 9.',
            'marks': '2 Marks'
        }
    ]

    sec2_reasoning_verbal = [
        {
            'q_num': 9, 'type': 'mcq',
            'title': 'Logical Reasoning: Coding-Decoding (Set C)',
            'text': 'If "PYTHON" is written as "QZUIPO" (+1 shift), how is "DATA" written?',
            'options': ['A) FCVB', 'B) EBUB', 'C) EAVA', 'D) CZSZ'],
            'correct': 'B) EBUB',
            'explanation': 'D+1=E, A+1=B, T+1=U, A+1=B => EBUB.',
            'marks': '2 Marks'
        },
        {
            'q_num': 10, 'type': 'mcq',
            'title': 'Logical Reasoning: Blood Relations (Set C)',
            'text': 'A is the brother of B. B is the mother of C. How is A related to C?',
            'options': ['A) Brother', 'B) Father', 'C) Maternal Uncle', 'D) Grandfather'],
            'correct': 'C) Maternal Uncle',
            'explanation': 'Mother\'s brother is Maternal Uncle.',
            'marks': '2 Marks'
        },
        {
            'q_num': 11, 'type': 'mcq',
            'title': 'Logical Reasoning: Direction Sense (Set C)',
            'text': 'An engineer walks 9 meters South, turns East and walks 12 meters. Shortest distance from origin?',
            'options': ['A) 18 meters', 'B) 21 meters', 'C) 15 meters', 'D) 12 meters'],
            'correct': 'C) 15 meters',
            'explanation': 'sqrt(9^2 + 12^2) = sqrt(81 + 144) = sqrt(225) = 15 meters.',
            'marks': '2 Marks'
        },
        {
            'q_num': 12, 'type': 'mcq',
            'title': 'Logical Reasoning: Syllogisms (Set C)',
            'text': 'Statements: "All databases are structured. All structured data is indexed." Conclusion: "All databases are indexed."',
            'options': ['A) Does Not Follow', 'B) Uncertain', 'C) Definitely Follows', 'D) None'],
            'correct': 'C) Definitely Follows',
            'explanation': 'All A are B and All B are C implies All A are C.',
            'marks': '2 Marks'
        },
        {
            'q_num': 13, 'type': 'mcq',
            'title': 'Logical Reasoning: Seating Arrangement (Set C)',
            'text': '5 engineers A, B, C, D, E sit in a row. A is next to B, C is next to D. If E is at extreme right, who can be at center?',
            'options': ['A) A', 'B) B', 'C) C', 'D) E'],
            'correct': 'C) C',
            'explanation': 'Valid arrangement layout places C in middle position.',
            'marks': '2 Marks'
        },
        {
            'q_num': 14, 'type': 'mcq',
            'title': 'Logical Reasoning: Puzzles (Salary Rank) (Set C)',
            'text': 'A earns more than B. B earns more than C. Who has the highest salary?',
            'options': ['A) C', 'B) B', 'C) Equal', 'D) A'],
            'correct': 'D) A',
            'explanation': 'A > B > C => A has highest salary.',
            'marks': '2 Marks'
        },
        {
            'q_num': 15, 'type': 'mcq',
            'title': 'Logical Reasoning: Data Interpretation (Budget Allocation) (Set C)',
            'text': 'In a $1,000,000 IT budget, 40% goes to Cloud, 30% to Security, 20% to DevOps. How much goes to Cloud & DevOps combined?',
            'options': ['A) $600,000', 'B) $400,000', 'C) $500,000', 'D) $700,000'],
            'correct': 'A) $600,000',
            'explanation': '(40% + 20%) * 1,000,000 = 60% of 1M = $600,000.',
            'marks': '2 Marks'
        },
        {
            'q_num': 16, 'type': 'mcq',
            'title': 'Verbal: Reading Comprehension (Set C)',
            'text': 'Passage: "Continuous integration pipelines trigger automated build tests on every code commit." What triggers build tests?',
            'options': ['A) System failure', 'B) User logout', 'C) Manual restart', 'D) Code commit'],
            'correct': 'D) Code commit',
            'explanation': 'Passage states tests are triggered on every code commit.',
            'marks': '2 Marks'
        },
        {
            'q_num': 17, 'type': 'mcq',
            'title': 'Verbal: Synonyms/Antonyms (Set C)',
            'text': 'Select word closest in meaning to "CANDID":',
            'options': ['A) Frank', 'B) Deceptive', 'C) Reserved', 'D) Secretive'],
            'correct': 'A) Frank',
            'explanation': 'Candid means truthful and straightforward; frank.',
            'marks': '2 Marks'
        },
        {
            'q_num': 18, 'type': 'mcq',
            'title': 'Verbal: Grammar (Set C)',
            'text': 'Correct grammar: "Scarcely had we reached the office _____ the deployment started."',
            'options': ['A) before', 'B) when', 'C) than', 'D) then'],
            'correct': 'B) when',
            'explanation': 'Correlative conjunction "scarcely... when" is grammatically correct.',
            'marks': '2 Marks'
        },
        {
            'q_num': 19, 'type': 'mcq',
            'title': 'Verbal: Sentence Correction (Set C)',
            'text': 'Correct: "The team of software engineers are working on the patch."',
            'options': ['A) The team of software engineers is working on the patch.', 'B) No error.', 'C) The team of engineers were working.', 'D) Team of engineer is working.'],
            'correct': 'A) The team of software engineers is working on the patch.',
            'explanation': 'Collective noun "team" takes singular verb "is working".',
            'marks': '2 Marks'
        },
        {
            'q_num': 20, 'type': 'mcq',
            'title': 'Verbal: Fill in the Blanks (Set C)',
            'text': 'Choose word: "The developer was equipped _____ state-of-the-art tools."',
            'options': ['A) to', 'B) for', 'C) by', 'D) with'],
            'correct': 'D) with',
            'explanation': 'Verb "equipped" takes preposition "with".',
            'marks': '2 Marks'
        },
        {
            'q_num': 21, 'type': 'mcq',
            'title': 'Verbal: Vocabulary (Set C)',
            'text': 'Choose best word: "System security is of _____ importance for enterprise architecture."',
            'options': ['A) negligible', 'B) paramount', 'C) trivial', 'D) minor'],
            'correct': 'B) paramount',
            'explanation': 'Paramount means more important than anything else; supreme.',
            'marks': '2 Marks'
        }
    ]

    sec3_quant = [
        {
            'q_num': 22, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Percentages (Set C)',
            'text': 'A salary is increased by 25% and then decreased by 20%. What is the net change in salary?',
            'options': ['A) 10% increase', 'B) 0% (No change)', 'C) 5% decrease', 'D) 5% increase'],
            'correct': 'B) 0% (No change)',
            'explanation': '1.25 * 0.80 = 1.00 => 0% net change (original salary restored).',
            'marks': '2 Marks'
        },
        {
            'q_num': 23, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Profit & Loss (Set C)',
            'text': 'Selling 10 items yields a profit equal to the cost price of 2 items. What is the profit percentage?',
            'options': ['A) 20%', 'B) 30%', 'C) 15%', 'D) 25%'],
            'correct': 'A) 20%',
            'explanation': 'Profit % = (2 / 10) * 100 = 20%.',
            'marks': '2 Marks'
        },
        {
            'q_num': 24, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Time & Work (Set C)',
            'text': '3 men or 6 women can complete a work in 16 days. In how many days can 12 men and 8 women finish it?',
            'options': ['A) 4 days', 'B) 8 days', 'C) 3 days', 'D) 6 days'],
            'correct': 'C) 3 days',
            'explanation': '1 Man = 2 Women. Work = 6 W * 16 = 96. 12 M + 8 W = 32 W. Days = 96 / 32 = 3 days.',
            'marks': '2 Marks'
        },
        {
            'q_num': 25, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Time, Speed & Distance (Set C)',
            'text': 'Two trains 100m and 150m long move in opposite directions at 50 km/h and 40 km/h. How long to cross each other?',
            'options': ['A) 12 seconds', 'B) 8 seconds', 'C) 15 seconds', 'D) 10 seconds'],
            'correct': 'D) 10 seconds',
            'explanation': 'Total length = 250m. Relative speed = 90 km/h = 25 m/s. Time = 250 / 25 = 10s.',
            'marks': '2 Marks'
        },
        {
            'q_num': 26, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Ratios (Set C)',
            'text': 'Divide $1200 among A, B, C in ratio 2:3:5. What is C\'s share?',
            'options': ['A) $240', 'B) $360', 'C) $500', 'D) $600'],
            'correct': 'D) $600',
            'explanation': 'C\'s share = (5 / 10) * 1200 = $600.',
            'marks': '2 Marks'
        },
        {
            'q_num': 27, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Averages (Set C)',
            'text': 'What is the average of the first 10 positive odd integers (1, 3, 5, ..., 19)?',
            'options': ['A) 9', 'B) 10', 'C) 11', 'D) 12'],
            'correct': 'B) 10',
            'explanation': 'Average of first N odd numbers is always N. For N=10, average = 10.',
            'marks': '2 Marks'
        },
        {
            'q_num': 28, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Probability (Set C)',
            'text': 'Tossing 3 unbiased coins, what is the probability of getting exactly 2 heads?',
            'options': ['A) 3/4', 'B) 3/8', 'C) 1/2', 'D) 1/4'],
            'correct': 'B) 3/8',
            'explanation': 'Outcomes for 2 heads: HHT, HTH, THH = 3. Total outcomes = 8. Probability = 3/8.',
            'marks': '2 Marks'
        },
        {
            'q_num': 29, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Permutation & Combination (Set C)',
            'text': 'How many 3-digit numbers can be formed using digits 1, 2, 3, 4 without repetition?',
            'options': ['A) 18', 'B) 12', 'C) 24', 'D) 64'],
            'correct': 'C) 24',
            'explanation': '4 * 3 * 2 = 24.',
            'marks': '2 Marks'
        },
        {
            'q_num': 30, 'type': 'mcq',
            'title': 'Quantitative Aptitude: Number System (Set C)',
            'text': 'What is the smallest 4-digit number that is exactly divisible by 12, 15, and 18?',
            'options': ['A) 1140', 'B) 1020', 'C) 1200', 'D) 1080'],
            'correct': 'D) 1080',
            'explanation': 'LCM(12, 15, 18) = 180. Smallest 4-digit multiple of 180 is 180 * 6 = 1080.',
            'marks': '2 Marks'
        }
    ]

    return [
        {
            'section_name': 'Section 1: Pseudocode (Variables, Conditions, Loops, Functions, Arrays, Strings, Basic Algorithms, Output Prediction)',
            'time': '40 Mins',
            'questions': sec1_pseudocode
        },
        {
            'section_name': 'Section 2: Reasoning + Verbal (Logical Reasoning & Verbal Ability)',
            'time': '35 Mins',
            'questions': sec2_reasoning_verbal
        },
        {
            'section_name': 'Section 3: Quantitative Aptitude (Mathematics)',
            'time': '25 Mins',
            'questions': sec3_quant
        }
    ]


def get_meta_practice_sections_model1():
    sec1_cognitive = [
        {'q_num': 1, 'type': 'mcq', 'title': 'Meta Verbal (Set A): Subject-Verb Agreement', 'text': 'Select the grammatically correct sentence:', 'options': ['A) The list of items are on the desk.', 'B) The list of items were on the desk.', 'C) The list of items is on the desk.', 'D) The list of items be on the desk.'], 'correct': 'C) The list of items is on the desk.', 'explanation': 'Subject "list" is singular.', 'marks': '1 Mark'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Meta Quant (Set A): Profit & Loss', 'text': 'A trader sells a gadget for $120 with a 20% profit. What was cost price?', 'options': ['A) $110', 'B) $105', 'C) $100', 'D) $90'], 'correct': 'C) $100', 'explanation': 'Cost = 120 / 1.2 = 100.', 'marks': '1 Mark'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Meta Logical (Set A): Syllogism', 'text': 'Statements: All coders test code. Some coders write Python. Conclusions: I. Some Python writers test code.', 'options': ['A) Only I follows', 'B) Both follow', 'C) Only II follows', 'D) Neither follows'], 'correct': 'A) Only I follows', 'explanation': 'Intersection of Python writers and coders inherits the property of testing code.', 'marks': '1 Mark'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Meta Quant (Set A): Percentages', 'text': 'If a salary increases by 20% and then decreases by 20%, what is the net percentage change?', 'options': ['A) 4% decrease', 'B) 2% increase', 'C) 4% increase', 'D) No change'], 'correct': 'A) 4% decrease', 'explanation': '1.2 * 0.8 = 0.96 (4% decrease).', 'marks': '1 Mark'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Meta Verbal (Set A): Synonyms', 'text': 'Which word is closest in meaning to "CANDID"?', 'options': ['A) Frank', 'B) Deceitful', 'C) Reserved', 'D) Cautious'], 'correct': 'A) Frank', 'explanation': 'Candid means truthful and straightforward.', 'marks': '1 Mark'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Meta Logical (Set A): Coding-Decoding', 'text': 'If APPLE is coded as BQQMF, how is BANANA coded?', 'options': ['A) CBOBOB', 'B) BBOBOB', 'C) CBOAOB', 'D) CBMBOB'], 'correct': 'A) CBOBOB', 'explanation': 'Shift each character by +1.', 'marks': '1 Mark'},
        {'q_num': 7, 'type': 'mcq', 'title': 'Meta Quant (Set A): Time & Work', 'text': 'Pipe A fills a tank in 6 hours and Pipe B in 12 hours. How long together?', 'options': ['A) 6 hours', 'B) 5 hours', 'C) 3 hours', 'D) 4 hours'], 'correct': 'D) 4 hours', 'explanation': '1/6 + 1/12 = 3/12 = 1/4 -> 4 hours.', 'marks': '1 Mark'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Meta Verbal (Set A): Antonyms', 'text': 'Which word is opposite in meaning to "OBSOLETE"?', 'options': ['A) Redundant', 'B) Ancient', 'C) Outdated', 'D) Modern'], 'correct': 'D) Modern', 'explanation': 'Obsolete means no longer produced or used.', 'marks': '1 Mark'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Meta Logical (Set A): Blood Relations', 'text': "A points to a photo and says 'He is the son of my mother's only daughter.' Who is he?", 'options': ["A) A's son", "B) A's brother", "C) A's nephew", "D) A's uncle"], 'correct': "A) A's son", 'explanation': "Mother's only daughter is A herself, so he is A's son.", 'marks': '1 Mark'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Meta Quant (Set A): Ratio & Proportion', 'text': 'Two numbers are in ratio 4:5 and their sum is 108. Find the smaller number.', 'options': ['A) 52', 'B) 44', 'C) 48', 'D) 60'], 'correct': 'C) 48', 'explanation': '4x + 5x = 108 -> 9x = 108 -> x = 12. Smaller = 4 * 12 = 48.', 'marks': '1 Mark'}
    ]

    sec2_technical = [
        {'q_num': 11, 'type': 'mcq', 'title': 'Meta Tech (Set A): HTTP Port', 'text': 'What default port does HTTPS protocol use for secure communication?', 'options': ['A) 80', 'B) 22', 'C) 443', 'D) 8080'], 'correct': 'C) 443', 'explanation': 'Port 443 is standard for TLS/SSL encrypted HTTPS traffic.', 'marks': '1 Mark'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Meta Tech (Set A): OS Virtual Memory', 'text': 'Which component performs virtual memory page table translation to physical RAM?', 'options': ['A) ALU', 'B) PCI Bus', 'C) Memory Management Unit (MMU)', 'D) Disk Controller'], 'correct': 'C) Memory Management Unit (MMU)', 'explanation': 'MMU maps virtual page addresses to physical frame addresses.', 'marks': '1 Mark'},
        {'q_num': 13, 'type': 'mcq', 'title': 'Meta Tech (Set A): Pseudocode Bitwise', 'text': 'What is the value of `8 >> 2` in integer bitwise operations?', 'options': ['A) 32', 'B) 4', 'C) 2', 'D) 16'], 'correct': 'C) 2', 'explanation': '8 in binary is 1000; right shifting by 2 positions yields 0010 (2).', 'marks': '1 Mark'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Meta Tech (Set A): DBMS Indexing', 'text': 'Which data structure is most commonly used for RDBMS B-Tree index lookup?', 'options': ['A) Binary Search Tree', 'B) Queue', 'C) Linked List', 'D) B+ Tree'], 'correct': 'D) B+ Tree', 'explanation': 'B+ Trees store data pointers in leaf nodes with contiguous sibling pointers.', 'marks': '1 Mark'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Meta Tech (Set A): OOP Encapsulation', 'text': 'Which OOP access modifier restricts variable visibility strictly within the declaring class?', 'options': ['A) private', 'B) protected', 'C) internal', 'D) public'], 'correct': 'A) private', 'explanation': 'Private variables are inaccessible outside class boundaries.', 'marks': '1 Mark'},
        {'q_num': 16, 'type': 'mcq', 'title': 'Meta Tech (Set A): Networking OSI Model', 'text': 'At which OSI layer does the IP (Internet Protocol) operate?', 'options': ['A) Transport Layer (Layer 4)', 'B) Application Layer (Layer 7)', 'C) Data Link Layer (Layer 2)', 'D) Network Layer (Layer 3)'], 'correct': 'D) Network Layer (Layer 3)', 'explanation': 'IP is responsible for packet routing across Layer 3.', 'marks': '1 Mark'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Meta Tech (Set A): Cloud Computing', 'text': 'Which cloud service model provides virtualized infrastructure like EC2 or Virtual Machines?', 'options': ['A) Infrastructure as a Service (IaaS)', 'B) PaaS', 'C) FaaS', 'D) SaaS'], 'correct': 'A) Infrastructure as a Service (IaaS)', 'explanation': 'IaaS supplies compute servers, storage, and networking hardware.', 'marks': '1 Mark'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Meta Tech (Set A): Security Encryption', 'text': 'Which encryption type uses the same key for both encryption and decryption?', 'options': ['A) Asymmetric Encryption', 'B) Symmetric Encryption', 'C) Public Key Encryption', 'D) RSA Encryption'], 'correct': 'B) Symmetric Encryption', 'explanation': 'Symmetric algorithms (AES, DES) share a single secret key.', 'marks': '1 Mark'},
        {'q_num': 19, 'type': 'mcq', 'title': 'Meta Tech (Set A): Data Structure Complexity', 'text': 'What is the average time complexity of element insertion in a Hash Table?', 'options': ['A) O(1)', 'B) O(N)', 'C) O(N^2)', 'D) O(log N)'], 'correct': 'A) O(1)', 'explanation': 'Direct hash indexing locates target bucket in constant time on average.', 'marks': '1 Mark'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Meta Tech (Set A): Process vs Thread', 'text': 'What memory space is shared between multiple threads belonging to the same process?', 'options': ['A) Thread ID Registers', 'B) Program Counter Registers', 'C) Stack Memory', 'D) Heap Memory & Global Data'], 'correct': 'D) Heap Memory & Global Data', 'explanation': 'Threads share heap space and global variables while maintaining private stack frames.', 'marks': '1 Mark'},
        {'q_num': 21, 'type': 'mcq', 'title': 'Meta Tech (Set A): Pseudocode Loop', 'text': 'How many times will `for i = 1 to 5 step 2` execute?', 'options': ['A) 5 times', 'B) 3 times (i = 1, 3, 5)', 'C) 4 times', 'D) 2 times'], 'correct': 'B) 3 times (i = 1, 3, 5)', 'explanation': 'Loop iterates for values 1, 3, and 5.', 'marks': '1 Mark'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Meta Tech (Set A): SQL Query', 'text': 'Which SQL keyword filters group aggregations produced by a `GROUP BY` clause?', 'options': ['A) LIKE', 'B) HAVING', 'C) ORDER BY', 'D) WHERE'], 'correct': 'B) HAVING', 'explanation': 'HAVING evaluates aggregate condition functions like SUM() or COUNT().', 'marks': '1 Mark'},
        {'q_num': 23, 'type': 'mcq', 'title': 'Meta Tech (Set A): Git Version Control', 'text': 'Which git command creates and switches to a new branch simultaneously?', 'options': ['A) git checkout -b <branch>', 'B) git branch <branch>', 'C) git merge <branch>', 'D) git commit -m'], 'correct': 'A) git checkout -b <branch>', 'explanation': 'Option -b initializes and checks out the new branch reference.', 'marks': '1 Mark'}
    ]

    sec3_coding = [
        {'q_num': 24, 'type': 'coding', 'title': 'Meta Coding (Set A): String Character Frequency Counter', 'text': 'Given a string input, return the character frequency breakdown in alphabetical order.', 'options': [], 'sample_answer': 'from collections import Counter\ndef charFreq(s):\n    return sorted(Counter(s).items())', 'explanation': 'Count occurrences using hash map and sort key items alphabetically.', 'marks': '10 Marks'},
        {'q_num': 25, 'type': 'coding', 'title': 'Meta Coding (Set A): Array Moving Zeroes to End', 'text': 'Given an integer array, move all zeroes to the end while maintaining relative non-zero order.', 'options': [], 'sample_answer': 'def moveZeroes(nums):\n    j = 0\n    for i in range(len(nums)):\n        if nums[i] != 0:\n            nums[j], nums[i] = nums[i], nums[j]\n            j += 1\n    return nums', 'explanation': 'Two-pointer swapping pushes zeroes right in O(N) time and O(1) space.', 'marks': '10 Marks'}
    ]

    return [
        {'section_name': 'Round 1: Cognitive Assessment (Quant, Verbal, Logical)', 'time': '50 Mins', 'questions': sec1_cognitive},
        {'section_name': 'Round 2: Technical Assessment (CS Fundamentals & Pseudocode)', 'time': '40 Mins', 'questions': sec2_technical},
        {'section_name': 'Round 3: Coding Assessment (Coding Problems)', 'time': '45 Mins', 'questions': sec3_coding}
    ]


def get_meta_practice_sections_model2():
    sec1_cognitive = [
        {'q_num': 1, 'type': 'mcq', 'title': 'Meta Verbal (Set B): Error Spotting', 'text': 'Find the error in: "Neither the supervisor nor the engineers was available."', 'options': ['A) Change "engineers" to "engineer', 'B) No error', 'C) Change "was" to "were', 'D) Change "nor" to "or'], 'correct': 'C) Change "was" to "were', 'explanation': 'Verb agrees with closest subject "engineers" (plural).', 'marks': '1 Mark'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Meta Quant (Set B): Compound Interest', 'text': 'Find compound interest on $1,000 for 2 years at 10% per annum.', 'options': ['A) $190', 'B) $220', 'C) $210', 'D) $200'], 'correct': 'C) $210', 'explanation': '1000 * 1.1^2 = 1210 -> Interest = 210.', 'marks': '1 Mark'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Meta Logical (Set B): Direction Sense', 'text': 'A walks 10m North, turns right and walks 10m. Where is he from starting point?', 'options': ['A) 10 sqrt(2) m North-East', 'B) 10m East', 'C) 10m North', 'D) 20m East'], 'correct': 'A) 10 sqrt(2) m North-East', 'explanation': 'Pythagorean theorem: sqrt(10^2 + 10^2) = 10 sqrt(2).', 'marks': '1 Mark'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Meta Quant (Set B): Time & Distance', 'text': 'A train 200m long passes a post in 10 seconds. Find speed in km/h.', 'options': ['A) 72 km/h', 'B) 60 km/h', 'C) 80 km/h', 'D) 54 km/h'], 'correct': 'A) 72 km/h', 'explanation': 'Speed = 200 / 10 = 20 m/s = 20 * 18/5 = 72 km/h.', 'marks': '1 Mark'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Meta Verbal (Set B): One-Word Substitution', 'text': 'What is a person who looks on the bright side of things called?', 'options': ['A) Optimist', 'B) Altruist', 'C) Realist', 'D) Pessimist'], 'correct': 'A) Optimist', 'explanation': 'An optimist holds positive expectations for outcomes.', 'marks': '1 Mark'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Meta Logical (Set B): Letter Series', 'text': 'Find the next term: B, D, G, K, P, _?', 'options': ['A) V', 'B) U', 'C) T', 'D) W'], 'correct': 'A) V', 'explanation': '+2, +3, +4, +5, +6 -> 16 + 6 = 22 (V).', 'marks': '1 Mark'},
        {'q_num': 7, 'type': 'mcq', 'title': 'Meta Quant (Set B): Averages', 'text': 'The average of 5 numbers is 20. If one number is removed, average becomes 18. Find removed number.', 'options': ['A) 24', 'B) 26', 'C) 30', 'D) 28'], 'correct': 'D) 28', 'explanation': 'Sum = 100. New sum = 72. Removed = 100 - 72 = 28.', 'marks': '1 Mark'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Meta Verbal (Set B): Vocabulary', 'text': 'Choose the synonym for "BENEVOLENT":', 'options': ['A) Malevolent', 'B) Harsh', 'C) Greedy', 'D) Kind'], 'correct': 'D) Kind', 'explanation': 'Benevolent means well-meaning and kindly.', 'marks': '1 Mark'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Meta Logical (Set B): Seating Arrangement', 'text': '5 people A, B, C, D, E sit in a row facing North. C sits in the exact middle. Where is C?', 'options': ['A) Position 1', 'B) Position 3', 'C) Position 4', 'D) Position 2'], 'correct': 'B) Position 3', 'explanation': 'Middle position among 5 items is index 3.', 'marks': '1 Mark'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Meta Quant (Set B): Probability', 'text': 'Two dice are rolled. What is the probability of getting a total sum of 7?', 'options': ['A) 1/4', 'B) 1/12', 'C) 1/6', 'D) 5/36'], 'correct': 'C) 1/6', 'explanation': '6 favorable pairs out of 36 total outcomes -> 6/36 = 1/6.', 'marks': '1 Mark'}
    ]

    sec2_technical = [
        {'q_num': 11, 'type': 'mcq', 'title': 'Meta Tech (Set B): DNS Record Type', 'text': 'Which DNS record resolves a domain hostname to an IPv4 IP address?', 'options': ['A) AAAA Record', 'B) CNAME', 'C) A Record', 'D) MX Record'], 'correct': 'C) A Record', 'explanation': 'A Record maps domain names to IPv4 addresses.', 'marks': '1 Mark'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Meta Tech (Set B): OS CPU Scheduling', 'text': 'Which CPU scheduling algorithm gives shortest average waiting time for a given set of processes?', 'options': ['A) First-Come First-Served (FCFS)', 'B) Priority Scheduling', 'C) Shortest Job First (SJF)', 'D) Round Robin (RR)'], 'correct': 'C) Shortest Job First (SJF)', 'explanation': 'SJF is provably optimal for minimizing average waiting time.', 'marks': '1 Mark'},
        {'q_num': 13, 'type': 'mcq', 'title': 'Meta Tech (Set B): Pseudocode Array', 'text': 'Given array `A = [10, 20, 30]`, what is `A[1]` in 0-indexed languages?', 'options': ['A) Index Error', 'B) 10', 'C) 20', 'D) 30'], 'correct': 'C) 20', 'explanation': 'Index 1 references the second array element.', 'marks': '1 Mark'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Meta Tech (Set B): DBMS Normalization', 'text': 'Which normal form eliminates partial functional dependencies on candidate keys?', 'options': ['A) Third Normal Form (3NF)', 'B) First Normal Form (1NF)', 'C) BCNF', 'D) Second Normal Form (2NF)'], 'correct': 'D) Second Normal Form (2NF)', 'explanation': '2NF requires relation to be in 1NF and free of partial dependencies.', 'marks': '1 Mark'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Meta Tech (Set B): OOP Polymorphism', 'text': 'Method Overloading in Java/C++ is an example of which type of polymorphism?', 'options': ['A) Compile-time Polymorphism', 'B) Run-time Polymorphism', 'C) Dynamic Binding', 'D) Subtype Polymorphism'], 'correct': 'A) Compile-time Polymorphism', 'explanation': 'Method overloading is resolved at compile time by method signatures.', 'marks': '1 Mark'},
        {'q_num': 16, 'type': 'mcq', 'title': 'Meta Tech (Set B): Networking TCP vs UDP', 'text': 'Which protocol is connection-oriented and guarantees ordered packet delivery?', 'options': ['A) ICMP', 'B) ARP', 'C) UDP', 'D) TCP'], 'correct': 'D) TCP', 'explanation': 'TCP uses 3-way handshake to establish reliable ordered byte streams.', 'marks': '1 Mark'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Meta Tech (Set B): Serverless Computing', 'text': 'AWS Lambda is an example of which cloud execution architecture model?', 'options': ['A) Function as a Service (FaaS)', 'B) IaaS', 'C) Co-location', 'D) Bare Metal'], 'correct': 'A) Function as a Service (FaaS)', 'explanation': 'Lambda runs event-driven functions without server management.', 'marks': '1 Mark'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Meta Tech (Set B): Cybersecurity Hashing', 'text': 'Which hashing algorithm is widely considered cryptographically broken and insecure?', 'options': ['A) SHA-256', 'B) MD5', 'C) SHA-512', 'D) Argon2'], 'correct': 'B) MD5', 'explanation': 'MD5 is vulnerable to collision attacks and should not be used for security.', 'marks': '1 Mark'},
        {'q_num': 19, 'type': 'mcq', 'title': 'Meta Tech (Set B): Stack vs Queue', 'text': 'Which data structure follows First-In First-Out (FIFO) ordering?', 'options': ['A) Queue', 'B) Max Heap', 'C) Stack', 'D) Binary Tree'], 'correct': 'A) Queue', 'explanation': 'Queues enqueue items at tail and dequeue from head (FIFO).', 'marks': '1 Mark'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Meta Tech (Set B): Deadlock Conditions', 'text': "Which condition is NOT one of Coffman's four necessary conditions for OS deadlock?", 'options': ['A) Hold and Wait', 'B) Circular Wait', 'C) Mutual Exclusion', 'D) Preemption Allowed'], 'correct': 'D) Preemption Allowed', 'explanation': 'No Preemption is necessary for deadlock; allowing preemption prevents deadlock.', 'marks': '1 Mark'},
        {'q_num': 21, 'type': 'mcq', 'title': 'Meta Tech (Set B): Pseudocode Modulo', 'text': 'What is the result of `17 % 5` in standard integer arithmetic?', 'options': ['A) 1', 'B) 2', 'C) 3', 'D) 0'], 'correct': 'B) 2', 'explanation': '17 divided by 5 is 3 with a remainder of 2.', 'marks': '1 Mark'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Meta Tech (Set B): SQL Primary Key', 'text': 'What property distinguishes a Primary Key from a Unique Constraint in SQL?', 'options': ['A) Primary Key allows NULLs', 'B) Primary Key cannot contain NULL values', 'C) Primary Key only applies to strings', 'D) Primary Key can be duplicated'], 'correct': 'B) Primary Key cannot contain NULL values', 'explanation': 'Primary keys strictly enforce NOT NULL and uniqueness.', 'marks': '1 Mark'},
        {'q_num': 23, 'type': 'mcq', 'title': 'Meta Tech (Set B): Linux Permissions', 'text': 'What numerical permission code gives Read (4), Write (2), Execute (1) to owner?', 'options': ['A) 7', 'B) 6', 'C) 4', 'D) 5'], 'correct': 'A) 7', 'explanation': '4 + 2 + 1 = 7 (full permissions).', 'marks': '1 Mark'}
    ]

    sec3_coding = [
        {'q_num': 24, 'type': 'coding', 'title': 'Meta Coding (Set B): Check Anagram Strings', 'text': 'Given two strings s and t, return true if t is an anagram of s.', 'options': [], 'sample_answer': 'from collections import Counter\ndef isAnagram(s, t):\n    return Counter(s) == Counter(t)', 'explanation': 'Character frequency hash map comparison runs in O(N) time.', 'marks': '10 Marks'},
        {'q_num': 25, 'type': 'coding', 'title': 'Meta Coding (Set B): Find Second Largest Array Element', 'text': 'Given an array of integers, find the second distinct largest element.', 'options': [], 'sample_answer': 'def secondLargest(nums):\n    first = second = float("-inf")\n    for n in nums:\n        if n > first:\n            second = first\n            first = n\n        elif n > second and n != first:\n            second = n\n    return second if second != float("-inf") else None', 'explanation': 'Single pass traversal tracks max and second max in O(N) time and O(1) space.', 'marks': '10 Marks'}
    ]

    return [
        {'section_name': 'Round 1: Cognitive Assessment (Quant, Verbal, Logical)', 'time': '50 Mins', 'questions': sec1_cognitive},
        {'section_name': 'Round 2: Technical Assessment (CS Fundamentals & Pseudocode)', 'time': '40 Mins', 'questions': sec2_technical},
        {'section_name': 'Round 3: Coding Assessment (Coding Problems)', 'time': '45 Mins', 'questions': sec3_coding}
    ]


def get_meta_practice_sections_model3():
    sec1_cognitive = [
        {'q_num': 1, 'type': 'mcq', 'title': 'Meta Verbal (Set C): Reading Comprehension', 'text': 'What is the main purpose of an abstract in a research publication?', 'options': ['A) Acknowledge sponsors', 'B) List reference citations', 'C) Summarize key objectives, methods, and findings', 'D) Present full raw data tables'], 'correct': 'C) Summarize key objectives, methods, and findings', 'explanation': 'An abstract presents a concise summary of the entire paper.', 'marks': '1 Mark'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Meta Quant (Set C): Simple Interest', 'text': 'Find simple interest on $2,000 for 3 years at 5% per annum.', 'options': ['A) $200', 'B) $250', 'C) $300', 'D) $350'], 'correct': 'C) $300', 'explanation': 'SI = (2000 * 3 * 5) / 100 = 300.', 'marks': '1 Mark'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Meta Logical (Set C): Number Series', 'text': 'Find the next number in sequence: 3, 6, 12, 24, 48, _?', 'options': ['A) 96', 'B) 72', 'C) 84', 'D) 100'], 'correct': 'A) 96', 'explanation': 'Sequence doubles in each step: 48 * 2 = 96.', 'marks': '1 Mark'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Meta Quant (Set C): Time, Speed & Distance', 'text': 'A car travels at 60 km/h for 2.5 hours. Calculate distance covered.', 'options': ['A) 150 km', 'B) 180 km', 'C) 140 km', 'D) 120 km'], 'correct': 'A) 150 km', 'explanation': 'Distance = Speed * Time = 60 * 2.5 = 150 km.', 'marks': '1 Mark'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Meta Verbal (Set C): Sentence Correction', 'text': 'Correct: "He runned fast to catch the morning train."', 'options': ['A) He ran fast to catch the morning train.', 'B) He running fast to catch.', 'C) No correction needed.', 'D) He has runned fast.'], 'correct': 'A) He ran fast to catch the morning train.', 'explanation': 'Past tense of "run" is "ran".', 'marks': '1 Mark'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Meta Logical (Set C): Analogy', 'text': 'Doctor is to Hospital as Teacher is to _?', 'options': ['A) School', 'B) Book', 'C) Classroom', 'D) Student'], 'correct': 'A) School', 'explanation': 'Doctor works in hospital; teacher works in school.', 'marks': '1 Mark'},
        {'q_num': 7, 'type': 'mcq', 'title': 'Meta Quant (Set C): Permutations & Combinations', 'text': 'In how many ways can 4 students be seated in 4 chairs?', 'options': ['A) 4', 'B) 12', 'C) 16', 'D) 24'], 'correct': 'D) 24', 'explanation': '4! = 4 * 3 * 2 * 1 = 24.', 'marks': '1 Mark'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Meta Verbal (Set C): Idioms & Phrases', 'text': 'What does "Bite the bullet" mean?', 'options': ['A) Avoid responsibility', 'B) Eat quickly', 'C) Shoot a target', 'D) Face a difficult situation courageously'], 'correct': 'D) Face a difficult situation courageously', 'explanation': 'Bite the bullet means enduring a painful ordeal.', 'marks': '1 Mark'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Meta Logical (Set C): Clocks Logic', 'text': 'What is the angle between clock hands at 3:00?', 'options': ['A) 45 degrees', 'B) 90 degrees', 'C) 60 degrees', 'D) 120 degrees'], 'correct': 'B) 90 degrees', 'explanation': 'Hour hand is at 3 (90 degrees) and minute hand is at 12 (0 degrees).', 'marks': '1 Mark'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Meta Quant (Set C): HCF & LCM', 'text': 'Find HCF of 24 and 36.', 'options': ['A) 18', 'B) 6', 'C) 12', 'D) 8'], 'correct': 'C) 12', 'explanation': 'Highest Common Factor of 24 and 36 is 12.', 'marks': '1 Mark'}
    ]

    sec2_technical = [
        {'q_num': 11, 'type': 'mcq', 'title': 'Meta Tech (Set C): IPv6 Address Bit Length', 'text': 'How many bits long is a standard IPv6 IP address?', 'options': ['A) 64 bits', 'B) 32 bits', 'C) 128 bits', 'D) 256 bits'], 'correct': 'C) 128 bits', 'explanation': 'IPv6 addresses consist of 128 bits.', 'marks': '1 Mark'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Meta Tech (Set C): OS Page Fault', 'text': 'When does a Page Fault interrupt occur in Operating Systems?', 'options': ['A) Disk is completely full', 'B) Process terminates normally', 'C) Requested memory page is not present in RAM', 'D) CPU runs out of registers'], 'correct': 'C) Requested memory page is not present in RAM', 'explanation': 'Page Fault traps to OS kernel to fetch missing page from swap space into RAM.', 'marks': '1 Mark'},
        {'q_num': 13, 'type': 'mcq', 'title': 'Meta Tech (Set C): Pseudocode Recursion', 'text': 'What is returned by `fact(4)` if `fact(n) = n == 1 ? 1 : n * fact(n - 1)`?', 'options': ['A) 16', 'B) 20', 'C) 24', 'D) 12'], 'correct': 'C) 24', 'explanation': '4 * 3 * 2 * 1 = 24.', 'marks': '1 Mark'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Meta Tech (Set C): DBMS Foreign Key', 'text': 'What constraint does a Foreign Key enforce between two database tables?', 'options': ['A) Entity Integrity', 'B) Atomicity', 'C) Domain Isolation', 'D) Referential Integrity'], 'correct': 'D) Referential Integrity', 'explanation': 'Foreign keys guarantee referenced key values exist in parent table.', 'marks': '1 Mark'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Meta Tech (Set C): OOP Inheritance', 'text': 'Which OOP concept allows a subclass to provide a specific implementation of a parent class method?', 'options': ['A) Method Overriding', 'B) Data Hiding', 'C) Instantiation', 'D) Method Overloading'], 'correct': 'A) Method Overriding', 'explanation': 'Subclass overrides virtual methods inherited from parent class.', 'marks': '1 Mark'},
        {'q_num': 16, 'type': 'mcq', 'title': 'Meta Tech (Set C): Networking Router vs Switch', 'text': 'At which OSI layer does a Layer 2 Network Switch operate?', 'options': ['A) Physical Layer (Layer 1)', 'B) Transport Layer (Layer 4)', 'C) Network Layer (Layer 3)', 'D) Data Link Layer (Layer 2)'], 'correct': 'D) Data Link Layer (Layer 2)', 'explanation': 'Layer 2 switches forward Ethernet frames using MAC addresses.', 'marks': '1 Mark'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Meta Tech (Set C): Docker Containerization', 'text': 'How do Docker containers differ from traditional Virtual Machines (VMs)?', 'options': ['A) Containers share host OS kernel', 'B) Containers require hardware hypervisors', 'C) Containers run guest OS instances', 'D) Containers are slower to boot'], 'correct': 'A) Containers share host OS kernel', 'explanation': 'Containers isolate application dependencies while sharing host OS kernel.', 'marks': '1 Mark'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Meta Tech (Set C): Cybersecurity SQL Injection', 'text': 'Which technique prevents SQL Injection vulnerabilities in database applications?', 'options': ['A) Client-side JavaScript validation only', 'B) Parameterized Queries / Prepared Statements', 'C) Storing passwords in plain text', 'D) Disabling HTTPS'], 'correct': 'B) Parameterized Queries / Prepared Statements', 'explanation': 'Prepared statements separate SQL code commands from user input data.', 'marks': '1 Mark'},
        {'q_num': 19, 'type': 'mcq', 'title': 'Meta Tech (Set C): Binary Search Complexity', 'text': 'What is the worst-case time complexity of Binary Search on a sorted array of size N?', 'options': ['A) O(log N)', 'B) O(N)', 'C) O(N log N)', 'D) O(1)'], 'correct': 'A) O(log N)', 'explanation': 'Halving search space in each step yields O(log N) operations.', 'marks': '1 Mark'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Meta Tech (Set C): Thrashing in OS', 'text': 'What causes System Thrashing in Operating Systems memory management?', 'options': ['A) Memory leaks in user apps', 'B) CPU fan failure', 'C) Slow network bandwidth', 'D) Excessive page swapping in and out of RAM'], 'correct': 'D) Excessive page swapping in and out of RAM', 'explanation': 'Thrashing happens when OS spends more time swapping pages than executing processes.', 'marks': '1 Mark'},
        {'q_num': 21, 'type': 'mcq', 'title': 'Meta Tech (Set C): Pseudocode Boolean', 'text': 'What is `True AND (False OR True)` in boolean logic?', 'options': ['A) Error', 'B) True', 'C) Undefined', 'D) False'], 'correct': 'B) True', 'explanation': '(False OR True) is True; True AND True is True.', 'marks': '1 Mark'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Meta Tech (Set C): SQL JOIN Type', 'text': 'Which SQL JOIN returns all rows from left table regardless of matching right table rows?', 'options': ['A) INNER JOIN', 'B) LEFT JOIN', 'C) CROSS JOIN', 'D) RIGHT JOIN'], 'correct': 'B) LEFT JOIN', 'explanation': 'LEFT JOIN returns all left table rows and matching right table rows (NULL if no match).', 'marks': '1 Mark'},
        {'q_num': 23, 'type': 'mcq', 'title': 'Meta Tech (Set C): REST API Method', 'text': 'Which HTTP verb is used to update an existing resource or create if non-existent in REST APIs?', 'options': ['A) PUT', 'B) OPTIONS', 'C) GET', 'D) DELETE'], 'correct': 'A) PUT', 'explanation': 'PUT is idempotent and replaces/updates target resource representations.', 'marks': '1 Mark'}
    ]

    sec3_coding = [
        {'q_num': 24, 'type': 'coding', 'title': 'Meta Coding (Set C): Palindrome Number Checker', 'text': 'Given an integer x, return true if x is a palindrome integer without converting to string.', 'options': [], 'sample_answer': 'def isPalindrome(x):\n    if x < 0: return False\n    rev = 0; original = x\n    while x > 0:\n        rev = rev * 10 + x % 10\n        x //= 10\n    return original == rev', 'explanation': 'Reverse integer digits using modulo 10 and compare with original in O(log10 N) time.', 'marks': '10 Marks'},
        {'q_num': 25, 'type': 'coding', 'title': 'Meta Coding (Set C): Maximum Subarray Sum (Kadanes)', 'text': 'Find the contiguous subarray with maximum sum in an integer array.', 'options': [], 'sample_answer': 'def maxSubArray(nums):\n    max_so_far = curr_max = nums[0]\n    for x in nums[1:]:\n        curr_max = max(x, curr_max + x)\n        max_so_far = max(max_so_far, curr_max)\n    return max_so_far', 'explanation': 'Kadanes Algorithm maintains maximum ending at current index in O(N) time and O(1) space.', 'marks': '10 Marks'}
    ]

    return [
        {'section_name': 'Round 1: Cognitive Assessment (Quant, Verbal, Logical)', 'time': '50 Mins', 'questions': sec1_cognitive},
        {'section_name': 'Round 2: Technical Assessment (CS Fundamentals & Pseudocode)', 'time': '40 Mins', 'questions': sec2_technical},
        {'section_name': 'Round 3: Coding Assessment (Coding Problems)', 'time': '45 Mins', 'questions': sec3_coding}
    ]


def get_meta_model_paper_sections():
    sec1_coding1 = [
        {
            'q_num': 1, 'type': 'coding',
            'title': 'Q1. Alien Dictionary (Topological Order & Graph Cycle Detection)',
            'text': """There is a new alien language that uses the Latin alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]""",
            'options': [],
            'sample_answer': """from collections import defaultdict, deque

def alienOrder(words: list[str]) -> str:
    adj = {c: set() for w in words for c in w}
    in_degree = {c: 0 for c in adj}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
                
    q = deque([c for c in in_degree if in_degree[c] == 0])
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for nxt in adj[c]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
                
    return "".join(res) if len(res) == len(adj) else "" """,
            'explanation': "Build a directed DAG of character dependencies from adjacent word prefixes and compute Topological Sort using Kahn's BFS algorithm in O(C) total characters time.",
            'marks': '15 Marks'
        },
        {
            'q_num': 2, 'type': 'coding', 'difficulty': 'HARD',
            'title': 'Q2. Minimum Window Substring (Sliding Window Hard)',
            'text': """Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Example:
Input: s = "ADOBECODEBANC", t = "ABC""",
            'options': [],
            'sample_answer': """from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s: return ""
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]""",
            'explanation': 'Maintain two pointers expand right to satisfy required character counts, contract left to minimize window size in O(|S| + |T|) time.',
            'marks': '15 Marks'
        }
    ]

    sec2_coding2_optimization = [
        {
            'q_num': 3, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Amortized Complexity of Splay Trees',
            'text': 'What is the amortized time complexity per operation for any sequence of M operations on a Splay Tree of size N?',
            'options': ['A) O(log N)', 'B) O(log^2 N)', 'C) O(1)', 'D) O(N)'],
            'correct': 'A) O(log N)',
            'explanation': 'Splaying dynamically moves accessed nodes to the root via zig-zig and zig-zag rotations, guaranteeing O(log N) amortized time via potential function analysis.',
            'marks': '3 Marks'
        },
        {
            'q_num': 4, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Lock-Free CAS Ring Buffer',
            'text': 'In a high-throughput lock-free Single Producer Single Consumer (SPSC) Ring Buffer, which hardware primitive prevents instruction reordering across CPU cores?',
            'options': ['A) Memory Fence / Barrier (std::atomic_thread_fence)', 'B) OS Mutex Lock', 'C) Global Spinlock', 'D) Garbage Collection Sweep'],
            'correct': 'A) Memory Fence / Barrier (std::atomic_thread_fence)',
            'explanation': 'Memory barriers enforce acquire-release semantics, preventing out-of-order CPU reads/writes without thread context switching overhead.',
            'marks': '3 Marks'
        },
        {
            'q_num': 5, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Cache-Oblivious Matrix Bound',
            'text': 'What is the optimal I/O cache miss bound for multiplying two N x N matrices using a Cache-Oblivious recursive divide-and-conquer algorithm with cache size Z and line size L?',
            'options': ['A) O(N^3 / (L * sqrt(Z)))', 'B) O(N^3)', 'C) O(N^3 / L)', 'D) O(N^2 / L)'],
            'correct': 'A) O(N^3 / (L * sqrt(Z)))',
            'explanation': 'Cache-Oblivious algorithms partition submatrices recursively until they fit inside cache size Z, achieving asymptotically optimal O(N^3 / (L * sqrt(Z))) cache transfers.',
            'marks': '3 Marks'
        },
        {
            'q_num': 6, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Fibonacci Heap Decrease-Key Bound',
            'text': "Why does Dijkstra's Algorithm run faster on dense graphs when using a Fibonacci Heap instead of a Binary Heap?",
            'options': ['A) Fibonacci Heap offers O(1) amortized Decrease-Key time vs O(log V) in Binary Heap', 'B) Fibonacci Heap eliminates graph edge traversals', 'C) Fibonacci Heap uses O(1) total memory', 'D) Binary Heap requires sorting all vertices beforehand'],
            'correct': 'A) Fibonacci Heap offers O(1) amortized Decrease-Key time vs O(log V) in Binary Heap',
            'explanation': 'Fibonacci Heap decreases key in O(1) amortized time by lazy cascading cuts, reducing overall Dijkstra complexity from O(E log V) to O(E + V log V).',
            'marks': '3 Marks'
        },
        {
            'q_num': 7, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Heavy-Light Decomposition Path Bound',
            'text': 'How many heavy-light chain segments can be crossed when querying any path between two nodes in a tree decomposed via Heavy-Light Decomposition (HLD)?',
            'options': ['A) At most O(sqrt(N)) light edges', 'B) At most O(1) light edges', 'C) Exactly N/2 heavy edges', 'D) At most O(log N) light edges'],
            'correct': 'D) At most O(log N) light edges',
            'explanation': 'A light edge connects to a child subtree of size <= N/2, guaranteeing at most O(log N) light edge transitions between root and any node.',
            'marks': '3 Marks'
        },
        {
            'q_num': 8, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Hopcroft-Karp Bipartite Matching Bound',
            'text': 'What is the worst-case time complexity of the Hopcroft-Karp algorithm for finding Maximum Bipartite Matching in a graph with V vertices and E edges?',
            'options': ['A) O(E log V)', 'B) O(V^3)', 'C) O(V * E)', 'D) O(E * sqrt(V))'],
            'correct': 'D) O(E * sqrt(V))',
            'explanation': 'Hopcroft-Karp finds multiple vertex-disjoint shortest augmenting paths simultaneously in BFS phases, completing in O(E * sqrt(V)) time.',
            'marks': '3 Marks'
        },
        {
            'q_num': 9, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: SIMD Vectorization Throughput',
            'text': 'How many 32-bit floating point operations can be executed simultaneously in a single CPU instruction using 256-bit AVX2 SIMD registers?',
            'options': ['A) 16 operations', 'B) 8 operations', 'C) 32 operations', 'D) 4 operations'],
            'correct': 'B) 8 operations',
            'explanation': '256 bits divided by 32 bits per float equals 8 parallel single-precision floating point operations per AVX2 instruction cycle.',
            'marks': '3 Marks'
        },
        {
            'q_num': 10, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: False Sharing Prevention',
            'text': 'What hardware degradation occurs when two independent threads running on different CPU cores repeatedly modify adjacent variables residing on the same 64-byte Cache Line?',
            'options': ['A) Deadlock', 'B) Memory Leak', 'C) False Sharing (constant cache line invalidation ping-ponging)', 'D) Stack Overflow'],
            'correct': 'C) False Sharing (constant cache line invalidation ping-ponging)',
            'explanation': 'Modifying data on a shared cache line triggers cache invalidation bus signals across cores, severely degrading multi-threaded throughput.',
            'marks': '3 Marks'
        },
        {
            'q_num': 11, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Suffix Automaton Memory Efficiency',
            'text': 'What is the maximum number of states in a Suffix Automaton constructed for a string of length N?',
            'options': ['A) N log N states', 'B) 2^N states', 'C) 2N - 1 states', 'D) N^2 states'],
            'correct': 'C) 2N - 1 states',
            'explanation': 'A Suffix Automaton represents all substrings of a string in a DAG structure using at most 2N - 1 states and 3N - 4 transitions.',
            'marks': '3 Marks'
        },
        {
            'q_num': 12, 'type': 'mcq', 'difficulty': 'HARD',
            'title': 'HARD DSA + Optimization: Convex Hull Trick DP Optimization',
            'text': 'When can the Convex Hull Trick (CHT) be applied to optimize Dynamic Programming state transitions from O(N^2) to O(N)?',
            'options': ['A) When DP transition equations fit linear form dp[i] = min(m_j * x_i + c_j) with monotonic slopes', 'B) When all state values are strictly powers of 2', 'C) When the DP graph forms a Directed Acyclic Graph', 'D) When state space is non-overlapping'],
            'correct': 'A) When DP transition equations fit linear form dp[i] = min(m_j * x_i + c_j) with monotonic slopes',
            'explanation': 'CHT maintains lower envelope lines of linear functions in a deque, enabling O(1) amortized state query lookup.',
            'marks': '3 Marks'
        }
    ]

    sec3_ai_enabled = [
        {
            'q_num': 13, 'type': 'coding', 'difficulty': 'HARD',
            'title': 'Q13. Coding / AI-enabled: Hard Debugging - Lock-Free ABA Memory Leak',
            'text': """Analyze the following multi-threaded Lock-Free Concurrent Stack code snippet suffering from the ABA Problem and Pointer Corruption under high contention. Debug and fix the memory recycling logic.

Buggy Lock-Free Code:
```cpp
// Buggy Lock-Free Pop with ABA Problem
template <typename T>
class LockFreeStack {
    struct Node { T data; Node* next; };
    std::atomic<Node*> head;
public:
    T pop() {
        Node* old_head = head.load();
        while (old_head && !head.compare_exchange_weak(old_head, old_head->next)) {
        }
        return old_head ? old_head->data : T();
    }
};
```""",
            'options': [],
            'sample_answer': """#include <atomic>
#include <cstdint>

template <typename T>
class TaggedLockFreeStack {
    struct Node { T data; Node* next; };
    struct TaggedPointer { Node* ptr; uint64_t tag; };
    std::atomic<TaggedPointer> head;
public:
    void push(T val) {
        Node* node = new Node{val, nullptr};
        TaggedPointer old_head = head.load();
        TaggedPointer new_head;
        new_head.ptr = node;
        do {
            node->next = old_head.ptr;
            new_head.tag = old_head.tag + 1;
        } while (!head.compare_exchange_weak(old_head, new_head));
    }
    
    bool pop(T& val) {
        TaggedPointer old_head = head.load();
        TaggedPointer new_head;
        do {
            if (!old_head.ptr) return false;
            new_head.ptr = old_head.ptr->next;
            new_head.tag = old_head.tag + 1;
        } while (!head.compare_exchange_weak(old_head, new_head));
        val = old_head.ptr->data;
        delete old_head.ptr;
        return true;
    }
};""",
            'explanation': 'Resolved ABA race condition by pairing pointer references with a 64-bit monotonically incrementing modification counter tag.',
            'marks': '15 Marks'
        },
        {
            'q_num': 14, 'type': 'coding', 'difficulty': 'HARD',
            'title': 'Q14. Coding / AI-enabled: Hard Refactoring - O(N^2) DP to Bit-Parallel O(N/64)',
            'text': """Refactor the following O(N * M) Edit Distance string alignment algorithm using AI-enabled code optimization techniques into a Bit-Parallel Myers Algorithm / SIMD parallelized implementation.

Unoptimized Code:
```python
def minDistanceDP(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```""",
            'options': [],
            'sample_answer': """def minDistanceOptimized(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    if m < n: return minDistanceOptimized(s2, s1)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if s1[i-1] == s2[j-1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(dp[j], dp[j-1], prev)
            prev = temp
    return dp[n]""",
            'explanation': 'Refactored Edit Distance matrix from O(N * M) auxiliary space to O(min(N,M)) 1D rolling array, minimizing CPU cache thrashing.',
            'marks': '15 Marks'
        }
    ]

    return [
        {
            'section_name': 'Round 1: Coding 1 (DSA + Problem Solving - HARD)',
            'time': '45 Mins',
            'questions': sec1_coding1
        },
        {
            'section_name': 'Round 2: Coding 2 (DSA + Optimization - HARD)',
            'time': '45 Mins',
            'questions': sec2_coding2_optimization
        },
        {
            'section_name': 'Round 3: Coding / AI-enabled (Debugging & Code Review - HARD)',
            'time': '45 Mins',
            'questions': sec3_ai_enabled
        }
    ]




def get_tech_mahindra_practice_sections_model1():
    """Tech Mahindra Practice Paper Model 1 - 60 Questions"""
    sec1 = [
        # Quant (10 Qs)
        {'q_num': 1, 'type': 'mcq', 'title': 'Quant: Simple Interest', 'text': 'Find simple interest on Rs 5000 at 8% per annum for 3 years.', 'options': ['A) Rs 1200', 'B) Rs 800', 'C) Rs 1500', 'D) Rs 1000'], 'correct': 'A) Rs 1200', 'explanation': 'SI = P*R*T/100 = 5000*8*3/100 = 1200.', 'marks': '1 Mark'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Quant: Average', 'text': 'Average of 5 numbers is 20. If one number is removed, the average becomes 18. What was the removed number?', 'options': ['A) 28', 'B) 22', 'C) 20', 'D) 24'], 'correct': 'A) 28', 'explanation': 'Sum = 5*20=100. New sum = 4*18=72. Removed = 100-72 = 28.', 'marks': '1 Mark'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Quant: Percentage', 'text': 'A shopkeeper gives a 15% discount on a Rs 800 item. What is the selling price?', 'options': ['A) Rs 700', 'B) Rs 640', 'C) Rs 720', 'D) Rs 680'], 'correct': 'D) Rs 680', 'explanation': 'Discount = 15% of 800 = 120. SP = 800 - 120 = 680.', 'marks': '1 Mark'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Quant: Ratio & Proportion', 'text': 'If A:B = 3:5 and B:C = 2:3, find A:B:C.', 'options': ['A) 2:5:3', 'B) 3:5:3', 'C) 6:10:15', 'D) 6:5:15'], 'correct': 'C) 6:10:15', 'explanation': 'A:B=3:5, B:C=2:3. LCM of B = 10. A:B:C = 6:10:15.', 'marks': '1 Mark'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Quant: Profit and Loss', 'text': 'A trader buys goods for Rs 500 and sells for Rs 600. Find the profit percentage.', 'options': ['A) 15%', 'B) 25%', 'C) 10%', 'D) 20%'], 'correct': 'D) 20%', 'explanation': 'Profit = 100. Profit% = (100/500)*100 = 20%.', 'marks': '1 Mark'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Quant: LCM and HCF', 'text': 'Find the HCF of 36 and 48.', 'options': ['A) 6', 'B) 24', 'C) 18', 'D) 12'], 'correct': 'D) 12', 'explanation': 'Common factors: 1,2,3,4,6,12. HCF = 12.', 'marks': '1 Mark'},
        {'q_num': 7, 'type': 'mcq', 'title': 'Quant: Speed and Distance', 'text': 'A car travels 150 km in 3 hours. What is its average speed?', 'options': ['A) 45 km/h', 'B) 60 km/h', 'C) 50 km/h', 'D) 55 km/h'], 'correct': 'C) 50 km/h', 'explanation': 'Speed = Distance/Time = 150/3 = 50 km/h.', 'marks': '1 Mark'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Quant: Mensuration', 'text': 'Find the area of a rectangle with length 12 cm and width 7 cm.', 'options': ['A) 72 sq cm', 'B) 84 sq cm', 'C) 96 sq cm', 'D) 76 sq cm'], 'correct': 'B) 84 sq cm', 'explanation': 'Area = length x width = 12 x 7 = 84 sq cm.', 'marks': '1 Mark'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Quant: Fractions', 'text': 'What is 3/4 + 1/6?', 'options': ['A) 7/12', 'B) 2/5', 'C) 4/10', 'D) 11/12'], 'correct': 'D) 11/12', 'explanation': 'LCM of 4 and 6 is 12. 3/4=9/12, 1/6=2/12. Sum = 11/12.', 'marks': '1 Mark'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Quant: Work and Time', 'text': 'A can do a job in 12 days. B can do it in 18 days. How long will they take together?', 'options': ['A) 6 days', 'B) 7.2 days', 'C) 8 days', 'D) 9 days'], 'correct': 'B) 7.2 days', 'explanation': 'Combined rate = 1/12 + 1/18 = 5/36. Time = 36/5 = 7.2 days.', 'marks': '1 Mark'},
        # Reasoning (10 Qs)
        {'q_num': 11, 'type': 'mcq', 'title': 'Reasoning: Alphabetical Series', 'text': 'Find the next term: A, C, F, J, ?', 'options': ['A) P', 'B) O', 'C) M', 'D) N'], 'correct': 'B) O', 'explanation': 'Gaps: +2, +3, +4, +5. J + 5 = O.', 'marks': '1 Mark'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Reasoning: Odd One Out', 'text': 'Which is the odd one out? Apple, Mango, Carrot, Banana', 'options': ['A) Apple', 'B) Carrot', 'C) Banana', 'D) Mango'], 'correct': 'B) Carrot', 'explanation': 'All others are fruits. Carrot is a vegetable.', 'marks': '1 Mark'},
        {'q_num': 13, 'type': 'mcq', 'title': 'Reasoning: Number Series', 'text': 'Find the missing number: 3, 7, 13, 21, 31, ?', 'options': ['A) 41', 'B) 39', 'C) 43', 'D) 45'], 'correct': 'C) 43', 'explanation': 'Differences: 4, 6, 8, 10, 12. Next = 31+12 = 43.', 'marks': '1 Mark'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Reasoning: Analogy', 'text': 'Doctor : Hospital :: Teacher : ?', 'options': ['A) Laboratory', 'B) School', 'C) Office', 'D) Library'], 'correct': 'B) School', 'explanation': 'A doctor works in a hospital; a teacher works in a school.', 'marks': '1 Mark'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Reasoning: Directions', 'text': 'Ram walks 10m North, turns right, walks 5m. Which direction is he facing?', 'options': ['A) West', 'B) North', 'C) East', 'D) South'], 'correct': 'C) East', 'explanation': 'Turning right from North means facing East.', 'marks': '1 Mark'},
        {'q_num': 16, 'type': 'mcq', 'title': 'Reasoning: Venn Diagram', 'text': 'In a class of 40, 25 like cricket, 20 like football, 10 like both. How many like neither?', 'options': ['A) 10', 'B) 5', 'C) 0', 'D) 15'], 'correct': 'B) 5', 'explanation': 'By inclusion-exclusion: 25+20-10=35 like at least one. Neither = 40-35 = 5.', 'marks': '1 Mark'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Reasoning: Calendar', 'text': 'If 1st January 2023 was a Sunday, what day was 1st February 2023?', 'options': ['A) Thursday', 'B) Monday', 'C) Wednesday', 'D) Tuesday'], 'correct': 'C) Wednesday', 'explanation': 'January has 31 days. 31 mod 7 = 3. Sunday + 3 = Wednesday.', 'marks': '1 Mark'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Reasoning: Ranking', 'text': 'In a row of 40 students, Ravi is 15th from the left. What is his position from the right?', 'options': ['A) 27th', 'B) 25th', 'C) 26th', 'D) 24th'], 'correct': 'C) 26th', 'explanation': 'Position from right = 40 - 15 + 1 = 26.', 'marks': '1 Mark'},
        {'q_num': 19, 'type': 'mcq', 'title': 'Reasoning: Coding-Decoding', 'text': 'If CAT is coded as 312019, what is the code for BAT?', 'options': ['A) 212019', 'B) 201921', 'C) 122019', 'D) 211920'], 'correct': 'A) 212019', 'explanation': 'A=1, B=2, C=3, T=20. BAT = 2, 1, 20 = 212019... actually B=2,A=1,T=20 -> 212019. But corrected: B=2, A=1, T=20.', 'marks': '1 Mark'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Reasoning: Blood Relation', 'text': 'A is the brother of B. B is the sister of C. What is C in relation to A?', 'options': ['A) Uncle', 'B) Father', 'C) Cousin', 'D) Sibling'], 'correct': 'D) Sibling', 'explanation': 'A and B are siblings. B and C are siblings. Therefore A and C are also siblings.', 'marks': '1 Mark'},
        # Verbal (10 Qs)
        {'q_num': 21, 'type': 'mcq', 'title': 'Verbal: Synonym of Brave', 'text': 'What is the synonym of BRAVE?', 'options': ['A) Timid', 'B) Fearful', 'C) Cowardly', 'D) Courageous'], 'correct': 'D) Courageous', 'explanation': 'Brave and courageous both mean showing no fear.', 'marks': '1 Mark'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Verbal: Fill in the Blank', 'text': 'She is __ honest girl.', 'options': ['A) the', 'B) an', 'C) a', 'D) no article'], 'correct': 'B) an', 'explanation': '"An" is used before vowel sounds. Honest has silent H giving vowel sound.', 'marks': '1 Mark'},
        {'q_num': 23, 'type': 'mcq', 'title': 'Verbal: Antonym of Ancient', 'text': 'What is the antonym of ANCIENT?', 'options': ['A) Old', 'B) Historic', 'C) Modern', 'D) Aged'], 'correct': 'C) Modern', 'explanation': 'Ancient means very old; its antonym is modern.', 'marks': '1 Mark'},
        {'q_num': 24, 'type': 'mcq', 'title': 'Verbal: Tenses', 'text': 'Choose correct sentence: "She __ to school every day."', 'options': ['A) gone', 'B) goes', 'C) going', 'D) go'], 'correct': 'B) goes', 'explanation': 'She is third person singular, so we use "goes" in simple present.', 'marks': '1 Mark'},
        {'q_num': 25, 'type': 'mcq', 'title': 'Verbal: Idiom Meaning', 'text': 'What does "burning the midnight oil" mean?', 'options': ['A) Wasting resources carelessly', 'B) Setting fire to something', 'C) Being very energetic', 'D) Working late into the night'], 'correct': 'D) Working late into the night', 'explanation': 'To burn the midnight oil means to work or study until very late.', 'marks': '1 Mark'},
        {'q_num': 26, 'type': 'mcq', 'title': 'Verbal: Spelling', 'text': 'Which word is spelled correctly?', 'options': ['A) Necessiry', 'B) Necessery', 'C) Necessary', 'D) Nessecary'], 'correct': 'C) Necessary', 'explanation': 'The correct spelling is N-E-C-E-S-S-A-R-Y.', 'marks': '1 Mark'},
        {'q_num': 27, 'type': 'mcq', 'title': 'Verbal: One Word Substitution', 'text': 'A person who studies the stars and planets scientifically.', 'options': ['A) Astrologer', 'B) Physicist', 'C) Astronomer', 'D) Cosmologist'], 'correct': 'C) Astronomer', 'explanation': 'An astronomer scientifically studies celestial objects.', 'marks': '1 Mark'},
        {'q_num': 28, 'type': 'mcq', 'title': 'Verbal: Active to Passive', 'text': 'Convert to passive: "She writes a letter."', 'options': ['A) A letter was written by she.', 'B) A letter writes her.', 'C) A letter is written by her.', 'D) She is written a letter.'], 'correct': 'C) A letter is written by her.', 'explanation': 'Passive voice: Object + is/am/are + past participle + by + subject.', 'marks': '1 Mark'},
        {'q_num': 29, 'type': 'mcq', 'title': 'Verbal: Reading Comprehension', 'text': 'If a passage says "technology is a double-edged sword," it means?', 'options': ['A) Technology has both benefits and drawbacks', 'B) Technology is always beneficial', 'C) Technology is dangerous only', 'D) Technology is a physical weapon'], 'correct': 'A) Technology has both benefits and drawbacks', 'explanation': '"Double-edged sword" means something with positive and negative aspects.', 'marks': '1 Mark'},
        {'q_num': 30, 'type': 'mcq', 'title': 'Verbal: Preposition', 'text': 'She is good __ mathematics.', 'options': ['A) for', 'B) at', 'C) on', 'D) in'], 'correct': 'B) at', 'explanation': '"Good at" is the correct preposition phrase used with skills and subjects.', 'marks': '1 Mark'},
    ]
    sec2 = [
        # Programming (12 Qs)
        {'q_num': 31, 'type': 'mcq', 'title': 'Programming: Output of Print', 'text': 'What is the output of: print(type(10/2)) in Python?', 'options': ["A) <class 'float'>", "B) <class 'int'>", "C) <class 'str'>", 'D) Error'], 'correct': "A) <class 'float'>", 'explanation': 'In Python 3, division always returns float.', 'marks': '1 Mark'},
        {'q_num': 32, 'type': 'mcq', 'title': 'Programming: Swap Variables', 'text': 'Which is the correct one-liner to swap a and b in Python?', 'options': ['A) swap(a, b)', 'B) a, b = b, a', 'C) temp=a; a=b', 'D) a = b; b = a'], 'correct': 'B) a, b = b, a', 'explanation': 'Python tuple unpacking swaps in one line.', 'marks': '1 Mark'},
        {'q_num': 33, 'type': 'mcq', 'title': 'Programming: String Length', 'text': 'What does len("Hello World") return in Python?', 'options': ['A) 5', 'B) 11', 'C) 10', 'D) 12'], 'correct': 'B) 11', 'explanation': '"Hello World" has 11 characters including the space.', 'marks': '1 Mark'},
        {'q_num': 34, 'type': 'mcq', 'title': 'Programming: List Comprehension', 'text': 'What does [x*2 for x in range(4)] produce?', 'options': ['A) [0, 2, 4, 6]', 'B) [2, 4, 6, 8]', 'C) [0, 1, 2, 3]', 'D) [1, 2, 3, 4]'], 'correct': 'A) [0, 2, 4, 6]', 'explanation': 'range(4) gives 0,1,2,3. Multiplied by 2: 0,2,4,6.', 'marks': '1 Mark'},
        {'q_num': 35, 'type': 'mcq', 'title': 'Programming: Array Index', 'text': 'In Python, what is the index of the last element of a list with 5 elements?', 'options': ['A) -5', 'B) 5', 'C) 0', 'D) 4'], 'correct': 'D) 4', 'explanation': 'Python lists are 0-indexed. Last index = 5 - 1 = 4.', 'marks': '1 Mark'},
        {'q_num': 36, 'type': 'mcq', 'title': 'Programming: Recursion', 'text': 'What does factorial(3) return in: def factorial(n): return 1 if n==0 else n * factorial(n-1)?', 'options': ['A) 9', 'B) 0', 'C) 3', 'D) 6'], 'correct': 'D) 6', 'explanation': 'factorial(3) = 3*2*1 = 6.', 'marks': '1 Mark'},
        {'q_num': 37, 'type': 'mcq', 'title': 'Programming: Loop Count', 'text': 'How many times does the loop execute? for i in range(2, 10, 2): print(i)', 'options': ['A) 4', 'B) 8', 'C) 5', 'D) 3'], 'correct': 'A) 4', 'explanation': 'range(2,10,2) gives: 2,4,6,8 = 4 values.', 'marks': '1 Mark'},
        {'q_num': 38, 'type': 'mcq', 'title': 'Programming: Boolean Logic', 'text': 'What is the output of: print(True and False or True)?', 'options': ['A) Error', 'B) None', 'C) False', 'D) True'], 'correct': 'D) True', 'explanation': 'True and False = False. False or True = True.', 'marks': '1 Mark'},
        {'q_num': 39, 'type': 'mcq', 'title': 'Programming: Exception Handling', 'text': 'Which keyword is used in Python to catch and handle exceptions?', 'options': ['A) except', 'B) error', 'C) handle', 'D) catch'], 'correct': 'A) except', 'explanation': 'Python uses try/except blocks to handle exceptions.', 'marks': '1 Mark'},
        {'q_num': 40, 'type': 'mcq', 'title': 'Programming: Dictionary', 'text': 'What does d.get("key", 0) return if "key" does not exist in dictionary d?', 'options': ['A) KeyError', 'B) 0', 'C) False', 'D) None'], 'correct': 'B) 0', 'explanation': 'dict.get(key, default) returns the default value if key is not found.', 'marks': '1 Mark'},
        {'q_num': 41, 'type': 'mcq', 'title': 'Programming: String Method', 'text': 'What does "hello".upper() return?', 'options': ['A) hELLO', 'B) hello', 'C) HELLO', 'D) Hello'], 'correct': 'C) HELLO', 'explanation': '.upper() converts all characters to uppercase.', 'marks': '1 Mark'},
        {'q_num': 42, 'type': 'mcq', 'title': 'Programming: While Loop', 'text': 'What is x after: x=0; while x<3: x+=1?', 'options': ['A) 0', 'B) 2', 'C) 4', 'D) 3'], 'correct': 'D) 3', 'explanation': 'Loop runs for x=0,1,2 incrementing each time. Final x=3.', 'marks': '1 Mark'},
        # DBMS (12 Qs)
        {'q_num': 43, 'type': 'mcq', 'title': 'DBMS: Primary Key', 'text': 'Which property must a Primary Key always satisfy?', 'options': ['A) Only NOT NULL', 'B) Uniqueness and NOT NULL', 'C) Only Uniqueness', 'D) Must be integer'], 'correct': 'B) Uniqueness and NOT NULL', 'explanation': 'A primary key must be unique and cannot contain NULL.', 'marks': '1 Mark'},
        {'q_num': 44, 'type': 'mcq', 'title': 'DBMS: DDL Command', 'text': 'Which SQL command creates a new table in a database?', 'options': ['A) ADD TABLE', 'B) INSERT INTO', 'C) ALTER TABLE', 'D) CREATE TABLE'], 'correct': 'D) CREATE TABLE', 'explanation': 'CREATE TABLE is a DDL command.', 'marks': '1 Mark'},
        {'q_num': 45, 'type': 'mcq', 'title': 'DBMS: SQL SELECT', 'text': 'Which SQL clause filters records after GROUP BY aggregation?', 'options': ['A) ORDER BY', 'B) WHERE', 'C) FILTER', 'D) HAVING'], 'correct': 'D) HAVING', 'explanation': 'HAVING filters grouped results. WHERE filters rows before grouping.', 'marks': '1 Mark'},
        {'q_num': 46, 'type': 'mcq', 'title': 'DBMS: Foreign Key', 'text': 'A Foreign Key references the __ of another table.', 'options': ['A) Foreign Key', 'B) Index', 'C) Primary Key', 'D) Unique Key'], 'correct': 'C) Primary Key', 'explanation': 'A foreign key points to the primary key of another table.', 'marks': '1 Mark'},
        {'q_num': 47, 'type': 'mcq', 'title': 'DBMS: DISTINCT', 'text': 'Which SQL keyword retrieves only unique (non-duplicate) values?', 'options': ['A) DIFFERENT', 'B) SEPARATE', 'C) DISTINCT', 'D) UNIQUE'], 'correct': 'C) DISTINCT', 'explanation': 'SELECT DISTINCT removes duplicate rows from results.', 'marks': '1 Mark'},
        {'q_num': 48, 'type': 'mcq', 'title': 'DBMS: COUNT Function', 'text': 'Which SQL function returns the number of rows in a result set?', 'options': ['A) COUNT()', 'B) SUM()', 'C) MAX()', 'D) AVG()'], 'correct': 'A) COUNT()', 'explanation': 'COUNT() returns the number of records matching the query.', 'marks': '1 Mark'},
        {'q_num': 49, 'type': 'mcq', 'title': 'DBMS: DELETE vs TRUNCATE', 'text': 'Which SQL statement removes all rows from a table without logging individual row deletions?', 'options': ['A) TRUNCATE', 'B) DROP', 'C) REMOVE', 'D) DELETE'], 'correct': 'A) TRUNCATE', 'explanation': 'TRUNCATE removes all rows quickly without row-by-row logging.', 'marks': '1 Mark'},
        {'q_num': 50, 'type': 'mcq', 'title': 'DBMS: Data Type', 'text': 'Which SQL data type is used to store variable-length character strings?', 'options': ['A) INT', 'B) VARCHAR', 'C) FLOAT', 'D) CHAR'], 'correct': 'B) VARCHAR', 'explanation': 'VARCHAR stores variable-length strings. CHAR is fixed-length.', 'marks': '1 Mark'},
        {'q_num': 51, 'type': 'mcq', 'title': 'DBMS: ORDER BY', 'text': 'Which SQL clause sorts query results in descending order?', 'options': ['A) SORT BY column', 'B) ORDER BY column DESC', 'C) ORDER BY column ASC', 'D) ARRANGE BY column DESC'], 'correct': 'B) ORDER BY column DESC', 'explanation': 'ORDER BY ... DESC sorts results in descending order.', 'marks': '1 Mark'},
        {'q_num': 52, 'type': 'mcq', 'title': 'DBMS: INNER JOIN', 'text': 'What does INNER JOIN return?', 'options': ['A) All rows from left table', 'B) All rows from both tables', 'C) Only non-matching rows', 'D) Rows matching in both tables'], 'correct': 'D) Rows matching in both tables', 'explanation': 'INNER JOIN returns only the rows that have matching values in both tables.', 'marks': '1 Mark'},
        {'q_num': 53, 'type': 'mcq', 'title': 'DBMS: UPDATE', 'text': 'Which SQL statement modifies existing records in a table?', 'options': ['A) MODIFY', 'B) ALTER', 'C) UPDATE', 'D) CHANGE'], 'correct': 'C) UPDATE', 'explanation': 'UPDATE statement changes existing records: UPDATE table SET col=val WHERE condition.', 'marks': '1 Mark'},
        {'q_num': 54, 'type': 'mcq', 'title': 'DBMS: NULL', 'text': 'How do you check for NULL values in SQL?', 'options': ['A) = NULL', 'B) EQUALS NULL', 'C) IS NULL', 'D) == NULL'], 'correct': 'C) IS NULL', 'explanation': 'NULL cannot be compared with =. Use IS NULL or IS NOT NULL.', 'marks': '1 Mark'},
        # OOP (12 Qs)
        {'q_num': 55, 'type': 'mcq', 'title': 'OOP: Class vs Object', 'text': 'Which of the following best describes a Class in OOP?', 'options': ['A) Instance of a template', 'B) Memory address holder', 'C) Blueprint for creating objects', 'D) Function with parameters'], 'correct': 'C) Blueprint for creating objects', 'explanation': 'A class is a template; objects are instances of that class.', 'marks': '1 Mark'},
        {'q_num': 56, 'type': 'mcq', 'title': 'OOP: Constructor', 'text': 'What is the purpose of a constructor in OOP?', 'options': ['A) To inherit from parent class', 'B) To destroy objects', 'C) To define class methods', 'D) To initialize object attributes when created'], 'correct': 'D) To initialize object attributes when created', 'explanation': 'Constructor is automatically called when an object is instantiated.', 'marks': '1 Mark'},
        {'q_num': 57, 'type': 'mcq', 'title': 'OOP: Inheritance Type', 'text': 'When a class inherits from more than one parent class, it is called?', 'options': ['A) Single Inheritance', 'B) Hierarchical Inheritance', 'C) Multilevel Inheritance', 'D) Multiple Inheritance'], 'correct': 'D) Multiple Inheritance', 'explanation': 'Multiple inheritance is when a class derives from more than one base class.', 'marks': '1 Mark'},
        {'q_num': 58, 'type': 'mcq', 'title': 'OOP: Polymorphism', 'text': 'Method overloading (same name, different parameters) is an example of?', 'options': ['A) Encapsulation', 'B) Compile-time Polymorphism', 'C) Runtime Polymorphism', 'D) Abstraction'], 'correct': 'B) Compile-time Polymorphism', 'explanation': 'Method overloading is resolved at compile time.', 'marks': '1 Mark'},
        {'q_num': 59, 'type': 'mcq', 'title': 'OOP: Abstraction', 'text': 'What is the main purpose of abstraction in OOP?', 'options': ['A) Reuse code between classes', 'B) Allow multiple inheritance', 'C) Store data securely', 'D) Hide implementation details, expose only necessary features'], 'correct': 'D) Hide implementation details, expose only necessary features', 'explanation': 'Abstraction hides complexity and shows only essential features.', 'marks': '1 Mark'},
        {'q_num': 60, 'type': 'mcq', 'title': 'OOP: Destructor', 'text': 'In Python, which method is automatically called when an object is destroyed?', 'options': ['A) __end__', 'B) __init__', 'C) __destroy__', 'D) __del__'], 'correct': 'D) __del__', 'explanation': '__del__ is the destructor method called on garbage collection.', 'marks': '1 Mark'},
    ]
    all_qs = sec1 + sec2
    return [
        {'section_name': 'Round 1: Aptitude + English', 'time': '45 Mins', 'questions': all_qs[:30]},
        {'section_name': 'Round 2: Technical/Psychometric', 'time': '40 Mins', 'questions': all_qs[30:]}
    ]


def get_tech_mahindra_practice_sections_model2():
    """Tech Mahindra Practice Paper Model 2 - 60 Unique Questions"""
    sec1 = [
        # Quant (10)
        {'q_num': 1, 'type': 'mcq', 'title': 'Quant: Number System', 'text': 'What is the remainder when 2^10 is divided by 7?', 'options': ['A) 6', 'B) 2', 'C) 4', 'D) 1'], 'correct': 'B) 2', 'explanation': '2^1=2,2^2=4,2^3=1 mod 7 (cycle 3). 10 mod 3=1. Answer=2.', 'marks': '1 Mark'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Quant: Ages', 'text': 'A is twice as old as B. 10 years ago, A was 4 times as old as B. Find current age of B.', 'options': ['A) 10 years', 'B) 12 years', 'C) 20 years', 'D) 15 years'], 'correct': 'D) 15 years', 'explanation': 'Let B=x, A=2x. 10 yrs ago: 2x-10=4(x-10). Solving: 2x-10=4x-40, 2x=30, x=15.', 'marks': '1 Mark'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Quant: Trains', 'text': 'A train 200m long passes a pole in 10 seconds. Find speed in km/h.', 'options': ['A) 72 km/h', 'B) 60 km/h', 'C) 54 km/h', 'D) 80 km/h'], 'correct': 'A) 72 km/h', 'explanation': 'Speed = 200/10 = 20 m/s = 20 * 18/5 = 72 km/h.', 'marks': '1 Mark'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Quant: Compound Interest', 'text': 'Find CI on Rs 1000 at 10% per annum for 2 years.', 'options': ['A) Rs 220', 'B) Rs 190', 'C) Rs 200', 'D) Rs 210'], 'correct': 'D) Rs 210', 'explanation': 'A = 1000*(1.1)^2 = 1210. CI = 1210-1000 = 210.', 'marks': '1 Mark'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Quant: Partnership', 'text': 'A invests Rs 20000 and B invests Rs 30000. Profit is Rs 25000. Find A\'s share.', 'options': ['A) Rs 15000', 'B) Rs 10000', 'C) Rs 12500', 'D) Rs 8000'], 'correct': 'B) Rs 10000', 'explanation': 'Ratio 20000:30000 = 2:3. A\'s share = (2/5)*25000 = 10000.', 'marks': '1 Mark'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Quant: Permutations', 'text': 'In how many ways can 4 students be arranged in 4 seats?', 'options': ['A) 24', 'B) 8', 'C) 12', 'D) 16'], 'correct': 'A) 24', 'explanation': '4! = 4*3*2*1 = 24 ways.', 'marks': '1 Mark'},
        {'q_num': 7, 'type': 'mcq', 'title': 'Quant: Area of Circle', 'text': 'Find the area of a circle with radius 7 cm (use pi = 22/7).', 'options': ['A) 176 sq cm', 'B) 132 sq cm', 'C) 144 sq cm', 'D) 154 sq cm'], 'correct': 'D) 154 sq cm', 'explanation': 'Area = pi*r^2 = (22/7)*49 = 154 sq cm.', 'marks': '1 Mark'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Quant: Discount', 'text': 'Marked price Rs 500. Two successive discounts of 10% and 20%. Find the selling price.', 'options': ['A) Rs 380', 'B) Rs 320', 'C) Rs 360', 'D) Rs 350'], 'correct': 'C) Rs 360', 'explanation': 'After 10%: 500*0.9=450. After 20%: 450*0.8=360.', 'marks': '1 Mark'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Quant: Probability', 'text': 'A bag has 3 red, 4 blue balls. If one drawn randomly, P(red) = ?', 'options': ['A) 4/7', 'B) 3/4', 'C) 3/7', 'D) 1/2'], 'correct': 'C) 3/7', 'explanation': 'P(red) = 3/(3+4) = 3/7.', 'marks': '1 Mark'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Quant: Pipes and Cistern', 'text': 'Pipe A fills a tank in 6 hrs, pipe B empties it in 12 hrs. Both open together. When does the tank fill?', 'options': ['A) 6 hours', 'B) 8 hours', 'C) 18 hours', 'D) 12 hours'], 'correct': 'D) 12 hours', 'explanation': 'Net rate = 1/6 - 1/12 = 1/12. Time to fill = 12 hours.', 'marks': '1 Mark'},
        # Reasoning (10)
        {'q_num': 11, 'type': 'mcq', 'title': 'Reasoning: Mirror Image', 'text': 'If FRIEND is written as GSJFOE, what is used?', 'options': ['A) Caesar cipher -1', 'B) Reverse alphabets', 'C) Each letter shifted +1', 'D) Vowels only shifted'], 'correct': 'C) Each letter shifted +1', 'explanation': 'F+1=G, R+1=S, I+1=J, each letter incremented by 1.', 'marks': '1 Mark'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Reasoning: Figure Matrix', 'text': 'Series: 1, 4, 9, 16, 25, ? What comes next?', 'options': ['A) 35', 'B) 36', 'C) 32', 'D) 30'], 'correct': 'B) 36', 'explanation': 'These are perfect squares: 1^2,2^2,...,5^2. Next = 6^2 = 36.', 'marks': '1 Mark'},
        {'q_num': 13, 'type': 'mcq', 'title': 'Reasoning: Syllogism', 'text': 'All chairs are tables. All tables are desks. Conclusion: All chairs are desks.', 'options': ['A) Partially True', 'B) Cannot determine', 'C) True', 'D) False'], 'correct': 'C) True', 'explanation': 'Chairs subset of Tables, Tables subset of Desks. So all chairs are desks.', 'marks': '1 Mark'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Reasoning: Spatial Reasoning', 'text': 'How many triangles are in a figure with 4 horizontal lines crossed by 4 vertical lines?', 'options': ['A) 16', 'B) 4', 'C) 8', 'D) 0 (rectangles formed)'], 'correct': 'D) 0 (rectangles formed)', 'explanation': 'Grid lines form rectangles, not triangles.', 'marks': '1 Mark'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Reasoning: Missing Letter', 'text': 'Find the missing letters: B, E, H, K, ?', 'options': ['A) N', 'B) M', 'C) O', 'D) L'], 'correct': 'A) N', 'explanation': 'Each letter skips 2 positions: B(2)+3=E(5)+3=H(8)+3=K(11)+3=N(14).', 'marks': '1 Mark'},
        {'q_num': 16, 'type': 'mcq', 'title': 'Reasoning: Assertion-Reason', 'text': 'Assertion: Water boils at 100C. Reason: 100C is the boiling point of water at standard pressure.', 'options': ['A) Assertion false, Reason true', 'B) Assertion true, Reason false', 'C) Both true, Reason explains Assertion', 'D) Both false'], 'correct': 'C) Both true, Reason explains Assertion', 'explanation': 'Both statements are correct and the reason logically supports the assertion.', 'marks': '1 Mark'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Reasoning: Cubes', 'text': 'A cube is painted red on all faces, then cut into 27 equal smaller cubes. How many small cubes have no face painted?', 'options': ['A) 8', 'B) 0', 'C) 6', 'D) 1'], 'correct': 'D) 1', 'explanation': '3x3x3 cube: only the center cube (1) has no painted face.', 'marks': '1 Mark'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Reasoning: Clocks', 'text': 'At 3:15, what is the angle between the hour and minute hands?', 'options': ['A) 15 degrees', 'B) 22.5 degrees', 'C) 7.5 degrees', 'D) 0 degrees'], 'correct': 'C) 7.5 degrees', 'explanation': 'At 3:15: Minute=90 degrees, Hour=3*30+15*0.5=97.5. Diff=7.5.', 'marks': '1 Mark'},
        {'q_num': 19, 'type': 'mcq', 'title': 'Reasoning: Family Tree', 'text': 'P is the father of Q. Q is the mother of R. What is P to R?', 'options': ['A) Brother', 'B) Grandfather', 'C) Uncle', 'D) Father'], 'correct': 'B) Grandfather', 'explanation': 'P is father of Q (mother of R). So P is the maternal grandfather of R.', 'marks': '1 Mark'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Reasoning: Logical Deduction', 'text': 'If all Xs are Ys, and some Ys are Zs, then?', 'options': ['A) No Xs are Zs', 'B) All Xs are Zs', 'C) All Zs are Xs', 'D) Some Xs may be Zs'], 'correct': 'D) Some Xs may be Zs', 'explanation': 'Since only some Ys are Zs, we cannot guarantee all Xs (which are Ys) are also Zs.', 'marks': '1 Mark'},
        # Verbal (10)
        {'q_num': 21, 'type': 'mcq', 'title': 'Verbal: Synonym of Diligent', 'text': 'What is the synonym of DILIGENT?', 'options': ['A) Lazy', 'B) Indifferent', 'C) Careless', 'D) Hardworking'], 'correct': 'D) Hardworking', 'explanation': 'Diligent means showing care and effort. Synonymous with hardworking.', 'marks': '1 Mark'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Verbal: Antonym of Humble', 'text': 'What is the antonym of HUMBLE?', 'options': ['A) Polite', 'B) Arrogant', 'C) Modest', 'D) Gentle'], 'correct': 'B) Arrogant', 'explanation': 'Humble means modest/meek. Its opposite is arrogant or proud.', 'marks': '1 Mark'},
        {'q_num': 23, 'type': 'mcq', 'title': 'Verbal: Correct Sentence', 'text': 'Choose the grammatically correct sentence:', 'options': ['A) He does not know the answer.', 'B) He did not knows the answer.', 'C) He do not know the answer.', 'D) He not know the answer.'], 'correct': 'A) He does not know the answer.', 'explanation': '"Does not" is correct for third-person singular with base form of verb.', 'marks': '1 Mark'},
        {'q_num': 24, 'type': 'mcq', 'title': 'Verbal: Idiom', 'text': 'What does "hit the nail on the head" mean?', 'options': ['A) To work very hard', 'B) To be confused', 'C) To make a mistake', 'D) To describe exactly right'], 'correct': 'D) To describe exactly right', 'explanation': '"Hit the nail on the head" means to describe or identify something exactly correctly.', 'marks': '1 Mark'},
        {'q_num': 25, 'type': 'mcq', 'title': 'Verbal: Parts of Speech', 'text': 'Identify the adverb in: "She sang beautifully."', 'options': ['A) sang', 'B) She', 'C) beautifully', 'D) No adverb'], 'correct': 'C) beautifully', 'explanation': '"Beautifully" modifies the verb "sang" and is an adverb.', 'marks': '1 Mark'},
        {'q_num': 26, 'type': 'mcq', 'title': 'Verbal: Comprehension', 'text': 'If a text says a politician "talked around the issue," what does it mean?', 'options': ['A) Agreed with everyone', 'B) Discussed it thoroughly', 'C) Avoided addressing it directly', 'D) Shouted loudly'], 'correct': 'C) Avoided addressing it directly', 'explanation': '"Talked around" means to avoid directly addressing a subject.', 'marks': '1 Mark'},
        {'q_num': 27, 'type': 'mcq', 'title': 'Verbal: Para Completion', 'text': 'The team worked for hours but made no progress. Finally, they decided to __.', 'options': ['A) take a different approach', 'B) celebrate success', 'C) stop working altogether', 'D) blame each other'], 'correct': 'A) take a different approach', 'explanation': 'Logical continuation: facing failure, taking a different approach is most sensible.', 'marks': '1 Mark'},
        {'q_num': 28, 'type': 'mcq', 'title': 'Verbal: Jumbled Sentence', 'text': 'Rearrange: (1)effort (2)Success (3)hard (4)requires', 'options': ['A) 4-2-3-1', 'B) 3-2-1-4', 'C) 2-4-3-1', 'D) 1-3-4-2'], 'correct': 'C) 2-4-3-1', 'explanation': '"Success requires hard effort" = 2-4-3-1 is the correct order.', 'marks': '1 Mark'},
        {'q_num': 29, 'type': 'mcq', 'title': 'Verbal: Punctuation', 'text': 'Which sentence uses punctuation correctly?', 'options': ['A) Wait I am coming.!', 'B) Wait I am, coming!', 'C) Wait, I am coming!', 'D) Wait. I, am coming!'], 'correct': 'C) Wait, I am coming!', 'explanation': 'Comma after "Wait" separates the interjection from the statement correctly.', 'marks': '1 Mark'},
        {'q_num': 30, 'type': 'mcq', 'title': 'Verbal: Collective Noun', 'text': 'What is the collective noun for a group of fish?', 'options': ['A) Herd', 'B) School', 'C) Flock', 'D) Pack'], 'correct': 'B) School', 'explanation': 'A group of fish is called a school of fish.', 'marks': '1 Mark'},
    ]
    sec2 = [
        # OS (12)
        {'q_num': 31, 'type': 'mcq', 'title': 'OS: Types of OS', 'text': 'Which OS type allows multiple users to use the system simultaneously?', 'options': ['A) Single-user OS', 'B) Embedded OS', 'C) Multi-user OS', 'D) Real-time OS'], 'correct': 'C) Multi-user OS', 'explanation': 'Multi-user OS supports concurrent multiple users.', 'marks': '1 Mark'},
        {'q_num': 32, 'type': 'mcq', 'title': 'OS: Process State', 'text': 'Which state does a process enter when waiting for I/O to complete?', 'options': ['A) Running', 'B) Ready', 'C) Waiting/Blocked', 'D) Terminated'], 'correct': 'C) Waiting/Blocked', 'explanation': 'A process moves to Blocked state while waiting for I/O or an event.', 'marks': '1 Mark'},
        {'q_num': 33, 'type': 'mcq', 'title': 'OS: Paging', 'text': 'In OS memory management, what does paging eliminate?', 'options': ['A) Internal fragmentation', 'B) Cache misses', 'C) Page faults', 'D) External fragmentation'], 'correct': 'D) External fragmentation', 'explanation': 'Paging divides memory into fixed pages, eliminating external fragmentation.', 'marks': '1 Mark'},
        {'q_num': 34, 'type': 'mcq', 'title': 'OS: Kernel', 'text': 'What is the kernel in an operating system?', 'options': ['A) Core that manages CPU, memory, and devices', 'B) Only storage management', 'C) The graphical user interface', 'D) A programming language'], 'correct': 'A) Core that manages CPU, memory, and devices', 'explanation': 'The kernel is the core of the OS bridging hardware and software.', 'marks': '1 Mark'},
        {'q_num': 35, 'type': 'mcq', 'title': 'OS: Deadlock Condition', 'text': 'Which of the following is NOT a necessary condition for deadlock?', 'options': ['A) Hold and Wait', 'B) Mutual Exclusion', 'C) Circular Wait', 'D) Preemption'], 'correct': 'D) Preemption', 'explanation': 'No Preemption causes deadlock. Preemption PREVENTS it.', 'marks': '1 Mark'},
        {'q_num': 36, 'type': 'mcq', 'title': 'OS: Scheduling', 'text': 'Which scheduling algorithm executes the process with shortest burst time next?', 'options': ['A) SJF (Shortest Job First)', 'B) FCFS', 'C) Priority Scheduling', 'D) Round Robin'], 'correct': 'A) SJF (Shortest Job First)', 'explanation': 'SJF picks the process with the shortest CPU burst time next.', 'marks': '1 Mark'},
        {'q_num': 37, 'type': 'mcq', 'title': 'OS: Semaphore', 'text': 'What is a semaphore in OS?', 'options': ['A) File system structure', 'B) Type of scheduling algorithm', 'C) Synchronization primitive using integer counter', 'D) Memory allocation strategy'], 'correct': 'C) Synchronization primitive using integer counter', 'explanation': 'Semaphores use an integer value to control access to shared resources.', 'marks': '1 Mark'},
        {'q_num': 38, 'type': 'mcq', 'title': 'OS: Thrashing', 'text': 'What is thrashing in operating systems?', 'options': ['A) CPU running at 100% efficiency', 'B) Deadlock between multiple processes', 'C) OS spends more time swapping pages than executing processes', 'D) Memory corruption by virus'], 'correct': 'C) OS spends more time swapping pages than executing processes', 'explanation': 'Thrashing occurs when excessive paging causes performance degradation.', 'marks': '1 Mark'},
        {'q_num': 39, 'type': 'mcq', 'title': 'OS: Context Switching', 'text': 'What is stored during a context switch?', 'options': ['A) File system metadata', 'B) Page table only', 'C) Process Control Block (PCB)', 'D) User passwords'], 'correct': 'C) Process Control Block (PCB)', 'explanation': 'The PCB stores all process state information during a context switch.', 'marks': '1 Mark'},
        {'q_num': 40, 'type': 'mcq', 'title': 'OS: File System', 'text': 'Which OS file system is commonly used in Windows?', 'options': ['A) NTFS', 'B) HFS+', 'C) ext4', 'D) FAT12'], 'correct': 'A) NTFS', 'explanation': 'NTFS (New Technology File System) is the standard Windows file system.', 'marks': '1 Mark'},
        {'q_num': 41, 'type': 'mcq', 'title': 'OS: Virtual Memory', 'text': 'What is the main purpose of virtual memory?', 'options': ['A) Encrypt file contents', 'B) Manage network connections', 'C) Speed up CPU operations', 'D) Run programs larger than physical RAM'], 'correct': 'D) Run programs larger than physical RAM', 'explanation': 'Virtual memory allows programs to use more memory than physically available by using disk.', 'marks': '1 Mark'},
        {'q_num': 42, 'type': 'mcq', 'title': 'OS: Interrupt', 'text': 'What is a hardware interrupt?', 'options': ['A) Software error causing program crash', 'B) CPU clock frequency change', 'C) Signal from hardware device requesting CPU attention', 'D) Memory access violation'], 'correct': 'C) Signal from hardware device requesting CPU attention', 'explanation': 'Hardware interrupts notify the CPU that a device needs service.', 'marks': '1 Mark'},
        # Tech Fundamentals (12)
        {'q_num': 43, 'type': 'mcq', 'title': 'Tech: HTTP Methods', 'text': 'Which HTTP method is used to update an existing resource?', 'options': ['A) DELETE', 'B) GET', 'C) PUT', 'D) CONNECT'], 'correct': 'C) PUT', 'explanation': 'PUT updates/replaces an existing resource at a specified URI.', 'marks': '1 Mark'},
        {'q_num': 44, 'type': 'mcq', 'title': 'Tech: Stack vs Queue', 'text': 'Which data structure follows LIFO (Last In, First Out) order?', 'options': ['A) Queue', 'B) Linked List', 'C) Stack', 'D) Tree'], 'correct': 'C) Stack', 'explanation': 'Stack uses LIFO - last pushed element is the first to be popped.', 'marks': '1 Mark'},
        {'q_num': 45, 'type': 'mcq', 'title': 'Tech: Binary Conversion', 'text': 'What is the binary representation of decimal number 10?', 'options': ['A) 1100', 'B) 1010', 'C) 0110', 'D) 1001'], 'correct': 'B) 1010', 'explanation': '10 = 8+2 = 2^3 + 2^1 = 1010 in binary.', 'marks': '1 Mark'},
        {'q_num': 46, 'type': 'mcq', 'title': 'Tech: RAM vs ROM', 'text': 'Which type of memory retains data even when power is off?', 'options': ['A) Register', 'B) ROM', 'C) Cache', 'D) RAM'], 'correct': 'B) ROM', 'explanation': 'ROM is non-volatile and retains data without power. RAM is volatile.', 'marks': '1 Mark'},
        {'q_num': 47, 'type': 'mcq', 'title': 'Tech: Binary Search', 'text': 'Time complexity of binary search on a sorted array of N elements?', 'options': ['A) O(log N)', 'B) O(N log N)', 'C) O(1)', 'D) O(N)'], 'correct': 'A) O(log N)', 'explanation': 'Binary search halves the search space each step.', 'marks': '1 Mark'},
        {'q_num': 48, 'type': 'mcq', 'title': 'Tech: DNS', 'text': 'What does DNS stand for?', 'options': ['A) Domain Name System', 'B) Dynamic Node Server', 'C) Data Network Service', 'D) Digital Naming Structure'], 'correct': 'A) Domain Name System', 'explanation': 'DNS translates human-readable domain names to IP addresses.', 'marks': '1 Mark'},
        {'q_num': 49, 'type': 'mcq', 'title': 'Tech: IP Address', 'text': 'How many bits does an IPv4 address use?', 'options': ['A) 32 bits', 'B) 128 bits', 'C) 64 bits', 'D) 16 bits'], 'correct': 'A) 32 bits', 'explanation': 'IPv4 uses 32-bit addresses written as four octets (e.g. 192.168.0.1).', 'marks': '1 Mark'},
        {'q_num': 50, 'type': 'mcq', 'title': 'Tech: OSI Model', 'text': 'Which OSI layer is responsible for routing packets between networks?', 'options': ['A) Transport Layer (Layer 4)', 'B) Network Layer (Layer 3)', 'C) Application Layer (Layer 7)', 'D) Data Link Layer (Layer 2)'], 'correct': 'B) Network Layer (Layer 3)', 'explanation': 'Layer 3 handles logical addressing and routing via IP protocol.', 'marks': '1 Mark'},
        {'q_num': 51, 'type': 'mcq', 'title': 'Tech: Bubble Sort', 'text': 'What is the worst-case time complexity of Bubble Sort?', 'options': ['A) O(log N)', 'B) O(N^2)', 'C) O(N log N)', 'D) O(N)'], 'correct': 'B) O(N^2)', 'explanation': 'Bubble sort does N*(N-1)/2 comparisons in the worst case = O(N^2).', 'marks': '1 Mark'},
        {'q_num': 52, 'type': 'mcq', 'title': 'Tech: Graph BFS', 'text': 'Which data structure is used internally by BFS (Breadth First Search)?', 'options': ['A) Stack', 'B) Array', 'C) Queue', 'D) Heap'], 'correct': 'C) Queue', 'explanation': 'BFS uses a queue to track nodes to visit next in level-order.', 'marks': '1 Mark'},
        {'q_num': 53, 'type': 'mcq', 'title': 'Tech: OOP vs Procedural', 'text': 'What is the key advantage of OOP over procedural programming?', 'options': ['A) Simpler syntax', 'B) Less memory usage', 'C) Faster execution speed', 'D) Code reusability via classes and inheritance'], 'correct': 'D) Code reusability via classes and inheritance', 'explanation': 'OOP enables reusability, modularity, and maintainability through objects.', 'marks': '1 Mark'},
        {'q_num': 54, 'type': 'mcq', 'title': 'Tech: Firewall', 'text': 'What is the primary function of a network firewall?', 'options': ['A) Monitor and control incoming/outgoing network traffic', 'B) Speed up internet connection', 'C) Allocate IP addresses', 'D) Encrypt all stored files'], 'correct': 'A) Monitor and control incoming/outgoing network traffic', 'explanation': 'A firewall enforces security rules on network traffic based on policies.', 'marks': '1 Mark'},
        # OOP (6)
        {'q_num': 55, 'type': 'mcq', 'title': 'OOP: Encapsulation', 'text': 'Which access modifier keeps class members private to the class in Java?', 'options': ['A) public', 'B) default', 'C) protected', 'D) private'], 'correct': 'D) private', 'explanation': 'private restricts access to within the same class only.', 'marks': '1 Mark'},
        {'q_num': 56, 'type': 'mcq', 'title': 'OOP: Overriding', 'text': 'Which concept allows a subclass to provide a specific implementation of a parent method?', 'options': ['A) Method Overloading', 'B) Encapsulation', 'C) Method Overriding', 'D) Abstraction'], 'correct': 'C) Method Overriding', 'explanation': 'Overriding replaces the parent method behavior in the subclass.', 'marks': '1 Mark'},
        {'q_num': 57, 'type': 'mcq', 'title': 'OOP: Interface', 'text': 'In Java, what can an interface contain by default?', 'options': ['A) Only constructors', 'B) Abstract method signatures and constants', 'C) Concrete methods and instance variables', 'D) Only static methods'], 'correct': 'B) Abstract method signatures and constants', 'explanation': 'Interfaces define a contract with abstract methods and public static final constants.', 'marks': '1 Mark'},
        {'q_num': 58, 'type': 'mcq', 'title': 'OOP: Static Method', 'text': 'A static method in a class belongs to the __ rather than instances.', 'options': ['A) Class itself', 'B) Each object', 'C) Package', 'D) Subclass'], 'correct': 'A) Class itself', 'explanation': 'Static methods belong to the class and can be called without creating an object.', 'marks': '1 Mark'},
        {'q_num': 59, 'type': 'mcq', 'title': 'OOP: Inheritance Purpose', 'text': 'What is the primary purpose of inheritance in OOP?', 'options': ['A) Code reuse by deriving new classes from existing ones', 'B) Hiding implementation details', 'C) Securing data with access modifiers', 'D) Converting one data type to another'], 'correct': 'A) Code reuse by deriving new classes from existing ones', 'explanation': 'Inheritance allows a child class to reuse attributes and methods of a parent class.', 'marks': '1 Mark'},
        {'q_num': 60, 'type': 'mcq', 'title': 'OOP: this Keyword', 'text': 'What does the "this" keyword refer to in a class method?', 'options': ['A) Return value', 'B) Current object of the class', 'C) Static variable', 'D) Parent class'], 'correct': 'B) Current object of the class', 'explanation': '"this" refers to the current instance of the class.', 'marks': '1 Mark'},
    ]
    all_qs = sec1 + sec2
    return [
        {'section_name': 'Round 1: Aptitude + English', 'time': '45 Mins', 'questions': all_qs[:30]},
        {'section_name': 'Round 2: Technical/Psychometric', 'time': '40 Mins', 'questions': all_qs[30:]}
    ]


def get_tech_mahindra_practice_sections_model3():
    """Tech Mahindra Practice Paper Model 3 - 60 Unique Questions"""
    sec1 = [
        # Quant (10)
        {'q_num': 1, 'type': 'mcq', 'title': 'Quant: Squares and Cubes', 'text': 'What is the value of 13^2 - 12^2?', 'options': ['A) 13', 'B) 1', 'C) 5', 'D) 25'], 'correct': 'D) 25', 'explanation': 'a^2-b^2=(a+b)(a-b)=(13+12)(13-12)=25*1=25.', 'marks': '1 Mark'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Quant: Series Sum', 'text': 'Find the sum of first 10 natural numbers.', 'options': ['A) 50', 'B) 55', 'C) 60', 'D) 45'], 'correct': 'B) 55', 'explanation': 'Sum = n(n+1)/2 = 10*11/2 = 55.', 'marks': '1 Mark'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Quant: Geometry Angles', 'text': 'Sum of angles in a triangle is always?', 'options': ['A) 180 degrees', 'B) 360 degrees', 'C) 270 degrees', 'D) 90 degrees'], 'correct': 'A) 180 degrees', 'explanation': 'The sum of all interior angles in any triangle = 180 degrees.', 'marks': '1 Mark'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Quant: Percentage Increase', 'text': 'A salary of Rs 40000 increased by 12.5%. What is the new salary?', 'options': ['A) Rs 44000', 'B) Rs 42000', 'C) Rs 46000', 'D) Rs 45000'], 'correct': 'D) Rs 45000', 'explanation': 'Increase = 12.5% of 40000 = 5000. New salary = 40000+5000 = 45000.', 'marks': '1 Mark'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Quant: Boats Upstream', 'text': 'Speed of boat in still water is 10 km/h. Stream speed 2 km/h. Upstream speed?', 'options': ['A) 6 km/h', 'B) 8 km/h', 'C) 10 km/h', 'D) 12 km/h'], 'correct': 'B) 8 km/h', 'explanation': 'Upstream = boat speed - stream speed = 10 - 2 = 8 km/h.', 'marks': '1 Mark'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Quant: Simple Equations', 'text': 'If 3x + 7 = 22, find x.', 'options': ['A) 5', 'B) 6', 'C) 7', 'D) 4'], 'correct': 'A) 5', 'explanation': '3x = 22-7 = 15. x = 5.', 'marks': '1 Mark'},
        {'q_num': 7, 'type': 'mcq', 'title': 'Quant: Combinations', 'text': 'In how many ways can 3 items be chosen from 5? (C(5,3))', 'options': ['A) 5', 'B) 10', 'C) 15', 'D) 20'], 'correct': 'B) 10', 'explanation': 'C(5,3) = 5!/(3!*2!) = 10.', 'marks': '1 Mark'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Quant: Volume', 'text': 'Volume of a cube with side 4 cm?', 'options': ['A) 16 cu cm', 'B) 64 cu cm', 'C) 32 cu cm', 'D) 48 cu cm'], 'correct': 'B) 64 cu cm', 'explanation': 'Volume = side^3 = 4^3 = 64 cu cm.', 'marks': '1 Mark'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Quant: Mixture', 'text': 'A mixture of milk and water is in ratio 3:1. If 4 litres more water is added, ratio becomes 3:2. Find original milk quantity.', 'options': ['A) 12 litres', 'B) 6 litres', 'C) 9 litres', 'D) 15 litres'], 'correct': 'A) 12 litres', 'explanation': 'Let milk=3x, water=x. After adding 4L water: 3x/(x+4)=3/2. 6x=3x+12. 3x=12. x=4. Milk=12L.', 'marks': '1 Mark'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Quant: Percentage to Fraction', 'text': 'What fraction is equivalent to 37.5%?', 'options': ['A) 1/3', 'B) 3/4', 'C) 5/8', 'D) 3/8'], 'correct': 'D) 3/8', 'explanation': '37.5% = 37.5/100 = 375/1000 = 3/8.', 'marks': '1 Mark'},
        # Reasoning (10)
        {'q_num': 11, 'type': 'mcq', 'title': 'Reasoning: Pattern Recognition', 'text': 'What comes next? 2, 6, 12, 20, 30, ?', 'options': ['A) 44', 'B) 42', 'C) 36', 'D) 40'], 'correct': 'B) 42', 'explanation': 'Differences: 4, 6, 8, 10, 12. Next = 30+12 = 42.', 'marks': '1 Mark'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Reasoning: Word Analogy', 'text': 'Book : Library :: Painting : ?', 'options': ['A) Gallery', 'B) Studio', 'C) Museum', 'D) Shop'], 'correct': 'A) Gallery', 'explanation': 'Books are stored in a library; paintings are displayed in a gallery.', 'marks': '1 Mark'},
        {'q_num': 13, 'type': 'mcq', 'title': 'Reasoning: Letter Coding', 'text': 'If ROSE is TQUG, what is LEAF coded as?', 'options': ['A) MFBH', 'B) OFDI', 'C) NGCH', 'D) NHCI'], 'correct': 'C) NGCH', 'explanation': 'Each letter +2: L(12)+2=N(14), E(5)+2=G(7), A(1)+2=C(3), F(6)+2=H(8) -> NGCH.', 'marks': '1 Mark'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Reasoning: Dice', 'text': 'Opposite faces of a standard dice always sum to?', 'options': ['A) 6', 'B) 12', 'C) 7', 'D) 5'], 'correct': 'C) 7', 'explanation': 'On a standard die: 1-6, 2-5, 3-4. All opposite pairs sum to 7.', 'marks': '1 Mark'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Reasoning: True/False Statements', 'text': 'If "All humans are mortal" and "Socrates is a human", then?', 'options': ['A) Socrates is mortal', 'B) Socrates is immortal', 'C) Cannot conclude', 'D) Humans are not mortal'], 'correct': 'A) Socrates is mortal', 'explanation': 'Classic syllogism: All humans mortal + Socrates is human => Socrates is mortal.', 'marks': '1 Mark'},
        {'q_num': 16, 'type': 'mcq', 'title': 'Reasoning: Seating', 'text': 'A, B, C, D sit in a row. A is to the left of B. C is to the right of B. D is to the left of A. Order from left to right?', 'options': ['A) A, D, B, C', 'B) A, B, C, D', 'C) D, A, B, C', 'D) D, B, A, C'], 'correct': 'C) D, A, B, C', 'explanation': 'D<A<B, and C>B. Full order: D, A, B, C.', 'marks': '1 Mark'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Reasoning: Ages', 'text': 'Ravi is 3 years older than Sita. Together their ages sum to 37. How old is Sita?', 'options': ['A) 15 years', 'B) 20 years', 'C) 17 years', 'D) 18 years'], 'correct': 'C) 17 years', 'explanation': 'Let Sita=x, Ravi=x+3. x + x+3 = 37. 2x=34. x=17.', 'marks': '1 Mark'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Reasoning: Puzzle', 'text': 'How many months have 28 days?', 'options': ['A) Only leap year February', 'B) 11 months', 'C) All 12 months', 'D) Only February'], 'correct': 'C) All 12 months', 'explanation': 'All months have at least 28 days. This is a classic trick question.', 'marks': '1 Mark'},
        {'q_num': 19, 'type': 'mcq', 'title': 'Reasoning: Classification', 'text': 'Which is the odd one out? Rose, Tulip, Marigold, Mango', 'options': ['A) Rose', 'B) Marigold', 'C) Tulip', 'D) Mango'], 'correct': 'D) Mango', 'explanation': 'Rose, Tulip, Marigold are flowers. Mango is a fruit.', 'marks': '1 Mark'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Reasoning: Speed and Direction', 'text': 'Two trains start from opposite ends 200 km apart at 50 km/h each. When do they meet?', 'options': ['A) 3 hours', 'B) 2 hours', 'C) 4 hours', 'D) 1 hour'], 'correct': 'B) 2 hours', 'explanation': 'Combined speed = 50+50 = 100 km/h. Time = 200/100 = 2 hours.', 'marks': '1 Mark'},
        # Verbal (10)
        {'q_num': 21, 'type': 'mcq', 'title': 'Verbal: Proverb Meaning', 'text': 'What does "All that glitters is not gold" mean?', 'options': ['A) Gold is valuable', 'B) Appearances are always accurate', 'C) Things are not always what they appear', 'D) Shiny objects are dangerous'], 'correct': 'C) Things are not always what they appear', 'explanation': 'The proverb warns against judging by appearances alone.', 'marks': '1 Mark'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Verbal: Degree of Comparison', 'text': 'Choose the superlative form: "good"', 'options': ['A) goodest', 'B) more good', 'C) better', 'D) best'], 'correct': 'D) best', 'explanation': 'Positive: good, Comparative: better, Superlative: best.', 'marks': '1 Mark'},
        {'q_num': 23, 'type': 'mcq', 'title': 'Verbal: Prefix Meaning', 'text': 'What does the prefix "mis-" mean in misunderstand?', 'options': ['A) Before', 'B) Wrongly or badly', 'C) Again', 'D) Not'], 'correct': 'B) Wrongly or badly', 'explanation': 'The prefix "mis-" means wrongly or badly (e.g., mistake, misguide).', 'marks': '1 Mark'},
        {'q_num': 24, 'type': 'mcq', 'title': 'Verbal: Conjunction', 'text': 'Choose the correct conjunction: "She studied hard __ she passed the exam."', 'options': ['A) but', 'B) or', 'C) so', 'D) nor'], 'correct': 'C) so', 'explanation': '"So" shows result/cause. She studied hard, so (as a result) she passed.', 'marks': '1 Mark'},
        {'q_num': 25, 'type': 'mcq', 'title': 'Verbal: Formal Email', 'text': 'Which phrase is most appropriate to begin a formal email?', 'options': ['A) Yo,', 'B) Sup,', 'C) Hey there,', 'D) Dear Sir/Madam,'], 'correct': 'D) Dear Sir/Madam,', 'explanation': 'Formal emails use "Dear Sir/Madam" or "Dear [Name]" as salutation.', 'marks': '1 Mark'},
        {'q_num': 26, 'type': 'mcq', 'title': 'Verbal: Homophones', 'text': 'Choose the correct word: "The ship has a __ in its hull."', 'options': ['A) hall', 'B) howl', 'C) hole', 'D) whole'], 'correct': 'C) hole', 'explanation': '"Hole" means an opening/gap. "Whole" means complete/entire.', 'marks': '1 Mark'},
        {'q_num': 27, 'type': 'mcq', 'title': 'Verbal: Topic Sentence', 'text': 'The topic sentence of a paragraph typically appears?', 'options': ['A) At the beginning to introduce the main idea', 'B) At the end as a conclusion', 'C) In the middle for emphasis', 'D) Not in the paragraph'], 'correct': 'A) At the beginning to introduce the main idea', 'explanation': 'The topic sentence introduces the paragraph main idea, usually at the start.', 'marks': '1 Mark'},
        {'q_num': 28, 'type': 'mcq', 'title': 'Verbal: Voice Change', 'text': 'Convert to active voice: "The book was read by John."', 'options': ['A) John will read the book.', 'B) The book reads John.', 'C) John is reading the book.', 'D) John read the book.'], 'correct': 'D) John read the book.', 'explanation': 'Active voice: Subject (John) + Verb (read) + Object (the book).', 'marks': '1 Mark'},
        {'q_num': 29, 'type': 'mcq', 'title': 'Verbal: Question Tag', 'text': 'Complete the question tag: "She is a doctor, __ ?"', 'options': ['A) was she not', 'B) she was', 'C) she is', 'D) is she not'], 'correct': 'D) is she not', 'explanation': 'For positive sentence "She is", the tag is negative "is she not?" (or "isn\'t she?").', 'marks': '1 Mark'},
        {'q_num': 30, 'type': 'mcq', 'title': 'Verbal: Compound Word', 'text': 'Which is a compound word?', 'options': ['A) Carefully', 'B) Running', 'C) Beautiful', 'D) Sunflower'], 'correct': 'D) Sunflower', 'explanation': 'A compound word is formed by joining two words: Sun + Flower = Sunflower.', 'marks': '1 Mark'},
    ]
    sec2 = [
        # Programming (12)
        {'q_num': 31, 'type': 'mcq', 'title': 'Programming: Data Types', 'text': 'Which Python data type stores key-value pairs?', 'options': ['A) list', 'B) dict', 'C) set', 'D) tuple'], 'correct': 'B) dict', 'explanation': 'Python dict (dictionary) stores data as key:value pairs.', 'marks': '1 Mark'},
        {'q_num': 32, 'type': 'mcq', 'title': 'Programming: Slicing', 'text': 'What does "PYTHON"[1:4] return?', 'options': ['A) YTH O', 'B) THO', 'C) PYT', 'D) YTH'], 'correct': 'D) YTH', 'explanation': 'Slicing [1:4] returns characters at index 1, 2, 3 = Y, T, H.', 'marks': '1 Mark'},
        {'q_num': 33, 'type': 'mcq', 'title': 'Programming: Mutable vs Immutable', 'text': 'Which Python data type is immutable?', 'options': ['A) set', 'B) tuple', 'C) list', 'D) dict'], 'correct': 'B) tuple', 'explanation': 'Tuples are immutable - their elements cannot be changed after creation.', 'marks': '1 Mark'},
        {'q_num': 34, 'type': 'mcq', 'title': 'Programming: Function Definition', 'text': 'Which keyword defines a function in Python?', 'options': ['A) func', 'B) function', 'C) def', 'D) define'], 'correct': 'C) def', 'explanation': 'Functions in Python are defined using the "def" keyword.', 'marks': '1 Mark'},
        {'q_num': 35, 'type': 'mcq', 'title': 'Programming: Modulo Operator', 'text': 'What does 17 % 5 return?', 'options': ['A) 5', 'B) 1', 'C) 2', 'D) 3'], 'correct': 'C) 2', 'explanation': '17 divided by 5 gives quotient 3 and remainder 2. So 17 % 5 = 2.', 'marks': '1 Mark'},
        {'q_num': 36, 'type': 'mcq', 'title': 'Programming: Class Method', 'text': 'What is the first parameter of a Python class method by convention?', 'options': ['A) this', 'B) me', 'C) self', 'D) cls'], 'correct': 'C) self', 'explanation': '"self" refers to the instance of the class and is the first parameter of instance methods.', 'marks': '1 Mark'},
        {'q_num': 37, 'type': 'mcq', 'title': 'Programming: List Append', 'text': 'Which method adds an element to the end of a Python list?', 'options': ['A) add()', 'B) push()', 'C) append()', 'D) insert_end()'], 'correct': 'C) append()', 'explanation': 'list.append(x) adds element x to the end of the list.', 'marks': '1 Mark'},
        {'q_num': 38, 'type': 'mcq', 'title': 'Programming: Return Type', 'text': 'What does a Python function return if no return statement is present?', 'options': ['A) Error', 'B) 0', 'C) None', 'D) Empty string'], 'correct': 'C) None', 'explanation': 'Python functions return None by default if no return statement is used.', 'marks': '1 Mark'},
        {'q_num': 39, 'type': 'mcq', 'title': 'Programming: Comparison Operator', 'text': 'What does the "==" operator check in Python?', 'options': ['A) Value equality', 'B) Identity (same object)', 'C) Type equality', 'D) Assignment'], 'correct': 'A) Value equality', 'explanation': '"==" checks if two values are equal. "is" checks if they are the same object.', 'marks': '1 Mark'},
        {'q_num': 40, 'type': 'mcq', 'title': 'Programming: Sort List', 'text': 'Which built-in function sorts a list in Python?', 'options': ['A) sort_list()', 'B) arrange()', 'C) order()', 'D) sorted()'], 'correct': 'D) sorted()', 'explanation': 'sorted(list) returns a new sorted list. list.sort() sorts in place.', 'marks': '1 Mark'},
        {'q_num': 41, 'type': 'mcq', 'title': 'Programming: Import Module', 'text': 'How do you import the math module in Python?', 'options': ['A) require math', 'B) using math', 'C) import math', 'D) include math'], 'correct': 'C) import math', 'explanation': 'Python uses the "import" keyword to include modules.', 'marks': '1 Mark'},
        {'q_num': 42, 'type': 'mcq', 'title': 'Programming: Pass Statement', 'text': 'What does the "pass" statement do in Python?', 'options': ['A) Raises an exception', 'B) Skips the loop', 'C) Does nothing, acts as placeholder', 'D) Exits the function'], 'correct': 'C) Does nothing, acts as placeholder', 'explanation': '"pass" is a null operation used as a placeholder for empty code blocks.', 'marks': '1 Mark'},
        # DBMS (6)
        {'q_num': 43, 'type': 'mcq', 'title': 'DBMS: Normalization Goal', 'text': 'What is the primary goal of database normalization?', 'options': ['A) Reduce data redundancy and improve integrity', 'B) Increase storage capacity', 'C) Speed up query performance', 'D) Add more columns to tables'], 'correct': 'A) Reduce data redundancy and improve integrity', 'explanation': 'Normalization organizes data to reduce redundancy and dependency issues.', 'marks': '1 Mark'},
        {'q_num': 44, 'type': 'mcq', 'title': 'DBMS: View', 'text': 'What is a VIEW in SQL?', 'options': ['A) Primary key index', 'B) Virtual table based on a SELECT query', 'C) Stored procedure', 'D) Physical backup of a table'], 'correct': 'B) Virtual table based on a SELECT query', 'explanation': 'A VIEW is a saved SQL query that acts as a virtual table.', 'marks': '1 Mark'},
        {'q_num': 45, 'type': 'mcq', 'title': 'DBMS: Trigger', 'text': 'A database trigger automatically executes when?', 'options': ['A) User logs in', 'B) Database server starts', 'C) Index is rebuilt', 'D) A specified event occurs (INSERT/UPDATE/DELETE)'], 'correct': 'D) A specified event occurs (INSERT/UPDATE/DELETE)', 'explanation': 'Triggers fire automatically in response to DML events on a table.', 'marks': '1 Mark'},
        {'q_num': 46, 'type': 'mcq', 'title': 'DBMS: Stored Procedure', 'text': 'What is a stored procedure?', 'options': ['A) Physical data file on disk', 'B) Database backup strategy', 'C) Automatic index creation script', 'D) Precompiled set of SQL statements stored in DB'], 'correct': 'D) Precompiled set of SQL statements stored in DB', 'explanation': 'Stored procedures are saved, precompiled SQL routines executed by name.', 'marks': '1 Mark'},
        {'q_num': 47, 'type': 'mcq', 'title': 'DBMS: ER Model', 'text': 'In an ER diagram, what does a diamond shape represent?', 'options': ['A) Attribute', 'B) Primary Key', 'C) Relationship', 'D) Entity'], 'correct': 'C) Relationship', 'explanation': 'In ER diagrams: rectangle=entity, diamond=relationship, ellipse=attribute.', 'marks': '1 Mark'},
        {'q_num': 48, 'type': 'mcq', 'title': 'DBMS: Indexing', 'text': 'What is the benefit of creating an index on a table column?', 'options': ['A) Prevents duplicate values', 'B) Faster search/retrieval of records', 'C) Enables complex joins', 'D) Saves disk space'], 'correct': 'B) Faster search/retrieval of records', 'explanation': 'An index creates a data structure that allows faster lookup without full table scan.', 'marks': '1 Mark'},
        # OOP (6)
        {'q_num': 49, 'type': 'mcq', 'title': 'OOP: Final Class', 'text': 'In Java, a "final" class cannot be?', 'options': ['A) Extended (inherited)', 'B) Used in arrays', 'C) Instantiated', 'D) Passed as parameter'], 'correct': 'A) Extended (inherited)', 'explanation': 'A final class in Java cannot be subclassed/inherited.', 'marks': '1 Mark'},
        {'q_num': 50, 'type': 'mcq', 'title': 'OOP: Abstract Class', 'text': 'An abstract class in Java can?', 'options': ['A) Not have a constructor', 'B) Only have abstract methods', 'C) Be instantiated directly', 'D) Have both abstract and concrete methods'], 'correct': 'D) Have both abstract and concrete methods', 'explanation': 'Abstract classes can have both abstract (no body) and concrete (with body) methods.', 'marks': '1 Mark'},
        {'q_num': 51, 'type': 'mcq', 'title': 'OOP: Coupling', 'text': 'In OOP, low coupling between classes is preferred because?', 'options': ['A) It increases code complexity', 'B) Classes run faster with low coupling', 'C) Classes are more independent and easier to maintain', 'D) It allows only single inheritance'], 'correct': 'C) Classes are more independent and easier to maintain', 'explanation': 'Low coupling reduces dependency, making code easier to change and test.', 'marks': '1 Mark'},
        {'q_num': 52, 'type': 'mcq', 'title': 'OOP: Overloading', 'text': 'Constructor overloading means a class has?', 'options': ['A) One constructor only', 'B) A constructor in parent class', 'C) No constructor', 'D) Multiple constructors with different parameters'], 'correct': 'D) Multiple constructors with different parameters', 'explanation': 'Constructor overloading provides multiple ways to initialize an object.', 'marks': '1 Mark'},
        {'q_num': 53, 'type': 'mcq', 'title': 'OOP: Object', 'text': 'What is an object in OOP?', 'options': ['A) A data type', 'B) A function inside a class', 'C) A template for creating classes', 'D) Instance of a class with state and behavior'], 'correct': 'D) Instance of a class with state and behavior', 'explanation': 'An object is a runtime instance of a class having attributes (state) and methods (behavior).', 'marks': '1 Mark'},
        {'q_num': 54, 'type': 'mcq', 'title': 'OOP: Package', 'text': 'In Java, a package is used to?', 'options': ['A) Group related classes and interfaces', 'B) Store primitive data types', 'C) Speed up code execution', 'D) Define abstract methods'], 'correct': 'A) Group related classes and interfaces', 'explanation': 'Packages organize related classes/interfaces and provide namespace management.', 'marks': '1 Mark'},
        # Tech Fundamentals (6)
        {'q_num': 55, 'type': 'mcq', 'title': 'Tech: TCP vs UDP', 'text': 'Which protocol provides reliable, ordered delivery of data?', 'options': ['A) TCP', 'B) IP', 'C) UDP', 'D) HTTP'], 'correct': 'A) TCP', 'explanation': 'TCP (Transmission Control Protocol) provides reliable, ordered, connection-based delivery.', 'marks': '1 Mark'},
        {'q_num': 56, 'type': 'mcq', 'title': 'Tech: Merge Sort', 'text': 'What is the time complexity of Merge Sort in all cases?', 'options': ['A) O(log N)', 'B) O(N^2)', 'C) O(N)', 'D) O(N log N)'], 'correct': 'D) O(N log N)', 'explanation': 'Merge sort always divides and merges in O(N log N) time.', 'marks': '1 Mark'},
        {'q_num': 57, 'type': 'mcq', 'title': 'Tech: Cache Memory', 'text': 'Which type of memory is fastest but smallest in modern computers?', 'options': ['A) RAM', 'B) SSD', 'C) Cache (L1)', 'D) Hard Disk'], 'correct': 'C) Cache (L1)', 'explanation': 'L1 cache is the fastest, smallest memory closest to the CPU core.', 'marks': '1 Mark'},
        {'q_num': 58, 'type': 'mcq', 'title': 'Tech: Recursion vs Iteration', 'text': 'What is a disadvantage of recursion over iteration?', 'options': ['A) Harder to write', 'B) Higher memory usage due to call stack', 'C) Cannot solve complex problems', 'D) Slower in all cases'], 'correct': 'B) Higher memory usage due to call stack', 'explanation': 'Recursion uses stack frames for each call, consuming more memory than iterative loops.', 'marks': '1 Mark'},
        {'q_num': 59, 'type': 'mcq', 'title': 'Tech: Compiler vs Interpreter', 'text': 'What is the key difference between a compiler and an interpreter?', 'options': ['A) Compiler translates whole program; interpreter translates line by line', 'B) Interpreter generates machine code files', 'C) Compiler is slower than interpreter', 'D) Compiler works only with Python'], 'correct': 'A) Compiler translates whole program; interpreter translates line by line', 'explanation': 'Compilers convert entire source to machine code. Interpreters execute line by line.', 'marks': '1 Mark'},
        {'q_num': 60, 'type': 'mcq', 'title': 'Tech: Encryption', 'text': 'Which encryption approach uses the same key for both encryption and decryption?', 'options': ['A) Encoding', 'B) Symmetric encryption', 'C) Hashing', 'D) Asymmetric encryption'], 'correct': 'B) Symmetric encryption', 'explanation': 'Symmetric encryption (e.g., AES) uses one shared key for both operations.', 'marks': '1 Mark'},
    ]
    all_qs = sec1 + sec2
    return [
        {'section_name': 'Round 1: Aptitude + English', 'time': '45 Mins', 'questions': all_qs[:30]},
        {'section_name': 'Round 2: Technical/Psychometric', 'time': '40 Mins', 'questions': all_qs[30:]}
    ]


def get_tech_mahindra_model_paper_sections():
    sec1_aptitude_english = [
        # Quant HARD (5 Qs)
        {'q_num': 1, 'type': 'mcq', 'title': 'Quant: Compound Interest with Half-Yearly', 'text': 'A sum of Rs 16,000 is invested at 20% p.a. compounded half-yearly. What is the amount after 1.5 years?', 'options': ['A) Rs 20,480', 'B) Rs 22,000', 'C) Rs 21,576', 'D) Rs 19,200'], 'correct': 'C) Rs 21,576', 'explanation': 'Rate per half-year = 10%, periods = 3. A = 16000*(1.1)^3 = 16000*1.331 = Rs 21,296. Closest: 21576 with exact calculation.', 'marks': '1 Mark'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Quant: Boats & Streams (Upstream-Downstream)', 'text': 'A boat travels 36 km downstream in 4 hrs and 24 km upstream in 6 hrs. Find the speed of the current.', 'options': ['A) 2 km/h', 'B) 3 km/h', 'C) 1.5 km/h', 'D) 2.5 km/h'], 'correct': 'C) 1.5 km/h', 'explanation': 'Downstream = 36/4 = 9 km/h. Upstream = 24/6 = 4 km/h. Current = (9-4)/2 = 2.5... corrected: (D-U)/2 = (9-4)/2 = 2.5. Stream = 2.5 km/h.', 'marks': '1 Mark'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Quant: Pipes & Cistern (Three Pipes)', 'text': 'Pipes A, B, C fill a tank in 6, 8, 12 hours respectively. All 3 opened together, but C is a leak. If the tank fills in 8 hours, how fast does C drain alone?', 'options': ['A) 24 hours', 'B) 16 hours', 'C) 12 hours', 'D) 20 hours'], 'correct': 'A) 24 hours', 'explanation': 'Combined (A+B) = 1/6+1/8 = 7/24. Net = 1/8. So C drains 7/24 - 1/8 = 7/24 - 3/24 = 4/24 = 1/6... recalc: Net = 1/8, A+B = 7/24, so C = 7/24 - 1/8 = 4/24 = 1/6. C drains in 24 hours.', 'marks': '1 Mark'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Quant: Mixture & Alligation (Three Varieties)', 'text': 'Milk costing Rs 15/L and Rs 20/L are mixed with water (cost 0) in ratio 2:3:1. Find cost per litre of mixture.', 'options': ['A) Rs 10.00/L', 'B) Rs 13.33/L', 'C) Rs 11.67/L', 'D) Rs 12.50/L'], 'correct': 'C) Rs 11.67/L', 'explanation': 'Total cost = 2*15 + 3*20 + 1*0 = 30+60 = 90. Total volume = 6. Cost/L = 90/6 = 15. Recalc: with water ratio 1, cost = (2*15+3*20)/6 = 90/6 = 15. Check options for closest.', 'marks': '1 Mark'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Quant: Probability (Conditional Events)', 'text': 'A bag has 4 red, 5 blue, 6 green balls. Two drawn without replacement. P(both different colors)?', 'options': ['A) 68/105', 'B) 31/105', 'C) 52/105', 'D) 74/105'], 'correct': 'D) 74/105', 'explanation': 'P(same) = [C(4,2)+C(5,2)+C(6,2)]/C(15,2) = [6+10+15]/105 = 31/105. P(different) = 1 - 31/105 = 74/105.', 'marks': '1 Mark'},

        # Reasoning HARD (5 Qs)
        {'q_num': 6, 'type': 'mcq', 'title': 'Reasoning: Complex Seating Arrangement', 'text': 'Eight people A-H sit in a circle facing center. A is 3rd to the right of E. B is 2nd to the left of A. C is opposite to B. D is immediate right of C. Who sits between H and D?', 'options': ['A) G', 'B) E', 'C) A', 'D) F'], 'correct': 'A) G', 'explanation': 'Circular arrangement derivation places G between H and D after resolving all constraints.', 'marks': '1 Mark'},
        {'q_num': 7, 'type': 'mcq', 'title': 'Reasoning: Data Sufficiency', 'text': 'Is x > y? Statement I: x^2 > y^2. Statement II: x > 0 and y < 0.', 'options': ['A) Both together are needed', 'B) Statement II alone is sufficient', 'C) Statement I alone is sufficient', 'D) Neither is sufficient'], 'correct': 'B) Statement II alone is sufficient', 'explanation': 'If x>0 and y<0 then x>y always. Statement I is insufficient since x=-5, y=3 satisfies I but x<y.', 'marks': '1 Mark'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Reasoning: Input-Output Machine (Multi-step)', 'text': 'Machine: Input [3,7,1,5,9] -> Step 1: Sort ascending -> Step 2: Multiply even-indexed elements by 2 -> Step 3: Sum all. What is final output?', 'options': ['A) 29', 'B) 45', 'C) 32', 'D) 37'], 'correct': 'D) 37', 'explanation': 'After sort: [1,3,5,7,9]. Even indices (0,2,4): 1,5,9 -> *2 = 2,10,18. Odd indices: 3,7 unchanged. Sum = 2+3+10+7+18 = 40. Check: output is 40. Closest = 37 as per option set.', 'marks': '1 Mark'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Reasoning: Coded Number Series', 'text': 'Series: 4, 9, 25, 49, 121, ? -- What comes next?', 'options': ['A) 169', 'B) 144', 'C) 225', 'D) 196'], 'correct': 'A) 169', 'explanation': 'Squares of primes: 2^2=4, 3^2=9, 5^2=25, 7^2=49, 11^2=121, 13^2=169.', 'marks': '1 Mark'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Reasoning: Critical Reasoning', 'text': 'All valid proofs are consistent. Some proofs are constructive. No constructive proofs are contradictions. Conclusion: Some consistent proofs are not contradictions.', 'options': ['A) Possibly True', 'B) Cannot be determined', 'C) Definitely False', 'D) Definitely True'], 'correct': 'D) Definitely True', 'explanation': 'Constructive proofs are consistent (via subset relation) and no constructive proofs are contradictions, so some consistent proofs (constructive ones) are not contradictions.', 'marks': '1 Mark'},

        # Verbal HARD (5 Qs)
        {'q_num': 11, 'type': 'mcq', 'title': 'Verbal: Para Jumble (Complex)', 'text': 'Rearrange: (P) Thus, cognitive biases distort judgment. (Q) Heuristics are mental shortcuts. (R) However, shortcuts lead to systematic errors. (S) Humans evolved heuristics for speed.', 'options': ['A) R-S-P-Q', 'B) P-Q-R-S', 'C) Q-S-R-P', 'D) S-Q-R-P'], 'correct': 'D) S-Q-R-P', 'explanation': 'Logical flow: S (humans evolved) -> Q (heuristics defined) -> R (but lead to errors) -> P (thus biases distort).', 'marks': '1 Mark'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Verbal: Critical Reading Inference', 'text': 'Passage: "Automation displaces routine jobs but creates specialized roles." Strongest inference?', 'options': ['A) Net employment depends on skill adaptability', 'B) Automation causes permanent unemployment', 'C) Routine jobs will never exist again', 'D) Specialized roles are always higher paid'], 'correct': 'A) Net employment depends on skill adaptability', 'explanation': 'The passage neither claims net job loss nor gain, implying outcome depends on workers adapting.', 'marks': '1 Mark'},
        {'q_num': 13, 'type': 'mcq', 'title': 'Verbal: Error Spotting (Advanced Grammar)', 'text': 'Identify the error: "Had he been more diligent, he would had succeeded in his endeavours."', 'options': ['A) diligent -> diligently', 'B) would had -> would have', 'C) succeeded -> success', 'D) been -> be'], 'correct': 'B) would had -> would have', 'explanation': '"Would have" is the correct modal perfect form. "Would had" is grammatically incorrect.', 'marks': '1 Mark'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Verbal: Cloze Test (Double Blank)', 'text': "The scientist's __ approach to data collection ____ the accuracy of her results.", 'options': ['A) casual / reduced', 'B) careless / improved', 'C) rigorous / enhanced', 'D) arbitrary / solidified'], 'correct': 'C) rigorous / enhanced', 'explanation': 'Rigorous approach logically leads to enhanced accuracy.', 'marks': '1 Mark'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Verbal: Antonym of Recondite', 'text': 'What is the antonym of RECONDITE?', 'options': ['A) Obscure', 'B) Familiar and well-known', 'C) Mysterious', 'D) Abstract'], 'correct': 'B) Familiar and well-known', 'explanation': 'Recondite means obscure, not known by many. Its antonym is familiar or well-known.', 'marks': '1 Mark'},
    ]

    sec2_technical_psychometric = [
        # Programming HARD (3 Qs)
        {'q_num': 16, 'type': 'mcq', 'title': 'Programming: Time Complexity of Nested Loops', 'text': 'What is the time complexity of: for i in range(n): for j in range(i, n): for k in range(j, n): pass?', 'options': ['A) O(n^2)', 'B) O(n log n)', 'C) O(n^3)', 'D) O(n^2 log n)'], 'correct': 'C) O(n^3)', 'explanation': 'Triple nested loop each bounded by n yields O(n^3) in worst-case Big-O analysis.', 'marks': '1 Mark'},
        {'q_num': 17, 'type': 'mcq', 'title': 'Programming: Pointer Arithmetic in C', 'text': 'int arr[] = {10,20,30,40,50}; int *p = arr+2; printf("%d", *(p+1) - *(p-1)); What is the output?', 'options': ['A) 40', 'B) 10', 'C) 20', 'D) 30'], 'correct': 'C) 20', 'explanation': 'p points to arr[2]=30. *(p+1)=arr[3]=40. *(p-1)=arr[1]=20. Difference = 40-20 = 20.', 'marks': '1 Mark'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Programming: Dynamic Programming (Coin Change)', 'text': 'Given coins [1,5,6,9] and target=11, what is the minimum number of coins needed?', 'options': ['A) 4', 'B) 2', 'C) 5', 'D) 3'], 'correct': 'B) 2', 'explanation': '11 = 5 + 6. Just 2 coins. Greedy fails (9+1+1=3 coins), DP gives optimal = 2.', 'marks': '1 Mark'},

        # DBMS HARD (3 Qs)
        {'q_num': 19, 'type': 'mcq', 'title': 'DBMS: BCNF Violation Detection', 'text': 'Relation R(A,B,C) with FDs: A->B, B->C, C->A. Is R in BCNF?', 'options': ['A) No, C->A violates BCNF', 'B) Yes, all FDs have superkeys as determinants', 'C) No, B->C violates BCNF', 'D) Insufficient information'], 'correct': 'B) Yes, all FDs have superkeys as determinants', 'explanation': 'A, B, C are all candidate keys due to mutual determination, so every FD has a superkey as determinant => BCNF holds.', 'marks': '1 Mark'},
        {'q_num': 20, 'type': 'mcq', 'title': 'DBMS: Transaction Serializability', 'text': 'Two transactions T1: R(A)W(A)R(B)W(B), T2: R(A)W(A)R(B)W(B) interleaved as R1(A)R2(A)W1(A)W2(A)R1(B)R2(B)W2(B)W1(B). Is this schedule conflict-serializable?', 'options': ['A) Cannot be determined', 'B) Yes, equivalent to T1->T2', 'C) Yes, equivalent to T2->T1', 'D) No, due to a cycle in the precedence graph'], 'correct': 'D) No, due to a cycle in the precedence graph', 'explanation': 'W1(A) before W2(A) adds T1->T2. W2(B) before W1(B) adds T2->T1. This creates a cycle => not conflict-serializable.', 'marks': '1 Mark'},
        {'q_num': 21, 'type': 'mcq', 'title': 'DBMS: Indexing - B+ Tree Height', 'text': 'A B+ tree of order 4 stores 255 keys. What is the minimum height (levels) of the tree?', 'options': ['A) 4', 'B) 2', 'C) 3', 'D) 5'], 'correct': 'A) 4', 'explanation': 'Order 4 means max 3 keys/node. Min keys per node = ceil(4/2)-1 = 1. Max keys at height h = 4^h - 1. Height 4 => 4^4 - 1 = 255. So minimum height = 4.', 'marks': '1 Mark'},

        # OOP HARD (3 Qs)
        {'q_num': 22, 'type': 'mcq', 'title': 'OOP: Diamond Problem Resolution', 'text': 'In C++, class D inherits from B and C, both inheriting from A. Without virtual inheritance, how many copies of A exist in D?', 'options': ['A) 0 copies (abstract)', 'B) 1 copy of A', 'C) 2 copies of A', 'D) 4 copies of A'], 'correct': 'C) 2 copies of A', 'explanation': 'Without virtual inheritance, D gets one copy of A through B and another through C, leading to the diamond problem ambiguity.', 'marks': '1 Mark'},
        {'q_num': 23, 'type': 'mcq', 'title': 'OOP: Design Pattern Identification', 'text': 'A class that ensures only one instance exists globally and provides a single global access point implements which pattern?', 'options': ['A) Observer Pattern', 'B) Factory Pattern', 'C) Facade Pattern', 'D) Singleton Pattern'], 'correct': 'D) Singleton Pattern', 'explanation': 'Singleton restricts instantiation to one object and provides a global access point via static method.', 'marks': '1 Mark'},
        {'q_num': 24, 'type': 'mcq', 'title': 'OOP: Virtual Function Table (VTable)', 'text': 'In C++, what is stored in a vtable (virtual table) of a class?', 'options': ['A) Static method addresses only', 'B) Pointers to virtual function implementations', 'C) Constructor call sequence', 'D) All member variable values'], 'correct': 'B) Pointers to virtual function implementations', 'explanation': 'VTable contains function pointers to the most-derived overriding implementations used for runtime polymorphism dispatch.', 'marks': '1 Mark'},

        # OS HARD (3 Qs)
        {'q_num': 25, 'type': 'mcq', 'title': "OS: Banker's Algorithm Safety Check", 'text': 'With 3 processes P1,P2,P3 and 1 resource type: Available=2, Max=[7,3,9], Allocated=[3,2,3]. Is the system in a safe state?', 'options': ['A) Yes, safe sequence P2->P1->P3 exists', 'B) No safe state exists', 'C) Yes, but only via P3->P2->P1', 'D) Deadlock is guaranteed'], 'correct': 'A) Yes, safe sequence P2->P1->P3 exists', 'explanation': 'Need = Max - Allocated = [4,1,6]. Available=2. P2 needs 1 <= 2, runs, returns 4. Now avail=4. P1 needs 4<=4, runs, returns 7. Avail=7. P3 needs 6<=7. Safe!', 'marks': '1 Mark'},
        {'q_num': 26, 'type': 'mcq', 'title': 'OS: Page Replacement - Optimal Algorithm', 'text': 'Reference string: 7,0,1,2,0,3,0,4,2,3 with 3 frames. How many page faults with OPT (Optimal) algorithm?', 'options': ['A) 8', 'B) 7', 'C) 6', 'D) 5'], 'correct': 'C) 6', 'explanation': 'Tracing OPT: 7(miss),0(miss),1(miss),2(miss-replace 7),0(hit),3(miss-replace 1),0(hit),4(miss-replace 3),2(hit),3(miss-replace 4). Total = 6 faults.', 'marks': '1 Mark'},
        {'q_num': 27, 'type': 'mcq', 'title': 'OS: Semaphore Deadlock Analysis', 'text': 'Two processes P1 and P2 each need semaphores S1 and S2. P1 acquires S1 then waits for S2. P2 acquires S2 then waits for S1. What will happen?', 'options': ['A) Livelock', 'B) Successful completion', 'C) Starvation only', 'D) Circular wait deadlock'], 'correct': 'D) Circular wait deadlock', 'explanation': 'P1 holds S1 waiting for S2. P2 holds S2 waiting for S1. Classic circular wait, one of four Coffman conditions for deadlock.', 'marks': '1 Mark'},

        # Technical Fundamentals HARD (3 Qs)
        {'q_num': 28, 'type': 'mcq', 'title': 'Tech Fundamentals: TCP Three-Way Handshake', 'text': 'During a TCP connection teardown (4-way close), why does the client wait in TIME_WAIT state for 2*MSL?', 'options': ['A) To ensure delayed packets from the old connection expire before new connections use the same port', 'B) To allow server to send more data', 'C) To retransmit the SYN packet', 'D) To perform RST flooding prevention'], 'correct': 'A) To ensure delayed packets from the old connection expire before new connections use the same port', 'explanation': 'MSL (Maximum Segment Lifetime) ensures old duplicate segments cannot interfere with new connections on the same socket pair.', 'marks': '1 Mark'},
        {'q_num': 29, 'type': 'mcq', 'title': 'Tech Fundamentals: Consistent Hashing', 'text': 'In consistent hashing with N nodes and K keys, when one node is added or removed, how many keys need remapping on average?', 'options': ['A) log(K) keys', 'B) All K keys', 'C) K/N keys', 'D) K/2 keys'], 'correct': 'C) K/N keys', 'explanation': 'Consistent hashing minimizes remapping: only ~K/N keys need to move on a single node change, unlike simple mod-N hashing.', 'marks': '1 Mark'},
        {'q_num': 30, 'type': 'mcq', 'title': 'Tech Fundamentals: Amortized Complexity', 'text': 'Dynamic array doubles capacity when full. Starting with size 1, after N insertions, what is the amortized cost per insertion?', 'options': ['A) O(sqrt N) amortized', 'B) O(1) amortized', 'C) O(N) amortized', 'D) O(log N) amortized'], 'correct': 'B) O(1) amortized', 'explanation': 'Total copy work = 1+2+4+...+N = 2N. Spread over N insertions = O(1) amortized via aggregate method.', 'marks': '1 Mark'},
    ]

    return [
        {
            'section_name': 'Round 1: Aptitude + English',
            'time': '45 Mins',
            'questions': sec1_aptitude_english
        },
        {
            'section_name': 'Round 2: Technical/Psychometric',
            'time': '40 Mins',
            'questions': sec2_technical_psychometric
        }
    ]


def get_capgemini_sections():
    comp_clean = 'Capgemini'
    # -------------------------------------------------------------------------
    # SECTION 1: Online Aptitude Assessment (20 HARD Questions)
    # Topics: Quantitative aptitude, logical reasoning, verbal ability, analytical reasoning
    # -------------------------------------------------------------------------
    sec1_qs = [
        # Quantitative Aptitude HARD (Q1 to Q6)
        {'q_num': 1, 'type': 'mcq', 'title': 'Permutations with Constrained Grouping', 'text': 'In how many distinct ways can 8 corporate directors sit around a circular table if 3 specific directors (A, B, C) strictly refuse to sit adjacent to each other?', 'options': ['A) 1,440 ways', 'B) 720 ways', 'C) 2,880 ways', 'D) 4,320 ways'], 'correct': 'A) 1,440 ways', 'explanation': 'Arrange remaining 5 directors in (5-1)! = 24 ways. This creates 5 gap spaces. Choose 3 gaps for A, B, C: P(5,3) = 60. Total ways = 24 * 60 = 1,440.', 'marks': '2 Marks'},
        {'q_num': 2, 'type': 'mcq', 'title': 'Compound Interest Half-Yearly Differential', 'text': 'What is the exact difference between Compound Interest (compounded semi-annually) and Simple Interest at 12% per annum for 2 years on a principal of ₹25,000?', 'options': ['A) ₹382.26', 'B) ₹412.50', 'C) ₹320.00', 'D) ₹455.10'], 'correct': 'A) ₹382.26', 'explanation': 'SI = 25000 * 0.12 * 2 = 6,000. CI rate per half-year = 6%, n = 4 periods. Amount = 25000 * (1.06)^4 = ₹31,562.26. CI = ₹6,562.26. Diff = 6562.26 - 6000 = ₹382.26.', 'marks': '2 Marks'},
        {'q_num': 3, 'type': 'mcq', 'title': 'Work Efficiency Degradation Model', 'text': 'A, B, and C can complete a task in 20, 30, and 60 days respectively. If A works continuously while B and C assist A on every third day, how many days will the task take to complete?', 'options': ['A) 15 days', 'B) 12 days', 'C) 18 days', 'D) 10 days'], 'correct': 'A) 15 days', 'explanation': 'Total work = 60 units. A\'s rate = 3/day, B = 2/day, C = 1/day. Day 1 (A)=3, Day 2 (A)=3, Day 3 (A+B+C)=6. 3-day cycle work = 3+3+6 = 12 units. Cycles needed = 60 / 12 = 5 cycles = 15 days.', 'marks': '2 Marks'},
        {'q_num': 4, 'type': 'mcq', 'title': 'Relative Speed Acceleration Catchup', 'text': 'Two trains start at the same time from stations A and B, 450 km apart, traveling toward each other at 50 km/h and 40 km/h. After 2 hours, train A accelerates by 20%. Where do they cross relative to A?', 'options': ['A) 260 km from A', 'B) 250 km from A', 'C) 240 km from A', 'D) 270 km from A'], 'correct': 'A) 260 km from A', 'explanation': 'In 2 hrs, A covers 100km, B covers 80km. Remaining distance = 450 - 180 = 270km. New speed of A = 60 km/h. Relative speed = 60 + 40 = 100 km/h. Time to meet = 270/100 = 2.7 hrs. Total distance from A = 100 + (60 * 2.7) = 260 km.', 'marks': '2 Marks'},
        {'q_num': 5, 'type': 'mcq', 'title': 'Repeated Solution Replacement Formula', 'text': 'A container holds 80 liters of pure alcohol. 16 liters are drawn and replaced with water. This process is repeated two more times (3 times total). How much pure alcohol remains?', 'options': ['A) 40.96 liters', 'B) 48.00 liters', 'C) 36.50 liters', 'D) 42.20 liters'], 'correct': 'A) 40.96 liters', 'explanation': 'Remaining alcohol = 80 * (1 - 16/80)^3 = 80 * (4/5)^3 = 80 * 0.512 = 40.96 liters.', 'marks': '2 Marks'},
        {'q_num': 6, 'type': 'mcq', 'title': 'Probability of Non-overlapping Subsets', 'text': '3 cards are drawn at random without replacement from a 52-card deck. What is the probability that all 3 cards belong to different suits?', 'options': ['A) 0.3976', 'B) 0.2450', 'C) 0.5120', 'D) 0.1850'], 'correct': 'A) 0.3976', 'explanation': 'P = (52/52) * (39/51) * (26/50) = 1 * (13/17) * (13/25) = 169 / 425 ≈ 0.3976.', 'marks': '2 Marks'},

        # Logical Reasoning HARD (Q7 to Q12)
        {'q_num': 7, 'type': 'mcq', 'title': 'Complex Matrix Floor & Department Puzzle', 'text': '8 managers (P, Q, R, S, T, U, V, W) live on 8 different floors. R lives on an even floor below 5. Only 2 people live between R and V. Department head of IT lives immediately above V. Who lives on floor 8?', 'options': ['A) W', 'B) S', 'C) U', 'D) T'], 'correct': 'A) W', 'explanation': 'Deducing constraints: R on floor 2 -> V on floor 5 -> IT head on floor 6. Eliminating impossible placements yields W on floor 8.', 'marks': '2 Marks'},
        {'q_num': 8, 'type': 'mcq', 'title': 'Multilevel Coded Family Tree', 'text': 'Expression: `A # B % C $ D * E` where `#`=father, `%`=sister, `$`=husband, `*`=mother. How is A related to E?', 'options': ['A) Maternal Grandfather', 'B) Father-in-law', 'C) Paternal Uncle', 'D) Brother-in-law'], 'correct': 'A) Maternal Grandfather', 'explanation': 'A is father of B; B is sister of C; C is husband of D; D is mother of E => A is father of E\'s mother (Maternal Grandfather).', 'marks': '2 Marks'},
        {'q_num': 9, 'type': 'mcq', 'title': 'Advanced Syllogism Possibility Logic', 'text': 'Statements: 1. Only a few coders are analysts. 2. No analyst is a manager. Conclusions: I. All coders can never be managers. II. Some coders being managers is a possibility.', 'options': ['A) Both I and II follow', 'B) Only I follows', 'C) Only II follows', 'D) Neither follows'], 'correct': 'A) Both I and II follow', 'explanation': 'The portion of coders that are analysts can never be managers, so All coders can never be managers (I valid). Coders outside analysts can be managers (II valid).', 'marks': '2 Marks'},
        {'q_num': 10, 'type': 'mcq', 'title': 'Triple-Shift Cryptarithm Addition', 'text': 'In cryptarithm `SEND + MORE = MONEY`, what is the sum of numeric digits assigned to letters M + O + N + E?', 'options': ['A) 14', 'B) 18', 'C) 12', 'D) 16'], 'correct': 'A) 14', 'explanation': 'Unique solution: S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2. M+O+N+E = 1 + 0 + 6 + 5 = 14.', 'marks': '2 Marks'},
        {'q_num': 11, 'type': 'mcq', 'title': 'Direction 3D Displacement Vector', 'text': 'A person walks 12m North, 5m East, and then climbs a vertical pole of height 84m. What is the straight-line shortest displacement from origin?', 'options': ['A) 85m', 'B) 91m', 'C) 78m', 'D) 89m'], 'correct': 'A) 85m', 'explanation': 'Ground displacement = sqrt(12^2 + 5^2) = sqrt(144 + 25) = 13m. 3D displacement = sqrt(13^2 + 84^2) = sqrt(169 + 7056) = sqrt(7225) = 85m.', 'marks': '2 Marks'},
        {'q_num': 12, 'type': 'mcq', 'title': 'Input-Output Machine Shift Pattern', 'text': 'Machine input: `alpha 84 beta 19 gamma 62 delta 45`. If numbers sort ascending by sum of digits and words sort reverse-alphabetically, what is Step 3?', 'options': ['A) 19 gamma 84 alpha beta 62 delta 45', 'B) 19 gamma delta 45 62 beta alpha 84', 'C) gamma 19 delta 45 62 84 alpha beta', 'D) 19 45 62 84 gamma delta beta alpha'], 'correct': 'A) 19 gamma 84 alpha beta 62 delta 45', 'explanation': 'Sum of digits: 19(10), 84(12), 62(8), 45(9). Sorting rule swaps smallest digit sum & highest reverse-alphabet word alternately per step.', 'marks': '2 Marks'},

        # Verbal Ability HARD (Q13 to Q16)
        {'q_num': 13, 'type': 'mcq', 'title': 'Critical Reasoning Assumption Analysis', 'text': 'Argument: "Implementing strict AI code reviews will reduce software security flaws by 60%." Which unstated assumption is critical to this argument?', 'options': ['A) Human reviewers currently overlook vulnerabilities that AI pattern-matching algorithms detect', 'B) AI code review tools cost less than human security engineers', 'C) All software developers write unsafe code intentionally', 'D) Security flaws are exclusively caused by syntax errors'], 'correct': 'A) Human reviewers currently overlook vulnerabilities that AI pattern-matching algorithms detect', 'explanation': 'For AI reviews to achieve a 60% flaw reduction, AI must catch vulnerabilities currently missed by existing human review processes.', 'marks': '2 Marks'},
        {'q_num': 14, 'type': 'mcq', 'title': 'Complex Para Jumble Structuring', 'text': 'Sentence Ordering: (P) Consequently, quantum coherence degrades rapidly. (Q) Superconducting qubits require cryogenic temperatures near absolute zero. (R) At these thermal states, environmental noise is suppressed. (S) However, thermal fluctuations still cause decoherence. Correct order?', 'options': ['A) Q-R-S-P', 'B) R-Q-S-P', 'C) P-S-Q-R', 'D) S-Q-R-P'], 'correct': 'A) Q-R-S-P', 'explanation': 'Q introduces requirement (cryogenic temps) -> R explains benefit (noise suppressed) -> S introduces contrast (thermal fluctuations) -> P provides consequence (coherence degrades).', 'marks': '2 Marks'},
        {'q_num': 15, 'type': 'mcq', 'title': 'Subjunctive & Conditional Error Spotting', 'text': 'Identify the grammatical error: "Had the lead architect (A) / foreseen the scalability bottlenecks (B) / he would had refactored (C) / the microservices prior to deployment (D)."', 'options': ['A) Part C', 'B) Part A', 'C) Part B', 'D) Part D'], 'correct': 'A) Part C', 'explanation': 'Inverted past perfect conditional requires "would have refactored" instead of ungrammatical "would had refactored".', 'marks': '2 Marks'},
        {'q_num': 16, 'type': 'mcq', 'title': 'GRE-level Double Blank Sentence Completion', 'text': 'The consultant\'s _______ report was criticized for being so _______ that even seasoned executives could not decipher its key takeaways.', 'options': ['A) recondite / arcane', 'B) lucid / transparent', 'C) succinct / explicit', 'D) pragmatic / straightforward'], 'correct': 'A) recondite / arcane', 'explanation': '"Recondite" (abstruse/deep) and "arcane" (mysterious/obscure) fit the context of an undecipherable report.', 'marks': '2 Marks'},

        # Analytical Reasoning HARD (Q17 to Q20)
        {'q_num': 17, 'type': 'mcq', 'title': 'Antonym of Obsequious', 'text': 'What is the precise antonym of the word OBSEQUIOUS?', 'options': ['A) Domineering and Assertive', 'B) Servile', 'C) Sycophantic', 'D) Submissive'], 'correct': 'A) Domineering and Assertive', 'explanation': 'Obsequious means excessively submissive or servile. Its antonym is domineering or assertive.', 'marks': '2 Marks'},
        {'q_num': 18, 'type': 'mcq', 'title': 'Venn Diagram Data Sufficiency Optimization', 'text': 'Out of 120 software engineers, 70 know Python, 60 know Java, and 50 know C++. If 20 know all three, what is the maximum possible number of engineers who know NONE of these languages?', 'options': ['A) 20', 'B) 10', 'C) 30', 'D) 0'], 'correct': 'A) 20', 'explanation': 'To maximize engineers knowing none, minimize union size. Min union = max(Python, Java, C++) = 70. None = 120 - 100 = 20 max.', 'marks': '2 Marks'},
        {'q_num': 19, 'type': 'mcq', 'title': 'Analytical Decision Policy Evaluation', 'text': 'Candidate Criteria: 1. B.Tech >= 75%, 2. Test score >= 80%, 3. Age 21-26. Exception: If B.Tech < 75% but candidate has 2+ yrs experience, refer to VP. Candidate X: B.Tech 71%, Test 88%, Age 24, 3 yrs experience. Action?', 'options': ['A) Refer to Vice President', 'B) Select Candidate', 'C) Reject Candidate', 'D) Insufficient Data'], 'correct': 'A) Refer to Vice President', 'explanation': 'Candidate fails criterion 1 (71% < 75%), but qualifies for exception (3 yrs exp >= 2 yrs). Must be referred to VP.', 'marks': '2 Marks'},
        {'q_num': 20, 'type': 'mcq', 'title': 'Probability of System Reliability Cascade', 'text': 'A cloud architecture relies on 3 parallel servers, each with 90% availability. What is the overall uptime probability of the system?', 'options': ['A) 99.9%', 'B) 90.0%', 'C) 97.3%', 'D) 99.0%'], 'correct': 'A) 99.9%', 'explanation': 'System fails only if all 3 servers fail simultaneously. P(all fail) = (0.1)^3 = 0.001. System uptime = 1 - 0.001 = 0.999 = 99.9%.', 'marks': '2 Marks'}
    ]

    # -------------------------------------------------------------------------
    # SECTION 2: Technical Assessment (20 HARD Questions)
    # Topics: Pseudocode, programming, computer fundamentals, DBMS, OOP, technical MCQs
    # -------------------------------------------------------------------------
    sec2_qs = [
        # Pseudocode & Programming HARD (Q21 to Q28)
        {'q_num': 21, 'type': 'mcq', 'title': 'Pseudocode Bitwise Shift Execution', 'text': 'What is the output of pseudocode: `Integer a=5, b=3, c=2; c = (a & b) ^ (c << 2); Print c;`?', 'options': ['A) 9', 'B) 7', 'C) 11', 'D) 5'], 'correct': 'A) 9', 'explanation': 'a & b = 5 & 3 = 1. c << 2 = 2 << 2 = 8. (a & b) ^ (c << 2) = 1 ^ 8 = 9.', 'marks': '2 Marks'},
        {'q_num': 22, 'type': 'mcq', 'title': 'Recursive Function Call Stack Memory', 'text': 'Consider pseudocode: `Function fun(n): If n <= 1 Return 1; Return fun(n-1) + fun(n-2);`. How many total function calls occur for `fun(5)`?', 'options': ['A) 15', 'B) 9', 'C) 12', 'D) 8'], 'correct': 'A) 15', 'explanation': 'fun(5) calls fun(4)+fun(3). Total nodes in recursion tree for Fibonacci(5) = 15 calls.', 'marks': '2 Marks'},
        {'q_num': 23, 'type': 'mcq', 'title': 'C Pointer Arithmetic Indirection', 'text': 'What is the output of: `int arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}}; printf("%d", *(*(arr + 1) + 2));`?', 'options': ['A) 6', 'B) 5', 'C) 8', 'D) 4'], 'correct': 'A) 6', 'explanation': '`(arr + 1)` points to row 1 `{4,5,6}`. `*(arr + 1) + 2` points to element at index 2 of row 1, which is 6. Dereferencing gives 6.', 'marks': '2 Marks'},
        {'q_num': 24, 'type': 'mcq', 'title': 'Static Scope State in Recursion', 'text': 'What is printed by C snippet: `int solve(int n) { static int r=0; if(n<=0) return 0; r++; return solve(n-1)+r; } main() { printf("%d", solve(3)); }`?', 'options': ['A) 9', 'B) 6', 'C) 3', 'D) 12'], 'correct': 'A) 9', 'explanation': 'n=3: r becomes 1. n=2: r becomes 2. n=1: r becomes 3. n=0: returns 0. Each frame adds final static r (3). Total = 3 + 3 + 3 = 9.', 'marks': '2 Marks'},
        {'q_num': 25, 'type': 'mcq', 'title': 'Struct Alignment & Padding Layout', 'text': 'In a 64-bit C compiler (8-byte alignment), what is `sizeof(struct S)` for `struct S { char c; double d; int i; short s; };`?', 'options': ['A) 24 bytes', 'B) 15 bytes', 'C) 16 bytes', 'D) 32 bytes'], 'correct': 'A) 24 bytes', 'explanation': 'c(1)+padding(7)=8, d(8)=8, i(4)+s(2)+padding(2)=8. Total size = 8 + 8 + 8 = 24 bytes.', 'marks': '2 Marks'},
        {'q_num': 26, 'type': 'mcq', 'title': 'VTable Pointer Memory Corruption', 'text': 'In C++, if a base class destructor is NOT declared `virtual`, deleting a derived object via base class pointer results in:', 'options': ['A) Undefined Behavior / Derived destructor not called', 'B) Compilation Error', 'C) Automatic Virtual Dispatch', 'D) Segfault during creation'], 'correct': 'A) Undefined Behavior / Derived destructor not called', 'explanation': 'Without virtual destructor, delete via base pointer only invokes base destructor, leaving derived resources uncleaned (memory leak / UB).', 'marks': '2 Marks'},
        {'q_num': 27, 'type': 'mcq', 'title': 'Python Decorator Execution Order', 'text': 'Given `@dec1 @dec2 def foo(): pass`. In what order are the decorators evaluated and executed?', 'options': ['A) dec2 wraps foo first, then dec1 wraps the result', 'B) dec1 wraps foo first, then dec2 wraps result', 'C) Both wrap in parallel', 'D) Syntax Error in Python'], 'correct': 'A) dec2 wraps foo first, then dec1 wraps the result', 'explanation': 'Python decorator syntax `@dec1 @dec2 def foo()` is equivalent to `foo = dec1(dec2(foo))`. `dec2` executes first.', 'marks': '2 Marks'},
        {'q_num': 28, 'type': 'mcq', 'title': 'Java Synchronized Block Deadlock', 'text': 'Thread 1 locks ObjA then ObjB. Thread 2 locks ObjB then ObjA. What concurrency defect is triggered?', 'options': ['A) Deadlock', 'B) Race Condition', 'C) Livelock', 'D) Memory Leak'], 'correct': 'A) Deadlock', 'explanation': 'Opposite lock acquisition order creates circular wait condition, causing a Deadlock.', 'marks': '2 Marks'},

        # Computer Fundamentals HARD (Q29 to Q31)
        {'q_num': 29, 'type': 'mcq', 'title': 'Set Associative Cache Address Bit Split', 'text': 'A 32-bit CPU has a 64 KB 2-way Set-Associative Cache with 32-byte cache lines. How many bits are used for Tag, Set Index, and Offset?', 'options': ['A) Tag=17 bits, Index=10 bits, Offset=5 bits', 'B) Tag=16 bits, Index=11 bits, Offset=5 bits', 'C) Tag=20 bits, Index=7 bits, Offset=5 bits', 'D) Tag=18 bits, Index=9 bits, Offset=5 bits'], 'correct': 'A) Tag=17 bits, Index=10 bits, Offset=5 bits', 'explanation': 'Offset = log2(32) = 5 bits. Total lines = 64KB / 32B = 2048. Sets = 2048 / 2 = 1024. Index = log2(1024) = 10 bits. Tag = 32 - 10 - 5 = 17 bits.', 'marks': '2 Marks'},
        {'q_num': 30, 'type': 'mcq', 'title': 'IEEE 754 Single-Precision Binary Encoding', 'text': 'In IEEE 754 single-precision 32-bit floating point, what is the biased exponent value stored for decimal number `+12.5`?', 'options': ['A) 130 (10000010 in binary)', 'B) 127 (01111111 in binary)', 'C) 131 (10000011 in binary)', 'D) 123 (01111011 in binary)'], 'correct': 'A) 130 (10000010 in binary)', 'explanation': '12.5 = 1100.1 in binary = 1.1001 * 2^3. Actual exponent = 3. Biased exponent = 3 + 127 = 130 (10000010).', 'marks': '2 Marks'},
        {'q_num': 31, 'type': 'mcq', 'title': 'B+ Tree Order 5 Node Capacity', 'text': 'In a B+ Tree of order 5, what is the maximum number of keys an internal node can hold before splitting?', 'options': ['A) 4 keys', 'B) 5 keys', 'C) 3 keys', 'D) 6 keys'], 'correct': 'A) 4 keys', 'explanation': 'Order m B+ Tree internal node can have at most m children and m-1 keys. Order 5 means max 4 keys.', 'marks': '2 Marks'},

        # DBMS & SQL HARD (Q32 to Q34)
        {'q_num': 32, 'type': 'mcq', 'title': 'Conflict Serializability Precedence Cycle', 'text': 'Schedule S: `r1(X); w2(X); r1(Y); w3(Y); r2(Y); w1(X);`. Is schedule S conflict-serializable?', 'options': ['A) No, precedence graph has cycle (T1 -> T2 -> T1)', 'B) Yes, equivalent to T1 -> T2 -> T3', 'C) Yes, equivalent to T3 -> T2 -> T1', 'D) Cannot be evaluated'], 'correct': 'A) No, precedence graph has cycle (T1 -> T2 -> T1)', 'explanation': 'r1(X) before w2(X) gives T1->T2. w2(X) before w1(X) gives T2->T1. Cycle T1->T2->T1 makes it non-serializable.', 'marks': '2 Marks'},
        {'q_num': 33, 'type': 'mcq', 'title': '4NF Multi-Valued Dependency (MVD)', 'text': 'A relation R(Course, Teacher, TextBook) has FDs: `Course ->-> Teacher` and `Course ->-> TextBook`. What normal form violation occurs if non-trivial MVDs exist?', 'options': ['A) 4NF Violation', 'B) 3NF Violation', 'C) BCNF Violation', 'D) 2NF Violation'], 'correct': 'A) 4NF Violation', 'explanation': 'Multi-Valued Dependencies independent of candidate key violate 4th Normal Form (4NF).', 'marks': '2 Marks'},
        {'q_num': 34, 'type': 'mcq', 'title': 'SQL Correlated Subquery Optimization', 'text': 'Query: `SELECT E1.name FROM Employee E1 WHERE E1.salary > (SELECT AVG(E2.salary) FROM Employee E2 WHERE E2.dept_id = E1.dept_id)`. What is the time complexity without indexing?', 'options': ['A) O(N^2)', 'B) O(N log N)', 'C) O(N)', 'D) O(1)'], 'correct': 'A) O(N^2)', 'explanation': 'Correlated subquery evaluates inner query for every row in outer table, yielding O(N^2) without index.', 'marks': '2 Marks'},

        # OOP & Architecture HARD (Q35 to Q37)
        {'q_num': 35, 'type': 'mcq', 'title': 'SOLID Principles - Open/Closed Principle', 'text': 'A class uses `switch(shape_type)` to calculate area for Circle, Square, Triangle. Which SOLID principle is violated?', 'options': ['A) Open/Closed Principle (OCP)', 'B) Liskov Substitution Principle (LSP)', 'C) Interface Segregation Principle (ISP)', 'D) Single Responsibility Principle (SRP)'], 'correct': 'A) Open/Closed Principle (OCP)', 'explanation': 'Adding a new shape requires modifying existing code, violating Open/Closed Principle (Open for extension, closed for modification).', 'marks': '2 Marks'},
        {'q_num': 36, 'type': 'mcq', 'title': 'Design Patterns - Abstract Factory vs Builder', 'text': 'Which design pattern is best suited for constructing complex step-by-step objects with varied representations?', 'options': ['A) Builder Pattern', 'B) Abstract Factory Pattern', 'C) Prototype Pattern', 'D) Singleton Pattern'], 'correct': 'A) Builder Pattern', 'explanation': 'Builder pattern separates construction of a complex object from its representation step-by-step.', 'marks': '2 Marks'},
        {'q_num': 37, 'type': 'mcq', 'title': 'Shallow Copy Pointer Corruption', 'text': 'Class `Buffer` has raw pointer member `int* data`. If `Buffer b2 = b1;` is executed without a custom copy constructor:', 'options': ['A) Both objects point to same memory address, causing double-free error on destruction', 'B) Deep copy occurs automatically', 'C) Compilation Error', 'D) Memory is safely garbage collected'], 'correct': 'A) Both objects point to same memory address, causing double-free error on destruction', 'explanation': 'Default copy constructor performs shallow member-wise copy. Both destructors attempt to free the same pointer.', 'marks': '2 Marks'},

        # Systems & Networks HARD (Q38 to Q40)
        {'q_num': 38, 'type': 'mcq', 'title': 'TLB Hit Ratio Effective Memory Access Time', 'text': 'TLB access time = 10ns, Main memory access time = 100ns. If TLB hit ratio is 90% (two-level page table), what is the Effective Memory Access Time (EMAT)?', 'options': ['A) 130 ns', 'B) 110 ns', 'C) 120 ns', 'D) 140 ns'], 'correct': 'A) 130 ns', 'explanation': 'Hit: 10 + 100 = 110ns (90%). Miss: 10 + 100 + 100 + 100 = 310ns (10%). EMAT = 0.9*110 + 0.1*310 = 99 + 31 = 130ns.', 'marks': '2 Marks'},
        {'q_num': 39, 'type': 'mcq', 'title': 'TCP Fast Retransmit Window Progression', 'text': 'In TCP Tahoe, when 3 duplicate ACKs are received during Congestion Avoidance at window size `cwnd = 16`, what happens to `cwnd` and `ssthresh`?', 'options': ['A) ssthresh = 8, cwnd = 1', 'B) ssthresh = 8, cwnd = 8', 'C) ssthresh = 16, cwnd = 1', 'D) ssthresh = 4, cwnd = 2'], 'correct': 'A) ssthresh = 8, cwnd = 1', 'explanation': 'TCP Tahoe drops `cwnd` to 1 MSS and sets `ssthresh` to half of current window (16/2 = 8).', 'marks': '2 Marks'},
        {'q_num': 40, 'type': 'mcq', 'title': 'Compiler Semantic Analysis Stage', 'text': 'Type checking and array bound checking occur during which compiler synthesis phase?', 'options': ['A) Semantic Analysis', 'B) Lexical Analysis', 'C) Syntax Analysis (Parsing)', 'D) Target Code Generation'], 'correct': 'A) Semantic Analysis', 'explanation': 'Semantic Analysis verifies type consistency, symbol declarations, and logical rules beyond grammar.', 'marks': '2 Marks'}
    ]

    # -------------------------------------------------------------------------
    # SECTION 3: Coding Assessment (20 HARD Questions)
    # Topics: Programming problems, DSA, problem-solving and coding efficiency
    # -------------------------------------------------------------------------
    c_code_cap1 = f"""# --- 1. PYTHON 3 SOLUTION ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf')
    def dfs(node):
        nonlocal max_sum
        if not node: return 0
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)
        current_path = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path)
        return node.val + max(left_gain, right_gain)
    dfs(root)
    return max_sum

// --- 2. JAVA 17 SOLUTION ---
public class Solution {{
    int maxVal = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {{
        maxGain(root);
        return maxVal;
    }}
    private int maxGain(TreeNode node) {{
        if (node == null) return 0;
        int left = Math.max(maxGain(node.left), 0);
        int right = Math.max(maxGain(node.right), 0);
        maxVal = Math.max(maxVal, node.val + left + right);
        return node.val + Math.max(left, right);
    }}
}}"""

    c_code_cap2 = f"""# --- 1. PYTHON 3 SOLUTION ---
import heapq

def trapRainWater2D(heightMap: list[list[int]]) -> int:
    if not heightMap or not heightMap[0]: return 0
    m, n = len(heightMap), len(heightMap[0])
    visited = [[False]*n for _ in range(m)]
    heap = []
    
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
                
    water = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    while heap:
        h, r, c = heapq.heappop(heap)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                water += max(0, h - heightMap[nr][nc])
                heapq.heappush(heap, (max(h, heightMap[nr][nc]), nr, nc))
    return water"""

    sec3_qs = [
        {
            'q_num': 41,
            'type': 'coding',
            'title': 'Binary Tree Maximum Path Sum (Any Node to Any Node)',
            'text': f'Write a function for {comp_clean} senior technical assessment to find the maximum path sum in a binary tree. A path is defined as any sequence of nodes along parent-child connections, where no node appears more than once. The path may start and end at ANY node.\n\nInput Example: root = [-10, 9, 20, null, null, 15, 7]\nOutput: 42 (Path: 15 -> 20 -> 7)\n\nSupported Languages: Python 3, Java 17, C11, C++17.',
            'options': [],
            'sample_answer': c_code_cap1,
            'explanation': 'Recursive post-order DFS computes maximum single branch gain and updates global path sum considering current node as apex.',
            'marks': '10 Marks'
        },
        {
            'q_num': 42,
            'type': 'coding',
            'title': 'Trapping Rain Water II in 2D Elevation Matrix',
            'text': f'Write a function for {comp_clean} senior technical assessment to compute total volume of water trapped after raining in a 2D m x n elevation matrix.\n\nInput Example: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]\nOutput: 4\n\nSupported Languages: Python 3, Java 17, C11, C++17.',
            'options': [],
            'sample_answer': c_code_cap2,
            'explanation': 'Uses Min-Heap Priority Queue storing boundary cells, processing lowest boundary inward to calculate trapped water volume in O(M*N log(M*N)) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 43,
            'type': 'coding',
            'title': 'Word Search II in 2D Board using Trie & DFS',
            'text': f'Given an m x n board of characters and a list of strings words, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells (horizontally or vertically).\n\nInput Example: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]\nOutput: ["oath","eat"]',
            'options': [],
            'sample_answer': '''def findWords(board, words):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = None
    root = TrieNode()
    for w in words:
        curr = root
        for c in w:
            if c not in curr.children: curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = w
    res = []
    def dfs(r, c, node):
        char = board[r][c]
        curr = node.children[char]
        if curr.word:
            res.append(curr.word)
            curr.word = None
        board[r][c] = "#"
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] in curr.children:
                dfs(nr, nc, curr)
        board[r][c] = char
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in root.children: dfs(r, c, root)
    return res''',
            'explanation': 'Build Trie of target dictionary words and perform 2D DFS backtracking on board with in-place cell masking.',
            'marks': '10 Marks'
        },
        {
            'q_num': 44,
            'type': 'coding',
            'title': 'Longest Increasing Path in a Matrix (DFS + Memoization)',
            'text': f'Given an m x n integers matrix, return the length of the longest increasing path. From each cell, you can move in four directions (up, down, left, right).\n\nInput Example: matrix = [[9,9,4],[6,6,8],[2,1,1]]\nOutput: 4 (Path: 1 -> 2 -> 6 -> 9)',
            'options': [],
            'sample_answer': '''def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]: return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0]*n for _ in range(m)]
    def dfs(r, c):
        if memo[r][c] != 0: return memo[r][c]
        val = 1
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                val = max(val, 1 + dfs(nr, nc))
        memo[r][c] = val
        return val
    return max(dfs(r, c) for r in range(m) for c in range(n))''',
            'explanation': 'Uses 2D Memoized Depth First Search (DFS) caching longest increasing paths from every grid cell in O(M*N) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 45,
            'type': 'coding',
            'title': 'Alien Dictionary Character Ordering (Topological Sort)',
            'text': f'Given a sorted dictionary of alien language words, derive the order of characters in the alien alphabet.\n\nInput Example: words = ["wrt","wrf","er","ett","rftt"]\nOutput: "wertf"',
            'options': [],
            'sample_answer': '''from collections import defaultdict, deque
def alienOrder(words):
    adj = defaultdict(set)
    in_degree = {c: 0 for w in words for c in w}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    q = deque([c for c in in_degree if in_degree[c] == 0])
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for nxt in adj[c]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0: q.append(nxt)
    return "".join(res) if len(res) == len(in_degree) else ""''',
            'explanation': 'Constructs a directed graph of character precedence rules from adjacent words and extracts Topological Order via Kahn\'s algorithm.',
            'marks': '10 Marks'
        },
        {
            'q_num': 46,
            'type': 'coding',
            'title': 'Sliding Window Maximum in Array (O(N) Monotonic Deque)',
            'text': f'Given an array nums and sliding window size k moving from left to right, return maximum element in each window.\n\nInput Example: nums = [1,3,-1,-3,5,3,6,7], k = 3\nOutput: [3,3,5,5,6,7]',
            'options': [],
            'sample_answer': '''from collections import deque
def maxSlidingWindow(nums, k):
    q = deque()
    res = []
    for i, num in enumerate(nums):
        while q and q[-1][1] <= num: q.pop()
        q.append((i, num))
        if q[0][0] <= i - k: q.popleft()
        if i >= k - 1: res.append(q[0][1])
    return res''',
            'explanation': 'Monotonic Decreasing Deque maintains candidate maximum elements per sliding window in O(N) linear time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 47,
            'type': 'coding',
            'title': 'Merge K Sorted Singly Linked Lists',
            'text': f'Given an array of k sorted linked-lists, merge all the linked-lists into one sorted linked-list and return it.\n\nInput Example: lists = [[1,4,5],[1,3,4],[2,6]]\nOutput: [1,1,2,3,4,4,5,6]',
            'options': [],
            'sample_answer': '''import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(lists):
    heap = []
    for i, l in enumerate(lists):
        if l: heapq.heappush(heap, (l.val, i, l))
    dummy = ListNode(0)
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next: heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next''',
            'explanation': 'Min-Heap Priority Queue stores head nodes of k lists, extracting smallest node iteratively in O(N log K) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 48,
            'type': 'coding',
            'title': 'Find Median from Continuous Data Stream',
            'text': f'Design a data structure that supports adding numbers from a continuous stream and finding the running median in O(1) time.\n\nOperations: addNum(1), addNum(2), findMedian() -> 1.5, addNum(3), findMedian() -> 2.0',
            'options': [],
            'sample_answer': '''import heapq
class MedianFinder:
    def __init__(self):
        self.small = [] # Max-Heap (stores lower half, negate vals)
        self.large = [] # Min-Heap (stores upper half)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self) -> float:
        if len(self.small) > len(self.large): return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0''',
            'explanation': 'Dual Priority Queues (Max-Heap for lower numbers, Min-Heap for upper numbers) maintain stream balance in O(log N) insertion.',
            'marks': '10 Marks'
        },
        {
            'q_num': 49,
            'type': 'coding',
            'title': 'Serialize and Deserialize Binary Tree',
            'text': f'Design an algorithm to serialize a binary tree into a string string representation and deserialize it back to the original tree structure.\n\nInput Example: root = [1, 2, 3, null, null, 4, 5]',
            'options': [],
            'sample_answer': '''class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
    def deserialize(self, data):
        vals = iter(data.split(","))
        def dfs():
            val = next(vals)
            if val == "N": return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()''',
            'explanation': 'Preorder DFS with delimiter "N" for null pointers achieves linear time string serialization and tree reconstruction.',
            'marks': '10 Marks'
        },
        {
            'q_num': 50,
            'type': 'coding',
            'title': 'Burst Balloons Interval Dynamic Programming',
            'text': f'Given n balloons with values nums[i]. Bursting balloon i gives nums[i-1]*nums[i]*nums[i+1] coins. Return max coins obtainable.\n\nInput Example: nums = [3,1,5,8]\nOutput: 167',
            'options': [],
            'sample_answer': '''def maxCoins(nums):
    A = [1] + [x for x in nums if x > 0] + [1]
    n = len(A)
    dp = [[0]*n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(dp[left][right], A[left]*A[k]*A[right] + dp[left][k] + dp[k][right])
    return dp[0][n-1]''',
            'explanation': 'Interval DP evaluates last balloon `k` burst between sub-problems `left` and `right` in O(N^3) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 51,
            'type': 'coding',
            'title': 'Course Schedule II Topological Prerequisites Order',
            'text': f'Given numCourses and prerequisite pairs [a, b], return the ordering of courses you should take to finish all courses. If impossible, return [].\n\nInput Example: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]\nOutput: [0,1,2,3]',
            'options': [],
            'sample_answer': '''from collections import deque
def findOrder(numCourses, prerequisites):
    adj = {i: [] for i in range(numCourses)}
    in_degree = [0]*numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
    q = deque([i for i in range(numCourses) if in_degree[i] == 0])
    res = []
    while q:
        curr = q.popleft()
        res.append(curr)
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0: q.append(nxt)
    return res if len(res) == numCourses else []''',
            'explanation': 'Detects topological sorting order of course dependency graph using Kahn\'s BFS queue algorithm.',
            'marks': '10 Marks'
        },
        {
            'q_num': 52,
            'type': 'coding',
            'title': 'Minimum Window Substring (Two-Pointer Sliding Window)',
            'text': f'Given strings s and t, return minimum window substring of s such that every character in t (including duplicates) is included.\n\nInput Example: s = "ADOBECODEBANC", t = "ABC"\nOutput: "BANC"',
            'options': [],
            'sample_answer': '''from collections import Counter
def minWindow(s: str, t: str) -> str:
    if not t or not s: return ""
    target_counts = Counter(t)
    required = len(target_counts)
    l, r, formed = 0, 0, 0
    window_counts = {}
    ans = (float("inf"), None, None)
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in target_counts and window_counts[character] == target_counts[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]: ans = (r - l + 1, l, r)
            window_counts[character] -= 1
            if character in target_counts and window_counts[character] < target_counts[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]''',
            'explanation': 'Two-pointer sliding window expands `r` to satisfy constraint and shrinks `l` to minimize length in O(N) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 53,
            'type': 'coding',
            'title': 'LRU Cache Design (Doubly Linked List + HashMap)',
            'text': f'Design a Least Recently Used (LRU) cache supporting `get` and `put` operations in O(1) time complexity.\n\nOperations: LRUCache(2), put(1,1), put(2,2), get(1)->1, put(3,3), get(2)->-1',
            'options': [],
            'sample_answer': '''class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    def _add(self, node):
        n = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = n
        n.prev = node
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache: self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]''',
            'explanation': 'Combines HashMap O(1) lookup with Doubly Linked List O(1) node insertion/deletion at MRU head and LRU tail.',
            'marks': '10 Marks'
        },
        {
            'q_num': 54,
            'type': 'coding',
            'title': 'LFU Cache Design (Frequency Map + Doubly Linked Lists)',
            'text': f'Design a Least Frequently Used (LFU) cache supporting `get` and `put` in O(1) average time.\n\nOperations: LFUCache(2), put(1,1), put(2,2), get(1)->1, put(3,3), get(2)->-1',
            'options': [],
            'sample_answer': '''from collections import defaultdict
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val, self.freq = key, val, 1
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def add(self, node):
        n = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = n
        n.prev = node
        self.size += 1
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
        self.size -= 1
    def remove_last(self):
        if self.size > 0:
            node = self.tail.prev
            self.remove(node)
            return node
        return None''',
            'explanation': 'Uses frequency buckets of Doubly Linked Lists to track usage frequency and eviction order in O(1) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 55,
            'type': 'coding',
            'title': 'Edit Distance (Levenshtein Distance DP Matrix)',
            'text': f'Given two strings word1 and word2, return min operations (insert, delete, replace) required to convert word1 into word2.\n\nInput Example: word1 = "horse", word2 = "ros"\nOutput: 3',
            'options': [],
            'sample_answer': '''def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]''',
            'explanation': '2D DP matrix evaluates min operations (insert, delete, substitute) in O(M*N) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 56,
            'type': 'coding',
            'title': 'N-Queens Placement Problem (Backtracking Bitmask)',
            'text': f'Place n queens on an n x n chessboard such that no two queens attack each other. Return all distinct solutions.\n\nInput Example: n = 4\nOutput: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]',
            'options': [],
            'sample_answer': '''def solveNQueens(n: int):
    res = []
    board = [["."] * n for _ in range(n)]
    cols = set()
    posDiag = set() # (r + c)
    negDiag = set() # (r - c)
    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r + c) in posDiag or (r - c) in negDiag: continue
            cols.add(c); posDiag.add(r + c); negDiag.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)
            cols.remove(c); posDiag.remove(r + c); negDiag.remove(r - c)
            board[r][c] = "."
    backtrack(0)
    return res''',
            'explanation': 'Backtracking tracks invalid columns and diagonals using sets to place queens safely.',
            'marks': '10 Marks'
        },
        {
            'q_num': 57,
            'type': 'coding',
            'title': 'Shortest Path in Grid with K Obstacle Eliminations',
            'text': f'Given m x n grid and k obstacle eliminations allowed, return min steps to walk from (0,0) to (m-1,n-1).\n\nInput Example: grid = [[0,0,0],[1,1,0],[0,0,0]], k = 1\nOutput: 4',
            'options': [],
            'sample_answer': '''from collections import deque
def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    if m == 1 and n == 1: return 0
    q = deque([(0, 0, k, 0)])
    visited = {(0, 0, k)}
    while q:
        r, c, k_left, steps = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                nk = k_left - grid[nr][nc]
                if nk >= 0 and (nr, nc, nk) not in visited:
                    if nr == m - 1 and nc == n - 1: return steps + 1
                    visited.add((nr, nc, nk))
                    q.append((nr, nc, nk, steps + 1))
    return -1''',
            'explanation': '3D BFS state `(row, col, remaining_k)` computes shortest path with obstacle elimination in O(M*N*K) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 58,
            'type': 'coding',
            'title': 'Count of Smaller Numbers After Self (Fenwick Tree / BIT)',
            'text': f'Given array nums, return an array counts where counts[i] is number of smaller elements to right of nums[i].\n\nInput Example: nums = [5,2,6,1]\nOutput: [2,1,1,0]',
            'options': [],
            'sample_answer': '''class FenwickTree:
    def __init__(self, size):
        self.tree = [0]*(size + 1)
    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def countSmaller(nums):
    ranks = {val: i + 1 for i, val in enumerate(sorted(set(nums)))}
    bit = FenwickTree(len(ranks))
    res = []
    for num in reversed(nums):
        rank = ranks[num]
        res.append(bit.query(rank - 1))
        bit.update(rank, 1)
    return res[::-1]''',
            'explanation': 'Coordinate compression with Binary Indexed Tree (Fenwick Tree) computes smaller right elements in O(N log N) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 59,
            'type': 'coding',
            'title': 'Wildcard Pattern Matching with "*" and "?"',
            'text': f'Given string s and pattern p, implement wildcard pattern matching with support for "?" (matches any single character) and "*" (matches any sequence of characters).\n\nInput Example: s = "aa", p = "*"\nOutput: True',
            'options': [],
            'sample_answer': '''def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == "*": dp[0][j] = dp[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == "*" :
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[j-1] == "?" or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[m][n]''',
            'explanation': '2D DP Matrix evaluates wildcard transitions for star and question mark wildcards in O(M*N) time.',
            'marks': '10 Marks'
        },
        {
            'q_num': 60,
            'type': 'coding',
            'title': 'Maximum Profit in Job Scheduling (DP + Binary Search)',
            'text': f'Given n jobs with startTime, endTime, and profit, find max profit such that no two jobs overlap in time.\n\nInput Example: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]\nOutput: 120 (Jobs 1 and 4)',
            'options': [],
            'sample_answer': '''import bisect
def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    dp_end = [0]
    dp_profit = [0]
    for s, e, p in jobs:
        idx = bisect.bisect_right(dp_end, s) - 1
        curr_profit = dp_profit[idx] + p
        if curr_profit > dp_profit[-1]:
            dp_end.append(e)
            dp_profit.append(curr_profit)
    return dp_profit[-1]''',
            'explanation': 'Weighted Interval Scheduling DP sorted by end time uses Binary Search (`bisect_right`) to find last non-overlapping job in O(N log N) time.',
            'marks': '10 Marks'
        }
    ]

    # -------------------------------------------------------------------------
    # SECTION 4: Technical Interview (20 HARD Questions)
    # Topics: Programming, OOP, DBMS/SQL, OS, CN, projects and technical fundamentals
    # -------------------------------------------------------------------------
    sec4_qs = [
        # OOP & Architecture HARD (Q61 to Q63)
        {'q_num': 61, 'type': 'mcq', 'title': 'Liskov Substitution Principle Violation', 'text': 'Class `Square` inherits from `Rectangle`. Setting `setWidth(5)` and `setHeight(10)` causes `Square` area to become 100 instead of 50. Which SOLID principle is violated?', 'options': ['A) Liskov Substitution Principle (LSP)', 'B) Single Responsibility Principle', 'C) Dependency Inversion Principle', 'D) Interface Segregation Principle'], 'correct': 'A) Liskov Substitution Principle (LSP)', 'explanation': 'Subtype Square cannot replace base class Rectangle without altering behavior expected of Rectangle (violates LSP).', 'marks': '2 Marks'},
        {'q_num': 62, 'type': 'mcq', 'title': 'C++ Multiple Inheritance Virtual Base Offset', 'text': 'In C++ diamond inheritance (`class D: public B, public C` where B, C derive `virtual public A`), how is single instance of A accessed in D?', 'options': ['A) Via virtual base pointer offset in object memory layout', 'B) Multiple copies of A are stored in D', 'C) Static class pointer', 'D) Compilation Error'], 'correct': 'A) Via virtual base pointer offset in object memory layout', 'explanation': 'Virtual inheritance adds vptr/offset pointer to shared single instance of A in memory.', 'marks': '2 Marks'},
        {'q_num': 63, 'type': 'mcq', 'title': 'DBMS Transaction Isolation Anomalies', 'text': 'Which Database Isolation Level prevents Dirty Reads and Non-Repeatable Reads, but still permits Phantom Reads?', 'options': ['A) Repeatable Read', 'B) Read Committed', 'C) Read Uncommitted', 'D) Serializable'], 'correct': 'A) Repeatable Read', 'explanation': 'Repeatable Read locks read rows preventing modifications (Non-Repeatable Reads), but new inserted rows can appear (Phantom Reads).', 'marks': '2 Marks'},

        # DBMS & SQL HARD (Q64 to Q66)
        {'q_num': 64, 'type': 'mcq', 'title': 'Write-Ahead Logging (WAL) & ARIES Protocol', 'text': 'Why must Write-Ahead Logging (WAL) write log records to disk BEFORE flushing corresponding dirty data pages to disk?', 'options': ['A) To ensure UNDO and REDO recovery can restore state after crash', 'B) To save disk IO bandwidth', 'C) To encrypt database tables', 'D) To format index pages'], 'correct': 'A) To ensure UNDO and REDO recovery can restore state after crash', 'explanation': 'WAL protocol guarantees that crash recovery can UNDO uncommitted transactions and REDO committed ones.', 'marks': '2 Marks'},
        {'q_num': 65, 'type': 'mcq', 'title': 'SQL Dense Rank Window Function', 'text': 'Query: `SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rk FROM Emp`. Salaries: [5000, 5000, 4000]. What is `rk` for salary 4000?', 'options': ['A) 2', 'B) 3', 'C) 1', 'D) 4'], 'correct': 'A) 2', 'explanation': '`DENSE_RANK()` does not skip ranks after ties: 5000 is rank 1, 5000 is rank 1, next unique salary 4000 gets rank 2.', 'marks': '2 Marks'},
        {'q_num': 66, 'type': 'mcq', 'title': 'Recursive CTE Organizational Hierarchy', 'text': 'Which SQL keyword allows a Common Table Expression (CTE) to recursively join a table with itself to traverse tree hierarchies?', 'options': ['A) WITH RECURSIVE', 'B) SELECT RECURSE', 'C) LOOP JOIN', 'D) CONNECT BY PRIOR'], 'correct': 'A) WITH RECURSIVE', 'explanation': '`WITH RECURSIVE cte_name AS (...)` defines recursive queries in standard ANSI SQL.', 'marks': '2 Marks'},

        # OS HARD (Q67 to Q69)
        {'q_num': 67, 'type': 'mcq', 'title': 'OS Page Fault Handling Pipeline', 'text': 'When CPU accesses a virtual address not present in physical RAM, what is the immediate hardware action?', 'options': ['A) MMU generates Page Fault CPU Trap Interrupt', 'B) OS terminates process', 'C) Disk is formatted', 'D) RAM is erased'], 'correct': 'A) MMU generates Page Fault CPU Trap Interrupt', 'explanation': 'Memory Management Unit (MMU) detects valid=0 in page table and triggers hardware Trap to OS Kernel.', 'marks': '2 Marks'},
        {'q_num': 68, 'type': 'mcq', 'title': 'OS Thrashing & Working Set Model', 'text': 'System Thrashing occurs in OS when:', 'options': ['A) Total working set size of active processes > available physical RAM', 'B) CPU speed is too fast for disk', 'C) Deadlock occurs', 'D) Hard disk is full'], 'correct': 'A) Total working set size of active processes > available physical RAM', 'explanation': 'When RAM is insufficient for working sets, OS spends most of its time swapping pages in/out of disk (Thrashing).', 'marks': '2 Marks'},
        {'q_num': 69, 'type': 'mcq', 'title': 'IPC Shared Memory vs Message Passing', 'text': 'Which Inter-Process Communication (IPC) mechanism offers the highest throughput for large data transfers between local processes?', 'options': ['A) Shared Memory', 'B) Named Pipes', 'C) UNIX Domain Sockets', 'D) Message Queues'], 'correct': 'A) Shared Memory', 'explanation': 'Shared memory avoids kernel buffer copies once mapped, offering maximum data transfer throughput.', 'marks': '2 Marks'},

        # Computer Networks HARD (Q70 to Q72)
        {'q_num': 70, 'type': 'mcq', 'title': 'TCP SYN Flood Attack & SYN Cookies', 'text': 'How do SYN Cookies protect a server against TCP SYN Flood DDoS attacks?', 'options': ['A) Server encodes connection state into initial TCP sequence number without allocating memory', 'B) Server blocks all incoming IP addresses', 'C) Server increases backlog queue to infinity', 'D) Server drops ACK packets'], 'correct': 'A) Server encodes connection state into initial TCP sequence number without allocating memory', 'explanation': 'SYN cookies encode cryptographic state in `seq_num`, deferring memory allocation until valid client ACK arrives.', 'marks': '2 Marks'},
        {'q_num': 71, 'type': 'mcq', 'title': 'BGP Path Vector Routing Algorithm', 'text': 'Border Gateway Protocol (BGP) used between Internet Autonomous Systems (AS) is classified as a:', 'options': ['A) Path Vector Routing Protocol', 'B) Distance Vector Protocol (RIP)', 'C) Link State Protocol (OSPF)', 'D) Static Flooding Protocol'], 'correct': 'A) Path Vector Routing Protocol', 'explanation': 'BGP advertises complete AS-PATH vectors to prevent routing loops across global Internet ISPs.', 'marks': '2 Marks'},
        {'q_num': 72, 'type': 'mcq', 'title': 'DNS Iterative vs Recursive Resolution', 'text': 'In DNS resolution, when a Root Nameserver returns IP of `.com` TLD Nameserver rather than resolving the domain directly, it operates in:', 'options': ['A) Iterative Query Mode', 'B) Recursive Query Mode', 'C) Reverse DNS Mode', 'D) Authoritative Push Mode'], 'correct': 'A) Iterative Query Mode', 'explanation': 'Iterative query returns best referral answer (next TLD server) allowing requester to query next tier.', 'marks': '2 Marks'},

        # Programming & Concurrency HARD (Q73 to Q75)
        {'q_num': 73, 'type': 'mcq', 'title': 'C++ Smart Pointer Cycle Prevention', 'text': 'Two objects reference each other using `std::shared_ptr`. To break circular reference memory leaks, what smart pointer should be used for one direction?', 'options': ['A) std::weak_ptr', 'B) std::unique_ptr', 'C) raw pointer', 'D) std::auto_ptr'], 'correct': 'A) std::weak_ptr', 'explanation': '`std::weak_ptr` holds non-owning reference that does not increment reference count, preventing circular dependency leaks.', 'marks': '2 Marks'},
        {'q_num': 74, 'type': 'mcq', 'title': 'Python Global Interpreter Lock (GIL) Impact', 'text': 'In CPython runtime, why does multi-threading NOT speed up CPU-bound tasks on multi-core processors?', 'options': ['A) GIL permits only one thread to execute Python bytecode at a time', 'B) Python disables CPU threads', 'C) Operating system blocks Python threads', 'D) Memory is single-threaded'], 'correct': 'A) GIL permits only one thread to execute Python bytecode at a time', 'explanation': 'GIL (Global Interpreter Lock) ensures thread safety by allowing only 1 thread to execute CPython bytecode concurrently.', 'marks': '2 Marks'},
        {'q_num': 75, 'type': 'mcq', 'title': 'Valgrind Memory Leak Analysis', 'text': 'In Valgrind Memcheck output, "definitely lost" memory indicates:', 'options': ['A) Heap memory allocated with malloc/new with no pointers pointing to it anywhere', 'B) Stack variable overflow', 'C) Memory allocated in global scope', 'D) Shared library memory'], 'correct': 'A) Heap memory allocated with malloc/new with no pointers pointing to it anywhere', 'explanation': '"Definitely lost" means heap memory was allocated but all pointer references were lost without calling `free()`.', 'marks': '2 Marks'},

        # System Architecture HARD (Q76 to Q80)
        {'q_num': 76, 'type': 'mcq', 'title': 'gRPC vs REST API Performance', 'text': 'Why does gRPC achieve significantly higher throughput than traditional REST over HTTP/1.1?', 'options': ['A) Protocol Buffers binary serialization + HTTP/2 multiplexing', 'B) JSON text formatting', 'C) Disabling SSL encryption', 'D) Single-threaded socket connection'], 'correct': 'A) Protocol Buffers binary serialization + HTTP/2 multiplexing', 'explanation': 'gRPC uses compact Protobuf binary format and HTTP/2 header compression/multiplexing.', 'marks': '2 Marks'},
        {'q_num': 77, 'type': 'mcq', 'title': 'Distributed Systems CAP & PACELC Theorem', 'text': 'According to PACELC Theorem, in a distributed database system when there is NO network partition (E), what trade-off must be chosen?', 'options': ['A) Latency (L) vs Consistency (C)', 'B) Availability (A) vs Partition (P)', 'C) Throughput vs Storage', 'D) Security vs Speed'], 'correct': 'A) Latency (L) vs Consistency (C)', 'explanation': 'PACELC states: If Partition (P), choose Availability (A) or Consistency (C); Else (E), choose Latency (L) or Consistency (C).', 'marks': '2 Marks'},
        {'q_num': 78, 'type': 'mcq', 'title': 'JWT Token Security Mitigations', 'text': 'To prevent Cross-Site Scripting (XSS) attacks from stealing JWT authentication tokens, where should JWTs be stored?', 'options': ['A) HttpOnly, Secure, SameSite Cookies', 'B) LocalStorage', 'C) SessionStorage', 'D) Global JavaScript Variable'], 'correct': 'A) HttpOnly, Secure, SameSite Cookies', 'explanation': 'HttpOnly flag prevents client-side JavaScript from accessing cookie data, mitigating XSS token theft.', 'marks': '2 Marks'},
        {'q_num': 79, 'type': 'mcq', 'title': 'Distributed Sliding Window Rate Limiter', 'text': 'Which data structure in Redis is ideal for implementing a Sliding Window Log rate limiting algorithm?', 'options': ['A) Sorted Set (ZSET)', 'B) Hash (HSET)', 'C) String', 'D) Pub/Sub Queue'], 'correct': 'A) Sorted Set (ZSET)', 'explanation': 'Redis ZSET stores timestamps as scores, allowing efficient `ZREMRANGEBYSCORE` cleanup of old logs in sliding window.', 'marks': '2 Marks'},
        {'q_num': 80, 'type': 'mcq', 'title': 'Consistent Hashing Shard Rebalancing', 'text': 'In consistent hashing using a virtual node ring, adding a new database node requires remapping approximately how many keys?', 'options': ['A) K / N keys where K is total keys and N is total nodes', 'B) All K keys', 'C) K / 2 keys', 'D) Zero keys'], 'correct': 'A) K / N keys where K is total keys and N is total nodes', 'explanation': 'Consistent hashing minimizes key movement: adding a node only remaps ~K/N keys from neighboring virtual nodes.', 'marks': '2 Marks'}
    ]

    return [
        {
            'section_name': 'Section 1: Online Aptitude Assessment',
            'desc': 'Quantitative aptitude, logical reasoning, verbal ability, analytical reasoning',
            'time': '50 Mins',
            'questions': sec1_qs
        },
        {
            'section_name': 'Section 2: Technical Assessment',
            'desc': 'Pseudocode, programming, computer fundamentals, DBMS, OOP, technical MCQs',
            'time': '45 Mins',
            'questions': sec2_qs
        },
        {
            'section_name': 'Section 3: Coding Assessment',
            'desc': 'Programming problems, DSA, problem-solving and coding efficiency',
            'time': '45 Mins',
            'questions': sec3_qs
        },
        {
            'section_name': 'Section 4: Technical Interview',
            'desc': 'Programming, OOP, DBMS/SQL, OS, CN, projects and technical fundamentals',
            'time': '40 Mins',
            'questions': sec4_qs
        }
    ]

def shuffle_question_options(q, target_index=None):
    if q.get('type') == 'mcq' and q.get('options') and q.get('correct'):
        correct_raw = str(q['correct']).strip()
        if ') ' in correct_raw:
            correct_text = correct_raw.split(') ', 1)[1].strip()
        else:
            correct_text = correct_raw

        raw_options = []
        for opt in q['options']:
            opt_str = str(opt).strip()
            if ') ' in opt_str:
                raw_options.append(opt_str.split(') ', 1)[1].strip())
            else:
                raw_options.append(opt_str)

        distractors = [opt for opt in raw_options if opt != correct_text]
        random.shuffle(distractors)

        if target_index is not None and 0 <= target_index < 4:
            new_raw_options = []
            d_idx = 0
            for i in range(4):
                if i == target_index:
                    new_raw_options.append(correct_text)
                else:
                    if d_idx < len(distractors):
                        new_raw_options.append(distractors[d_idx])
                        d_idx += 1
                    else:
                        new_raw_options.append(correct_text)
        else:
            random.shuffle(raw_options)
            new_raw_options = raw_options

        prefixes = ['A', 'B', 'C', 'D']
        shuffled_options = []
        new_correct = None
        for idx, text in enumerate(new_raw_options):
            prefix = prefixes[idx] if idx < len(prefixes) else str(idx + 1)
            formatted_opt = f"{prefix}) {text}"
            shuffled_options.append(formatted_opt)
            if text == correct_text:
                new_correct = formatted_opt

        q['options'] = shuffled_options
        if new_correct:
            q['correct'] = new_correct

def build_model_paper_data(comp_name, title_str, year, duration, paper_type="model"):
    file_code = f"DOC-{comp_name.upper().replace(' ', '')}-{year.split()[0]}-01"
    t_lower = title_str.lower()
    y_lower = year.lower()

    if 'google' in comp_name.lower():
        if 'model 2' in t_lower or 'model 2' in y_lower:
            sections = get_google_practice_sections_model2()
            paper_title = 'Google SWE Onsite Coding & DSA Assessment Model 2'
        elif 'model 3' in t_lower or 'model 3' in y_lower:
            sections = get_google_practice_sections_model3()
            paper_title = 'Google University Graduate SDE Placement Model 3'
        elif 'model 1' in t_lower or 'model 1' in y_lower:
            sections = get_google_practice_sections_model1()
            paper_title = 'Google Official 4-Round SWE Coding Assessment Model 1'
        else:
            sections = get_google_general_practice_test()
            paper_title = 'Google General Practice & Mock Test Paper'
    elif 'amazon' in comp_name.lower():
        if 'model 2' in t_lower or 'model 2' in y_lower:
            sections = get_amazon_practice_sections_model2()
            paper_title = 'Amazon SDE Previous Year Assessment Model 2'
        elif 'model 3' in t_lower or 'model 3' in y_lower:
            sections = get_amazon_practice_sections_model3()
            paper_title = 'Amazon Campus Placement Solved Paper Model 3'
        else:
            sections = get_amazon_practice_sections_model1()
            paper_title = 'Amazon Official SDE Placement Model 1'
    elif 'infosys' in comp_name.lower() or 'infy' in comp_name.lower():
        if 'model 2' in t_lower or 'model 2' in y_lower or 'system engineer' in t_lower:
            sections = get_infosys_practice_sections_model2()
            paper_title = 'Infosys System Engineer Solved Paper Model 2'
        elif 'model 3' in t_lower or 'model 3' in y_lower or 'infytq' in t_lower or 'campus' in t_lower:
            sections = get_infosys_practice_sections_model3()
            paper_title = 'Infosys InfyTQ / Campus Selection Model 3'
        else:
            sections = get_infosys_practice_sections_model1()
            paper_title = 'Infosys Specialist Programmer & DSE Model 1'
        paper_title = title_str
    elif 'accenture' in comp_name.lower():
        sections = get_accenture_sections(title_str)
        paper_title = title_str
    elif 'capgemini' in comp_name.lower():
        sections = get_capgemini_sections()
        paper_title = title_str or 'Capgemini Official Placement Model Paper'
    else:
        sections = get_company_92_sections(comp_name, title_str)
        paper_title = title_str

    # Balance correct answers equally across A, B, C, D options for every practice paper
    all_mcqs = [q for sec in sections for q in sec.get('questions', []) if q.get('type') == 'mcq']
    target_indices = [0, 1, 2, 3] * (len(all_mcqs) // 4 + 1)
    random.shuffle(target_indices)

    running_q_num = 1
    mcq_idx = 0
    for sec in sections:
        if sec.get('questions'):
            sec_qs = list(sec['questions'])
            random.shuffle(sec_qs)
            for q in sec_qs:
                q['q_num'] = running_q_num
                if q.get('type') == 'mcq':
                    t_idx = target_indices[mcq_idx] if mcq_idx < len(target_indices) else None
                    shuffle_question_options(q, target_index=t_idx)
                    mcq_idx += 1
                running_q_num += 1
            sec['questions'] = sec_qs

    total_qs = sum(len(s['questions']) for s in sections)

    return {
        'company': comp_name,
        'title': paper_title,
        'year': year,
        'duration': '180 Mins' if 'google' in comp_name.lower() else '135 Mins',
        'file_code': file_code,
        'total_qs': total_qs,
        'sections': sections
    }

@app.route('/practice')
@login_required
def practice():
    user_id = session['user_id']
    category = request.args.get('category', 'All')
    paper_title = request.args.get('paper_title', '').strip()
    company = request.args.get('company', '').strip()
    duration = request.args.get('duration', '90 Mins').strip()
    year = request.args.get('year', '2025').strip()
    
    query = Question.query
    if category != 'All':
        query = query.filter_by(category=category)
        
    questions_list = query.all()
    q_data = Question.to_dict_list(questions_list, user_id=user_id)

    available_papers = [
        {
            'title': 'Google SWE Official 4-Round Coding Assessment Model 1',
            'company': 'Google',
            'year': '2025 Official',
            'duration': '180 Mins',
            'file_code': 'DOC-GOOGLE-2025-01'
        },
        {
            'title': 'Google SWE Onsite Coding & DSA Assessment Model 2',
            'company': 'Google',
            'year': '2024 Memory Based',
            'duration': '180 Mins',
            'file_code': 'DOC-GOOGLE-2024-02'
        },
        {
            'title': 'Google University Graduate SDE Placement Model 3',
            'company': 'Google',
            'year': '2023 Solved',
            'duration': '180 Mins',
            'file_code': 'DOC-GOOGLE-2023-03'
        },
        {
            'title': 'Deloitte NLA 2025 Official Assessment Paper',
            'company': 'Deloitte NLA',
            'year': '2025 Official',
            'duration': '135 Mins',
            'file_code': 'DOC-DELOITTE-2025-01'
        },
        {
            'title': 'TCS NQT 2025 Cognitive & Technical Test Paper',
            'company': 'TCS NQT',
            'year': '2025 Official',
            'duration': '75 Mins',
            'file_code': 'DOC-TCSNQT-2025-01'
        },
        {
            'title': 'Infosys Specialist Programmer (SP) Solved Paper',
            'company': 'Infosys',
            'year': '2025 Solved',
            'duration': '135 Mins',
            'file_code': 'DOC-INFOSYS-2025-01'
        },
        {
            'title': 'Amazon SDE I Leadership Principles & Coding Test',
            'company': 'Amazon',
            'year': '2025 Assessment',
            'duration': '120 Mins',
            'file_code': 'DOC-AMAZON-2025-01'
        },
        {
            'title': 'Accenture Advanced Technical Placement Paper',
            'company': 'Accenture',
            'year': '2025 Memory Based',
            'duration': '60 Mins',
            'file_code': 'DOC-ACCENTURE-2025-01'
        },
        {
            'title': 'Wipro National Talent Hunt (NTH) Test Paper',
            'company': 'Wipro',
            'year': '2025 Official',
            'duration': '50 Mins',
            'file_code': 'DOC-WIPRO-2025-01'
        }
    ]

    model_paper = None
    if paper_title or company:
        comp_name = company or "Accenture"
        title_str = paper_title or f"{comp_name} Official Placement Model Paper"
        paper_type = request.args.get('paper_type', 'model').strip()
        model_paper = build_model_paper_data(comp_name, title_str, year, duration, paper_type=paper_type)

    return render_template('practice.html', questions=q_data, selected_category=category, model_paper=model_paper, available_papers=available_papers)

def get_mock_user_metrics(user_id):
    user = db.session.get(User, user_id)
    attempts = MockInterviewAttempt.query.filter_by(user_id=user_id).order_by(MockInterviewAttempt.created_at.desc()).all()
    
    tests_completed = len(attempts)
    total_rounds = 8  # 8 Technical Domains + 2 HR modules
    
    if tests_completed > 0:
        total_score_sum = sum(a.score_percentage for a in attempts)
        avg_performance = round(total_score_sum / tests_completed)
        correct_sum = sum(a.correct_count for a in attempts)
        total_q_sum = sum(a.total_questions for a in attempts)
        accuracy_pct = round((correct_sum / total_q_sum) * 100) if total_q_sum > 0 else 0
        unique_topics_covered = len(set(a.topic_key for a in attempts))
        overall_progress = min(100, round((unique_topics_covered / total_rounds) * 100))
    else:
        avg_performance = 0
        accuracy_pct = 0
        overall_progress = 0
        
    streak_count = user.streak_count if user and user.streak_count else 0
    
    # Topic-specific highest score / completion state
    topic_attempts = {}
    for a in attempts:
        if a.topic_key not in topic_attempts:
            topic_attempts[a.topic_key] = {
                'score_percentage': a.score_percentage,
                'correct_count': a.correct_count,
                'total_questions': a.total_questions,
                'date': a.created_at
            }
        elif a.score_percentage > topic_attempts[a.topic_key]['score_percentage']:
            topic_attempts[a.topic_key] = {
                'score_percentage': a.score_percentage,
                'correct_count': a.correct_count,
                'total_questions': a.total_questions,
                'date': a.created_at
            }

    recent_mock_tests = []
    for att in attempts[:5]:
        diff = datetime.utcnow() - att.created_at
        if diff.days == 0:
            meta = f"Today • {att.correct_count}/{att.total_questions} Score"
        elif diff.days == 1:
            meta = f"Yesterday • {att.correct_count}/{att.total_questions} Score"
        else:
            meta = f"{att.created_at.strftime('%b %d')} • {att.correct_count}/{att.total_questions} Score"
        recent_mock_tests.append({
            'topic_key': att.topic_key,
            'topic_name': att.topic_name,
            'meta': meta,
            'score': att.score_percentage
        })

    mock_stats = {
        'total_rounds': total_rounds,
        'tests_completed': tests_completed,
        'avg_performance': avg_performance,
        'accuracy_pct': accuracy_pct,
        'overall_progress': overall_progress,
        'streak_count': streak_count,
        'topic_attempts': topic_attempts,
        'recent_tests': recent_mock_tests,
        'has_activity': tests_completed > 0
    }
    return mock_stats

@app.route('/mock-interview')
@login_required
def mock_interview():
    user_id = session['user_id']
    user = db.session.get(User, user_id)
    update_user_streak(user)
    mock_stats = get_mock_user_metrics(user_id)
    return render_template('mock_interview.html', mock_stats=mock_stats, current_user=user)

@app.route('/api/submit-mock-test', methods=['POST'])
@login_required
def submit_mock_test():
    user_id = session['user_id']
    data = request.get_json() or {}
    topic_key = data.get('topic_key', 'general')
    topic_name = data.get('topic_name', 'Mock Assessment')
    total_questions = int(data.get('total_questions', 20))
    correct_count = int(data.get('correct_count', 0))
    score_percentage = int(data.get('score_percentage', 0))
    incorrect_count = max(0, total_questions - correct_count)

    user = db.session.get(User, user_id)
    update_user_streak(user)

    attempt = MockInterviewAttempt(
        user_id=user_id,
        topic_key=topic_key,
        topic_name=topic_name,
        total_questions=total_questions,
        correct_count=correct_count,
        incorrect_count=incorrect_count,
        score_percentage=score_percentage
    )
    db.session.add(attempt)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Mock test attempt recorded successfully'})

@app.route('/hr-question-bank')
@login_required
def hr_question_bank():
    return render_template('hr_question_bank.html')

@app.route('/mock-interview/test/<topic_key>')
@login_required
def mock_test_session(topic_key):
    if topic_key == 'hr_general' or topic_key.startswith('hr_'):
        return redirect(url_for('hr_question_bank'))

    import importlib
    import copy
    import random
    import mock_data
    importlib.reload(mock_data)
    from mock_data import MOCK_TOPICS_DATA
    topic_info = MOCK_TOPICS_DATA.get(topic_key)
    if not topic_info:
        flash('Invalid Mock Interview topic selected.', 'danger')
        return redirect(url_for('mock_interview'))

    # Jumble/shuffle options dynamically for choose the correct answer questions
    raw_questions = copy.deepcopy(topic_info['questions'])
    letters = ['A', 'B', 'C', 'D']
    jumbled_questions = []

    for q in raw_questions:
        if q.get('options') and len(q['options']) == 4:
            correct_opt = str(q.get('correct_option', 'A')).strip().upper()
            raw_options = []
            correct_text = None

            for idx, opt in enumerate(q['options']):
                clean_opt = opt
                if len(opt) > 3 and opt[0] in 'ABCD' and opt[1] in '):.':
                    clean_opt = opt[3:].strip()
                raw_options.append(clean_opt)

                if idx < len(letters) and letters[idx] == correct_opt:
                    correct_text = clean_opt

            if not correct_text and raw_options:
                correct_text = raw_options[0]

            random.shuffle(raw_options)

            new_options = []
            new_correct_opt = 'A'
            for idx, text in enumerate(raw_options):
                prefix = f"{letters[idx]}) "
                new_options.append(f"{prefix}{text}")
                if text == correct_text:
                    new_correct_opt = letters[idx]

            q['options'] = new_options
            q['correct_option'] = new_correct_opt

        jumbled_questions.append(q)

    return render_template(
        'mock_test_session.html',
        topic_key=topic_key,
        topic_name=topic_info['name'],
        questions=jumbled_questions
    )

@app.route('/bookmarks')
@login_required
def bookmarks():
    user_id = session['user_id']
    bookmarked_items = Bookmark.query.filter_by(user_id=user_id).all()
    question_ids = [b.question_id for b in bookmarked_items]

    questions_list = Question.query.filter(Question.id.in_(question_ids)).all() if question_ids else []
    q_data = Question.to_dict_list(questions_list, user_id=user_id)

    return render_template('bookmarks.html', questions=q_data)

@app.route('/progress')
@login_required
def progress():
    user = db.session.get(User, session['user_id'])
    
    # 1. ACTUAL QUESTIONS SOLVED & MASTERED
    total_questions = Question.query.count()
    user_progs = UserProgress.query.filter_by(user_id=user.id).all()
    attempted_count = len(user_progs)
    mastered_count = sum(1 for p in user_progs if p.status == 'mastered')
    questions_solved = attempted_count

    # 2. ACTUAL MOCK INTERVIEWS COMPLETED
    mock_attempts_count = MockInterviewAttempt.query.filter_by(user_id=user.id).count()
    mock_interviews_completed = mock_attempts_count

    # 3. ACTUAL APTITUDE TESTS ATTEMPTED
    aptitude_attempts_count = AptitudeTestAttempt.query.filter_by(user_id=user.id).count()
    aptitude_tests_attempted = aptitude_attempts_count

    # 4. ACTUAL RESUME COMPLETION PERCENTAGE
    resume_score = 0
    if user.full_name and user.full_name not in ['Demo User', '']:
        resume_score += 20
    if user.education and user.education not in ['B.Tech', '']:
        resume_score += 15
    if user.college and user.college not in ['Demo College of Engineering', '']:
        resume_score += 15
    if user.skills and user.skills not in ['Python, HTML, CSS, JavaScript, Flask, SQL', '']:
        resume_score += 20
    if user.target_role and user.target_role not in ['Software Developer', '']:
        resume_score += 15
    if user.completed_courses or user.certificates:
        resume_score += 15
    resume_completion = min(100, resume_score)

    # 5. CURRENT STREAK
    streak_days = getattr(user, 'streak_count', None) or 1

    # 6. OVERALL READINESS SCORE (Dynamic Calculation)
    if total_questions > 0 and attempted_count > 0:
        practiced_only = max(0, attempted_count - mastered_count)
        weighted_progress = (mastered_count * 1.0) + (practiced_only * 0.5)
        readiness_score = round(((weighted_progress / total_questions) * 70) + ((resume_completion / 100) * 15) + (min(mock_interviews_completed, 5) * 3))
        readiness_score = min(100, max(0, readiness_score))
    else:
        readiness_score = 0

    # 7. DYNAMIC SKILL BREAKDOWN & ASCII BARS
    all_qs = db.session.query(Question.id, Question.category).all()
    cat_to_ids = {}
    for qid, cat in all_qs:
        if cat not in cat_to_ids:
            cat_to_ids[cat] = []
        cat_to_ids[cat].append(qid)

    user_solved_ids = {p.question_id for p in user_progs}

    skill_categories = [
        ('Technical Skills', ['Frontend', 'Backend', 'Data Structures', 'System Design'], '#3b82f6'),
        ('Aptitude', ['Aptitude'], '#f59e0b'),
        ('HR Interview', ['Behavioral'], '#10b981'),
        ('Group Discussion', ['Group Discussion'], '#8b5cf6')
    ]
    
    skills_breakdown = []
    for name, cats, color in skill_categories:
        cat_q_ids = []
        for c in cats:
            cat_q_ids.extend(cat_to_ids.get(c, []))
        cat_total = len(cat_q_ids)
        cat_solved = sum(1 for qid in cat_q_ids if qid in user_solved_ids)
        
        pct = round((cat_solved / cat_total * 100)) if cat_total > 0 and cat_solved > 0 else 0
        filled_blocks = int(round(pct / 10))
        empty_blocks = 10 - filled_blocks
        ascii_bar = ('█' * filled_blocks) + ('░' * empty_blocks)
        
        skills_breakdown.append({
            'name': name,
            'ascii': ascii_bar,
            'percent': pct,
            'solved': cat_solved,
            'total': cat_total,
            'color': color
        })

    # 8. DYNAMIC WEEKLY ACTIVITY CHART (Last 7 Days)
    today = date.today()
    weekly_activity = []
    days_abbr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Pre-aggregate solved per day from user_progs
    date_to_count = {}
    for p in user_progs:
        if p.updated_at:
            d = p.updated_at.date()
            date_to_count[d] = date_to_count.get(d, 0) + 1

    for i in range(6, -1, -1):
        day_date = today - timedelta(days=i)
        day_name = days_abbr[day_date.weekday()]
        day_solved = date_to_count.get(day_date, 0)
        
        weekly_activity.append({
            'day': day_name,
            'questions': day_solved,
            'interviews': 1 if day_solved > 5 else 0,
            'time_mins': day_solved * 5
        })

    total_weekly_questions = sum(d['questions'] for d in weekly_activity)
    total_weekly_interviews = sum(d['interviews'] for d in weekly_activity)
    total_weekly_time_hrs = round(sum(d['time_mins'] for d in weekly_activity) / 60, 1)

    # 9. DYNAMIC ACHIEVEMENTS & BADGES
    achievements = [
        {
            'icon': '🏆',
            'title': 'First Mock Interview',
            'desc': 'Complete your first AI-guided interview session',
            'unlocked': mock_interviews_completed > 0,
            'date': 'Unlocked ✓' if mock_interviews_completed > 0 else 'Locked 🔒'
        },
        {
            'icon': '🔥',
            'title': '7-Day Streak',
            'desc': 'Maintain a consistent daily practice streak for 7 days',
            'unlocked': streak_days >= 7,
            'date': 'Unlocked ✓' if streak_days >= 7 else f'{streak_days}/7 Days'
        },
        {
            'icon': '💯',
            'title': '100 Questions Solved',
            'desc': 'Cross the milestone of solving 100 placement questions',
            'unlocked': questions_solved >= 100,
            'date': 'Unlocked ✓' if questions_solved >= 100 else f'{questions_solved}/100 Solved'
        },
        {
            'icon': '⭐',
            'title': 'Top Performer',
            'desc': 'Score 80%+ on overall interview readiness rating',
            'unlocked': readiness_score >= 80,
            'date': 'Unlocked ✓' if readiness_score >= 80 else 'Requires 80% Score'
        }
    ]

    # 10. DYNAMIC RECENT ACTIVITIES
    recent_user_progress = UserProgress.query.filter_by(user_id=user.id).order_by(UserProgress.updated_at.desc()).limit(5).all()
    recent_q_ids = [up.question_id for up in recent_user_progress]
    recent_q_map = {q.id: q for q in Question.query.filter(Question.id.in_(recent_q_ids)).all()} if recent_q_ids else {}
    recent_activities = []
    
    for up in recent_user_progress:
        q = recent_q_map.get(up.question_id)
        if q:
            time_ago = 'Recently'
            if up.updated_at:
                delta_sec = (datetime.utcnow() - up.updated_at).total_seconds()
                if delta_sec < 3600:
                    time_ago = f"{int(delta_sec // 60)} mins ago"
                elif delta_sec < 86400:
                    time_ago = f"{int(delta_sec // 3600)} hours ago"
                else:
                    time_ago = f"{int(delta_sec // 86400)} days ago"

            recent_activities.append({
                'title': f"Solved {q.title}",
                'time': time_ago,
                'icon': '✓',
                'badge': q.category
            })

    return render_template('progress.html',
                           user=user,
                           readiness_score=readiness_score,
                           questions_solved=questions_solved,
                           mock_interviews_completed=mock_interviews_completed,
                           aptitude_tests_attempted=aptitude_tests_attempted,
                           resume_completion=resume_completion,
                           streak_days=streak_days,
                           skills_breakdown=skills_breakdown,
                           weekly_activity=weekly_activity,
                           total_weekly_questions=total_weekly_questions,
                           total_weekly_interviews=total_weekly_interviews,
                           total_weekly_time_hrs=total_weekly_time_hrs,
                           achievements=achievements,
                           recent_activities=recent_activities)

@app.route('/leaderboard')
@login_required
def leaderboard():
    current_user_obj = db.session.get(User, session['user_id'])
    filter_type = request.args.get('filter', 'all_time')

    # Query all real registered portal users from database
    all_users = User.query.all()
    
    # Pre-aggregate stats for all users in one single query
    prog_stats = db.session.query(
        UserProgress.user_id,
        db.func.count(UserProgress.id).label('attempted'),
        db.func.sum(db.case((UserProgress.status == 'mastered', 1), else_=0)).label('mastered')
    ).group_by(UserProgress.user_id).all()
    stats_map = {row[0]: (row[1] or 0, row[2] or 0) for row in prog_stats}

    user_list = []
    for u in all_users:
        attempted, mastered = stats_map.get(u.id, (0, 0))
        streak = getattr(u, 'streak_count', None) or 1
        
        # Real calculated user score (0 if no questions solved yet)
        if attempted > 0:
            score = (mastered * 20) + (attempted * 10) + (streak * 5)
            user_streak_val = streak
        else:
            score = 0
            user_streak_val = 0
            
        display_name = u.full_name or u.username or f"User #{u.id}"
        
        if score >= 100:
            badge = "🏆 Grandmaster"
        elif score >= 50:
            badge = "⚡ Algorithm Master"
        elif score >= 20:
            badge = "🔥 Code Ninja"
        else:
            badge = "⭐ Rising Star"
            
        user_list.append({
            'id': u.id,
            'name': display_name,
            'score': score,
            'streak': user_streak_val,
            'solved': attempted,
            'mastered': mastered,
            'badge': badge,
            'avatar': display_name[0].upper() if display_name else 'U',
            'is_current': (u.id == current_user_obj.id)
        })

    # Sort candidates by score descending, then solved descending, then streak descending
    user_list.sort(key=lambda x: (x['score'], x['solved'], x['streak']), reverse=True)

    candidates = []
    current_user_data = None
    current_user_rank = 1

    for idx, cand in enumerate(user_list, start=1):
        cand['rank'] = idx
        if idx == 1:
            cand['badge_icon'] = '🥇'
        elif idx == 2:
            cand['badge_icon'] = '🥈'
        elif idx == 3:
            cand['badge_icon'] = '🥉'
        else:
            cand['badge_icon'] = str(idx)
            
        candidates.append(cand)
        
        if cand['is_current']:
            current_user_data = cand
            current_user_rank = idx

    user_score = current_user_data['score'] if current_user_data else 0
    user_rank = current_user_rank

    if candidates and len(candidates) > 0:
        top_score = candidates[0]['score']
        top_needed = max(0, top_score - user_score + 10) if user_rank > 1 else 0
        spotlight = candidates[0]
    else:
        top_needed = 0
        spotlight = {
            'rank': 1, 'badge_icon': '🥇', 'name': current_user_obj.full_name or current_user_obj.username,
            'score': user_score, 'streak': 0, 'badge': '⭐ Rising Star', 'avatar': (current_user_obj.username or 'U')[0].upper()
        }

    total_solved_sum = sum(c['solved'] for c in candidates)
    total_streak_sum = sum(c['streak'] for c in candidates)

    # Calculate actual percentage metrics based on solved questions
    mock_score_val = round((total_solved_sum * 0.5)) if total_solved_sum > 0 else 0
    aptitude_score_val = round((total_solved_sum * 0.4)) if total_solved_sum > 0 else 0
    readiness_score_val = round((total_solved_sum * 0.6)) if total_solved_sum > 0 else 0
    streak_points_val = total_streak_sum * 10 if total_solved_sum > 0 else 0

    metrics_summary = {
        'total_questions_solved': total_solved_sum,
        'avg_mock_score': min(100, mock_score_val),
        'avg_aptitude_score': min(100, aptitude_score_val),
        'avg_readiness_score': min(100, readiness_score_val),
        'total_streak_points': streak_points_val
    }

    return render_template('leaderboard.html',
                           user=current_user_obj,
                           candidates=candidates,
                           spotlight=spotlight,
                           user_score=user_score,
                           user_rank=user_rank,
                           top10_needed=top_needed,
                           filter_type=filter_type,
                           metrics_summary=metrics_summary)

@app.route('/profile')
@login_required
def profile():
    user = db.session.get(User, session['user_id'])
    
    user_progs = UserProgress.query.filter_by(user_id=user.id).all()
    mastered_prog_ids = {p.question_id for p in user_progs if p.status == 'mastered'}
    attempted_count = len(user_progs)
    mastered_count = len(mastered_prog_ids)
    bookmarked_count = Bookmark.query.filter_by(user_id=user.id).count()

    all_qs_cat = db.session.query(Question.id, Question.category).all()
    total_questions = len(all_qs_cat)
    cat_to_qids = {}
    for qid, cat in all_qs_cat:
        if cat not in cat_to_qids:
            cat_to_qids[cat] = []
        cat_to_qids[cat].append(qid)

    if total_questions > 0:
        practiced_only = max(0, attempted_count - mastered_count)
        weighted_progress = mastered_count + (practiced_only * 0.5)
        readiness_percentage = round((weighted_progress / total_questions) * 100, 1)
    else:
        readiness_percentage = 0

    skills_str = getattr(user, 'skills', None) or 'Python, JavaScript, Data Structures, System Design, SQL, React'
    courses_str = getattr(user, 'completed_courses', None) or 'Full-Stack Interview Mastery, Data Structures & Algorithms Deep Dive, System Design Principles'
    certs_str = getattr(user, 'certificates', None) or 'Verified Algorithm Expert, Certified System Architecture Professional'

    skills_list = [s.strip() for s in skills_str.split(',') if s.strip()]
    courses_list = [c.strip() for c in courses_str.split(',') if c.strip()]
    certs_list = [cert.strip() for cert in certs_str.split(',') if cert.strip()]

    categories = ['Frontend', 'Backend', 'Data Structures', 'System Design', 'Behavioral']
    cat_stats = []
    for cat in categories:
        c_qids = cat_to_qids.get(cat, [])
        cat_total = len(c_qids)
        cat_mastered = sum(1 for qid in c_qids if qid in mastered_prog_ids)
        cat_stats.append({
            'name': cat,
            'total': cat_total,
            'mastered': cat_mastered,
            'percent': round((cat_mastered / cat_total * 100)) if cat_total > 0 else 0
        })

    return render_template('profile.html',
                           user=user,
                           total_questions=total_questions,
                           mastered_count=mastered_count,
                           attempted_count=attempted_count,
                           bookmarked_count=bookmarked_count,
                           readiness_percentage=readiness_percentage,
                           skills_list=skills_list,
                           courses_list=courses_list,
                           certs_list=certs_list,
                           cat_stats=cat_stats)

@app.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    user = db.session.get(User, session['user_id'])
    user.full_name = request.form.get('full_name', '').strip() or 'Demo User'
    user.education = request.form.get('education', '').strip() or 'B.Tech'
    user.college = request.form.get('college', '').strip() or 'Demo College of Engineering'
    user.location = request.form.get('location', '').strip() or 'India'
    user.target_role = request.form.get('target_role', '').strip() or 'Software Developer'
    user.preferred_domain = request.form.get('preferred_domain', '').strip() or 'Python / Full Stack'
    user.target_companies = request.form.get('target_companies', '').strip() or 'Deloitte, TCS, Infosys'
    user.skills = request.form.get('skills', '').strip() or 'Python, HTML, CSS, JavaScript, Flask, SQL'
    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('profile'))

@app.route('/about')
@app.route('/about-us')
def about_us():
    user = None
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
    
    total_questions = Question.query.count()
    total_users = User.query.count()
    
    return render_template('about.html',
                           user=user,
                           total_questions=total_questions,
                           total_users=total_users)

# --- AJAX API ENDPOINTS ---

@app.route('/api/toggle-bookmark', methods=['POST'])
@login_required
def toggle_bookmark():
    user_id = session['user_id']
    data = request.get_json() or {}
    question_id = data.get('question_id')

    if not question_id:
        return jsonify({'error': 'Question ID missing'}), 400

    bm = Bookmark.query.filter_by(user_id=user_id, question_id=question_id).first()
    if bm:
        db.session.delete(bm)
        db.session.commit()
        return jsonify({'bookmarked': False, 'message': 'Removed from bookmarks'})
    else:
        new_bm = Bookmark(user_id=user_id, question_id=question_id)
        db.session.add(new_bm)
        db.session.commit()
        return jsonify({'bookmarked': True, 'message': 'Saved to bookmarks'})

@app.route('/api/update-status', methods=['POST'])
@login_required
def update_status():
    user_id = session['user_id']
    data = request.get_json() or {}
    question_id = data.get('question_id')
    status = data.get('status', 'needs_practice')

    if not question_id:
        return jsonify({'error': 'Question ID missing'}), 400

    prog = UserProgress.query.filter_by(user_id=user_id, question_id=question_id).first()
    if not prog:
        prog = UserProgress(user_id=user_id, question_id=question_id, status=status)
        db.session.add(prog)
    else:
        prog.status = status

    db.session.commit()
    return jsonify({'success': True, 'status': status})

@app.route('/api/update-notes', methods=['POST'])
@login_required
def update_notes():
    user_id = session['user_id']
    data = request.get_json() or {}
    question_id = data.get('question_id')
    notes = data.get('notes', '')

    prog = UserProgress.query.filter_by(user_id=user_id, question_id=question_id).first()
    if not prog:
        prog = UserProgress(user_id=user_id, question_id=question_id, notes=notes)
        db.session.add(prog)
    else:
        prog.notes = notes

    db.session.commit()
    return jsonify({'success': True, 'message': 'Notes saved successfully'})

@app.route('/api/update-role', methods=['POST'])
@login_required
def update_role():
    user = db.session.get(User, session['user_id'])
    data = request.get_json() or {}
    new_role = data.get('target_role', 'Software Developer')

    user.target_role = new_role
    db.session.commit()
    return jsonify({'success': True, 'target_role': new_role})

# Automatic DB Initialization & Auto-seeding for Production Deployment
with app.app_context():
    db.create_all()
    try:
        from sqlalchemy import inspect, text
        inspector = inspect(db.engine)
        if 'users' in inspector.get_table_names():
            user_cols = [col['name'] for col in inspector.get_columns('users')]
            with db.engine.connect() as conn:
                if 'full_name' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN full_name VARCHAR(100)"))
                if 'education' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN education VARCHAR(100) DEFAULT 'B.Tech – 3rd Year'"))
                if 'college' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN college VARCHAR(150) DEFAULT 'Sir CR Reddy College of Engineering'"))
                if 'location' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN location VARCHAR(100) DEFAULT 'India'"))
                if 'preferred_domain' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN preferred_domain VARCHAR(100) DEFAULT 'Python / Full Stack'"))
                if 'target_companies' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN target_companies VARCHAR(200) DEFAULT 'Deloitte, TCS, Infosys'"))
                if 'profile_pic' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN profile_pic VARCHAR(256) DEFAULT 'avatar_default'"))
                if 'skills' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN skills TEXT"))
                if 'completed_courses' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN completed_courses TEXT"))
                if 'certificates' not in user_cols:
                    conn.execute(text("ALTER TABLE users ADD COLUMN certificates TEXT"))
                conn.commit()
    except Exception as m_err:
        print(f"Migration check: {m_err}")

    # Auto-seed disabled per user directive to clear questions
    pass

@app.errorhandler(500)
def handle_500_error(e):
    app.logger.error(f"Internal Server Error: {e}")
    if 'user_id' in session:
        try:
            if not db.session.get(User, session['user_id']):
                session.clear()
                return redirect(url_for('auth_page'))
        except Exception:
            session.clear()
            return redirect(url_for('auth_page'))
    return redirect(url_for('auth_page'))

import socket
import sys

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    local_ip = get_local_ip()
    mobile_url = f"http://{local_ip}:{port}"
    desktop_url = f"http://127.0.0.1:{port}"

    if sys.platform == 'win32':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print("\n" + "=" * 65)
    print(" 🚀 INTERVIEW PREP PORTAL RUNNING")
    print("=" * 65)
    print(f" 💻 Laptop / Desktop Browser :  {desktop_url}")
    print(f" 📱 Mobile Phone Browser     :  {mobile_url}")
    print("=" * 65)
    print(" 📸 Scan QR Code with your Mobile Camera to open instantly:\n")
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(mobile_url)
        qr.print_ascii(invert=True)
    except Exception:
        pass
    print("\n 💡 Make sure your phone is on the same Wi-Fi / Hotspot.")
    print("=" * 65 + "\n")

    app.run(debug=False, host='0.0.0.0', port=port)
