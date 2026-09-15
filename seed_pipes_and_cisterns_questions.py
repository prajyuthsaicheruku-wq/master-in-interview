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
        "title": "Pipes & Cisterns - Fraction Filled in 3 Hours",
        "difficulty": "Medium",
        "question_text": "A pipe can fill a tank in 12 hours. How much of the tank will it fill in 3 hours?",
        "sample_answer": "Rate of pipe = 1/12 of tank per hour.\nIn 3 hours, fraction filled = 3 × (1/12) = 3/12 = 1/4 of the tank.",
        "tips": "Fraction filled = Time elapsed / Total time to fill.",
        "options": [
            {"label": "A", "text": "1/6", "is_correct": False},
            {"label": "B", "text": "1/4", "is_correct": True},
            {"label": "C", "text": "1/3", "is_correct": False},
            {"label": "D", "text": "1/2", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets Combined Time",
        "difficulty": "Medium",
        "question_text": "Pipe A fills a tank in 10 hours and Pipe B fills it in 15 hours. How long will they take to fill the tank together?",
        "sample_answer": "Pipe A 1-hr rate = 1/10, Pipe B 1-hr rate = 1/15\nCombined 1-hr rate = 1/10 + 1/15 = (3 + 2)/30 = 5/30 = 1/6\nTotal time together = 6 hours.",
        "tips": "Combined Rate = 1/A + 1/B. Total Time = 1 / Combined Rate.",
        "options": [
            {"label": "A", "text": "5 hours", "is_correct": False},
            {"label": "B", "text": "6 hours", "is_correct": True},
            {"label": "C", "text": "7.5 hours", "is_correct": False},
            {"label": "D", "text": "8 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - One Inlet and One Outlet",
        "difficulty": "Medium",
        "question_text": "A pipe can fill a tank in 8 hours. Another pipe can empty it in 24 hours. If both are opened together, how long will it take to fill the tank?",
        "sample_answer": "Inlet rate = 1/8, Outlet rate = 1/24\nNet filling rate = 1/8 − 1/24 = (3 − 1)/24 = 2/24 = 1/12\nTotal time to fill = 12 hours.",
        "tips": "Net Rate = Inlet Rate − Outlet Rate.",
        "options": [
            {"label": "A", "text": "10 hours", "is_correct": False},
            {"label": "B", "text": "12 hours", "is_correct": True},
            {"label": "C", "text": "14 hours", "is_correct": False},
            {"label": "D", "text": "16 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Fraction Filled by Two Pipes",
        "difficulty": "Medium",
        "question_text": "Pipe A fills a tank in 20 hours and Pipe B in 30 hours. What fraction of the tank is filled in 4 hours when both pipes are opened?",
        "sample_answer": "Combined 1-hr rate = 1/20 + 1/30 = (3 + 2)/60 = 5/60 = 1/12\nFraction filled in 4 hours = 4 × (1/12) = 4/12 = 1/3.",
        "tips": "Fraction filled = Hours elapsed × Combined Rate.",
        "options": [
            {"label": "A", "text": "1/4", "is_correct": False},
            {"label": "B", "text": "1/3", "is_correct": True},
            {"label": "C", "text": "2/5", "is_correct": False},
            {"label": "D", "text": "1/2", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Portion Filled in 6 Hours",
        "difficulty": "Medium",
        "question_text": "A pipe fills a tank in 16 hours. How much of the tank is filled in 6 hours?",
        "sample_answer": "Hourly filling rate = 1/16\nFraction filled in 6 hours = 6/16 = 3/8.",
        "tips": "Fraction = Hours elapsed / Total hours.",
        "options": [
            {"label": "A", "text": "1/4", "is_correct": False},
            {"label": "B", "text": "3/8", "is_correct": True},
            {"label": "C", "text": "1/2", "is_correct": False},
            {"label": "D", "text": "5/8", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Remaining Unfilled Fraction",
        "difficulty": "Medium",
        "question_text": "Pipe A fills a tank in 12 hours and Pipe B in 18 hours. Both are opened together for 3 hours. What fraction of the tank remains unfilled?",
        "sample_answer": "Combined 1-hr rate = 1/12 + 1/18 = (3 + 2)/36 = 5/36\nFraction filled in 3 hours = 3 × (5/36) = 15/36 = 5/12\nFraction remaining unfilled = 1 − 5/12 = 7/12.",
        "tips": "Unfilled Fraction = 1 − (Hours Elapsed × Combined Rate).",
        "options": [
            {"label": "A", "text": "5/12", "is_correct": False},
            {"label": "B", "text": "7/12", "is_correct": True},
            {"label": "C", "text": "1/3", "is_correct": False},
            {"label": "D", "text": "2/3", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Second Pipe Joined Later",
        "difficulty": "Medium",
        "question_text": "A tank is filled by Pipe A in 15 hours. After 5 hours, Pipe B is opened and together they fill the remaining tank in 4 hours. Find the time taken by Pipe B alone.",
        "sample_answer": "Pipe A in 5 hours = 5/15 = 1/3 of tank\nRemaining tank = 1 − 1/3 = 2/3\n(A + B) fill 2/3 in 4 hours → Combined rate = (2/3) / 4 = 1/6\nPipe B rate = 1/6 − 1/15 = (5 − 2)/30 = 3/30 = 1/10\nTime taken by Pipe B alone = 10 hours.",
        "tips": "B's rate = Combined rate − A's rate.",
        "options": [
            {"label": "A", "text": "8 hours", "is_correct": False},
            {"label": "B", "text": "10 hours", "is_correct": True},
            {"label": "C", "text": "12 hours", "is_correct": False},
            {"label": "D", "text": "15 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Fractional Combined Time",
        "difficulty": "Medium",
        "question_text": "Two pipes can fill a tank in 6 hours and 8 hours respectively. How long will they take together?",
        "sample_answer": "Combined 1-hr rate = 1/6 + 1/8 = (4 + 3)/24 = 7/24\nTotal time together = 24/7 hours = 3 3/7 hours.",
        "tips": "Total Time = (A × B) / (A + B) = (6 × 8) / (6 + 8) = 48/14 = 24/7.",
        "options": [
            {"label": "A", "text": "3 3/7 hours", "is_correct": True},
            {"label": "B", "text": "3.5 hours", "is_correct": False},
            {"label": "C", "text": "4 hours", "is_correct": False},
            {"label": "D", "text": "4 1/2 hours", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Slow Outlet Pipe",
        "difficulty": "Medium",
        "question_text": "Pipe A fills a tank in 24 hours. Pipe B empties it in 36 hours. If both are opened together, how long will it take to fill the tank?",
        "sample_answer": "Inlet rate = 1/24, Outlet rate = 1/36\nNet rate = 1/24 − 1/36 = (3 − 2)/72 = 1/72\nTotal time = 72 hours.",
        "tips": "Net Rate = 1/24 − 1/36 = 1/72.",
        "options": [
            {"label": "A", "text": "60 hours", "is_correct": False},
            {"label": "B", "text": "72 hours", "is_correct": True},
            {"label": "C", "text": "84 hours", "is_correct": False},
            {"label": "D", "text": "96 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Cistern Portion Filled",
        "difficulty": "Medium",
        "question_text": "A cistern can be filled in 9 hours by Pipe A. How much of the tank is filled in 5 hours?",
        "sample_answer": "1-hr filling rate = 1/9\nFraction filled in 5 hours = 5 × (1/9) = 5/9.",
        "tips": "Fraction = Hours elapsed / Total filling duration.",
        "options": [
            {"label": "A", "text": "4/9", "is_correct": False},
            {"label": "B", "text": "5/9", "is_correct": True},
            {"label": "C", "text": "1/2", "is_correct": False},
            {"label": "D", "text": "2/3", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Decimal Hour Filling Time",
        "difficulty": "Medium",
        "question_text": "Pipe A fills a tank in 14 hours and Pipe B in 21 hours. How long will they take together?",
        "sample_answer": "Combined 1-hr rate = 1/14 + 1/21 = (3 + 2)/42 = 5/42\nTotal time = 42/5 = 8.4 hours.",
        "tips": "Total Time = 42 / 5 = 8.4 hours.",
        "options": [
            {"label": "A", "text": "8 hours", "is_correct": False},
            {"label": "B", "text": "8.4 hours", "is_correct": True},
            {"label": "C", "text": "9 hours", "is_correct": False},
            {"label": "D", "text": "9.6 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Opposite Rates System",
        "difficulty": "Medium",
        "question_text": "A tank is filled in 10 hours by one pipe. Another pipe empties it in 15 hours. If both are opened together, how long will it take to fill the tank?",
        "sample_answer": "Inlet rate = 1/10, Outlet rate = 1/15\nNet rate = 1/10 − 1/15 = (3 − 2)/30 = 1/30\nTotal time = 30 hours.",
        "tips": "Net Rate = 1/10 − 1/15 = 1/30.",
        "options": [
            {"label": "A", "text": "20 hours", "is_correct": False},
            {"label": "B", "text": "25 hours", "is_correct": False},
            {"label": "C", "text": "30 hours", "is_correct": True},
            {"label": "D", "text": "35 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Joint Filling for 5 Hours",
        "difficulty": "Medium",
        "question_text": "Pipe A can fill a tank in 25 hours and Pipe B in 20 hours. They work together for 5 hours. What fraction of the tank is filled?",
        "sample_answer": "Combined rate = 1/25 + 1/20 = (4 + 5)/100 = 9/100\nFraction filled in 5 hours = 5 × (9/100) = 45/100 = 9/20.",
        "tips": "Fraction filled = 5 × (1/25 + 1/20) = 9/20.",
        "options": [
            {"label": "A", "text": "2/5", "is_correct": False},
            {"label": "B", "text": "9/20", "is_correct": True},
            {"label": "C", "text": "1/2", "is_correct": False},
            {"label": "D", "text": "11/20", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Fast Inlets Combined",
        "difficulty": "Medium",
        "question_text": "Pipe A fills a tank in 18 hours and Pipe B in 12 hours. How much time will they take together?",
        "sample_answer": "Combined rate = 1/18 + 1/12 = (2 + 3)/36 = 5/36\nTotal time = 36/5 = 7.2 hours.",
        "tips": "Total Time = 36 / 5 = 7.2 hours.",
        "options": [
            {"label": "A", "text": "6.5 hours", "is_correct": False},
            {"label": "B", "text": "7.2 hours", "is_correct": True},
            {"label": "C", "text": "8 hours", "is_correct": False},
            {"label": "D", "text": "8.5 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Finding Rate of Second Pipe",
        "difficulty": "Medium",
        "question_text": "Pipe A can fill a tank in 30 hours. After working for 10 hours, another pipe is opened and the tank gets filled in 5 more hours. Find the rate of the second pipe.",
        "sample_answer": "Pipe A in 10 hours = 10/30 = 1/3\nRemaining tank = 1 − 1/3 = 2/3\nCombined rate = (2/3) / 5 = 2/15\nPipe B rate = 2/15 − 1/30 = 3/30 = 1/10 (Fills 1/10 of tank per hour).",
        "tips": "B's rate = Combined rate − A's rate = 2/15 − 1/30 = 1/10.",
        "options": [
            {"label": "A", "text": "1/10 of tank per hour (Fills in 10 hours)", "is_correct": True},
            {"label": "B", "text": "1/12 of tank per hour (Fills in 12 hours)", "is_correct": False},
            {"label": "C", "text": "1/15 of tank per hour (Fills in 15 hours)", "is_correct": False},
            {"label": "D", "text": "1/20 of tank per hour (Fills in 20 hours)", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- HARD LEVEL (Q16 - Q30) ---
    {
        "title": "Pipes & Cisterns - Two Inlets and One Outlet",
        "difficulty": "Hard",
        "question_text": "Pipe A fills a tank in 10 hours, Pipe B in 15 hours, and Pipe C empties it in 30 hours. If all three are opened together, how long will it take to fill the tank?",
        "sample_answer": "Net rate = 1/10 + 1/15 − 1/30 = (3 + 2 − 1)/30 = 4/30 = 2/15\nTotal time = 15/2 = 7.5 hours.",
        "tips": "Net Rate = 1/A + 1/B − 1/C.",
        "options": [
            {"label": "A", "text": "6 hours", "is_correct": False},
            {"label": "B", "text": "7.5 hours", "is_correct": True},
            {"label": "C", "text": "8 hours", "is_correct": False},
            {"label": "D", "text": "9 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Leak Rate Calculation",
        "difficulty": "Hard",
        "question_text": "A pipe fills a tank in 12 hours. Due to a leak, the tank gets filled in 15 hours. In how many hours can the leak empty the full tank?",
        "sample_answer": "Filling rate = 1/12\nNet filling rate with leak = 1/15\nLeak emptying rate = 1/12 − 1/15 = (5 − 4)/60 = 1/60\nTime for leak alone = 60 hours.",
        "tips": "Leak Rate = Normal Rate − Rate with Leak = 1/12 − 1/15 = 1/60.",
        "options": [
            {"label": "A", "text": "45 hours", "is_correct": False},
            {"label": "B", "text": "50 hours", "is_correct": False},
            {"label": "C", "text": "60 hours", "is_correct": True},
            {"label": "D", "text": "72 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Alternate Hour Filling",
        "difficulty": "Hard",
        "question_text": "Pipe A can fill a tank in 8 hours and Pipe B in 12 hours. They are opened alternately starting with A. How long will it take to fill the tank?",
        "sample_answer": "Capacity = LCM(8, 12) = 24 units.\nRate A = 3 units/hr, Rate B = 2 units/hr.\n2-hr cycle = 3 + 2 = 5 units.\n4 cycles (8 hours) = 20 units. Remaining = 4 units.\nHour 9 (A): A fills 3 units. Total = 23 units. Remaining = 1 unit.\nHour 10 (B): B needs 1 unit at 2 units/hr → takes 1/2 hour.\nTotal time = 9.5 hours.",
        "tips": "Calculate 2-hour cycle work, find full cycles, then calculate remaining fraction.",
        "options": [
            {"label": "A", "text": "9 hours", "is_correct": False},
            {"label": "B", "text": "9.5 hours", "is_correct": True},
            {"label": "C", "text": "10 hours", "is_correct": False},
            {"label": "D", "text": "10.5 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Three Inlets Simultaneous Filling",
        "difficulty": "Hard",
        "question_text": "Three pipes can fill a tank in 12, 15, and 20 hours respectively. How long will they take together?",
        "sample_answer": "Combined rate = 1/12 + 1/15 + 1/20 = (5 + 4 + 3)/60 = 12/60 = 1/5\nTotal time = 5 hours.",
        "tips": "Combined Rate = 1/12 + 1/15 + 1/20 = 1/5.",
        "options": [
            {"label": "A", "text": "4 hours", "is_correct": False},
            {"label": "B", "text": "5 hours", "is_correct": True},
            {"label": "C", "text": "6 hours", "is_correct": False},
            {"label": "D", "text": "7 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes with One Outlet",
        "difficulty": "Hard",
        "question_text": "Pipe A fills a tank in 6 hours. Pipe B empties it in 18 hours. Pipe C fills it in 9 hours. If all are opened together, how long will it take to fill the tank?",
        "sample_answer": "Net rate = 1/6 − 1/18 + 1/9 = (3 − 1 + 2)/18 = 4/18 = 2/9\nTotal time = 9/2 = 4.5 hours.",
        "tips": "Net Rate = 1/6 − 1/18 + 1/9 = 2/9.",
        "options": [
            {"label": "A", "text": "4 hours", "is_correct": False},
            {"label": "B", "text": "4.5 hours", "is_correct": True},
            {"label": "C", "text": "5 hours", "is_correct": False},
            {"label": "D", "text": "5.5 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Outlet Closed Mid-Way",
        "difficulty": "Hard",
        "question_text": "A tank can be filled in 20 hours by Pipe A and emptied in 30 hours by Pipe B. If both are opened together and after 10 hours Pipe B is closed, how much more time is needed to fill the tank?",
        "sample_answer": "Net rate = 1/20 − 1/30 = 1/60\nIn 10 hours, filled = 10/60 = 1/6\nRemaining tank = 1 − 1/6 = 5/6\nPipe A rate = 1/20\nTime for A = (5/6) / (1/20) = 100/6 = 16 2/3 hours.",
        "tips": "Find remaining volume after 10 hours, then divide by A's filling rate.",
        "options": [
            {"label": "A", "text": "15 hours", "is_correct": False},
            {"label": "B", "text": "16 2/3 hours", "is_correct": True},
            {"label": "C", "text": "18 hours", "is_correct": False},
            {"label": "D", "text": "20 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Inlet Closed Mid-Way",
        "difficulty": "Hard",
        "question_text": "Pipe A fills a tank in 16 hours and Pipe B fills it in 24 hours. They work together for 4 hours, then B is closed. How much longer will A take to fill the remaining tank?",
        "sample_answer": "Combined rate = 1/16 + 1/24 = 5/48\nFilled in 4 hours = 4 × (5/48) = 5/12\nRemaining tank = 1 − 5/12 = 7/12\nPipe A rate = 1/16\nTime for A = (7/12) / (1/16) = 28/3 = 9 1/3 hours.",
        "tips": "Remaining fraction / A's rate = (7/12) × 16 = 9 1/3 hours.",
        "options": [
            {"label": "A", "text": "8 hours", "is_correct": False},
            {"label": "B", "text": "9 1/3 hours", "is_correct": True},
            {"label": "C", "text": "10 hours", "is_correct": False},
            {"label": "D", "text": "11 1/3 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes 5-Hour Progress",
        "difficulty": "Hard",
        "question_text": "Pipe A fills a tank in 10 hours, Pipe B in 20 hours, and Pipe C empties it in 40 hours. If all are opened together, what fraction of the tank is filled in 5 hours?",
        "sample_answer": "Net rate = 1/10 + 1/20 − 1/40 = (4 + 2 − 1)/40 = 5/40 = 1/8\nFraction filled in 5 hours = 5 × (1/8) = 5/8.",
        "tips": "Fraction = 5 × Net Rate = 5 × (1/8) = 5/8.",
        "options": [
            {"label": "A", "text": "1/2", "is_correct": False},
            {"label": "B", "text": "5/8", "is_correct": True},
            {"label": "C", "text": "3/4", "is_correct": False},
            {"label": "D", "text": "7/8", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Fast Inlet with Slow Leak",
        "difficulty": "Hard",
        "question_text": "A leak can empty a full tank in 48 hours. A pipe can fill it in 16 hours. If both are opened together, how long will it take to fill the tank?",
        "sample_answer": "Inlet rate = 1/16, Leak rate = 1/48\nNet filling rate = 1/16 − 1/48 = (3 − 1)/48 = 2/48 = 1/24\nTotal time = 24 hours.",
        "tips": "Net Rate = 1/16 − 1/48 = 1/24.",
        "options": [
            {"label": "A", "text": "18 hours", "is_correct": False},
            {"label": "B", "text": "20 hours", "is_correct": False},
            {"label": "C", "text": "24 hours", "is_correct": True},
            {"label": "D", "text": "32 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Finding Single Pipe Filling Time",
        "difficulty": "Hard",
        "question_text": "Pipe A and Pipe B together fill a tank in 8 hours. Pipe A alone fills it in 12 hours. In how many hours can Pipe B alone fill the tank?",
        "sample_answer": "Pipe B rate = 1/8 − 1/12 = (3 − 2)/24 = 1/24\nTime for B alone = 24 hours.",
        "tips": "B's rate = (A+B) rate − A's rate = 1/8 − 1/12 = 1/24.",
        "options": [
            {"label": "A", "text": "16 hours", "is_correct": False},
            {"label": "B", "text": "20 hours", "is_correct": False},
            {"label": "C", "text": "24 hours", "is_correct": True},
            {"label": "D", "text": "30 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Outlet Closed after Initial Hours",
        "difficulty": "Hard",
        "question_text": "Pipe A fills a tank in 18 hours. Pipe B empties it in 36 hours. If A and B are opened together for 6 hours and then B is closed, how much more time is required to fill the tank?",
        "sample_answer": "Net rate = 1/18 − 1/36 = 1/36\nFilled in 6 hours = 6/36 = 1/6\nRemaining tank = 1 − 1/6 = 5/6\nPipe A rate = 1/18\nTime for A = (5/6) / (1/18) = 15 hours.",
        "tips": "Remaining fraction / A's rate = (5/6) × 18 = 15 hours.",
        "options": [
            {"label": "A", "text": "12 hours", "is_correct": False},
            {"label": "B", "text": "15 hours", "is_correct": True},
            {"label": "C", "text": "18 hours", "is_correct": False},
            {"label": "D", "text": "20 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Three Inlets Fractional Time",
        "difficulty": "Hard",
        "question_text": "Three pipes A, B, and C can fill a tank in 12, 18, and 24 hours respectively. If all are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/12 + 1/18 + 1/24 = (6 + 4 + 3)/72 = 13/72\nTotal time = 72/13 hours = 5 7/13 hours.",
        "tips": "Combined Rate = 13/72. Total Time = 72/13 = 5 7/13 hours.",
        "options": [
            {"label": "A", "text": "5 7/13 hours", "is_correct": True},
            {"label": "B", "text": "6 hours", "is_correct": False},
            {"label": "C", "text": "5 5/13 hours", "is_correct": False},
            {"label": "D", "text": "6 2/13 hours", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Time to Reach 2/3 Capacity",
        "difficulty": "Hard",
        "question_text": "Pipe A fills a tank in 9 hours and Pipe B empties it in 27 hours. If both are opened together, after how many hours will the tank be 2/3 full?",
        "sample_answer": "Net filling rate = 1/9 − 1/27 = (3 − 1)/27 = 2/27\nTime for 2/3 full = (2/3) / (2/27) = (2/3) × (27/2) = 9 hours.",
        "tips": "Time = Targeted Fraction / Net Rate = (2/3) / (2/27) = 9 hours.",
        "options": [
            {"label": "A", "text": "7 hours", "is_correct": False},
            {"label": "B", "text": "8 hours", "is_correct": False},
            {"label": "C", "text": "9 hours", "is_correct": True},
            {"label": "D", "text": "10 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Waste Pipe with Two Inlets",
        "difficulty": "Hard",
        "question_text": "Two pipes can fill a tank in 10 hours and 15 hours respectively. A waste pipe can empty it in 30 hours. If all are opened together, how long will it take to fill the tank?",
        "sample_answer": "Net rate = 1/10 + 1/15 − 1/30 = (3 + 2 − 1)/30 = 4/30 = 2/15\nTotal time = 15/2 = 7.5 hours.",
        "tips": "Net Rate = 1/10 + 1/15 − 1/30 = 2/15.",
        "options": [
            {"label": "A", "text": "6 hours", "is_correct": False},
            {"label": "B", "text": "7.5 hours", "is_correct": True},
            {"label": "C", "text": "8 hours", "is_correct": False},
            {"label": "D", "text": "9 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Alternate Hour Filling and Emptying",
        "difficulty": "Hard",
        "question_text": "A pipe fills a tank in 12 hours. Another pipe empties it in 18 hours. They are opened alternately for one hour each, starting with the filling pipe. In how many hours will the tank be completely filled?",
        "sample_answer": "Tank capacity = LCM(12, 18) = 36 units.\nInlet rate A = +3 units/hr, Outlet rate B = −2 units/hr.\n2-hr cycle net gain = +3 − 2 = +1 unit.\nSince filling pipe A completes 3 units in the final hour:\nTarget volume before last filling step = 36 − 3 = 33 units.\nTime to reach 33 units = 33 × 2 = 66 hours.\nHour 67 (A's turn): A fills +3 units → 33 + 3 = 36 units (Tank is Full!).\nTotal time = 67 hours.",
        "tips": "For alternating filling & emptying, calculate cycles up to (Total Capacity − Filling Rate), then add 1 final hour for the filling pipe.",
        "options": [
            {"label": "A", "text": "66 hours", "is_correct": False},
            {"label": "B", "text": "67 hours", "is_correct": True},
            {"label": "C", "text": "70 hours", "is_correct": False},
            {"label": "D", "text": "72 hours", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_pipes_and_cisterns():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Pipes & Cisterns'")
            print(f"Deleted old 'Pipes & Cisterns' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Time-Based Problems',
                    'Pipes & Cisterns',
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
    seed_pipes_and_cisterns()
