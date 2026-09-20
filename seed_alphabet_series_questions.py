"""
Seed script for Alphabet Series (Logical Reasoning)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Alphabet Series - Letter Skip Progression 1",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: B, D, F, H, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = J.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "K",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "J",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "L",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "I",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 2",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: C, E, G, I, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = K.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "M",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "K",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "L",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "J",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 3",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: D, H, L, P, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = T.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "T",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "U",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "V",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 4",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: E, I, M, Q, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = U.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "W",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "T",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "V",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "U",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 5",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: A, C, E, G, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = I.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "H",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "I",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "K",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "J",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 6",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: B, D, F, H, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = J.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "K",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "I",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "J",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "L",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 7",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: C, E, G, I, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = K.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "L",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "J",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "M",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "K",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 8",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: D, G, J, M, ?",
        "sample_answer": "Each subsequent letter advances by +3 positions in the English alphabet.\nNext letter = P.",
        "tips": "Letter position advances by +3.",
        "options": [
            {
                "label": "A",
                "text": "Q",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "O",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 9",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: E, H, K, N, ?",
        "sample_answer": "Each subsequent letter advances by +3 positions in the English alphabet.\nNext letter = Q.",
        "tips": "Letter position advances by +3.",
        "options": [
            {
                "label": "A",
                "text": "Q",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "P",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 10",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: A, D, G, J, ?",
        "sample_answer": "Each subsequent letter advances by +3 positions in the English alphabet.\nNext letter = M.",
        "tips": "Letter position advances by +3.",
        "options": [
            {
                "label": "A",
                "text": "O",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "L",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "M",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "N",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 11",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: B, D, F, H, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = J.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "I",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "L",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "K",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "J",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 12",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: C, G, K, O, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = S.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "T",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "U",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "R",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 13",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: D, G, J, M, ?",
        "sample_answer": "Each subsequent letter advances by +3 positions in the English alphabet.\nNext letter = P.",
        "tips": "Letter position advances by +3.",
        "options": [
            {
                "label": "A",
                "text": "Q",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "O",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 14",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: E, G, I, K, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = M.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "M",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "L",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "O",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "N",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 15",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: A, C, E, G, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = I.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "J",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "I",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "K",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "H",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 16",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: B, E, H, K, ?",
        "sample_answer": "Each subsequent letter advances by +3 positions in the English alphabet.\nNext letter = N.",
        "tips": "Letter position advances by +3.",
        "options": [
            {
                "label": "A",
                "text": "P",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "N",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "O",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "M",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 17",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: C, G, K, O, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = S.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "T",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "U",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 18",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: D, H, L, P, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = T.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "T",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "V",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "U",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 19",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: E, I, M, Q, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = U.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "V",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "U",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "W",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "T",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 20",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: A, C, E, G, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = I.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "K",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "I",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "J",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "H",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 21",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: B, F, J, N, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = R.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "R",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Q",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "T",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 22",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: C, G, K, O, ?",
        "sample_answer": "Each subsequent letter advances by +4 positions in the English alphabet.\nNext letter = S.",
        "tips": "Letter position advances by +4.",
        "options": [
            {
                "label": "A",
                "text": "T",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "U",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "R",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 23",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: D, G, J, M, ?",
        "sample_answer": "Each subsequent letter advances by +3 positions in the English alphabet.\nNext letter = P.",
        "tips": "Letter position advances by +3.",
        "options": [
            {
                "label": "A",
                "text": "O",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Q",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 24",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: E, H, K, N, ?",
        "sample_answer": "Each subsequent letter advances by +3 positions in the English alphabet.\nNext letter = Q.",
        "tips": "Letter position advances by +3.",
        "options": [
            {
                "label": "A",
                "text": "Q",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "P",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Letter Skip Progression 25",
        "difficulty": "Easy",
        "question_text": "Find the next letter in the given sequence: A, C, E, G, ?",
        "sample_answer": "Each subsequent letter advances by +2 positions in the English alphabet.\nNext letter = I.",
        "tips": "Letter position advances by +2.",
        "options": [
            {
                "label": "A",
                "text": "J",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "K",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "I",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "H",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Cluster Progression 26",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EIP",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Cluster Progression 27",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Cluster Progression 28",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Cluster Progression 29",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 30",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 31",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 32",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Cluster Progression 33",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Cluster Progression 34",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EJO",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Alphabet Series - Cluster Progression 35",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Cluster Progression 36",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 37",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 38",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Cluster Progression 39",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EJO",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Alphabet Series - Cluster Progression 40",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EIP",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series - Cluster Progression 41",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 42",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 43",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 44",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "EIP",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 45",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Cluster Progression 46",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 47",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "FIN",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "EKO",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Cluster Progression 48",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series - Cluster Progression 49",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "FIN",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series - Cluster Progression 50",
        "difficulty": "Medium",
        "question_text": "What comes next in the letter series: BDF, CFI, DHL, ... ?",
        "sample_answer": "First letters: B (+1) -> C (+1) -> D (+1) -> E\nSecond letters: D (+2) -> F (+2) -> H (+2) -> J\nThird letters: F (+3) -> I (+3) -> L (+3) -> O\nResult = EJO.",
        "tips": "Analyze the shift for each position in the letter group independently.",
        "options": [
            {
                "label": "A",
                "text": "EKO",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "EIP",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "EJO",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "FIN",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Alphabet Series').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Alphabet Series').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Logical Reasoning',
                    topic='Alphabet Series',
                    title=q.get('title', 'Alphabet Series'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Alphabet Series via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Alphabet Series: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Alphabet Series',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Logical Reasoning', 'Alphabet Series',
                        q.get('title', 'Alphabet Series'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Alphabet Series into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
