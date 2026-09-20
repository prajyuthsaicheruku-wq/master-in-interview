"""
Seed script for Boats & Streams (Time-Based Problems)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Boats & Streams - Downstream Speed 1",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 19 km/h in still water. If the speed of the river stream is 2 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 19 + 2 = 21 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "23 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "19 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed 2",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 13 km/h in still water. If the speed of the river stream is 5 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 13 + 5 = 18 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "20 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "8 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Downstream Speed 3",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 17 km/h in still water. If the speed of the river stream is 4 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 17 + 4 = 21 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "21 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "23 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Downstream Speed 4",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 18 km/h in still water. If the speed of the river stream is 6 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 18 + 6 = 24 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "24 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "26 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Downstream Speed 5",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 20 km/h in still water. If the speed of the river stream is 6 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 20 + 6 = 26 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "24 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "14 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed 6",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 16 km/h in still water. If the speed of the river stream is 2 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 16 + 2 = 18 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "16 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Downstream Speed 7",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 13 km/h in still water. If the speed of the river stream is 2 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 13 + 2 = 15 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "11 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "17 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Downstream Speed 8",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 15 km/h in still water. If the speed of the river stream is 6 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 15 + 6 = 21 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "23 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "19 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed 9",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 19 km/h in still water. If the speed of the river stream is 2 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 19 + 2 = 21 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "19 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "23 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Downstream Speed 10",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 10 km/h in still water. If the speed of the river stream is 2 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 10 + 2 = 12 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "12 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "14 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Downstream Speed 11",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 18 km/h in still water. If the speed of the river stream is 6 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 18 + 6 = 24 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "22 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "24 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Downstream Speed 12",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 19 km/h in still water. If the speed of the river stream is 4 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 19 + 4 = 23 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "25 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Downstream Speed 13",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 13 km/h in still water. If the speed of the river stream is 5 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 13 + 5 = 18 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "8 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "20 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Downstream Speed 14",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 11 km/h in still water. If the speed of the river stream is 5 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 11 + 5 = 16 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "6 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "18 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed 15",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 17 km/h in still water. If the speed of the river stream is 6 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 17 + 6 = 23 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "25 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "23 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "11 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Downstream Speed 16",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 16 km/h in still water. If the speed of the river stream is 6 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 16 + 6 = 22 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "10 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "24 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed 17",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 17 km/h in still water. If the speed of the river stream is 3 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 17 + 3 = 20 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "18 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "14 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Downstream Speed 18",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 13 km/h in still water. If the speed of the river stream is 5 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 13 + 5 = 18 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "18 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "20 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Downstream Speed 19",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 13 km/h in still water. If the speed of the river stream is 6 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 13 + 6 = 19 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "19 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "17 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Downstream Speed 20",
        "difficulty": "Easy",
        "question_text": "A boat can travel with a speed of 18 km/h in still water. If the speed of the river stream is 3 km/h, find the speed of the boat going downstream.",
        "sample_answer": "Downstream Speed = Speed of Boat + Speed of Stream = 18 + 3 = 21 km/h.",
        "tips": "Downstream = Boat + Stream. Upstream = Boat - Stream.",
        "options": [
            {
                "label": "A",
                "text": "19 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "15 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 21",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 18 km/h downstream and 14 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (18 + 14) / 2 = 16 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "16 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 22",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 20 km/h downstream and 12 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (20 + 12) / 2 = 16 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "16 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 23",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 18 km/h downstream and 10 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (18 + 10) / 2 = 14 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "16.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 24",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 20 km/h downstream and 10 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (20 + 10) / 2 = 15 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "17.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 25",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 16 km/h downstream and 12 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (16 + 12) / 2 = 14 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 26",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 16 km/h downstream and 12 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (16 + 12) / 2 = 14 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "12.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "16.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 27",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 18 km/h downstream and 14 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (18 + 14) / 2 = 16 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 28",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 20 km/h downstream and 12 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (20 + 12) / 2 = 16 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "18.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 29",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 18 km/h downstream and 12 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (18 + 12) / 2 = 15 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "3.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 30",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 18 km/h downstream and 8 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (18 + 8) / 2 = 13 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "5.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 31",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 18 km/h downstream and 8 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (18 + 8) / 2 = 13 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "13 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "11.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 32",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 16 km/h downstream and 12 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (16 + 12) / 2 = 14 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "16.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 33",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 16 km/h downstream and 14 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (16 + 14) / 2 = 15 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "13.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 34",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 16 km/h downstream and 14 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (16 + 14) / 2 = 15 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "13.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Speed in Still Water 35",
        "difficulty": "Medium",
        "question_text": "A motorboat travels at 18 km/h downstream and 14 km/h upstream. Find the speed of the boat in still water.",
        "sample_answer": "Speed in still water = (Downstream Speed + Upstream Speed) / 2 = (18 + 14) / 2 = 16 km/h.",
        "tips": "Boat in still water = (Downstream + Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "16 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "18.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Stream Rate 36",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 16 km/h and upstream is 10 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (16 - 10) / 2 = 3 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Stream Rate 37",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 18 km/h and upstream is 10 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (18 - 10) / 2 = 4 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "5.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "14.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Stream Rate 38",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 16 km/h and upstream is 12 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (16 - 12) / 2 = 2 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "2 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "1 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Stream Rate 39",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 18 km/h and upstream is 10 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (18 - 10) / 2 = 4 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "3.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Stream Rate 40",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 22 km/h and upstream is 12 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (22 - 12) / 2 = 5 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "5 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Stream Rate 41",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 22 km/h and upstream is 6 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (22 - 6) / 2 = 8 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "7.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Stream Rate 42",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 22 km/h and upstream is 10 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (22 - 10) / 2 = 6 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "5.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "7.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "16.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Stream Rate 43",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 14 km/h and upstream is 6 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (14 - 6) / 2 = 4 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "4 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "10.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Stream Rate 44",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 22 km/h and upstream is 6 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (22 - 6) / 2 = 8 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "9.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Stream Rate 45",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 14 km/h and upstream is 12 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (14 - 12) / 2 = 1 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "1 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Stream Rate 46",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 18 km/h and upstream is 12 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (18 - 12) / 2 = 3 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "15.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Boats & Streams - Stream Rate 47",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 18 km/h and upstream is 12 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (18 - 12) / 2 = 3 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "15.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Boats & Streams - Stream Rate 48",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 18 km/h and upstream is 6 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (18 - 6) / 2 = 6 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "6 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "7.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Boats & Streams - Stream Rate 49",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 22 km/h and upstream is 6 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (22 - 6) / 2 = 8 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "14.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "7.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Boats & Streams - Stream Rate 50",
        "difficulty": "Medium",
        "question_text": "If a rower's speed downstream is 22 km/h and upstream is 12 km/h, what is the speed of the current?",
        "sample_answer": "Speed of current / stream = (Downstream Speed - Upstream Speed) / 2 = (22 - 12) / 2 = 5 km/h.",
        "tips": "Stream rate = (Downstream - Upstream) / 2.",
        "options": [
            {
                "label": "A",
                "text": "4.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5 km/h",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Boats & Streams').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Boats & Streams').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Time-Based Problems',
                    topic='Boats & Streams',
                    title=q.get('title', 'Boats & Streams'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Boats & Streams via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Boats & Streams: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Boats & Streams',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Time-Based Problems', 'Boats & Streams',
                        q.get('title', 'Boats & Streams'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Boats & Streams into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
