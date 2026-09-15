import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db')

questions = [
    {
        "title": "Simplification - 48 / 6 * 4 + 12 - 5",
        "difficulty": "Medium",
        "question_text": "Simplify: 48 ÷ 6 × 4 + 12 − 5",
        "sample_answer": "Apply BODMAS:\n1. 48 ÷ 6 = 8\n2. 8 × 4 = 32\n3. 32 + 12 = 44\n4. 44 − 5 = 39.",
        "tips": "Follow order of operations: Division -> Multiplication -> Addition -> Subtraction.",
        "options": [
            {"label": "A", "text": "32", "is_correct": False},
            {"label": "B", "text": "39", "is_correct": True},
            {"label": "C", "text": "44", "is_correct": False},
            {"label": "D", "text": "48", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - 25 + 36 / 6 * 3 - 8",
        "difficulty": "Medium",
        "question_text": "Simplify: 25 + 36 ÷ 6 × 3 − 8",
        "sample_answer": "1. 36 ÷ 6 = 6\n2. 6 × 3 = 18\n3. 25 + 18 = 43\n4. 43 − 8 = 35.",
        "tips": "Perform division and multiplication before addition and subtraction.",
        "options": [
            {"label": "A", "text": "25", "is_correct": False},
            {"label": "B", "text": "30", "is_correct": False},
            {"label": "C", "text": "35", "is_correct": True},
            {"label": "D", "text": "42", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - 3/4 + 5/8 - 1/2",
        "difficulty": "Medium",
        "question_text": "Find the value: 3/4 + 5/8 − 1/2",
        "sample_answer": "LCM of denominators 4, 8, 2 is 8.\n3/4 = 6/8, 5/8 = 5/8, 1/2 = 4/8.\n(6 + 5 - 4) / 8 = 7/8.",
        "tips": "Convert all fractions to common denominator 8.",
        "options": [
            {"label": "A", "text": "5/8", "is_correct": False},
            {"label": "B", "text": "7/8", "is_correct": True},
            {"label": "C", "text": "9/8", "is_correct": False},
            {"label": "D", "text": "1/2", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - (24 * 15) / (8 * 5)",
        "difficulty": "Medium",
        "question_text": "Simplify: (24 × 15) / (8 × 5)",
        "sample_answer": "Cancel out common terms:\n24 / 8 = 3\n15 / 5 = 3\n3 × 3 = 9.",
        "tips": "Simplify terms in numerator and denominator individually.",
        "options": [
            {"label": "A", "text": "6", "is_correct": False},
            {"label": "B", "text": "8", "is_correct": False},
            {"label": "C", "text": "9", "is_correct": True},
            {"label": "D", "text": "12", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - sqrt(144) + sqrt(225) - sqrt(81)",
        "difficulty": "Medium",
        "question_text": "Find: √144 + √225 − √81",
        "sample_answer": "√144 = 12\n√225 = 15\n√81 = 9\n12 + 15 − 9 = 27 − 9 = 18.",
        "tips": "Evaluate square roots first.",
        "options": [
            {"label": "A", "text": "15", "is_correct": False},
            {"label": "B", "text": "18", "is_correct": True},
            {"label": "C", "text": "21", "is_correct": False},
            {"label": "D", "text": "24", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - (2/3 * 9/4) + 5/6",
        "difficulty": "Medium",
        "question_text": "Simplify: (2/3 × 9/4) + 5/6",
        "sample_answer": "(2/3 × 9/4) = 18/12 = 3/2.\n3/2 + 5/6 = 9/6 + 5/6 = 14/6 = 7/3.",
        "tips": "Multiply fractions first, then add.",
        "options": [
            {"label": "A", "text": "5/3", "is_correct": False},
            {"label": "B", "text": "2", "is_correct": False},
            {"label": "C", "text": "7/3", "is_correct": True},
            {"label": "D", "text": "8/3", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - 18^2 - 12^2",
        "difficulty": "Medium",
        "question_text": "Find the value: 18² − 12²",
        "sample_answer": "Using a² − b² = (a − b)(a + b):\n(18 − 12)(18 + 12) = 6 × 30 = 180.",
        "tips": "Use algebraic identity a^2 - b^2.",
        "options": [
            {"label": "A", "text": "150", "is_correct": False},
            {"label": "B", "text": "180", "is_correct": True},
            {"label": "C", "text": "210", "is_correct": False},
            {"label": "D", "text": "240", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - 125/5 + 144/12 - 7",
        "difficulty": "Medium",
        "question_text": "Simplify: 125/5 + 144/12 − 7",
        "sample_answer": "125 / 5 = 25\n144 / 12 = 12\n25 + 12 − 7 = 37 − 7 = 30.",
        "tips": "Perform divisions before addition/subtraction.",
        "options": [
            {"label": "A", "text": "25", "is_correct": False},
            {"label": "B", "text": "30", "is_correct": True},
            {"label": "C", "text": "35", "is_correct": False},
            {"label": "D", "text": "40", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - (15 + 5) * (18 - 8) / 10",
        "difficulty": "Medium",
        "question_text": "Find: (15 + 5) × (18 − 8) ÷ 10",
        "sample_answer": "(15 + 5) = 20\n(18 − 8) = 10\n20 × 10 ÷ 10 = 20.",
        "tips": "Simplify terms inside parentheses first.",
        "options": [
            {"label": "A", "text": "10", "is_correct": False},
            {"label": "B", "text": "20", "is_correct": True},
            {"label": "C", "text": "30", "is_correct": False},
            {"label": "D", "text": "40", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - 7/12 + 5/18 - 1/9",
        "difficulty": "Medium",
        "question_text": "Simplify: 7/12 + 5/18 − 1/9",
        "sample_answer": "LCM of 12, 18, 9 is 36.\n(21 + 10 − 4) / 36 = 27 / 36 = 3/4.",
        "tips": "Use common denominator 36.",
        "options": [
            {"label": "A", "text": "1/2", "is_correct": False},
            {"label": "B", "text": "2/3", "is_correct": False},
            {"label": "C", "text": "3/4", "is_correct": True},
            {"label": "D", "text": "5/6", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - 2^5 + 3^3 - 4^2",
        "difficulty": "Medium",
        "question_text": "Find the value: 2⁵ + 3³ − 4²",
        "sample_answer": "2⁵ = 32\n3³ = 27\n4² = 16\n32 + 27 − 16 = 59 − 16 = 43.",
        "tips": "Evaluate exponent powers individually.",
        "options": [
            {"label": "A", "text": "37", "is_correct": False},
            {"label": "B", "text": "43", "is_correct": True},
            {"label": "C", "text": "49", "is_correct": False},
            {"label": "D", "text": "55", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - (45/9 * 18/5) + 7",
        "difficulty": "Medium",
        "question_text": "Simplify: (45/9 × 18/5) + 7",
        "sample_answer": "45 / 9 = 5\n5 × (18 / 5) = 18\n18 + 7 = 25.",
        "tips": "Cancel out common factor 5.",
        "options": [
            {"label": "A", "text": "18", "is_correct": False},
            {"label": "B", "text": "23", "is_correct": False},
            {"label": "C", "text": "25", "is_correct": True},
            {"label": "D", "text": "29", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - sqrt(400) + sqrt(196) - sqrt(64)",
        "difficulty": "Medium",
        "question_text": "Find: √400 + √196 − √64",
        "sample_answer": "√400 = 20\n√196 = 14\n√64 = 8\n20 + 14 − 8 = 34 − 8 = 26.",
        "tips": "20 + 14 - 8.",
        "options": [
            {"label": "A", "text": "22", "is_correct": False},
            {"label": "B", "text": "24", "is_correct": False},
            {"label": "C", "text": "26", "is_correct": True},
            {"label": "D", "text": "28", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - 75 - {18 + 6 * 4}",
        "difficulty": "Medium",
        "question_text": "Simplify: 75 − {18 + 6 × 4}",
        "sample_answer": "Inside braces: 6 × 4 = 24.\n18 + 24 = 42.\n75 − 42 = 33.",
        "tips": "Work from innermost operations outward.",
        "options": [
            {"label": "A", "text": "27", "is_correct": False},
            {"label": "B", "text": "33", "is_correct": True},
            {"label": "C", "text": "39", "is_correct": False},
            {"label": "D", "text": "45", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - (5/6 / 10/9) + 3/4",
        "difficulty": "Medium",
        "question_text": "Find the value: (5/6 ÷ 10/9) + 3/4",
        "sample_answer": "(5/6 × 9/10) = 45/60 = 3/4.\n3/4 + 3/4 = 6/4 = 3/2.",
        "tips": "Invert fraction for division.",
        "options": [
            {"label": "A", "text": "1", "is_correct": False},
            {"label": "B", "text": "5/4", "is_correct": False},
            {"label": "C", "text": "3/2", "is_correct": True},
            {"label": "D", "text": "7/4", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # QUESTIONS 16 TO 30
    {
        "title": "Simplification - 3/5 + (7/10 * 15/14) - 1/4",
        "difficulty": "Hard",
        "question_text": "Simplify: 3/5 + (7/10 × 15/14) − 1/4",
        "sample_answer": "(7/10 × 15/14) = 3/4.\n3/5 + 3/4 − 1/4 = 3/5 + 2/4 = 3/5 + 1/2 = 11/10.",
        "tips": "Multiply first, then simplify fractions.",
        "options": [
            {"label": "A", "text": "9/10", "is_correct": False},
            {"label": "B", "text": "11/10", "is_correct": True},
            {"label": "C", "text": "6/5", "is_correct": False},
            {"label": "D", "text": "13/10", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - (3/4 + 5/6) / (19/12)",
        "difficulty": "Hard",
        "question_text": "Find the value: (3/4 + 5/6) ÷ (19/12)",
        "sample_answer": "(3/4 + 5/6) = (9 + 10) / 12 = 19/12.\n(19/12) ÷ (19/12) = 1.",
        "tips": "Numerator equals denominator.",
        "options": [
            {"label": "A", "text": "1/2", "is_correct": False},
            {"label": "B", "text": "1", "is_correct": True},
            {"label": "C", "text": "3/2", "is_correct": False},
            {"label": "D", "text": "2", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - (3^3 * 2^5) / 6^2 + sqrt(625)",
        "difficulty": "Hard",
        "question_text": "Simplify: (3³ × 2⁵) / 6² + √625",
        "sample_answer": "(27 × 32) / 36 = 864 / 36 = 24.\n√625 = 25.\n24 + 25 = 49.",
        "tips": "Express 6^2 as 3^2 * 2^2.",
        "options": [
            {"label": "A", "text": "39", "is_correct": False},
            {"label": "B", "text": "45", "is_correct": False},
            {"label": "C", "text": "49", "is_correct": True},
            {"label": "D", "text": "54", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - (15^2 - 9^2) / (15 - 9)",
        "difficulty": "Hard",
        "question_text": "Find: (15² − 9²) / (15 − 9)",
        "sample_answer": "Using (a² − b²) / (a − b) = a + b:\n15 + 9 = 24.",
        "tips": "Cancel (a - b) term.",
        "options": [
            {"label": "A", "text": "18", "is_correct": False},
            {"label": "B", "text": "21", "is_correct": False},
            {"label": "C", "text": "24", "is_correct": True},
            {"label": "D", "text": "27", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - (7/8 * 16/21) + (5/6 / 10/9)",
        "difficulty": "Hard",
        "question_text": "Simplify: (7/8 × 16/21) + (5/6 ÷ 10/9)",
        "sample_answer": "Term 1: (7/8 × 16/21) = 2/3.\nTerm 2: (5/6 × 9/10) = 3/4.\n2/3 + 3/4 = (8 + 9) / 12 = 17/12.",
        "tips": "Evaluate both fraction terms separately.",
        "options": [
            {"label": "A", "text": "13/12", "is_correct": False},
            {"label": "B", "text": "15/12", "is_correct": False},
            {"label": "C", "text": "17/12", "is_correct": True},
            {"label": "D", "text": "19/12", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - (25 + 15)^2 / 20^2 + 3^2 / 9",
        "difficulty": "Hard",
        "question_text": "Find the value: (25 + 15)² / 20² + 3² / 9",
        "sample_answer": "(40)² / 20² = 1600 / 400 = 4.\n3² / 9 = 9 / 9 = 1.\n4 + 1 = 5.",
        "tips": "(40 / 20)^2 + 1.",
        "options": [
            {"label": "A", "text": "3", "is_correct": False},
            {"label": "B", "text": "4", "is_correct": False},
            {"label": "C", "text": "5", "is_correct": True},
            {"label": "D", "text": "6", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - (5/7 / 10/21) + (3/4 * 8/9)",
        "difficulty": "Hard",
        "question_text": "Simplify: (5/7 ÷ 10/21) + (3/4 × 8/9)",
        "sample_answer": "Term 1: (5/7 × 21/10) = 3/2.\nTerm 2: (3/4 × 8/9) = 2/3.\n3/2 + 2/3 = (9 + 4) / 6 = 13/6.",
        "tips": "Common denominator is 6.",
        "options": [
            {"label": "A", "text": "11/6", "is_correct": False},
            {"label": "B", "text": "13/6", "is_correct": True},
            {"label": "C", "text": "15/6", "is_correct": False},
            {"label": "D", "text": "17/6", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - sqrt(1296) + sqrt(625) - sqrt(256)",
        "difficulty": "Hard",
        "question_text": "Find: √1296 + √625 − √256",
        "sample_answer": "√1296 = 36\n√625 = 25\n√256 = 16\n36 + 25 − 16 = 61 − 16 = 45.",
        "tips": "Square roots of 36, 25, 16.",
        "options": [
            {"label": "A", "text": "35", "is_correct": False},
            {"label": "B", "text": "40", "is_correct": False},
            {"label": "C", "text": "45", "is_correct": True},
            {"label": "D", "text": "50", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - (3^3 + 4^3 - 5^2) / 2^3",
        "difficulty": "Hard",
        "question_text": "Simplify: (3³ + 4³ − 5²) / 2³",
        "sample_answer": "3³ = 27, 4³ = 64, 5² = 25.\nNumerator = 27 + 64 − 25 = 66.\nDenominator = 2³ = 8.\n66 / 8 = 33/4.",
        "tips": "66 / 8 = 33 / 4.",
        "options": [
            {"label": "A", "text": "27/4", "is_correct": False},
            {"label": "B", "text": "31/4", "is_correct": False},
            {"label": "C", "text": "33/4", "is_correct": True},
            {"label": "D", "text": "35/4", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - (5/6 - 1/4) * (12/7)",
        "difficulty": "Hard",
        "question_text": "Find the value: (5/6 − 1/4) × (12/7)",
        "sample_answer": "(5/6 − 1/4) = (10 − 3) / 12 = 7/12.\n(7/12) × (12/7) = 1.",
        "tips": "Numerator cancels denominator.",
        "options": [
            {"label": "A", "text": "1/2", "is_correct": False},
            {"label": "B", "text": "3/4", "is_correct": False},
            {"label": "C", "text": "1", "is_correct": True},
            {"label": "D", "text": "7/6", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - (15 * 10) / ((18 + 12) * (25 - 15))",
        "difficulty": "Hard",
        "question_text": "Simplify: (15 × 10) / [(18 + 12) × (25 − 15)]",
        "sample_answer": "Numerator = 15 × 10 = 150.\nDenominator = 30 × 10 = 300.\n150 / 300 = 1/2.",
        "tips": "150 / 300.",
        "options": [
            {"label": "A", "text": "1/4", "is_correct": False},
            {"label": "B", "text": "1/2", "is_correct": True},
            {"label": "C", "text": "3/4", "is_correct": False},
            {"label": "D", "text": "1", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - 2/3 + (4/9 / 8/27) - 5/6",
        "difficulty": "Hard",
        "question_text": "Find: 2/3 + (4/9 ÷ 8/27) − 5/6",
        "sample_answer": "(4/9 × 27/8) = 3/2.\n2/3 + 3/2 − 5/6 = (4 + 9 − 5) / 6 = 8/6 = 4/3.",
        "tips": "Convert division to multiplication.",
        "options": [
            {"label": "A", "text": "1", "is_correct": False},
            {"label": "B", "text": "7/6", "is_correct": False},
            {"label": "C", "text": "4/3", "is_correct": True},
            {"label": "D", "text": "3/2", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - ((7^2 - 5^2)(7^2 + 5^2)) / 24",
        "difficulty": "Hard",
        "question_text": "Simplify: [(7² − 5²)(7² + 5²)] / 24",
        "sample_answer": "(7² − 5²) = 49 − 25 = 24.\n(7² + 5²) = 49 + 25 = 74.\n(24 × 74) / 24 = 74.",
        "tips": "Cancel factor 24.",
        "options": [
            {"label": "A", "text": "48", "is_correct": False},
            {"label": "B", "text": "60", "is_correct": False},
            {"label": "C", "text": "74", "is_correct": True},
            {"label": "D", "text": "96", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - 3/4 * [8/9 + 5/6] - 1/8",
        "difficulty": "Hard",
        "question_text": "Find the value: 3/4 × [8/9 + 5/6] − 1/8",
        "sample_answer": "[8/9 + 5/6] = (16 + 15) / 18 = 31/18.\n3/4 × 31/18 = 31/24.\n31/24 − 1/8 = (31 − 3) / 24 = 28/24 = 7/6.",
        "tips": "Common denominator for fraction addition.",
        "options": [
            {"label": "A", "text": "5/6", "is_correct": False},
            {"label": "B", "text": "1", "is_correct": False},
            {"label": "C", "text": "7/6", "is_correct": True},
            {"label": "D", "text": "4/3", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - 13/sqrt(5^2 + 12^2) + 15/sqrt(17^2 - 8^2)",
        "difficulty": "Hard",
        "question_text": "Simplify: 13 / √(5² + 12²) + 15 / √(17² − 8²)",
        "sample_answer": "√(5² + 12²) = √(25 + 144) = √169 = 13.\n13 / 13 = 1.\n√(17² − 8²) = √(289 − 64) = √225 = 15.\n15 / 15 = 1.\n1 + 1 = 2.",
        "tips": "Evaluate Pythagorean radicals.",
        "options": [
            {"label": "A", "text": "1", "is_correct": False},
            {"label": "B", "text": "2", "is_correct": True},
            {"label": "C", "text": "3", "is_correct": False},
            {"label": "D", "text": "4", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete old Simplification questions to replace with exact 30 questions requested by user
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Simplification'")
    print("Cleared existing Simplification questions.")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'Aptitude',
            'Number & Arithmetic',
            'Simplification',
            q['title'],
            q['difficulty'],
            q['question_text'],
            q['sample_answer'],
            q['tips'],
            json.dumps(q['options']),
            q['correct_option']
        ))
        
    conn.commit()
    conn.close()
    print(f"Successfully seeded {len(questions)} Simplification questions into SQLite DB!")

if __name__ == '__main__':
    seed_db()
