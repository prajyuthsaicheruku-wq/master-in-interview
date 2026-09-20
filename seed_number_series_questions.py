"""
Seed script for Number Series (Logical Reasoning)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Number Series - AP Sequence 1",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 17, 24, 31, 38, 45, ?",
        "sample_answer": "Each term increases by a constant common difference of +7.\nNext term = 45 + 7 = 52.",
        "tips": "Identify the common difference (+7).",
        "options": [
            {
                "label": "A",
                "text": "51",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "52",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "59",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - AP Sequence 2",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 17, 23, 29, 35, 41, ?",
        "sample_answer": "Each term increases by a constant common difference of +6.\nNext term = 41 + 6 = 47.",
        "tips": "Identify the common difference (+6).",
        "options": [
            {
                "label": "A",
                "text": "46",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "53",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "49",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "47",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - AP Sequence 3",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 19, 24, 29, 34, 39, ?",
        "sample_answer": "Each term increases by a constant common difference of +5.\nNext term = 39 + 5 = 44.",
        "tips": "Identify the common difference (+5).",
        "options": [
            {
                "label": "A",
                "text": "44",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "43",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "49",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "46",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - AP Sequence 4",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 19, 26, 33, 40, 47, ?",
        "sample_answer": "Each term increases by a constant common difference of +7.\nNext term = 47 + 7 = 54.",
        "tips": "Identify the common difference (+7).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "61",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "53",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "56",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - AP Sequence 5",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 9, 12, 15, 18, 21, ?",
        "sample_answer": "Each term increases by a constant common difference of +3.\nNext term = 21 + 3 = 24.",
        "tips": "Identify the common difference (+3).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "27",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - AP Sequence 6",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 20, 26, 32, 38, 44, ?",
        "sample_answer": "Each term increases by a constant common difference of +6.\nNext term = 44 + 6 = 50.",
        "tips": "Identify the common difference (+6).",
        "options": [
            {
                "label": "A",
                "text": "49",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "56",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - AP Sequence 7",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 3, 7, 11, 15, 19, ?",
        "sample_answer": "Each term increases by a constant common difference of +4.\nNext term = 19 + 4 = 23.",
        "tips": "Identify the common difference (+4).",
        "options": [
            {
                "label": "A",
                "text": "25",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "23",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "27",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - AP Sequence 8",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 17, 24, 31, 38, 45, ?",
        "sample_answer": "Each term increases by a constant common difference of +7.\nNext term = 45 + 7 = 52.",
        "tips": "Identify the common difference (+7).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "59",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "51",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - AP Sequence 9",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 8, 11, 14, 17, 20, ?",
        "sample_answer": "Each term increases by a constant common difference of +3.\nNext term = 20 + 3 = 23.",
        "tips": "Identify the common difference (+3).",
        "options": [
            {
                "label": "A",
                "text": "22",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - AP Sequence 10",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 19, 24, 29, 34, 39, ?",
        "sample_answer": "Each term increases by a constant common difference of +5.\nNext term = 39 + 5 = 44.",
        "tips": "Identify the common difference (+5).",
        "options": [
            {
                "label": "A",
                "text": "44",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "49",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "43",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "46",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - AP Sequence 11",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 11, 19, 27, 35, 43, ?",
        "sample_answer": "Each term increases by a constant common difference of +8.\nNext term = 43 + 8 = 51.",
        "tips": "Identify the common difference (+8).",
        "options": [
            {
                "label": "A",
                "text": "50",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "51",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "59",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "53",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - AP Sequence 12",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 7, 11, 15, 19, 23, ?",
        "sample_answer": "Each term increases by a constant common difference of +4.\nNext term = 23 + 4 = 27.",
        "tips": "Identify the common difference (+4).",
        "options": [
            {
                "label": "A",
                "text": "29",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "27",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "31",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - AP Sequence 13",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 8, 13, 18, 23, 28, ?",
        "sample_answer": "Each term increases by a constant common difference of +5.\nNext term = 28 + 5 = 33.",
        "tips": "Identify the common difference (+5).",
        "options": [
            {
                "label": "A",
                "text": "38",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "35",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "33",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - AP Sequence 14",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 20, 23, 26, 29, 32, ?",
        "sample_answer": "Each term increases by a constant common difference of +3.\nNext term = 32 + 3 = 35.",
        "tips": "Identify the common difference (+3).",
        "options": [
            {
                "label": "A",
                "text": "35",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "38",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "37",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - AP Sequence 15",
        "difficulty": "Easy",
        "question_text": "Find the next number in the series: 18, 26, 34, 42, 50, ?",
        "sample_answer": "Each term increases by a constant common difference of +8.\nNext term = 50 + 8 = 58.",
        "tips": "Identify the common difference (+8).",
        "options": [
            {
                "label": "A",
                "text": "60",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "58",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "57",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "66",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - Square Pattern 16",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "48",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Square Pattern 17",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "48",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Square Pattern 18",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Square Pattern 19",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "54",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Square Pattern 20",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Square Pattern 21",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "52",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Square Pattern 22",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "54",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - Square Pattern 23",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "52",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Square Pattern 24",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "52",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Square Pattern 25",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "52",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Square Pattern 26",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Square Pattern 27",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "54",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Square Pattern 28",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Square Pattern 29",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "54",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Square Pattern 30",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Square Pattern 31",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "48",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Square Pattern 32",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Square Pattern 33",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "52",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - Square Pattern 34",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "54",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Square Pattern 35",
        "difficulty": "Medium",
        "question_text": "Identify the missing number in the sequence: 5, 10, 17, 26, 37, ?",
        "sample_answer": "Pattern follows n\u00b2 + 1:\n2\u00b2 + 1 = 5, 3\u00b2 + 1 = 10, 4\u00b2 + 1 = 17, 5\u00b2 + 1 = 26, 6\u00b2 + 1 = 37.\nNext term = 7\u00b2 + 1 = 49 + 1 = 50.",
        "tips": "Check for square or cube relations (n^2 + 1).",
        "options": [
            {
                "label": "A",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "48",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Multiplicative Addition 36",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "127",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Multiplicative Addition 37",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "127",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Multiplicative Addition 38",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "132",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Multiplicative Addition 39",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "132",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - Multiplicative Addition 40",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "132",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Multiplicative Addition 41",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "125",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Multiplicative Addition 42",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "125",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number Series - Multiplicative Addition 43",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "132",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Multiplicative Addition 44",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "132",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Multiplicative Addition 45",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "125",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Multiplicative Addition 46",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "127",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number Series - Multiplicative Addition 47",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "129",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Multiplicative Addition 48",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "129",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number Series - Multiplicative Addition 49",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "132",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "125",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number Series - Multiplicative Addition 50",
        "difficulty": "Medium",
        "question_text": "Find the next term in the sequence: 3, 7, 15, 31, 63, ?",
        "sample_answer": "Pattern: Each term is multiplied by 2 and then added 1: (term \u00d7 2) + 1.\nNext term = (63 \u00d7 2) + 1 = 127.",
        "tips": "Notice how numbers nearly double each step.",
        "options": [
            {
                "label": "A",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "129",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "127",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "132",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Number Series').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Number Series').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Logical Reasoning',
                    topic='Number Series',
                    title=q.get('title', 'Number Series'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Number Series via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Number Series: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Number Series',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Logical Reasoning', 'Number Series',
                        q.get('title', 'Number Series'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Number Series into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
