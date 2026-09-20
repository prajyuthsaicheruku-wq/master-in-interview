"""
Seed script for Divisibility (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 9 (#1)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 8820* so that the resulting number is completely divisible by 9?",
        "sample_answer": "For divisibility by 9, the required digit test yields * = 0.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 9 (#2)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 8497* so that the resulting number is completely divisible by 9?",
        "sample_answer": "For divisibility by 9, the required digit test yields * = 8.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 9 (#3)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 7293* so that the resulting number is completely divisible by 9?",
        "sample_answer": "For divisibility by 9, the required digit test yields * = 6.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
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
                "text": "6",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "7",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 11 (#4)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 1188* so that the resulting number is completely divisible by 11?",
        "sample_answer": "For divisibility by 11, the required digit test yields * = 0.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 9 (#5)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 8368* so that the resulting number is completely divisible by 9?",
        "sample_answer": "For divisibility by 9, the required digit test yields * = 2.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 9 (#6)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 3231* so that the resulting number is completely divisible by 9?",
        "sample_answer": "For divisibility by 9, the required digit test yields * = 0.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 3 (#7)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 6764* so that the resulting number is completely divisible by 3?",
        "sample_answer": "For divisibility by 3, the required digit test yields * = 1.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 9 (#8)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 1166* so that the resulting number is completely divisible by 9?",
        "sample_answer": "For divisibility by 9, the required digit test yields * = 4.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
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
                "text": "7",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 11 (#9)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 8096* so that the resulting number is completely divisible by 11?",
        "sample_answer": "For divisibility by 11, the required digit test yields * = 0.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "1",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "0",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 11 (#10)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 5788* so that the resulting number is completely divisible by 11?",
        "sample_answer": "For divisibility by 11, the required digit test yields * = 2.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 3 (#11)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 7545* so that the resulting number is completely divisible by 3?",
        "sample_answer": "For divisibility by 3, the required digit test yields * = 0.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "0",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "3",
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
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 3 (#12)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 5372* so that the resulting number is completely divisible by 3?",
        "sample_answer": "For divisibility by 3, the required digit test yields * = 1.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
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
                "text": "1",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "4",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Smallest Digit for Divisibility by 3 (#13)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 3335* so that the resulting number is completely divisible by 3?",
        "sample_answer": "For divisibility by 3, the required digit test yields * = 1.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "2",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1",
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
        "title": "Divisibility - Smallest Digit for Divisibility by 11 (#14)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 2680* so that the resulting number is completely divisible by 11?",
        "sample_answer": "For divisibility by 11, the required digit test yields * = 7.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
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
        "title": "Divisibility - Smallest Digit for Divisibility by 3 (#15)",
        "difficulty": "Easy",
        "question_text": "What smallest single-digit number must replace * in 4042* so that the resulting number is completely divisible by 3?",
        "sample_answer": "For divisibility by 3, the required digit test yields * = 2.",
        "tips": "Sum of digits rule for 3 and 9; alternate digit sum difference for 11.",
        "options": [
            {
                "label": "A",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Divisible by 6 (#16)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 6?",
        "sample_answer": "A number is divisible by 6 if it is divisible by both 2 and 3.\nAmong the choices, 900 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 2 and 3.",
        "options": [
            {
                "label": "A",
                "text": "902",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "900",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "901",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "905",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Divisible by 12 (#17)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 12?",
        "sample_answer": "A number is divisible by 12 if it is divisible by both 3 and 4.\nAmong the choices, 864 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 3 and 4.",
        "options": [
            {
                "label": "A",
                "text": "866",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "864",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "865",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "869",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Divisible by 15 (#18)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 15?",
        "sample_answer": "A number is divisible by 15 if it is divisible by both 3 and 5.\nAmong the choices, 1500 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 3 and 5.",
        "options": [
            {
                "label": "A",
                "text": "1501",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1500",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "1505",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1502",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Divisible by 18 (#19)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 18?",
        "sample_answer": "A number is divisible by 18 if it is divisible by both 2 and 9.\nAmong the choices, 1854 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 2 and 9.",
        "options": [
            {
                "label": "A",
                "text": "1854",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "1856",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1859",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1855",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Divisible by 72 (#20)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 72?",
        "sample_answer": "A number is divisible by 72 if it is divisible by both 8 and 9.\nAmong the choices, 10152 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 8 and 9.",
        "options": [
            {
                "label": "A",
                "text": "10154",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10153",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10152",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "10157",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Divisible by 6 (#21)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 6?",
        "sample_answer": "A number is divisible by 6 if it is divisible by both 2 and 3.\nAmong the choices, 426 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 2 and 3.",
        "options": [
            {
                "label": "A",
                "text": "428",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "426",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "427",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "431",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Divisible by 12 (#22)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 12?",
        "sample_answer": "A number is divisible by 12 if it is divisible by both 3 and 4.\nAmong the choices, 1632 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 3 and 4.",
        "options": [
            {
                "label": "A",
                "text": "1632",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "1637",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1634",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1633",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Divisible by 15 (#23)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 15?",
        "sample_answer": "A number is divisible by 15 if it is divisible by both 3 and 5.\nAmong the choices, 2520 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 3 and 5.",
        "options": [
            {
                "label": "A",
                "text": "2521",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2525",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2522",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2520",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Divisible by 18 (#24)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 18?",
        "sample_answer": "A number is divisible by 18 if it is divisible by both 2 and 9.\nAmong the choices, 2160 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 2 and 9.",
        "options": [
            {
                "label": "A",
                "text": "2165",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2162",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2161",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2160",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Divisible by 72 (#25)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 72?",
        "sample_answer": "A number is divisible by 72 if it is divisible by both 8 and 9.\nAmong the choices, 8352 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 8 and 9.",
        "options": [
            {
                "label": "A",
                "text": "8353",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8354",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8357",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8352",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Divisible by 6 (#26)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 6?",
        "sample_answer": "A number is divisible by 6 if it is divisible by both 2 and 3.\nAmong the choices, 588 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 2 and 3.",
        "options": [
            {
                "label": "A",
                "text": "593",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "590",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "589",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "588",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Divisible by 12 (#27)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 12?",
        "sample_answer": "A number is divisible by 12 if it is divisible by both 3 and 4.\nAmong the choices, 612 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 3 and 4.",
        "options": [
            {
                "label": "A",
                "text": "613",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "617",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "614",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "612",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Divisible by 15 (#28)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 15?",
        "sample_answer": "A number is divisible by 15 if it is divisible by both 3 and 5.\nAmong the choices, 2370 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 3 and 5.",
        "options": [
            {
                "label": "A",
                "text": "2370",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "2372",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2375",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2371",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Divisible by 18 (#29)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 18?",
        "sample_answer": "A number is divisible by 18 if it is divisible by both 2 and 9.\nAmong the choices, 1944 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 2 and 9.",
        "options": [
            {
                "label": "A",
                "text": "1946",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1945",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1949",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1944",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Divisible by 72 (#30)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is divisible by 72?",
        "sample_answer": "A number is divisible by 72 if it is divisible by both 8 and 9.\nAmong the choices, 13104 satisfies both conditions.",
        "tips": "Check divisibility by co-prime factors 8 and 9.",
        "options": [
            {
                "label": "A",
                "text": "13106",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13105",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13109",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13104",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Direct Test of 25 (#31)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 25?",
        "sample_answer": "Rule for 25: Check the last digits. The number 6150 is exactly divisible by 25.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "6153",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6151",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6150",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "6152",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#32)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 3000 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "3000",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "3003",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3001",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3002",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#33)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 2576 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "2578",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2576",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "2577",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2579",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Direct Test of 25 (#34)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 25?",
        "sample_answer": "Rule for 25: Check the last digits. The number 8200 is exactly divisible by 25.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "8200",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "8203",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8201",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8202",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#35)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 2984 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "2985",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "2984",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "2986",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2987",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Direct Test of 4 (#36)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 4?",
        "sample_answer": "Rule for 4: Check the last digits. The number 1040 is exactly divisible by 4.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "1043",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1040",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "1042",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1041",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Direct Test of 25 (#37)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 25?",
        "sample_answer": "Rule for 25: Check the last digits. The number 6850 is exactly divisible by 25.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "6853",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6851",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6852",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6850",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Direct Test of 25 (#38)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 25?",
        "sample_answer": "Rule for 25: Check the last digits. The number 3875 is exactly divisible by 25.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "3877",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3878",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3876",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3875",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Direct Test of 4 (#39)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 4?",
        "sample_answer": "Rule for 4: Check the last digits. The number 644 is exactly divisible by 4.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "647",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "645",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "644",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "646",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#40)",
        "difficulty": "Easy",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 3544 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "3544",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "3545",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3547",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3546",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Direct Test of 4 (#41)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 4?",
        "sample_answer": "Rule for 4: Check the last digits. The number 1764 is exactly divisible by 4.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "1766",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1764",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "1767",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1765",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Direct Test of 25 (#42)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 25?",
        "sample_answer": "Rule for 25: Check the last digits. The number 5075 is exactly divisible by 25.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "5077",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5075",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "5078",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5076",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#43)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 1960 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "1963",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1960",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "1961",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1962",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Direct Test of 25 (#44)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 25?",
        "sample_answer": "Rule for 25: Check the last digits. The number 10175 is exactly divisible by 25.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "10175",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "10178",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10176",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10177",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#45)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 1656 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "1656",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "1659",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1658",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1657",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#46)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 3264 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "3266",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3264",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "3267",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3265",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#47)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 1432 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "1433",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1435",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1434",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1432",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Direct Test of 25 (#48)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 25?",
        "sample_answer": "Rule for 25: Check the last digits. The number 5200 is exactly divisible by 25.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "5202",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5203",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5201",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5200",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#49)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 1840 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "1842",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1843",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1841",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "1840",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Divisibility - Direct Test of 8 (#50)",
        "difficulty": "Medium",
        "question_text": "Which of the following numbers is completely divisible by 8?",
        "sample_answer": "Rule for 8: Check the last digits. The number 3168 is exactly divisible by 8.",
        "tips": "For 4: last 2 digits; for 8: last 3 digits; for 25: ends in 00, 25, 50, 75.",
        "options": [
            {
                "label": "A",
                "text": "3170",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3171",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3169",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3168",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Divisibility').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Divisibility').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='Divisibility',
                    title=q.get('title', 'Divisibility'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Divisibility via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Divisibility: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Divisibility',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'Divisibility',
                        q.get('title', 'Divisibility'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Divisibility into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
