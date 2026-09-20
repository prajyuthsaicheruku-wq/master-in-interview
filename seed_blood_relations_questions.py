"""
Seed script for Blood Relations (Logical Reasoning)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Blood Relations - Decipher Relationship 1",
        "difficulty": "Easy",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Grandmother",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 2",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Nephew",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Father or Brother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Cousin",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 3",
        "difficulty": "Easy",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Niece",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Aunt",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 4",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Priya Herself",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 5",
        "difficulty": "Easy",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Father",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 6",
        "difficulty": "Easy",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Aunt",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 7",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Nephew",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Cousin",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Father or Brother",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 8",
        "difficulty": "Easy",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Niece",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 9",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Priya Herself",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Mother-in-law",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 10",
        "difficulty": "Easy",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Father",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Brother-in-law",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 11",
        "difficulty": "Easy",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 12",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Father or Brother",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Nephew",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Cousin",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 13",
        "difficulty": "Easy",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Niece",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 14",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Priya Herself",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 15",
        "difficulty": "Easy",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Father",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 16",
        "difficulty": "Easy",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Aunt",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 17",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Cousin",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Father or Brother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Nephew",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 18",
        "difficulty": "Easy",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Niece",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 19",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Priya Herself",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 20",
        "difficulty": "Easy",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Father",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Uncle",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 21",
        "difficulty": "Easy",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Grandmother",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 22",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Nephew",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Cousin",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Father or Brother",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 23",
        "difficulty": "Easy",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Niece",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Aunt",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 24",
        "difficulty": "Easy",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Priya Herself",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Mother",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 25",
        "difficulty": "Easy",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Father",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Grandfather",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 26",
        "difficulty": "Medium",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 27",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Cousin",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Father or Brother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Nephew",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 28",
        "difficulty": "Medium",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Niece",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 29",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Priya Herself",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Mother-in-law",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 30",
        "difficulty": "Medium",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Father",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Brother-in-law",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 31",
        "difficulty": "Medium",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Mother",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 32",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Father or Brother",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Cousin",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Nephew",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 33",
        "difficulty": "Medium",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Niece",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 34",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Priya Herself",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 35",
        "difficulty": "Medium",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Father",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Grandfather",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 36",
        "difficulty": "Medium",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Aunt",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 37",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Cousin",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Nephew",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Father or Brother",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 38",
        "difficulty": "Medium",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Niece",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 39",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Priya Herself",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Mother",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 40",
        "difficulty": "Medium",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Father",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 41",
        "difficulty": "Medium",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 42",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Nephew",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Father or Brother",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Cousin",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 43",
        "difficulty": "Medium",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Niece",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 44",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Priya Herself",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Mother",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 45",
        "difficulty": "Medium",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Father",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 46",
        "difficulty": "Medium",
        "question_text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Mother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Grandmother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sister",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations - Decipher Relationship 47",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Rohan said, 'He is the son of the only son of my grandfather.' How is Rohan related to the boy?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Father or Brother.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Uncle",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Cousin",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Father or Brother",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Nephew",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations - Decipher Relationship 48",
        "difficulty": "Medium",
        "question_text": "Introducing a girl, Amit says, 'She is the daughter of the only son of my father.' How is the girl related to Amit?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Daughter.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Daughter",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Aunt",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Niece",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations - Decipher Relationship 49",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Priya said, 'She is the mother of the brother of my son.' How is the woman in the photograph related to Priya?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Priya Herself.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Mother",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Mother-in-law",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Sister",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Priya Herself",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Blood Relations - Decipher Relationship 50",
        "difficulty": "Medium",
        "question_text": "Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter\u2019s father.' How is the gentleman related to Deepak?",
        "sample_answer": "By breaking down the relationship step-by-step from the speaker's perspective, the answer is Uncle.",
        "tips": "Trace backward starting from 'my mother's only daughter' etc.",
        "options": [
            {
                "label": "A",
                "text": "Brother-in-law",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Grandfather",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Uncle",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Father",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Blood Relations').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Blood Relations').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Logical Reasoning',
                    topic='Blood Relations',
                    title=q.get('title', 'Blood Relations'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Blood Relations via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Blood Relations: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Blood Relations',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Logical Reasoning', 'Blood Relations',
                        q.get('title', 'Blood Relations'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Blood Relations into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
