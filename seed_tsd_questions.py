"""
Seed script for Time, Speed & Distance (Time-Based Problems)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Time, Speed & Distance - Unit Conversion 1",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 18 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n18 \u00d7 (5 / 18) = 5 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "0 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5 m/s",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 2",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 36 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n36 \u00d7 (5 / 18) = 10 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "15 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 m/s",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "20 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 3",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 54 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n54 \u00d7 (5 / 18) = 15 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "25 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 m/s",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 4",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 72 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n72 \u00d7 (5 / 18) = 20 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "25 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 5",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 90 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n90 \u00d7 (5 / 18) = 25 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "20 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25 m/s",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 6",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 108 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n108 \u00d7 (5 / 18) = 30 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "35 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 m/s",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "25 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 7",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 126 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n126 \u00d7 (5 / 18) = 35 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "30 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "40 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "35 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "45 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 8",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 144 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n144 \u00d7 (5 / 18) = 40 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "45 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "50 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 9",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 162 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n162 \u00d7 (5 / 18) = 45 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "55 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "40 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "45 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "50 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 10",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 180 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n180 \u00d7 (5 / 18) = 50 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "55 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "45 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "60 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 11",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 198 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n198 \u00d7 (5 / 18) = 55 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "50 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "55 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "65 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 12",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 216 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n216 \u00d7 (5 / 18) = 60 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "60 m/s",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "55 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "70 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "65 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 13",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 234 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n234 \u00d7 (5 / 18) = 65 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "65 m/s",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "60 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "70 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "75 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 14",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 252 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n252 \u00d7 (5 / 18) = 70 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "75 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "65 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "80 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "70 m/s",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 15",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 270 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n270 \u00d7 (5 / 18) = 75 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "85 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "70 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "75 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "80 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 16",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 288 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n288 \u00d7 (5 / 18) = 80 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "80 m/s",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "90 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "75 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "85 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 17",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 306 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n306 \u00d7 (5 / 18) = 85 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "80 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "90 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "85 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "95 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 18",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 324 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n324 \u00d7 (5 / 18) = 90 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "100 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "90 m/s",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "95 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "85 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 19",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 342 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n342 \u00d7 (5 / 18) = 95 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "95 m/s",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "100 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "90 m/s",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "105 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Unit Conversion 20",
        "difficulty": "Easy",
        "question_text": "Convert a speed of 360 km/h into meters per second (m/s):",
        "sample_answer": "To convert km/h to m/s, multiply by 5/18:\n360 \u00d7 (5 / 18) = 100 m/s.",
        "tips": "Multiply km/h by 5/18 to get m/s.",
        "options": [
            {
                "label": "A",
                "text": "95 m/s",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "110 m/s",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "100 m/s",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "105 m/s",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 21",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 90 km/h. How much distance will it cover in 4 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 90 km/h \u00d7 4 hours = 360 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "410 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "340 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "380 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "360 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 22",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 80 km/h. How much distance will it cover in 4 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 80 km/h \u00d7 4 hours = 320 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "370 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "340 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "300 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "320 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 23",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 90 km/h. How much distance will it cover in 3 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 90 km/h \u00d7 3 hours = 270 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "320 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "250 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "290 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "270 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 24",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 90 km/h. How much distance will it cover in 2 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 90 km/h \u00d7 2 hours = 180 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "160 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "200 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "230 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "180 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 25",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 45 km/h. How much distance will it cover in 4 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 45 km/h \u00d7 4 hours = 180 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "160 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "230 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "200 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "180 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 26",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 75 km/h. How much distance will it cover in 2 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 75 km/h \u00d7 2 hours = 150 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "200 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "170 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "150 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "130 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 27",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 45 km/h. How much distance will it cover in 5 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 45 km/h \u00d7 5 hours = 225 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "225 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "275 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "245 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "205 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 28",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 90 km/h. How much distance will it cover in 4 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 90 km/h \u00d7 4 hours = 360 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "360 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "410 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "340 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "380 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 29",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 80 km/h. How much distance will it cover in 5 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 80 km/h \u00d7 5 hours = 400 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "380 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "400 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "450 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "420 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 30",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 45 km/h. How much distance will it cover in 4 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 45 km/h \u00d7 4 hours = 180 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "180 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "200 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "160 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "230 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 31",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 75 km/h. How much distance will it cover in 3 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 75 km/h \u00d7 3 hours = 225 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "205 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "225 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "275 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "245 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 32",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 80 km/h. How much distance will it cover in 2 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 80 km/h \u00d7 2 hours = 160 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "160 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "210 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "180 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "140 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 33",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 80 km/h. How much distance will it cover in 3 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 80 km/h \u00d7 3 hours = 240 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "290 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "220 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "240 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "260 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 34",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 90 km/h. How much distance will it cover in 4 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 90 km/h \u00d7 4 hours = 360 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "340 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "360 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "410 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "380 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Distance Traveled 35",
        "difficulty": "Easy",
        "question_text": "A bus travels at a uniform speed of 45 km/h. How much distance will it cover in 3 hours?",
        "sample_answer": "Distance = Speed \u00d7 Time = 45 km/h \u00d7 3 hours = 135 km.",
        "tips": "Distance = Speed * Time.",
        "options": [
            {
                "label": "A",
                "text": "115 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "185 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "155 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "135 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 36",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "50 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 37",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "50 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 38",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "50 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 39",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 40",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 41",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "60 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 42",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 43",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "50 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 44",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "50 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 45",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 46",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 47",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 48",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 49",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time, Speed & Distance - Early/Late Distance 50",
        "difficulty": "Medium",
        "question_text": "If a student travels at 40 km/h, he reaches school 10 minutes late. If he travels at 60 km/h, he reaches 10 minutes early. Find the distance to his school.",
        "sample_answer": "Difference in time = 10 min late + 10 min early = 20 min = 20/60 = 1/3 hr.\nD/40 - D/60 = 1/3 => D(60 - 40) / (40 \u00d7 60) = 1/3 => 20D / 2400 = 1/3 => D = 40 km.",
        "tips": "Distance = (S1 * S2 / (S2 - S1)) * Difference in Time.",
        "options": [
            {
                "label": "A",
                "text": "60 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Time, Speed & Distance').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Time, Speed & Distance').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Time-Based Problems',
                    topic='Time, Speed & Distance',
                    title=q.get('title', 'Time, Speed & Distance'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Time, Speed & Distance via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Time, Speed & Distance: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Time, Speed & Distance',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Time-Based Problems', 'Time, Speed & Distance',
                        q.get('title', 'Time, Speed & Distance'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Time, Speed & Distance into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
