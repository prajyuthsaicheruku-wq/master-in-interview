import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db')

questions = [
    {
        "title": "HCF & LCM - HCF of 84 and 126",
        "difficulty": "Medium",
        "question_text": "Find the HCF of 84 and 126.",
        "sample_answer": "84 = 2^2 * 3 * 7\n126 = 2 * 3^2 * 7\nHCF = 2^1 * 3^1 * 7^1 = 42.",
        "tips": "Take the common prime factors with the lowest powers.",
        "options": [
            {"label": "A", "text": "14", "is_correct": False},
            {"label": "B", "text": "21", "is_correct": False},
            {"label": "C", "text": "42", "is_correct": True},
            {"label": "D", "text": "84", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - LCM of 24, 36, and 48",
        "difficulty": "Medium",
        "question_text": "Find the LCM of 24, 36, and 48.",
        "sample_answer": "24 = 2^3 * 3\n36 = 2^2 * 3^2\n48 = 2^4 * 3\nLCM = 2^4 * 3^2 = 16 * 9 = 144.",
        "tips": "Take highest powers of all prime factors present.",
        "options": [
            {"label": "A", "text": "72", "is_correct": False},
            {"label": "B", "text": "144", "is_correct": True},
            {"label": "C", "text": "288", "is_correct": False},
            {"label": "D", "text": "432", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Product Formula Finding Second Number",
        "difficulty": "Medium",
        "question_text": "The HCF of two numbers is 12 and their LCM is 360. If one number is 72, find the other number.",
        "sample_answer": "Formula: A * B = HCF * LCM\n72 * B = 12 * 360\n72 * B = 4320 => B = 60.",
        "tips": "Second Number = (HCF * LCM) / First Number.",
        "options": [
            {"label": "A", "text": "48", "is_correct": False},
            {"label": "B", "text": "60", "is_correct": True},
            {"label": "C", "text": "72", "is_correct": False},
            {"label": "D", "text": "90", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Greatest Divisor with Different Remainders",
        "difficulty": "Medium",
        "question_text": "Find the greatest number that divides 245 and 1029 leaving remainders 5 and 9 respectively.",
        "sample_answer": "Subtract remainders first:\n245 - 5 = 240\n1029 - 9 = 1020\nRequired number = HCF(240, 1020) = 60.",
        "tips": "HCF of (A - r1) and (B - r2).",
        "options": [
            {"label": "A", "text": "30", "is_correct": False},
            {"label": "B", "text": "45", "is_correct": False},
            {"label": "C", "text": "60", "is_correct": True},
            {"label": "D", "text": "120", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Least Number Divisible by 15, 20, 25",
        "difficulty": "Medium",
        "question_text": "Find the least number divisible by 15, 20, and 25.",
        "sample_answer": "15 = 3 * 5\n20 = 2^2 * 5\n25 = 5^2\nLCM = 2^2 * 3 * 5^2 = 4 * 3 * 25 = 300.",
        "tips": "Calculate LCM of 15, 20, and 25.",
        "options": [
            {"label": "A", "text": "150", "is_correct": False},
            {"label": "B", "text": "300", "is_correct": True},
            {"label": "C", "text": "450", "is_correct": False},
            {"label": "D", "text": "600", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Product and HCF to Find LCM",
        "difficulty": "Medium",
        "question_text": "The product of two numbers is 432 and their HCF is 6. Find their LCM.",
        "sample_answer": "Product = HCF * LCM\n432 = 6 * LCM => LCM = 432 / 6 = 72.",
        "tips": "LCM = Product / HCF.",
        "options": [
            {"label": "A", "text": "36", "is_correct": False},
            {"label": "B", "text": "54", "is_correct": False},
            {"label": "C", "text": "72", "is_correct": True},
            {"label": "D", "text": "108", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - HCF of Three Numbers (108, 180, 252)",
        "difficulty": "Medium",
        "question_text": "Find the HCF of 108, 180, and 252.",
        "sample_answer": "108 = 36 * 3\n180 = 36 * 5\n252 = 36 * 7\nHCF = 36.",
        "tips": "Factor out common factors.",
        "options": [
            {"label": "A", "text": "18", "is_correct": False},
            {"label": "B", "text": "27", "is_correct": False},
            {"label": "C", "text": "36", "is_correct": True},
            {"label": "D", "text": "54", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Smallest Number Divisible by 8, 12, 18",
        "difficulty": "Medium",
        "question_text": "Find the smallest number that when divided by 8, 12, and 18 leaves no remainder.",
        "sample_answer": "Required number = LCM(8, 12, 18).\n8 = 2^3, 12 = 2^2 * 3, 18 = 2 * 3^2.\nLCM = 2^3 * 3^2 = 8 * 9 = 72.",
        "tips": "Find LCM of given divisors.",
        "options": [
            {"label": "A", "text": "36", "is_correct": False},
            {"label": "B", "text": "48", "is_correct": False},
            {"label": "C", "text": "72", "is_correct": True},
            {"label": "D", "text": "144", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Finding Second Number given HCF 14 & LCM 840",
        "difficulty": "Medium",
        "question_text": "The LCM of two numbers is 840 and their HCF is 14. If one number is 70, find the other.",
        "sample_answer": "Formula: A * B = HCF * LCM\n70 * B = 14 * 840 => 70 * B = 11760 => B = 168.",
        "tips": "Divide (HCF * LCM) by given number.",
        "options": [
            {"label": "A", "text": "140", "is_correct": False},
            {"label": "B", "text": "168", "is_correct": True},
            {"label": "C", "text": "196", "is_correct": False},
            {"label": "D", "text": "210", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Greatest Common Divisor of 100, 200, 300",
        "difficulty": "Medium",
        "question_text": "Find the greatest number that divides 100, 200, and 300 exactly.",
        "sample_answer": "Required number = HCF(100, 200, 300) = 100.",
        "tips": "HCF of round numbers.",
        "options": [
            {"label": "A", "text": "20", "is_correct": False},
            {"label": "B", "text": "50", "is_correct": False},
            {"label": "C", "text": "100", "is_correct": True},
            {"label": "D", "text": "200", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Common Remainder 3 for Divisors 4, 5, 6, 8",
        "difficulty": "Medium",
        "question_text": "Find the least number which when divided by 4, 5, 6, and 8 leaves remainder 3 in each case.",
        "sample_answer": "LCM(4, 5, 6, 8) = 120.\nRequired number = LCM + remainder = 120 + 3 = 123.",
        "tips": "Add remainder to the LCM.",
        "options": [
            {"label": "A", "text": "123", "is_correct": True},
            {"label": "B", "text": "120", "is_correct": False},
            {"label": "C", "text": "117", "is_correct": False},
            {"label": "D", "text": "243", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - HCF of 144 and 216",
        "difficulty": "Medium",
        "question_text": "Find the HCF of 144 and 216.",
        "sample_answer": "144 = 72 * 2\n216 = 72 * 3\nHCF = 72.",
        "tips": "Look for highest common factor.",
        "options": [
            {"label": "A", "text": "36", "is_correct": False},
            {"label": "B", "text": "48", "is_correct": False},
            {"label": "C", "text": "72", "is_correct": True},
            {"label": "D", "text": "108", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - LCM of 16, 24, and 40",
        "difficulty": "Medium",
        "question_text": "Find the LCM of 16, 24, and 40.",
        "sample_answer": "16 = 2^4\n24 = 2^3 * 3\n40 = 2^3 * 5\nLCM = 2^4 * 3 * 5 = 16 * 15 = 240.",
        "tips": "Use prime factorization method.",
        "options": [
            {"label": "A", "text": "120", "is_correct": False},
            {"label": "B", "text": "180", "is_correct": False},
            {"label": "C", "text": "240", "is_correct": True},
            {"label": "D", "text": "480", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Finding Second Number given HCF 9 & LCM 540",
        "difficulty": "Medium",
        "question_text": "Two numbers have HCF 9 and LCM 540. If one number is 45, find the other.",
        "sample_answer": "45 * B = 9 * 540\n45 * B = 4860 => B = 108.",
        "tips": "Apply product rule.",
        "options": [
            {"label": "A", "text": "90", "is_correct": False},
            {"label": "B", "text": "108", "is_correct": True},
            {"label": "C", "text": "126", "is_correct": False},
            {"label": "D", "text": "135", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Same Remainder Divisor for 1257 and 1575",
        "difficulty": "Medium",
        "question_text": "Find the largest number that divides 1257 and 1575 leaving the same remainder.",
        "sample_answer": "When remainder is the same, required number divides (1575 - 1257) = 318.\nLargest divisor of 318 is 318.\nCheck: 1257 mod 318 = 303, 1575 mod 318 = 303.",
        "tips": "Find HCF of difference between numbers.",
        "options": [
            {"label": "A", "text": "159", "is_correct": False},
            {"label": "B", "text": "318", "is_correct": True},
            {"label": "C", "text": "106", "is_correct": False},
            {"label": "D", "text": "53", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # QUESTIONS 16 TO 30
    {
        "title": "HCF & LCM - Three Bells Ringing at Intervals",
        "difficulty": "Hard",
        "question_text": "Three bells ring at intervals of 18, 24, and 30 minutes. If they ring together at 8:00 AM, when will they ring together again?",
        "sample_answer": "Find LCM(18, 24, 30):\n18 = 2 * 3^2, 24 = 2^3 * 3, 30 = 2 * 3 * 5\nLCM = 2^3 * 3^2 * 5 = 360 minutes = 6 hours.\n8:00 AM + 6 hours = 2:00 PM.",
        "tips": "Convert LCM in minutes to hours.",
        "options": [
            {"label": "A", "text": "12:00 PM", "is_correct": False},
            {"label": "B", "text": "1:30 PM", "is_correct": False},
            {"label": "C", "text": "2:00 PM", "is_correct": True},
            {"label": "D", "text": "4:00 PM", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Least Number with Remainder 7 for 12, 18, 24",
        "difficulty": "Hard",
        "question_text": "Find the least number which when divided by 12, 18, and 24 leaves remainder 7 in each case.",
        "sample_answer": "LCM(12, 18, 24) = 72.\nRequired number = 72 + 7 = 79.",
        "tips": "Add constant remainder to LCM.",
        "options": [
            {"label": "A", "text": "72", "is_correct": False},
            {"label": "B", "text": "79", "is_correct": True},
            {"label": "C", "text": "85", "is_correct": False},
            {"label": "D", "text": "151", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Product and HCF to Find LCM (12288 / 16)",
        "difficulty": "Hard",
        "question_text": "The HCF of two numbers is 16 and their product is 12288. Find their LCM.",
        "sample_answer": "Product = HCF * LCM\n12288 = 16 * LCM => LCM = 12288 / 16 = 768.",
        "tips": "LCM = Product / HCF.",
        "options": [
            {"label": "A", "text": "384", "is_correct": False},
            {"label": "B", "text": "512", "is_correct": False},
            {"label": "C", "text": "768", "is_correct": True},
            {"label": "D", "text": "1024", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Greatest Divisor with Constant Remainder 1",
        "difficulty": "Hard",
        "question_text": "Find the greatest number that divides 101, 201, and 301 leaving remainder 1 in each case.",
        "sample_answer": "Subtract remainder 1:\n101 - 1 = 100, 201 - 1 = 200, 301 - 1 = 300\nRequired number = HCF(100, 200, 300) = 100.",
        "tips": "Find HCF of (number - remainder).",
        "options": [
            {"label": "A", "text": "50", "is_correct": False},
            {"label": "B", "text": "100", "is_correct": True},
            {"label": "C", "text": "150", "is_correct": False},
            {"label": "D", "text": "200", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Least Multiple of 18 Divisible by 24",
        "difficulty": "Hard",
        "question_text": "Find the least multiple of 18 that is exactly divisible by 24.",
        "sample_answer": "Least common multiple of 18 and 24 = LCM(18, 24).\n18 = 2 * 3^2, 24 = 2^3 * 3\nLCM = 2^3 * 3^2 = 72.",
        "tips": "Calculate LCM of 18 and 24.",
        "options": [
            {"label": "A", "text": "36", "is_correct": False},
            {"label": "B", "text": "48", "is_correct": False},
            {"label": "C", "text": "72", "is_correct": True},
            {"label": "D", "text": "144", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Ratio of Numbers 5:7 with HCF 8",
        "difficulty": "Hard",
        "question_text": "Two numbers are in the ratio 5:7. Their HCF is 8. Find the numbers.",
        "sample_answer": "First number = 5 * HCF = 5 * 8 = 40.\nSecond number = 7 * HCF = 7 * 8 = 56.",
        "tips": "Numbers = ratio * HCF.",
        "options": [
            {"label": "A", "text": "30 and 42", "is_correct": False},
            {"label": "B", "text": "40 and 56", "is_correct": True},
            {"label": "C", "text": "45 and 63", "is_correct": False},
            {"label": "D", "text": "50 and 70", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Finding Second Number given HCF 15 & LCM 900",
        "difficulty": "Hard",
        "question_text": "The HCF and LCM of two numbers are 15 and 900 respectively. If one number is 225, find the other.",
        "sample_answer": "225 * B = 15 * 900\n225 * B = 13500 => B = 60.",
        "tips": "Divide (15 * 900) by 225.",
        "options": [
            {"label": "A", "text": "45", "is_correct": False},
            {"label": "B", "text": "60", "is_correct": True},
            {"label": "C", "text": "75", "is_correct": False},
            {"label": "D", "text": "90", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Smallest Dividend with Remainder 2 for 5, 7, 9",
        "difficulty": "Hard",
        "question_text": "Find the smallest number which when divided by 5, 7, and 9 leaves remainder 2 in each case.",
        "sample_answer": "LCM(5, 7, 9) = 315.\nRequired number = 315 + 2 = 317.",
        "tips": "LCM of coprime numbers = 5 * 7 * 9.",
        "options": [
            {"label": "A", "text": "315", "is_correct": False},
            {"label": "B", "text": "317", "is_correct": True},
            {"label": "C", "text": "319", "is_correct": False},
            {"label": "D", "text": "632", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Finding Third Number given LCM 720 & HCF 6",
        "difficulty": "Hard",
        "question_text": "The LCM of three numbers is 720 and their HCF is 6. One number is 90 and another is 120. Find the third number.",
        "sample_answer": "90 = 2 * 3^2 * 5, 120 = 2^3 * 3 * 5.\nLCM = 720 = 2^4 * 3^2 * 5^1.\nThird number C must contribute 2^4 and have 3^1 to satisfy HCF = 6.\nC = 2^4 * 3^1 = 48.",
        "tips": "Analyze prime factorization for LCM and HCF.",
        "options": [
            {"label": "A", "text": "48", "is_correct": True},
            {"label": "B", "text": "60", "is_correct": False},
            {"label": "C", "text": "72", "is_correct": False},
            {"label": "D", "text": "96", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - Same Remainder Divisor for 395 and 455",
        "difficulty": "Hard",
        "question_text": "Find the greatest number that divides 395 and 455 leaving the same remainder.",
        "sample_answer": "Required number divides (455 - 395) = 60.\nGreatest divisor of 60 is 60.\nCheck: 395 mod 60 = 35, 455 mod 60 = 35.",
        "tips": "Find HCF of difference (455 - 395).",
        "options": [
            {"label": "A", "text": "30", "is_correct": False},
            {"label": "B", "text": "45", "is_correct": False},
            {"label": "C", "text": "60", "is_correct": True},
            {"label": "D", "text": "90", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Least Number Divisible by 18, 24, 32, 40",
        "difficulty": "Hard",
        "question_text": "Find the least number divisible by 18, 24, 32, and 40.",
        "sample_answer": "18 = 2 * 3^2, 24 = 2^3 * 3, 32 = 2^5, 40 = 2^3 * 5\nLCM = 2^5 * 3^2 * 5 = 32 * 9 * 5 = 1440.",
        "tips": "Take maximum power of each prime factor.",
        "options": [
            {"label": "A", "text": "720", "is_correct": False},
            {"label": "B", "text": "1440", "is_correct": True},
            {"label": "C", "text": "2880", "is_correct": False},
            {"label": "D", "text": "4320", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Finding Second Number given HCF 18 & LCM 1260",
        "difficulty": "Hard",
        "question_text": "The HCF of two numbers is 18 and their LCM is 1260. If one number is 180, find the other.",
        "sample_answer": "180 * B = 18 * 1260\n180 * B = 22680 => B = 126.",
        "tips": "Apply product rule.",
        "options": [
            {"label": "A", "text": "108", "is_correct": False},
            {"label": "B", "text": "126", "is_correct": True},
            {"label": "C", "text": "144", "is_correct": False},
            {"label": "D", "text": "162", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Three Blinking Lights at Intervals",
        "difficulty": "Hard",
        "question_text": "A room has three blinking lights that blink every 15, 20, and 30 seconds. If they blink together now, after how many seconds will they blink together again?",
        "sample_answer": "Required time = LCM(15, 20, 30) = 60 seconds.",
        "tips": "LCM of 15, 20, and 30.",
        "options": [
            {"label": "A", "text": "30 seconds", "is_correct": False},
            {"label": "B", "text": "45 seconds", "is_correct": False},
            {"label": "C", "text": "60 seconds", "is_correct": True},
            {"label": "D", "text": "120 seconds", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Smallest Addition to 5000 Divisible by 24, 36, 54",
        "difficulty": "Hard",
        "question_text": "Find the least number that must be added to 5000 to make it exactly divisible by 24, 36, and 54.",
        "sample_answer": "LCM(24, 36, 54) = 216.\n5000 / 216 = 23 remainder 32.\nNext multiple = 24 * 216 = 5184.\nNumber to add = 5184 - 5000 = 184.",
        "tips": "Number to add = (LCM - remainder).",
        "options": [
            {"label": "A", "text": "32", "is_correct": False},
            {"label": "B", "text": "184", "is_correct": True},
            {"label": "C", "text": "216", "is_correct": False},
            {"label": "D", "text": "248", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Finding Second Number given HCF 24 & LCM 2016",
        "difficulty": "Hard",
        "question_text": "The HCF of two numbers is 24 and their LCM is 2016. If one number is 336, find the other.",
        "sample_answer": "336 * B = 24 * 2016\n336 * B = 48384 => B = 144.",
        "tips": "B = (24 * 2016) / 336.",
        "options": [
            {"label": "A", "text": "120", "is_correct": False},
            {"label": "B", "text": "144", "is_correct": True},
            {"label": "C", "text": "168", "is_correct": False},
            {"label": "D", "text": "192", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete old HCF & LCM questions to replace with exact 30 questions requested by user
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'HCF & LCM'")
    print("Cleared existing HCF & LCM questions.")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'Aptitude',
            'Number & Arithmetic',
            'HCF & LCM',
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
    print(f"Successfully seeded {len(questions)} HCF & LCM questions into SQLite DB!")

if __name__ == '__main__':
    seed_db()
