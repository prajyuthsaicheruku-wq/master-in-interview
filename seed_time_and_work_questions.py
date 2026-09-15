import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- MEDIUM LEVEL (Q1 - Q15) ---
    {
        "title": "Time & Work - Combined Work Rate of A and B",
        "difficulty": "Medium",
        "question_text": "A can complete a work in 12 days and B in 18 days. In how many days can they complete it together?",
        "sample_answer": "A's 1 day work = 1/12\nB's 1 day work = 1/18\nTogether 1 day work = 1/12 + 1/18 = (3 + 2)/36 = 5/36\nTotal time taken together = 36/5 = 7.2 days.",
        "tips": "Combined 1-day work = (1/A) + (1/B). Total Days = 1 / (Combined 1-day work).",
        "options": [
            {"label": "A", "text": "6 days", "is_correct": False},
            {"label": "B", "text": "7.2 days", "is_correct": True},
            {"label": "C", "text": "8 days", "is_correct": False},
            {"label": "D", "text": "9 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Remaining Work Fraction",
        "difficulty": "Medium",
        "question_text": "A can do a piece of work in 15 days, B in 20 days. They work together for 5 days. What fraction of work is left?",
        "sample_answer": "A's 1 day work = 1/15, B's 1 day work = 1/20\nTogether 1 day work = 1/15 + 1/20 = (4 + 3)/60 = 7/60\nWork done in 5 days = 5 × (7/60) = 35/60 = 7/12\nFraction of work left = 1 − 7/12 = 5/12.",
        "tips": "Remaining Fraction = 1 − (Days Worked × Combined Rate).",
        "options": [
            {"label": "A", "text": "5/12", "is_correct": True},
            {"label": "B", "text": "7/12", "is_correct": False},
            {"label": "C", "text": "1/3", "is_correct": False},
            {"label": "D", "text": "1/4", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Efficiency Ratio of A and B",
        "difficulty": "Medium",
        "question_text": "A is twice as efficient as B. If B can finish a work in 24 days, how many days will A take?",
        "sample_answer": "Efficiency ratio (A : B) = 2 : 1\nSince Efficiency is inversely proportional to Time taken:\nTime ratio (A : B) = 1 : 2\nIf B takes 24 days, A takes 24 / 2 = 12 days.",
        "tips": "Time taken is inversely proportional to efficiency.",
        "options": [
            {"label": "A", "text": "8 days", "is_correct": False},
            {"label": "B", "text": "10 days", "is_correct": False},
            {"label": "C", "text": "12 days", "is_correct": True},
            {"label": "D", "text": "16 days", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Three Workers Combined Rate",
        "difficulty": "Medium",
        "question_text": "A, B, and C can complete a work in 12, 18, and 24 days respectively. In how many days can they complete it together?",
        "sample_answer": "1 day work = 1/12 + 1/18 + 1/24\nLCM(12, 18, 24) = 72\nCombined 1 day work = (6 + 4 + 3) / 72 = 13/72\nTotal time = 72/13 days = 5 7/13 days.",
        "tips": "Combined 1-day work = 1/A + 1/B + 1/C.",
        "options": [
            {"label": "A", "text": "5 7/13 days", "is_correct": True},
            {"label": "B", "text": "6 days", "is_correct": False},
            {"label": "C", "text": "5 5/13 days", "is_correct": False},
            {"label": "D", "text": "7 days", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Partner Leaves Mid-Way",
        "difficulty": "Medium",
        "question_text": "A can do a work in 10 days and B in 15 days. After working together for 2 days, B leaves. How many more days will A take to finish the remaining work?",
        "sample_answer": "Combined 1 day work = 1/10 + 1/15 = 1/6\nWork done in 2 days together = 2 × (1/6) = 1/3\nRemaining work = 1 − 1/3 = 2/3\nA's 1 day rate = 1/10\nDays for A to finish remaining = (2/3) / (1/10) = 20/3 = 6 2/3 days.",
        "tips": "Calculate work done together, find remaining work, then divide by remaining person's daily rate.",
        "options": [
            {"label": "A", "text": "5 days", "is_correct": False},
            {"label": "B", "text": "6 2/3 days", "is_correct": True},
            {"label": "C", "text": "7 days", "is_correct": False},
            {"label": "D", "text": "8 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Alternate Days Working",
        "difficulty": "Medium",
        "question_text": "A can complete a work in 8 days and B in 12 days. They work on alternate days starting with A. In how many days will the work be completed?",
        "sample_answer": "Total Work = LCM(8, 12) = 24 units.\nA's rate = 3 units/day, B's rate = 2 units/day.\nIn 2 days (Day 1: A, Day 2: B) work done = 3 + 2 = 5 units.\nIn 8 days (4 cycles of 2 days), work done = 4 × 5 = 20 units.\nRemaining work = 24 − 20 = 4 units.\nDay 9 (A's turn): A does 3 units. Total work = 23 units. Remaining = 1 unit.\nDay 10 (B's turn): B needs 1 unit at 2 units/day → takes 1/2 day.\nTotal days = 9.5 days.",
        "tips": "Find work done in one 2-day cycle, determine complete cycles, and calculate remaining days.",
        "options": [
            {"label": "A", "text": "9 days", "is_correct": False},
            {"label": "B", "text": "9.5 days", "is_correct": True},
            {"label": "C", "text": "10 days", "is_correct": False},
            {"label": "D", "text": "10.5 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Individual Time from Partial Work",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days. He works for 5 days and leaves. B completes the remaining work in 10 days. In how many days can B alone complete the work?",
        "sample_answer": "A's work in 5 days = 5/20 = 1/4\nRemaining work = 1 − 1/4 = 3/4\nB completes 3/4 work in 10 days\nTime for B alone = 10 / (3/4) = 40/3 = 13 1/3 days.",
        "tips": "B's Total Time = Days taken by B / Fraction of work B completed.",
        "options": [
            {"label": "A", "text": "12 days", "is_correct": False},
            {"label": "B", "text": "13 1/3 days", "is_correct": True},
            {"label": "C", "text": "15 days", "is_correct": False},
            {"label": "D", "text": "16 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Men and Days Proportionality",
        "difficulty": "Medium",
        "question_text": "12 men can complete a work in 15 days. How many men are required to complete the same work in 9 days?",
        "sample_answer": "M1 × D1 = M2 × D2\n12 × 15 = M2 × 9\n180 = 9 × M2 → M2 = 20 men.",
        "tips": "Use inverse variation formula M1 × D1 = M2 × D2.",
        "options": [
            {"label": "A", "text": "16 men", "is_correct": False},
            {"label": "B", "text": "18 men", "is_correct": False},
            {"label": "C", "text": "20 men", "is_correct": True},
            {"label": "D", "text": "24 men", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Work Done in N Days",
        "difficulty": "Medium",
        "question_text": "A can complete a work in 16 days and B in 24 days. How much work can they complete together in 4 days?",
        "sample_answer": "A's rate = 1/16, B's rate = 1/24\nCombined rate = 1/16 + 1/24 = (3 + 2)/48 = 5/48\nWork done in 4 days = 4 × (5/48) = 5/12.",
        "tips": "Work done = Days Worked × Combined Rate.",
        "options": [
            {"label": "A", "text": "1/3", "is_correct": False},
            {"label": "B", "text": "5/12", "is_correct": True},
            {"label": "C", "text": "1/2", "is_correct": False},
            {"label": "D", "text": "7/12", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Single Worker Rate from Combined Rate",
        "difficulty": "Medium",
        "question_text": "A and B together can do a work in 8 days. A alone can do it in 12 days. In how many days can B alone do it?",
        "sample_answer": "(A + B)'s 1 day work = 1/8\nA's 1 day work = 1/12\nB's 1 day work = 1/8 − 1/12 = (3 − 2)/24 = 1/24\nB alone takes 24 days.",
        "tips": "B's 1-day rate = (A+B)'s 1-day rate − A's 1-day rate.",
        "options": [
            {"label": "A", "text": "16 days", "is_correct": False},
            {"label": "B", "text": "20 days", "is_correct": False},
            {"label": "C", "text": "24 days", "is_correct": True},
            {"label": "D", "text": "32 days", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Workers and Days Inverse Relation",
        "difficulty": "Medium",
        "question_text": "If 8 workers can complete a task in 18 days, how many workers are needed to complete it in 12 days?",
        "sample_answer": "W1 × D1 = W2 × D2\n8 × 18 = W2 × 12\n144 = 12 × W2 → W2 = 12 workers.",
        "tips": "W1 × D1 = W2 × D2.",
        "options": [
            {"label": "A", "text": "10 workers", "is_correct": False},
            {"label": "B", "text": "12 workers", "is_correct": True},
            {"label": "C", "text": "14 workers", "is_correct": False},
            {"label": "D", "text": "16 workers", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Percentage Work to Total Days",
        "difficulty": "Medium",
        "question_text": "A can do 60% of a work in 12 days. How many days will he take to complete the whole work?",
        "sample_answer": "60% of work = 3/5 of work = 12 days\nWhole work (100%) = 12 / (3/5) = 12 × 5 / 3 = 20 days.",
        "tips": "Total Days = Days / Fraction completed.",
        "options": [
            {"label": "A", "text": "18 days", "is_correct": False},
            {"label": "B", "text": "20 days", "is_correct": True},
            {"label": "C", "text": "22 days", "is_correct": False},
            {"label": "D", "text": "25 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Half Work Rates",
        "difficulty": "Medium",
        "question_text": "A does half the work in 10 days. B finishes the remaining half in 15 days. In how many days can they complete the work together?",
        "sample_answer": "A takes 2 × 10 = 20 days for total work.\nB takes 2 × 15 = 30 days for total work.\nTogether 1 day work = 1/20 + 1/30 = (3 + 2)/60 = 5/60 = 1/12\nTotal days together = 12 days.",
        "tips": "First find full work duration for A and B, then combine rates.",
        "options": [
            {"label": "A", "text": "10 days", "is_correct": False},
            {"label": "B", "text": "12 days", "is_correct": True},
            {"label": "C", "text": "15 days", "is_correct": False},
            {"label": "D", "text": "18 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Finding Joined Worker Efficiency",
        "difficulty": "Medium",
        "question_text": "A can complete a work in 30 days. After working for 10 days, he is joined by B and together they finish the remaining work in 8 days. Find B's efficiency.",
        "sample_answer": "A's work in 10 days = 10/30 = 1/3\nRemaining work = 1 − 1/3 = 2/3\nA + B do 2/3 work in 8 days → Combined rate = (2/3) / 8 = 1/12 work/day\nB's 1 day rate = Combined rate − A's rate = 1/12 − 1/30 = (5 − 2)/60 = 3/60 = 1/20\nB takes 20 days (efficiency = 1/20 of work per day).",
        "tips": "Calculate remaining work, combined rate, and subtract A's rate to get B's rate.",
        "options": [
            {"label": "A", "text": "B takes 20 days (1/20 per day)", "is_correct": True},
            {"label": "B", "text": "B takes 24 days (1/24 per day)", "is_correct": False},
            {"label": "C", "text": "B takes 25 days (1/25 per day)", "is_correct": False},
            {"label": "D", "text": "B takes 15 days (1/15 per day)", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Pairwise Combined Rates",
        "difficulty": "Medium",
        "question_text": "A and B together complete a work in 6 days. B and C in 8 days. A and C in 12 days. In how many days can A, B, and C together complete the work?",
        "sample_answer": "(A+B) 1-day work = 1/6\n(B+C) 1-day work = 1/8\n(A+C) 1-day work = 1/12\nSumming all three: 2(A + B + C) = 1/6 + 1/8 + 1/12 = (4 + 3 + 2)/24 = 9/24 = 3/8\n(A + B + C) 1-day work = (3/8) / 2 = 3/16\nTotal days = 16/3 = 5 1/3 days.",
        "tips": "Sum pairwise rates to get 2(A+B+C), divide by 2, then invert.",
        "options": [
            {"label": "A", "text": "4.5 days", "is_correct": False},
            {"label": "B", "text": "5 1/3 days", "is_correct": True},
            {"label": "C", "text": "6 days", "is_correct": False},
            {"label": "D", "text": "7 days", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- HARD LEVEL (Q16 - Q30) ---
    {
        "title": "Time & Work - Work Left for Second Worker",
        "difficulty": "Hard",
        "question_text": "A can do a work in 24 days, B in 36 days. They work together for 8 days and then A leaves. How many more days will B take to finish the remaining work?",
        "sample_answer": "Combined 1 day work = 1/24 + 1/36 = (3 + 2)/72 = 5/72\nWork done in 8 days = 8 × (5/72) = 40/72 = 5/9\nRemaining work = 1 − 5/9 = 4/9\nB's 1 day work = 1/36\nDays for B = (4/9) / (1/36) = 16 days.",
        "tips": "Find work done in 8 days, calculate remaining fraction, divide by B's daily rate.",
        "options": [
            {"label": "A", "text": "12 days", "is_correct": False},
            {"label": "B", "text": "14 days", "is_correct": False},
            {"label": "C", "text": "16 days", "is_correct": True},
            {"label": "D", "text": "18 days", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Third Worker Joining Mid-Way",
        "difficulty": "Hard",
        "question_text": "A can do a work in 15 days and B in 20 days. They work together for 4 days. Then C joins them and the work is completed in 3 more days. If C alone can do the work in x days, find x.",
        "sample_answer": "A+B 1 day work = 1/15 + 1/20 = 7/60\nWork done in first 4 days = 4 × (7/60) = 7/15\nRemaining work = 1 − 7/15 = 8/15\nA+B+C finish 8/15 work in 3 days → Combined rate = (8/15) / 3 = 8/45\nC's rate = 8/45 − 7/60 = (32 − 21) / 180 = 11/180\nx = 180/11 = 16 4/11 days.",
        "tips": "Subtract A and B's rates from combined (A+B+C) rate to find C's rate.",
        "options": [
            {"label": "A", "text": "15 days", "is_correct": False},
            {"label": "B", "text": "16 4/11 days", "is_correct": True},
            {"label": "C", "text": "18 days", "is_correct": False},
            {"label": "D", "text": "20 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Additional Days Needed by A",
        "difficulty": "Hard",
        "question_text": "A and B together can complete a work in 10 days. A alone takes 15 days. They work together for 5 days and then B leaves. How many more days will A need?",
        "sample_answer": "B's 1 day rate = 1/10 − 1/15 = 1/30\nWork done in 5 days together = 5 × (1/10) = 1/2\nRemaining work = 1/2\nA's rate = 1/15\nMore days needed by A = (1/2) / (1/15) = 15/2 = 7.5 days.",
        "tips": "5 days of combined work completes half the work. A takes half of 15 days = 7.5 days.",
        "options": [
            {"label": "A", "text": "5 days", "is_correct": False},
            {"label": "B", "text": "6.5 days", "is_correct": False},
            {"label": "C", "text": "7.5 days", "is_correct": True},
            {"label": "D", "text": "8 days", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Additional Workers Joining",
        "difficulty": "Hard",
        "question_text": "18 men can complete a work in 20 days. After 5 days, 6 more men join. In how many total days will the work be completed?",
        "sample_answer": "Total man-days = 18 × 20 = 360\nMan-days done in first 5 days = 18 × 5 = 90\nRemaining man-days = 360 − 90 = 270\nNew team size = 18 + 6 = 24 men\nAdditional days required = 270 / 24 = 11.25 days\nTotal days = 5 + 11.25 = 16.25 days.",
        "tips": "Total Days = Initial Days + (Remaining Man-Days / New Team Size).",
        "options": [
            {"label": "A", "text": "15 days", "is_correct": False},
            {"label": "B", "text": "16.25 days", "is_correct": True},
            {"label": "C", "text": "17.5 days", "is_correct": False},
            {"label": "D", "text": "18 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Percentage Efficiency Increase",
        "difficulty": "Hard",
        "question_text": "A can do a work in 25 days. B is 25% more efficient than A. In how many days can B complete the work?",
        "sample_answer": "Ratio of efficiency (A : B) = 100 : 125 = 4 : 5\nRatio of time taken (A : B) = 5 : 4\nIf A takes 25 days (5 units = 25 → 1 unit = 5),\nThen B takes 4 units = 4 × 5 = 20 days.",
        "tips": "Time taken by B = Days of A / (1 + Percentage Increase). 25 / 1.25 = 20.",
        "options": [
            {"label": "A", "text": "18 days", "is_correct": False},
            {"label": "B", "text": "20 days", "is_correct": True},
            {"label": "C", "text": "22 days", "is_correct": False},
            {"label": "D", "text": "24 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Daily vs Alternate Day Combination",
        "difficulty": "Hard",
        "question_text": "A can complete a work in 12 days and B in 18 days. If A works every day and B works every alternate day starting from Day 1, how many days will they take to complete the work?",
        "sample_answer": "Total Work = LCM(12, 18) = 36 units.\nA's rate = 3 units/day, B's rate = 2 units/day.\nDay 1 (A + B): 3 + 2 = 5 units.\nDay 2 (A only): 3 units.\nWork done in 2-day cycle = 5 + 3 = 8 units.\nIn 4 cycles (8 days), work done = 4 × 8 = 32 units.\nRemaining work = 36 − 32 = 4 units.\nDay 9 (A + B turn): Rate is 5 units/day. Time needed for 4 units = 4/5 = 0.8 days.\nTotal days = 8 + 0.8 = 8.8 days.",
        "tips": "Find work done in a 2-day cycle and compute partial day at the end.",
        "options": [
            {"label": "A", "text": "8.5 days", "is_correct": False},
            {"label": "B", "text": "8.8 days", "is_correct": True},
            {"label": "C", "text": "9 days", "is_correct": False},
            {"label": "D", "text": "9.2 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Work Left for Second Person",
        "difficulty": "Hard",
        "question_text": "A can do a work in 30 days. B can do it in 45 days. They work together for 6 days, then A leaves. How long will B take to finish the rest?",
        "sample_answer": "1 day combined work = 1/30 + 1/45 = (3 + 2)/90 = 5/90 = 1/18\nWork done in 6 days = 6/18 = 1/3\nRemaining work = 1 − 1/3 = 2/3\nB's daily rate = 1/45\nTime for B = (2/3) / (1/45) = 30 days.",
        "tips": "Remaining fraction / B's daily rate.",
        "options": [
            {"label": "A", "text": "24 days", "is_correct": False},
            {"label": "B", "text": "28 days", "is_correct": False},
            {"label": "C", "text": "30 days", "is_correct": True},
            {"label": "D", "text": "32 days", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Three Workers with One Leaving",
        "difficulty": "Hard",
        "question_text": "A, B, and C can complete a work in 10, 15, and 20 days respectively. They work together for 2 days. Then A leaves. How many more days are needed?",
        "sample_answer": "Combined rate (A+B+C) = 1/10 + 1/15 + 1/20 = (6 + 4 + 3)/60 = 13/60\nWork done in 2 days = 2 × (13/60) = 13/30\nRemaining work = 1 − 13/30 = 17/30\n(B + C) rate = 1/15 + 1/20 = (4 + 3)/60 = 7/60\nMore days needed = (17/30) / (7/60) = 34/7 = 4 6/7 days.",
        "tips": "Calculate 2-day work of all three, then divide remaining work by combined rate of B and C.",
        "options": [
            {"label": "A", "text": "4 6/7 days", "is_correct": True},
            {"label": "B", "text": "5 days", "is_correct": False},
            {"label": "C", "text": "5 1/7 days", "is_correct": False},
            {"label": "D", "text": "6 days", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Workers, Hours, and Days Compound Relation",
        "difficulty": "Hard",
        "question_text": "If 20 workers working 8 hours a day can finish a work in 15 days, how many workers working 10 hours a day are needed to finish it in 12 days?",
        "sample_answer": "M1 × H1 × D1 = M2 × H2 × D2\n20 × 8 × 15 = M2 × 10 × 12\n2400 = 120 × M2 → M2 = 20 workers.",
        "tips": "Use formula M1 × H1 × D1 = M2 × H2 × D2.",
        "options": [
            {"label": "A", "text": "16 workers", "is_correct": False},
            {"label": "B", "text": "18 workers", "is_correct": False},
            {"label": "C", "text": "20 workers", "is_correct": True},
            {"label": "D", "text": "24 workers", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Percentage of Work Remaining",
        "difficulty": "Hard",
        "question_text": "A can do a work in 40 days, B in 60 days. They work together for 12 days. What percentage of work remains?",
        "sample_answer": "Combined 1 day work = 1/40 + 1/60 = (3 + 2)/120 = 5/120 = 1/24\nWork done in 12 days = 12 × (1/24) = 1/2 = 50%\nRemaining work percentage = 100% − 50% = 50%.",
        "tips": "Remaining Percentage = 100% − (12 × Combined Rate × 100%).",
        "options": [
            {"label": "A", "text": "40%", "is_correct": False},
            {"label": "B", "text": "45%", "is_correct": False},
            {"label": "C", "text": "50%", "is_correct": True},
            {"label": "D", "text": "60%", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Pairwise Systems to Individual Time",
        "difficulty": "Hard",
        "question_text": "A and B together can do a work in 9 days. B and C together in 12 days. A and C together in 18 days. Find the time taken by A alone.",
        "sample_answer": "2(A + B + C) 1-day work = 1/9 + 1/12 + 1/18 = (4 + 3 + 2)/36 = 9/36 = 1/4\n(A + B + C) 1-day work = 1/8\nA's 1-day rate = (A + B + C) − (B + C) = 1/8 − 1/12 = (3 − 2)/24 = 1/24\nA alone takes 24 days.",
        "tips": "Subtract (B+C) rate from (A+B+C) rate to get A's rate.",
        "options": [
            {"label": "A", "text": "18 days", "is_correct": False},
            {"label": "B", "text": "20 days", "is_correct": False},
            {"label": "C", "text": "24 days", "is_correct": True},
            {"label": "D", "text": "36 days", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Efficiency Percentage with Combined Days",
        "difficulty": "Hard",
        "question_text": "A is 50% more efficient than B. Together they complete a work in 8 days. In how many days can A alone complete the work?",
        "sample_answer": "Efficiency of B = 1, Efficiency of A = 1.5 = 3/2\nCombined efficiency = 1 + 1.5 = 2.5 = 5/2\nTotal Work = Combined Efficiency × Days = (5/2) × 8 = 20 units\nDays for A alone = Total Work / A's Efficiency = 20 / (3/2) = 40/3 = 13 1/3 days.",
        "tips": "Total Work = Combined Efficiency × Days. A's Time = Total Work / A's Efficiency.",
        "options": [
            {"label": "A", "text": "12 days", "is_correct": False},
            {"label": "B", "text": "13 1/3 days", "is_correct": True},
            {"label": "C", "text": "15 days", "is_correct": False},
            {"label": "D", "text": "16 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Workers Leaving After Partial Work",
        "difficulty": "Hard",
        "question_text": "15 men can complete a work in 24 days. After 8 days, 5 men leave. How many more days are required?",
        "sample_answer": "Total man-days = 15 × 24 = 360\nMan-days completed in 8 days = 15 × 8 = 120\nRemaining man-days = 360 − 120 = 240\nRemaining men = 15 − 5 = 10 men\nMore days required = 240 / 10 = 24 days.",
        "tips": "Remaining Man-Days / Remaining Men = Additional Days.",
        "options": [
            {"label": "A", "text": "20 days", "is_correct": False},
            {"label": "B", "text": "22 days", "is_correct": False},
            {"label": "C", "text": "24 days", "is_correct": True},
            {"label": "D", "text": "28 days", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Periodic Alternate Absence",
        "difficulty": "Hard",
        "question_text": "A can do a work in 18 days. B can do the same work in 24 days. They work together but every third day only A works. In how many days will the work be completed?",
        "sample_answer": "Total Work = LCM(18, 24) = 72 units.\nA's rate = 4 units/day, B's rate = 3 units/day.\nDay 1 (A + B): 4 + 3 = 7 units.\nDay 2 (A + B): 4 + 3 = 7 units.\nDay 3 (A only): 4 units.\nWork in 3-day cycle = 7 + 7 + 4 = 18 units.\nNumber of 3-day cycles needed = 72 / 18 = 4 cycles.\nTotal days = 4 × 3 = 12 days.",
        "tips": "Calculate work in 3-day pattern: (A+B) + (A+B) + A.",
        "options": [
            {"label": "A", "text": "11 days", "is_correct": False},
            {"label": "B", "text": "12 days", "is_correct": True},
            {"label": "C", "text": "13 days", "is_correct": False},
            {"label": "D", "text": "14 days", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Pairwise System to Find C Alone",
        "difficulty": "Hard",
        "question_text": "A and B together can complete a work in 4 days, B and C in 6 days, and A and C in 8 days. In how many days can C alone complete the work?",
        "sample_answer": "2(A + B + C) 1-day work = 1/4 + 1/6 + 1/8 = (6 + 4 + 3)/24 = 13/24\n(A + B + C) 1-day work = 13/48\nC's 1-day work = (A + B + C) − (A + B) = 13/48 − 1/4 = 13/48 − 12/48 = 1/48\nC alone takes 48 days.",
        "tips": "C's rate = (A+B+C) rate − (A+B) rate.",
        "options": [
            {"label": "A", "text": "36 days", "is_correct": False},
            {"label": "B", "text": "40 days", "is_correct": False},
            {"label": "C", "text": "48 days", "is_correct": True},
            {"label": "D", "text": "52 days", "is_correct": False}
        ],
        "correct_option": "C"
    }
]

def seed_time_and_work():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Time & Work'")
            print(f"Deleted old 'Time & Work' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Time-Based Problems',
                    'Time & Work',
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
    seed_time_and_work()
