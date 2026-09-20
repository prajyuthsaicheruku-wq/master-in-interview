"""
Seed script for Simplification (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Simplification - BODMAS Expression 1",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 14 + 3 \u00d7 4 \u2212 9",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 3 \u00d7 4 = 12\n2. Addition & Subtraction: 14 + 12 \u2212 9 = 17.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "19",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "22",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - BODMAS Expression 2",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 14 + 4 \u00d7 4 \u2212 2",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 4 \u00d7 4 = 16\n2. Addition & Subtraction: 14 + 16 \u2212 2 = 28.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "33",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - BODMAS Expression 3",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 15 + 4 \u00d7 5 \u2212 6",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 4 \u00d7 5 = 20\n2. Addition & Subtraction: 15 + 20 \u2212 6 = 29.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "34",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "31",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "29",
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
        "title": "Simplification - BODMAS Expression 4",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 27 + 6 \u00d7 5 \u2212 9",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 6 \u00d7 5 = 30\n2. Addition & Subtraction: 27 + 30 \u2212 9 = 48.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "53",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "46",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - BODMAS Expression 5",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 31 + 7 \u00d7 6 \u2212 3",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 7 \u00d7 6 = 42\n2. Addition & Subtraction: 31 + 42 \u2212 3 = 70.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "70",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "68",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "72",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "75",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - BODMAS Expression 6",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 16 + 2 \u00d7 5 \u2212 10",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 2 \u00d7 5 = 10\n2. Addition & Subtraction: 16 + 10 \u2212 10 = 16.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "18",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - BODMAS Expression 7",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 38 + 3 \u00d7 6 \u2212 10",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 3 \u00d7 6 = 18\n2. Addition & Subtraction: 38 + 18 \u2212 10 = 46.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "46",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "51",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "44",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - BODMAS Expression 8",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 27 + 7 \u00d7 2 \u2212 8",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 7 \u00d7 2 = 14\n2. Addition & Subtraction: 27 + 14 \u2212 8 = 33.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "38",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "33",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "31",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "35",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - BODMAS Expression 9",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 23 + 8 \u00d7 4 \u2212 9",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 8 \u00d7 4 = 32\n2. Addition & Subtraction: 23 + 32 \u2212 9 = 46.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "44",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "51",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "46",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - BODMAS Expression 10",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 36 + 6 \u00d7 5 \u2212 2",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 6 \u00d7 5 = 30\n2. Addition & Subtraction: 36 + 30 \u2212 2 = 64.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "69",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "64",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "66",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "62",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - BODMAS Expression 11",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 34 + 3 \u00d7 2 \u2212 8",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 3 \u00d7 2 = 6\n2. Addition & Subtraction: 34 + 6 \u2212 8 = 32.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "37",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - BODMAS Expression 12",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 27 + 3 \u00d7 5 \u2212 3",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 3 \u00d7 5 = 15\n2. Addition & Subtraction: 27 + 15 \u2212 3 = 39.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "44",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "37",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "41",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "39",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - BODMAS Expression 13",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 36 + 2 \u00d7 4 \u2212 10",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 2 \u00d7 4 = 8\n2. Addition & Subtraction: 36 + 8 \u2212 10 = 34.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "36",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "39",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "32",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - BODMAS Expression 14",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 31 + 2 \u00d7 4 \u2212 9",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 2 \u00d7 4 = 8\n2. Addition & Subtraction: 31 + 8 \u2212 9 = 30.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "32",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "35",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - BODMAS Expression 15",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 13 + 2 \u00d7 2 \u2212 6",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 2 \u00d7 2 = 4\n2. Addition & Subtraction: 13 + 4 \u2212 6 = 11.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "11",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "13",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "16",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - BODMAS Expression 16",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 26 + 5 \u00d7 4 \u2212 4",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 5 \u00d7 4 = 20\n2. Addition & Subtraction: 26 + 20 \u2212 4 = 42.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "44",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "47",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "42",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - BODMAS Expression 17",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 16 + 3 \u00d7 3 \u2212 7",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 3 \u00d7 3 = 9\n2. Addition & Subtraction: 16 + 9 \u2212 7 = 18.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "16",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "23",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - BODMAS Expression 18",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 24 + 2 \u00d7 2 \u2212 7",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 2 \u00d7 2 = 4\n2. Addition & Subtraction: 24 + 4 \u2212 7 = 21.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "23",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "19",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - BODMAS Expression 19",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 11 + 8 \u00d7 6 \u2212 3",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 8 \u00d7 6 = 48\n2. Addition & Subtraction: 11 + 48 \u2212 3 = 56.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "61",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "56",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "58",
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
        "title": "Simplification - BODMAS Expression 20",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 28 + 5 \u00d7 4 \u2212 9",
        "sample_answer": "According to BODMAS:\n1. Multiplication: 5 \u00d7 4 = 20\n2. Addition & Subtraction: 28 + 20 \u2212 9 = 39.",
        "tips": "BODMAS order: Brackets, Orders, Division/Multiplication, Addition/Subtraction.",
        "options": [
            {
                "label": "A",
                "text": "39",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "37",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "41",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "44",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Square Root of 144",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a144.",
        "sample_answer": "Since 12 \u00d7 12 = 144, \u221a144 = 12.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "11",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Square Root of 225",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a225.",
        "sample_answer": "Since 15 \u00d7 15 = 225, \u221a225 = 15.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "17",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Square Root of 324",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a324.",
        "sample_answer": "Since 18 \u00d7 18 = 324, \u221a324 = 18.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "18",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "19",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Square Root of 441",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a441.",
        "sample_answer": "Since 21 \u00d7 21 = 441, \u221a441 = 21.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "23",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - Square Root of 625",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a625.",
        "sample_answer": "Since 25 \u00d7 25 = 625, \u221a625 = 25.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "25",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "27",
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
        "title": "Simplification - Square Root of 196",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a196.",
        "sample_answer": "Since 14 \u00d7 14 = 196, \u221a196 = 14.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "13",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "16",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Square Root of 256",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a256.",
        "sample_answer": "Since 16 \u00d7 16 = 256, \u221a256 = 16.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "15",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "16",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - Square Root of 576",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a576.",
        "sample_answer": "Since 24 \u00d7 24 = 576, \u221a576 = 24.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "25",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "26",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - Square Root of 484",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a484.",
        "sample_answer": "Since 22 \u00d7 22 = 484, \u221a484 = 22.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "22",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "23",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "24",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Square Root of 900",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a900.",
        "sample_answer": "Since 30 \u00d7 30 = 900, \u221a900 = 30.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "32",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "31",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "29",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Square Root of 169",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a169.",
        "sample_answer": "Since 13 \u00d7 13 = 169, \u221a169 = 13.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "12",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - Square Root of 289",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a289.",
        "sample_answer": "Since 17 \u00d7 17 = 289, \u221a289 = 17.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "17",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "16",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "19",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Square Root of 361",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a361.",
        "sample_answer": "Since 19 \u00d7 19 = 361, \u221a361 = 19.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "19",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "21",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Square Root of 529",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a529.",
        "sample_answer": "Since 23 \u00d7 23 = 529, \u221a529 = 23.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "23",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "25",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - Square Root of 676",
        "difficulty": "Easy",
        "question_text": "Find the value of \u221a676.",
        "sample_answer": "Since 26 \u00d7 26 = 676, \u221a676 = 26.",
        "tips": "Recall common squares from 1 to 30.",
        "options": [
            {
                "label": "A",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "27",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 36",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 6/17 into decimal (rounded to 2 decimal places):",
        "sample_answer": "6 divided by 17 = 0.35.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.3",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.35",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "0.45",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.4",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 37",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 8/24 into decimal (rounded to 2 decimal places):",
        "sample_answer": "8 divided by 24 = 0.33.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.28",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.43",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.33",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "0.38",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 38",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 6/22 into decimal (rounded to 2 decimal places):",
        "sample_answer": "6 divided by 22 = 0.27.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.22",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.37",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.27",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "0.32",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 39",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 7/23 into decimal (rounded to 2 decimal places):",
        "sample_answer": "7 divided by 23 = 0.3.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.25",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.4",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.35",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.3",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 40",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 8/19 into decimal (rounded to 2 decimal places):",
        "sample_answer": "8 divided by 19 = 0.42.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.42",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "0.52",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.37",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.47",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 41",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 8/23 into decimal (rounded to 2 decimal places):",
        "sample_answer": "8 divided by 23 = 0.35.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.4",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.3",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.35",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "0.45",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 42",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 2/14 into decimal (rounded to 2 decimal places):",
        "sample_answer": "2 divided by 14 = 0.14.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.09",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.14",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "0.19",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 43",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 2/19 into decimal (rounded to 2 decimal places):",
        "sample_answer": "2 divided by 19 = 0.11.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.06",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.21",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.16",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.11",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 44",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 5/13 into decimal (rounded to 2 decimal places):",
        "sample_answer": "5 divided by 13 = 0.38.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.33",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.38",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "0.43",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.48",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 45",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 2/16 into decimal (rounded to 2 decimal places):",
        "sample_answer": "2 divided by 16 = 0.12.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.22",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.17",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.07",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.12",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 46",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 7/23 into decimal (rounded to 2 decimal places):",
        "sample_answer": "7 divided by 23 = 0.3.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.25",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.4",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.35",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.3",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 47",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 7/22 into decimal (rounded to 2 decimal places):",
        "sample_answer": "7 divided by 22 = 0.32.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.32",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "0.27",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.37",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.42",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 48",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 4/18 into decimal (rounded to 2 decimal places):",
        "sample_answer": "4 divided by 18 = 0.22.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.22",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "0.17",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.27",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.32",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 49",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 6/11 into decimal (rounded to 2 decimal places):",
        "sample_answer": "6 divided by 11 = 0.55.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.6",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.5",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.65",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0.55",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simplification - Fraction Decimal Equivalent 50",
        "difficulty": "Medium",
        "question_text": "Simplify the fraction 2/19 into decimal (rounded to 2 decimal places):",
        "sample_answer": "2 divided by 19 = 0.11.",
        "tips": "Perform direct decimal division.",
        "options": [
            {
                "label": "A",
                "text": "0.21",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0.16",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0.11",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "0.06",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Simplification').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Simplification').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='Simplification',
                    title=q.get('title', 'Simplification'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Simplification via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Simplification: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Simplification',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'Simplification',
                        q.get('title', 'Simplification'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Simplification into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
