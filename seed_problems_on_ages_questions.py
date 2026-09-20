"""
Seed script for Problems on Ages (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Problems on Ages - Father & Son Age 1",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 60 years and his son is 20 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 60 + 5 = 65 years.\nSon's age after 5 years = 20 + 5 = 25 years.\nRatio = 65 : 25.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "65:25",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "60:20",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "67:25",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "65:27",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Father & Son Age 2",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 38 years and his son is 19 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 38 + 10 = 48 years.\nSon's age after 10 years = 19 + 10 = 29 years.\nRatio = 48 : 29.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "48:31",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50:29",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48:29",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "38:19",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Father & Son Age 3",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 36 years and his son is 18 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 36 + 10 = 46 years.\nSon's age after 10 years = 18 + 10 = 28 years.\nRatio = 46 : 28.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "46:28",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "36:18",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48:28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "46:30",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Father & Son Age 4",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 54 years and his son is 18 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 54 + 10 = 64 years.\nSon's age after 10 years = 18 + 10 = 28 years.\nRatio = 64 : 28.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "54:18",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "64:28",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "66:28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "64:30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Father & Son Age 5",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 54 years and his son is 18 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 54 + 10 = 64 years.\nSon's age after 10 years = 18 + 10 = 28 years.\nRatio = 64 : 28.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "54:18",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "64:28",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "66:28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "64:30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Father & Son Age 6",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 36 years and his son is 18 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 36 + 5 = 41 years.\nSon's age after 5 years = 18 + 5 = 23 years.\nRatio = 41 : 23.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "41:25",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36:18",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "43:23",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "41:23",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Father & Son Age 7",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 42 years and his son is 14 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 42 + 5 = 47 years.\nSon's age after 5 years = 14 + 5 = 19 years.\nRatio = 47 : 19.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "47:21",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "47:19",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "49:19",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "42:14",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Father & Son Age 8",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 39 years and his son is 13 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 39 + 10 = 49 years.\nSon's age after 10 years = 13 + 10 = 23 years.\nRatio = 49 : 23.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "51:23",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "49:25",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "39:13",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "49:23",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Father & Son Age 9",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 33 years and his son is 11 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 33 + 5 = 38 years.\nSon's age after 5 years = 11 + 5 = 16 years.\nRatio = 38 : 16.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "33:11",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "38:18",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "38:16",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "40:16",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Father & Son Age 10",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 40 years and his son is 20 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 40 + 5 = 45 years.\nSon's age after 5 years = 20 + 5 = 25 years.\nRatio = 45 : 25.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "45:25",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "47:25",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "45:27",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40:20",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Father & Son Age 11",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 60 years and his son is 20 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 60 + 5 = 65 years.\nSon's age after 5 years = 20 + 5 = 25 years.\nRatio = 65 : 25.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "65:27",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "67:25",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "65:25",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "60:20",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Father & Son Age 12",
        "difficulty": "Easy",
        "question_text": "The present age of a father is 24 years and his son is 12 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 24 + 10 = 34 years.\nSon's age after 10 years = 12 + 10 = 22 years.\nRatio = 34 : 22.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "24:12",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "34:24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "36:22",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34:22",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Father & Son Age 13",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 51 years and his son is 17 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 51 + 5 = 56 years.\nSon's age after 5 years = 17 + 5 = 22 years.\nRatio = 56 : 22.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "56:24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "51:17",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "56:22",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "58:22",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Father & Son Age 14",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 30 years and his son is 15 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 30 + 10 = 40 years.\nSon's age after 10 years = 15 + 10 = 25 years.\nRatio = 40 : 25.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "40:27",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "40:25",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "42:25",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30:15",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Father & Son Age 15",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 24 years and his son is 12 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 24 + 10 = 34 years.\nSon's age after 10 years = 12 + 10 = 22 years.\nRatio = 34 : 22.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "34:24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36:22",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34:22",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "24:12",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Father & Son Age 16",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 20 years and his son is 10 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 20 + 10 = 30 years.\nSon's age after 10 years = 10 + 10 = 20 years.\nRatio = 30 : 20.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "20:10",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30:22",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "32:20",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30:20",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Father & Son Age 17",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 51 years and his son is 17 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 51 + 10 = 61 years.\nSon's age after 10 years = 17 + 10 = 27 years.\nRatio = 61 : 27.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "61:29",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "61:27",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "63:27",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "51:17",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Father & Son Age 18",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 60 years and his son is 20 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 60 + 10 = 70 years.\nSon's age after 10 years = 20 + 10 = 30 years.\nRatio = 70 : 30.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "60:20",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "72:30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "70:32",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "70:30",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Father & Son Age 19",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 30 years and his son is 15 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 30 + 5 = 35 years.\nSon's age after 5 years = 15 + 5 = 20 years.\nRatio = 35 : 20.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "35:20",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "35:22",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "37:20",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30:15",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Father & Son Age 20",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 42 years and his son is 14 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 42 + 5 = 47 years.\nSon's age after 5 years = 14 + 5 = 19 years.\nRatio = 47 : 19.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "42:14",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "49:19",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "47:19",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "47:21",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Father & Son Age 21",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 30 years and his son is 10 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 30 + 5 = 35 years.\nSon's age after 5 years = 10 + 5 = 15 years.\nRatio = 35 : 15.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "35:15",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "35:17",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30:10",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "37:15",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Father & Son Age 22",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 60 years and his son is 20 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 60 + 10 = 70 years.\nSon's age after 10 years = 20 + 10 = 30 years.\nRatio = 70 : 30.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "60:20",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "70:30",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "70:32",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "72:30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Father & Son Age 23",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 28 years and his son is 14 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 28 + 5 = 33 years.\nSon's age after 5 years = 14 + 5 = 19 years.\nRatio = 33 : 19.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "33:19",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "35:19",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28:14",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "33:21",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Father & Son Age 24",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 48 years and his son is 16 years. What will be the ratio of father's age to son's age after 5 years?",
        "sample_answer": "Father's age after 5 years = 48 + 5 = 53 years.\nSon's age after 5 years = 16 + 5 = 21 years.\nRatio = 53 : 21.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "53:21",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "48:16",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "55:21",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "53:23",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Father & Son Age 25",
        "difficulty": "Medium",
        "question_text": "The present age of a father is 30 years and his son is 10 years. What will be the ratio of father's age to son's age after 10 years?",
        "sample_answer": "Father's age after 10 years = 30 + 10 = 40 years.\nSon's age after 10 years = 10 + 10 = 20 years.\nRatio = 40 : 20.",
        "tips": "Add given years to both ages before reducing the ratio.",
        "options": [
            {
                "label": "A",
                "text": "40:20",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30:10",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40:22",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "42:20",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 26",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 49 years. A is 9 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 9.\n(x + 9) + x = 49 => 2x + 9 = 49 => 2x = 40 => x = 20.\nA's age = 29 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "29 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "31 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "27 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 27",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 80 years. A is 4 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 4.\n(x + 4) + x = 80 => 2x + 4 = 80 => 2x = 76 => x = 38.\nA's age = 42 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "44 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "42 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "40 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "38 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 28",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 84 years. A is 6 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 6.\n(x + 6) + x = 84 => 2x + 6 = 84 => 2x = 78 => x = 39.\nA's age = 45 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "47 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "45 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "39 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "43 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 29",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 37 years. A is 9 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 9.\n(x + 9) + x = 37 => 2x + 9 = 37 => 2x = 28 => x = 14.\nA's age = 23 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "14 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23 years",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 30",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 70 years. A is 10 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 10.\n(x + 10) + x = 70 => 2x + 10 = 70 => 2x = 60 => x = 30.\nA's age = 40 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "42 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "38 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 31",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 53 years. A is 5 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 5.\n(x + 5) + x = 53 => 2x + 5 = 53 => 2x = 48 => x = 24.\nA's age = 29 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "31 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "27 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "29 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "24 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 32",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 77 years. A is 9 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 9.\n(x + 9) + x = 77 => 2x + 9 = 77 => 2x = 68 => x = 34.\nA's age = 43 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "45 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "34 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "43 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "41 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 33",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 78 years. A is 12 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 12.\n(x + 12) + x = 78 => 2x + 12 = 78 => 2x = 66 => x = 33.\nA's age = 45 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "47 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "43 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "45 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "33 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 34",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 40 years. A is 12 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 12.\n(x + 12) + x = 40 => 2x + 12 = 40 => 2x = 28 => x = 14.\nA's age = 26 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "24 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "28 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 35",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 58 years. A is 8 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 8.\n(x + 8) + x = 58 => 2x + 8 = 58 => 2x = 50 => x = 25.\nA's age = 33 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "33 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "35 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "31 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 36",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 65 years. A is 11 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 11.\n(x + 11) + x = 65 => 2x + 11 = 65 => 2x = 54 => x = 27.\nA's age = 38 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "38 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "40 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "27 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "36 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 37",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 50 years. A is 8 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 8.\n(x + 8) + x = 50 => 2x + 8 = 50 => 2x = 42 => x = 21.\nA's age = 29 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "27 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "29 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "31 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 38",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 43 years. A is 9 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 9.\n(x + 9) + x = 43 => 2x + 9 = 43 => 2x = 34 => x = 17.\nA's age = 26 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "28 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "24 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26 years",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 39",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 64 years. A is 4 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 4.\n(x + 4) + x = 64 => 2x + 4 = 64 => 2x = 60 => x = 30.\nA's age = 34 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "34 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "36 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 40",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 69 years. A is 7 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 7.\n(x + 7) + x = 69 => 2x + 7 = 69 => 2x = 62 => x = 31.\nA's age = 38 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "31 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "38 years",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 41",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 39 years. A is 9 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 9.\n(x + 9) + x = 39 => 2x + 9 = 39 => 2x = 30 => x = 15.\nA's age = 24 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "24 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "26 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 42",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 75 years. A is 5 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 5.\n(x + 5) + x = 75 => 2x + 5 = 75 => 2x = 70 => x = 35.\nA's age = 40 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "42 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "38 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 43",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 72 years. A is 6 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 6.\n(x + 6) + x = 72 => 2x + 6 = 72 => 2x = 66 => x = 33.\nA's age = 39 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "39 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "41 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "33 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "37 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 44",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 74 years. A is 10 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 10.\n(x + 10) + x = 74 => 2x + 10 = 74 => 2x = 64 => x = 32.\nA's age = 42 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "42 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "44 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "32 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 45",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 52 years. A is 4 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 4.\n(x + 4) + x = 52 => 2x + 4 = 52 => 2x = 48 => x = 24.\nA's age = 28 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "26 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "28 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "24 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 46",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 33 years. A is 7 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 7.\n(x + 7) + x = 33 => 2x + 7 = 33 => 2x = 26 => x = 13.\nA's age = 20 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "13 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "18 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 47",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 63 years. A is 9 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 9.\n(x + 9) + x = 63 => 2x + 9 = 63 => 2x = 54 => x = 27.\nA's age = 36 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "36 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "27 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "38 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 48",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 60 years. A is 8 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 8.\n(x + 8) + x = 60 => 2x + 8 = 60 => 2x = 52 => x = 26.\nA's age = 34 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "34 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "32 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "36 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 49",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 69 years. A is 11 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 11.\n(x + 11) + x = 69 => 2x + 11 = 69 => 2x = 58 => x = 29.\nA's age = 40 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "29 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "40 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "42 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "38 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Problems on Ages - Two Friends Age Sum 50",
        "difficulty": "Medium",
        "question_text": "The sum of present ages of A and B is 70 years. A is 6 years older than B. What is A's present age?",
        "sample_answer": "Let B's age be x. Then A's age = x + 6.\n(x + 6) + x = 70 => 2x + 6 = 70 => 2x = 64 => x = 32.\nA's age = 38 years.",
        "tips": "Form linear equation: (A + B = Sum) and (A - B = Difference).",
        "options": [
            {
                "label": "A",
                "text": "36 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "38 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "40 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Problems on Ages').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Problems on Ages').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='Problems on Ages',
                    title=q.get('title', 'Problems on Ages'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Problems on Ages via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Problems on Ages: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Problems on Ages',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'Problems on Ages',
                        q.get('title', 'Problems on Ages'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Problems on Ages into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
