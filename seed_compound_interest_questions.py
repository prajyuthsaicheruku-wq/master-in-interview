"""
Seed script for Compound Interest (Commercial Mathematics)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Compound Interest - 2 Year Compound Interest 1",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b910,000 at 5% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 10000 \u00d7 (1 + 5/100)^2 = \u20b911,025.\nCompound Interest = A - P = \u20b911,025 - \u20b910,000 = \u20b91,025.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,175",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9925",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,025",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b91,325",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 2",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b920,000 at 5% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 20000 \u00d7 (1 + 5/100)^2 = \u20b922,050.\nCompound Interest = A - P = \u20b922,050 - \u20b920,000 = \u20b92,050.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,050",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,200",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,950",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,350",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 3",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b912,000 at 10% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 12000 \u00d7 (1 + 10/100)^2 = \u20b914,520.\nCompound Interest = A - P = \u20b914,520 - \u20b912,000 = \u20b92,520.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,520",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,420",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,670",
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
        "title": "Compound Interest - 2 Year Compound Interest 4",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b95,000 at 10% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 5000 \u00d7 (1 + 10/100)^2 = \u20b96,050.\nCompound Interest = A - P = \u20b96,050 - \u20b95,000 = \u20b91,050.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,200",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,350",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,050",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b9950",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 5",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b95,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 5000 \u00d7 (1 + 20/100)^2 = \u20b97,200.\nCompound Interest = A - P = \u20b97,200 - \u20b95,000 = \u20b92,200.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,100",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,350",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,500",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,200",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 6",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b95,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 5000 \u00d7 (1 + 20/100)^2 = \u20b97,200.\nCompound Interest = A - P = \u20b97,200 - \u20b95,000 = \u20b92,200.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,200",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,350",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,100",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,500",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 7",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b95,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 5000 \u00d7 (1 + 20/100)^2 = \u20b97,200.\nCompound Interest = A - P = \u20b97,200 - \u20b95,000 = \u20b92,200.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,500",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,200",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b92,350",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,100",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 8",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b920,000 at 5% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 20000 \u00d7 (1 + 5/100)^2 = \u20b922,050.\nCompound Interest = A - P = \u20b922,050 - \u20b920,000 = \u20b92,050.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,950",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,050",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b92,350",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,200",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 9",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b910,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 10000 \u00d7 (1 + 20/100)^2 = \u20b914,400.\nCompound Interest = A - P = \u20b914,400 - \u20b910,000 = \u20b94,400.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,300",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,400",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b94,700",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,550",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 10",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b910,000 at 5% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 10000 \u00d7 (1 + 5/100)^2 = \u20b911,025.\nCompound Interest = A - P = \u20b911,025 - \u20b910,000 = \u20b91,025.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,325",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,175",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,025",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b9925",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 11",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b98,000 at 10% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 8000 \u00d7 (1 + 10/100)^2 = \u20b99,680.\nCompound Interest = A - P = \u20b99,680 - \u20b98,000 = \u20b91,680.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,680",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b91,830",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,580",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,980",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 12",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b920,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 20000 \u00d7 (1 + 20/100)^2 = \u20b928,800.\nCompound Interest = A - P = \u20b928,800 - \u20b920,000 = \u20b98,800.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b98,950",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b98,800",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b99,100",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b98,700",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 13",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b910,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 10000 \u00d7 (1 + 20/100)^2 = \u20b914,400.\nCompound Interest = A - P = \u20b914,400 - \u20b910,000 = \u20b94,400.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,550",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,300",
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
        "title": "Compound Interest - 2 Year Compound Interest 14",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b912,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 12000 \u00d7 (1 + 20/100)^2 = \u20b917,280.\nCompound Interest = A - P = \u20b917,280 - \u20b912,000 = \u20b95,280.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b95,430",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b95,280",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b95,580",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b95,180",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 15",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b98,000 at 20% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 8000 \u00d7 (1 + 20/100)^2 = \u20b911,520.\nCompound Interest = A - P = \u20b911,520 - \u20b98,000 = \u20b93,520.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,420",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,670",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,820",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,520",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 16",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b920,000 at 10% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 20000 \u00d7 (1 + 10/100)^2 = \u20b924,200.\nCompound Interest = A - P = \u20b924,200 - \u20b920,000 = \u20b94,200.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,200",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b94,500",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b94,100",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,350",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 17",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b98,000 at 10% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 8000 \u00d7 (1 + 10/100)^2 = \u20b99,680.\nCompound Interest = A - P = \u20b99,680 - \u20b98,000 = \u20b91,680.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,580",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,830",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,980",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,680",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 18",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b910,000 at 10% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 10000 \u00d7 (1 + 10/100)^2 = \u20b912,100.\nCompound Interest = A - P = \u20b912,100 - \u20b910,000 = \u20b92,100.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,250",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,000",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,400",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,100",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 19",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b910,000 at 5% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 10000 \u00d7 (1 + 5/100)^2 = \u20b911,025.\nCompound Interest = A - P = \u20b911,025 - \u20b910,000 = \u20b91,025.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,175",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9925",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,025",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b91,325",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - 2 Year Compound Interest 20",
        "difficulty": "Medium",
        "question_text": "What is the compound interest on a sum of \u20b95,000 at 5% per annum compounded annually for 2 years?",
        "sample_answer": "Amount A = P \u00d7 (1 + R/100)^T = 5000 \u00d7 (1 + 5/100)^2 = \u20b95,512.\nCompound Interest = A - P = \u20b95,512 - \u20b95,000 = \u20b9512.",
        "tips": "A = P(1 + R/100)^T. CI = A - P.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9662",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9412",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9512",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b9812",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - CI and SI Difference 21",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b98,000 for 2 years at 5% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 8000 \u00d7 (5/100)^2 = \u20b920.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b945",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b935",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b920",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b910",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - CI and SI Difference 22",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b920,000 for 2 years at 8% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 20000 \u00d7 (8/100)^2 = \u20b9128.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9118",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9143",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9153",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9128",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - CI and SI Difference 23",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b94,000 for 2 years at 8% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 4000 \u00d7 (8/100)^2 = \u20b925.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b925",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b940",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b915",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b950",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - CI and SI Difference 24",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b95,000 for 2 years at 8% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 5000 \u00d7 (8/100)^2 = \u20b932.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b947",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b932",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b922",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b957",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - CI and SI Difference 25",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b98,000 for 2 years at 5% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 8000 \u00d7 (5/100)^2 = \u20b920.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b910",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b935",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b945",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b920",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - CI and SI Difference 26",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b915,000 for 2 years at 8% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 15000 \u00d7 (8/100)^2 = \u20b996.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b996",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b986",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9121",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9111",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - CI and SI Difference 27",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b94,000 for 2 years at 5% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 4000 \u00d7 (5/100)^2 = \u20b910.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b910",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b925",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b90",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b935",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - CI and SI Difference 28",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b920,000 for 2 years at 5% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 20000 \u00d7 (5/100)^2 = \u20b950.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b965",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b950",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b975",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b940",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - CI and SI Difference 29",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b95,000 for 2 years at 10% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 5000 \u00d7 (10/100)^2 = \u20b950.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b965",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b975",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b950",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b940",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - CI and SI Difference 30",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b910,000 for 2 years at 5% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 10000 \u00d7 (5/100)^2 = \u20b925.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b950",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b915",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b940",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b925",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - CI and SI Difference 31",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b915,000 for 2 years at 12% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 15000 \u00d7 (12/100)^2 = \u20b9216.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9231",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9216",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b9241",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9206",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - CI and SI Difference 32",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b98,000 for 2 years at 5% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 8000 \u00d7 (5/100)^2 = \u20b920.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b945",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b935",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b920",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b910",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - CI and SI Difference 33",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b920,000 for 2 years at 10% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 20000 \u00d7 (10/100)^2 = \u20b9200.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9225",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9190",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9215",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9200",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - CI and SI Difference 34",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b98,000 for 2 years at 12% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 8000 \u00d7 (12/100)^2 = \u20b9115.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9130",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9115",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b9140",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9105",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - CI and SI Difference 35",
        "difficulty": "Medium",
        "question_text": "The difference between compound interest and simple interest on \u20b96,000 for 2 years at 5% per annum is:",
        "sample_answer": "Difference for 2 years = P \u00d7 (R / 100)^2 = 6000 \u00d7 (5/100)^2 = \u20b915.",
        "tips": "Difference between CI and SI for 2 years = P * (R/100)^2.",
        "options": [
            {
                "label": "A",
                "text": "\u20b915",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b930",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b95",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b940",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 36",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 7 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 7 years, it becomes 2^3 = 8 times in (3 \u00d7 7) = 21 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "21 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "23 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 37",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 3 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 3 years, it becomes 2^3 = 8 times in (3 \u00d7 3) = 9 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "12 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "11 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 38",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 3 years. In how many years will it become 4 times itself?",
        "sample_answer": "If money becomes 2 times in 3 years, it becomes 2^2 = 4 times in (2 \u00d7 3) = 6 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "8 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "3 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 39",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 3 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 3 years, it becomes 2^3 = 8 times in (3 \u00d7 3) = 9 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "12 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "6 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 40",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 5 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 5 years, it becomes 2^3 = 8 times in (3 \u00d7 5) = 15 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "17 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "20 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 41",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 7 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 7 years, it becomes 2^3 = 8 times in (3 \u00d7 7) = 21 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "21 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "28 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "23 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "14 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 42",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 7 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 7 years, it becomes 2^3 = 8 times in (3 \u00d7 7) = 21 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "23 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "28 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21 years",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "14 years",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 43",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 4 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 4 years, it becomes 2^3 = 8 times in (3 \u00d7 4) = 12 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "12 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "16 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 44",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 3 years. In how many years will it become 4 times itself?",
        "sample_answer": "If money becomes 2 times in 3 years, it becomes 2^2 = 4 times in (2 \u00d7 3) = 6 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "8 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6 years",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 45",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 3 years. In how many years will it become 4 times itself?",
        "sample_answer": "If money becomes 2 times in 3 years, it becomes 2^2 = 4 times in (2 \u00d7 3) = 6 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "9 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6 years",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 46",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 6 years. In how many years will it become 4 times itself?",
        "sample_answer": "If money becomes 2 times in 6 years, it becomes 2^2 = 4 times in (2 \u00d7 6) = 12 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "18 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 years",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 47",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 6 years. In how many years will it become 4 times itself?",
        "sample_answer": "If money becomes 2 times in 6 years, it becomes 2^2 = 4 times in (2 \u00d7 6) = 12 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "18 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 years",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "14 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6 years",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 48",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 4 years. In how many years will it become 4 times itself?",
        "sample_answer": "If money becomes 2 times in 4 years, it becomes 2^2 = 4 times in (2 \u00d7 4) = 8 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "8 years",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "10 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4 years",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 49",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 3 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 3 years, it becomes 2^3 = 8 times in (3 \u00d7 3) = 9 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "6 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9 years",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Compound Interest - Money Multiplication Rule 50",
        "difficulty": "Medium",
        "question_text": "A sum of money placed at compound interest doubles itself in 5 years. In how many years will it become 8 times itself?",
        "sample_answer": "If money becomes 2 times in 5 years, it becomes 2^3 = 8 times in (3 \u00d7 5) = 15 years.",
        "tips": "If sum doubles in T years, it becomes 2^k times in k * T years.",
        "options": [
            {
                "label": "A",
                "text": "20 years",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 years",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17 years",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 years",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Compound Interest').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Compound Interest').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Commercial Mathematics',
                    topic='Compound Interest',
                    title=q.get('title', 'Compound Interest'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Compound Interest via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Compound Interest: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Compound Interest',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Commercial Mathematics', 'Compound Interest',
                        q.get('title', 'Compound Interest'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Compound Interest into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
