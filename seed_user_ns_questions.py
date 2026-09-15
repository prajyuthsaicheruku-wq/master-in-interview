import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db')

questions = [
    {
        "title": "Number System - Remainder of 2^50 / 7",
        "difficulty": "Medium",
        "question_text": "Find the remainder when 2^50 is divided by 7.",
        "sample_answer": "2^1 = 2 mod 7\n2^2 = 4 mod 7\n2^3 = 8 = 1 mod 7 (cyclicity of 3).\n50 = 3 * 16 + 2.\n2^50 = (2^3)^16 * 2^2 = (1)^16 * 4 = 4 mod 7.\nHence, the remainder is 4.",
        "tips": "Identify the power cycle of base 2 modulo 7.",
        "options": [
            {"label": "A", "text": "2", "is_correct": False},
            {"label": "B", "text": "4", "is_correct": True},
            {"label": "C", "text": "1", "is_correct": False},
            {"label": "D", "text": "5", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Two-Digit Number & Reversal",
        "difficulty": "Medium",
        "question_text": "The sum of digits of a two-digit number is 12. If the digits are reversed, the number decreases by 18. Find the number.",
        "sample_answer": "Let the number be 10x + y.\nSum of digits: x + y = 12.\nReversed number: 10y + x.\nGiven: (10x + y) - (10y + x) = 18 => 9(x - y) = 18 => x - y = 2.\nSolving x + y = 12 and x - y = 2:\n2x = 14 => x = 7, y = 5.\nThe required number is 75.",
        "tips": "Use algebraic equations for digits x and y.",
        "options": [
            {"label": "A", "text": "75", "is_correct": True},
            {"label": "B", "text": "57", "is_correct": False},
            {"label": "C", "text": "84", "is_correct": False},
            {"label": "D", "text": "93", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Greatest 4-Digit Number Divisible by 15",
        "difficulty": "Medium",
        "question_text": "Find the greatest 4-digit number divisible by 15.",
        "sample_answer": "Greatest 4-digit number = 9999.\n9999 / 15 = 666 remainder 9.\nSubtract remainder: 9999 - 9 = 9990.\nCheck: 9990 ends in 0 (divisible by 5) and sum of digits = 27 (divisible by 3).",
        "tips": "Divisibility by 15 requires divisibility by both 3 and 5.",
        "options": [
            {"label": "A", "text": "9995", "is_correct": False},
            {"label": "B", "text": "9990", "is_correct": True},
            {"label": "C", "text": "9985", "is_correct": False},
            {"label": "D", "text": "9975", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Count Multiples of 3 and 5",
        "difficulty": "Medium",
        "question_text": "How many numbers between 1 and 500 are divisible by both 3 and 5?",
        "sample_answer": "Numbers divisible by both 3 and 5 must be divisible by LCM(3, 5) = 15.\nNumbers strictly between 1 and 500 divisible by 15 = floor(499 / 15) = 33.",
        "tips": "Use LCM of 3 and 5.",
        "options": [
            {"label": "A", "text": "33", "is_correct": True},
            {"label": "B", "text": "34", "is_correct": False},
            {"label": "C", "text": "32", "is_correct": False},
            {"label": "D", "text": "30", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Unit Digit of 7^2026",
        "difficulty": "Medium",
        "question_text": "Find the unit digit of 7^2026.",
        "sample_answer": "Cyclicity of powers of 7: 7^1 = 7, 7^2 = 9, 7^3 = 3, 7^4 = 1 (cycle length = 4).\nDivide power by 4: 2026 mod 4 = 2.\nUnit digit = 7^2 mod 10 = 9.",
        "tips": "Unit digit repeats in cycles of 4.",
        "options": [
            {"label": "A", "text": "7", "is_correct": False},
            {"label": "B", "text": "9", "is_correct": True},
            {"label": "C", "text": "3", "is_correct": False},
            {"label": "D", "text": "1", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Remainder of Squared Dividend",
        "difficulty": "Medium",
        "question_text": "A number leaves remainder 5 when divided by 8. What remainder will its square leave when divided by 8?",
        "sample_answer": "Let N = 8k + 5.\nN^2 = (8k + 5)^2 = 64k^2 + 80k + 25 = 8(8k^2 + 10k + 3) + 1.\nRemainder = 25 mod 8 = 1.",
        "tips": "Square the remainder directly: 5^2 = 25.",
        "options": [
            {"label": "A", "text": "1", "is_correct": True},
            {"label": "B", "text": "3", "is_correct": False},
            {"label": "C", "text": "5", "is_correct": False},
            {"label": "D", "text": "7", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Relation Between HCF, LCM & Numbers",
        "difficulty": "Medium",
        "question_text": "The LCM of two numbers is 180 and their HCF is 12. If one number is 36, find the other.",
        "sample_answer": "Formula: First Number * Second Number = HCF * LCM.\n36 * B = 12 * 180.\n36 * B = 2160 => B = 60.",
        "tips": "Product of two numbers equals Product of their HCF and LCM.",
        "options": [
            {"label": "A", "text": "48", "is_correct": False},
            {"label": "B", "text": "54", "is_correct": False},
            {"label": "C", "text": "60", "is_correct": True},
            {"label": "D", "text": "72", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Divisibility Test for 11",
        "difficulty": "Medium",
        "question_text": "Find the smallest number that must be added to 9876 to make it divisible by 11.",
        "sample_answer": "9876 / 11 = 897 remainder 9.\nNext multiple of 11 = 898 * 11 = 9878.\nSmallest number to add = 9878 - 9876 = 2.",
        "tips": "Add (11 - remainder).",
        "options": [
            {"label": "A", "text": "2", "is_correct": True},
            {"label": "B", "text": "5", "is_correct": False},
            {"label": "C", "text": "9", "is_correct": False},
            {"label": "D", "text": "7", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Remainder of 9999 / 13",
        "difficulty": "Medium",
        "question_text": "What is the remainder when 9999 is divided by 13?",
        "sample_answer": "9999 = 13 * 769 + 2.\nHence, the remainder when 9999 is divided by 13 is 2.",
        "tips": "Perform standard long division.",
        "options": [
            {"label": "A", "text": "2", "is_correct": True},
            {"label": "B", "text": "4", "is_correct": False},
            {"label": "C", "text": "6", "is_correct": False},
            {"label": "D", "text": "8", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Total Factors of 360",
        "difficulty": "Medium",
        "question_text": "Find the number of factors of 360.",
        "sample_answer": "Prime factorization of 360 = 2^3 * 3^2 * 5^1.\nTotal number of factors = (3 + 1)(2 + 1)(1 + 1) = 4 * 3 * 2 = 24.",
        "tips": "Add 1 to each prime exponent and multiply.",
        "options": [
            {"label": "A", "text": "18", "is_correct": False},
            {"label": "B", "text": "20", "is_correct": False},
            {"label": "C", "text": "24", "is_correct": True},
            {"label": "D", "text": "36", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Missing Digit for Divisibility by 9",
        "difficulty": "Medium",
        "question_text": "A number is divisible by 9. If its digits are 4, x, 7, and 5, find x.",
        "sample_answer": "Divisibility rule for 9: Sum of digits must be a multiple of 9.\nSum = 4 + x + 7 + 5 = 16 + x.\nNext multiple of 9 is 18 => 16 + x = 18 => x = 2.",
        "tips": "Sum of digits must be divisible by 9.",
        "options": [
            {"label": "A", "text": "2", "is_correct": True},
            {"label": "B", "text": "4", "is_correct": False},
            {"label": "C", "text": "6", "is_correct": False},
            {"label": "D", "text": "8", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Least Common Multiple of 12, 15, 20",
        "difficulty": "Medium",
        "question_text": "Find the least number divisible by 12, 15, and 20.",
        "sample_answer": "Find LCM(12, 15, 20):\n12 = 2^2 * 3\n15 = 3 * 5\n20 = 2^2 * 5\nLCM = 2^2 * 3 * 5 = 60.",
        "tips": "Take highest powers of all prime factors.",
        "options": [
            {"label": "A", "text": "30", "is_correct": False},
            {"label": "B", "text": "60", "is_correct": True},
            {"label": "C", "text": "120", "is_correct": False},
            {"label": "D", "text": "180", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - HCF and Product to Find LCM",
        "difficulty": "Medium",
        "question_text": "The product of two numbers is 216 and their HCF is 6. Find their LCM.",
        "sample_answer": "Product of numbers = HCF * LCM.\n216 = 6 * LCM => LCM = 216 / 6 = 36.",
        "tips": "LCM = Product / HCF.",
        "options": [
            {"label": "A", "text": "24", "is_correct": False},
            {"label": "B", "text": "36", "is_correct": True},
            {"label": "C", "text": "48", "is_correct": False},
            {"label": "D", "text": "72", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Last Two Digits of 13^25",
        "difficulty": "Medium",
        "question_text": "Find the last two digits of 13^25.",
        "sample_answer": "13^20 = 01 mod 100.\n13^5 = 371293 = 93 mod 100.\n13^25 = (13^20) * (13^5) = 01 * 93 = 93 mod 100.\nHence, the last two digits are 93.",
        "tips": "Use Euler's totient theorem: 13^20 mod 100 = 1.",
        "options": [
            {"label": "A", "text": "13", "is_correct": False},
            {"label": "B", "text": "43", "is_correct": False},
            {"label": "C", "text": "73", "is_correct": False},
            {"label": "D", "text": "93", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Trailing Zeros in 100!",
        "difficulty": "Medium",
        "question_text": "How many trailing zeros are there in 100!?",
        "sample_answer": "Number of trailing zeros = floor(100 / 5) + floor(100 / 25) = 20 + 4 = 24.",
        "tips": "Count prime factors of 5 in n!.",
        "options": [
            {"label": "A", "text": "20", "is_correct": False},
            {"label": "B", "text": "24", "is_correct": True},
            {"label": "C", "text": "25", "is_correct": False},
            {"label": "D", "text": "28", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # HARD LEVEL QUESTIONS (16 - 30)
    {
        "title": "Number System - Remainder of 3^100 / 17",
        "difficulty": "Hard",
        "question_text": "Find the remainder when 3^100 is divided by 17.",
        "sample_answer": "By Fermat's Little Theorem, 3^16 = 1 mod 17.\n100 = 16 * 6 + 4.\n3^100 = (3^16)^6 * 3^4 = (1)^6 * 81 = 81 mod 17.\n81 = 17 * 4 + 13 => Remainder = 13.",
        "tips": "Apply Fermat's Little Theorem: a^(p-1) = 1 mod p.",
        "options": [
            {"label": "A", "text": "9", "is_correct": False},
            {"label": "B", "text": "13", "is_correct": True},
            {"label": "C", "text": "15", "is_correct": False},
            {"label": "D", "text": "1", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Common Remainder Problem",
        "difficulty": "Hard",
        "question_text": "Find the smallest number that leaves remainder 2 when divided by 3, 4, and 5.",
        "sample_answer": "Required Number = LCM(3, 4, 5) * k + 2.\nLCM(3, 4, 5) = 60.\nFor smallest positive integer, k = 1 => Number = 60 * 1 + 2 = 62.",
        "tips": "Number = LCM(divisors) * k + remainder.",
        "options": [
            {"label": "A", "text": "58", "is_correct": False},
            {"label": "B", "text": "62", "is_correct": True},
            {"label": "C", "text": "122", "is_correct": False},
            {"label": "D", "text": "182", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Remainder Multiplier Property",
        "difficulty": "Hard",
        "question_text": "If a number is divided by 13, it leaves remainder 8. What remainder will 5x that number leave when divided by 13?",
        "sample_answer": "Let N = 8 mod 13.\n5N = 5 * 8 = 40 mod 13.\n40 = 13 * 3 + 1 => Remainder = 1.",
        "tips": "Multiply the remainder directly by 5.",
        "options": [
            {"label": "A", "text": "1", "is_correct": True},
            {"label": "B", "text": "3", "is_correct": False},
            {"label": "C", "text": "5", "is_correct": False},
            {"label": "D", "text": "8", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Highest Power of 2 in 1000!",
        "difficulty": "Hard",
        "question_text": "Find the highest power of 2 that divides 1000!.",
        "sample_answer": "Legendre's Formula for 2 in 1000!:\nfloor(1000/2) + floor(1000/4) + floor(1000/8) + floor(1000/16) + floor(1000/32) + floor(1000/64) + floor(1000/128) + floor(1000/256) + floor(1000/512)\n= 500 + 250 + 125 + 62 + 31 + 15 + 7 + 3 + 1 = 994.",
        "tips": "Sum floor(n / 2^k) for k = 1, 2, 3...",
        "options": [
            {"label": "A", "text": "990", "is_correct": False},
            {"label": "B", "text": "994", "is_correct": True},
            {"label": "C", "text": "998", "is_correct": False},
            {"label": "D", "text": "1000", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Unit Digit of 17^123",
        "difficulty": "Hard",
        "question_text": "Find the unit digit of 17^123.",
        "sample_answer": "Unit digit depends on 7^123.\nCyclicity of 7 is 4.\n123 mod 4 = 3.\n7^3 = 343 => Unit digit is 3.",
        "tips": "Check remainder when exponent is divided by 4.",
        "options": [
            {"label": "A", "text": "1", "is_correct": False},
            {"label": "B", "text": "3", "is_correct": True},
            {"label": "C", "text": "7", "is_correct": False},
            {"label": "D", "text": "9", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Inclusion-Exclusion Principle",
        "difficulty": "Hard",
        "question_text": "How many numbers from 1 to 1000 are not divisible by either 2 or 5?",
        "sample_answer": "Divisible by 2 = 500.\nDivisible by 5 = 200.\nDivisible by 10 = 100.\nDivisible by 2 or 5 = 500 + 200 - 100 = 600.\nNot divisible by either 2 or 5 = 1000 - 600 = 400.",
        "tips": "Total - n(A U B).",
        "options": [
            {"label": "A", "text": "400", "is_correct": True},
            {"label": "B", "text": "500", "is_correct": False},
            {"label": "C", "text": "600", "is_correct": False},
            {"label": "D", "text": "700", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Remainder of 11^50 / 12",
        "difficulty": "Hard",
        "question_text": "Find the remainder when 11^50 is divided by 12.",
        "sample_answer": "11 = -1 mod 12.\n11^50 = (-1)^50 mod 12 = 1 mod 12.\nHence, the remainder is 1.",
        "tips": "Use negative remainders: 11 = -1 mod 12.",
        "options": [
            {"label": "A", "text": "1", "is_correct": True},
            {"label": "B", "text": "5", "is_correct": False},
            {"label": "C", "text": "7", "is_correct": False},
            {"label": "D", "text": "11", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - HCF and LCM Product Application",
        "difficulty": "Hard",
        "question_text": "The HCF of two numbers is 16 and their LCM is 960. If one number is 160, find the other.",
        "sample_answer": "First Number * Second Number = HCF * LCM.\n160 * B = 16 * 960 => 160 * B = 15360 => B = 96.",
        "tips": "Divide product of HCF and LCM by the given number.",
        "options": [
            {"label": "A", "text": "80", "is_correct": False},
            {"label": "B", "text": "96", "is_correct": True},
            {"label": "C", "text": "112", "is_correct": False},
            {"label": "D", "text": "128", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Perfect Square Multiplier",
        "difficulty": "Hard",
        "question_text": "Find the least number that should be multiplied by 432 to make it a perfect square.",
        "sample_answer": "Prime factorization of 432 = 2^4 * 3^3.\nFor a perfect square, all prime exponents must be even.\nExponent of 2 is 4 (even).\nExponent of 3 is 3 (odd) => Needs one more 3 (3^4).\nHence, least multiplier = 3.",
        "tips": "Check odd exponents in prime factorization.",
        "options": [
            {"label": "A", "text": "2", "is_correct": False},
            {"label": "B", "text": "3", "is_correct": True},
            {"label": "C", "text": "6", "is_correct": False},
            {"label": "D", "text": "9", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Remainder of 8^75 / 13",
        "difficulty": "Hard",
        "question_text": "What is the remainder when 8^75 is divided by 13?",
        "sample_answer": "By Fermat's Little Theorem, 8^12 = 1 mod 13.\n75 = 12 * 6 + 3.\n8^75 = (8^12)^6 * 8^3 = (1)^6 * 512 = 512 mod 13.\n512 = 13 * 39 + 5 => Remainder = 5.",
        "tips": "8^3 = 512 = 5 mod 13.",
        "options": [
            {"label": "A", "text": "2", "is_correct": False},
            {"label": "B", "text": "5", "is_correct": True},
            {"label": "C", "text": "8", "is_correct": False},
            {"label": "D", "text": "11", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Count Divisors of Prime Factorization",
        "difficulty": "Hard",
        "question_text": "Find the number of divisors of 2^5 * 3^4 * 5^2.",
        "sample_answer": "Total Divisors = (5 + 1)(4 + 1)(2 + 1) = 6 * 5 * 3 = 90.",
        "tips": "Formula: (a+1)(b+1)(c+1)...",
        "options": [
            {"label": "A", "text": "60", "is_correct": False},
            {"label": "B", "text": "80", "is_correct": False},
            {"label": "C", "text": "90", "is_correct": True},
            {"label": "D", "text": "120", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Remainder of Cubed Dividend",
        "difficulty": "Hard",
        "question_text": "A number when divided by 7 leaves remainder 3. What remainder will its cube leave when divided by 7?",
        "sample_answer": "Let N = 3 mod 7.\nN^3 = 3^3 = 27 mod 7.\n27 = 7 * 3 + 6 => Remainder = 6.",
        "tips": "Cube the remainder: 3^3 = 27 mod 7.",
        "options": [
            {"label": "A", "text": "1", "is_correct": False},
            {"label": "B", "text": "3", "is_correct": False},
            {"label": "C", "text": "5", "is_correct": False},
            {"label": "D", "text": "6", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Smallest Dividend with Constant Remainder",
        "difficulty": "Hard",
        "question_text": "Find the smallest number which when divided by 6, 8, and 15 leaves remainder 5 in each case.",
        "sample_answer": "Number = LCM(6, 8, 15) * k + 5.\nLCM(6, 8, 15) = 120.\nFor smallest positive number, k = 1 => 120 * 1 + 5 = 125.",
        "tips": "Number = LCM(6, 8, 15) + remainder.",
        "options": [
            {"label": "A", "text": "120", "is_correct": False},
            {"label": "B", "text": "125", "is_correct": True},
            {"label": "C", "text": "130", "is_correct": False},
            {"label": "D", "text": "245", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Highest Power of 5 in 200!",
        "difficulty": "Hard",
        "question_text": "Find the highest power of 5 that divides 200!.",
        "sample_answer": "Legendre's formula: floor(200/5) + floor(200/25) + floor(200/125) = 40 + 8 + 1 = 49.",
        "tips": "Sum floor(200 / 5^k) for k = 1, 2, 3...",
        "options": [
            {"label": "A", "text": "40", "is_correct": False},
            {"label": "B", "text": "48", "is_correct": False},
            {"label": "C", "text": "49", "is_correct": True},
            {"label": "D", "text": "50", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - 3-Digit Number Word Problem",
        "difficulty": "Hard",
        "question_text": "A number consists of three digits. The sum of digits is 15. The hundreds digit is twice the units digit. The tens digit is 3 more than the units digit. Find the number.",
        "sample_answer": "Let digits be H, T, U.\nH + T + U = 15.\nH = 2U.\nT = U + 3.\nSubstitute: (2U) + (U + 3) + U = 15 => 4U + 3 = 15 => 4U = 12 => U = 3.\nThen H = 2(3) = 6, and T = 3 + 3 = 6.\nRequired number = 663.",
        "tips": "Express all digits in terms of units digit U.",
        "options": [
            {"label": "A", "text": "663", "is_correct": True},
            {"label": "B", "text": "636", "is_correct": False},
            {"label": "C", "text": "366", "is_correct": False},
            {"label": "D", "text": "843", "is_correct": False}
        ],
        "correct_option": "A"
    }
]

def seed_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Remove previous Number System questions to replace with exact user questions
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Number System'")
    print("Cleared existing Number System questions.")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'Aptitude',
            'Number & Arithmetic',
            'Number System',
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
    print(f"Successfully seeded {len(questions)} Number System questions into SQLite DB!")

if __name__ == '__main__':
    seed_db()
