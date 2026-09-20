"""
Seed script for Coding & Decoding (Logical Reasoning)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Coding & Decoding - Letter Shift 1",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'LIGHT'?",
        "sample_answer": "Shifting every letter in 'LIGHT' forward by 1 places in the alphabet gives 'MJHIU'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "MJHIZ",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "MJHIU",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "XJHIU",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "MJHAB",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 2",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'SMART'?",
        "sample_answer": "Shifting every letter in 'SMART' forward by 2 places in the alphabet gives 'UOCTV'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "UOCTZ",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "UOCTV",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "UOCAB",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "XOCTV",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 3",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'BRAIN'?",
        "sample_answer": "Shifting every letter in 'BRAIN' forward by 1 places in the alphabet gives 'CSBJO'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "CSBAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "CSBJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "XSBJO",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "CSBJZ",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 4",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'CLOUD'?",
        "sample_answer": "Shifting every letter in 'CLOUD' forward by 2 places in the alphabet gives 'ENQWF'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "ENQAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "ENQWF",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "XNQWF",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "ENQWZ",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 5",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'POWER'?",
        "sample_answer": "Shifting every letter in 'POWER' forward by 1 places in the alphabet gives 'QPXFS'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "XPXFS",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "QPXAB",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "QPXFZ",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "QPXFS",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Letter Shift 6",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'TRAIN'?",
        "sample_answer": "Shifting every letter in 'TRAIN' forward by 2 places in the alphabet gives 'VTCKP'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "VTCAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "VTCKZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "VTCKP",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "XTCKP",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding - Letter Shift 7",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'APPLE'?",
        "sample_answer": "Shifting every letter in 'APPLE' forward by 1 places in the alphabet gives 'BQQMF'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "XQQMF",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "BQQMZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "BQQAB",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "BQQMF",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Letter Shift 8",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'RIVER'?",
        "sample_answer": "Shifting every letter in 'RIVER' forward by 2 places in the alphabet gives 'TKXGT'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "TKXGZ",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "TKXGT",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "XKXGT",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "TKXAB",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 9",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'EARTH'?",
        "sample_answer": "Shifting every letter in 'EARTH' forward by 1 places in the alphabet gives 'FBSUI'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "FBSUI",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "FBSAB",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "FBSUZ",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "XBSUI",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Letter Shift 10",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'STORM'?",
        "sample_answer": "Shifting every letter in 'STORM' forward by 2 places in the alphabet gives 'UVQTO'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "UVQTO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "XVQTO",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "UVQTZ",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "UVQAB",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Letter Shift 11",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'FLASH'?",
        "sample_answer": "Shifting every letter in 'FLASH' forward by 1 places in the alphabet gives 'GMBTI'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "GMBTI",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "XMBTI",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "GMBAB",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "GMBTZ",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Letter Shift 12",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'DREAM'?",
        "sample_answer": "Shifting every letter in 'DREAM' forward by 2 places in the alphabet gives 'FTGCO'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "FTGAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "XTGCO",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "FTGCO",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "FTGCZ",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding - Letter Shift 13",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'PLANT'?",
        "sample_answer": "Shifting every letter in 'PLANT' forward by 1 places in the alphabet gives 'QMBOU'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "XMBOU",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "QMBOU",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "QMBAB",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "QMBOZ",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 14",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'SOLAR'?",
        "sample_answer": "Shifting every letter in 'SOLAR' forward by 2 places in the alphabet gives 'UQNCT'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "UQNAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "UQNCT",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "UQNCZ",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "XQNCT",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 15",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'MUSIC'?",
        "sample_answer": "Shifting every letter in 'MUSIC' forward by 1 places in the alphabet gives 'NVTJD'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "NVTJZ",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "NVTAB",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "XVTJD",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "NVTJD",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Letter Shift 16",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'WATER'?",
        "sample_answer": "Shifting every letter in 'WATER' forward by 2 places in the alphabet gives 'YCVGT'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "YCVAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "YCVGZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "YCVGT",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "XCVGT",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding - Letter Shift 17",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'SPACE'?",
        "sample_answer": "Shifting every letter in 'SPACE' forward by 1 places in the alphabet gives 'TQBDF'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "TQBDF",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "TQBDZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "TQBAB",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "XQBDF",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Letter Shift 18",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'STONE'?",
        "sample_answer": "Shifting every letter in 'STONE' forward by 2 places in the alphabet gives 'UVQPG'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "UVQPG",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "UVQPZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "XVQPG",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "UVQAB",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Letter Shift 19",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'SHINE'?",
        "sample_answer": "Shifting every letter in 'SHINE' forward by 1 places in the alphabet gives 'TIJOF'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "TIJAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "TIJOZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "XIJOF",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "TIJOF",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Letter Shift 20",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'GUIDE'?",
        "sample_answer": "Shifting every letter in 'GUIDE' forward by 2 places in the alphabet gives 'IWKFG'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "IWKAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "XWKFG",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "IWKFG",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "IWKFZ",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding - Letter Shift 21",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'MAGIC'?",
        "sample_answer": "Shifting every letter in 'MAGIC' forward by 1 places in the alphabet gives 'NBHJD'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "NBHJZ",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "NBHJD",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "XBHJD",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "NBHAB",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 22",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'TIGER'?",
        "sample_answer": "Shifting every letter in 'TIGER' forward by 2 places in the alphabet gives 'VKIGT'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "VKIAB",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "VKIGZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "XKIGT",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "VKIGT",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Letter Shift 23",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'HONEY'?",
        "sample_answer": "Shifting every letter in 'HONEY' forward by 1 places in the alphabet gives 'IPOFZ'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "IPOFZ",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "XPOFZ",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "IPOAB",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Letter Shift 24",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +2 positions, what is the code for the word 'CHAIR'?",
        "sample_answer": "Shifting every letter in 'CHAIR' forward by 2 places in the alphabet gives 'EJCKT'.",
        "tips": "Shift every letter by +2.",
        "options": [
            {
                "label": "A",
                "text": "EJCKZ",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJCKT",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "XJCKT",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EJCAB",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Letter Shift 25",
        "difficulty": "Easy",
        "question_text": "In a certain code language, if each letter is shifted by +1 positions, what is the code for the word 'TABLE'?",
        "sample_answer": "Shifting every letter in 'TABLE' forward by 1 places in the alphabet gives 'UBCMF'.",
        "tips": "Shift every letter by +1.",
        "options": [
            {
                "label": "A",
                "text": "UBCMF",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "UBCMZ",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "UBCAB",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "XBCMF",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 26",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
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
                "text": "30",
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
        "title": "Coding & Decoding - Word Code Equivalent 27",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "28",
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
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 28",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 29",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 30",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
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
        "title": "Coding & Decoding - Word Code Equivalent 31",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "28",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 32",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 33",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "24",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 34",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28",
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
        "title": "Coding & Decoding - Word Code Equivalent 35",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "24",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 36",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 37",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 38",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 39",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 40",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 41",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
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
                "text": "24",
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
        "title": "Coding & Decoding - Word Code Equivalent 42",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28",
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
        "title": "Coding & Decoding - Word Code Equivalent 43",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
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
        "title": "Coding & Decoding - Word Code Equivalent 44",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 45",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 46",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 47",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding - Word Code Equivalent 48",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
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
        "title": "Coding & Decoding - Word Code Equivalent 49",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26",
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
        "title": "Coding & Decoding - Word Code Equivalent 50",
        "difficulty": "Medium",
        "question_text": "If 'CAT' is coded as 24 (since C=3, A=1, T=20, 3+1+20=24), how will 'DOG' be coded?",
        "sample_answer": "D = 4, O = 15, G = 7.\nSum of alphabet positional values = 4 + 15 + 7 = 26.",
        "tips": "Sum the alphabetical position values (A=1, B=2, ..., Z=26).",
        "options": [
            {
                "label": "A",
                "text": "24",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Coding & Decoding').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Coding & Decoding').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Logical Reasoning',
                    topic='Coding & Decoding',
                    title=q.get('title', 'Coding & Decoding'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Coding & Decoding via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Coding & Decoding: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Coding & Decoding',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Logical Reasoning', 'Coding & Decoding',
                        q.get('title', 'Coding & Decoding'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Coding & Decoding into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
