import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- POINTING BASED BLOOD RELATIONS (Q1 - Q10) ---
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "Pointing to a man, Ravi said, \"He is the son of my father's only son.\" How is the man related to Ravi?",
        "sample_answer": "Ravi's father's only son = Ravi himself.\nThe man is the son of Ravi.\nRelationship: Son.",
        "tips": "'My father's only son' refers to Ravi himself.",
        "options": [
            {"label": "A", "text": "Brother", "is_correct": False},
            {"label": "B", "text": "Son", "is_correct": True},
            {"label": "C", "text": "Nephew", "is_correct": False},
            {"label": "D", "text": "Father", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "A woman introduces a boy as \"He is the son of the daughter of my mother.\" How is the boy related to the woman?",
        "sample_answer": "Daughter of my mother = The woman herself (or her sister).\nSon of the daughter = Her Son.",
        "tips": "Daughter of mother is the woman herself.",
        "options": [
            {"label": "A", "text": "Nephew", "is_correct": False},
            {"label": "B", "text": "Son", "is_correct": True},
            {"label": "C", "text": "Brother", "is_correct": False},
            {"label": "D", "text": "Cousin", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "Pointing to a girl, Arun said, \"She is the daughter of my grandfather's only son.\" How is the girl related to Arun?",
        "sample_answer": "Arun's grandfather's only son = Arun's father.\nDaughter of Arun's father = Sister.",
        "tips": "Grandfather's only son is father.",
        "options": [
            {"label": "A", "text": "Sister", "is_correct": True},
            {"label": "B", "text": "Cousin", "is_correct": False},
            {"label": "C", "text": "Niece", "is_correct": False},
            {"label": "D", "text": "Mother", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "A man said, \"My mother's brother is the brother of your father.\" How is the man related to you?",
        "sample_answer": "Man's mother's brother = Maternal Uncle.\nMaternal Uncle is brother of your father → Man is your Cousin.",
        "tips": "Trace maternal uncle to father's brother.",
        "options": [
            {"label": "A", "text": "Uncle", "is_correct": False},
            {"label": "B", "text": "Cousin", "is_correct": True},
            {"label": "C", "text": "Brother", "is_correct": False},
            {"label": "D", "text": "Father", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "Pointing to a photograph, Raj said, \"The lady in the photograph is the daughter of my grandfather's only child.\" Who is the lady?",
        "sample_answer": "Grandfather's only child = Raj's father.\nDaughter of Raj's father = Sister.",
        "tips": "Grandfather's only child = Father.",
        "options": [
            {"label": "A", "text": "Sister", "is_correct": True},
            {"label": "B", "text": "Mother", "is_correct": False},
            {"label": "C", "text": "Cousin", "is_correct": False},
            {"label": "D", "text": "Daughter", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "A is the brother of B. B is the sister of C. How is A related to C?",
        "sample_answer": "A is male (brother), B is female (sister). All three are siblings.\nA is the Brother of C.",
        "tips": "A is male and sibling of C.",
        "options": [
            {"label": "A", "text": "Sister", "is_correct": False},
            {"label": "B", "text": "Brother", "is_correct": True},
            {"label": "C", "text": "Cousin", "is_correct": False},
            {"label": "D", "text": "Father", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "P is the father of Q. Q is the mother of R. How is P related to R?",
        "sample_answer": "P (male) → Q (female, mother) → R.\nP is R's mother's father = Grandfather.",
        "tips": "Mother's father = Grandfather.",
        "options": [
            {"label": "A", "text": "Father", "is_correct": False},
            {"label": "B", "text": "Grandfather", "is_correct": True},
            {"label": "C", "text": "Uncle", "is_correct": False},
            {"label": "D", "text": "Brother", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "X is the sister of Y. Y is the father of Z. How is X related to Z?",
        "sample_answer": "X is sister of father Y → X is Aunt.",
        "tips": "Father's sister = Aunt.",
        "options": [
            {"label": "A", "text": "Mother", "is_correct": False},
            {"label": "B", "text": "Aunt", "is_correct": True},
            {"label": "C", "text": "Sister", "is_correct": False},
            {"label": "D", "text": "Grandmother", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "A woman says, \"The father of my son is the son of your grandfather.\" How is the woman related to you?",
        "sample_answer": "Father of woman's son = Husband.\nHusband = Son of your grandfather = Your Father.\nHence, woman is your Mother.",
        "tips": "Father of son = Husband = Your Father → Woman is Mother.",
        "options": [
            {"label": "A", "text": "Sister", "is_correct": False},
            {"label": "B", "text": "Mother", "is_correct": True},
            {"label": "C", "text": "Aunt", "is_correct": False},
            {"label": "D", "text": "Daughter", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Medium",
        "question_text": "Pointing to a man, Sita said, \"His mother is the only daughter of my mother.\" How is the man related to Sita?",
        "sample_answer": "Only daughter of Sita's mother = Sita herself.\nHis mother = Sita → Man is Sita's Son.",
        "tips": "Only daughter of mother = Sita.",
        "options": [
            {"label": "A", "text": "Brother", "is_correct": False},
            {"label": "B", "text": "Son", "is_correct": True},
            {"label": "C", "text": "Nephew", "is_correct": False},
            {"label": "D", "text": "Father", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- HARD LEVEL (Q11 - Q20) ---
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A man introduces a woman as \"She is the wife of the grandson of my mother.\" How is the woman related to the man?",
        "sample_answer": "Grandson of my mother = Man's son.\nWife of man's son = Daughter-in-law.",
        "tips": "Grandson of mother = Son.",
        "options": [
            {"label": "A", "text": "Daughter", "is_correct": False},
            {"label": "B", "text": "Daughter-in-law", "is_correct": True},
            {"label": "C", "text": "Sister-in-law", "is_correct": False},
            {"label": "D", "text": "Wife", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "Pointing to a boy, Ramesh said, \"He is the son of the daughter of the father of my wife.\" How is the boy related to Ramesh?",
        "sample_answer": "Father of wife = Father-in-law.\nDaughter of father-in-law = Ramesh's wife.\nSon of Ramesh's wife = Son.",
        "tips": "Father of wife's daughter = Wife.",
        "options": [
            {"label": "A", "text": "Son", "is_correct": True},
            {"label": "B", "text": "Nephew", "is_correct": False},
            {"label": "C", "text": "Brother", "is_correct": False},
            {"label": "D", "text": "Cousin", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A woman said, \"The only son of my father's father is the father of my son.\" How is the woman related to the son?",
        "sample_answer": "The woman is the Mother of the son.",
        "tips": "Direct parent relationship.",
        "options": [
            {"label": "A", "text": "Mother", "is_correct": True},
            {"label": "B", "text": "Sister", "is_correct": False},
            {"label": "C", "text": "Daughter", "is_correct": False},
            {"label": "D", "text": "Aunt", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "P is the father of Q, R is the mother of S, Q is married to R, and S is the daughter of T. How is T related to P?",
        "sample_answer": "R is mother of S, S is daughter of T → T and R are parents. Since R is mother, T = Q (husband).\nT (Q) is the Son of P.",
        "tips": "T is Q, who is the son of P.",
        "options": [
            {"label": "A", "text": "Son", "is_correct": True},
            {"label": "B", "text": "Father", "is_correct": False},
            {"label": "C", "text": "Brother", "is_correct": False},
            {"label": "D", "text": "Son-in-law", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A man said, \"My brother's father is your grandfather.\" How is the man related to you?",
        "sample_answer": "Man's brother's father = Man's Father.\nMan's father is your grandfather → Man is your Uncle (or Father).",
        "tips": "Brother's father = Father = Your grandfather → Uncle.",
        "options": [
            {"label": "A", "text": "Father", "is_correct": False},
            {"label": "B", "text": "Uncle", "is_correct": True},
            {"label": "C", "text": "Brother", "is_correct": False},
            {"label": "D", "text": "Grandfather", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "Introducing a woman, Mohan said, \"She is the daughter of the only daughter of my mother.\" How is the woman related to Mohan?",
        "sample_answer": "Only daughter of Mohan's mother = Sister.\nDaughter of sister = Niece.",
        "tips": "Sister's daughter = Niece.",
        "options": [
            {"label": "A", "text": "Daughter", "is_correct": False},
            {"label": "B", "text": "Niece", "is_correct": True},
            {"label": "C", "text": "Sister", "is_correct": False},
            {"label": "D", "text": "Cousin", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "Pointing to a person, Rita said, \"His father is the son of my grandfather.\" How is the person related to Rita?",
        "sample_answer": "Son of grandfather = Father.\nPerson's father is Rita's father → Brother.",
        "tips": "Grandfather's son = Father → Brother.",
        "options": [
            {"label": "A", "text": "Brother", "is_correct": True},
            {"label": "B", "text": "Cousin", "is_correct": False},
            {"label": "C", "text": "Uncle", "is_correct": False},
            {"label": "D", "text": "Father", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A man said, \"The girl is the wife of the only son of my mother.\" How is the girl related to the man?",
        "sample_answer": "Only son of my mother = The man himself.\nWife of the man = Wife.",
        "tips": "Only son of mother = Himself.",
        "options": [
            {"label": "A", "text": "Sister", "is_correct": False},
            {"label": "B", "text": "Wife", "is_correct": True},
            {"label": "C", "text": "Sister-in-law", "is_correct": False},
            {"label": "D", "text": "Daughter", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "P is the father of Q. Q is the brother of R. R is married to S. How is S related to P?",
        "sample_answer": "P is father of R. S is married to R.\nS is the Daughter-in-law (or Son-in-law) of P.",
        "tips": "Child's spouse.",
        "options": [
            {"label": "A", "text": "Daughter-in-law", "is_correct": True},
            {"label": "B", "text": "Son-in-law", "is_correct": False},
            {"label": "C", "text": "Sister-in-law", "is_correct": False},
            {"label": "D", "text": "Mother", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A woman points to a boy and says, \"He is the son of the only daughter of my mother.\" How is the boy related to the woman?",
        "sample_answer": "Only daughter of my mother = Woman herself.\nSon of woman = Son.",
        "tips": "Only daughter of mother = Woman herself.",
        "options": [
            {"label": "A", "text": "Nephew", "is_correct": False},
            {"label": "B", "text": "Son", "is_correct": True},
            {"label": "C", "text": "Brother", "is_correct": False},
            {"label": "D", "text": "Cousin", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- FAMILY TREE BASED QUESTIONS (Q21 - Q25) ---
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A is B's father. B is C's sister. C is D's father. How is A related to D?",
        "sample_answer": "A is father of C. C is father of D.\nA is D's Grandfather.",
        "tips": "Father's father = Grandfather.",
        "options": [
            {"label": "A", "text": "Grandfather", "is_correct": True},
            {"label": "B", "text": "Father", "is_correct": False},
            {"label": "C", "text": "Uncle", "is_correct": False},
            {"label": "D", "text": "Great-Grandfather", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "P is Q's mother. Q is R's brother. R is S's mother. How is P related to S?",
        "sample_answer": "P is mother of R. R is mother of S.\nP is S's Grandmother.",
        "tips": "Mother's mother = Grandmother.",
        "options": [
            {"label": "A", "text": "Mother", "is_correct": False},
            {"label": "B", "text": "Grandmother", "is_correct": True},
            {"label": "C", "text": "Aunt", "is_correct": False},
            {"label": "D", "text": "Sister", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "M is the father of N. N is the mother of O. O is married to P. How is M related to P?",
        "sample_answer": "M is grandfather of O. O is spouse of P.\nM is Grandfather-in-law of P.",
        "tips": "Spouse's grandfather = Grandfather-in-law.",
        "options": [
            {"label": "A", "text": "Grandfather", "is_correct": False},
            {"label": "B", "text": "Father-in-law", "is_correct": False},
            {"label": "C", "text": "Grandfather-in-law", "is_correct": True},
            {"label": "D", "text": "Uncle", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A is the son of B. B is married to C. C is the daughter of D. How is D related to A?",
        "sample_answer": "C is mother of A. D is parent of C.\nD is Grandparent of A.",
        "tips": "Mother's parent = Grandparent.",
        "options": [
            {"label": "A", "text": "Father", "is_correct": False},
            {"label": "B", "text": "Grandparent", "is_correct": True},
            {"label": "C", "text": "Uncle", "is_correct": False},
            {"label": "D", "text": "Brother", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "X is Y's brother. Y is Z's mother. How is X related to Z?",
        "sample_answer": "X is brother of mother Y.\nX is Z's Uncle.",
        "tips": "Mother's brother = Uncle.",
        "options": [
            {"label": "A", "text": "Uncle", "is_correct": True},
            {"label": "B", "text": "Father", "is_correct": False},
            {"label": "C", "text": "Brother", "is_correct": False},
            {"label": "D", "text": "Cousin", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- PLACEMENT LEVEL BLOOD RELATIONS (Q26 - Q30) ---
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "Pointing to a photograph, a man said, \"I have no brother or sister, but that man's father is my father's son.\" Who is in the photograph?",
        "sample_answer": "'My father's son' = Himself.\n'That man's father' = Himself → The photograph is of his Son.",
        "tips": "Father's son (only child) = Himself.",
        "options": [
            {"label": "A", "text": "Himself", "is_correct": False},
            {"label": "B", "text": "His Son", "is_correct": True},
            {"label": "C", "text": "His Father", "is_correct": False},
            {"label": "D", "text": "His Nephew", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A woman said, \"The son of my brother's father is my nephew.\" How is the woman related to the nephew?",
        "sample_answer": "Brother's father = Father.\nFather's son = Brother.\nBrother's son = Nephew → Woman is Aunt.",
        "tips": "Nephew's father is her brother.",
        "options": [
            {"label": "A", "text": "Mother", "is_correct": False},
            {"label": "B", "text": "Aunt", "is_correct": True},
            {"label": "C", "text": "Sister", "is_correct": False},
            {"label": "D", "text": "Grandmother", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "Pointing to a girl, Ravi said, \"She is the daughter of the only child of my mother.\" How is the girl related to Ravi?",
        "sample_answer": "Only child of my mother = Ravi.\nDaughter of Ravi = Daughter.",
        "tips": "Only child of mother = Himself.",
        "options": [
            {"label": "A", "text": "Sister", "is_correct": False},
            {"label": "B", "text": "Daughter", "is_correct": True},
            {"label": "C", "text": "Niece", "is_correct": False},
            {"label": "D", "text": "Cousin", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "A man introduced a woman as, \"Her mother's husband is the son of my grandfather.\" How is the woman related to the man?",
        "sample_answer": "Mother's husband = Father.\nSon of my grandfather = Father.\nWoman's father is man's father → Sister.",
        "tips": "Shared father = Sister.",
        "options": [
            {"label": "A", "text": "Sister", "is_correct": True},
            {"label": "B", "text": "Mother", "is_correct": False},
            {"label": "C", "text": "Daughter", "is_correct": False},
            {"label": "D", "text": "Aunt", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Blood Relations",
        "difficulty": "Hard",
        "question_text": "Pointing to a person, Suresh said, \"His father's mother is my mother's mother.\" How is the person related to Suresh?",
        "sample_answer": "Mother's mother = Maternal Grandmother.\nPerson's father's mother = Paternal Grandmother.\nPaternal & Maternal grandmothers match → Suresh and person are Cousins.",
        "tips": "Shared grandmother = Cousin.",
        "options": [
            {"label": "A", "text": "Brother", "is_correct": False},
            {"label": "B", "text": "Cousin", "is_correct": True},
            {"label": "C", "text": "Nephew", "is_correct": False},
            {"label": "D", "text": "Uncle", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_blood_relations():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Blood Relations'")
            print(f"Deleted old 'Blood Relations' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Logical Reasoning',
                    'Blood Relations',
                    q['title'],
                    q['difficulty'],
                    q['question_text'],
                    q['sample_answer'],
                    q['tips'],
                    json.dumps(q['options']),
                    q['correct_option'],
                    json.dumps({
                        'options': q['options'],
                        'correct_option': q['correct_option']
                    })
                ))
                inserted_count += 1

            conn.commit()
            conn.close()
            print(f"Successfully inserted {inserted_count} questions into {db_path}.")
        except Exception as e:
            print(f"Skipping {db_path}: {e}")

if __name__ == '__main__':
    seed_blood_relations()
