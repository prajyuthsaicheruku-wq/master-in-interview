"""
Seed script for Ratio & Proportion (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Ratio & Proportion - Share of Sum 1",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9712 between A and B in the ratio 3:5. What is A's share?",
        "sample_answer": "Total parts = 3 + 5 = 8.\nValue of 1 part = \u20b9712 / 8 = \u20b989.\nA's share = 3 \u00d7 \u20b989 = \u20b9267.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9287",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9178",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9356",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9267",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 2",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9496 between A and B in the ratio 3:5. What is A's share?",
        "sample_answer": "Total parts = 3 + 5 = 8.\nValue of 1 part = \u20b9496 / 8 = \u20b962.\nA's share = 3 \u00d7 \u20b962 = \u20b9186.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9124",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9206",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9186",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b9248",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 3",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9210 between A and B in the ratio 2:3. What is A's share?",
        "sample_answer": "Total parts = 2 + 3 = 5.\nValue of 1 part = \u20b9210 / 5 = \u20b942.\nA's share = 2 \u00d7 \u20b942 = \u20b984.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b984",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b9126",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b942",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9104",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 4",
        "difficulty": "Easy",
        "question_text": "Divide \u20b91164 between A and B in the ratio 5:7. What is A's share?",
        "sample_answer": "Total parts = 5 + 7 = 12.\nValue of 1 part = \u20b91164 / 12 = \u20b997.\nA's share = 5 \u00d7 \u20b997 = \u20b9485.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9582",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9388",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9485",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b9505",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 5",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9200 between A and B in the ratio 3:5. What is A's share?",
        "sample_answer": "Total parts = 3 + 5 = 8.\nValue of 1 part = \u20b9200 / 8 = \u20b925.\nA's share = 3 \u00d7 \u20b925 = \u20b975.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b975",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b950",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9100",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b995",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 6",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9108 between A and B in the ratio 1:2. What is A's share?",
        "sample_answer": "Total parts = 1 + 2 = 3.\nValue of 1 part = \u20b9108 / 3 = \u20b936.\nA's share = 1 \u00d7 \u20b936 = \u20b936.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b936",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b972",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b956",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b90",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 7",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9455 between A and B in the ratio 2:3. What is A's share?",
        "sample_answer": "Total parts = 2 + 3 = 5.\nValue of 1 part = \u20b9455 / 5 = \u20b991.\nA's share = 2 \u00d7 \u20b991 = \u20b9182.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9182",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b9273",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9202",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b991",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 8",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9207 between A and B in the ratio 1:2. What is A's share?",
        "sample_answer": "Total parts = 1 + 2 = 3.\nValue of 1 part = \u20b9207 / 3 = \u20b969.\nA's share = 1 \u00d7 \u20b969 = \u20b969.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b989",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b90",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9138",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b969",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 9",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9648 between A and B in the ratio 4:5. What is A's share?",
        "sample_answer": "Total parts = 4 + 5 = 9.\nValue of 1 part = \u20b9648 / 9 = \u20b972.\nA's share = 4 \u00d7 \u20b972 = \u20b9288.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9288",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b9308",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9360",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9216",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 10",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9312 between A and B in the ratio 5:7. What is A's share?",
        "sample_answer": "Total parts = 5 + 7 = 12.\nValue of 1 part = \u20b9312 / 12 = \u20b926.\nA's share = 5 \u00d7 \u20b926 = \u20b9130.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9104",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9130",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b9156",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9150",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 11",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9210 between A and B in the ratio 2:3. What is A's share?",
        "sample_answer": "Total parts = 2 + 3 = 5.\nValue of 1 part = \u20b9210 / 5 = \u20b942.\nA's share = 2 \u00d7 \u20b942 = \u20b984.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b942",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b984",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b9126",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9104",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 12",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9176 between A and B in the ratio 3:5. What is A's share?",
        "sample_answer": "Total parts = 3 + 5 = 8.\nValue of 1 part = \u20b9176 / 8 = \u20b922.\nA's share = 3 \u00d7 \u20b922 = \u20b966.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b944",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b986",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b966",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b988",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 13",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9488 between A and B in the ratio 3:5. What is A's share?",
        "sample_answer": "Total parts = 3 + 5 = 8.\nValue of 1 part = \u20b9488 / 8 = \u20b961.\nA's share = 3 \u00d7 \u20b961 = \u20b9183.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9183",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b9122",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9244",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9203",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 14",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9201 between A and B in the ratio 1:2. What is A's share?",
        "sample_answer": "Total parts = 1 + 2 = 3.\nValue of 1 part = \u20b9201 / 3 = \u20b967.\nA's share = 1 \u00d7 \u20b967 = \u20b967.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b967",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b90",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b987",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9134",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 15",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9420 between A and B in the ratio 2:3. What is A's share?",
        "sample_answer": "Total parts = 2 + 3 = 5.\nValue of 1 part = \u20b9420 / 5 = \u20b984.\nA's share = 2 \u00d7 \u20b984 = \u20b9168.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9188",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b984",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9252",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9168",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 16",
        "difficulty": "Easy",
        "question_text": "Divide \u20b91092 between A and B in the ratio 5:7. What is A's share?",
        "sample_answer": "Total parts = 5 + 7 = 12.\nValue of 1 part = \u20b91092 / 12 = \u20b991.\nA's share = 5 \u00d7 \u20b991 = \u20b9455.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9546",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9475",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9364",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9455",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 17",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9395 between A and B in the ratio 2:3. What is A's share?",
        "sample_answer": "Total parts = 2 + 3 = 5.\nValue of 1 part = \u20b9395 / 5 = \u20b979.\nA's share = 2 \u00d7 \u20b979 = \u20b9158.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b979",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9158",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b9178",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9237",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 18",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9440 between A and B in the ratio 3:5. What is A's share?",
        "sample_answer": "Total parts = 3 + 5 = 8.\nValue of 1 part = \u20b9440 / 8 = \u20b955.\nA's share = 3 \u00d7 \u20b955 = \u20b9165.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9165",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b9110",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9185",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9220",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 19",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9864 between A and B in the ratio 5:7. What is A's share?",
        "sample_answer": "Total parts = 5 + 7 = 12.\nValue of 1 part = \u20b9864 / 12 = \u20b972.\nA's share = 5 \u00d7 \u20b972 = \u20b9360.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b9380",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9432",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b9360",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b9288",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Share of Sum 20",
        "difficulty": "Easy",
        "question_text": "Divide \u20b9150 between A and B in the ratio 2:3. What is A's share?",
        "sample_answer": "Total parts = 2 + 3 = 5.\nValue of 1 part = \u20b9150 / 5 = \u20b930.\nA's share = 2 \u00d7 \u20b930 = \u20b960.",
        "tips": "Sum divided by total ratio parts gives value of 1 part.",
        "options": [
            {
                "label": "A",
                "text": "\u20b930",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b960",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b980",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b990",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 21",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 8 and 10:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(8 \u00d7 10) = 8.94.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "8.94",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "10.14",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11.44",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.74",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 22",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 12 and 8:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(12 \u00d7 8) = 9.8.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "9.8",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "12.3",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11.0",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.6",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 23",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 6 and 12:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(6 \u00d7 12) = 8.49.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "7.29",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.49",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10.99",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9.69",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 24",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 10 and 16:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(10 \u00d7 16) = 12.65.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "11.45",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13.85",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.65",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "15.15",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 25",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 6 and 8:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(6 \u00d7 8) = 6.93.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "6.93",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "9.43",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.13",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5.73",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 26",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 6 and 8:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(6 \u00d7 8) = 6.93.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "8.13",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "9.43",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6.93",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "5.73",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 27",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 8 and 14:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(8 \u00d7 14) = 10.58.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "9.38",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11.78",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.08",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10.58",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 28",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 4 and 6:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(4 \u00d7 6) = 4.9.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "7.4",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3.7",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6.1",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4.9",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 29",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 10 and 8:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(10 \u00d7 8) = 8.94.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "7.74",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.94",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10.14",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11.44",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 30",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 6 and 6:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(6 \u00d7 6) = 6.0.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "6.0",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "4.8",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.5",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7.2",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 31",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 12 and 16:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(12 \u00d7 16) = 13.86.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "15.06",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12.66",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.86",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "16.36",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 32",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 10 and 12:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(10 \u00d7 12) = 10.95.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "13.45",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10.95",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "9.75",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12.15",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 33",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 12 and 8:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(12 \u00d7 8) = 9.8.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "8.6",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11.0",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9.8",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "12.3",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 34",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 8 and 12:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(8 \u00d7 12) = 9.8.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "11.0",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.6",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "9.8",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "12.3",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Mean Proportional 35",
        "difficulty": "Medium",
        "question_text": "Find the mean proportional between 6 and 8:",
        "sample_answer": "Mean proportional between a and b is \u221a(a \u00d7 b) = \u221a(6 \u00d7 8) = 6.93.",
        "tips": "Mean proportional of a and b is sqrt(a * b).",
        "options": [
            {
                "label": "A",
                "text": "9.43",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5.73",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.13",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6.93",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 36",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b971.50, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 71.50 / 2.75 = 26.\nNumber of \u20b91 coins = 26.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "21",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "31",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "36",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 37",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b935.75, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 35.75 / 2.75 = 13.\nNumber of \u20b91 coins = 13.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
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
                "text": "13",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "23",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 38",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b966.00, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 66.00 / 2.75 = 24.\nNumber of \u20b91 coins = 24.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "34",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "29",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "19",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "24",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 39",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b941.25, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 41.25 / 2.75 = 15.\nNumber of \u20b91 coins = 15.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 40",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b933.00, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 33.00 / 2.75 = 12.\nNumber of \u20b91 coins = 12.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "22",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12",
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
        "title": "Ratio & Proportion - Coin Bag Problem 41",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b944.00, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 44.00 / 2.75 = 16.\nNumber of \u20b91 coins = 16.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "26",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "16",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "21",
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
        "title": "Ratio & Proportion - Coin Bag Problem 42",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b974.25, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 74.25 / 2.75 = 27.\nNumber of \u20b91 coins = 27.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "27",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "37",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "32",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 43",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b999.00, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 99.00 / 2.75 = 36.\nNumber of \u20b91 coins = 36.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "36",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "41",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "31",
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
        "title": "Ratio & Proportion - Coin Bag Problem 44",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b971.50, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 71.50 / 2.75 = 26.\nNumber of \u20b91 coins = 26.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "21",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "31",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 45",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b979.75, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 79.75 / 2.75 = 29.\nNumber of \u20b91 coins = 29.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "29",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "39",
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
        "title": "Ratio & Proportion - Coin Bag Problem 46",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b9107.25, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 107.25 / 2.75 = 39.\nNumber of \u20b91 coins = 39.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "44",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "39",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "49",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 47",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b927.50, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 27.50 / 2.75 = 10.\nNumber of \u20b91 coins = 10.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "5",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15",
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
        "title": "Ratio & Proportion - Coin Bag Problem 48",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b949.50, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 49.50 / 2.75 = 18.\nNumber of \u20b91 coins = 18.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "18",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "23",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 49",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b966.00, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 66.00 / 2.75 = 24.\nNumber of \u20b91 coins = 24.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "29",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Ratio & Proportion - Coin Bag Problem 50",
        "difficulty": "Medium",
        "question_text": "A bag contains \u20b91, 50p, and 25p coins in the ratio 1:2:3. If total money in the bag is \u20b952.25, find the number of \u20b91 coins.",
        "sample_answer": "Let parts be 1x, 2x, 3x.\nTotal value = 1x(1) + 2x(0.50) + 3x(0.25) = 2.75x = 2.75x.\nx = 52.25 / 2.75 = 19.\nNumber of \u20b91 coins = 19.",
        "tips": "Convert each coin denomination to rupee value and sum with ratio variables.",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "29",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "19",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "14",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Ratio & Proportion').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Ratio & Proportion').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='Ratio & Proportion',
                    title=q.get('title', 'Ratio & Proportion'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Ratio & Proportion via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Ratio & Proportion: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Ratio & Proportion',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'Ratio & Proportion',
                        q.get('title', 'Ratio & Proportion'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Ratio & Proportion into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
