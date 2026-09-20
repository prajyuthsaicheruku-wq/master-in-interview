"""
Seed script for Averages (Number & Arithmetic)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Averages - 5 Consecutive Integers 1",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 14 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 14 + (5-1)/2 = 16.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "15",
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
                "text": "17",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - 5 Consecutive Integers 2",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 20 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 20 + (5-1)/2 = 22.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
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
                "text": "24",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "21",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - 5 Consecutive Integers 3",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 35 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 35 + (5-1)/2 = 37.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
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
                "text": "37",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "38",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - 9 Consecutive Integers 4",
        "difficulty": "Easy",
        "question_text": "The average of 9 consecutive integers starting from 27 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 27 + (9-1)/2 = 31.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "31",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "32",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "33",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - 7 Consecutive Integers 5",
        "difficulty": "Easy",
        "question_text": "The average of 7 consecutive integers starting from 44 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 44 + (7-1)/2 = 47.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "46",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "49",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "47",
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
        "title": "Averages - 5 Consecutive Integers 6",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 14 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 14 + (5-1)/2 = 16.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
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
                "text": "16",
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
        "title": "Averages - 5 Consecutive Integers 7",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 32 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 32 + (5-1)/2 = 34.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "33",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "34",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "36",
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
        "title": "Averages - 7 Consecutive Integers 8",
        "difficulty": "Easy",
        "question_text": "The average of 7 consecutive integers starting from 27 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 27 + (7-1)/2 = 30.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "31",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "29",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - 5 Consecutive Integers 9",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 28 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 28 + (5-1)/2 = 30.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "29",
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
                "text": "32",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - 7 Consecutive Integers 10",
        "difficulty": "Easy",
        "question_text": "The average of 7 consecutive integers starting from 36 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 36 + (7-1)/2 = 39.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "39",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "38",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "41",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - 7 Consecutive Integers 11",
        "difficulty": "Easy",
        "question_text": "The average of 7 consecutive integers starting from 34 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 34 + (7-1)/2 = 37.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "38",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "39",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "37",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - 5 Consecutive Integers 12",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 32 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 32 + (5-1)/2 = 34.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "33",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34",
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
        "title": "Averages - 9 Consecutive Integers 13",
        "difficulty": "Easy",
        "question_text": "The average of 9 consecutive integers starting from 49 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 49 + (9-1)/2 = 53.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "53",
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
                "text": "55",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - 5 Consecutive Integers 14",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 35 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 35 + (5-1)/2 = 37.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
        "options": [
            {
                "label": "A",
                "text": "39",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "37",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "38",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - 5 Consecutive Integers 15",
        "difficulty": "Easy",
        "question_text": "The average of 5 consecutive integers starting from 30 is:",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle term: 30 + (5-1)/2 = 32.",
        "tips": "The average of consecutive numbers in AP is always the middle number.",
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
                "text": "32",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "33",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - New Group Member Weight 16",
        "difficulty": "Medium",
        "question_text": "The average weight of 15 students is 28 kg. If a new student joins, the average weight changes by -1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 15 \u00d7 28 = 420.\nNew total = 16 \u00d7 27 = 432.\nNew student's weight = New total - Old total = 12 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "12 kg",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "9 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17 kg",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - New Group Member Weight 17",
        "difficulty": "Medium",
        "question_text": "The average weight of 9 students is 20 kg. If a new student joins, the average weight changes by -1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 9 \u00d7 20 = 180.\nNew total = 10 \u00d7 19 = 190.\nNew student's weight = New total - Old total = 10 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "7 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "13 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - New Group Member Weight 18",
        "difficulty": "Medium",
        "question_text": "The average weight of 8 students is 27 kg. If a new student joins, the average weight changes by -2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 8 \u00d7 27 = 216.\nNew total = 9 \u00d7 25 = 225.\nNew student's weight = New total - Old total = 9 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "6 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "9 kg",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - New Group Member Weight 19",
        "difficulty": "Medium",
        "question_text": "The average weight of 9 students is 28 kg. If a new student joins, the average weight changes by 2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 9 \u00d7 28 = 252.\nNew total = 10 \u00d7 30 = 300.\nNew student's weight = New total - Old total = 48 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "45 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "53 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "51 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - New Group Member Weight 20",
        "difficulty": "Medium",
        "question_text": "The average weight of 13 students is 20 kg. If a new student joins, the average weight changes by -1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 13 \u00d7 20 = 260.\nNew total = 14 \u00d7 19 = 266.\nNew student's weight = New total - Old total = 6 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "9 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6 kg",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "3 kg",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - New Group Member Weight 21",
        "difficulty": "Medium",
        "question_text": "The average weight of 8 students is 32 kg. If a new student joins, the average weight changes by -1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 8 \u00d7 32 = 256.\nNew total = 9 \u00d7 31 = 279.\nNew student's weight = New total - Old total = 23 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "23 kg",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "28 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26 kg",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - New Group Member Weight 22",
        "difficulty": "Medium",
        "question_text": "The average weight of 11 students is 30 kg. If a new student joins, the average weight changes by -2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 11 \u00d7 30 = 330.\nNew total = 12 \u00d7 28 = 336.\nNew student's weight = New total - Old total = 6 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "9 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "6 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "3 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - New Group Member Weight 23",
        "difficulty": "Medium",
        "question_text": "The average weight of 15 students is 35 kg. If a new student joins, the average weight changes by -2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 15 \u00d7 35 = 525.\nNew total = 16 \u00d7 33 = 528.\nNew student's weight = New total - Old total = 3 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "6 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "3 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "8 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "0 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - New Group Member Weight 24",
        "difficulty": "Medium",
        "question_text": "The average weight of 12 students is 22 kg. If a new student joins, the average weight changes by -1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 12 \u00d7 22 = 264.\nNew total = 13 \u00d7 21 = 273.\nNew student's weight = New total - Old total = 9 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "9 kg",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "14 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "6 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 kg",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - New Group Member Weight 25",
        "difficulty": "Medium",
        "question_text": "The average weight of 10 students is 20 kg. If a new student joins, the average weight changes by 1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 10 \u00d7 20 = 200.\nNew total = 11 \u00d7 21 = 231.\nNew student's weight = New total - Old total = 31 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "31 kg",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "36 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28 kg",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - New Group Member Weight 26",
        "difficulty": "Medium",
        "question_text": "The average weight of 12 students is 27 kg. If a new student joins, the average weight changes by 2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 12 \u00d7 27 = 324.\nNew total = 13 \u00d7 29 = 377.\nNew student's weight = New total - Old total = 53 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "56 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "53 kg",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "58 kg",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - New Group Member Weight 27",
        "difficulty": "Medium",
        "question_text": "The average weight of 14 students is 28 kg. If a new student joins, the average weight changes by 2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 14 \u00d7 28 = 392.\nNew total = 15 \u00d7 30 = 450.\nNew student's weight = New total - Old total = 58 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "55 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "58 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "61 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "63 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - New Group Member Weight 28",
        "difficulty": "Medium",
        "question_text": "The average weight of 15 students is 23 kg. If a new student joins, the average weight changes by 1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 15 \u00d7 23 = 345.\nNew total = 16 \u00d7 24 = 384.\nNew student's weight = New total - Old total = 39 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "44 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "42 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "39 kg",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - New Group Member Weight 29",
        "difficulty": "Medium",
        "question_text": "The average weight of 9 students is 30 kg. If a new student joins, the average weight changes by 2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 9 \u00d7 30 = 270.\nNew total = 10 \u00d7 32 = 320.\nNew student's weight = New total - Old total = 50 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "50 kg",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "47 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "55 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "53 kg",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - New Group Member Weight 30",
        "difficulty": "Medium",
        "question_text": "The average weight of 11 students is 20 kg. If a new student joins, the average weight changes by -2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 11 \u00d7 20 = 220.\nNew total = 12 \u00d7 18 = 216.\nNew student's weight = New total - Old total = -4 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "-1 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "-7 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "1 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "-4 kg",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - New Group Member Weight 31",
        "difficulty": "Medium",
        "question_text": "The average weight of 13 students is 25 kg. If a new student joins, the average weight changes by 1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 13 \u00d7 25 = 325.\nNew total = 14 \u00d7 26 = 364.\nNew student's weight = New total - Old total = 39 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "42 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "39 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "36 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "44 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - New Group Member Weight 32",
        "difficulty": "Medium",
        "question_text": "The average weight of 11 students is 26 kg. If a new student joins, the average weight changes by 1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 11 \u00d7 26 = 286.\nNew total = 12 \u00d7 27 = 324.\nNew student's weight = New total - Old total = 38 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "38 kg",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "35 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "43 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "41 kg",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - New Group Member Weight 33",
        "difficulty": "Medium",
        "question_text": "The average weight of 13 students is 32 kg. If a new student joins, the average weight changes by 2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 13 \u00d7 32 = 416.\nNew total = 14 \u00d7 34 = 476.\nNew student's weight = New total - Old total = 60 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "65 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "57 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "63 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - New Group Member Weight 34",
        "difficulty": "Medium",
        "question_text": "The average weight of 14 students is 20 kg. If a new student joins, the average weight changes by 2 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 14 \u00d7 20 = 280.\nNew total = 15 \u00d7 22 = 330.\nNew student's weight = New total - Old total = 50 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "50 kg",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "47 kg",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "53 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "55 kg",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - New Group Member Weight 35",
        "difficulty": "Medium",
        "question_text": "The average weight of 8 students is 22 kg. If a new student joins, the average weight changes by -1 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 8 \u00d7 22 = 176.\nNew total = 9 \u00d7 21 = 189.\nNew student's weight = New total - Old total = 13 kg.",
        "tips": "New Value = New Average + (Old Count * Change in Average).",
        "options": [
            {
                "label": "A",
                "text": "18 kg",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13 kg",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "10 kg",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "16 kg",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Round Trip Average Speed 36",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 60 km/h and returns from town B to town A at 80 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 60 \u00d7 80) / (60 + 80) = 68.6 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "70.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "72.6 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "64.6 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "68.6 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - Round Trip Average Speed 37",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 40 km/h and returns from town B to town A at 80 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 40 \u00d7 80) / (40 + 80) = 53.3 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "49.3 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "57.3 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "53.3 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - Round Trip Average Speed 38",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 30 km/h and returns from town B to town A at 120 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 30 \u00d7 120) / (30 + 120) = 48.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "44.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "48.0 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "52.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "75.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Round Trip Average Speed 39",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 30 km/h and returns from town B to town A at 80 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 30 \u00d7 80) / (30 + 80) = 43.6 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "55.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "47.6 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "39.6 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "43.6 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - Round Trip Average Speed 40",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 60 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 60 \u00d7 60) / (60 + 60) = 60.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "64.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60.0 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "56.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Round Trip Average Speed 41",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 40 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 40 \u00d7 60) / (40 + 60) = 48.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "52.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "44.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "48.0 km/h",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - Round Trip Average Speed 42",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 60 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 60 \u00d7 60) / (60 + 60) = 60.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "64.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60.0 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "56.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Round Trip Average Speed 43",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 60 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 60 \u00d7 60) / (60 + 60) = 60.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "60.0 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "56.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "64.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - Round Trip Average Speed 44",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 30 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 30 \u00d7 60) / (30 + 60) = 40.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "36.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "45.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "40.0 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "44.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Round Trip Average Speed 45",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 60 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 60 \u00d7 60) / (60 + 60) = 60.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60.0 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "56.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "64.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Round Trip Average Speed 46",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 60 km/h and returns from town B to town A at 120 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 60 \u00d7 120) / (60 + 120) = 80.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "80.0 km/h",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "90.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "84.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "76.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - Round Trip Average Speed 47",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 40 km/h and returns from town B to town A at 120 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 40 \u00d7 120) / (40 + 120) = 60.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "64.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60.0 km/h",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "80.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "56.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Round Trip Average Speed 48",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 40 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 40 \u00d7 60) / (40 + 60) = 48.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "52.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "50.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48.0 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "44.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Round Trip Average Speed 49",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 30 km/h and returns from town B to town A at 120 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 30 \u00d7 120) / (30 + 120) = 48.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "52.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "44.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "48.0 km/h",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "75.0 km/h",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Round Trip Average Speed 50",
        "difficulty": "Medium",
        "question_text": "A car travels from town A to town B at 30 km/h and returns from town B to town A at 60 km/h. What is the average speed of the car for the entire journey?",
        "sample_answer": "Average speed for equal distances = (2 \u00d7 S1 \u00d7 S2) / (S1 + S2) = (2 \u00d7 30 \u00d7 60) / (30 + 60) = 40.0 km/h.",
        "tips": "Harmonic mean formula: 2xy / (x + y).",
        "options": [
            {
                "label": "A",
                "text": "36.0 km/h",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "44.0 km/h",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "45.0 km/h",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40.0 km/h",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Averages').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Averages').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Number & Arithmetic',
                    topic='Averages',
                    title=q.get('title', 'Averages'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Averages via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Averages: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Averages',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Number & Arithmetic', 'Averages',
                        q.get('title', 'Averages'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Averages into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
