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
        "title": "Boats & Streams - Downstream Speed Calculation",
        "difficulty": "Medium",
        "question_text": "A boat travels 30 km downstream in 2 hours. Find its downstream speed.",
        "sample_answer": "Downstream Speed = Distance / Time = 30 / 2 = 15 km/h.",
        "tips": "Downstream Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "12 km/h", "is_correct": False},
            {"label": "B", "text": "15 km/h", "is_correct": True},
            {"label": "C", "text": "18 km/h", "is_correct": False},
            {"label": "D", "text": "20 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Upstream Speed Calculation",
        "difficulty": "Medium",
        "question_text": "A boat travels 24 km upstream in 4 hours. Find its upstream speed.",
        "sample_answer": "Upstream Speed = Distance / Time = 24 / 4 = 6 km/h.",
        "tips": "Upstream Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "4 km/h", "is_correct": False},
            {"label": "B", "text": "6 km/h", "is_correct": True},
            {"label": "C", "text": "8 km/h", "is_correct": False},
            {"label": "D", "text": "10 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed from Still Water & Stream",
        "difficulty": "Medium",
        "question_text": "The speed of a boat in still water is 12 km/h and the speed of the stream is 3 km/h. Find the downstream speed.",
        "sample_answer": "Downstream Speed = Speed in Still Water + Speed of Stream = 12 + 3 = 15 km/h.",
        "tips": "Downstream Speed = Boat Speed + Stream Speed.",
        "options": [
            {"label": "A", "text": "9 km/h", "is_correct": False},
            {"label": "B", "text": "12 km/h", "is_correct": False},
            {"label": "C", "text": "15 km/h", "is_correct": True},
            {"label": "D", "text": "18 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Upstream Speed from Still Water & Stream",
        "difficulty": "Medium",
        "question_text": "The speed of a boat in still water is 15 km/h and the speed of the stream is 4 km/h. Find the upstream speed.",
        "sample_answer": "Upstream Speed = Speed in Still Water − Speed of Stream = 15 − 4 = 11 km/h.",
        "tips": "Upstream Speed = Boat Speed − Stream Speed.",
        "options": [
            {"label": "A", "text": "10 km/h", "is_correct": False},
            {"label": "B", "text": "11 km/h", "is_correct": True},
            {"label": "C", "text": "15 km/h", "is_correct": False},
            {"label": "D", "text": "19 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Decimal Time Downstream Speed",
        "difficulty": "Medium",
        "question_text": "A boat travels 40 km downstream in 2.5 hours. Find its downstream speed.",
        "sample_answer": "Downstream Speed = Distance / Time = 40 / 2.5 = 16 km/h.",
        "tips": "Downstream Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "14 km/h", "is_correct": False},
            {"label": "B", "text": "16 km/h", "is_correct": True},
            {"label": "C", "text": "18 km/h", "is_correct": False},
            {"label": "D", "text": "20 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Both Speeds Calculation",
        "difficulty": "Medium",
        "question_text": "A boat can travel at 18 km/h in still water. If the stream speed is 5 km/h, find the upstream and downstream speeds.",
        "sample_answer": "Upstream Speed = 18 − 5 = 13 km/h\nDownstream Speed = 18 + 5 = 23 km/h.",
        "tips": "Upstream = B − S, Downstream = B + S.",
        "options": [
            {"label": "A", "text": "Upstream = 13 km/h, Downstream = 23 km/h", "is_correct": True},
            {"label": "B", "text": "Upstream = 12 km/h, Downstream = 22 km/h", "is_correct": False},
            {"label": "C", "text": "Upstream = 14 km/h, Downstream = 24 km/h", "is_correct": False},
            {"label": "D", "text": "Upstream = 15 km/h, Downstream = 25 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Distance Projection at Same Speed",
        "difficulty": "Medium",
        "question_text": "A boat covers 36 km downstream in 3 hours. How far will it travel in 5 hours at the same speed?",
        "sample_answer": "Downstream Speed = 36 / 3 = 12 km/h\nDistance covered in 5 hours = 12 × 5 = 60 km.",
        "tips": "Distance = Speed × Time.",
        "options": [
            {"label": "A", "text": "50 km", "is_correct": False},
            {"label": "B", "text": "54 km", "is_correct": False},
            {"label": "C", "text": "60 km", "is_correct": True},
            {"label": "D", "text": "65 km", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Downstream Travel Time",
        "difficulty": "Medium",
        "question_text": "A boat's speed in still water is 20 km/h and the stream speed is 4 km/h. Find the time taken to travel 48 km downstream.",
        "sample_answer": "Downstream Speed = 20 + 4 = 24 km/h\nTime = Distance / Speed = 48 / 24 = 2 hours.",
        "tips": "Time = Distance / (Boat Speed + Stream Speed).",
        "options": [
            {"label": "A", "text": "1.5 hours", "is_correct": False},
            {"label": "B", "text": "2 hours", "is_correct": True},
            {"label": "C", "text": "2.5 hours", "is_correct": False},
            {"label": "D", "text": "3 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Upstream Speed from 28 km",
        "difficulty": "Medium",
        "question_text": "A boat travels 28 km upstream in 4 hours. Find its upstream speed.",
        "sample_answer": "Upstream Speed = 28 / 4 = 7 km/h.",
        "tips": "Upstream Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "6 km/h", "is_correct": False},
            {"label": "B", "text": "7 km/h", "is_correct": True},
            {"label": "C", "text": "8 km/h", "is_correct": False},
            {"label": "D", "text": "9 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Time for 54 km Downstream",
        "difficulty": "Medium",
        "question_text": "A boat's speed in still water is 16 km/h and stream speed is 2 km/h. Find the time taken to cover 54 km downstream.",
        "sample_answer": "Downstream Speed = 16 + 2 = 18 km/h\nTime = 54 / 18 = 3 hours.",
        "tips": "Time = 54 / (16 + 2) = 3 hours.",
        "options": [
            {"label": "A", "text": "2.5 hours", "is_correct": False},
            {"label": "B", "text": "3 hours", "is_correct": True},
            {"label": "C", "text": "3.5 hours", "is_correct": False},
            {"label": "D", "text": "4 hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed from Equal Distance",
        "difficulty": "Medium",
        "question_text": "A boat covers 50 km downstream in 2 hours and the same distance upstream in 2.5 hours. Find the downstream speed.",
        "sample_answer": "Downstream Speed = Distance / Time = 50 / 2 = 25 km/h.",
        "tips": "Downstream Speed = Downstream Distance / Downstream Time.",
        "options": [
            {"label": "A", "text": "20 km/h", "is_correct": False},
            {"label": "B", "text": "22 km/h", "is_correct": False},
            {"label": "C", "text": "25 km/h", "is_correct": True},
            {"label": "D", "text": "30 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Basic Upstream Speed",
        "difficulty": "Medium",
        "question_text": "If the speed of the stream is 3 km/h and the boat speed in still water is 17 km/h, find the upstream speed.",
        "sample_answer": "Upstream Speed = Boat Speed − Stream Speed = 17 − 3 = 14 km/h.",
        "tips": "Upstream Speed = B − S.",
        "options": [
            {"label": "A", "text": "12 km/h", "is_correct": False},
            {"label": "B", "text": "14 km/h", "is_correct": True},
            {"label": "C", "text": "15 km/h", "is_correct": False},
            {"label": "D", "text": "20 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Rate from 72 km",
        "difficulty": "Medium",
        "question_text": "A boat covers 72 km downstream in 4 hours. Find its speed downstream.",
        "sample_answer": "Downstream Speed = 72 / 4 = 18 km/h.",
        "tips": "Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "15 km/h", "is_correct": False},
            {"label": "B", "text": "16 km/h", "is_correct": False},
            {"label": "C", "text": "18 km/h", "is_correct": True},
            {"label": "D", "text": "20 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Upstream Rate from 45 km",
        "difficulty": "Medium",
        "question_text": "A boat travels 45 km upstream in 5 hours. Find its upstream speed.",
        "sample_answer": "Upstream Speed = 45 / 5 = 9 km/h.",
        "tips": "Speed = Distance / Time.",
        "options": [
            {"label": "A", "text": "7 km/h", "is_correct": False},
            {"label": "B", "text": "8 km/h", "is_correct": False},
            {"label": "C", "text": "9 km/h", "is_correct": True},
            {"label": "D", "text": "10 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Downstream Speed for 14 km/h Boat",
        "difficulty": "Medium",
        "question_text": "A boat's speed in still water is 14 km/h and stream speed is 2 km/h. Find the downstream speed.",
        "sample_answer": "Downstream Speed = 14 + 2 = 16 km/h.",
        "tips": "Downstream Speed = B + S.",
        "options": [
            {"label": "A", "text": "12 km/h", "is_correct": False},
            {"label": "B", "text": "14 km/h", "is_correct": False},
            {"label": "C", "text": "16 km/h", "is_correct": True},
            {"label": "D", "text": "18 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # --- HARD LEVEL (Q16 - Q30) ---
    {
        "title": "Boats & Streams - Boat & Stream Speeds from Both Legs",
        "difficulty": "Hard",
        "question_text": "A boat covers 30 km downstream in 2 hours and the same distance upstream in 3 hours. Find the speed of the boat in still water and the speed of the stream.",
        "sample_answer": "Downstream speed D = 30 / 2 = 15 km/h\nUpstream speed U = 30 / 3 = 10 km/h\nBoat speed B = (D + U) / 2 = (15 + 10) / 2 = 12.5 km/h\nStream speed S = (D − U) / 2 = (15 − 10) / 2 = 2.5 km/h.",
        "tips": "Boat Speed = (D + U)/2, Stream Speed = (D − U)/2.",
        "options": [
            {"label": "A", "text": "Boat = 12.5 km/h, Stream = 2.5 km/h", "is_correct": True},
            {"label": "B", "text": "Boat = 12.0 km/h, Stream = 3.0 km/h", "is_correct": False},
            {"label": "C", "text": "Boat = 13.0 km/h, Stream = 2.0 km/h", "is_correct": False},
            {"label": "D", "text": "Boat = 14.0 km/h, Stream = 1.5 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Finding Stream Speed from Downstream",
        "difficulty": "Hard",
        "question_text": "A boat's speed in still water is 18 km/h. It takes 2 hours to travel 36 km downstream. Find the speed of the stream.",
        "sample_answer": "Downstream speed D = 36 / 2 = 18 km/h\nStream speed S = Downstream speed − Boat speed in still water = 18 − 18 = 0 km/h.",
        "tips": "Stream Speed = Downstream Speed − Boat Speed.",
        "options": [
            {"label": "A", "text": "0 km/h", "is_correct": True},
            {"label": "B", "text": "2 km/h", "is_correct": False},
            {"label": "C", "text": "3 km/h", "is_correct": False},
            {"label": "D", "text": "4 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Boat Speed from Unequal Distances",
        "difficulty": "Hard",
        "question_text": "A boat travels 48 km upstream in 4 hours and 60 km downstream in 3 hours. Find the speed of the boat in still water.",
        "sample_answer": "Upstream speed U = 48 / 4 = 12 km/h\nDownstream speed D = 60 / 3 = 20 km/h\nBoat speed B = (D + U) / 2 = (20 + 12) / 2 = 16 km/h.",
        "tips": "Boat Speed = (Downstream + Upstream) / 2.",
        "options": [
            {"label": "A", "text": "14 km/h", "is_correct": False},
            {"label": "B", "text": "15 km/h", "is_correct": False},
            {"label": "C", "text": "16 km/h", "is_correct": True},
            {"label": "D", "text": "18 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Stream Speed from Fractional Times",
        "difficulty": "Hard",
        "question_text": "A boat takes 5 hours to travel 40 km upstream and 3 hours to travel the same distance downstream. Find the speed of the stream.",
        "sample_answer": "Upstream speed U = 40 / 5 = 8 km/h\nDownstream speed D = 40 / 3 = 13.33 km/h (13 1/3 km/h)\nStream speed S = (D − U) / 2 = (13.33 − 8) / 2 = 5.33 / 2 = 2.67 km/h (2 2/3 km/h).",
        "tips": "Stream Speed = (Downstream Speed − Upstream Speed) / 2.",
        "options": [
            {"label": "A", "text": "2.0 km/h", "is_correct": False},
            {"label": "B", "text": "2.67 km/h (2 2/3 km/h)", "is_correct": True},
            {"label": "C", "text": "3.0 km/h", "is_correct": False},
            {"label": "D", "text": "3.5 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Difference Between Downstream & Upstream",
        "difficulty": "Hard",
        "question_text": "The speed of a boat in still water is 20 km/h. If the stream speed is 5 km/h, find the difference between downstream and upstream speeds.",
        "sample_answer": "Downstream speed = 20 + 5 = 25 km/h\nUpstream speed = 20 − 5 = 15 km/h\nDifference = 25 − 15 = 10 km/h (Notice: Difference = 2 × Stream Speed = 2 × 5 = 10 km/h).",
        "tips": "Difference between Downstream and Upstream = 2 × Stream Speed.",
        "options": [
            {"label": "A", "text": "5 km/h", "is_correct": False},
            {"label": "B", "text": "8 km/h", "is_correct": False},
            {"label": "C", "text": "10 km/h", "is_correct": True},
            {"label": "D", "text": "15 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Stream Speed from Round Trip Times",
        "difficulty": "Hard",
        "question_text": "A boat travels 72 km downstream in 4 hours and returns upstream in 6 hours. Find the speed of the stream.",
        "sample_answer": "Downstream speed D = 72 / 4 = 18 km/h\nUpstream speed U = 72 / 6 = 12 km/h\nStream speed S = (D − U) / 2 = (18 − 12) / 2 = 3 km/h.",
        "tips": "Stream Speed = (Downstream − Upstream) / 2.",
        "options": [
            {"label": "A", "text": "2 km/h", "is_correct": False},
            {"label": "B", "text": "3 km/h", "is_correct": True},
            {"label": "C", "text": "4 km/h", "is_correct": False},
            {"label": "D", "text": "5 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Total Round Trip Duration",
        "difficulty": "Hard",
        "question_text": "A man rows to a place 24 km away and back. His speed in still water is 8 km/h and stream speed is 2 km/h. Find the total time taken.",
        "sample_answer": "Downstream speed = 8 + 2 = 10 km/h → Time = 24 / 10 = 2.4 hours\nUpstream speed = 8 − 2 = 6 km/h → Time = 24 / 6 = 4 hours\nTotal time = 2.4 + 4 = 6.4 hours (6 hours 24 minutes).",
        "tips": "Total Time = (d / Downstream) + (d / Upstream).",
        "options": [
            {"label": "A", "text": "5.8 hours", "is_correct": False},
            {"label": "B", "text": "6.0 hours", "is_correct": False},
            {"label": "C", "text": "6.4 hours (6h 24m)", "is_correct": True},
            {"label": "D", "text": "7.0 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Boat Speed from Equal Duration Legs",
        "difficulty": "Hard",
        "question_text": "A boat covers 90 km downstream in 5 hours and 60 km upstream in 5 hours. Find the speed of the boat in still water.",
        "sample_answer": "Downstream speed D = 90 / 5 = 18 km/h\nUpstream speed U = 60 / 5 = 12 km/h\nBoat speed B = (18 + 12) / 2 = 15 km/h.",
        "tips": "Boat Speed = (D + U) / 2.",
        "options": [
            {"label": "A", "text": "13 km/h", "is_correct": False},
            {"label": "B", "text": "14 km/h", "is_correct": False},
            {"label": "C", "text": "15 km/h", "is_correct": True},
            {"label": "D", "text": "16 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Upstream Time for 54 km",
        "difficulty": "Hard",
        "question_text": "A boat's speed in still water is 15 km/h and stream speed is 3 km/h. Find the time taken to travel 54 km upstream.",
        "sample_answer": "Upstream speed = 15 − 3 = 12 km/h\nTime = 54 / 12 = 4.5 hours.",
        "tips": "Time = Distance / Upstream Speed = 54 / 12 = 4.5 hours.",
        "options": [
            {"label": "A", "text": "3.5 hours", "is_correct": False},
            {"label": "B", "text": "4.0 hours", "is_correct": False},
            {"label": "C", "text": "4.5 hours", "is_correct": True},
            {"label": "D", "text": "5.0 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Stream Speed from 3-Hour Legs",
        "difficulty": "Hard",
        "question_text": "A boat can travel 42 km downstream in 3 hours and 30 km upstream in 3 hours. Find the speed of the stream.",
        "sample_answer": "Downstream speed D = 42 / 3 = 14 km/h\nUpstream speed U = 30 / 3 = 10 km/h\nStream speed S = (D − U) / 2 = (14 − 10) / 2 = 2 km/h.",
        "tips": "Stream Speed = (14 − 10) / 2 = 2 km/h.",
        "options": [
            {"label": "A", "text": "1.5 km/h", "is_correct": False},
            {"label": "B", "text": "2.0 km/h", "is_correct": True},
            {"label": "C", "text": "2.5 km/h", "is_correct": False},
            {"label": "D", "text": "3.0 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Round Trip Time for 120 km",
        "difficulty": "Hard",
        "question_text": "A boat's speed in still water is 24 km/h and the stream speed is 6 km/h. Find the time taken to travel 120 km downstream and return.",
        "sample_answer": "Downstream speed = 24 + 6 = 30 km/h → Time = 120 / 30 = 4 hours\nUpstream speed = 24 − 6 = 18 km/h → Time = 120 / 18 = 6.67 hours (6 2/3 h)\nTotal time = 4 + 6.67 = 10.67 hours (10 2/3 hours).",
        "tips": "Total Time = (120 / 30) + (120 / 18) = 4 + 6 2/3 = 10 2/3 hours.",
        "options": [
            {"label": "A", "text": "9.5 hours", "is_correct": False},
            {"label": "B", "text": "10.0 hours", "is_correct": False},
            {"label": "C", "text": "10.67 hours (10 2/3 h)", "is_correct": True},
            {"label": "D", "text": "11.5 hours", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Boat Speed from Given Stream & Time Ratio",
        "difficulty": "Hard",
        "question_text": "A boat takes 4 hours downstream and 6 hours upstream to cover the same distance. If the stream speed is 2 km/h, find the speed of the boat in still water.",
        "sample_answer": "Let distance = d, boat speed = b.\nd = 4(b + 2) and d = 6(b − 2)\n4(b + 2) = 6(b − 2) → 4b + 8 = 6b − 12 → 2b = 20 → b = 10 km/h.",
        "tips": "Equate Distance: T_down × (b + s) = T_up × (b − s).",
        "options": [
            {"label": "A", "text": "8 km/h", "is_correct": False},
            {"label": "B", "text": "10 km/h", "is_correct": True},
            {"label": "C", "text": "12 km/h", "is_correct": False},
            {"label": "D", "text": "14 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Stream Speed from 4-Hour Distances",
        "difficulty": "Hard",
        "question_text": "A boat covers 36 km upstream in 4 hours and 60 km downstream in 4 hours. Find the speed of the stream.",
        "sample_answer": "Upstream speed U = 36 / 4 = 9 km/h\nDownstream speed D = 60 / 4 = 15 km/h\nStream speed S = (D − U) / 2 = (15 − 9) / 2 = 3 km/h.",
        "tips": "Stream Speed = (15 − 9) / 2 = 3 km/h.",
        "options": [
            {"label": "A", "text": "2 km/h", "is_correct": False},
            {"label": "B", "text": "3 km/h", "is_correct": True},
            {"label": "C", "text": "4 km/h", "is_correct": False},
            {"label": "D", "text": "5 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Both Boat & Stream Speeds from 4-Hour Leg",
        "difficulty": "Hard",
        "question_text": "A boat travels 80 km downstream in 4 hours and 48 km upstream in 4 hours. Find the speed of the boat in still water and the stream.",
        "sample_answer": "Downstream speed D = 80 / 4 = 20 km/h\nUpstream speed U = 48 / 4 = 12 km/h\nBoat speed B = (20 + 12) / 2 = 16 km/h\nStream speed S = (20 − 12) / 2 = 4 km/h.",
        "tips": "Boat = (D+U)/2, Stream = (D−U)/2.",
        "options": [
            {"label": "A", "text": "Boat = 16 km/h, Stream = 4 km/h", "is_correct": True},
            {"label": "B", "text": "Boat = 15 km/h, Stream = 5 km/h", "is_correct": False},
            {"label": "C", "text": "Boat = 17 km/h, Stream = 3 km/h", "is_correct": False},
            {"label": "D", "text": "Boat = 18 km/h, Stream = 2 km/h", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Stream Speed Quadratic Calculation",
        "difficulty": "Hard",
        "question_text": "A boat's speed in still water is 16 km/h. It travels 64 km downstream and 48 km upstream in a total of 8 hours. Find the speed of the stream.",
        "sample_answer": "Let stream speed = s km/h.\nTime equation: 64 / (16 + s) + 48 / (16 − s) = 8\nDividing by 8: 8 / (16 + s) + 6 / (16 − s) = 1\n8(16 − s) + 6(16 + s) = (16 + s)(16 − s)\n128 − 8s + 96 + 6s = 256 − s² → 224 − 2s = 256 − s²\ns² − 2s − 32 = 0 → s = (2 ± √(4 + 128)) / 2 = (2 + √132) / 2 ≈ 6.74 km/h.",
        "tips": "Set up total time equation and solve quadratic equation for s.",
        "options": [
            {"label": "A", "text": "4 km/h", "is_correct": False},
            {"label": "B", "text": "6.74 km/h", "is_correct": True},
            {"label": "C", "text": "8 km/h", "is_correct": False},
            {"label": "D", "text": "10 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_boats():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Boats & Streams'")
            print(f"Deleted old 'Boats & Streams' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Time-Based Problems',
                    'Boats & Streams',
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
    seed_boats()
