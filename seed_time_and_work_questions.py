"""
Seed script for Time & Work (Time-Based Problems)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Time & Work - Work Together 1",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 20 days, and B can complete the same work in 12 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/20.\nB's 1 day work = 1/12.\nTogether 1 day work = 1/20 + 1/12 = (20 + 12) / (20 \u00d7 12).\nTotal days = (20 \u00d7 12) / (20 + 12) = 7.5 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "32 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "5.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Work Together 2",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 12 days, and B can complete the same work in 30 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/12.\nB's 1 day work = 1/30.\nTogether 1 day work = 1/12 + 1/30 = (12 + 30) / (12 \u00d7 30).\nTotal days = (12 \u00d7 30) / (12 + 30) = 8.6 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "42 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10.6 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6.6 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.6 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Work Together 3",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 15 days, and B can complete the same work in 12 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/15.\nB's 1 day work = 1/12.\nTogether 1 day work = 1/15 + 1/12 = (15 + 12) / (15 \u00d7 12).\nTotal days = (15 \u00d7 12) / (15 + 12) = 6.7 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "27 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.7 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4.7 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6.7 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Work Together 4",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 30 days, and B can complete the same work in 30 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/30.\nB's 1 day work = 1/30.\nTogether 1 day work = 1/30 + 1/30 = (30 + 30) / (30 \u00d7 30).\nTotal days = (30 \u00d7 30) / (30 + 30) = 15 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "17.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Work Together 5",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 12 days, and B can complete the same work in 30 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/12.\nB's 1 day work = 1/30.\nTogether 1 day work = 1/12 + 1/30 = (12 + 30) / (12 \u00d7 30).\nTotal days = (12 \u00d7 30) / (12 + 30) = 8.6 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "42 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.6 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10.6 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.6 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Work Together 6",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 10 days, and B can complete the same work in 20 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/10.\nB's 1 day work = 1/20.\nTogether 1 day work = 1/10 + 1/20 = (10 + 20) / (10 \u00d7 20).\nTotal days = (10 \u00d7 20) / (10 + 20) = 6.7 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "6.7 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.7 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4.7 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Work Together 7",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 15 days, and B can complete the same work in 20 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/15.\nB's 1 day work = 1/20.\nTogether 1 day work = 1/15 + 1/20 = (15 + 20) / (15 \u00d7 20).\nTotal days = (15 \u00d7 20) / (15 + 20) = 8.6 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "35 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.6 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.6 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "10.6 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Work Together 8",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 24 days, and B can complete the same work in 30 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/24.\nB's 1 day work = 1/30.\nTogether 1 day work = 1/24 + 1/30 = (24 + 30) / (24 \u00d7 30).\nTotal days = (24 \u00d7 30) / (24 + 30) = 13.3 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "13.3 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "54 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15.3 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11.3 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Work Together 9",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 10 days, and B can complete the same work in 40 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/10.\nB's 1 day work = 1/40.\nTogether 1 day work = 1/10 + 1/40 = (10 + 40) / (10 \u00d7 40).\nTotal days = (10 \u00d7 40) / (10 + 40) = 8 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "50 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "10.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Work Together 10",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 20 days, and B can complete the same work in 20 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/20.\nB's 1 day work = 1/20.\nTogether 1 day work = 1/20 + 1/20 = (20 + 20) / (20 \u00d7 20).\nTotal days = (20 \u00d7 20) / (20 + 20) = 10 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "12.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Work Together 11",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 10 days, and B can complete the same work in 12 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/10.\nB's 1 day work = 1/12.\nTogether 1 day work = 1/10 + 1/12 = (10 + 12) / (10 \u00d7 12).\nTotal days = (10 \u00d7 12) / (10 + 12) = 5.5 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "22 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5.5 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "7.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "3.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Work Together 12",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 24 days, and B can complete the same work in 12 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/24.\nB's 1 day work = 1/12.\nTogether 1 day work = 1/24 + 1/12 = (24 + 12) / (24 \u00d7 12).\nTotal days = (24 \u00d7 12) / (24 + 12) = 8 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "6.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "10.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Work Together 13",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 15 days, and B can complete the same work in 15 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/15.\nB's 1 day work = 1/15.\nTogether 1 day work = 1/15 + 1/15 = (15 + 15) / (15 \u00d7 15).\nTotal days = (15 \u00d7 15) / (15 + 15) = 7.5 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "30 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "5.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Work Together 14",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 15 days, and B can complete the same work in 40 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/15.\nB's 1 day work = 1/40.\nTogether 1 day work = 1/15 + 1/40 = (15 + 40) / (15 \u00d7 40).\nTotal days = (15 \u00d7 40) / (15 + 40) = 10.9 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "10.9 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "8.9 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.9 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "55 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Work Together 15",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 10 days, and B can complete the same work in 40 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/10.\nB's 1 day work = 1/40.\nTogether 1 day work = 1/10 + 1/40 = (10 + 40) / (10 \u00d7 40).\nTotal days = (10 \u00d7 40) / (10 + 40) = 8 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "50 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Work Together 16",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 12 days, and B can complete the same work in 15 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/12.\nB's 1 day work = 1/15.\nTogether 1 day work = 1/12 + 1/15 = (12 + 15) / (12 \u00d7 15).\nTotal days = (12 \u00d7 15) / (12 + 15) = 6.7 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "8.7 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "4.7 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "27 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "6.7 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Work Together 17",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 24 days, and B can complete the same work in 20 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/24.\nB's 1 day work = 1/20.\nTogether 1 day work = 1/24 + 1/20 = (24 + 20) / (24 \u00d7 20).\nTotal days = (24 \u00d7 20) / (24 + 20) = 10.9 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "10.9 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "12.9 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.9 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "44 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Work Together 18",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 30 days, and B can complete the same work in 40 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/30.\nB's 1 day work = 1/40.\nTogether 1 day work = 1/30 + 1/40 = (30 + 40) / (30 \u00d7 40).\nTotal days = (30 \u00d7 40) / (30 + 40) = 17.1 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "70 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.1 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "15.1 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19.1 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Work Together 19",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 24 days, and B can complete the same work in 12 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/24.\nB's 1 day work = 1/12.\nTogether 1 day work = 1/24 + 1/12 = (24 + 12) / (24 \u00d7 12).\nTotal days = (24 \u00d7 12) / (24 + 12) = 8 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "6.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "36 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Work Together 20",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 24 days, and B can complete the same work in 12 days. Working together, in how many days can they complete the work?",
        "sample_answer": "A's 1 day work = 1/24.\nB's 1 day work = 1/12.\nTogether 1 day work = 1/24 + 1/12 = (24 + 12) / (24 \u00d7 12).\nTotal days = (24 \u00d7 12) / (24 + 12) = 8 days.",
        "tips": "Together time = (A * B) / (A + B).",
        "options": [
            {
                "label": "A",
                "text": "36 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Leaving Early 21",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 10 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 10 days, A completes 10/20 of the work.\nRemaining work = 1 - 10/20 = 0.50.\nB finishes remaining work in 0.50 \u00d7 30 = 15 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "15 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "12.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Leaving Early 22",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 10 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 10 days, A completes 10/20 of the work.\nRemaining work = 1 - 10/20 = 0.50.\nB finishes remaining work in 0.50 \u00d7 30 = 15 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "15 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "20.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Leaving Early 23",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 10 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 10 days, A completes 10/20 of the work.\nRemaining work = 1 - 10/20 = 0.50.\nB finishes remaining work in 0.50 \u00d7 30 = 15 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "18.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Leaving Early 24",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 10 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 10 days, A completes 10/20 of the work.\nRemaining work = 1 - 10/20 = 0.50.\nB finishes remaining work in 0.50 \u00d7 30 = 15 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "20.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "12.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Leaving Early 25",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 5 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 5 days, A completes 5/20 of the work.\nRemaining work = 1 - 5/20 = 0.75.\nB finishes remaining work in 0.75 \u00d7 30 = 22.5 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "25.5 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "27.5 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "19.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "22.5 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Leaving Early 26",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 8 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 8 days, A completes 8/20 of the work.\nRemaining work = 1 - 8/20 = 0.60.\nB finishes remaining work in 0.60 \u00d7 30 = 18 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "18 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "21.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "23.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Leaving Early 27",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 8 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 8 days, A completes 8/20 of the work.\nRemaining work = 1 - 8/20 = 0.60.\nB finishes remaining work in 0.60 \u00d7 30 = 18 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "15.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "23.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "18 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "21.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Leaving Early 28",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 8 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 8 days, A completes 8/20 of the work.\nRemaining work = 1 - 8/20 = 0.60.\nB finishes remaining work in 0.60 \u00d7 30 = 18 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "21.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "23.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "18 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Leaving Early 29",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 10 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 10 days, A completes 10/20 of the work.\nRemaining work = 1 - 10/20 = 0.50.\nB finishes remaining work in 0.50 \u00d7 30 = 15 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "18.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "12.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Leaving Early 30",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 5 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 5 days, A completes 5/20 of the work.\nRemaining work = 1 - 5/20 = 0.75.\nB finishes remaining work in 0.75 \u00d7 30 = 22.5 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "22.5 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "19.5 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "27.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Leaving Early 31",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 5 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 5 days, A completes 5/20 of the work.\nRemaining work = 1 - 5/20 = 0.75.\nB finishes remaining work in 0.75 \u00d7 30 = 22.5 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "25.5 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22.5 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "27.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Leaving Early 32",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 5 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 5 days, A completes 5/20 of the work.\nRemaining work = 1 - 5/20 = 0.75.\nB finishes remaining work in 0.75 \u00d7 30 = 22.5 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "27.5 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "19.5 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22.5 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "25.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Leaving Early 33",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 8 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 8 days, A completes 8/20 of the work.\nRemaining work = 1 - 8/20 = 0.60.\nB finishes remaining work in 0.60 \u00d7 30 = 18 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "21.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "18 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "23.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Leaving Early 34",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 5 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 5 days, A completes 5/20 of the work.\nRemaining work = 1 - 5/20 = 0.75.\nB finishes remaining work in 0.75 \u00d7 30 = 22.5 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "27.5 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "22.5 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "25.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Leaving Early 35",
        "difficulty": "Medium",
        "question_text": "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 5 days. In how many more days will B alone complete the remaining work?",
        "sample_answer": "In 5 days, A completes 5/20 of the work.\nRemaining work = 1 - 5/20 = 0.75.\nB finishes remaining work in 0.75 \u00d7 30 = 22.5 days.",
        "tips": "Remaining Work = 1 - Work already done. Days = Remaining Work / Individual Rate.",
        "options": [
            {
                "label": "A",
                "text": "27.5 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "19.5 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22.5 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "25.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 36",
        "difficulty": "Medium",
        "question_text": "If 16 workers can build a wall in 20 days, in how many days can 24 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 16 \u00d7 20 = 320 man-days.\nRequired days = Total Work / M2 = 320 / 24 = 13.3 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "11.3 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.3 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15.3 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13.3 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 37",
        "difficulty": "Medium",
        "question_text": "If 15 workers can build a wall in 10 days, in how many days can 24 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 15 \u00d7 10 = 150 man-days.\nRequired days = Total Work / M2 = 150 / 24 = 6.2 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "6.2 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "10.2 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "4.2 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8.2 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 38",
        "difficulty": "Medium",
        "question_text": "If 16 workers can build a wall in 20 days, in how many days can 8 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 16 \u00d7 20 = 320 man-days.\nRequired days = Total Work / M2 = 320 / 8 = 40 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "40 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "42.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "38.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "44.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 39",
        "difficulty": "Medium",
        "question_text": "If 12 workers can build a wall in 10 days, in how many days can 8 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 12 \u00d7 10 = 120 man-days.\nRequired days = Total Work / M2 = 120 / 8 = 15 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "19.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "17.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 40",
        "difficulty": "Medium",
        "question_text": "If 12 workers can build a wall in 10 days, in how many days can 8 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 12 \u00d7 10 = 120 man-days.\nRequired days = Total Work / M2 = 120 / 8 = 15 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "19.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "13.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 41",
        "difficulty": "Medium",
        "question_text": "If 15 workers can build a wall in 15 days, in how many days can 8 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 15 \u00d7 15 = 225 man-days.\nRequired days = Total Work / M2 = 225 / 8 = 28.1 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "32.1 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.1 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26.1 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28.1 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 42",
        "difficulty": "Medium",
        "question_text": "If 15 workers can build a wall in 10 days, in how many days can 10 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 15 \u00d7 10 = 150 man-days.\nRequired days = Total Work / M2 = 150 / 10 = 15 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "15 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "19.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 43",
        "difficulty": "Medium",
        "question_text": "If 25 workers can build a wall in 10 days, in how many days can 10 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 25 \u00d7 10 = 250 man-days.\nRequired days = Total Work / M2 = 250 / 10 = 25 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "27.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "29.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "23.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 44",
        "difficulty": "Medium",
        "question_text": "If 16 workers can build a wall in 12 days, in how many days can 8 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 16 \u00d7 12 = 192 man-days.\nRequired days = Total Work / M2 = 192 / 8 = 24 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "24 days",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "22.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 45",
        "difficulty": "Medium",
        "question_text": "If 20 workers can build a wall in 10 days, in how many days can 24 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 20 \u00d7 10 = 200 man-days.\nRequired days = Total Work / M2 = 200 / 24 = 8.3 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "10.3 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.3 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "8.3 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "12.3 days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 46",
        "difficulty": "Medium",
        "question_text": "If 20 workers can build a wall in 10 days, in how many days can 8 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 20 \u00d7 10 = 200 man-days.\nRequired days = Total Work / M2 = 200 / 8 = 25 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "27.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "23.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "29.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25 days",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 47",
        "difficulty": "Medium",
        "question_text": "If 12 workers can build a wall in 15 days, in how many days can 24 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 12 \u00d7 15 = 180 man-days.\nRequired days = Total Work / M2 = 180 / 24 = 7.5 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "9.5 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7.5 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "5.5 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11.5 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 48",
        "difficulty": "Medium",
        "question_text": "If 16 workers can build a wall in 15 days, in how many days can 8 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 16 \u00d7 15 = 240 man-days.\nRequired days = Total Work / M2 = 240 / 8 = 30 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "32.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28.0 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34.0 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 49",
        "difficulty": "Medium",
        "question_text": "If 12 workers can build a wall in 10 days, in how many days can 18 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 12 \u00d7 10 = 120 man-days.\nRequired days = Total Work / M2 = 120 / 18 = 6.7 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "10.7 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6.7 days",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8.7 days",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "4.7 days",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Time & Work - Man-Days Equivalence 50",
        "difficulty": "Medium",
        "question_text": "If 16 workers can build a wall in 15 days, in how many days can 24 workers build the same wall working at the same pace?",
        "sample_answer": "Total work = M1 \u00d7 D1 = 16 \u00d7 15 = 240 man-days.\nRequired days = Total Work / M2 = 240 / 24 = 10 days.",
        "tips": "Use formula: M1 * D1 = M2 * D2.",
        "options": [
            {
                "label": "A",
                "text": "14.0 days",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8.0 days",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10 days",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "12.0 days",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Time & Work').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Time & Work').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Time-Based Problems',
                    topic='Time & Work',
                    title=q.get('title', 'Time & Work'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Time & Work via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Time & Work: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Time & Work',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Time-Based Problems', 'Time & Work',
                        q.get('title', 'Time & Work'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Time & Work into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
