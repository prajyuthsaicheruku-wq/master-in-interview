"""
Seed script for Grammar (Verbal Ability)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Grammar Rule 1",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nNeither the teacher nor the students ______ present in the auditorium yesterday.",
        "sample_answer": "When subjects are joined by 'neither... nor', the verb agrees with the nearer subject ('students' is plural).",
        "tips": "Check subject closer to the verb.",
        "options": [
            {
                "label": "A",
                "text": "is",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "were",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "are",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "was",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 2",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe quality of these mangoes ______ not satisfactory.",
        "sample_answer": "The subject is 'quality' (singular, uncountable noun), not 'mangoes'.",
        "tips": "Subject is 'quality', not the plural prepositional object.",
        "options": [
            {
                "label": "A",
                "text": "were",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "is",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "have been",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "are",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 3",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nEach of the candidates ______ required to bring their original certificates.",
        "sample_answer": "'Each' is an indefinite pronoun that takes a singular verb.",
        "tips": "'Each of' always takes a singular verb.",
        "options": [
            {
                "label": "A",
                "text": "were",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "have been",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "is",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "are",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 4",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nA bouquet of yellow roses ______ gifted to the chief guest.",
        "sample_answer": "The subject is 'bouquet' (singular), not 'roses'.",
        "tips": "Head noun is 'bouquet'.",
        "options": [
            {
                "label": "A",
                "text": "are",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "were",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "was",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "have been",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 5",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nBread and butter ______ his favorite breakfast.",
        "sample_answer": "When two singular nouns express a single unified idea or dish, they take a singular verb.",
        "tips": "Bread and butter forms one collective meal concept.",
        "options": [
            {
                "label": "A",
                "text": "are",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "have",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "is",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "were",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 6",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nTen miles ______ a long distance to walk on foot.",
        "sample_answer": "A specific distance, amount, or time considered as a single unit takes a singular verb.",
        "tips": "Measurements of distance take singular verbs.",
        "options": [
            {
                "label": "A",
                "text": "were",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "are",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "have been",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "is",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Grammar Rule 7",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nEither Rahul or his brothers ______ attending the reception.",
        "sample_answer": "With 'either... or', the verb agrees with the subject closer to it ('brothers' is plural).",
        "tips": "Verb matches the plural noun 'brothers'.",
        "options": [
            {
                "label": "A",
                "text": "has",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "are",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "was",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "is",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 8",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe committee ______ divided in their opinions regarding the new proposal.",
        "sample_answer": "When members of a collective noun act individually or disagree, a plural verb is used.",
        "tips": "Divided opinions indicate individual members acting separately.",
        "options": [
            {
                "label": "A",
                "text": "is",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "were",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "was",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "has been",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 9",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nOne of my friends ______ a software architect at a tech firm.",
        "sample_answer": "'One of + plural noun' takes a singular verb agreeing with 'One'.",
        "tips": "The subject is 'One'.",
        "options": [
            {
                "label": "A",
                "text": "have",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "is",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "were",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "are",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 10",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nPhysics ______ an interesting subject for many students.",
        "sample_answer": "Names of subjects ending in 's' (physics, mathematics) are singular.",
        "tips": "Academic subjects are singular.",
        "options": [
            {
                "label": "A",
                "text": "is",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "have been",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "are",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "were",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 11",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nBy the time we arrived at the station, the express train ______.",
        "sample_answer": "Use Past Perfect ('had left') for an action completed before another past action ('arrived').",
        "tips": "Past action occurring before another past action takes past perfect.",
        "options": [
            {
                "label": "A",
                "text": "had already left",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "has already left",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "already left",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "was leaving",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 12",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHe ______ here for more than ten years now.",
        "sample_answer": "Use Present Perfect Continuous for an action that started in the past and continues into the present.",
        "tips": "Ongoing action with 'for ten years' requires present perfect continuous.",
        "options": [
            {
                "label": "A",
                "text": "lived",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "has been living",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "was living",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "is living",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 13",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nIf it rains this evening, we ______ our football match.",
        "sample_answer": "First Conditional: 'If + Present Simple' is followed by 'will + base verb'.",
        "tips": "First conditional structure: If + present, will + verb.",
        "options": [
            {
                "label": "A",
                "text": "cancelled",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "would have cancelled",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "will cancel",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "would cancel",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 14",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nI wish I ______ more time to practice coding algorithms.",
        "sample_answer": "Use past subjunctive 'had' to express a hypothetical or unreal wish in the present.",
        "tips": "Wishes in the present take past simple.",
        "options": [
            {
                "label": "A",
                "text": "had",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "will have",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "have",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "would have",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 15",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe sun ______ in the east and sets in the west.",
        "sample_answer": "Universal truths and habitual actions are expressed in the Simple Present tense.",
        "tips": "Universal scientific truth.",
        "options": [
            {
                "label": "A",
                "text": "is rising",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "rose",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "rises",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "has risen",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 16",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nWhen I saw him yesterday, he ______ a newspaper in the library.",
        "sample_answer": "Past Continuous indicates an action in progress at a specific moment in the past.",
        "tips": "Past action in progress.",
        "options": [
            {
                "label": "A",
                "text": "was reading",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "has read",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "is reading",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "reads",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 17",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nBy next December, she ______ her doctoral dissertation.",
        "sample_answer": "Future Perfect ('will have completed') is used for an action that will be finished by a specified future time.",
        "tips": "Look for 'By next [time]' signaling future perfect.",
        "options": [
            {
                "label": "A",
                "text": "will complete",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "completes",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "would complete",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "will have completed",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Grammar Rule 18",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nI haven't seen him ______ last Monday.",
        "sample_answer": "Use 'since' with a specific point in time (last Monday) with perfect tenses.",
        "tips": "'Since' marks the starting point in time.",
        "options": [
            {
                "label": "A",
                "text": "for",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "since",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "from",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "during",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 19",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nShe waited at the bus stop ______ forty-five minutes.",
        "sample_answer": "Use 'for' to denote a duration or period of time.",
        "tips": "'For' indicates a duration.",
        "options": [
            {
                "label": "A",
                "text": "since",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "until",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "for",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "from",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 20",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nScarcely had the bell rung when the students ______ out of the classroom.",
        "sample_answer": "'Scarcely had... when' is followed by the simple past tense.",
        "tips": "Correlative conjunction scarcely had... when + simple past.",
        "options": [
            {
                "label": "A",
                "text": "run",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "had run",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "ran",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "running",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 21",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe manager congratulated the engineer ______ completing the project ahead of schedule.",
        "sample_answer": "The verb 'congratulate' takes the preposition 'on'.",
        "tips": "Congratulate someone 'on' an achievement.",
        "options": [
            {
                "label": "A",
                "text": "for",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "at",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "with",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "on",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Grammar Rule 22",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nShe is extremely proficient ______ speaking German and French.",
        "sample_answer": "'Proficient' is followed by the preposition 'in'.",
        "tips": "Proficient 'in' a language or skill.",
        "options": [
            {
                "label": "A",
                "text": "at",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "for",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "with",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "in",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Grammar Rule 23",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHe prevented the child ______ touching the hot kettle.",
        "sample_answer": "The verb 'prevent' takes 'from + gerund'.",
        "tips": "Prevent someone 'from' doing something.",
        "options": [
            {
                "label": "A",
                "text": "from",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "to",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "for",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "against",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 24",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe patient is slowly recovering ______ a severe bout of pneumonia.",
        "sample_answer": "The verb 'recover' pairs with 'from'.",
        "tips": "Recover 'from' an illness.",
        "options": [
            {
                "label": "A",
                "text": "with",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "off",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "from",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "of",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 25",
        "difficulty": "Easy",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHe is very good ______ solving complex logical puzzles.",
        "sample_answer": "Use 'good at' when referring to skills, talents, or abilities.",
        "tips": "Good 'at' an activity.",
        "options": [
            {
                "label": "A",
                "text": "for",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "at",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "in",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "with",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 26",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nAre you familiar ______ the guidelines issued by the council?",
        "sample_answer": "'Familiar with' means having knowledge or acquaintance of something.",
        "tips": "Familiar 'with' rules or people.",
        "options": [
            {
                "label": "A",
                "text": "to",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "about",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "with",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "at",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 27",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe principal abstained ______ casting his vote in the election.",
        "sample_answer": "The verb 'abstain' takes the preposition 'from'.",
        "tips": "Abstain 'from' doing something.",
        "options": [
            {
                "label": "A",
                "text": "against",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "with",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "from",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "to",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 28",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nWe should adhere ______ the safety protocols at all times.",
        "sample_answer": "'Adhere' takes the preposition 'to' (meaning follow or stick to).",
        "tips": "Adhere 'to' a rule.",
        "options": [
            {
                "label": "A",
                "text": "by",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "for",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "to",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "with",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 29",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe company complies ______ all environmental regulations.",
        "sample_answer": "'Comply' is always paired with 'with'.",
        "tips": "Comply 'with' regulations.",
        "options": [
            {
                "label": "A",
                "text": "to",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "by",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "at",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "with",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Grammar Rule 30",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHe was accused ______ forging the financial documents.",
        "sample_answer": "'Accused' takes the preposition 'of'.",
        "tips": "Accused 'of' a crime.",
        "options": [
            {
                "label": "A",
                "text": "of",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "for",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "about",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "with",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 31",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHonesty is ______ best policy.",
        "sample_answer": "Superlative adjectives ('best') require the definite article 'the'.",
        "tips": "Superlative adjectives take 'the'.",
        "options": [
            {
                "label": "A",
                "text": "an",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "a",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "the",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "no article",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 32",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHe is ______ European citizen working in Bengaluru.",
        "sample_answer": "'European' starts with a consonant sound (/ju\u02d0/), so 'a' is used instead of 'an'.",
        "tips": "Article choice depends on phonetic vowel sound, not just written vowel.",
        "options": [
            {
                "label": "A",
                "text": "a",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "an",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "no article",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "the",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 33",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nShe returned home after ______ hour of intense workout.",
        "sample_answer": "'Hour' starts with a vowel sound (silent 'h'), so 'an' is appropriate.",
        "tips": "'Hour' begins with a vowel sound.",
        "options": [
            {
                "label": "A",
                "text": "a",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "an",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "no article",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "the",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 34",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\n______ higher you climb, the colder it gets.",
        "sample_answer": "Parallel comparative structures use 'The + comparative..., the + comparative...'.",
        "tips": "Double comparative structure: The more... the more...",
        "options": [
            {
                "label": "A",
                "text": "A",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "The",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "More",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "An",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 35",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHe gave me ______ useful piece of advice yesterday.",
        "sample_answer": "'Useful' starts with a consonant 'y' sound (/ju\u02d0/), hence 'a useful'.",
        "tips": "'Useful' begins with a consonant sound.",
        "options": [
            {
                "label": "A",
                "text": "a",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "no article",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "an",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "the",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 36",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nBetween you and ______, this business proposal seems unviable.",
        "sample_answer": "Prepositions ('between') are followed by objective case pronouns ('me', not 'I').",
        "tips": "Between takes objective case pronouns.",
        "options": [
            {
                "label": "A",
                "text": "me",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "myself",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "I",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "we",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 37",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nThe man ______ car was vandalized called the police immediately.",
        "sample_answer": "'Whose' is the possessive relative pronoun modifying 'car'.",
        "tips": "Possessive relative pronoun is 'whose'.",
        "options": [
            {
                "label": "A",
                "text": "whose",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "who",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "which",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "whom",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 38",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nYou ______ not worry about the transport; company buses are provided.",
        "sample_answer": "'Need not' expresses lack of obligation or necessity.",
        "tips": "'Need not' indicates absence of necessity.",
        "options": [
            {
                "label": "A",
                "text": "ought",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "must",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "need",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "shall",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 39",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nWalk carefully lest you ______ stumble on the rocky path.",
        "sample_answer": "'Lest' is traditionally followed by 'should' (meaning 'for fear that').",
        "tips": "'Lest' pairs with 'should'.",
        "options": [
            {
                "label": "A",
                "text": "would",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "shall",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "might",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "should",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Grammar Rule 40",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nHardly had she entered the room ______ the lights flickered and went out.",
        "sample_answer": "'Hardly' takes the correlative conjunction 'when'.",
        "tips": "Hardly... when, No sooner... than.",
        "options": [
            {
                "label": "A",
                "text": "then",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "when",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "after",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "than",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 41",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nNo sooner did the bell ring ______ the students packed their bags.",
        "sample_answer": "'No sooner' is followed by 'than'.",
        "tips": "No sooner pairs with 'than'.",
        "options": [
            {
                "label": "A",
                "text": "then",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "when",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "than",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "since",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 42",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nShe is as tall as, if not taller than, ______.",
        "sample_answer": "In formal comparative constructions, subjective case 'I' is standard (as tall as I am).",
        "tips": "Comparison of subjects uses subjective case.",
        "options": [
            {
                "label": "A",
                "text": "myself",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "I",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "mine",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "me",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 43",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nNeither the coach nor the players ______ satisfied with the referee's call.",
        "sample_answer": "Verb agrees with the nearer plural subject 'players'.",
        "tips": "Agreement with nearer subject.",
        "options": [
            {
                "label": "A",
                "text": "is",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "were",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "has been",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "was",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 44",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nAlthough it was raining heavily, ______ he went for his morning jog.",
        "sample_answer": "'Although' can be followed by 'yet' or a simple comma, never by 'but'.",
        "tips": "Although pairs with yet (or comma), not but.",
        "options": [
            {
                "label": "A",
                "text": "but",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "yet",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "and",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "so",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 45",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nEvery student and every teacher ______ invited to the annual function.",
        "sample_answer": "Nouns preceded by 'every' take a singular verb even when joined by 'and'.",
        "tips": "'Every' takes singular verbs.",
        "options": [
            {
                "label": "A",
                "text": "was",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "have been",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "were",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "are",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 46",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nChoose the correct passive voice: 'The chef cooked a lavish dinner.'",
        "sample_answer": "Simple past active ('cooked') transforms to 'was/were + past participle' ('was cooked').",
        "tips": "Simple past active -> was/were + V3.",
        "options": [
            {
                "label": "A",
                "text": "A lavish dinner was cooked by the chef.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "A lavish dinner is cooked by the chef.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "A lavish dinner has been cooked by the chef.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "A lavish dinner was being cooked by the chef.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar Rule 47",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nChoose the correct passive voice: 'They are constructing a new highway.'",
        "sample_answer": "Present continuous active changes to 'is/are + being + past participle'.",
        "tips": "Continuous active -> being + V3.",
        "options": [
            {
                "label": "A",
                "text": "A new highway was constructed by them.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "A new highway has been constructed by them.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "A new highway is being constructed by them.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "A new highway is constructed by them.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 48",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nChoose the correct passive voice: 'Who wrote this famous novel?'",
        "sample_answer": "'Who' changes to 'By whom' followed by auxiliary verb 'was' + subject + V3.",
        "tips": "Who -> By whom + aux + subject + V3.",
        "options": [
            {
                "label": "A",
                "text": "By who was this novel written?",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "By whom was this famous novel written?",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Who was this famous novel written by?",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "By whom this famous novel was written?",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar Rule 49",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nChoose the correct indirect speech: He said, 'I am feeling unwell today.'",
        "sample_answer": "Present continuous ('am feeling') shifts to past continuous ('was feeling'), and 'today' changes to 'that day'.",
        "tips": "Tense shift and adverb change (today -> that day).",
        "options": [
            {
                "label": "A",
                "text": "He said that he is feeling unwell today.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He said that he had been feeling unwell that day.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He said that he was feeling unwell that day.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "He said that he was feeling unwell today.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar Rule 50",
        "difficulty": "Medium",
        "question_text": "Choose the correct option to complete the sentence grammatically:\n\nChoose the correct indirect speech: She said to me, 'Where do you live?'",
        "sample_answer": "In reported wh-questions, the sentence structure becomes affirmative: 'where + subject + verb'.",
        "tips": "Wh-question becomes affirmative clause in indirect speech.",
        "options": [
            {
                "label": "A",
                "text": "She asked where do I live.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "She asked me where I do live.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "She asked me where I lived.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "She asked me where did I live.",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Grammar').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Grammar').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Verbal Ability',
                    topic='Grammar',
                    title=q.get('title', 'Grammar'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Grammar via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Grammar: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Grammar',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Verbal Ability', 'Grammar',
                        q.get('title', 'Grammar'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Grammar into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
