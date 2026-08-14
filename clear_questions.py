from app import app, db, Question, UserProgress, Bookmark

with app.app_context():
    num_bookmarks = Bookmark.query.delete()
    num_progress = UserProgress.query.delete()
    num_questions = Question.query.delete()
    db.session.commit()
    print(f"Successfully deleted {num_questions} questions, {num_progress} progress records, and {num_bookmarks} bookmarks.")
