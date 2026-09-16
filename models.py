from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    full_name = db.Column(db.String(100), nullable=True, default='Demo User')
    education = db.Column(db.String(100), nullable=True, default='B.Tech')
    college = db.Column(db.String(150), nullable=True, default='Demo College of Engineering')
    location = db.Column(db.String(100), nullable=True, default='India')
    preferred_domain = db.Column(db.String(100), nullable=True, default='Python / Full Stack')
    target_companies = db.Column(db.String(200), nullable=True, default='Deloitte, TCS, Infosys')
    profile_pic = db.Column(db.String(256), nullable=True, default='avatar_default')
    skills = db.Column(db.Text, nullable=True, default='Python, HTML, CSS, JavaScript, Flask, SQL')
    completed_courses = db.Column(db.Text, nullable=True, default='Full-Stack Interview Mastery, Data Structures & Algorithms Deep Dive, System Design Principles')
    certificates = db.Column(db.Text, nullable=True, default='Verified Algorithm Expert, Certified System Architecture Professional')
    target_role = db.Column(db.String(64), default='Software Developer')
    streak_count = db.Column(db.Integer, default=1)
    last_active_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    progress_entries = db.relationship('UserProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    bookmarks = db.relationship('Bookmark', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'target_role': self.target_role,
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), nullable=False, index=True)  # Frontend, Backend, System Design, Data Structures, Behavioral, Aptitude
    sub_category = db.Column(db.String(64), nullable=True, index=True) # Number & Arithmetic, Commercial Mathematics, Time-Based Problems
    topic = db.Column(db.String(64), nullable=True, index=True)        # Number System, Profit & Loss, Boats & Streams, etc.
    title = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)  # Easy, Medium, Hard
    question_text = db.Column(db.Text, nullable=False)
    sample_answer = db.Column(db.Text, nullable=False)
    tips = db.Column(db.Text, nullable=True)
    star_guide = db.Column(db.Text, nullable=True)  # For behavioral questions
    options = db.Column(db.Text, nullable=True)          # JSON string of options list
    correct_option = db.Column(db.String(10), nullable=True) # A, B, C, or D

    def get_options_list(self):
        import json
        if self.options:
            try:
                opts = json.loads(self.options)
                if opts:
                    return opts
            except Exception:
                pass
        if self.star_guide:
            try:
                sg = json.loads(self.star_guide)
                if isinstance(sg, dict) and 'options' in sg:
                    return sg['options']
            except Exception:
                pass
        return []

    def get_correct_option(self):
        if self.correct_option:
            return self.correct_option
        if self.star_guide:
            try:
                import json
                sg = json.loads(self.star_guide)
                if isinstance(sg, dict) and 'correct_option' in sg:
                    return sg['correct_option']
            except Exception:
                pass
        return 'A'

    def to_dict(self, user_id=None, progress_map=None, bookmark_map=None):
        data = {
            'id': self.id,
            'category': self.category,
            'sub_category': self.sub_category,
            'topic': self.topic,
            'title': self.title,
            'difficulty': self.difficulty,
            'question_text': self.question_text,
            'sample_answer': self.sample_answer,
            'tips': self.tips,
            'star_guide': self.star_guide,
            'options': self.get_options_list(),
            'correct_option': self.get_correct_option()
        }
        if user_id:
            if progress_map is not None or bookmark_map is not None:
                p_info = (progress_map or {}).get(self.id)
                data['status'] = p_info.status if p_info else 'unattempted'
                data['user_notes'] = p_info.notes if (p_info and p_info.notes) else ''
                data['is_bookmarked'] = bool((bookmark_map or {}).get(self.id))
            else:
                progress = UserProgress.query.filter_by(user_id=user_id, question_id=self.id).first()
                bookmark = Bookmark.query.filter_by(user_id=user_id, question_id=self.id).first()
                data['status'] = progress.status if progress else 'unattempted'
                data['user_notes'] = progress.notes if progress else ''
                data['is_bookmarked'] = bool(bookmark)
        return data

    @classmethod
    def to_dict_list(cls, questions, user_id=None):
        if not questions:
            return []
        if not user_id:
            return [q.to_dict() for q in questions]

        q_ids = [q.id for q in questions]
        user_progs = UserProgress.query.filter(
            UserProgress.user_id == user_id,
            UserProgress.question_id.in_(q_ids)
        ).all()
        user_bookmarks = Bookmark.query.filter(
            Bookmark.user_id == user_id,
            Bookmark.question_id.in_(q_ids)
        ).all()

        progress_map = {p.question_id: p for p in user_progs}
        bookmark_map = {b.question_id: True for b in user_bookmarks}

        return [q.to_dict(user_id=user_id, progress_map=progress_map, bookmark_map=bookmark_map) for q in questions]

class UserProgress(db.Model):
    __tablename__ = 'user_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False, index=True)
    status = db.Column(db.String(20), default='needs_practice', index=True)  # needs_practice, mastered
    notes = db.Column(db.Text, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('user_id', 'question_id', name='_user_question_prog_uc'),)

class Bookmark(db.Model):
    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('user_id', 'question_id', name='_user_question_uc'),)

class AptitudeTestAttempt(db.Model):
    __tablename__ = 'aptitude_test_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    test_title = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=True)
    total_questions = db.Column(db.Integer, default=10)
    correct_count = db.Column(db.Integer, default=0)
    incorrect_count = db.Column(db.Integer, default=0)
    score_percentage = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class MockInterviewAttempt(db.Model):
    __tablename__ = 'mock_interview_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    topic_key = db.Column(db.String(100), nullable=False)
    topic_name = db.Column(db.String(100), nullable=False)
    total_questions = db.Column(db.Integer, default=20)
    correct_count = db.Column(db.Integer, default=0)
    incorrect_count = db.Column(db.Integer, default=0)
    score_percentage = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class EmailVerificationOTP(db.Model):
    __tablename__ = 'email_verification_otps'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, index=True)
    otp_code = db.Column(db.String(10), nullable=False)
    purpose = db.Column(db.String(32), default='register')  # 'register', 'reset_password'
    is_used = db.Column(db.Boolean, default=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def is_valid(self):
        return (not self.is_used) and (datetime.utcnow() <= self.expires_at)


