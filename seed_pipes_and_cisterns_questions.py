"""
Seed script for Pipes & Cisterns (Time-Based Problems)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Pipes & Cisterns - Two Inlets 1",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 12 hours and Pipe B can fill it in 15 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/12 + 1/15 = (12 + 15) / (12 \u00d7 15).\nTime = (12 \u00d7 15) / (12 + 15) = 6.7 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "6.7 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "27 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4.7 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.7 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 2",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 12 hours and Pipe B can fill it in 60 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/12 + 1/60 = (12 + 60) / (12 \u00d7 60).\nTime = (12 \u00d7 60) / (12 + 60) = 10 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "10 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "8.0 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "72 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 3",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 30 hours and Pipe B can fill it in 10 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/30 + 1/10 = (30 + 10) / (30 \u00d7 10).\nTime = (30 \u00d7 10) / (30 + 10) = 7.5 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "40 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "5.5 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9.5 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 4",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 24 hours and Pipe B can fill it in 30 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/24 + 1/30 = (24 + 30) / (24 \u00d7 30).\nTime = (24 \u00d7 30) / (24 + 30) = 13.3 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "15.3 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11.3 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.3 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "54 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 5",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 20 hours and Pipe B can fill it in 10 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/20 + 1/10 = (20 + 10) / (20 \u00d7 10).\nTime = (20 \u00d7 10) / (20 + 10) = 6.7 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "30 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4.7 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6.7 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "8.7 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 6",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 30 hours and Pipe B can fill it in 10 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/30 + 1/10 = (30 + 10) / (30 \u00d7 10).\nTime = (30 \u00d7 10) / (30 + 10) = 7.5 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "9.5 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5.5 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "40 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 7",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 24 hours and Pipe B can fill it in 20 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/24 + 1/20 = (24 + 20) / (24 \u00d7 20).\nTime = (24 \u00d7 20) / (24 + 20) = 10.9 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "10.9 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "12.9 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "44 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.9 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 8",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 24 hours and Pipe B can fill it in 10 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/24 + 1/10 = (24 + 10) / (24 \u00d7 10).\nTime = (24 \u00d7 10) / (24 + 10) = 7.1 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "7.1 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "5.1 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9.1 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 9",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 15 hours and Pipe B can fill it in 15 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/15 + 1/15 = (15 + 15) / (15 \u00d7 15).\nTime = (15 \u00d7 15) / (15 + 15) = 7.5 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5.5 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9.5 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 10",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 12 hours and Pipe B can fill it in 20 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/12 + 1/20 = (12 + 20) / (12 \u00d7 20).\nTime = (12 \u00d7 20) / (12 + 20) = 7.5 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "5.5 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "32 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9.5 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 11",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 20 hours and Pipe B can fill it in 10 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/20 + 1/10 = (20 + 10) / (20 \u00d7 10).\nTime = (20 \u00d7 10) / (20 + 10) = 6.7 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "30 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.7 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8.7 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4.7 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 12",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 24 hours and Pipe B can fill it in 30 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/24 + 1/30 = (24 + 30) / (24 \u00d7 30).\nTime = (24 \u00d7 30) / (24 + 30) = 13.3 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "54 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15.3 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11.3 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13.3 hours",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 13",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 12 hours and Pipe B can fill it in 20 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/12 + 1/20 = (12 + 20) / (12 \u00d7 20).\nTime = (12 \u00d7 20) / (12 + 20) = 7.5 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "9.5 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "5.5 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 14",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 30 hours and Pipe B can fill it in 30 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/30 + 1/30 = (30 + 30) / (30 \u00d7 30).\nTime = (30 \u00d7 30) / (30 + 30) = 15 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "15 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "13.0 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 15",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 15 hours and Pipe B can fill it in 30 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/15 + 1/30 = (15 + 30) / (15 \u00d7 30).\nTime = (15 \u00d7 30) / (15 + 30) = 10 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "45 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8.0 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 16",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 20 hours and Pipe B can fill it in 15 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/20 + 1/15 = (20 + 15) / (20 \u00d7 15).\nTime = (20 \u00d7 15) / (20 + 15) = 8.6 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "35 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.6 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10.6 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.6 hours",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 17",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 30 hours and Pipe B can fill it in 60 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/30 + 1/60 = (30 + 60) / (30 \u00d7 60).\nTime = (30 \u00d7 60) / (30 + 60) = 20 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "20 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "90 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22.0 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 18",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 15 hours and Pipe B can fill it in 30 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/15 + 1/30 = (15 + 30) / (15 \u00d7 30).\nTime = (15 \u00d7 30) / (15 + 30) = 10 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "12.0 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "45 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 19",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 12 hours and Pipe B can fill it in 30 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/12 + 1/30 = (12 + 30) / (12 \u00d7 30).\nTime = (12 \u00d7 30) / (12 + 30) = 8.6 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "42 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.6 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "6.6 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10.6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Two Inlets 20",
        "difficulty": "Easy",
        "question_text": "Pipe A can fill a tank in 30 hours and Pipe B can fill it in 10 hours. If both pipes are opened together, how long will they take to fill the tank?",
        "sample_answer": "Combined rate = 1/30 + 1/10 = (30 + 10) / (30 \u00d7 10).\nTime = (30 \u00d7 10) / (30 + 10) = 7.5 hours.",
        "tips": "Combined fill time = (p1 * p2) / (p1 + p2).",
        "options": [
            {
                "label": "A",
                "text": "40 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5.5 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9.5 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.5 hours",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 21",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 6 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 24 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/6 - 1/24 = (24 - 6) / (6 \u00d7 24).\nTime = (6 \u00d7 24) / (24 - 6) = 8 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "8 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "5.0 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 22",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 10 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 18 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/10 - 1/18 = (18 - 10) / (10 \u00d7 18).\nTime = (10 \u00d7 18) / (18 - 10) = 22.5 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "19.5 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "25.5 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22.5 hours",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 23",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 8 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 20 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/8 - 1/20 = (20 - 8) / (8 \u00d7 20).\nTime = (8 \u00d7 20) / (20 - 8) = 13.3 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "16.3 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10.3 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.3 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "28 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 24",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 12 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 15 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/12 - 1/15 = (15 - 12) / (12 \u00d7 15).\nTime = (12 \u00d7 15) / (15 - 12) = 60 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "63.0 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "57.0 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "27 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 25",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 10 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 24 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/10 - 1/24 = (24 - 10) / (10 \u00d7 24).\nTime = (10 \u00d7 24) / (24 - 10) = 17.1 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "17.1 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "20.1 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.1 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 26",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 6 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 20 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/6 - 1/20 = (20 - 6) / (6 \u00d7 20).\nTime = (6 \u00d7 20) / (20 - 6) = 8.6 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "8.6 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "5.6 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11.6 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 27",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 6 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 15 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/6 - 1/15 = (15 - 6) / (6 \u00d7 15).\nTime = (6 \u00d7 15) / (15 - 6) = 10 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "13.0 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "21 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 28",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 6 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 18 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/6 - 1/18 = (18 - 6) / (6 \u00d7 18).\nTime = (6 \u00d7 18) / (18 - 6) = 9 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "24 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "12.0 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 29",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 6 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 20 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/6 - 1/20 = (20 - 6) / (6 \u00d7 20).\nTime = (6 \u00d7 20) / (20 - 6) = 8.6 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "11.6 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.6 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "26 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5.6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 30",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 8 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 20 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/8 - 1/20 = (20 - 8) / (8 \u00d7 20).\nTime = (8 \u00d7 20) / (20 - 8) = 13.3 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "16.3 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10.3 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.3 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "28 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 31",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 10 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 15 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/10 - 1/15 = (15 - 10) / (10 \u00d7 15).\nTime = (10 \u00d7 15) / (15 - 10) = 30 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "30 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "25 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "27.0 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "33.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 32",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 12 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 15 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/12 - 1/15 = (15 - 12) / (12 \u00d7 15).\nTime = (12 \u00d7 15) / (15 - 12) = 60 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "57.0 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "27 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "63.0 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "60 hours",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 33",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 10 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 15 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/10 - 1/15 = (15 - 10) / (10 \u00d7 15).\nTime = (10 \u00d7 15) / (15 - 10) = 30 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "30 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "33.0 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "27.0 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 34",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 8 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 20 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/8 - 1/20 = (20 - 8) / (8 \u00d7 20).\nTime = (8 \u00d7 20) / (20 - 8) = 13.3 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "10.3 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16.3 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.3 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "28 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Inlet and Leak 35",
        "difficulty": "Medium",
        "question_text": "A tap can fill a tank in 8 hours, but due to a leak at the bottom, it takes longer. If the leak alone can empty the full tank in 15 hours, how long will it take to fill the tank when both are open?",
        "sample_answer": "Net filling rate = 1/8 - 1/15 = (15 - 8) / (8 \u00d7 15).\nTime = (8 \u00d7 15) / (15 - 8) = 17.1 hours.",
        "tips": "Net rate = (1/Inlet) - (1/Outlet).",
        "options": [
            {
                "label": "A",
                "text": "14.1 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20.1 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17.1 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "23 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 36",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "6 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 37",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 38",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "8 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 39",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 40",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 41",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 42",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "6 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 43",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 44",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 45",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "6 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 46",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.5 hours",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 47",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "9 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 48",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.5 hours",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 49",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "6 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 hours",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Pipes & Cisterns - Three Pipes System 50",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a cistern in 10 hours and 15 hours respectively, while pipe C can empty it in 30 hours. If all three pipes are opened together, in how many hours will the cistern be full?",
        "sample_answer": "Net rate per hour = 1/10 + 1/15 - 1/30 = 1/10 + 1/15 - 1/30 = (3 + 2 - 1) / 30 = 4/30.\nTotal time = 30 / 4 = 7.5 hours.",
        "tips": "Sum the filling rates and subtract the emptying rate.",
        "options": [
            {
                "label": "A",
                "text": "9 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 hours",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8 hours",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6 hours",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Pipes & Cisterns').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Pipes & Cisterns').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Time-Based Problems',
                    topic='Pipes & Cisterns',
                    title=q.get('title', 'Pipes & Cisterns'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Pipes & Cisterns via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Pipes & Cisterns: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Pipes & Cisterns',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Time-Based Problems', 'Pipes & Cisterns',
                        q.get('title', 'Pipes & Cisterns'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Pipes & Cisterns into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
