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
        "title": "Trains - Speed Crossing a Pole",
        "difficulty": "Medium",
        "question_text": "A train 120 m long crosses a pole in 12 seconds. Find its speed.",
        "sample_answer": "Speed = Distance / Time = 120 / 12 = 10 m/s (36 km/h).",
        "tips": "Speed = Train Length / Time.",
        "options": [
            {"label": "A", "text": "8 m/s (28.8 km/h)", "is_correct": False},
            {"label": "B", "text": "10 m/s (36 km/h)", "is_correct": True},
            {"label": "C", "text": "12 m/s (43.2 km/h)", "is_correct": False},
            {"label": "D", "text": "15 m/s (54 km/h)", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Train Length from Man Crossing",
        "difficulty": "Medium",
        "question_text": "A train running at 54 km/h crosses a man standing on a platform in 20 seconds. Find the length of the train.",
        "sample_answer": "Speed in m/s = 54 × (5/18) = 15 m/s\nTrain Length = Speed × Time = 15 × 20 = 300 m.",
        "tips": "Length = Speed in m/s × Time.",
        "options": [
            {"label": "A", "text": "250 m", "is_correct": False},
            {"label": "B", "text": "280 m", "is_correct": False},
            {"label": "C", "text": "300 m", "is_correct": True},
            {"label": "D", "text": "350 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Speed Conversion to km/h",
        "difficulty": "Medium",
        "question_text": "A train 180 m long crosses a pole in 15 seconds. Find its speed in km/h.",
        "sample_answer": "Speed in m/s = 180 / 15 = 12 m/s\nSpeed in km/h = 12 × (18/5) = 43.2 km/h.",
        "tips": "Multiply m/s by 18/5 to get km/h.",
        "options": [
            {"label": "A", "text": "36 km/h", "is_correct": False},
            {"label": "B", "text": "43.2 km/h", "is_correct": True},
            {"label": "C", "text": "48 km/h", "is_correct": False},
            {"label": "D", "text": "54 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Total Distance While Crossing Platform",
        "difficulty": "Medium",
        "question_text": "A train moving at 72 km/h crosses a platform 180 m long in 24 seconds. If the train length is 300 m, find the total distance covered while crossing.",
        "sample_answer": "Total distance = Train length + Platform length = 300 + 180 = 480 m.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {"label": "A", "text": "360 m", "is_correct": False},
            {"label": "B", "text": "420 m", "is_correct": False},
            {"label": "C", "text": "480 m", "is_correct": True},
            {"label": "D", "text": "540 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Speed for 240m Train",
        "difficulty": "Medium",
        "question_text": "A train 240 m long crosses a pole in 16 seconds. Find its speed.",
        "sample_answer": "Speed = 240 / 16 = 15 m/s = 54 km/h.",
        "tips": "Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "12 m/s (43.2 km/h)", "is_correct": False},
            {"label": "B", "text": "15 m/s (54 km/h)", "is_correct": True},
            {"label": "C", "text": "18 m/s (64.8 km/h)", "is_correct": False},
            {"label": "D", "text": "20 m/s (72 km/h)", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Length of 90 km/h Train",
        "difficulty": "Medium",
        "question_text": "A train moving at 90 km/h crosses a man standing on a platform in 8 seconds. Find the length of the train.",
        "sample_answer": "Speed in m/s = 90 × (5/18) = 25 m/s\nTrain Length = 25 × 8 = 200 m.",
        "tips": "Train Length = Speed in m/s × Time.",
        "options": [
            {"label": "A", "text": "180 m", "is_correct": False},
            {"label": "B", "text": "200 m", "is_correct": True},
            {"label": "C", "text": "220 m", "is_correct": False},
            {"label": "D", "text": "250 m", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Speed Crossing 300m Platform",
        "difficulty": "Medium",
        "question_text": "A train 200 m long crosses a platform 300 m long in 25 seconds. Find its speed.",
        "sample_answer": "Total distance = 200 + 300 = 500 m\nSpeed in m/s = 500 / 25 = 20 m/s (72 km/h).",
        "tips": "Speed = (Train Length + Platform Length) / Time.",
        "options": [
            {"label": "A", "text": "16 m/s (57.6 km/h)", "is_correct": False},
            {"label": "B", "text": "18 m/s (64.8 km/h)", "is_correct": False},
            {"label": "C", "text": "20 m/s (72 km/h)", "is_correct": True},
            {"label": "D", "text": "25 m/s (90 km/h)", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Length of 108 km/h Train",
        "difficulty": "Medium",
        "question_text": "A train running at 108 km/h crosses a pole in 10 seconds. Find the train's length.",
        "sample_answer": "Speed in m/s = 108 × (5/18) = 30 m/s\nTrain Length = 30 × 10 = 300 m.",
        "tips": "Length = 30 m/s × 10 s = 300 m.",
        "options": [
            {"label": "A", "text": "250 m", "is_correct": False},
            {"label": "B", "text": "280 m", "is_correct": False},
            {"label": "C", "text": "300 m", "is_correct": True},
            {"label": "D", "text": "350 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Speed Crossing 250m Platform",
        "difficulty": "Medium",
        "question_text": "A train 150 m long crosses a platform 250 m long in 20 seconds. Find its speed.",
        "sample_answer": "Total distance = 150 + 250 = 400 m\nSpeed in m/s = 400 / 20 = 20 m/s (72 km/h).",
        "tips": "Speed = 400 / 20 = 20 m/s.",
        "options": [
            {"label": "A", "text": "15 m/s (54 km/h)", "is_correct": False},
            {"label": "B", "text": "18 m/s (64.8 km/h)", "is_correct": False},
            {"label": "C", "text": "20 m/s (72 km/h)", "is_correct": True},
            {"label": "D", "text": "25 m/s (90 km/h)", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Length of 60 km/h Train",
        "difficulty": "Medium",
        "question_text": "A train moving at 60 km/h crosses a pole in 18 seconds. Find its length.",
        "sample_answer": "Speed in m/s = 60 × (5/18) = 50/3 m/s\nLength = (50/3) × 18 = 300 m.",
        "tips": "Length = Speed in m/s × Time.",
        "options": [
            {"label": "A", "text": "250 m", "is_correct": False},
            {"label": "B", "text": "280 m", "is_correct": False},
            {"label": "C", "text": "300 m", "is_correct": True},
            {"label": "D", "text": "320 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Speed Crossing 420m Bridge",
        "difficulty": "Medium",
        "question_text": "A train 180 m long crosses a bridge 420 m long in 30 seconds. Find its speed.",
        "sample_answer": "Total distance = 180 + 420 = 600 m\nSpeed in m/s = 600 / 30 = 20 m/s (72 km/h).",
        "tips": "Speed = (Train + Bridge) / Time.",
        "options": [
            {"label": "A", "text": "16 m/s (57.6 km/h)", "is_correct": False},
            {"label": "B", "text": "18 m/s (64.8 km/h)", "is_correct": False},
            {"label": "C", "text": "20 m/s (72 km/h)", "is_correct": True},
            {"label": "D", "text": "24 m/s (86.4 km/h)", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Train Length with Platform Given",
        "difficulty": "Medium",
        "question_text": "A train moving at 72 km/h crosses a platform 280 m long in 28 seconds. Find the train's length if its speed remains constant.",
        "sample_answer": "Speed in m/s = 72 × (5/18) = 20 m/s\nTotal distance = 20 × 28 = 560 m\nTrain length = 560 − 280 = 280 m.",
        "tips": "Train Length = (Speed × Time) − Platform Length.",
        "options": [
            {"label": "A", "text": "240 m", "is_correct": False},
            {"label": "B", "text": "260 m", "is_correct": False},
            {"label": "C", "text": "280 m", "is_correct": True},
            {"label": "D", "text": "300 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Speed of 300m Train",
        "difficulty": "Medium",
        "question_text": "A train 300 m long crosses a pole in 15 seconds. Find its speed.",
        "sample_answer": "Speed = 300 / 15 = 20 m/s (72 km/h).",
        "tips": "Speed = 300 / 15 = 20 m/s.",
        "options": [
            {"label": "A", "text": "15 m/s (54 km/h)", "is_correct": False},
            {"label": "B", "text": "18 m/s (64.8 km/h)", "is_correct": False},
            {"label": "C", "text": "20 m/s (72 km/h)", "is_correct": True},
            {"label": "D", "text": "25 m/s (90 km/h)", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Relative Speed Same Direction Walking Man",
        "difficulty": "Medium",
        "question_text": "A train moving at 45 km/h crosses a man walking at 9 km/h in the same direction. Find the relative speed.",
        "sample_answer": "Relative speed in same direction = 45 − 9 = 36 km/h (10 m/s).",
        "tips": "Relative Speed = Train Speed − Man Speed.",
        "options": [
            {"label": "A", "text": "28 km/h", "is_correct": False},
            {"label": "B", "text": "36 km/h (10 m/s)", "is_correct": True},
            {"label": "C", "text": "40 km/h", "is_correct": False},
            {"label": "D", "text": "54 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Speed in m/s of 250m Train",
        "difficulty": "Medium",
        "question_text": "A train 250 m long crosses a pole in 20 seconds. Find its speed in m/s.",
        "sample_answer": "Speed = 250 / 20 = 12.5 m/s.",
        "tips": "Speed in m/s = Distance / Time = 250 / 20 = 12.5 m/s.",
        "options": [
            {"label": "A", "text": "10 m/s", "is_correct": False},
            {"label": "B", "text": "12.5 m/s", "is_correct": True},
            {"label": "C", "text": "15 m/s", "is_correct": False},
            {"label": "D", "text": "17.5 m/s", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- HARD LEVEL (Q16 - Q30) ---
    {
        "title": "Trains - Two Trains Opposite Directions Crossing Time",
        "difficulty": "Hard",
        "question_text": "Two trains of lengths 180 m and 220 m move in opposite directions at 54 km/h and 72 km/h. How long will they take to cross each other?",
        "sample_answer": "Total distance = 180 + 220 = 400 m\nRelative speed = 54 + 72 = 126 km/h = 126 × (5/18) = 35 m/s\nCrossing time = 400 / 35 = 11.43 seconds (11 3/7 s).",
        "tips": "Crossing Time = Total Lengths / Relative Speed in m/s.",
        "options": [
            {"label": "A", "text": "10 seconds", "is_correct": False},
            {"label": "B", "text": "11.43 seconds (11 3/7 s)", "is_correct": True},
            {"label": "C", "text": "12.5 seconds", "is_correct": False},
            {"label": "D", "text": "14 seconds", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing Time of 240m and 160m Trains",
        "difficulty": "Hard",
        "question_text": "A train 240 m long moving at 72 km/h crosses another train 160 m long moving in the opposite direction at 54 km/h. Find the crossing time.",
        "sample_answer": "Total distance = 240 + 160 = 400 m\nRelative speed = 72 + 54 = 126 km/h = 35 m/s\nCrossing time = 400 / 35 = 11.43 seconds (11 3/7 s).",
        "tips": "Time = (L1 + L2) / Relative Speed.",
        "options": [
            {"label": "A", "text": "10 seconds", "is_correct": False},
            {"label": "B", "text": "11.43 seconds (11 3/7 s)", "is_correct": True},
            {"label": "C", "text": "12.5 seconds", "is_correct": False},
            {"label": "D", "text": "14 seconds", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Same Direction Overtaking Time",
        "difficulty": "Hard",
        "question_text": "Two trains 150 m and 250 m long move in the same direction at 60 km/h and 42 km/h. How long will the faster train take to overtake the slower train?",
        "sample_answer": "Total distance = 150 + 250 = 400 m\nRelative speed = 60 − 42 = 18 km/h = 18 × (5/18) = 5 m/s\nOvertaking time = 400 / 5 = 80 seconds (1 min 20 s).",
        "tips": "Relative Speed = S1 − S2. Overtaking Time = Total Lengths / Relative Speed.",
        "options": [
            {"label": "A", "text": "60 seconds (1 min)", "is_correct": False},
            {"label": "B", "text": "72 seconds", "is_correct": False},
            {"label": "C", "text": "80 seconds (1 min 20 s)", "is_correct": True},
            {"label": "D", "text": "90 seconds", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Pole and Platform System for Length",
        "difficulty": "Hard",
        "question_text": "A train crosses a pole in 12 seconds and a platform 180 m long in 24 seconds. Find the train's length.",
        "sample_answer": "Let train length = L, speed = S.\nL = 12 × S\nL + 180 = 24 × S → 12S + 180 = 24S → 12S = 180 → S = 15 m/s\nLength L = 12 × 15 = 180 m.",
        "tips": "Platform Time − Pole Time = Platform Length / Speed.",
        "options": [
            {"label": "A", "text": "150 m", "is_correct": False},
            {"label": "B", "text": "180 m", "is_correct": True},
            {"label": "C", "text": "200 m", "is_correct": False},
            {"label": "D", "text": "240 m", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Bridge Length Calculation",
        "difficulty": "Hard",
        "question_text": "A train 300 m long crosses a bridge in 40 seconds at a speed of 54 km/h. Find the length of the bridge.",
        "sample_answer": "Speed in m/s = 54 × (5/18) = 15 m/s\nTotal distance = 15 × 40 = 600 m\nBridge length = 600 − 300 = 300 m.",
        "tips": "Bridge Length = (Speed × Time) − Train Length.",
        "options": [
            {"label": "A", "text": "250 m", "is_correct": False},
            {"label": "B", "text": "280 m", "is_correct": False},
            {"label": "C", "text": "300 m", "is_correct": True},
            {"label": "D", "text": "350 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Length of Second Train in Opposite Motion",
        "difficulty": "Hard",
        "question_text": "Two trains running at 90 km/h and 54 km/h in opposite directions cross each other in 12 seconds. If one train is 180 m long, find the length of the other train.",
        "sample_answer": "Relative speed = 90 + 54 = 144 km/h = 144 × (5/18) = 40 m/s\nTotal distance = 40 × 12 = 480 m\nLength of second train = 480 − 180 = 300 m.",
        "tips": "Length2 = (Relative Speed × Time) − Length1.",
        "options": [
            {"label": "A", "text": "250 m", "is_correct": False},
            {"label": "B", "text": "280 m", "is_correct": False},
            {"label": "C", "text": "300 m", "is_correct": True},
            {"label": "D", "text": "320 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Length of Train Crossing Tunnel",
        "difficulty": "Hard",
        "question_text": "A train moving at 108 km/h crosses a tunnel 450 m long in 30 seconds. Find the length of the train.",
        "sample_answer": "Speed in m/s = 108 × (5/18) = 30 m/s\nTotal distance = 30 × 30 = 900 m\nTrain length = 900 − 450 = 450 m.",
        "tips": "Train Length = (Speed × Time) − Tunnel Length.",
        "options": [
            {"label": "A", "text": "350 m", "is_correct": False},
            {"label": "B", "text": "400 m", "is_correct": False},
            {"label": "C", "text": "450 m", "is_correct": True},
            {"label": "D", "text": "500 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Equal Length Trains Crossing",
        "difficulty": "Hard",
        "question_text": "Two trains of equal lengths moving in opposite directions at 60 km/h and 90 km/h cross each other in 8 seconds. Find the length of each train.",
        "sample_answer": "Relative speed = 60 + 90 = 150 km/h = 150 × (5/18) = 125/3 m/s\nTotal distance = (125/3) × 8 = 1000/3 m = 333.33 m\nLength of each train = (1000/3) / 2 = 500/3 m = 166.67 m (166 2/3 m).",
        "tips": "Length of each train = (Relative Speed × Time) / 2.",
        "options": [
            {"label": "A", "text": "150 m", "is_correct": False},
            {"label": "B", "text": "166.67 m (166 2/3 m)", "is_correct": True},
            {"label": "C", "text": "180 m", "is_correct": False},
            {"label": "D", "text": "200 m", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Platform Length from Pole and Platform Times",
        "difficulty": "Hard",
        "question_text": "A train moving at 72 km/h crosses a platform in 36 seconds and a pole in 18 seconds. Find the length of the platform.",
        "sample_answer": "Speed in m/s = 72 × (5/18) = 20 m/s\nTrain length = 20 × 18 = 360 m\nPlatform + Train length = 20 × 36 = 720 m\nPlatform length = 720 − 360 = 360 m.",
        "tips": "Platform Length = Speed in m/s × (Platform Time − Pole Time).",
        "options": [
            {"label": "A", "text": "300 m", "is_correct": False},
            {"label": "B", "text": "320 m", "is_correct": False},
            {"label": "C", "text": "360 m", "is_correct": True},
            {"label": "D", "text": "400 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Overtaking Running Man Verification",
        "difficulty": "Hard",
        "question_text": "A train 250 m long overtakes a man running at 10 km/h in the same direction in 20 seconds. If the train speed is 55 km/h, verify the overtaking time.",
        "sample_answer": "Relative speed = 55 − 10 = 45 km/h = 45 × (5/18) = 12.5 m/s\nOvertaking time = 250 / 12.5 = 20 seconds.",
        "tips": "Time = Train Length / Relative Speed in m/s.",
        "options": [
            {"label": "A", "text": "16 seconds", "is_correct": False},
            {"label": "B", "text": "18 seconds", "is_correct": False},
            {"label": "C", "text": "20 seconds", "is_correct": True},
            {"label": "D", "text": "24 seconds", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Both Length and Speed from Bridge and Pole",
        "difficulty": "Hard",
        "question_text": "A train crosses a bridge 500 m long in 45 seconds and a pole in 15 seconds. Find the train's length and speed.",
        "sample_answer": "Let train length = L, speed = S.\nL = 15S\nL + 500 = 45S → 15S + 500 = 45S → 30S = 500 → S = 50/3 m/s = 60 km/h\nTrain length L = 15 × (50/3) = 250 m.",
        "tips": "Speed = Bridge Length / (Bridge Time − Pole Time).",
        "options": [
            {"label": "A", "text": "Length = 250 m, Speed = 60 km/h (16.67 m/s)", "is_correct": True},
            {"label": "B", "text": "Length = 200 m, Speed = 54 km/h (15 m/s)", "is_correct": False},
            {"label": "C", "text": "Length = 300 m, Speed = 72 km/h (20 m/s)", "is_correct": False},
            {"label": "D", "text": "Length = 220 m, Speed = 50 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Overtaking Duration for 180m & 240m Trains",
        "difficulty": "Hard",
        "question_text": "Two trains 180 m and 240 m long move in the same direction at 72 km/h and 54 km/h. Find the time taken for the faster train to overtake the slower train.",
        "sample_answer": "Total distance = 180 + 240 = 420 m\nRelative speed = 72 − 54 = 18 km/h = 18 × (5/18) = 5 m/s\nOvertaking time = 420 / 5 = 84 seconds (1 min 24 s).",
        "tips": "Overtaking Time = Total Lengths / Relative Speed.",
        "options": [
            {"label": "A", "text": "72 seconds", "is_correct": False},
            {"label": "B", "text": "80 seconds", "is_correct": False},
            {"label": "C", "text": "84 seconds (1 min 24 s)", "is_correct": True},
            {"label": "D", "text": "90 seconds", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Train Length from 350m Platform Crossing",
        "difficulty": "Hard",
        "question_text": "A train running at 90 km/h crosses a platform 350 m long in 28 seconds. Find the train's length.",
        "sample_answer": "Speed in m/s = 90 × (5/18) = 25 m/s\nTotal distance = 25 × 28 = 700 m\nTrain length = 700 − 350 = 350 m.",
        "tips": "Train Length = (Speed × Time) − Platform Length.",
        "options": [
            {"label": "A", "text": "300 m", "is_correct": False},
            {"label": "B", "text": "320 m", "is_correct": False},
            {"label": "C", "text": "350 m", "is_correct": True},
            {"label": "D", "text": "400 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Second Train Length from 180 km/h Relative Speed",
        "difficulty": "Hard",
        "question_text": "Two trains moving in opposite directions at 72 km/h and 108 km/h cross each other in 10 seconds. If one train is 200 m long, find the length of the other train.",
        "sample_answer": "Relative speed = 72 + 108 = 180 km/h = 180 × (5/18) = 50 m/s\nTotal distance = 50 × 10 = 500 m\nLength of second train = 500 − 200 = 300 m.",
        "tips": "Length2 = (Relative Speed × Time) − Length1.",
        "options": [
            {"label": "A", "text": "250 m", "is_correct": False},
            {"label": "B", "text": "280 m", "is_correct": False},
            {"label": "C", "text": "300 m", "is_correct": True},
            {"label": "D", "text": "350 m", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Speed & Length from Pole & 250m Platform",
        "difficulty": "Hard",
        "question_text": "A train crosses a pole in 10 seconds and a platform 250 m long in 20 seconds. Find the speed and length of the train.",
        "sample_answer": "Platform Time − Pole Time = 20 − 10 = 10 seconds for 250 m platform.\nSpeed = 250 / 10 = 25 m/s = 90 km/h\nTrain length = Speed × Pole Time = 25 × 10 = 250 m.",
        "tips": "Speed = Platform Length / (Platform Time − Pole Time). Length = Speed × Pole Time.",
        "options": [
            {"label": "A", "text": "Length = 200 m, Speed = 72 km/h (20 m/s)", "is_correct": False},
            {"label": "B", "text": "Length = 250 m, Speed = 90 km/h (25 m/s)", "is_correct": True},
            {"label": "C", "text": "Length = 300 m, Speed = 108 km/h (30 m/s)", "is_correct": False},
            {"label": "D", "text": "Length = 220 m, Speed = 80 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_trains():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Trains'")
            print(f"Deleted old 'Trains' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Time-Based Problems',
                    'Trains',
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
    seed_trains()
