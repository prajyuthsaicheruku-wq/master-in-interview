"""
Seed script for HCF & LCM (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "HCF & LCM - HCF of 12 and 18",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 12 and 18.",
        "sample_answer": "Factors of 12 and 18 yield greatest common divisor = 6.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5",
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
        "title": "HCF & LCM - LCM of 15 and 25",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 15 and 25.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (15 \u00d7 25) / 5 = 75.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "90",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "75",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "37",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - HCF of 24 and 36",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 24 and 36.",
        "sample_answer": "Factors of 24 and 36 yield greatest common divisor = 12.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "15",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - LCM of 30 and 45",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 30 and 45.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (30 \u00d7 45) / 15 = 90.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "45",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "120",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "90",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - HCF of 14 and 21",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 14 and 21.",
        "sample_answer": "Factors of 14 and 21 yield greatest common divisor = 7.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "7",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "6",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - LCM of 16 and 24",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 16 and 24.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (16 \u00d7 24) / 8 = 48.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "64",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - HCF of 20 and 30",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 20 and 30.",
        "sample_answer": "Factors of 20 and 30 yield greatest common divisor = 10.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "10",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "13",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20",
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
        "title": "HCF & LCM - LCM of 35 and 49",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 35 and 49.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (35 \u00d7 49) / 7 = 245.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "280",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "122",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "196",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "245",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - HCF of 28 and 42",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 28 and 42.",
        "sample_answer": "Factors of 28 and 42 yield greatest common divisor = 14.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14",
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
        "title": "HCF & LCM - LCM of 40 and 60",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 40 and 60.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (40 \u00d7 60) / 20 = 120.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "120",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "160",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "60",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - HCF of 18 and 27",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 18 and 27.",
        "sample_answer": "Factors of 18 and 27 yield greatest common divisor = 9.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "18",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12",
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
        "title": "HCF & LCM - LCM of 22 and 33",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 22 and 33.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (22 \u00d7 33) / 11 = 66.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "33",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "88",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "66",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - HCF of 25 and 35",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 25 and 35.",
        "sample_answer": "Factors of 25 and 35 yield greatest common divisor = 5.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "4",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5",
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
        "title": "HCF & LCM - LCM of 32 and 48",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 32 and 48.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (32 \u00d7 48) / 16 = 96.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "96",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "128",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - HCF of 36 and 54",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 36 and 54.",
        "sample_answer": "Factors of 36 and 54 yield greatest common divisor = 18.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "18",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "21",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "36",
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
        "title": "HCF & LCM - LCM of 45 and 75",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 45 and 75.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (45 \u00d7 75) / 15 = 225.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "270",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "112",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "150",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "225",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - HCF of 50 and 75",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 50 and 75.",
        "sample_answer": "Factors of 50 and 75 yield greatest common divisor = 25.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
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
                "text": "50",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - LCM of 48 and 72",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 48 and 72.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (48 \u00d7 72) / 24 = 144.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "192",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "72",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "144",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - HCF of 60 and 90",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 60 and 90.",
        "sample_answer": "Factors of 60 and 90 yield greatest common divisor = 30.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "33",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "29",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - LCM of 64 and 96",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 64 and 96.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (64 \u00d7 96) / 32 = 192.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "96",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "256",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "192",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - HCF of 54 and 81",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 54 and 81.",
        "sample_answer": "Factors of 54 and 81 yield greatest common divisor = 27.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "27",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
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
        "title": "HCF & LCM - LCM of 56 and 84",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 56 and 84.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (56 \u00d7 84) / 28 = 168.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "224",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "168",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "84",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - HCF of 63 and 84",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 63 and 84.",
        "sample_answer": "Factors of 63 and 84 yield greatest common divisor = 21.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "42",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "20",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - LCM of 70 and 105",
        "difficulty": "Easy",
        "question_text": "Find the Least Common Multiple (LCM) of 70 and 105.",
        "sample_answer": "LCM = (a \u00d7 b) / HCF = (70 \u00d7 105) / 35 = 210.",
        "tips": "LCM(a, b) = (a * b) / GCD(a, b).",
        "options": [
            {
                "label": "A",
                "text": "280",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "210",
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
        "title": "HCF & LCM - HCF of 72 and 108",
        "difficulty": "Easy",
        "question_text": "Find the Highest Common Factor (HCF / GCD) of 72 and 108.",
        "sample_answer": "Factors of 72 and 108 yield greatest common divisor = 36.",
        "tips": "Use Euclidean division algorithm or prime factorization.",
        "options": [
            {
                "label": "A",
                "text": "39",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "72",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "36",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 26",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 15 and 150 respectively. If one of the numbers is 30, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (15 \u00d7 150) / 30 = 75.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "60",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "90",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "77",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "75",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 27",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 15 and 105 respectively. If one of the numbers is 30, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (15 \u00d7 105) / 30 = 52.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "52",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "54",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "67",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "37",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 28",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 15 and 105 respectively. If one of the numbers is 30, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (15 \u00d7 105) / 30 = 52.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "37",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "52",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "67",
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
        "title": "HCF & LCM - Missing Number Relation 29",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 15 and 75 respectively. If one of the numbers is 30, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (15 \u00d7 75) / 30 = 37.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "37",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "22",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "52",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "39",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 30",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 12 and 72 respectively. If one of the numbers is 24, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (12 \u00d7 72) / 24 = 36.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "38",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "36",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "24",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 31",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 4 and 28 respectively. If one of the numbers is 8, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (4 \u00d7 28) / 8 = 14.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "16",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 32",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 4 and 32 respectively. If one of the numbers is 8, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (4 \u00d7 32) / 8 = 16.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "12",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "18",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20",
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
        "title": "HCF & LCM - Missing Number Relation 33",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 6 and 36 respectively. If one of the numbers is 12, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (6 \u00d7 36) / 12 = 18.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "18",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 34",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 6 and 48 respectively. If one of the numbers is 12, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (6 \u00d7 48) / 12 = 24.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "18",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - Missing Number Relation 35",
        "difficulty": "Medium",
        "question_text": "The HCF and LCM of two numbers are 15 and 120 respectively. If one of the numbers is 30, find the other number.",
        "sample_answer": "We know: Product of two numbers = HCF \u00d7 LCM.\nTherefore, other number = (HCF \u00d7 LCM) / a = (15 \u00d7 120) / 30 = 60.",
        "tips": "HCF * LCM = First Number * Second Number.",
        "options": [
            {
                "label": "A",
                "text": "62",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "75",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "45",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "60",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 36",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 3, 4, and 6 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(3, 4, 6) = 12 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "24 seconds",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22 seconds",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6 seconds",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 seconds",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 37",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 4, 6, and 8 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(4, 6, 8) = 24 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "24 seconds",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "12 seconds",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34 seconds",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "48 seconds",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 38",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 6, 8, and 12 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(6, 8, 12) = 24 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "24 seconds",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "12 seconds",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48 seconds",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34 seconds",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 39",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 5, 10, and 15 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(5, 10, 15) = 30 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "60 seconds",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 seconds",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30 seconds",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "40 seconds",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 40",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 8, 12, and 16 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(8, 12, 16) = 48 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "24 seconds",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "96 seconds",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "58 seconds",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "48 seconds",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 41",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 10, 15, and 20 minutes respectively. If they toll together now, after how many minutes will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(10, 15, 20) = 60 minutes.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "30 minutes",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 minutes",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "120 minutes",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "70 minutes",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 42",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 12, 15, and 18 minutes respectively. If they toll together now, after how many minutes will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(12, 15, 18) = 180 minutes.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "360 minutes",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "90 minutes",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "190 minutes",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "180 minutes",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 43",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 9, 12, and 15 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(9, 12, 15) = 180 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "190 seconds",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "180 seconds",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "90 seconds",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "360 seconds",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 44",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 15, 20, and 30 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(15, 20, 30) = 60 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "30 seconds",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 seconds",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "120 seconds",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "70 seconds",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "HCF & LCM - Simultaneous Bells Toll Problem 45",
        "difficulty": "Medium",
        "question_text": "Three bells toll at intervals of 12, 16, and 24 seconds respectively. If they toll together now, after how many seconds will they toll together next?",
        "sample_answer": "The bells toll together at intervals equal to the LCM of their individual intervals.\nLCM(12, 16, 24) = 48 seconds.",
        "tips": "Simultaneous tolling/blinking interval = LCM of intervals.",
        "options": [
            {
                "label": "A",
                "text": "24 seconds",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "96 seconds",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48 seconds",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "58 seconds",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "HCF & LCM - Advanced Application 46",
        "difficulty": "Medium",
        "question_text": "What is the greatest number that divides 43, 91 and 183 so as to leave the same remainder in each case?",
        "sample_answer": "Solution: The answer is 4.",
        "tips": "HCF of fractions = HCF(numerators)/LCM(denominators).",
        "options": [
            {
                "label": "A",
                "text": "6",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Advanced Application 47",
        "difficulty": "Medium",
        "question_text": "Find the greatest number that will divide 148 and 246 leaving a remainder of 4 and 6 respectively.",
        "sample_answer": "Solution: The answer is 12.",
        "tips": "HCF of fractions = HCF(numerators)/LCM(denominators).",
        "options": [
            {
                "label": "A",
                "text": "18",
                "is_correct": false
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
                "text": "12",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Advanced Application 48",
        "difficulty": "Medium",
        "question_text": "What is the greatest number which divides 64 and 82 leaving remainders of 4 and 2 respectively?",
        "sample_answer": "Solution: The answer is 10.",
        "tips": "HCF of fractions = HCF(numerators)/LCM(denominators).",
        "options": [
            {
                "label": "A",
                "text": "8",
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
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Advanced Application 49",
        "difficulty": "Medium",
        "question_text": "Find the HCF of fractions 2/3, 8/9, 16/81, and 10/27.",
        "sample_answer": "Solution: The answer is 2/81.",
        "tips": "HCF of fractions = HCF(numerators)/LCM(denominators).",
        "options": [
            {
                "label": "A",
                "text": "80/3",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "80/81",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "2/9",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "2/81",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "HCF & LCM - Advanced Application 50",
        "difficulty": "Medium",
        "question_text": "Find the LCM of fractions 1/3, 5/6, 2/9, and 4/27.",
        "sample_answer": "Solution: The answer is 20/3.",
        "tips": "HCF of fractions = HCF(numerators)/LCM(denominators).",
        "options": [
            {
                "label": "A",
                "text": "10/3",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "1/27",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20/27",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20/3",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='HCF & LCM').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='HCF & LCM').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='HCF & LCM',
                    title=q.get('title', 'HCF & LCM'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for HCF & LCM via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for HCF & LCM: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('HCF & LCM',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'HCF & LCM',
                        q.get('title', 'HCF & LCM'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for HCF & LCM into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
