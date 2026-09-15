import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- FIND NEXT / MISSING TERM (Q1 - Q25) ---
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 2, 5, 10, 17, 26, ?",
        "sample_answer": "Pattern: n² + 1 for n = 1, 2, 3, 4, 5, 6\n1² + 1 = 2\n2² + 1 = 5\n3² + 1 = 10\n4² + 1 = 17\n5² + 1 = 26\n6² + 1 = 37.",
        "tips": "Observe the differences: +3, +5, +7, +9, +11.",
        "options": [
            {"label": "A", "text": "35", "is_correct": False},
            {"label": "B", "text": "37", "is_correct": True},
            {"label": "C", "text": "38", "is_correct": False},
            {"label": "D", "text": "40", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 3, 8, 15, 24, 35, ?",
        "sample_answer": "Pattern: n² − 1 for n = 2, 3, 4, 5, 6, 7\n2² − 1 = 3\n3² − 1 = 8\n4² − 1 = 15\n5² − 1 = 24\n6² − 1 = 35\n7² − 1 = 48.",
        "tips": "Observe differences: +5, +7, +9, +11, +13.",
        "options": [
            {"label": "A", "text": "44", "is_correct": False},
            {"label": "B", "text": "46", "is_correct": False},
            {"label": "C", "text": "48", "is_correct": True},
            {"label": "D", "text": "50", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 1, 4, 9, 16, 25, ?",
        "sample_answer": "Pattern: Consecutive squares n² for n = 1, 2, 3, 4, 5, 6\n1² = 1, 2² = 4, 3² = 9, 4² = 16, 5² = 25, 6² = 36.",
        "tips": "Squares of consecutive natural numbers.",
        "options": [
            {"label": "A", "text": "30", "is_correct": False},
            {"label": "B", "text": "32", "is_correct": False},
            {"label": "C", "text": "36", "is_correct": True},
            {"label": "D", "text": "49", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the missing number: 7, 14, 28, 56, ?, 224",
        "sample_answer": "Pattern: Multiply by 2 at each step (×2).\n7 × 2 = 14\n14 × 2 = 28\n28 × 2 = 56\n56 × 2 = 112\n112 × 2 = 224.",
        "tips": "Geometric progression with common ratio = 2.",
        "options": [
            {"label": "A", "text": "98", "is_correct": False},
            {"label": "B", "text": "110", "is_correct": False},
            {"label": "C", "text": "112", "is_correct": True},
            {"label": "D", "text": "120", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the missing number: 5, 11, 23, 47, ?, 191",
        "sample_answer": "Pattern: ×2 + 1\n5 × 2 + 1 = 11\n11 × 2 + 1 = 23\n23 × 2 + 1 = 47\n47 × 2 + 1 = 95\n95 × 2 + 1 = 191.",
        "tips": "Each number is double the previous plus 1.",
        "options": [
            {"label": "A", "text": "93", "is_correct": False},
            {"label": "B", "text": "95", "is_correct": True},
            {"label": "C", "text": "96", "is_correct": False},
            {"label": "D", "text": "99", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 2, 4, 8, 16, 32, ?",
        "sample_answer": "Pattern: Powers of 2 (2ⁿ for n = 1, 2, 3, 4, 5, 6)\n2¹ = 2, 2² = 4, 2³ = 8, 2⁴ = 16, 2⁵ = 32, 2⁶ = 64.",
        "tips": "Double each term.",
        "options": [
            {"label": "A", "text": "48", "is_correct": False},
            {"label": "B", "text": "56", "is_correct": False},
            {"label": "C", "text": "64", "is_correct": True},
            {"label": "D", "text": "72", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 1, 8, 27, 64, 125, ?",
        "sample_answer": "Pattern: Perfect cubes n³ for n = 1, 2, 3, 4, 5, 6\n1³ = 1, 2³ = 8, 3³ = 27, 4³ = 64, 5³ = 125, 6³ = 216.",
        "tips": "Cubes of natural numbers.",
        "options": [
            {"label": "A", "text": "180", "is_correct": False},
            {"label": "B", "text": "216", "is_correct": True},
            {"label": "C", "text": "243", "is_correct": False},
            {"label": "D", "text": "256", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern: n² + 1 for n = 2, 3, 4, 5, 6, 7\n2² + 1 = 5, 3² + 1 = 10, 4² + 1 = 17, 5² + 1 = 26, 6² + 1 = 37, 7² + 1 = 50.",
        "tips": "Observe differences: +5, +7, +9, +11, +13.",
        "options": [
            {"label": "A", "text": "46", "is_correct": False},
            {"label": "B", "text": "48", "is_correct": False},
            {"label": "C", "text": "50", "is_correct": True},
            {"label": "D", "text": "52", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 3, 7, 13, 21, 31, ?",
        "sample_answer": "Pattern: Add consecutive even numbers (+4, +6, +8, +10, +12)\n3 + 4 = 7\n7 + 6 = 13\n13 + 8 = 21\n21 + 10 = 31\n31 + 12 = 43.",
        "tips": "Differences are +4, +6, +8, +10, +12.",
        "options": [
            {"label": "A", "text": "41", "is_correct": False},
            {"label": "B", "text": "43", "is_correct": True},
            {"label": "C", "text": "45", "is_correct": False},
            {"label": "D", "text": "47", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 2, 5, 11, 23, 47, ?",
        "sample_answer": "Pattern: ×2 + 1\n2 × 2 + 1 = 5\n5 × 2 + 1 = 11\n11 × 2 + 1 = 23\n23 × 2 + 1 = 47\n47 × 2 + 1 = 95.",
        "tips": "Double the previous number and add 1.",
        "options": [
            {"label": "A", "text": "93", "is_correct": False},
            {"label": "B", "text": "94", "is_correct": False},
            {"label": "C", "text": "95", "is_correct": True},
            {"label": "D", "text": "97", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 1, 2, 6, 24, 120, ?",
        "sample_answer": "Pattern: Multiply by consecutive integers (×2, ×3, ×4, ×5, ×6)\n1 × 2 = 2\n2 × 3 = 6\n6 × 4 = 24\n24 × 5 = 120\n120 × 6 = 720.",
        "tips": "Factorial sequence: n!",
        "options": [
            {"label": "A", "text": "600", "is_correct": False},
            {"label": "B", "text": "720", "is_correct": True},
            {"label": "C", "text": "840", "is_correct": False},
            {"label": "D", "text": "960", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 2, 3, 5, 9, 17, 33, ?",
        "sample_answer": "Pattern: ×2 − 1\n2 × 2 − 1 = 3\n3 × 2 − 1 = 5\n5 × 2 − 1 = 9\n9 × 2 − 1 = 17\n17 × 2 − 1 = 33\n33 × 2 − 1 = 65.",
        "tips": "Double the previous number and subtract 1.",
        "options": [
            {"label": "A", "text": "61", "is_correct": False},
            {"label": "B", "text": "63", "is_correct": False},
            {"label": "C", "text": "65", "is_correct": True},
            {"label": "D", "text": "67", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 8, 14, 26, 50, 98, ?",
        "sample_answer": "Pattern: ×2 − 2\n8 × 2 − 2 = 14\n14 × 2 − 2 = 26\n26 × 2 − 2 = 50\n50 × 2 − 2 = 98\n98 × 2 − 2 = 194.",
        "tips": "Double the previous number and subtract 2.",
        "options": [
            {"label": "A", "text": "186", "is_correct": False},
            {"label": "B", "text": "192", "is_correct": False},
            {"label": "C", "text": "194", "is_correct": True},
            {"label": "D", "text": "198", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 3, 9, 21, 45, 93, ?",
        "sample_answer": "Pattern: ×2 + 3\n3 × 2 + 3 = 9\n9 × 2 + 3 = 21\n21 × 2 + 3 = 45\n45 × 2 + 3 = 93\n93 × 2 + 3 = 189.",
        "tips": "Double the previous number and add 3.",
        "options": [
            {"label": "A", "text": "183", "is_correct": False},
            {"label": "B", "text": "189", "is_correct": True},
            {"label": "C", "text": "192", "is_correct": False},
            {"label": "D", "text": "195", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Medium",
        "question_text": "Find the next number in the series: 1, 5, 14, 30, 55, ?",
        "sample_answer": "Pattern: Add consecutive square numbers (+2², +3², +4², +5², +6²)\n1 + 4 = 5\n5 + 9 = 14\n14 + 16 = 30\n30 + 25 = 55\n55 + 36 = 91.",
        "tips": "Differences are 4, 9, 16, 25, 36.",
        "options": [
            {"label": "A", "text": "85", "is_correct": False},
            {"label": "B", "text": "90", "is_correct": False},
            {"label": "C", "text": "91", "is_correct": True},
            {"label": "D", "text": "95", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # --- HARD LEVEL (Q16 - Q30) ---
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 2, 7, 15, 26, 40, ?",
        "sample_answer": "Pattern: Differences are +5, +8, +11, +14, +17 (increasing by 3)\n2 + 5 = 7\n7 + 8 = 15\n15 + 11 = 26\n26 + 14 = 40\n40 + 17 = 57.",
        "tips": "Second difference is constant (+3).",
        "options": [
            {"label": "A", "text": "54", "is_correct": False},
            {"label": "B", "text": "56", "is_correct": False},
            {"label": "C", "text": "57", "is_correct": True},
            {"label": "D", "text": "60", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 11, 22, 44, 88, 176, ?",
        "sample_answer": "Pattern: Double each term (×2)\n11 × 2 = 22\n22 × 2 = 44\n44 × 2 = 88\n88 × 2 = 176\n176 × 2 = 352.",
        "tips": "Geometric sequence with multiplier = 2.",
        "options": [
            {"label": "A", "text": "320", "is_correct": False},
            {"label": "B", "text": "340", "is_correct": False},
            {"label": "C", "text": "352", "is_correct": True},
            {"label": "D", "text": "364", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 4, 18, 48, 100, 180, ?",
        "sample_answer": "Pattern: n³ − n² = n²(n − 1) for n = 2, 3, 4, 5, 6, 7\n2³ − 2² = 4\n3³ − 3² = 18\n4³ − 4² = 48\n5³ − 5² = 100\n6³ − 6² = 180\n7³ − 7² = 343 − 49 = 294.",
        "tips": "Each term is n³ − n².",
        "options": [
            {"label": "A", "text": "252", "is_correct": False},
            {"label": "B", "text": "270", "is_correct": False},
            {"label": "C", "text": "294", "is_correct": True},
            {"label": "D", "text": "315", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 7, 21, 43, 73, 111, ?",
        "sample_answer": "Pattern: Differences are +14, +22, +30, +38, +46 (increasing by +8)\n7 + 14 = 21\n21 + 22 = 43\n43 + 30 = 73\n73 + 38 = 111\n111 + 46 = 157.",
        "tips": "Difference of differences is +8.",
        "options": [
            {"label": "A", "text": "149", "is_correct": False},
            {"label": "B", "text": "155", "is_correct": False},
            {"label": "C", "text": "157", "is_correct": True},
            {"label": "D", "text": "161", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 2, 12, 36, 80, 150, ?",
        "sample_answer": "Pattern: n³ + n² = n²(n + 1) for n = 1, 2, 3, 4, 5, 6\n1³ + 1² = 2\n2³ + 2² = 12\n3³ + 3² = 36\n4³ + 4² = 80\n5³ + 5² = 150\n6³ + 6² = 216 + 36 = 252.",
        "tips": "Each term is n³ + n².",
        "options": [
            {"label": "A", "text": "216", "is_correct": False},
            {"label": "B", "text": "240", "is_correct": False},
            {"label": "C", "text": "252", "is_correct": True},
            {"label": "D", "text": "280", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 1, 2, 4, 7, 11, 16, ?",
        "sample_answer": "Pattern: Add consecutive integers (+1, +2, +3, +4, +5, +6)\n1 + 1 = 2\n2 + 2 = 4\n4 + 3 = 7\n7 + 4 = 11\n11 + 5 = 16\n16 + 6 = 22.",
        "tips": "Differences increase by +1 at each step.",
        "options": [
            {"label": "A", "text": "20", "is_correct": False},
            {"label": "B", "text": "21", "is_correct": False},
            {"label": "C", "text": "22", "is_correct": True},
            {"label": "D", "text": "24", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 3, 6, 18, 72, 360, ?",
        "sample_answer": "Pattern: Multiply by 2, 3, 4, 5, 6\n3 × 2 = 6\n6 × 3 = 18\n18 × 4 = 72\n72 × 5 = 360\n360 × 6 = 2160.",
        "tips": "Multipliers are 2, 3, 4, 5, 6.",
        "options": [
            {"label": "A", "text": "1800", "is_correct": False},
            {"label": "B", "text": "2160", "is_correct": True},
            {"label": "C", "text": "2400", "is_correct": False},
            {"label": "D", "text": "2520", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 5, 7, 13, 25, 49, ?",
        "sample_answer": "Pattern: ×2 − 3\n5 × 2 − 3 = 7\n7 × 2 − 3 = 13\n13 × 2 − 3 = 25\n25 × 2 − 3 = 49\n49 × 2 − 3 = 95.",
        "tips": "Double the previous number and subtract 3.",
        "options": [
            {"label": "A", "text": "89", "is_correct": False},
            {"label": "B", "text": "93", "is_correct": False},
            {"label": "C", "text": "95", "is_correct": True},
            {"label": "D", "text": "97", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 2, 10, 30, 68, 130, ?",
        "sample_answer": "Pattern: n³ + n for n = 1, 2, 3, 4, 5, 6\n1³ + 1 = 2\n2³ + 2 = 10\n3³ + 3 = 30\n4³ + 4 = 68\n5³ + 5 = 130\n6³ + 6 = 216 + 6 = 222.",
        "tips": "Each term is n³ + n.",
        "options": [
            {"label": "A", "text": "210", "is_correct": False},
            {"label": "B", "text": "216", "is_correct": False},
            {"label": "C", "text": "222", "is_correct": True},
            {"label": "D", "text": "230", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the next number in the series: 1, 4, 13, 40, 121, ?",
        "sample_answer": "Pattern: ×3 + 1\n1 × 3 + 1 = 4\n4 × 3 + 1 = 13\n13 × 3 + 1 = 40\n40 × 3 + 1 = 121\n121 × 3 + 1 = 364.",
        "tips": "Triple the previous number and add 1.",
        "options": [
            {"label": "A", "text": "350", "is_correct": False},
            {"label": "B", "text": "360", "is_correct": False},
            {"label": "C", "text": "364", "is_correct": True},
            {"label": "D", "text": "372", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # --- WRONG TERM IN SERIES (Q26 - Q30) ---
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the wrong number in the series: 2, 6, 12, 20, 30, 41, 56",
        "sample_answer": "Pattern: n(n + 1)\n1 × 2 = 2\n2 × 3 = 6\n3 × 4 = 12\n4 × 5 = 20\n5 × 6 = 30\n6 × 7 = 42 (Given 41)\n7 × 8 = 56.\nHence, 41 is wrong and should be 42.",
        "tips": "Product sequence n(n+1): 6 × 7 = 42, not 41.",
        "options": [
            {"label": "A", "text": "20", "is_correct": False},
            {"label": "B", "text": "30", "is_correct": False},
            {"label": "C", "text": "41", "is_correct": True},
            {"label": "D", "text": "56", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the wrong number in the series: 3, 9, 27, 81, 244, 729",
        "sample_answer": "Pattern: Powers of 3 (3ⁿ for n = 1, 2, 3, 4, 5, 6)\n3¹ = 3, 3² = 9, 3³ = 27, 3⁴ = 81, 3⁵ = 243, 3⁶ = 729.\nThe term 244 is incorrect and should be 243.",
        "tips": "Powers of 3: 3⁵ = 243.",
        "options": [
            {"label": "A", "text": "81", "is_correct": False},
            {"label": "B", "text": "244", "is_correct": True},
            {"label": "C", "text": "729", "is_correct": False},
            {"label": "D", "text": "27", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the wrong number in the series: 5, 10, 20, 40, 85, 160",
        "sample_answer": "Pattern: Multiply by 2 at each step\n5 × 2 = 10\n10 × 2 = 20\n20 × 2 = 40\n40 × 2 = 80 (Given 85)\n80 × 2 = 160.\nThe term 85 is wrong and should be 80.",
        "tips": "40 × 2 = 80, not 85.",
        "options": [
            {"label": "A", "text": "20", "is_correct": False},
            {"label": "B", "text": "40", "is_correct": False},
            {"label": "C", "text": "85", "is_correct": True},
            {"label": "D", "text": "160", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the wrong number in the series: 1, 4, 9, 16, 26, 36",
        "sample_answer": "Pattern: Perfect squares n² for n = 1, 2, 3, 4, 5, 6\n1² = 1, 2² = 4, 3² = 9, 4² = 16, 5² = 25 (Given 26), 6² = 36.\nThe term 26 is incorrect and should be 25.",
        "tips": "5² = 25, not 26.",
        "options": [
            {"label": "A", "text": "9", "is_correct": False},
            {"label": "B", "text": "16", "is_correct": False},
            {"label": "C", "text": "26", "is_correct": True},
            {"label": "D", "text": "36", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series",
        "difficulty": "Hard",
        "question_text": "Find the wrong number in the series: 7, 14, 28, 56, 110, 224",
        "sample_answer": "Pattern: Multiply by 2 at each step\n7 × 2 = 14\n14 × 2 = 28\n28 × 2 = 56\n56 × 2 = 112 (Given 110)\n112 × 2 = 224.\nThe term 110 is wrong and should be 112.",
        "tips": "56 × 2 = 112, not 110.",
        "options": [
            {"label": "A", "text": "28", "is_correct": False},
            {"label": "B", "text": "56", "is_correct": False},
            {"label": "C", "text": "110", "is_correct": True},
            {"label": "D", "text": "224", "is_correct": False}
        ],
        "correct_option": "C"
    }
]

def seed_number_series():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Number Series'")
            print(f"Deleted old 'Number Series' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Logical Reasoning',
                    'Number Series',
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
    seed_number_series()
