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
        "title": "Time, Speed & Distance - Basic Speed Calculation",
        "difficulty": "Medium",
        "question_text": "A car travels 240 km in 4 hours. Find its speed.",
        "sample_answer": "Speed = Distance / Time = 240 / 4 = 60 km/h.",
        "tips": "Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "50 km/h", "is_correct": False},
            {"label": "B", "text": "60 km/h", "is_correct": True},
            {"label": "C", "text": "70 km/h", "is_correct": False},
            {"label": "D", "text": "80 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Distance Covered by Train",
        "difficulty": "Medium",
        "question_text": "A train travels at 72 km/h. How much distance will it cover in 2.5 hours?",
        "sample_answer": "Distance = Speed × Time = 72 × 2.5 = 180 km.",
        "tips": "Distance = Speed × Time.",
        "options": [
            {"label": "A", "text": "150 km", "is_correct": False},
            {"label": "B", "text": "160 km", "is_correct": False},
            {"label": "C", "text": "180 km", "is_correct": True},
            {"label": "D", "text": "200 km", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Time Taken to Walk",
        "difficulty": "Medium",
        "question_text": "A person walks at 5 km/h. How long will it take to cover 20 km?",
        "sample_answer": "Time = Distance / Speed = 20 / 5 = 4 hours.",
        "tips": "Time = Distance / Speed.",
        "options": [
            {"label": "A", "text": "3 hours", "is_correct": False},
            {"label": "B", "text": "4 hours", "is_correct": True},
            {"label": "C", "text": "5 hours", "is_correct": False},
            {"label": "D", "text": "6 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Speed Conversion to m/s",
        "difficulty": "Medium",
        "question_text": "A bike covers 180 km in 3 hours. Find its speed in m/s.",
        "sample_answer": "Speed in km/h = 180 / 3 = 60 km/h\nTo convert km/h to m/s, multiply by 5/18:\nSpeed in m/s = 60 × (5/18) = 50/3 = 16.67 m/s (16 2/3 m/s).",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {"label": "A", "text": "15 m/s", "is_correct": False},
            {"label": "B", "text": "16.67 m/s (16 2/3 m/s)", "is_correct": True},
            {"label": "C", "text": "18 m/s", "is_correct": False},
            {"label": "D", "text": "20 m/s", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Train Crossing a Pole",
        "difficulty": "Medium",
        "question_text": "A train 180 m long crosses a pole in 12 seconds. Find its speed.",
        "sample_answer": "Speed = Train Length / Time = 180 m / 12 s = 15 m/s\nIn km/h = 15 × (18/5) = 54 km/h.",
        "tips": "When crossing a pole, distance = train length. Multiply m/s by 18/5 to get km/h.",
        "options": [
            {"label": "A", "text": "45 km/h (12.5 m/s)", "is_correct": False},
            {"label": "B", "text": "54 km/h (15 m/s)", "is_correct": True},
            {"label": "C", "text": "60 km/h (16.67 m/s)", "is_correct": False},
            {"label": "D", "text": "72 km/h (20 m/s)", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Relative Speed Same Direction",
        "difficulty": "Medium",
        "question_text": "A car travels at 60 km/h and another at 80 km/h. What is their relative speed if they move in the same direction?",
        "sample_answer": "Relative speed in same direction = Speed1 − Speed2 = 80 − 60 = 20 km/h.",
        "tips": "Same direction relative speed = |S1 − S2|.",
        "options": [
            {"label": "A", "text": "20 km/h", "is_correct": True},
            {"label": "B", "text": "40 km/h", "is_correct": False},
            {"label": "C", "text": "140 km/h", "is_correct": False},
            {"label": "D", "text": "160 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Travel Duration Calculation",
        "difficulty": "Medium",
        "question_text": "A train travels 300 km at 50 km/h. How much time does it take?",
        "sample_answer": "Time = Distance / Speed = 300 / 50 = 6 hours.",
        "tips": "Time = Distance / Speed.",
        "options": [
            {"label": "A", "text": "5 hours", "is_correct": False},
            {"label": "B", "text": "6 hours", "is_correct": True},
            {"label": "C", "text": "7 hours", "is_correct": False},
            {"label": "D", "text": "8 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Average Speed for Equal Halves",
        "difficulty": "Medium",
        "question_text": "A man covers half the distance at 40 km/h and the other half at 60 km/h. Find the average speed.",
        "sample_answer": "Average Speed = 2xy / (x + y) = 2(40)(60) / (40 + 60) = 4800 / 100 = 48 km/h.",
        "tips": "Harmonic mean formula for equal distances: Average Speed = 2xy / (x + y).",
        "options": [
            {"label": "A", "text": "48 km/h", "is_correct": True},
            {"label": "B", "text": "50 km/h", "is_correct": False},
            {"label": "C", "text": "52 km/h", "is_correct": False},
            {"label": "D", "text": "55 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Train Crossing a Platform",
        "difficulty": "Medium",
        "question_text": "A train 240 m long crosses a platform 360 m long in 30 seconds. Find the speed of the train.",
        "sample_answer": "Total distance = Train length + Platform length = 240 + 360 = 600 m\nSpeed in m/s = 600 / 30 = 20 m/s\nIn km/h = 20 × (18/5) = 72 km/h.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {"label": "A", "text": "60 km/h (16.67 m/s)", "is_correct": False},
            {"label": "B", "text": "72 km/h (20 m/s)", "is_correct": True},
            {"label": "C", "text": "80 km/h (22.22 m/s)", "is_correct": False},
            {"label": "D", "text": "90 km/h (25 m/s)", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Time Saved by Speed Increase",
        "difficulty": "Medium",
        "question_text": "A cyclist increases his speed from 12 km/h to 15 km/h. How much time will he save in covering 60 km?",
        "sample_answer": "Initial time = 60 / 12 = 5 hours\nNew time = 60 / 15 = 4 hours\nTime saved = 5 − 4 = 1 hour (60 minutes).",
        "tips": "Time Saved = Initial Time − New Time.",
        "options": [
            {"label": "A", "text": "30 minutes", "is_correct": False},
            {"label": "B", "text": "45 minutes", "is_correct": False},
            {"label": "C", "text": "1 hour (60 minutes)", "is_correct": True},
            {"label": "D", "text": "1.5 hours (90 minutes)", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Two Trains Crossing Opposite",
        "difficulty": "Medium",
        "question_text": "Two trains moving in opposite directions at 54 km/h and 72 km/h cross each other. If one train is 150 m long and the other is 210 m long, find the exact crossing time.",
        "sample_answer": "Relative speed = 54 + 72 = 126 km/h = 126 × (5/18) = 35 m/s\nTotal distance = 150 + 210 = 360 m\nCrossing time = 360 / 35 = 10.285 seconds (10 2/7 seconds).",
        "tips": "Crossing Time = (L1 + L2) / (Relative Speed in m/s).",
        "options": [
            {"label": "A", "text": "10.28 seconds (10 2/7 s)", "is_correct": True},
            {"label": "B", "text": "12 seconds", "is_correct": False},
            {"label": "C", "text": "15 seconds", "is_correct": False},
            {"label": "D", "text": "18 seconds", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Downstream Boat Speed",
        "difficulty": "Medium",
        "question_text": "A boat travels 24 km downstream in 2 hours. Find its downstream speed.",
        "sample_answer": "Downstream speed = Distance / Time = 24 / 2 = 12 km/h.",
        "tips": "Downstream Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "8 km/h", "is_correct": False},
            {"label": "B", "text": "10 km/h", "is_correct": False},
            {"label": "C", "text": "12 km/h", "is_correct": True},
            {"label": "D", "text": "14 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Round Trip Average Speed",
        "difficulty": "Medium",
        "question_text": "A person walks 12 km at 4 km/h and returns at 6 km/h. Find the average speed.",
        "sample_answer": "Average speed for equal distance round trip = 2xy / (x + y) = 2(4)(6) / (4 + 6) = 48 / 10 = 4.8 km/h.",
        "tips": "Average Speed = 2xy / (x + y) for equal distances.",
        "options": [
            {"label": "A", "text": "4.5 km/h", "is_correct": False},
            {"label": "B", "text": "4.8 km/h", "is_correct": True},
            {"label": "C", "text": "5.0 km/h", "is_correct": False},
            {"label": "D", "text": "5.2 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Speed from Distance and Hours",
        "difficulty": "Medium",
        "question_text": "A car covers 150 km in 2.5 hours. What is its speed?",
        "sample_answer": "Speed = Distance / Time = 150 / 2.5 = 60 km/h.",
        "tips": "Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "50 km/h", "is_correct": False},
            {"label": "B", "text": "55 km/h", "is_correct": False},
            {"label": "C", "text": "60 km/h", "is_correct": True},
            {"label": "D", "text": "65 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Train Length from Man Crossing",
        "difficulty": "Medium",
        "question_text": "A train moving at 90 km/h crosses a man standing on a platform in 8 seconds. Find the train's length.",
        "sample_answer": "Speed in m/s = 90 × (5/18) = 25 m/s\nTrain Length = Speed × Time = 25 × 8 = 200 m.",
        "tips": "Train Length = Speed in m/s × Crossing Time.",
        "options": [
            {"label": "A", "text": "180 m", "is_correct": False},
            {"label": "B", "text": "200 m", "is_correct": True},
            {"label": "C", "text": "220 m", "is_correct": False},
            {"label": "D", "text": "250 m", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- HARD LEVEL (Q16 - Q30) ---
    {
        "title": "Time, Speed & Distance - Long Platform Crossing",
        "difficulty": "Hard",
        "question_text": "A train 300 m long crosses a platform 500 m long in 40 seconds. Find its speed.",
        "sample_answer": "Total distance = 300 + 500 = 800 m\nSpeed in m/s = 800 / 40 = 20 m/s\nSpeed in km/h = 20 × (18/5) = 72 km/h.",
        "tips": "Speed = (Train Length + Platform Length) / Time.",
        "options": [
            {"label": "A", "text": "60 km/h (16.67 m/s)", "is_correct": False},
            {"label": "B", "text": "72 km/h (20 m/s)", "is_correct": True},
            {"label": "C", "text": "80 km/h (22.22 m/s)", "is_correct": False},
            {"label": "D", "text": "90 km/h (25 m/s)", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Two Trains Crossing Duration",
        "difficulty": "Hard",
        "question_text": "Two trains of lengths 180 m and 220 m are moving in opposite directions at 54 km/h and 72 km/h. How long will they take to cross each other?",
        "sample_answer": "Total distance = 180 + 220 = 400 m\nRelative speed = 54 + 72 = 126 km/h = 126 × (5/18) = 35 m/s\nCrossing time = 400 / 35 = 11.43 seconds (11 3/7 s).",
        "tips": "Time = Total Distance / Relative Speed.",
        "options": [
            {"label": "A", "text": "10 seconds", "is_correct": False},
            {"label": "B", "text": "11.43 seconds (11 3/7 s)", "is_correct": True},
            {"label": "C", "text": "12.5 seconds", "is_correct": False},
            {"label": "D", "text": "14 seconds", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Finding Distance from Speed Change",
        "difficulty": "Hard",
        "question_text": "A man covers a distance in 8 hours. Had he moved 2 km/h faster, he would have taken 6 hours. Find the distance.",
        "sample_answer": "Let speed be S km/h.\nDistance D = S × 8 = (S + 2) × 6\n8S = 6S + 12 → 2S = 12 → S = 6 km/h\nDistance D = 6 × 8 = 48 km.",
        "tips": "Equate Distance formulas: S1 × T1 = S2 × T2.",
        "options": [
            {"label": "A", "text": "36 km", "is_correct": False},
            {"label": "B", "text": "40 km", "is_correct": False},
            {"label": "C", "text": "48 km", "is_correct": True},
            {"label": "D", "text": "60 km", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Boat Speed in Still Water",
        "difficulty": "Hard",
        "question_text": "A boat takes 6 hours to travel 36 km upstream and 3 hours to travel the same distance downstream. Find the speed of the boat in still water.",
        "sample_answer": "Upstream speed U = 36 / 6 = 6 km/h\nDownstream speed D = 36 / 3 = 12 km/h\nSpeed of boat in still water = (D + U) / 2 = (12 + 6) / 2 = 9 km/h.",
        "tips": "Speed of Boat in Still Water = (Downstream + Upstream) / 2.",
        "options": [
            {"label": "A", "text": "7.5 km/h", "is_correct": False},
            {"label": "B", "text": "9 km/h", "is_correct": True},
            {"label": "C", "text": "10.5 km/h", "is_correct": False},
            {"label": "D", "text": "12 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Train Crossing a Bridge",
        "difficulty": "Hard",
        "question_text": "A train running at 72 km/h crosses a bridge. If the train length is 250 m and the bridge length is 500 m, find the exact crossing time.",
        "sample_answer": "Speed in m/s = 72 × (5/18) = 20 m/s\nTotal distance = 250 + 500 = 750 m\nCrossing time = 750 / 20 = 37.5 seconds.",
        "tips": "Time = (Train Length + Bridge Length) / Speed in m/s.",
        "options": [
            {"label": "A", "text": "35 seconds", "is_correct": False},
            {"label": "B", "text": "37.5 seconds", "is_correct": True},
            {"label": "C", "text": "40 seconds", "is_correct": False},
            {"label": "D", "text": "45 seconds", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Average Speed for Two Legs",
        "difficulty": "Hard",
        "question_text": "A car travels the first 120 km at 40 km/h and the next 180 km at 60 km/h. Find the average speed for the entire journey.",
        "sample_answer": "Time 1 = 120 / 40 = 3 hours\nTime 2 = 180 / 60 = 3 hours\nTotal Distance = 120 + 180 = 300 km\nTotal Time = 3 + 3 = 6 hours\nAverage Speed = 300 / 6 = 50 km/h.",
        "tips": "Average Speed = Total Distance / Total Time.",
        "options": [
            {"label": "A", "text": "45 km/h", "is_correct": False},
            {"label": "B", "text": "48 km/h", "is_correct": False},
            {"label": "C", "text": "50 km/h", "is_correct": True},
            {"label": "D", "text": "52 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Meeting Time of Two Trains",
        "difficulty": "Hard",
        "question_text": "Two trains start from stations A and B, 360 km apart, moving towards each other at 40 km/h and 50 km/h. After how many hours will they meet?",
        "sample_answer": "Relative speed = 40 + 50 = 90 km/h\nTime to meet = Distance / Relative Speed = 360 / 90 = 4 hours.",
        "tips": "Meeting Time = Distance / (Speed1 + Speed2).",
        "options": [
            {"label": "A", "text": "3 hours", "is_correct": False},
            {"label": "B", "text": "4 hours", "is_correct": True},
            {"label": "C", "text": "4.5 hours", "is_correct": False},
            {"label": "D", "text": "5 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Pole and Platform Crossing System",
        "difficulty": "Hard",
        "question_text": "A train crosses a pole in 15 seconds and a platform 300 m long in 35 seconds. Find the length of the train.",
        "sample_answer": "Let train length = L, speed = S.\nL = 15 × S\nL + 300 = 35 × S\n15S + 300 = 35S → 20S = 300 → S = 15 m/s\nTrain Length L = 15 × 15 = 225 m.",
        "tips": "Platform time − Pole time = Platform length / Speed.",
        "options": [
            {"label": "A", "text": "200 m", "is_correct": False},
            {"label": "B", "text": "225 m", "is_correct": True},
            {"label": "C", "text": "250 m", "is_correct": False},
            {"label": "D", "text": "300 m", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Upstream Travel Time",
        "difficulty": "Hard",
        "question_text": "A boat's speed in still water is 12 km/h and the stream speed is 4 km/h. Find the time taken to travel 48 km upstream.",
        "sample_answer": "Upstream speed = Boat speed − Stream speed = 12 − 4 = 8 km/h\nTime = 48 / 8 = 6 hours.",
        "tips": "Upstream Speed = Speed in Still Water − Stream Speed.",
        "options": [
            {"label": "A", "text": "4 hours", "is_correct": False},
            {"label": "B", "text": "5 hours", "is_correct": False},
            {"label": "C", "text": "6 hours", "is_correct": True},
            {"label": "D", "text": "8 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Total Time Distance Problem",
        "difficulty": "Hard",
        "question_text": "A person covers a certain distance at 5 km/h and returns at 3 km/h. If the total time taken is 16 hours, find the distance.",
        "sample_answer": "Let distance = D km.\nD/5 + D/3 = 16\n(3D + 5D) / 15 = 16 → 8D / 15 = 16 → 8D = 240 → D = 30 km.",
        "tips": "Distance = Total Time × (x × y) / (x + y).",
        "options": [
            {"label": "A", "text": "25 km", "is_correct": False},
            {"label": "B", "text": "30 km", "is_correct": True},
            {"label": "C", "text": "35 km", "is_correct": False},
            {"label": "D", "text": "40 km", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Distance Separation Between Cars",
        "difficulty": "Hard",
        "question_text": "Two cars start simultaneously from the same point in the same direction at 60 km/h and 80 km/h. After how much time will they be 100 km apart?",
        "sample_answer": "Relative speed = 80 − 60 = 20 km/h\nTime = Separation / Relative Speed = 100 / 20 = 5 hours.",
        "tips": "Time = Separation Distance / Relative Speed.",
        "options": [
            {"label": "A", "text": "4 hours", "is_correct": False},
            {"label": "B", "text": "5 hours", "is_correct": True},
            {"label": "C", "text": "6 hours", "is_correct": False},
            {"label": "D", "text": "7.5 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Speed of Second Train in Opposite Direction",
        "difficulty": "Hard",
        "question_text": "A train 240 m long crosses another train 160 m long moving in the opposite direction at 54 km/h. If the crossing time is 10 seconds, find the speed of the second train.",
        "sample_answer": "Total distance = 240 + 160 = 400 m\nRelative speed = 400 / 10 = 40 m/s = 40 × (18/5) = 144 km/h\nTrain 2 speed = 144 − 54 = 90 km/h.",
        "tips": "Speed of Train 2 = Total Relative Speed in km/h − Speed of Train 1.",
        "options": [
            {"label": "A", "text": "72 km/h", "is_correct": False},
            {"label": "B", "text": "80 km/h", "is_correct": False},
            {"label": "C", "text": "90 km/h", "is_correct": True},
            {"label": "D", "text": "100 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Three Thirds Journey Average Speed",
        "difficulty": "Hard",
        "question_text": "A cyclist covers one-third of a journey at 10 km/h, one-third at 15 km/h, and the remaining one-third at 20 km/h. Find the average speed.",
        "sample_answer": "Average Speed = 3 / (1/10 + 1/15 + 1/20) = 3 / ((6 + 4 + 3)/60) = 3 / (13/60) = 180 / 13 = 13.85 km/h (13 11/13 km/h).",
        "tips": "Harmonic mean formula for three equal parts: 3 / (1/x + 1/y + 1/z).",
        "options": [
            {"label": "A", "text": "13.85 km/h (13 11/13 km/h)", "is_correct": True},
            {"label": "B", "text": "14.5 km/h", "is_correct": False},
            {"label": "C", "text": "15.0 km/h", "is_correct": False},
            {"label": "D", "text": "16.2 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Stream Speed Calculation",
        "difficulty": "Hard",
        "question_text": "A boat travels 30 km downstream in 2 hours and the same distance upstream in 3 hours. Find the speed of the stream.",
        "sample_answer": "Downstream speed D = 30 / 2 = 15 km/h\nUpstream speed U = 30 / 3 = 10 km/h\nStream speed = (D − U) / 2 = (15 − 10) / 2 = 2.5 km/h.",
        "tips": "Speed of Stream = (Downstream Speed − Upstream Speed) / 2.",
        "options": [
            {"label": "A", "text": "2.0 km/h", "is_correct": False},
            {"label": "B", "text": "2.5 km/h", "is_correct": True},
            {"label": "C", "text": "3.0 km/h", "is_correct": False},
            {"label": "D", "text": "3.5 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Train Length from Tunnel Crossing",
        "difficulty": "Hard",
        "question_text": "A train moving at 108 km/h crosses a tunnel 450 m long in 30 seconds. Find the length of the train.",
        "sample_answer": "Speed in m/s = 108 × (5/18) = 30 m/s\nTotal distance = 30 × 30 = 900 m\nTrain length = Total distance − Tunnel length = 900 − 450 = 450 m.",
        "tips": "Train Length = (Speed in m/s × Time) − Tunnel Length.",
        "options": [
            {"label": "A", "text": "350 m", "is_correct": False},
            {"label": "B", "text": "400 m", "is_correct": False},
            {"label": "C", "text": "450 m", "is_correct": True},
            {"label": "D", "text": "500 m", "is_correct": False}
        ],
        "correct_option": "C"
    }
]

def seed_tsd():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Time, Speed & Distance'")
            print(f"Deleted old 'Time, Speed & Distance' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Time-Based Problems',
                    'Time, Speed & Distance',
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
    seed_tsd()
