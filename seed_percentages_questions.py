"""
Seed script for Percentages (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Percentages - Simple Calculation 1",
        "difficulty": "Easy",
        "question_text": "What is 15% of 310?",
        "sample_answer": "Calculation: (15 / 100) \u00d7 310 = 46.",
        "tips": "15% is equivalent to 15/100.",
        "options": [
            {
                "label": "A",
                "text": "51",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "41",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "56",
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
        "title": "Percentages - Simple Calculation 2",
        "difficulty": "Easy",
        "question_text": "What is 10% of 430?",
        "sample_answer": "Calculation: (10 / 100) \u00d7 430 = 43.",
        "tips": "10% is equivalent to 10/100.",
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
                "text": "43",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "53",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Simple Calculation 3",
        "difficulty": "Easy",
        "question_text": "What is 50% of 410?",
        "sample_answer": "Calculation: (50 / 100) \u00d7 410 = 205.",
        "tips": "50% is equivalent to 50/100.",
        "options": [
            {
                "label": "A",
                "text": "210",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "215",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "205",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "200",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Simple Calculation 4",
        "difficulty": "Easy",
        "question_text": "What is 40% of 100?",
        "sample_answer": "Calculation: (40 / 100) \u00d7 100 = 40.",
        "tips": "40% is equivalent to 40/100.",
        "options": [
            {
                "label": "A",
                "text": "35",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "45",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Simple Calculation 5",
        "difficulty": "Easy",
        "question_text": "What is 10% of 480?",
        "sample_answer": "Calculation: (10 / 100) \u00d7 480 = 48.",
        "tips": "10% is equivalent to 10/100.",
        "options": [
            {
                "label": "A",
                "text": "58",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "53",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "43",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "48",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Simple Calculation 6",
        "difficulty": "Easy",
        "question_text": "What is 75% of 290?",
        "sample_answer": "Calculation: (75 / 100) \u00d7 290 = 217.",
        "tips": "75% is equivalent to 75/100.",
        "options": [
            {
                "label": "A",
                "text": "227",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "217",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "212",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "222",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Simple Calculation 7",
        "difficulty": "Easy",
        "question_text": "What is 25% of 100?",
        "sample_answer": "Calculation: (25 / 100) \u00d7 100 = 25.",
        "tips": "25% is equivalent to 25/100.",
        "options": [
            {
                "label": "A",
                "text": "35",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Simple Calculation 8",
        "difficulty": "Easy",
        "question_text": "What is 75% of 790?",
        "sample_answer": "Calculation: (75 / 100) \u00d7 790 = 592.",
        "tips": "75% is equivalent to 75/100.",
        "options": [
            {
                "label": "A",
                "text": "597",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "602",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "592",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "587",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Simple Calculation 9",
        "difficulty": "Easy",
        "question_text": "What is 75% of 780?",
        "sample_answer": "Calculation: (75 / 100) \u00d7 780 = 585.",
        "tips": "75% is equivalent to 75/100.",
        "options": [
            {
                "label": "A",
                "text": "585",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "580",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "595",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "590",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Simple Calculation 10",
        "difficulty": "Easy",
        "question_text": "What is 20% of 160?",
        "sample_answer": "Calculation: (20 / 100) \u00d7 160 = 32.",
        "tips": "20% is equivalent to 20/100.",
        "options": [
            {
                "label": "A",
                "text": "42",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "27",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "37",
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
        "title": "Percentages - Simple Calculation 11",
        "difficulty": "Easy",
        "question_text": "What is 50% of 370?",
        "sample_answer": "Calculation: (50 / 100) \u00d7 370 = 185.",
        "tips": "50% is equivalent to 50/100.",
        "options": [
            {
                "label": "A",
                "text": "195",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "190",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "180",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "185",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Simple Calculation 12",
        "difficulty": "Easy",
        "question_text": "What is 20% of 560?",
        "sample_answer": "Calculation: (20 / 100) \u00d7 560 = 112.",
        "tips": "20% is equivalent to 20/100.",
        "options": [
            {
                "label": "A",
                "text": "112",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "122",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "117",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "107",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Simple Calculation 13",
        "difficulty": "Easy",
        "question_text": "What is 30% of 200?",
        "sample_answer": "Calculation: (30 / 100) \u00d7 200 = 60.",
        "tips": "30% is equivalent to 30/100.",
        "options": [
            {
                "label": "A",
                "text": "60",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "65",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "55",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "70",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Simple Calculation 14",
        "difficulty": "Easy",
        "question_text": "What is 20% of 750?",
        "sample_answer": "Calculation: (20 / 100) \u00d7 750 = 150.",
        "tips": "20% is equivalent to 20/100.",
        "options": [
            {
                "label": "A",
                "text": "145",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "155",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "150",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "160",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Simple Calculation 15",
        "difficulty": "Easy",
        "question_text": "What is 15% of 530?",
        "sample_answer": "Calculation: (15 / 100) \u00d7 530 = 79.",
        "tips": "15% is equivalent to 15/100.",
        "options": [
            {
                "label": "A",
                "text": "84",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "89",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "79",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "74",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 16",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b916,000 per month. If the company gives a 20% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 20% of \u20b916,000 = \u20b93,200.\nNew salary = \u20b916,000 + \u20b93,200 = \u20b919,200.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b918,200",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b920,700",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b921,200",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b919,200",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Salary Hike 17",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b919,000 per month. If the company gives a 10% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 10% of \u20b919,000 = \u20b91,900.\nNew salary = \u20b919,000 + \u20b91,900 = \u20b920,900.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b919,900",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b922,400",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b920,900",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b922,900",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 18",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b915,000 per month. If the company gives a 25% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 25% of \u20b915,000 = \u20b93,750.\nNew salary = \u20b915,000 + \u20b93,750 = \u20b918,750.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b918,750",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b920,250",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b920,750",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b917,750",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Salary Hike 19",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b936,000 per month. If the company gives a 25% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 25% of \u20b936,000 = \u20b99,000.\nNew salary = \u20b936,000 + \u20b99,000 = \u20b945,000.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b947,000",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b944,000",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b945,000",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b946,500",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 20",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b926,000 per month. If the company gives a 20% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 20% of \u20b926,000 = \u20b95,200.\nNew salary = \u20b926,000 + \u20b95,200 = \u20b931,200.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b931,200",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b932,700",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b930,200",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b933,200",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Salary Hike 21",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b920,000 per month. If the company gives a 15% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 15% of \u20b920,000 = \u20b93,000.\nNew salary = \u20b920,000 + \u20b93,000 = \u20b923,000.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b922,000",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b924,500",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b923,000",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b925,000",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 22",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b932,000 per month. If the company gives a 10% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 10% of \u20b932,000 = \u20b93,200.\nNew salary = \u20b932,000 + \u20b93,200 = \u20b935,200.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b937,200",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b934,200",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b935,200",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b936,700",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 23",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b939,000 per month. If the company gives a 20% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 20% of \u20b939,000 = \u20b97,800.\nNew salary = \u20b939,000 + \u20b97,800 = \u20b946,800.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b948,800",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b948,300",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b946,800",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b945,800",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 24",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b915,000 per month. If the company gives a 25% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 25% of \u20b915,000 = \u20b93,750.\nNew salary = \u20b915,000 + \u20b93,750 = \u20b918,750.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b920,250",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b920,750",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b917,750",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b918,750",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Salary Hike 25",
        "difficulty": "Easy",
        "question_text": "An employee earns \u20b923,000 per month. If the company gives a 25% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 25% of \u20b923,000 = \u20b95,750.\nNew salary = \u20b923,000 + \u20b95,750 = \u20b928,750.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b928,750",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b930,250",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b930,750",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b927,750",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Salary Hike 26",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b926,000 per month. If the company gives a 10% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 10% of \u20b926,000 = \u20b92,600.\nNew salary = \u20b926,000 + \u20b92,600 = \u20b928,600.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b930,600",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b927,600",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b930,100",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b928,600",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Salary Hike 27",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b919,000 per month. If the company gives a 10% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 10% of \u20b919,000 = \u20b91,900.\nNew salary = \u20b919,000 + \u20b91,900 = \u20b920,900.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b919,900",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b922,400",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b922,900",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b920,900",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Salary Hike 28",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b917,000 per month. If the company gives a 15% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 15% of \u20b917,000 = \u20b92,550.\nNew salary = \u20b917,000 + \u20b92,550 = \u20b919,550.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b921,050",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b918,550",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b919,550",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b921,550",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 29",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b936,000 per month. If the company gives a 10% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 10% of \u20b936,000 = \u20b93,600.\nNew salary = \u20b936,000 + \u20b93,600 = \u20b939,600.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b939,600",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b941,100",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b938,600",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b941,600",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Salary Hike 30",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b928,000 per month. If the company gives a 20% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 20% of \u20b928,000 = \u20b95,600.\nNew salary = \u20b928,000 + \u20b95,600 = \u20b933,600.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b935,600",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b935,100",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b933,600",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b932,600",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 31",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b932,000 per month. If the company gives a 20% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 20% of \u20b932,000 = \u20b96,400.\nNew salary = \u20b932,000 + \u20b96,400 = \u20b938,400.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b937,400",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b938,400",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b940,400",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b939,900",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Salary Hike 32",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b936,000 per month. If the company gives a 10% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 10% of \u20b936,000 = \u20b93,600.\nNew salary = \u20b936,000 + \u20b93,600 = \u20b939,600.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b941,100",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b938,600",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b939,600",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b941,600",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 33",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b924,000 per month. If the company gives a 15% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 15% of \u20b924,000 = \u20b93,599.\nNew salary = \u20b924,000 + \u20b93,599 = \u20b927,599.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b927,599",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b926,599",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b929,599",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b929,099",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Salary Hike 34",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b939,000 per month. If the company gives a 10% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 10% of \u20b939,000 = \u20b93,900.\nNew salary = \u20b939,000 + \u20b93,900 = \u20b942,900.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b944,900",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b944,400",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b942,900",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b941,900",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Salary Hike 35",
        "difficulty": "Medium",
        "question_text": "An employee earns \u20b934,000 per month. If the company gives a 25% salary hike, what is the new monthly salary?",
        "sample_answer": "Hike amount = 25% of \u20b934,000 = \u20b98,500.\nNew salary = \u20b934,000 + \u20b98,500 = \u20b942,500.",
        "tips": "New value = Base * (1 + rate/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b944,000",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b942,500",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b944,500",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b941,500",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Successive Increase 36",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 20% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 20 + 20 + (20 \u00d7 20 / 100) = 44.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "42.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "44.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "40%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "46.0%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Successive Increase 37",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 10%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 10 + (10 \u00d7 10 / 100) = 21.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "21.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "23.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Successive Increase 38",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 20 + (10 \u00d7 20 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Successive Increase 39",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 20% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 20 + 20 + (20 \u00d7 20 / 100) = 44.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "44.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "40%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "42.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "46.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Successive Increase 40",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 20 + (10 \u00d7 20 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Successive Increase 41",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 10%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 10 + (10 \u00d7 10 / 100) = 21.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "20%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "19.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21.0%",
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
        "title": "Percentages - Successive Increase 42",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 20% and then further increases by 10%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 20 + 10 + (20 \u00d7 10 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Successive Increase 43",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 20 + (10 \u00d7 20 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Successive Increase 44",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 20 + (10 \u00d7 20 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Successive Increase 45",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 20% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 20 + 20 + (20 \u00d7 20 / 100) = 44.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "42.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "44.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "40%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "46.0%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Successive Increase 46",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 20% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 20 + 20 + (20 \u00d7 20 / 100) = 44.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "40%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "46.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "42.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "44.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Successive Increase 47",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 20% and then further increases by 10%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 20 + 10 + (20 \u00d7 10 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Successive Increase 48",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 20 + (10 \u00d7 20 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Successive Increase 49",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 20% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 20 + 20 + (20 \u00d7 20 / 100) = 44.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "46.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "42.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "44.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Percentages - Successive Increase 50",
        "difficulty": "Medium",
        "question_text": "If the price of a commodity increases by 10% and then further increases by 20%, find the net percentage increase in price.",
        "sample_answer": "Net percentage formula: a + b + (ab / 100) = 10 + 20 + (10 \u00d7 20 / 100) = 32.0%.",
        "tips": "Formula: Net % = a + b + (ab/100).",
        "options": [
            {
                "label": "A",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30%",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Percentages').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Percentages').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='Percentages',
                    title=q.get('title', 'Percentages'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Percentages via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Percentages: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Percentages',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'Percentages',
                        q.get('title', 'Percentages'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Percentages into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
