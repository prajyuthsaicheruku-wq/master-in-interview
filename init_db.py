"""
Database Initialization & Management Script for Interview Portal
Creates tables, applies schema migrations, seeds default users, and populates all curated questions.
"""

import os
import sys
import argparse
import subprocess
import glob
from datetime import datetime
from models import db, User, Question, UserProgress, Bookmark

def get_app():
    from app import app
    return app

def ensure_instance_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    instance_dir = os.path.join(base_dir, 'instance')
    os.makedirs(instance_dir, exist_ok=True)
    return instance_dir

def create_tables(app, reset=False):
    with app.app_context():
        if reset:
            print("[*] Dropping existing tables...")
            db.drop_all()
        print("[*] Creating database schema tables...")
        db.create_all()
        print("[OK] Schema tables created successfully.")

def ensure_users(app):
    with app.app_context():
        # Demo User
        demo_user = User.query.filter_by(username='demo').first()
        if not demo_user:
            demo_user = User(
                username='demo',
                email='demo@example.com',
                full_name='Demo Candidate',
                education='B.Tech - Computer Science',
                college='National Institute of Technology',
                location='India',
                preferred_domain='Full Stack Web Development',
                target_companies='Google, Microsoft, Amazon, TCS, Infosys',
                target_role='Software Engineer',
                skills='Python, JavaScript, Flask, React, SQL, Algorithms',
                completed_courses='Data Structures Deep Dive, Full-Stack Mastery, System Design Fundamentals',
                certificates='Certified Python Developer, Algorithms Specialist'
            )
            demo_user.set_password('password123')
            db.session.add(demo_user)
            print("[+] Created demo user (Username: 'demo', Password: 'password123').")
        else:
            print("[i] Demo user 'demo' already exists.")

        # Admin User
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            admin_user = User(
                username='admin',
                email='admin@interviewportal.local',
                full_name='Portal Administrator',
                education='M.Tech - Computer Science',
                college='Indian Institute of Technology',
                location='India',
                preferred_domain='System Architecture & Engineering',
                target_companies='Tier-1 Tech Companies',
                target_role='Lead System Architect',
                skills='Python, Go, System Design, Distributed Systems, SQL, Cloud Architecture',
                completed_courses='Enterprise Architecture, Advanced Distributed Systems',
                certificates='Master Architect, Cloud Solutions Architect'
            )
            admin_user.set_password('admin123')
            db.session.add(admin_user)
            print("[+] Created admin user (Username: 'admin', Password: 'admin123').")
        else:
            print("[i] Admin user 'admin' already exists.")

        db.session.commit()

def seed_core_questions(app):
    with app.app_context():
        try:
            from seed import SEED_QUESTIONS
            print(f"[*] Seeding {len(SEED_QUESTIONS)} core Frontend & Behavioral questions...")
            for q_data in SEED_QUESTIONS:
                existing = Question.query.filter_by(
                    title=q_data['title'],
                    category=q_data['category']
                ).first()
                if not existing:
                    q = Question(**q_data)
                    db.session.add(q)
            db.session.commit()
            print("[OK] Core questions seeded.")
        except Exception as e:
            print(f"[!] Error seeding core questions: {e}")

def seed_all_specialized_topics():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    seed_files = sorted(glob.glob(os.path.join(base_dir, 'seed_*.py')))
    print(f"\n[*] Running {len(seed_files)} specialized topic seed scripts...")
    
    success_count = 0
    for sf in seed_files:
        script_name = os.path.basename(sf)
        try:
            res = subprocess.run([sys.executable, sf], capture_output=True, text=True, cwd=base_dir)
            if res.returncode == 0:
                success_count += 1
                print(f"  [+] {script_name}")
            else:
                print(f"  [-] {script_name} failed: {res.stderr.strip()[:100]}")
        except Exception as err:
            print(f"  [-] {script_name} error: {err}")

    print(f"[OK] Finished running topic seeders ({success_count}/{len(seed_files)} successful).\n")

def print_database_status(app):
    with app.app_context():
        print("=" * 60)
        print(" INTERVIEW PORTAL DATABASE SUMMARY")
        print("=" * 60)
        
        user_count = User.query.count()
        question_count = Question.query.count()
        progress_count = UserProgress.query.count()
        bookmark_count = Bookmark.query.count()

        print(f" * Total Registered Users:   {user_count}")
        print(f" * Total Questions:          {question_count}")
        print(f" * Total Progress Records:   {progress_count}")
        print(f" * Total Bookmarks:          {bookmark_count}")
        print("-" * 60)
        
        from sqlalchemy import func
        cat_counts = db.session.query(Question.category, func.count(Question.id)).group_by(Question.category).all()
        print("Questions by Category:")
        for cat, count in cat_counts:
            print(f"   - {cat:20}: {count} questions")
        
        topic_counts = db.session.query(Question.topic, func.count(Question.id)).filter(Question.topic != None).group_by(Question.topic).all()
        print(f"\nCurated Topics Covered:     {len(topic_counts)} topics")
        print("=" * 60)

import sqlite3

def migrate_from_sqlite_if_needed(app):
    sqlite_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'interview_portal.db')
    if not os.path.exists(sqlite_path):
        return

    with app.app_context():
        # Check if TiDB already has questions
        existing_count = Question.query.count()
        if existing_count > 0:
            print(f"[i] Target database already has {existing_count} questions. Skipping SQLite migration.")
            return

        print(f"[*] Migrating existing questions and users from local SQLite database ({sqlite_path})...")
        try:
            conn = sqlite3.connect(sqlite_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            # Migrate Users
            cursor.execute("SELECT * FROM users")
            sqlite_users = cursor.fetchall()
            for u in sqlite_users:
                u_dict = dict(u)
                if not User.query.filter_by(username=u_dict['username']).first():
                    # clean up columns
                    u_obj = User(
                        username=u_dict['username'],
                        email=u_dict['email'],
                        password_hash=u_dict['password_hash'],
                        full_name=u_dict.get('full_name', 'Demo User'),
                        education=u_dict.get('education', 'B.Tech'),
                        college=u_dict.get('college', 'Engineering College'),
                        location=u_dict.get('location', 'India'),
                        preferred_domain=u_dict.get('preferred_domain', 'Full Stack'),
                        target_companies=u_dict.get('target_companies', 'TCS, Infosys'),
                        profile_pic=u_dict.get('profile_pic', 'avatar_default'),
                        skills=u_dict.get('skills', 'Python, SQL'),
                        completed_courses=u_dict.get('completed_courses', ''),
                        certificates=u_dict.get('certificates', ''),
                        target_role=u_dict.get('target_role', 'Software Developer'),
                        streak_count=u_dict.get('streak_count', 1)
                    )
                    db.session.add(u_obj)
            db.session.commit()
            print(f"[+] Migrated {len(sqlite_users)} users.")

            # Migrate Questions
            cursor.execute("SELECT * FROM questions")
            sqlite_questions = cursor.fetchall()
            q_batch = []
            for q in sqlite_questions:
                q_dict = dict(q)
                q_obj = Question(
                    category=q_dict.get('category'),
                    sub_category=q_dict.get('sub_category'),
                    topic=q_dict.get('topic'),
                    title=q_dict.get('title'),
                    difficulty=q_dict.get('difficulty'),
                    question_text=q_dict.get('question_text'),
                    sample_answer=q_dict.get('sample_answer'),
                    tips=q_dict.get('tips'),
                    star_guide=q_dict.get('star_guide'),
                    options=q_dict.get('options'),
                    correct_option=q_dict.get('correct_option')
                )
                q_batch.append(q_obj)
                if len(q_batch) >= 100:
                    db.session.bulk_save_objects(q_batch)
                    db.session.commit()
                    q_batch = []

            if q_batch:
                db.session.bulk_save_objects(q_batch)
                db.session.commit()

            print(f"[OK] Migrated all {len(sqlite_questions)} questions to target database.")
            conn.close()
        except Exception as e:
            print(f"[!] SQLite migration error: {e}")
            db.session.rollback()

def main():
    parser = argparse.ArgumentParser(description="Initialize and seed the Interview Portal database.")
    parser.add_argument('--reset', action='store_true', help="Drop all tables and re-create everything from scratch.")
    parser.add_argument('--status', action='store_true', help="Only display the database summary/status without modifying data.")
    args = parser.parse_args()

    ensure_instance_dir()
    app = get_app()

    if args.status:
        print_database_status(app)
        return

    print("[*] Initializing Database for Interview Portal...")
    create_tables(app, reset=args.reset)
    ensure_users(app)
    migrate_from_sqlite_if_needed(app)
    with app.app_context():
        if Question.query.count() == 0:
            seed_core_questions(app)
            seed_all_specialized_topics()
    print_database_status(app)
    print("[SUCCESS] Database is ready to use!")

if __name__ == '__main__':
    main()
