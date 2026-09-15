import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db')

questions = [
    {
        "title": "Divisibility - Smallest Digit x for 45x Divisible by 9",
        "difficulty": "Medium",
        "question_text": "Find the smallest digit x such that 45x is divisible by 9.",
        "sample_answer": "Sum of digits = 4 + 5 + x = 9 + x.\nFor (9 + x) to be divisible by 9, the smallest non-negative digit digit x is 0.",
        "tips": "Sum of digits must be divisible by 9.",
        "options": [
            {"label": "A", "text": "0", "is_correct": True},
            {"label": "B", "text": "3", "is_correct": False},
            {"label": "C", "text": "6", "is_correct": False},
            {"label": "D", "text": "9", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Possible Values of x in 7x2 Divisible by 3",
        "difficulty": "Medium",
        "question_text": "A number 7x2 is divisible by 3. Find all possible values of x.",
        "sample_answer": "Sum of digits = 7 + x + 2 = 9 + x.\nFor (9 + x) to be divisible by 3, x can be 0, 3, 6, or 9.",
        "tips": "Test single digit values 0 through 9.",
        "options": [
            {"label": "A", "text": "1, 4, 7", "is_correct": False},
            {"label": "B", "text": "0, 3, 6, 9", "is_correct": True},
            {"label": "C", "text": "2, 5, 8", "is_correct": False},
            {"label": "D", "text": "3, 6", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Addition to Make 7865 Divisible by 11",
        "difficulty": "Medium",
        "question_text": "Find the smallest number that must be added to 7865 to make it divisible by 11.",
        "sample_answer": "7865 / 11 = 715 remainder 0.\nSince 7865 is already exactly divisible by 11, the smallest number to add is 0.",
        "tips": "Check alternating sum of digits.",
        "options": [
            {"label": "A", "text": "0", "is_correct": True},
            {"label": "B", "text": "2", "is_correct": False},
            {"label": "C", "text": "5", "is_correct": False},
            {"label": "D", "text": "9", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Check Divisibility of 123456 by 6",
        "difficulty": "Medium",
        "question_text": "Determine whether 123456 is divisible by 6.",
        "sample_answer": "1. Divisibility by 2: Last digit is 6 (even) => Yes.\n2. Divisibility by 3: Sum of digits = 1+2+3+4+5+6 = 21 (divisible by 3) => Yes.\nSince it is divisible by both 2 and 3, 123456 is divisible by 6.",
        "tips": "Must be divisible by both 2 and 3.",
        "options": [
            {"label": "A", "text": "Yes, it is divisible by 6", "is_correct": True},
            {"label": "B", "text": "No, it is not divisible by 2", "is_correct": False},
            {"label": "C", "text": "No, it is not divisible by 3", "is_correct": False},
            {"label": "D", "text": "Cannot be determined", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Largest 4-Digit Number Divisible by 12",
        "difficulty": "Medium",
        "question_text": "Find the largest 4-digit number divisible by 12.",
        "sample_answer": "Largest 4-digit number = 9999.\n9999 / 12 = 833 remainder 3.\nSubtract remainder: 9999 - 3 = 9996.",
        "tips": "Must be divisible by both 3 and 4.",
        "options": [
            {"label": "A", "text": "9984", "is_correct": False},
            {"label": "B", "text": "9992", "is_correct": False},
            {"label": "C", "text": "9996", "is_correct": True},
            {"label": "D", "text": "9998", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Properties of Numbers Divisible by 4 and 9",
        "difficulty": "Medium",
        "question_text": "A number is divisible by both 4 and 9. Which of the following must be true?",
        "sample_answer": "Since gcd(4, 9) = 1, any number divisible by both 4 and 9 must be divisible by 4 * 9 = 36.",
        "tips": "LCM(4, 9) = 36.",
        "options": [
            {"label": "A", "text": "Divisible by 36", "is_correct": True},
            {"label": "B", "text": "Divisible by 13", "is_correct": False},
            {"label": "C", "text": "Divisible by 18", "is_correct": False},
            {"label": "D", "text": "None of the above", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Find x in 53x4 Divisible by 11",
        "difficulty": "Medium",
        "question_text": "Find the value of x if 53x4 is divisible by 11.",
        "sample_answer": "Alternating sum = (5 + x) - (3 + 4) = (5 + x) - 7 = x - 2.\nFor (x - 2) to equal 0, x = 2.",
        "tips": "Sum of odd-position digits minus sum of even-position digits.",
        "options": [
            {"label": "A", "text": "2", "is_correct": True},
            {"label": "B", "text": "4", "is_correct": False},
            {"label": "C", "text": "6", "is_correct": False},
            {"label": "D", "text": "8", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Count Multiples of 7 Between 1 and 200",
        "difficulty": "Medium",
        "question_text": "How many numbers between 1 and 200 are divisible by 7?",
        "sample_answer": "Count of numbers strictly between 1 and 200 divisible by 7 = floor(199 / 7) = 28.",
        "tips": "Divide 199 by 7.",
        "options": [
            {"label": "A", "text": "27", "is_correct": False},
            {"label": "B", "text": "28", "is_correct": True},
            {"label": "C", "text": "29", "is_correct": False},
            {"label": "D", "text": "30", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Remainder of 98765 / 9",
        "difficulty": "Medium",
        "question_text": "Find the remainder when 98765 is divided by 9.",
        "sample_answer": "Sum of digits = 9 + 8 + 7 + 6 + 5 = 35.\n35 mod 9 = 8.\nRemainder = 8.",
        "tips": "Remainder of a number divided by 9 equals the digital sum mod 9.",
        "options": [
            {"label": "A", "text": "3", "is_correct": False},
            {"label": "B", "text": "5", "is_correct": False},
            {"label": "C", "text": "7", "is_correct": False},
            {"label": "D", "text": "8", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Check Divisibility of 45672 by 8",
        "difficulty": "Medium",
        "question_text": "Determine whether 45672 is divisible by 8.",
        "sample_answer": "Check last 3 digits: 672.\n672 / 8 = 84 (no remainder).\nHence, 45672 is divisible by 8.",
        "tips": "Check if last 3 digits are divisible by 8.",
        "options": [
            {"label": "A", "text": "Yes, it is divisible by 8", "is_correct": True},
            {"label": "B", "text": "No, last 3 digits are not divisible", "is_correct": False},
            {"label": "C", "text": "No, it is an odd number", "is_correct": False},
            {"label": "D", "text": "Cannot be determined", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Smallest 3-Digit Number Divisible by 15",
        "difficulty": "Medium",
        "question_text": "Find the smallest 3-digit number divisible by 15.",
        "sample_answer": "Smallest 3-digit number = 100.\n100 / 15 = 6.66 => Next integer multiple = 7 * 15 = 105.",
        "tips": "First multiple of 15 >= 100.",
        "options": [
            {"label": "A", "text": "100", "is_correct": False},
            {"label": "B", "text": "105", "is_correct": True},
            {"label": "C", "text": "115", "is_correct": False},
            {"label": "D", "text": "120", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Remainder Modulo 4 from Remainder Modulo 8",
        "difficulty": "Medium",
        "question_text": "A number leaves remainder 5 when divided by 8. What remainder will it leave when divided by 4?",
        "sample_answer": "N = 8k + 5 = 4(2k + 1) + 1.\nRemainder when divided by 4 = 5 mod 4 = 1.",
        "tips": "Evaluate (remainder mod 4).",
        "options": [
            {"label": "A", "text": "1", "is_correct": True},
            {"label": "B", "text": "2", "is_correct": False},
            {"label": "C", "text": "3", "is_correct": False},
            {"label": "D", "text": "0", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Greatest Number Less than 500 Divisible by 6 & 8",
        "difficulty": "Medium",
        "question_text": "Find the greatest number less than 500 divisible by both 6 and 8.",
        "sample_answer": "LCM(6, 8) = 24.\nGreatest multiple of 24 less than 500 = floor(499 / 24) * 24 = 20 * 24 = 480.",
        "tips": "Find greatest multiple of LCM(6, 8) < 500.",
        "options": [
            {"label": "A", "text": "464", "is_correct": False},
            {"label": "B", "text": "480", "is_correct": True},
            {"label": "C", "text": "492", "is_correct": False},
            {"label": "D", "text": "496", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Least 3-Digit Number Divisible by 2, 3, 5",
        "difficulty": "Medium",
        "question_text": "A number is divisible by 2, 3, and 5. What is the least possible 3-digit number?",
        "sample_answer": "LCM(2, 3, 5) = 30.\nSmallest 3-digit multiple of 30 = 30 * 4 = 120.",
        "tips": "First multiple of 30 >= 100.",
        "options": [
            {"label": "A", "text": "100", "is_correct": False},
            {"label": "B", "text": "110", "is_correct": False},
            {"label": "C", "text": "120", "is_correct": True},
            {"label": "D", "text": "150", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Subtraction to Make 6743 Divisible by 7",
        "difficulty": "Medium",
        "question_text": "Find the least number to be subtracted from 6743 to make it divisible by 7.",
        "sample_answer": "6743 / 7 = 963 remainder 2.\nSubtract remainder: 2.",
        "tips": "Subtract the remainder.",
        "options": [
            {"label": "A", "text": "2", "is_correct": True},
            {"label": "B", "text": "3", "is_correct": False},
            {"label": "C", "text": "5", "is_correct": False},
            {"label": "D", "text": "6", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # QUESTIONS 16 TO 30
    {
        "title": "Divisibility - Find x in 67x42 Divisible by 11",
        "difficulty": "Hard",
        "question_text": "Find the smallest digit x such that 67x42 is divisible by 11.",
        "sample_answer": "Alternating sum = (6 + x + 2) - (7 + 4) = (8 + x) - 11 = x - 3.\nFor (x - 3) = 0, x = 3.",
        "tips": "Set alternating sum of digits equal to 0.",
        "options": [
            {"label": "A", "text": "1", "is_correct": False},
            {"label": "B", "text": "3", "is_correct": True},
            {"label": "C", "text": "5", "is_correct": False},
            {"label": "D", "text": "7", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Count Numbers Divisible by Neither 2 nor 3",
        "difficulty": "Hard",
        "question_text": "How many numbers from 1 to 1000 are divisible by neither 2 nor 3?",
        "sample_answer": "Divisible by 2 = 500.\nDivisible by 3 = 333.\nDivisible by 6 = 166.\nDivisible by 2 or 3 = 500 + 333 - 166 = 667.\nNeither 2 nor 3 = 1000 - 667 = 333.",
        "tips": "Use Inclusion-Exclusion Principle.",
        "options": [
            {"label": "A", "text": "333", "is_correct": True},
            {"label": "B", "text": "500", "is_correct": False},
            {"label": "C", "text": "667", "is_correct": False},
            {"label": "D", "text": "166", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Largest 5-Digit Number Divisible by 18",
        "difficulty": "Hard",
        "question_text": "Find the largest 5-digit number divisible by 18.",
        "sample_answer": "Largest 5-digit number = 99999.\n99999 / 18 = 5555 remainder 9.\nSubtract remainder: 99999 - 9 = 99990.\n(Ends in 0 => even, digit sum = 36 => div by 9).",
        "tips": "Subtract remainder of 99999 / 18.",
        "options": [
            {"label": "A", "text": "99992", "is_correct": False},
            {"label": "B", "text": "99990", "is_correct": True},
            {"label": "C", "text": "99982", "is_correct": False},
            {"label": "D", "text": "99972", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Remainder of Double the Number Divided by 7",
        "difficulty": "Hard",
        "question_text": "A number when divided by 7 leaves remainder 4. What remainder will twice the number leave when divided by 7?",
        "sample_answer": "Let N = 4 mod 7.\n2N = 2 * 4 = 8 mod 7.\n8 mod 7 = 1.",
        "tips": "Multiply remainder 4 by 2.",
        "options": [
            {"label": "A", "text": "1", "is_correct": True},
            {"label": "B", "text": "2", "is_correct": False},
            {"label": "C", "text": "4", "is_correct": False},
            {"label": "D", "text": "6", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Least 4-Digit Number Divisible by 24",
        "difficulty": "Hard",
        "question_text": "Find the least 4-digit number divisible by 24.",
        "sample_answer": "Smallest 4-digit number = 1000.\n1000 / 24 = 41.66 => Next integer multiple = 42 * 24 = 1008.",
        "tips": "First multiple of 24 >= 1000.",
        "options": [
            {"label": "A", "text": "1000", "is_correct": False},
            {"label": "B", "text": "1008", "is_correct": True},
            {"label": "C", "text": "1016", "is_correct": False},
            {"label": "D", "text": "1024", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Addition to Make 9999 Divisible by 13",
        "difficulty": "Hard",
        "question_text": "Determine the smallest number that should be added to 9999 to make it divisible by 13.",
        "sample_answer": "9999 / 13 = 769 remainder 2.\nNumber to add = 13 - 2 = 11.",
        "tips": "Add (13 - remainder).",
        "options": [
            {"label": "A", "text": "2", "is_correct": False},
            {"label": "B", "text": "7", "is_correct": False},
            {"label": "C", "text": "11", "is_correct": True},
            {"label": "D", "text": "12", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Count Multiples of 4 and 6 from 1 to 500",
        "difficulty": "Hard",
        "question_text": "Find the number of integers from 1 to 500 divisible by both 4 and 6.",
        "sample_answer": "LCM(4, 6) = 12.\nCount = floor(500 / 12) = 41.",
        "tips": "Find multiples of LCM(4, 6) = 12.",
        "options": [
            {"label": "A", "text": "41", "is_correct": True},
            {"label": "B", "text": "42", "is_correct": False},
            {"label": "C", "text": "83", "is_correct": False},
            {"label": "D", "text": "125", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Digit Sum 27 Rule",
        "difficulty": "Hard",
        "question_text": "The sum of digits of a number is 27. Is it necessarily divisible by 9? By 3?",
        "sample_answer": "1. 27 is divisible by 9 (27 / 9 = 3) => Divisible by 9.\n2. 27 is divisible by 3 (27 / 3 = 9) => Divisible by 3.\nHence, the number is divisible by both 9 and 3.",
        "tips": "Divisibility by 9 implies divisibility by 3.",
        "options": [
            {"label": "A", "text": "Yes, divisible by both 9 and 3", "is_correct": True},
            {"label": "B", "text": "Divisible by 3 only", "is_correct": False},
            {"label": "C", "text": "Divisible by 9 only", "is_correct": False},
            {"label": "D", "text": "Divisible by neither", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Greatest Divisor of 1458 and 2547 with Remainder 6",
        "difficulty": "Hard",
        "question_text": "Find the greatest number that divides 1458 and 2547 leaving remainder 6 in each case.",
        "sample_answer": "Subtract remainder 6:\n1458 - 6 = 1452\n2547 - 6 = 2541\nRequired number = HCF(1452, 2541) = 363.",
        "tips": "HCF of (1458 - 6) and (2547 - 6).",
        "options": [
            {"label": "A", "text": "121", "is_correct": False},
            {"label": "B", "text": "242", "is_correct": False},
            {"label": "C", "text": "363", "is_correct": True},
            {"label": "D", "text": "484", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Properties of Numbers Divisible by 72",
        "difficulty": "Hard",
        "question_text": "A number is divisible by 72. Which of the following is definitely true?",
        "sample_answer": "Since 72 = 6 * 12 = 8 * 9, any multiple of 72 is divisible by 6, 8, and 9.",
        "tips": "Check factors of 72.",
        "options": [
            {"label": "A", "text": "(a) Divisible by 6", "is_correct": False},
            {"label": "B", "text": "(b) Divisible by 8", "is_correct": False},
            {"label": "C", "text": "(c) Divisible by 9", "is_correct": False},
            {"label": "D", "text": "(d) All of the above", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Smallest Number Divisible by 7, 9, 11",
        "difficulty": "Hard",
        "question_text": "Find the smallest positive number divisible by 7, 9, and 11.",
        "sample_answer": "Since 7, 9, and 11 are pairwise coprime, LCM = 7 * 9 * 11 = 693.",
        "tips": "Multiply prime/coprime numbers.",
        "options": [
            {"label": "A", "text": "346", "is_correct": False},
            {"label": "B", "text": "693", "is_correct": True},
            {"label": "C", "text": "1386", "is_correct": False},
            {"label": "D", "text": "2079", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Count Numbers Divisible by 5 but not 10",
        "difficulty": "Hard",
        "question_text": "How many numbers between 1 and 1000 are divisible by 5 but not by 10?",
        "sample_answer": "Divisible by 5 = floor(999 / 5) = 199.\nDivisible by 10 = floor(999 / 10) = 99.\nDivisible by 5 but not 10 = 199 - 99 = 100.",
        "tips": "Count odd multiples of 5.",
        "options": [
            {"label": "A", "text": "99", "is_correct": False},
            {"label": "B", "text": "100", "is_correct": True},
            {"label": "C", "text": "101", "is_correct": False},
            {"label": "D", "text": "200", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Remainder of 123456789 / 9",
        "difficulty": "Hard",
        "question_text": "Find the remainder when 123456789 is divided by 9.",
        "sample_answer": "Sum of digits = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45.\n45 mod 9 = 0.\nRemainder = 0.",
        "tips": "Sum of digits 1 to 9 is 45.",
        "options": [
            {"label": "A", "text": "0", "is_correct": True},
            {"label": "B", "text": "1", "is_correct": False},
            {"label": "C", "text": "4", "is_correct": False},
            {"label": "D", "text": "8", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Smallest Addition to 54321 Divisible by 99",
        "difficulty": "Hard",
        "question_text": "Find the least number that must be added to 54321 to make it divisible by 99.",
        "sample_answer": "54321 / 99 = 548 remainder 69.\nNumber to add = 99 - 69 = 30.\n(54321 + 30 = 54351 = 549 * 99).",
        "tips": "Number to add = 99 - remainder.",
        "options": [
            {"label": "A", "text": "30", "is_correct": True},
            {"label": "B", "text": "69", "is_correct": False},
            {"label": "C", "text": "79", "is_correct": False},
            {"label": "D", "text": "99", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Least Number > 100 Divisible by 2, 3, 4, 5, 6, 8",
        "difficulty": "Hard",
        "question_text": "A number is divisible by 2, 3, 4, 5, 6, and 8. What is the least such number greater than 100?",
        "sample_answer": "Find LCM(2, 3, 4, 5, 6, 8):\nLCM = 2^3 * 3 * 5 = 120.\nSince 120 > 100, 120 is the least such number.",
        "tips": "LCM(2, 3, 4, 5, 6, 8) = 120.",
        "options": [
            {"label": "A", "text": "120", "is_correct": True},
            {"label": "B", "text": "180", "is_correct": False},
            {"label": "C", "text": "240", "is_correct": False},
            {"label": "D", "text": "360", "is_correct": False}
        ],
        "correct_option": "A"
    }
]

def seed_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete old Divisibility questions to replace with exact 30 questions requested by user
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Divisibility'")
    print("Cleared existing Divisibility questions.")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'Aptitude',
            'Number & Arithmetic',
            'Divisibility',
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
    print(f"Successfully seeded {len(questions)} Divisibility questions into SQLite DB!")

if __name__ == '__main__':
    seed_db()
