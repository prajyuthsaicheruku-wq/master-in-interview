"""
Seed script for Number System (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Number System - Unit Digit of 2^33",
        "difficulty": "Easy",
        "question_text": "Find the unit digit of 2^33.",
        "sample_answer": "The cyclicity of 2 is 4. Power 33 mod 4 = 1. Therefore, the unit digit is 2.",
        "tips": "Remember the unit digit cycle for base 2.",
        "options": [
            {
                "label": "A",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "3",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Unit Digit of 3^45",
        "difficulty": "Easy",
        "question_text": "Find the unit digit of 3^45.",
        "sample_answer": "The cyclicity of 3 is 4. Power 45 mod 4 = 1. Therefore, the unit digit is 3.",
        "tips": "Remember the unit digit cycle for base 3.",
        "options": [
            {
                "label": "A",
                "text": "3",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Unit Digit of 4^62",
        "difficulty": "Easy",
        "question_text": "Find the unit digit of 4^62.",
        "sample_answer": "The cyclicity of 4 is 2. Power 62 mod 2 = 0. Therefore, the unit digit is 6.",
        "tips": "Remember the unit digit cycle for base 4.",
        "options": [
            {
                "label": "A",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Unit Digit of 7^54",
        "difficulty": "Easy",
        "question_text": "Find the unit digit of 7^54.",
        "sample_answer": "The cyclicity of 7 is 4. Power 54 mod 4 = 2. Therefore, the unit digit is 9.",
        "tips": "Remember the unit digit cycle for base 7.",
        "options": [
            {
                "label": "A",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "1",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Unit Digit of 8^73",
        "difficulty": "Easy",
        "question_text": "Find the unit digit of 8^73.",
        "sample_answer": "The cyclicity of 8 is 4. Power 73 mod 4 = 1. Therefore, the unit digit is 8.",
        "tips": "Remember the unit digit cycle for base 8.",
        "options": [
            {
                "label": "A",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "0",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Unit Digit of 9^81",
        "difficulty": "Medium",
        "question_text": "Find the unit digit of 9^81.",
        "sample_answer": "The cyclicity of 9 is 2. Power 81 mod 2 = 1. Therefore, the unit digit is 9.",
        "tips": "Remember the unit digit cycle for base 9.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Unit Digit of 2^55",
        "difficulty": "Medium",
        "question_text": "Find the unit digit of 2^55.",
        "sample_answer": "The cyclicity of 2 is 4. Power 55 mod 4 = 3. Therefore, the unit digit is 8.",
        "tips": "Remember the unit digit cycle for base 2.",
        "options": [
            {
                "label": "A",
                "text": "8",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Unit Digit of 3^71",
        "difficulty": "Medium",
        "question_text": "Find the unit digit of 3^71.",
        "sample_answer": "The cyclicity of 3 is 4. Power 71 mod 4 = 3. Therefore, the unit digit is 7.",
        "tips": "Remember the unit digit cycle for base 3.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Unit Digit of 7^65",
        "difficulty": "Medium",
        "question_text": "Find the unit digit of 7^65.",
        "sample_answer": "The cyclicity of 7 is 4. Power 65 mod 4 = 1. Therefore, the unit digit is 7.",
        "tips": "Remember the unit digit cycle for base 7.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "9",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Unit Digit of 8^46",
        "difficulty": "Medium",
        "question_text": "Find the unit digit of 8^46.",
        "sample_answer": "The cyclicity of 8 is 4. Power 46 mod 4 = 2. Therefore, the unit digit is 4.",
        "tips": "Remember the unit digit cycle for base 8.",
        "options": [
            {
                "label": "A",
                "text": "4",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "6",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Sum of First 15 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 15 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 15 \u00d7 16 / 2 = 120.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "125",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "135",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "120",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "105",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Sum of First 16 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 16 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 16 \u00d7 17 / 2 = 136.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "141",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "120",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "136",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "152",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Sum of First 17 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 17 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 17 \u00d7 18 / 2 = 153.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "153",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "158",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "170",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "136",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Sum of First 18 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 18 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 18 \u00d7 19 / 2 = 171.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "189",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "171",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "176",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "153",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Sum of First 19 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 19 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 19 \u00d7 20 / 2 = 190.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "171",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "195",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "209",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "190",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Sum of First 20 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 20 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 20 \u00d7 21 / 2 = 210.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "230",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "210",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "215",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "190",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Sum of First 21 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 21 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 21 \u00d7 22 / 2 = 231.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "236",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "252",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "210",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "231",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Sum of First 22 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 22 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 22 \u00d7 23 / 2 = 253.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "253",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "231",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "258",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "275",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Sum of First 23 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 23 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 23 \u00d7 24 / 2 = 276.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "281",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "276",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "299",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "253",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Sum of First 24 Natural Numbers",
        "difficulty": "Easy",
        "question_text": "What is the sum of the first 24 positive integers?",
        "sample_answer": "Sum = n(n + 1) / 2 = 24 \u00d7 25 / 2 = 300.",
        "tips": "Use formula S = n(n+1)/2.",
        "options": [
            {
                "label": "A",
                "text": "276",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "324",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "300",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "305",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Remainder of 125 divided by 9",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 125 is divided by 9.",
        "sample_answer": "125 = 9 \u00d7 13 + 8. Hence the remainder is 8.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Remainder of 247 divided by 8",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 247 is divided by 8.",
        "sample_answer": "247 = 8 \u00d7 30 + 7. Hence the remainder is 7.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Remainder of 358 divided by 11",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 358 is divided by 11.",
        "sample_answer": "358 = 11 \u00d7 32 + 6. Hence the remainder is 6.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "6",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Remainder of 512 divided by 7",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 512 is divided by 7.",
        "sample_answer": "512 = 7 \u00d7 73 + 1. Hence the remainder is 1.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Remainder of 629 divided by 13",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 629 is divided by 13.",
        "sample_answer": "629 = 13 \u00d7 48 + 5. Hence the remainder is 5.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Remainder of 487 divided by 6",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 487 is divided by 6.",
        "sample_answer": "487 = 6 \u00d7 81 + 1. Hence the remainder is 1.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Remainder of 715 divided by 12",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 715 is divided by 12.",
        "sample_answer": "715 = 12 \u00d7 59 + 7. Hence the remainder is 7.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "10",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "8",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Remainder of 833 divided by 5",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 833 is divided by 5.",
        "sample_answer": "833 = 5 \u00d7 166 + 3. Hence the remainder is 3.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Remainder of 941 divided by 4",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 941 is divided by 4.",
        "sample_answer": "941 = 4 \u00d7 235 + 1. Hence the remainder is 1.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "1",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Remainder of 1050 divided by 11",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 1050 is divided by 11.",
        "sample_answer": "1050 = 11 \u00d7 95 + 5. Hence the remainder is 5.",
        "tips": "Divide directly or use divisibility checks.",
        "options": [
            {
                "label": "A",
                "text": "5",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Total Factors of 36",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 36 have?",
        "sample_answer": "By prime factorizing 36, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 9.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9",
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
        "title": "Number System - Total Factors of 48",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 48 have?",
        "sample_answer": "By prime factorizing 48, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 10.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "10",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "12",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Total Factors of 60",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 60 have?",
        "sample_answer": "By prime factorizing 60, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 12.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "16",
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
                "text": "10",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Total Factors of 72",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 72 have?",
        "sample_answer": "By prime factorizing 72, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 12.",
        "tips": "Prime factorize and multiply (power + 1).",
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
                "text": "12",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "10",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Total Factors of 84",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 84 have?",
        "sample_answer": "By prime factorizing 84, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 12.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "12",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Total Factors of 90",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 90 have?",
        "sample_answer": "By prime factorizing 90, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 12.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "12",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "16",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Number System - Total Factors of 100",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 100 have?",
        "sample_answer": "By prime factorizing 100, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 9.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "13",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Total Factors of 120",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 120 have?",
        "sample_answer": "By prime factorizing 120, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 16.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "14",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "18",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Total Factors of 144",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 144 have?",
        "sample_answer": "By prime factorizing 144, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 15.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "17",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "19",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15",
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
        "title": "Number System - Total Factors of 180",
        "difficulty": "Medium",
        "question_text": "How many positive factors (divisors) does the number 180 have?",
        "sample_answer": "By prime factorizing 180, express as p1^a * p2^b. The total number of factors is (a+1)(b+1)... = 18.",
        "tips": "Prime factorize and multiply (power + 1).",
        "options": [
            {
                "label": "A",
                "text": "16",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22",
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
        "title": "Number System - Arithmetic Concept 41",
        "difficulty": "Easy",
        "question_text": "The place value of 7 in 85,742 is:",
        "sample_answer": "Direct computation: The result is 700.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "7000",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "70",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "700",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Arithmetic Concept 42",
        "difficulty": "Easy",
        "question_text": "The face value of 9 in 49,382 is:",
        "sample_answer": "Direct computation: The result is 9.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "9000",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "900",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "90",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Arithmetic Concept 43",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is prime?",
        "sample_answer": "Direct computation: The result is 47.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "57",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "51",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "63",
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
        "title": "Number System - Arithmetic Concept 44",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is a composite number?",
        "sample_answer": "Direct computation: The result is 91.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "73",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "71",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "91",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "79",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Arithmetic Concept 45",
        "difficulty": "Easy",
        "question_text": "The difference between place value and face value of 6 in 6,852 is:",
        "sample_answer": "Direct computation: The result is 5994.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "5990",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5994",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "6000",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Arithmetic Concept 46",
        "difficulty": "Medium",
        "question_text": "How many two-digit prime numbers end with the digit 3?",
        "sample_answer": "Direct computation: The result is 7.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Number System - Arithmetic Concept 47",
        "difficulty": "Medium",
        "question_text": "The smallest 3-digit prime number is:",
        "sample_answer": "Direct computation: The result is 101.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "109",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "103",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "101",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "107",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Arithmetic Concept 48",
        "difficulty": "Medium",
        "question_text": "The largest 2-digit prime number is:",
        "sample_answer": "Direct computation: The result is 97.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "91",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "97",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "93",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "99",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Number System - Arithmetic Concept 49",
        "difficulty": "Medium",
        "question_text": "What is the sum of all prime numbers less than 10?",
        "sample_answer": "Direct computation: The result is 17.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "18",
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
                "text": "21",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Number System - Arithmetic Concept 50",
        "difficulty": "Medium",
        "question_text": "If a number is multiplied by 3 and then increased by 12 gives 45, what is the number?",
        "sample_answer": "Direct computation: The result is 11.",
        "tips": "Apply basic definition of prime numbers, place/face values.",
        "options": [
            {
                "label": "A",
                "text": "12",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Number System').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Number System').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='Number System',
                    title=q.get('title', 'Number System'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Number System via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Number System: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Number System',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'Number System',
                        q.get('title', 'Number System'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Number System into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
