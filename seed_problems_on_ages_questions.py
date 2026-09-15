import sqlite3
import json

questions_data = [
    {
        "q_num": 1,
        "title": "Problems on Ages - Age Ratio",
        "question_text": "The present ages of A and B are in the ratio 4:5. After 6 years, their ages will be in the ratio 5:6. Find their present ages.\n\nA) 20 and 25\nB) 24 and 30\nC) 28 and 35\nD) 32 and 40",
        "options": [
            {"label": "A", "text": "20 and 25", "is_correct": False},
            {"label": "B", "text": "24 and 30", "is_correct": True},
            {"label": "C", "text": "28 and 35", "is_correct": False},
            {"label": "D", "text": "32 and 40", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let present ages be 4x and 5x.\nAfter 6 years:\n(4x + 6) / (5x + 6) = 5 / 6\n=> 6(4x + 6) = 5(5x + 6)\n=> 24x + 36 = 25x + 30\n=> x = 6\n\nPresent age of A = 4 * 6 = 24 years\nPresent age of B = 5 * 6 = 30 years.",
        "tips": "Set up the ratio equation after adding the given years to both numerator and denominator."
    },
    {
        "q_num": 2,
        "title": "Problems on Ages - Father and Son Sum & Past Ratio",
        "question_text": "The sum of the ages of a father and son is 60 years. Four years ago, the father's age was 5 times the son's age. Find their present ages.\n\nA) 44 and 16\nB) 47.33 and 12.67\nC) 48 and 12\nD) 50 and 10",
        "options": [
            {"label": "A", "text": "44 and 16", "is_correct": False},
            {"label": "B", "text": "47.33 and 12.67", "is_correct": True},
            {"label": "C", "text": "48 and 12", "is_correct": False},
            {"label": "D", "text": "50 and 10", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let Son's present age = S, Father's present age = F.\nF + S = 60 => F = 60 - S\nFour years ago:\nF - 4 = 5(S - 4)\n=> (60 - S) - 4 = 5S - 20\n=> 56 - S = 5S - 20\n=> 6S = 76 => S = 12.67 years\nFather's age = 60 - 12.67 = 47.33 years.",
        "tips": "Subtract the past years from both ages before building the multiple equation."
    },
    {
        "q_num": 3,
        "title": "Problems on Ages - Age Difference & Future Multiple",
        "question_text": "A is 8 years older than B. After 4 years, A will be twice as old as B. Find their present ages.\n\nA) 10 and 2\nB) 12 and 4\nC) 14 and 6\nD) 16 and 8",
        "options": [
            {"label": "A", "text": "10 and 2", "is_correct": False},
            {"label": "B", "text": "12 and 4", "is_correct": True},
            {"label": "C", "text": "14 and 6", "is_correct": False},
            {"label": "D", "text": "16 and 8", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let B = x, then A = x + 8.\nAfter 4 years:\n(x + 8) + 4 = 2(x + 4)\n=> x + 12 = 2x + 8\n=> x = 4\n\nPresent age of B = 4 years\nPresent age of A = 4 + 8 = 12 years.",
        "tips": "Age difference remains constant at any point in time."
    },
    {
        "q_num": 4,
        "title": "Problems on Ages - Ratio Progress 3:4 to 5:6",
        "question_text": "The ratio of the present ages of P and Q is 3:4. After 8 years, the ratio becomes 5:6. Find their present ages.\n\nA) 9 and 12\nB) 12 and 16\nC) 15 and 20\nD) 18 and 24",
        "options": [
            {"label": "A", "text": "9 and 12", "is_correct": False},
            {"label": "B", "text": "12 and 16", "is_correct": True},
            {"label": "C", "text": "15 and 20", "is_correct": False},
            {"label": "D", "text": "18 and 24", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let P = 3x and Q = 4x.\n(3x + 8) / (4x + 8) = 5 / 6\n=> 6(3x + 8) = 5(4x + 8)\n=> 18x + 48 = 20x + 40\n=> 2x = 8 => x = 4\n\nPresent age of P = 3 * 4 = 12 years\nPresent age of Q = 4 * 4 = 16 years.",
        "tips": "Observe the constant ratio difference (5-3=2, 6-4=2) corresponding to 8 years."
    },
    {
        "q_num": 5,
        "title": "Problems on Ages - Average Age with Joining Teacher",
        "question_text": "The average age of 5 students is 18 years. If a teacher joins them, the average becomes 23 years. Find the teacher's age.\n\nA) 42 years\nB) 45 years\nC) 48 years\nD) 52 years",
        "options": [
            {"label": "A", "text": "42 years", "is_correct": False},
            {"label": "B", "text": "45 years", "is_correct": False},
            {"label": "C", "text": "48 years", "is_correct": True},
            {"label": "D", "text": "52 years", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Total age of 5 students = 5 * 18 = 90 years.\nTotal age of 6 people (students + teacher) = 6 * 23 = 138 years.\nTeacher's age = 138 - 90 = 48 years.",
        "tips": "New Person's Age = New Total Sum - Old Total Sum."
    },
    {
        "q_num": 6,
        "title": "Problems on Ages - Father 3x Son to 2x Son",
        "question_text": "The present age of a father is 3 times the age of his son. After 10 years, the father's age will be twice the son's age. Find their present ages.\n\nA) 30 and 10\nB) 36 and 12\nC) 45 and 15\nD) 60 and 20",
        "options": [
            {"label": "A", "text": "30 and 10", "is_correct": True},
            {"label": "B", "text": "36 and 12", "is_correct": False},
            {"label": "C", "text": "45 and 15", "is_correct": False},
            {"label": "D", "text": "60 and 20", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Let son's age = x, father's age = 3x.\nAfter 10 years:\n3x + 10 = 2(x + 10)\n=> 3x + 10 = 2x + 20\n=> x = 10\n\nFather's present age = 3 * 10 = 30 years\nSon's present age = 10 years.",
        "tips": "Express father's age directly as a multiple of son's age."
    },
    {
        "q_num": 7,
        "title": "Problems on Ages - Past Ratio and Present Sum",
        "question_text": "Five years ago, the ratio of the ages of A and B was 3:4. Their present ages add up to 52 years. Find their present ages.\n\nA) 20 and 32\nB) 23 and 29\nC) 25 and 27\nD) 22 and 30",
        "options": [
            {"label": "A", "text": "20 and 32", "is_correct": False},
            {"label": "B", "text": "23 and 29", "is_correct": True},
            {"label": "C", "text": "25 and 27", "is_correct": False},
            {"label": "D", "text": "22 and 30", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let ages 5 years ago be 3x and 4x.\nPresent ages = 3x + 5 and 4x + 5.\nSum of present ages = (3x + 5) + (4x + 5) = 7x + 10 = 52\n=> 7x = 42 => x = 6\n\nPresent age of A = 3(6) + 5 = 23 years\nPresent age of B = 4(6) + 5 = 29 years.",
        "tips": "Subtract 2 * 5 = 10 years from the present sum to find past total."
    },
    {
        "q_num": 8,
        "title": "Problems on Ages - Present Sum and Past Multiple",
        "question_text": "The sum of the present ages of A and B is 70 years. Five years ago, A was twice as old as B. Find their present ages.\n\nA) 40 and 30\nB) 45 and 25\nC) 50 and 20\nD) 42 and 28",
        "options": [
            {"label": "A", "text": "40 and 30", "is_correct": False},
            {"label": "B", "text": "45 and 25", "is_correct": True},
            {"label": "C", "text": "50 and 20", "is_correct": False},
            {"label": "D", "text": "42 and 28", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "A + B = 70 => A = 70 - B.\n5 years ago:\nA - 5 = 2(B - 5)\n=> (70 - B) - 5 = 2B - 10\n=> 65 - B = 2B - 10\n=> 3B = 75 => B = 25\nA = 70 - 25 = 45 years.",
        "tips": "Substitute A = 70 - B into the past age relation."
    },
    {
        "q_num": 9,
        "title": "Problems on Ages - Mother and Daughter Difference",
        "question_text": "A mother is 24 years older than her daughter. After 4 years, the mother will be twice the daughter's age. Find their present ages.\n\nA) 40 and 16\nB) 44 and 20\nC) 48 and 24\nD) 36 and 12",
        "options": [
            {"label": "A", "text": "40 and 16", "is_correct": False},
            {"label": "B", "text": "44 and 20", "is_correct": True},
            {"label": "C", "text": "48 and 24", "is_correct": False},
            {"label": "D", "text": "36 and 12", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let daughter's age = x, mother's age = x + 24.\nAfter 4 years:\n(x + 24) + 4 = 2(x + 4)\n=> x + 28 = 2x + 8\n=> x = 20\n\nDaughter = 20 years, Mother = 44 years.",
        "tips": "Age difference remains constant (24 years)."
    },
    {
        "q_num": 10,
        "title": "Problems on Ages - Three Person Average & Age Relationships",
        "question_text": "The average age of A, B, and C is 24 years. A is 6 years older than B, and C is 4 years younger than A. Find their ages.\n\nA) A=26, B=20, C=22\nB) A=27.33, B=21.33, C=23.33\nC) A=28, B=22, C=24\nD) A=30, B=24, C=26",
        "options": [
            {"label": "A", "text": "A=26, B=20, C=22", "is_correct": False},
            {"label": "B", "text": "A=27.33, B=21.33, C=23.33", "is_correct": True},
            {"label": "C", "text": "A=28, B=22, C=24", "is_correct": False},
            {"label": "D", "text": "A=30, B=24, C=26", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Total age = 3 * 24 = 72 years.\nB = A - 6, C = A - 4.\nA + (A - 6) + (A - 4) = 72\n=> 3A - 10 = 72\n=> 3A = 82 => A = 27.33 years\nB = 21.33 years, C = 23.33 years.",
        "tips": "Express all person ages in terms of variable A."
    },
    {
        "q_num": 11,
        "title": "Problems on Ages - Age Ratio Progress 7:2 to 9:4",
        "question_text": "The ratio of the ages of a father and his son is 7:2. After 10 years, their ages will be in the ratio 9:4. Find their present ages.\n\nA) 35 and 10\nB) 42 and 12\nC) 49 and 14\nD) 28 and 8",
        "options": [
            {"label": "A", "text": "35 and 10", "is_correct": True},
            {"label": "B", "text": "42 and 12", "is_correct": False},
            {"label": "C", "text": "49 and 14", "is_correct": False},
            {"label": "D", "text": "28 and 8", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Let father = 7x, son = 2x.\n(7x + 10) / (2x + 10) = 9 / 4\n=> 4(7x + 10) = 9(2x + 10)\n=> 28x + 40 = 18x + 90\n=> 10x = 50 => x = 5\n\nFather = 7 * 5 = 35 years, Son = 2 * 5 = 10 years.",
        "tips": "Notice equal increase in ratio parts (9-7=2, 4-2=2) for 10 years."
    },
    {
        "q_num": 12,
        "title": "Problems on Ages - 4x Son to 2x Son",
        "question_text": "A person's age is 4 times the age of his son. After 12 years, his age will be twice his son's age. Find their present ages.\n\nA) 20 and 5\nB) 24 and 6\nC) 28 and 7\nD) 32 and 8",
        "options": [
            {"label": "A", "text": "20 and 5", "is_correct": False},
            {"label": "B", "text": "24 and 6", "is_correct": True},
            {"label": "C", "text": "28 and 7", "is_correct": False},
            {"label": "D", "text": "32 and 8", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Son = x, Father = 4x.\n4x + 12 = 2(x + 12)\n=> 4x + 12 = 2x + 24\n=> 2x = 12 => x = 6\n\nSon = 6 years, Father = 24 years.",
        "tips": "Solve linear equation for son's age x."
    },
    {
        "q_num": 13,
        "title": "Problems on Ages - Ratio and Difference",
        "question_text": "The ages of A and B are in the ratio 5:7. If their age difference is 10 years, find their present ages.\n\nA) 20 and 30\nB) 25 and 35\nC) 30 and 40\nD) 35 and 45",
        "options": [
            {"label": "A", "text": "20 and 30", "is_correct": False},
            {"label": "B", "text": "25 and 35", "is_correct": True},
            {"label": "C", "text": "30 and 40", "is_correct": False},
            {"label": "D", "text": "35 and 45", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Difference in ratio parts = 7 - 5 = 2 parts.\n2 parts = 10 years => 1 part = 5 years.\nA = 5 * 5 = 25 years\nB = 7 * 5 = 35 years.",
        "tips": "Value of one unit = Difference in ages / Difference in ratio terms."
    },
    {
        "q_num": 14,
        "title": "Problems on Ages - Past and Future Fractional Multiples",
        "question_text": "Six years ago, the age of A was twice the age of B. Six years from now, A will be 1.5 times B's age. Find their present ages.\n\nA) 24 and 15\nB) 30 and 18\nC) 36 and 21\nD) 40 and 22",
        "options": [
            {"label": "A", "text": "24 and 15", "is_correct": False},
            {"label": "B", "text": "30 and 18", "is_correct": True},
            {"label": "C", "text": "36 and 21", "is_correct": False},
            {"label": "D", "text": "40 and 22", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "6 years ago: A - 6 = 2(B - 6) => A = 2B - 6.\n6 years from now: A + 6 = 1.5(B + 6)\n=> (2B - 6) + 6 = 1.5B + 9\n=> 2B = 1.5B + 9 => 0.5B = 9 => B = 18\nA = 2(18) - 6 = 30 years.",
        "tips": "Express present age A in terms of B using the past condition."
    },
    {
        "q_num": 15,
        "title": "Problems on Ages - Family Average Age",
        "question_text": "The average age of a husband and wife is 30 years. After 5 years, the average age of the husband, wife, and their child will be 25 years. Find the present age of the child.\n\nA) 0 years (Newborn)\nB) 2 years\nC) 3 years\nD) 5 years",
        "options": [
            {"label": "A", "text": "0 years (Newborn)", "is_correct": True},
            {"label": "B", "text": "2 years", "is_correct": False},
            {"label": "C", "text": "3 years", "is_correct": False},
            {"label": "D", "text": "5 years", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Present total age (H + W) = 2 * 30 = 60 years.\nAfter 5 years, total age (H + W) = 60 + 5 + 5 = 70 years.\nAfter 5 years, total age (H + W + Child) = 3 * 25 = 75 years.\nChild's age after 5 years = 75 - 70 = 5 years.\nChild's present age = 5 - 5 = 0 years (Newborn).",
        "tips": "Add 5 years to each existing member's age when progressing time."
    },
    {
        "q_num": 16,
        "title": "Problems on Ages - Past to Present Ratio (5:7 and 3:5)",
        "question_text": "The present ages of A and B are in the ratio 5:7. Eight years ago, their ages were in the ratio 3:5. Find their present ages.\n\nA) 15 and 21\nB) 20 and 28\nC) 25 and 35\nD) 30 and 42",
        "options": [
            {"label": "A", "text": "15 and 21", "is_correct": False},
            {"label": "B", "text": "20 and 28", "is_correct": True},
            {"label": "C", "text": "25 and 35", "is_correct": False},
            {"label": "D", "text": "30 and 42", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Present ages = 5x and 7x.\n8 years ago:\n(5x - 8) / (7x - 8) = 3 / 5\n=> 5(5x - 8) = 3(7x - 8)\n=> 25x - 40 = 21x - 24\n=> 4x = 16 => x = 4\n\nPresent age of A = 5 * 4 = 20 years\nPresent age of B = 7 * 4 = 28 years.",
        "tips": "Observe that ratio terms decrease equally by 2 units for 8 years."
    },
    {
        "q_num": 17,
        "title": "Problems on Ages - Father and Son 4:1 to 3:1",
        "question_text": "The ratio of the present ages of a father and son is 4:1. After 8 years, the ratio will become 3:1. Find their present ages.\n\nA) 48 and 12\nB) 64 and 16\nC) 56 and 14\nD) 72 and 18",
        "options": [
            {"label": "A", "text": "48 and 12", "is_correct": False},
            {"label": "B", "text": "64 and 16", "is_correct": True},
            {"label": "C", "text": "56 and 14", "is_correct": False},
            {"label": "D", "text": "72 and 18", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Son = x, Father = 4x.\n(4x + 8) / (x + 8) = 3 / 1\n=> 4x + 8 = 3x + 24\n=> x = 16\n\nSon = 16 years, Father = 4 * 16 = 64 years.",
        "tips": "Cross-multiply after adding 8 years."
    },
    {
        "q_num": 18,
        "title": "Problems on Ages - 2x to 3x 10 Years Ago",
        "question_text": "The present age of A is twice the present age of B. 10 years ago, A was three times as old as B. Find their present ages.\n\nA) 30 and 15\nB) 40 and 20\nC) 50 and 25\nD) 60 and 30",
        "options": [
            {"label": "A", "text": "30 and 15", "is_correct": False},
            {"label": "B", "text": "40 and 20", "is_correct": True},
            {"label": "C", "text": "50 and 25", "is_correct": False},
            {"label": "D", "text": "60 and 30", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "B = x, A = 2x.\n10 years ago:\n2x - 10 = 3(x - 10)\n=> 2x - 10 = 3x - 30\n=> x = 20\n\nPresent age of B = 20 years, A = 40 years.",
        "tips": "Subtract 10 from both ages before applying 3x factor."
    },
    {
        "q_num": 19,
        "title": "Problems on Ages - Two Era Ratio Progress (4:5 to 7:8)",
        "question_text": "Five years ago, the ages of A and B were in the ratio 4:5. Ten years from now, their ages will be in the ratio 7:8. Find their present ages.\n\nA) 20 and 25\nB) 25 and 30\nC) 30 and 35\nD) 35 and 40",
        "options": [
            {"label": "A", "text": "20 and 25", "is_correct": False},
            {"label": "B", "text": "25 and 30", "is_correct": True},
            {"label": "C", "text": "30 and 35", "is_correct": False},
            {"label": "D", "text": "35 and 40", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Ages 5 years ago = 4x and 5x.\n10 years from now = 4x + 15 and 5x + 15 (total gap = 15 years).\n(4x + 15) / (5x + 15) = 7 / 8\n=> 8(4x + 15) = 7(5x + 15)\n=> 32x + 120 = 35x + 105\n=> 3x = 15 => x = 5\n\nPresent age A = 4(5) + 5 = 25 years\nPresent age B = 5(5) + 5 = 30 years.",
        "tips": "Total time difference between -5 and +10 years is 15 years."
    },
    {
        "q_num": 20,
        "title": "Problems on Ages - Three Person Family Past Ratio",
        "question_text": "The sum of the ages of a father, mother, and son is 100 years. Five years ago, the ratio of their ages was 7:6:2. Find their present ages.\n\nA) 40, 35, 15\nB) 44.67, 39, 16.33\nC) 45, 40, 15\nD) 50, 42, 18",
        "options": [
            {"label": "A", "text": "40, 35, 15", "is_correct": False},
            {"label": "B", "text": "44.67, 39, 16.33", "is_correct": True},
            {"label": "C", "text": "45, 40, 15", "is_correct": False},
            {"label": "D", "text": "50, 42, 18", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Sum 5 years ago = 100 - (3 * 5) = 85 years.\nRatio sum = 7 + 6 + 2 = 15 parts.\nValue per part = 85 / 15 = 5.67 years.\nAges 5 years ago: F = 39.67, M = 34, S = 11.33.\nPresent ages: F = 44.67, M = 39, S = 16.33 years.",
        "tips": "Subtract 3 * 5 = 15 years from present sum to get total past sum."
    },
    {
        "q_num": 21,
        "title": "Problems on Ages - 3x to 7x 20 Years Ago",
        "question_text": "A father is currently 3 times as old as his son. Twenty years ago, he was 7 times as old as his son. Find their present ages.\n\nA) 60 and 20\nB) 90 and 30\nC) 75 and 25\nD) 105 and 35",
        "options": [
            {"label": "A", "text": "60 and 20", "is_correct": False},
            {"label": "B", "text": "90 and 30", "is_correct": True},
            {"label": "C", "text": "75 and 25", "is_correct": False},
            {"label": "D", "text": "105 and 35", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Son = x, Father = 3x.\n20 years ago:\n3x - 20 = 7(x - 20)\n=> 3x - 20 = 7x - 140\n=> 4x = 120 => x = 30\n\nSon = 30 years, Father = 90 years.",
        "tips": "Solve linear equation for past multiple relation."
    },
    {
        "q_num": 22,
        "title": "Problems on Ages - Replacement Average Age",
        "question_text": "The average age of 6 people is 28 years. If the youngest person, aged 18 years, is replaced by another person, the average becomes 31 years. Find the age of the new person.\n\nA) 32 years\nB) 36 years\nC) 40 years\nD) 42 years",
        "options": [
            {"label": "A", "text": "32 years", "is_correct": False},
            {"label": "B", "text": "36 years", "is_correct": True},
            {"label": "C", "text": "40 years", "is_correct": False},
            {"label": "D", "text": "42 years", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Initial sum = 6 * 28 = 168 years.\nNew sum = 6 * 31 = 186 years.\nIncrease in sum = 186 - 168 = 18 years.\nNew person's age = Replaced person's age + Increase = 18 + 18 = 36 years.",
        "tips": "New Age = Replaced Age + (Number of Persons * Change in Average)."
    },
    {
        "q_num": 23,
        "title": "Problems on Ages - Compound Ratio & Three Person Sum",
        "question_text": "The ratio of the ages of A and B is 6:7, while the ratio of the ages of B and C is 8:9. If the sum of their ages is 131 years, find the ages of A, B, and C.\n\nA) 32, 40, 45\nB) 37.65, 43.93, 49.42\nC) 40, 48, 54\nD) 36, 42, 48",
        "options": [
            {"label": "A", "text": "32, 40, 45", "is_correct": False},
            {"label": "B", "text": "37.65, 43.93, 49.42", "is_correct": True},
            {"label": "C", "text": "40, 48, 54", "is_correct": False},
            {"label": "D", "text": "36, 42, 48", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Combine ratios A:B:C:\nA:B = 48:56, B:C = 56:63 => A:B:C = 48:56:63.\nTotal ratio parts = 48 + 56 + 63 = 167.\nUnit value = 131 / 167 = 0.7844.\nAges: A = 37.65, B = 43.93, C = 49.42 years.",
        "tips": "First merge ratios by equalizing B's component using LCM."
    },
    {
        "q_num": 24,
        "title": "Problems on Ages - Future Ratio Goal Calculation",
        "question_text": "A mother is 4 times as old as her daughter. After 12 years, she will be twice as old as her daughter. After how many years from now will the mother's age be 1.5 times her daughter's age?\n\nA) 20 years\nB) 24 years\nC) 30 years\nD) 36 years",
        "options": [
            {"label": "A", "text": "20 years", "is_correct": False},
            {"label": "B", "text": "24 years", "is_correct": False},
            {"label": "C", "text": "30 years", "is_correct": True},
            {"label": "D", "text": "36 years", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Daughter = x, Mother = 4x.\nIn 12 years: 4x + 12 = 2(x + 12) => 2x = 12 => x = 6.\nPresent ages: Daughter = 6, Mother = 24.\nLet target be T years from now:\n24 + T = 1.5(6 + T)\n=> 24 + T = 9 + 1.5T\n=> 0.5T = 15 => T = 30 years.",
        "tips": "First find present ages, then solve for future years T."
    },
    {
        "q_num": 25,
        "title": "Problems on Ages - Three Siblings Ratio & Past Sum",
        "question_text": "The present ages of three siblings are in the ratio 2:3:4. Six years ago, the sum of their ages was 54 years. Find their present ages.\n\nA) 12, 18, 24\nB) 16, 24, 32\nC) 20, 30, 40\nD) 14, 21, 28",
        "options": [
            {"label": "A", "text": "12, 18, 24", "is_correct": False},
            {"label": "B", "text": "16, 24, 32", "is_correct": True},
            {"label": "C", "text": "20, 30, 40", "is_correct": False},
            {"label": "D", "text": "14, 21, 28", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let present ages = 2x, 3x, 4x. Sum = 9x.\n6 years ago sum = 9x - 18 = 54 => 9x = 72 => x = 8.\nPresent ages: 2(8) = 16, 3(8) = 24, 4(8) = 32 years.",
        "tips": "Subtract 3 * 6 = 18 years from current sum for past sum."
    },
    {
        "q_num": 26,
        "title": "Problems on Ages - Fractional Age Progression",
        "question_text": "A person's age is equal to one-fourth of the age of his father. After 6 years, the person's age will be one-third of his father's age. Find their present ages.\n\nA) 10 and 40\nB) 12 and 48\nC) 14 and 56\nD) 15 and 60",
        "options": [
            {"label": "A", "text": "10 and 40", "is_correct": False},
            {"label": "B", "text": "12 and 48", "is_correct": True},
            {"label": "C", "text": "14 and 56", "is_correct": False},
            {"label": "D", "text": "15 and 60", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Son = x, Father = 4x.\nIn 6 years: x + 6 = (1/3)(4x + 6)\n=> 3(x + 6) = 4x + 6\n=> 3x + 18 = 4x + 6 => x = 12\nSon = 12 years, Father = 48 years.",
        "tips": "Multiply denominator 3 across to clear fraction."
    },
    {
        "q_num": 27,
        "title": "Problems on Ages - Linear Equation Age Relationship",
        "question_text": "The present age of a father is 5 years more than 3 times the age of his son. Five years from now, the father will be 2.5 times the son's age. Find their present ages.\n\nA) 15 and 3\nB) 20 and 5\nC) 25 and 7\nD) 30 and 8",
        "options": [
            {"label": "A", "text": "15 and 3", "is_correct": False},
            {"label": "B", "text": "20 and 5", "is_correct": True},
            {"label": "C", "text": "25 and 7", "is_correct": False},
            {"label": "D", "text": "30 and 8", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Son = x, Father = 3x + 5.\nIn 5 years:\n(3x + 5) + 5 = 2.5(x + 5)\n=> 3x + 10 = 2.5x + 12.5\n=> 0.5x = 2.5 => x = 5\nSon = 5 years, Father = 3(5) + 5 = 20 years.",
        "tips": "Set up Father's age as 3x + 5."
    },
    {
        "q_num": 28,
        "title": "Problems on Ages - Ratio to Future Target Ratio",
        "question_text": "The ratio of the present ages of A and B is 7:9. Six years ago, the ratio was 5:7. After how many years from now will their ages be in the ratio 4:5?\n\nA) 2 years\nB) 3 years\nC) 4 years\nD) 5 years",
        "options": [
            {"label": "A", "text": "2 years", "is_correct": False},
            {"label": "B", "text": "3 years", "is_correct": True},
            {"label": "C", "text": "4 years", "is_correct": False},
            {"label": "D", "text": "5 years", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Present ages = 7x and 9x.\n6 years ago:\n(7x - 6) / (9x - 6) = 5 / 7\n=> 7(7x - 6) = 5(9x - 6)\n=> 49x - 42 = 45x - 30 => 4x = 12 => x = 3\nPresent ages = 21 and 27.\nTarget ratio 4:5:\n(21 + T) / (27 + T) = 4 / 5\n=> 5(21 + T) = 4(27 + T)\n=> 105 + 5T = 108 + 4T => T = 3 years.",
        "tips": "Solve for present multiplier x first, then for future time T."
    },
    {
        "q_num": 29,
        "title": "Problems on Ages - Father & Daughter Multi-Stage Target",
        "question_text": "The present ages of a father and daughter add up to 70 years. Ten years ago, the father's age was 5 times the daughter's age. After how many years will the father's age be twice the daughter's age?\n\nA) 10 years\nB) 12 years\nC) 15 years\nD) 18 years",
        "options": [
            {"label": "A", "text": "10 years", "is_correct": False},
            {"label": "B", "text": "12 years", "is_correct": False},
            {"label": "C", "text": "15 years", "is_correct": True},
            {"label": "D", "text": "18 years", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "F + D = 70 => F = 70 - D.\n10 years ago:\nF - 10 = 5(D - 10)\n=> (70 - D) - 10 = 5D - 50\n=> 60 - D = 5D - 50 => 6D = 110 => D = 18.33 years, F = 51.67 years.\nTarget T years:\n51.67 + T = 2(18.33 + T)\n=> 51.67 + T = 36.67 + 2T => T = 15 years.",
        "tips": "Calculate present ages first using past sum & multiple."
    },
    {
        "q_num": 30,
        "title": "Problems on Ages - Multi-Stage Three Person Ratio & Future Target",
        "question_text": "The ages of A, B, and C are in the ratio 3:4:5. After 6 years, their ages will be in the ratio 4:5:6. Find their present ages and determine after how many years their ages will be in the ratio 5:6:7.\n\nA) Ages 18, 24, 30 and 12 years\nB) Ages 15, 20, 25 and 10 years\nC) Ages 21, 28, 35 and 14 years\nD) Ages 12, 16, 20 and 8 years",
        "options": [
            {"label": "A", "text": "Ages 18, 24, 30 and 12 years", "is_correct": True},
            {"label": "B", "text": "Ages 15, 20, 25 and 10 years", "is_correct": False},
            {"label": "C", "text": "Ages 21, 28, 35 and 14 years", "is_correct": False},
            {"label": "D", "text": "Ages 12, 16, 20 and 8 years", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Present ages = 3x, 4x, 5x.\nAfter 6 years: (3x + 6) / (4x + 6) = 4 / 5\n=> 5(3x + 6) = 4(4x + 6)\n=> 15x + 30 = 16x + 24 => x = 6.\nPresent ages = 18, 24, 30 years.\nRatio increases by 1 part for every 6 years (3->4->5).\nTherefore, ratio becomes 5:6:7 after 2 * 6 = 12 years.",
        "tips": "Linear step progression: 1 ratio unit corresponds to 6 years."
    }
]

def seed_database():
    conn = sqlite3.connect('instance/interview_portal.db')
    cursor = conn.cursor()
    
    # Clean out existing Problems on Ages questions if any
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Problems on Ages'")
    print(f"Cleared previous Problems on Ages questions.")
    
    for q in questions_data:
        category = "Aptitude"
        sub_category = "Commercial Mathematics"
        topic = "Problems on Ages"
        title = q["title"]
        difficulty = "Medium" if q["q_num"] <= 15 else "Hard"
        question_text = q["question_text"]
        sample_answer = q["sample_answer"]
        tips = q["tips"]
        options_json = json.dumps(q["options"])
        correct_option = q["correct_option"]
        
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options_json, correct_option))
        
    conn.commit()
    print(f"Successfully seeded {len(questions_data)} Problems on Ages questions into instance/interview_portal.db!")
    conn.close()

if __name__ == "__main__":
    seed_database()
