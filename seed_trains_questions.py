"""
Seed script for Trains (Time-Based Problems)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Trains - Crossing a Telegraph Pole 1",
        "difficulty": "Easy",
        "question_text": "A train 180 m long is running at a speed of 72 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 72 \u00d7 (5 / 18) = 20 m/s.\nDistance to cross a pole = Length of train = 180 m.\nTime = Distance / Speed = 180 / 20 = 9 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "7.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 2",
        "difficulty": "Easy",
        "question_text": "A train 180 m long is running at a speed of 90 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 90 \u00d7 (5 / 18) = 25 m/s.\nDistance to cross a pole = Length of train = 180 m.\nTime = Distance / Speed = 180 / 25 = 7.2 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "5.2 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9.2 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11.2 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.2 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 3",
        "difficulty": "Easy",
        "question_text": "A train 200 m long is running at a speed of 72 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 72 \u00d7 (5 / 18) = 20 m/s.\nDistance to cross a pole = Length of train = 200 m.\nTime = Distance / Speed = 200 / 20 = 10 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "14.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 4",
        "difficulty": "Easy",
        "question_text": "A train 200 m long is running at a speed of 72 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 72 \u00d7 (5 / 18) = 20 m/s.\nDistance to cross a pole = Length of train = 200 m.\nTime = Distance / Speed = 200 / 20 = 10 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "14.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 5",
        "difficulty": "Easy",
        "question_text": "A train 150 m long is running at a speed of 72 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 72 \u00d7 (5 / 18) = 20 m/s.\nDistance to cross a pole = Length of train = 150 m.\nTime = Distance / Speed = 150 / 20 = 7.5 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "5.5 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "11.5 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9.5 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 6",
        "difficulty": "Easy",
        "question_text": "A train 150 m long is running at a speed of 72 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 72 \u00d7 (5 / 18) = 20 m/s.\nDistance to cross a pole = Length of train = 150 m.\nTime = Distance / Speed = 150 / 20 = 7.5 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "5.5 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9.5 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "11.5 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 7",
        "difficulty": "Easy",
        "question_text": "A train 150 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 150 m.\nTime = Distance / Speed = 150 / 15 = 10 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "10 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "8.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 8",
        "difficulty": "Easy",
        "question_text": "A train 200 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 200 m.\nTime = Distance / Speed = 200 / 15 = 13.3 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "17.3 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15.3 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11.3 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13.3 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 9",
        "difficulty": "Easy",
        "question_text": "A train 240 m long is running at a speed of 72 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 72 \u00d7 (5 / 18) = 20 m/s.\nDistance to cross a pole = Length of train = 240 m.\nTime = Distance / Speed = 240 / 20 = 12 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "10.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 10",
        "difficulty": "Easy",
        "question_text": "A train 180 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 180 m.\nTime = Distance / Speed = 180 / 15 = 12 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "10.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 11",
        "difficulty": "Easy",
        "question_text": "A train 180 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 180 m.\nTime = Distance / Speed = 180 / 15 = 12 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "16.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "14.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 12",
        "difficulty": "Easy",
        "question_text": "A train 150 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 150 m.\nTime = Distance / Speed = 150 / 15 = 10 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "10 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "8.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 13",
        "difficulty": "Easy",
        "question_text": "A train 240 m long is running at a speed of 36 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 36 \u00d7 (5 / 18) = 10 m/s.\nDistance to cross a pole = Length of train = 240 m.\nTime = Distance / Speed = 240 / 10 = 24 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "26.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 14",
        "difficulty": "Easy",
        "question_text": "A train 120 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 120 m.\nTime = Distance / Speed = 120 / 15 = 8 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "10.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "12.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 15",
        "difficulty": "Easy",
        "question_text": "A train 150 m long is running at a speed of 36 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 36 \u00d7 (5 / 18) = 10 m/s.\nDistance to cross a pole = Length of train = 150 m.\nTime = Distance / Speed = 150 / 10 = 15 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "17.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "19.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 16",
        "difficulty": "Easy",
        "question_text": "A train 120 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 120 m.\nTime = Distance / Speed = 120 / 15 = 8 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "6.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 17",
        "difficulty": "Easy",
        "question_text": "A train 200 m long is running at a speed of 36 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 36 \u00d7 (5 / 18) = 10 m/s.\nDistance to cross a pole = Length of train = 200 m.\nTime = Distance / Speed = 200 / 10 = 20 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "18.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "22.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 18",
        "difficulty": "Easy",
        "question_text": "A train 180 m long is running at a speed of 36 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 36 \u00d7 (5 / 18) = 10 m/s.\nDistance to cross a pole = Length of train = 180 m.\nTime = Distance / Speed = 180 / 10 = 18 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "18 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "16.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 19",
        "difficulty": "Easy",
        "question_text": "A train 180 m long is running at a speed of 90 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 90 \u00d7 (5 / 18) = 25 m/s.\nDistance to cross a pole = Length of train = 180 m.\nTime = Distance / Speed = 180 / 25 = 7.2 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "5.2 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9.2 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.2 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "11.2 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Crossing a Telegraph Pole 20",
        "difficulty": "Easy",
        "question_text": "A train 180 m long is running at a speed of 54 km/h. How many seconds will it take to pass a telegraph post?",
        "sample_answer": "Speed in m/s = 54 \u00d7 (5 / 18) = 15 m/s.\nDistance to cross a pole = Length of train = 180 m.\nTime = Distance / Speed = 180 / 15 = 12 sec.",
        "tips": "Distance to cross a pole/man is strictly the train's own length.",
        "options": [
            {
                "label": "A",
                "text": "14.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "16.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing Platform 21",
        "difficulty": "Medium",
        "question_text": "A train 150 m in length travels at 54 km/h. How much time does it take to cross a platform of length 150 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 150 + 150 = 300 m.\nSpeed in m/s = 54 \u00d7 5/18 = 15 m/s.\nTime = 300 / 15 = 20 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "26.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "17.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing Platform 22",
        "difficulty": "Medium",
        "question_text": "A train 150 m in length travels at 54 km/h. How much time does it take to cross a platform of length 200 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 150 + 200 = 350 m.\nSpeed in m/s = 54 \u00d7 5/18 = 15 m/s.\nTime = 350 / 15 = 23.3 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "23.3 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "20.3 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26.3 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "29.3 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Crossing Platform 23",
        "difficulty": "Medium",
        "question_text": "A train 150 m in length travels at 72 km/h. How much time does it take to cross a platform of length 200 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 150 + 200 = 350 m.\nSpeed in m/s = 72 \u00d7 5/18 = 20 m/s.\nTime = 350 / 20 = 17.5 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "23.5 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20.5 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.5 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17.5 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing Platform 24",
        "difficulty": "Medium",
        "question_text": "A train 200 m in length travels at 72 km/h. How much time does it take to cross a platform of length 150 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 200 + 150 = 350 m.\nSpeed in m/s = 72 \u00d7 5/18 = 20 m/s.\nTime = 350 / 20 = 17.5 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "14.5 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.5 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "23.5 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20.5 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing Platform 25",
        "difficulty": "Medium",
        "question_text": "A train 250 m in length travels at 54 km/h. How much time does it take to cross a platform of length 200 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 250 + 200 = 450 m.\nSpeed in m/s = 54 \u00d7 5/18 = 15 m/s.\nTime = 450 / 15 = 30 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "27.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "36.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "33.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing Platform 26",
        "difficulty": "Medium",
        "question_text": "A train 150 m in length travels at 72 km/h. How much time does it take to cross a platform of length 250 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 150 + 250 = 400 m.\nSpeed in m/s = 72 \u00d7 5/18 = 20 m/s.\nTime = 400 / 20 = 20 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "26.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "17.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing Platform 27",
        "difficulty": "Medium",
        "question_text": "A train 200 m in length travels at 90 km/h. How much time does it take to cross a platform of length 250 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 200 + 250 = 450 m.\nSpeed in m/s = 90 \u00d7 5/18 = 25 m/s.\nTime = 450 / 25 = 18 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "18 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "24.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "21.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Crossing Platform 28",
        "difficulty": "Medium",
        "question_text": "A train 250 m in length travels at 90 km/h. How much time does it take to cross a platform of length 250 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 250 + 250 = 500 m.\nSpeed in m/s = 90 \u00d7 5/18 = 25 m/s.\nTime = 500 / 25 = 20 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "26.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "23.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Crossing Platform 29",
        "difficulty": "Medium",
        "question_text": "A train 150 m in length travels at 72 km/h. How much time does it take to cross a platform of length 150 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 150 + 150 = 300 m.\nSpeed in m/s = 72 \u00d7 5/18 = 20 m/s.\nTime = 300 / 20 = 15 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "15 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "18.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Crossing Platform 30",
        "difficulty": "Medium",
        "question_text": "A train 250 m in length travels at 90 km/h. How much time does it take to cross a platform of length 250 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 250 + 250 = 500 m.\nSpeed in m/s = 90 \u00d7 5/18 = 25 m/s.\nTime = 500 / 25 = 20 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "17.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "26.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Crossing Platform 31",
        "difficulty": "Medium",
        "question_text": "A train 200 m in length travels at 54 km/h. How much time does it take to cross a platform of length 250 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 200 + 250 = 450 m.\nSpeed in m/s = 54 \u00d7 5/18 = 15 m/s.\nTime = 450 / 15 = 30 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "36.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "27.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "33.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Crossing Platform 32",
        "difficulty": "Medium",
        "question_text": "A train 200 m in length travels at 90 km/h. How much time does it take to cross a platform of length 200 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 200 + 200 = 400 m.\nSpeed in m/s = 90 \u00d7 5/18 = 25 m/s.\nTime = 400 / 25 = 16 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "19.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Crossing Platform 33",
        "difficulty": "Medium",
        "question_text": "A train 200 m in length travels at 90 km/h. How much time does it take to cross a platform of length 150 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 200 + 150 = 350 m.\nSpeed in m/s = 90 \u00d7 5/18 = 25 m/s.\nTime = 350 / 25 = 14 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "14 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "11.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Crossing Platform 34",
        "difficulty": "Medium",
        "question_text": "A train 200 m in length travels at 90 km/h. How much time does it take to cross a platform of length 200 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 200 + 200 = 400 m.\nSpeed in m/s = 90 \u00d7 5/18 = 25 m/s.\nTime = 400 / 25 = 16 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "13.0 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22.0 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "19.0 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Crossing Platform 35",
        "difficulty": "Medium",
        "question_text": "A train 200 m in length travels at 54 km/h. How much time does it take to cross a platform of length 200 m?",
        "sample_answer": "Total distance to cross platform = Length of train + Length of platform = 200 + 200 = 400 m.\nSpeed in m/s = 54 \u00d7 5/18 = 15 m/s.\nTime = 400 / 15 = 26.7 sec.",
        "tips": "Total Distance = Train Length + Platform Length.",
        "options": [
            {
                "label": "A",
                "text": "23.7 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32.7 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "29.7 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26.7 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Opposite Directions Crossing 36",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Opposite Directions Crossing 37",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Opposite Directions Crossing 38",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Opposite Directions Crossing 39",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Opposite Directions Crossing 40",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Opposite Directions Crossing 41",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Opposite Directions Crossing 42",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "15 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Opposite Directions Crossing 43",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "15 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Opposite Directions Crossing 44",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Opposite Directions Crossing 45",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Opposite Directions Crossing 46",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18 sec",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Trains - Opposite Directions Crossing 47",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 sec",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Trains - Opposite Directions Crossing 48",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Trains - Opposite Directions Crossing 49",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "18 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "15 sec",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Trains - Opposite Directions Crossing 50",
        "difficulty": "Medium",
        "question_text": "Two trains of lengths 120 m and 180 m travel in opposite directions at 54 km/h and 36 km/h. In how many seconds will they completely cross each other?",
        "sample_answer": "Total distance = 120 + 180 = 300 m.\nRelative speed in opposite directions = 54 + 36 = 90 km/h = (90 \u00d7 5/18) = 25 m/s.\nTime = 300 / 25 = 12 seconds.",
        "tips": "Opposite directions: Relative Speed = Speed1 + Speed2.",
        "options": [
            {
                "label": "A",
                "text": "10 sec",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 sec",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "15 sec",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18 sec",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Trains').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Trains').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Time-Based Problems',
                    topic='Trains',
                    title=q.get('title', 'Trains'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Trains via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Trains: {e}")

    # 2. Update local SQLite database if present
    db_paths = [
        os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
        os.path.join(os.path.dirname(__file__), 'interview_portal.db')
    ]
    for p in db_paths:
        if os.path.exists(p):
            try:
                conn = sqlite3.connect(p)
                cur = conn.cursor()
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Trains',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Time-Based Problems', 'Trains',
                        q.get('title', 'Trains'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Trains into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
