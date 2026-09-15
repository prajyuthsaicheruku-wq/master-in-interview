import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- DIRECTION & DISTANCE FUNDAMENTALS (Q1 - Q10) ---
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "Ravi walks 10 m towards North, then turns right and walks 15 m. In which direction is he now from his starting point?",
        "sample_answer": "Displacement: +10 m North, +15 m East.\nCoordinates from origin: (15, 10).\nDirection from starting point: North-East.",
        "tips": "Plot movements on a Cartesian grid: (+X = East, +Y = North).",
        "options": [
            {"label": "A", "text": "North", "is_correct": False},
            {"label": "B", "text": "East", "is_correct": False},
            {"label": "C", "text": "North-East", "is_correct": True},
            {"label": "D", "text": "South-East", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A man walks 20 m East, then turns left and walks 10 m. Which direction is he facing now?",
        "sample_answer": "Facing East → Turns Left → Now facing North.",
        "tips": "Left turn from East is North.",
        "options": [
            {"label": "A", "text": "North", "is_correct": True},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": False},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "Ramesh walks 15 m South, then turns left and walks 20 m. Which direction is he facing?",
        "sample_answer": "Facing South → Turns Left → Now facing East.",
        "tips": "Left turn from South is East.",
        "options": [
            {"label": "A", "text": "North", "is_correct": False},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": True},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A person walks 12 m North, then 5 m East, then 12 m South. How far is he from the starting point?",
        "sample_answer": "North 12 m and South 12 m cancel out.\nRemaining distance = 5 m East.",
        "tips": "Opposite direction movements cancel out.",
        "options": [
            {"label": "A", "text": "5 m", "is_correct": True},
            {"label": "B", "text": "12 m", "is_correct": False},
            {"label": "C", "text": "17 m", "is_correct": False},
            {"label": "D", "text": "29 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A boy walks 25 m West, then turns right and walks 15 m. Which direction is he facing now?",
        "sample_answer": "Facing West → Turns Right → Now facing North.",
        "tips": "Right turn from West is North.",
        "options": [
            {"label": "A", "text": "North", "is_correct": True},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": False},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A man starts from a point, walks 10 m East, then 10 m North, then 10 m West. How far is he from the starting point?",
        "sample_answer": "East 10 m and West 10 m cancel out.\nDistance from starting point = 10 m North.",
        "tips": "X-axis displacement = 10 - 10 = 0.",
        "options": [
            {"label": "A", "text": "0 m", "is_correct": False},
            {"label": "B", "text": "10 m", "is_correct": True},
            {"label": "C", "text": "20 m", "is_correct": False},
            {"label": "D", "text": "30 m", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A person moves 30 m South, then turns left and moves 20 m. Which direction is he facing?",
        "sample_answer": "Facing South → Turns Left → Now facing East.",
        "tips": "Left turn from South is East.",
        "options": [
            {"label": "A", "text": "North", "is_correct": False},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": True},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A girl walks 8 m North, then 6 m East. What is her shortest distance from the starting point?",
        "sample_answer": "Shortest distance = √(8² + 6²) = √(64 + 36) = √100 = 10 m.",
        "tips": "Apply Pythagoras Theorem: √(North² + East²).",
        "options": [
            {"label": "A", "text": "10 m", "is_correct": True},
            {"label": "B", "text": "14 m", "is_correct": False},
            {"label": "C", "text": "12 m", "is_correct": False},
            {"label": "D", "text": "16 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A man walks 5 m East, 5 m South, 5 m West, and 5 m North. Where is he now?",
        "sample_answer": "East 5 m cancels West 5 m. South 5 m cancels North 5 m.\nHe is back at the Starting Point (0 m).",
        "tips": "Net displacement is 0 in both X and Y axes.",
        "options": [
            {"label": "A", "text": "Starting Point", "is_correct": True},
            {"label": "B", "text": "5 m East", "is_correct": False},
            {"label": "C", "text": "5 m North", "is_correct": False},
            {"label": "D", "text": "10 m Away", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Medium",
        "question_text": "A person walks 20 m North, then 15 m East, then 20 m South. How far is he from the starting point?",
        "sample_answer": "North 20 m cancels South 20 m.\nDistance from starting point = 15 m.",
        "tips": "Net Y displacement = 0.",
        "options": [
            {"label": "A", "text": "15 m", "is_correct": True},
            {"label": "B", "text": "20 m", "is_correct": False},
            {"label": "C", "text": "35 m", "is_correct": False},
            {"label": "D", "text": "55 m", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- HARD LEVEL (Q11 - Q20) ---
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A man walks 15 m North, then 20 m East, then 15 m South. In which direction is he from the starting point?",
        "sample_answer": "North 15 m cancels South 15 m.\nRemaining position: 20 m East → Direction is East.",
        "tips": "Net Y-axis movement is 0.",
        "options": [
            {"label": "A", "text": "North", "is_correct": False},
            {"label": "B", "text": "East", "is_correct": True},
            {"label": "C", "text": "South", "is_correct": False},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "Ravi walks 10 m South, then 10 m West, then 10 m North. How far and in which direction is he from the starting point?",
        "sample_answer": "South 10 m cancels North 10 m.\nRemaining position: 10 m West.",
        "tips": "Net Y displacement = 0, X displacement = -10 m.",
        "options": [
            {"label": "A", "text": "10 m West", "is_correct": True},
            {"label": "B", "text": "10 m East", "is_correct": False},
            {"label": "C", "text": "20 m West", "is_correct": False},
            {"label": "D", "text": "Starting Point", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A boy starts facing North. He turns right, then right again, then left. Which direction is he facing now?",
        "sample_answer": "North → Right = East → Right = South → Left = East.",
        "tips": "Two rights + one left = One net right turn from North.",
        "options": [
            {"label": "A", "text": "North", "is_correct": False},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": True},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A person walks 20 m East, then 15 m North, then 20 m West, then 10 m South. How far is he from the starting point?",
        "sample_answer": "East 20 m and West 20 m cancel out.\nNorth 15 m − South 10 m = 5 m North.",
        "tips": "Net X = 0, Net Y = 15 - 10 = 5 m.",
        "options": [
            {"label": "A", "text": "5 m", "is_correct": True},
            {"label": "B", "text": "10 m", "is_correct": False},
            {"label": "C", "text": "15 m", "is_correct": False},
            {"label": "D", "text": "25 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A man walks 12 m North, 5 m East, 12 m South, and 5 m West. Where is he now?",
        "sample_answer": "North 12 m cancels South 12 m. East 5 m cancels West 5 m.\nHe is at the Starting Point.",
        "tips": "Full closed loop = 0 m.",
        "options": [
            {"label": "A", "text": "Starting Point", "is_correct": True},
            {"label": "B", "text": "5 m East", "is_correct": False},
            {"label": "C", "text": "12 m North", "is_correct": False},
            {"label": "D", "text": "17 m Away", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A girl walks 18 m West, then turns left and walks 24 m. What is her distance from the starting point?",
        "sample_answer": "Shortest distance = √(18² + 24²) = √(324 + 576) = √900 = 30 m.",
        "tips": "3-4-5 triplet scaled by 6 (18-24-30).",
        "options": [
            {"label": "A", "text": "30 m", "is_correct": True},
            {"label": "B", "text": "42 m", "is_correct": False},
            {"label": "C", "text": "36 m", "is_correct": False},
            {"label": "D", "text": "24 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A man walks 10 m North, 24 m East, and 10 m South. Find the shortest distance from the starting point.",
        "sample_answer": "North 10 m and South 10 m cancel out.\nShortest distance = 24 m East.",
        "tips": "Net Y displacement = 0.",
        "options": [
            {"label": "A", "text": "24 m", "is_correct": True},
            {"label": "B", "text": "26 m", "is_correct": False},
            {"label": "C", "text": "44 m", "is_correct": False},
            {"label": "D", "text": "10 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A person starts facing East. He turns 135° clockwise. Which direction is he facing now?",
        "sample_answer": "East = 90°.\nClockwise turn of 135° → 90° + 135° = 225° (South-West).",
        "tips": "90° (East) + 135° clockwise = South-West.",
        "options": [
            {"label": "A", "text": "South-East", "is_correct": False},
            {"label": "B", "text": "South-West", "is_correct": True},
            {"label": "C", "text": "North-West", "is_correct": False},
            {"label": "D", "text": "North-East", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A man walks 14 m South, then 48 m East. Find the shortest distance from the starting point.",
        "sample_answer": "Shortest distance = √(14² + 48²) = √(196 + 2304) = √2500 = 50 m.",
        "tips": "Pythagorean triplet 7-24-25 doubled (14-48-50).",
        "options": [
            {"label": "A", "text": "50 m", "is_correct": True},
            {"label": "B", "text": "62 m", "is_correct": False},
            {"label": "C", "text": "52 m", "is_correct": False},
            {"label": "D", "text": "48 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A boy walks 30 m North, then 40 m East, then 30 m South. How far is he from the starting point?",
        "sample_answer": "North 30 m cancels South 30 m.\nRemaining distance = 40 m East.",
        "tips": "Y-axis movement cancels out.",
        "options": [
            {"label": "A", "text": "40 m", "is_correct": True},
            {"label": "B", "text": "30 m", "is_correct": False},
            {"label": "C", "text": "70 m", "is_correct": False},
            {"label": "D", "text": "100 m", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- ADVANCED PLACEMENT-LEVEL QUESTIONS (Q21 - Q30) ---
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A person starts facing North. He turns right, walks 10 m, turns left, walks 20 m, turns left, and walks 10 m. In which direction is he from the starting point?",
        "sample_answer": "Turn Right (East) 10 m → Turn Left (North) 20 m → Turn Left (West) 10 m.\nEast 10 m and West 10 m cancel out.\nFinal position: 20 m North → Direction is North.",
        "tips": "East 10 m and West 10 m cancel out, leaving North 20 m.",
        "options": [
            {"label": "A", "text": "North", "is_correct": True},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": False},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A man walks 25 m East, then 20 m North, then 25 m West, then 10 m South. How far is he from the starting point?",
        "sample_answer": "East 25 m cancels West 25 m.\nNorth 20 m − South 10 m = 10 m North.",
        "tips": "Net X = 0, Net Y = 10 m.",
        "options": [
            {"label": "A", "text": "10 m", "is_correct": True},
            {"label": "B", "text": "20 m", "is_correct": False},
            {"label": "C", "text": "30 m", "is_correct": False},
            {"label": "D", "text": "80 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A boy starts facing South. He turns left, then right, then right. Which direction is he facing now?",
        "sample_answer": "South → Left = East → Right = South → Right = West.",
        "tips": "Turn sequence: South → East → South → West.",
        "options": [
            {"label": "A", "text": "North", "is_correct": False},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": False},
            {"label": "D", "text": "West", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A person moves 8 m North, 15 m East, 8 m South. What is the shortest distance from the starting point?",
        "sample_answer": "North 8 m cancels South 8 m.\nRemaining distance = 15 m.",
        "tips": "Y-axis cancellation.",
        "options": [
            {"label": "A", "text": "15 m", "is_correct": True},
            {"label": "B", "text": "17 m", "is_correct": False},
            {"label": "C", "text": "23 m", "is_correct": False},
            {"label": "D", "text": "31 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A man walks 12 m East, 16 m North. Find the shortest distance from the starting point.",
        "sample_answer": "Shortest distance = √(12² + 16²) = √(144 + 256) = √400 = 20 m.",
        "tips": "3-4-5 triplet scaled by 4 (12-16-20).",
        "options": [
            {"label": "A", "text": "20 m", "is_correct": True},
            {"label": "B", "text": "28 m", "is_correct": False},
            {"label": "C", "text": "24 m", "is_correct": False},
            {"label": "D", "text": "16 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A person starts facing West. He turns 90° clockwise, then 180° clockwise. Which direction is he facing now?",
        "sample_answer": "West → 90° clockwise = North → 180° clockwise = South.",
        "tips": "90° + 180° = 270° clockwise from West = South.",
        "options": [
            {"label": "A", "text": "North", "is_correct": False},
            {"label": "B", "text": "South", "is_correct": True},
            {"label": "C", "text": "East", "is_correct": False},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A girl walks 20 m South, then 21 m East. Find the shortest distance from the starting point.",
        "sample_answer": "Shortest distance = √(20² + 21²) = √(400 + 441) = √841 = 29 m.",
        "tips": "Pythagorean triplet 20-21-29.",
        "options": [
            {"label": "A", "text": "29 m", "is_correct": True},
            {"label": "B", "text": "41 m", "is_correct": False},
            {"label": "C", "text": "31 m", "is_correct": False},
            {"label": "D", "text": "25 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A man walks 9 m North, then 12 m East. Find the shortest distance from the starting point.",
        "sample_answer": "Shortest distance = √(9² + 12²) = √(81 + 144) = √225 = 15 m.",
        "tips": "3-4-5 triplet scaled by 3 (9-12-15).",
        "options": [
            {"label": "A", "text": "15 m", "is_correct": True},
            {"label": "B", "text": "21 m", "is_correct": False},
            {"label": "C", "text": "18 m", "is_correct": False},
            {"label": "D", "text": "12 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A person walks 15 m North, then 20 m East, then 15 m South, then 5 m West. How far is he from the starting point?",
        "sample_answer": "North 15 m cancels South 15 m.\nEast 20 m − West 5 m = 15 m East.",
        "tips": "Net X = 20 - 5 = 15 m.",
        "options": [
            {"label": "A", "text": "15 m", "is_correct": True},
            {"label": "B", "text": "20 m", "is_correct": False},
            {"label": "C", "text": "25 m", "is_correct": False},
            {"label": "D", "text": "55 m", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense",
        "difficulty": "Hard",
        "question_text": "A boy starts facing North. He turns left, walks 10 m, turns right, walks 20 m, turns right, walks 10 m. In which direction is he from the starting point?",
        "sample_answer": "Turn Left (West) 10 m → Turn Right (North) 20 m → Turn Right (East) 10 m.\nWest 10 m and East 10 m cancel out.\nFinal position: 20 m North → Direction is North.",
        "tips": "West 10 m cancels East 10 m, leaving 20 m North.",
        "options": [
            {"label": "A", "text": "North", "is_correct": True},
            {"label": "B", "text": "South", "is_correct": False},
            {"label": "C", "text": "East", "is_correct": False},
            {"label": "D", "text": "West", "is_correct": False}
        ],
        "correct_option": "A"
    }
]

def seed_direction_sense():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Direction Sense'")
            print(f"Deleted old 'Direction Sense' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Logical Reasoning',
                    'Direction Sense',
                    q['title'],
                    q['difficulty'],
                    q['question_text'],
                    q['sample_answer'],
                    q['tips'],
                    json.dumps(q['options']),
                    q['correct_option'],
                    json.dumps({
                        'options': q['options'],
                        'correct_option': q['correct_option']
                    })
                ))
                inserted_count += 1

            conn.commit()
            conn.close()
            print(f"Successfully inserted {inserted_count} questions into {db_path}.")
        except Exception as e:
            print(f"Skipping {db_path}: {e}")

if __name__ == '__main__':
    seed_direction_sense()
