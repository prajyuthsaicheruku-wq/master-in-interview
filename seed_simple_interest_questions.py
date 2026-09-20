"""
Seed script for Simple Interest (Commercial Mathematics)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Simple Interest - Basic Computation 1",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b93,000 at 12% per annum for 3 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (3000 \u00d7 12 \u00d7 3) / 100 = \u20b91,080.\nTotal amount after 3 years = \u20b94,080.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,580",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,080",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b9880",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,380",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 2",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b911,000 at 10% per annum for 4 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (11000 \u00d7 10 \u00d7 4) / 100 = \u20b94,400.\nTotal amount after 4 years = \u20b915,400.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,200",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,900",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b94,700",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,400",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Basic Computation 3",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b97,000 at 12% per annum for 3 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (7000 \u00d7 12 \u00d7 3) / 100 = \u20b92,520.\nTotal amount after 3 years = \u20b99,520.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,520",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,020",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,320",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,820",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Basic Computation 4",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b919,000 at 12% per annum for 3 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (19000 \u00d7 12 \u00d7 3) / 100 = \u20b96,840.\nTotal amount after 3 years = \u20b925,840.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b96,640",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b97,140",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b96,840",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b97,340",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Basic Computation 5",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b920,000 at 6% per annum for 4 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (20000 \u00d7 6 \u00d7 4) / 100 = \u20b94,800.\nTotal amount after 4 years = \u20b924,800.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,600",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,800",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b95,300",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b95,100",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 6",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b92,000 at 12% per annum for 5 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (2000 \u00d7 12 \u00d7 5) / 100 = \u20b91,200.\nTotal amount after 5 years = \u20b93,200.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,700",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,000",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,200",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b91,500",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Basic Computation 7",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b915,000 at 8% per annum for 2 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (15000 \u00d7 8 \u00d7 2) / 100 = \u20b92,400.\nTotal amount after 2 years = \u20b917,400.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,400",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,900",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,200",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,700",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Basic Computation 8",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b913,000 at 12% per annum for 5 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (13000 \u00d7 12 \u00d7 5) / 100 = \u20b97,800.\nTotal amount after 5 years = \u20b920,800.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b97,600",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b97,800",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b98,300",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b98,100",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 9",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b913,000 at 6% per annum for 4 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (13000 \u00d7 6 \u00d7 4) / 100 = \u20b93,120.\nTotal amount after 4 years = \u20b916,120.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,120",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,920",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,420",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,620",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Basic Computation 10",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b98,000 at 8% per annum for 3 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (8000 \u00d7 8 \u00d7 3) / 100 = \u20b91,920.\nTotal amount after 3 years = \u20b99,920.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,720",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,920",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b92,420",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,220",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 11",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b916,000 at 6% per annum for 4 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (16000 \u00d7 6 \u00d7 4) / 100 = \u20b93,840.\nTotal amount after 4 years = \u20b919,840.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,140",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,840",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b94,340",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,640",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 12",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b920,000 at 10% per annum for 5 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (20000 \u00d7 10 \u00d7 5) / 100 = \u20b910,000.\nTotal amount after 5 years = \u20b930,000.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b99,800",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b910,000",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b910,500",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b910,300",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 13",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b97,000 at 6% per annum for 2 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (7000 \u00d7 6 \u00d7 2) / 100 = \u20b9840.\nTotal amount after 2 years = \u20b97,840.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9640",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,340",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9840",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b91,140",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Basic Computation 14",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b916,000 at 6% per annum for 2 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (16000 \u00d7 6 \u00d7 2) / 100 = \u20b91,920.\nTotal amount after 2 years = \u20b917,920.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,220",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,720",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,920",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b92,420",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Basic Computation 15",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b98,000 at 5% per annum for 2 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (8000 \u00d7 5 \u00d7 2) / 100 = \u20b9800.\nTotal amount after 2 years = \u20b98,800.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9800",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b91,100",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,300",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9600",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Basic Computation 16",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b94,000 at 10% per annum for 3 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (4000 \u00d7 10 \u00d7 3) / 100 = \u20b91,200.\nTotal amount after 3 years = \u20b95,200.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,500",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,000",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,200",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b91,700",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Basic Computation 17",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b918,000 at 5% per annum for 5 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (18000 \u00d7 5 \u00d7 5) / 100 = \u20b94,500.\nTotal amount after 5 years = \u20b922,500.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,800",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,500",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b95,000",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,300",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 18",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b92,000 at 6% per annum for 4 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (2000 \u00d7 6 \u00d7 4) / 100 = \u20b9480.\nTotal amount after 4 years = \u20b92,480.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9780",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9280",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9480",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b9980",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Basic Computation 19",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b913,000 at 5% per annum for 5 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (13000 \u00d7 5 \u00d7 5) / 100 = \u20b93,250.\nTotal amount after 5 years = \u20b916,250.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,550",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,250",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b93,050",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,750",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Basic Computation 20",
        "difficulty": "Easy",
        "question_text": "Find the simple interest on a principal of \u20b912,000 at 8% per annum for 5 years.",
        "sample_answer": "SI = (P \u00d7 R \u00d7 T) / 100 = (12000 \u00d7 8 \u00d7 5) / 100 = \u20b94,800.\nTotal amount after 5 years = \u20b916,800.",
        "tips": "Formula: SI = (P * R * T) / 100.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,600",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,800",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b95,300",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b95,100",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 21",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b99,000 yields an interest of \u20b91,800 in 4 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (1800 \u00d7 100) / (9000 \u00d7 4) = 5%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "5%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "4%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 22",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b923,000 yields an interest of \u20b96,900 in 3 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (6900 \u00d7 100) / (23000 \u00d7 3) = 10%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "11%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 23",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b97,000 yields an interest of \u20b92,520 in 3 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (2520 \u00d7 100) / (7000 \u00d7 3) = 12%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "14%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "13%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 24",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b920,000 yields an interest of \u20b93,200 in 2 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (3200 \u00d7 100) / (20000 \u00d7 2) = 8%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "10%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "7%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 25",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b914,000 yields an interest of \u20b93,360 in 3 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (3360 \u00d7 100) / (14000 \u00d7 3) = 8%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 26",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b914,000 yields an interest of \u20b92,100 in 3 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (2100 \u00d7 100) / (14000 \u00d7 3) = 5%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "6%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 27",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b96,000 yields an interest of \u20b9600 in 2 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (600 \u00d7 100) / (6000 \u00d7 2) = 5%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "6%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "4%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 28",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b925,000 yields an interest of \u20b93,750 in 3 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (3750 \u00d7 100) / (25000 \u00d7 3) = 5%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "6%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 29",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b918,000 yields an interest of \u20b93,600 in 4 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (3600 \u00d7 100) / (18000 \u00d7 4) = 5%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "5%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 30",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b99,000 yields an interest of \u20b9900 in 2 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (900 \u00d7 100) / (9000 \u00d7 2) = 5%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "6%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 31",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b917,000 yields an interest of \u20b92,720 in 2 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (2720 \u00d7 100) / (17000 \u00d7 2) = 8%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "10%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 32",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b97,000 yields an interest of \u20b92,800 in 4 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (2800 \u00d7 100) / (7000 \u00d7 4) = 10%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "11%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 33",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b912,000 yields an interest of \u20b93,600 in 3 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (3600 \u00d7 100) / (12000 \u00d7 3) = 10%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "9%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "11%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 34",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b923,000 yields an interest of \u20b92,300 in 2 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (2300 \u00d7 100) / (23000 \u00d7 2) = 5%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "7%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "6%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Find Rate of Interest 35",
        "difficulty": "Medium",
        "question_text": "A sum of \u20b910,000 yields an interest of \u20b94,800 in 4 years at simple interest. Find the annual rate of interest.",
        "sample_answer": "Rate R = (SI \u00d7 100) / (P \u00d7 T) = (4800 \u00d7 100) / (10000 \u00d7 4) = 12%.",
        "tips": "R = (SI * 100) / (P * T).",
        "options": [
            {
                "label": "A",
                "text": "12%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "13%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 36",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 20 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 20) = 100 / 20 = 5.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "9.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "7.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 37",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 8 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 8) = 100 / 8 = 12.5%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "10.5%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16.5%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12.5%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 38",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 5 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 5) = 100 / 5 = 20.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "18.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "22.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 39",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 10 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 10) = 100 / 10 = 10.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "8.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 40",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 4 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 4) = 100 / 4 = 25.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "27.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "25.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "29.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23.0%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 41",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 5 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 5) = 100 / 5 = 20.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "18.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "22.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 42",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 20 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 20) = 100 / 20 = 5.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "5.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "9.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 43",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 20 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 20) = 100 / 20 = 5.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "7.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "3.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 44",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 8 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 8) = 100 / 8 = 12.5%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "12.5%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "16.5%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10.5%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 45",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 10 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 10) = 100 / 10 = 10.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "12.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 46",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 4 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 4) = 100 / 4 = 25.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "27.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "29.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "23.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 47",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 20 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 20) = 100 / 20 = 5.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "7.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "9.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3.0%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 48",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 5 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 5) = 100 / 5 = 20.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "22.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 49",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 4 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 4) = 100 / 4 = 25.0%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "27.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "29.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "23.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Simple Interest - Sum Doubles Condition 50",
        "difficulty": "Medium",
        "question_text": "At what annual rate of simple interest will a sum of money double itself in 8 years?",
        "sample_answer": "Let Principal = P. Amount = 2P => Simple Interest SI = 2P - P = P.\nR = (SI \u00d7 100) / (P \u00d7 T) = (P \u00d7 100) / (P \u00d7 8) = 100 / 8 = 12.5%.",
        "tips": "For sum to double at SI: Rate = 100 / Time.",
        "options": [
            {
                "label": "A",
                "text": "12.5%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "16.5%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14.5%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Simple Interest').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Simple Interest').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Commercial Mathematics',
                    topic='Simple Interest',
                    title=q.get('title', 'Simple Interest'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Simple Interest via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Simple Interest: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Simple Interest',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Commercial Mathematics', 'Simple Interest',
                        q.get('title', 'Simple Interest'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Simple Interest into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
