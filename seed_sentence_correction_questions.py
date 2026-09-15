import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- SUBJECT-VERB & TENSE CORRECTION (Q1 - Q10) ---
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "Third person singular subject 'He' requires 'does not' followed by the base verb 'like'.",
        "tips": "He/She/It + does not + base verb.",
        "options": [
            {"label": "A", "text": "He do not like coffee.", "is_correct": False},
            {"label": "B", "text": "He does not likes coffee.", "is_correct": False},
            {"label": "C", "text": "He does not like coffee.", "is_correct": True},
            {"label": "D", "text": "He not likes coffee.", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "Subject 'She' takes auxiliary 'has' for present perfect tense ('has completed').",
        "tips": "She + has + past participle (V3).",
        "options": [
            {"label": "A", "text": "She have completed her work.", "is_correct": False},
            {"label": "B", "text": "She has completed her work.", "is_correct": True},
            {"label": "C", "text": "She had completes her work.", "is_correct": False},
            {"label": "D", "text": "She completed has her work.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "'Neither of + plural noun' takes a singular verb ('is').",
        "tips": "Neither of + plural noun -> singular verb.",
        "options": [
            {"label": "A", "text": "Neither of the boys are present.", "is_correct": False},
            {"label": "B", "text": "Neither of the boys is present.", "is_correct": True},
            {"label": "C", "text": "Neither boys are present.", "is_correct": False},
            {"label": "D", "text": "Neither boys is present.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "'News' is an uncountable singular noun requiring singular verb 'is'.",
        "tips": "News is always singular.",
        "options": [
            {"label": "A", "text": "The news are interesting.", "is_correct": False},
            {"label": "B", "text": "The news is interesting.", "is_correct": True},
            {"label": "C", "text": "The news were interesting.", "is_correct": False},
            {"label": "D", "text": "The news have interesting.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "Academic subject names ending in '-s' (Mathematics) take singular verb 'is'.",
        "tips": "Subject names take singular verb.",
        "options": [
            {"label": "A", "text": "Mathematics are my favorite subject.", "is_correct": False},
            {"label": "B", "text": "Mathematics is my favorite subject.", "is_correct": True},
            {"label": "C", "text": "Mathematics were my favorite subject.", "is_correct": False},
            {"label": "D", "text": "Mathematics have my favorite subject.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Find the error: \"Each of the students have submitted their assignment.\"",
        "sample_answer": "'Each of + plural noun' requires singular verb 'has' instead of 'have'.",
        "tips": "Each of requires a singular verb.",
        "options": [
            {"label": "A", "text": "Each", "is_correct": False},
            {"label": "B", "text": "students", "is_correct": False},
            {"label": "C", "text": "have", "is_correct": True},
            {"label": "D", "text": "assignment", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Find the correct sentence:",
        "sample_answer": "Comparative adjectives ending in '-ior' (senior, junior) take preposition 'to'.",
        "tips": "Senior is followed by 'to'.",
        "options": [
            {"label": "A", "text": "She is senior than me.", "is_correct": False},
            {"label": "B", "text": "She is senior to me.", "is_correct": True},
            {"label": "C", "text": "She is senior from me.", "is_correct": False},
            {"label": "D", "text": "She is senior over me.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "'One of + plural noun' takes a singular verb ('One of my friends is...').",
        "tips": "One of + plural noun + singular verb.",
        "options": [
            {"label": "A", "text": "One of my friend is a doctor.", "is_correct": False},
            {"label": "B", "text": "One of my friends is a doctor.", "is_correct": True},
            {"label": "C", "text": "One of my friends are a doctor.", "is_correct": False},
            {"label": "D", "text": "One my friends is a doctor.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "The verb 'prefer' takes preposition 'to' when expressing preference.",
        "tips": "Prefer X to Y.",
        "options": [
            {"label": "A", "text": "I prefer tea than coffee.", "is_correct": False},
            {"label": "B", "text": "I prefer tea to coffee.", "is_correct": True},
            {"label": "C", "text": "I prefer tea over coffee than.", "is_correct": False},
            {"label": "D", "text": "I prefer tea with coffee.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Medium",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "Expressing skill or proficiency requires preposition 'at' ('good at Mathematics').",
        "tips": "Good at + subject/activity.",
        "options": [
            {"label": "A", "text": "He is good in Mathematics.", "is_correct": False},
            {"label": "B", "text": "He is good at Mathematics.", "is_correct": True},
            {"label": "C", "text": "He is good on Mathematics.", "is_correct": False},
            {"label": "D", "text": "He is good with Mathematics.", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- HARD LEVEL (Q11 - Q20) ---
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "Inverted third conditional: 'Had + subject + V3 (known) ..., would have + V3 (told)'.",
        "tips": "Had I known ..., I would have told you.",
        "options": [
            {"label": "A", "text": "Had I knew the answer, I would tell you.", "is_correct": False},
            {"label": "B", "text": "Had I known the answer, I would have told you.", "is_correct": True},
            {"label": "C", "text": "Had I know the answer, I would tell you.", "is_correct": False},
            {"label": "D", "text": "Had I knowing the answer, I would told you.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "Correlative conjunction pair is 'No sooner had ... than'.",
        "tips": "No sooner ... than.",
        "options": [
            {"label": "A", "text": "No sooner had he arrived when it started raining.", "is_correct": False},
            {"label": "B", "text": "No sooner had he arrived than it started raining.", "is_correct": True},
            {"label": "C", "text": "No sooner he arrived than it started raining.", "is_correct": False},
            {"label": "D", "text": "No sooner had he arrived then it started raining.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "Correlative conjunction pair with inversion is 'Hardly had ... when'.",
        "tips": "Hardly had ... when.",
        "options": [
            {"label": "A", "text": "Hardly had I reached the station when the train left.", "is_correct": True},
            {"label": "B", "text": "Hardly I reached the station when the train left.", "is_correct": False},
            {"label": "C", "text": "Hardly had I reached the station than the train left.", "is_correct": False},
            {"label": "D", "text": "Hardly I had reached the station than the train left.", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "Correlative conjunction pair is 'Scarcely had ... when'.",
        "tips": "Scarcely had ... when.",
        "options": [
            {"label": "A", "text": "Scarcely had he entered than the meeting began.", "is_correct": False},
            {"label": "B", "text": "Scarcely had he entered when the meeting began.", "is_correct": True},
            {"label": "C", "text": "Scarcely he entered when the meeting began.", "is_correct": False},
            {"label": "D", "text": "Scarcely entered he when the meeting began.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "Subjunctive mood for unreal present condition requires 'were' ('If I were rich...').",
        "tips": "Subjunctive conditional takes 'were'.",
        "options": [
            {"label": "A", "text": "If I was rich, I would buy a yacht.", "is_correct": False},
            {"label": "B", "text": "If I were rich, I would buy a yacht.", "is_correct": True},
            {"label": "C", "text": "If I am rich, I would buy a yacht.", "is_correct": False},
            {"label": "D", "text": "If I be rich, I would buy a yacht.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Select the correct sentence:",
        "sample_answer": "With 'Neither ... nor', the verb agrees with the closer subject ('employees' -> 'are').",
        "tips": "Proximity rule in neither/nor.",
        "options": [
            {"label": "A", "text": "Neither the manager nor the employees is willing.", "is_correct": False},
            {"label": "B", "text": "Neither the manager nor the employees are willing.", "is_correct": True},
            {"label": "C", "text": "Neither the manager nor the employees has willing.", "is_correct": False},
            {"label": "D", "text": "Neither the manager nor employees is willing.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "'Either of + plural noun' takes a singular verb ('is').",
        "tips": "Either of + plural noun -> singular verb.",
        "options": [
            {"label": "A", "text": "Either of the answers are correct.", "is_correct": False},
            {"label": "B", "text": "Either of the answers is correct.", "is_correct": True},
            {"label": "C", "text": "Either answers are correct.", "is_correct": False},
            {"label": "D", "text": "Either answer are correct.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "When members of a collective noun ('committee') express divided opinions, a plural verb ('are') and plural pronoun ('their') are used.",
        "tips": "Divided collective noun takes plural verb and pronoun.",
        "options": [
            {"label": "A", "text": "The committee are divided in their opinion.", "is_correct": True},
            {"label": "B", "text": "The committee is divided in its opinion.", "is_correct": False},
            {"label": "C", "text": "The committee were divided in its opinion.", "is_correct": False},
            {"label": "D", "text": "The committee have divided in its opinion.", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct sentence:",
        "sample_answer": "With 'Not only ... but also', the verb agrees with the subject closest to it ('teacher' -> 'was').",
        "tips": "Proximity rule for not only/but also.",
        "options": [
            {"label": "A", "text": "Not only the students but also the teacher were present.", "is_correct": False},
            {"label": "B", "text": "Not only the students but also the teacher was present.", "is_correct": True},
            {"label": "C", "text": "Not only students but teacher were present.", "is_correct": False},
            {"label": "D", "text": "Not only students but also teacher were present.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Identify the correct sentence:",
        "sample_answer": "Relative pronoun 'who' refers to plural antecedent 'boys', requiring plural verb 'were selected'. Main clause verb remains 'is'.",
        "tips": "Relative clause verb agrees with antecedent 'boys'.",
        "options": [
            {"label": "A", "text": "One of the boys who was selected is my friend.", "is_correct": False},
            {"label": "B", "text": "One of the boys who were selected is my friend.", "is_correct": True},
            {"label": "C", "text": "One of the boys who is selected is my friend.", "is_correct": False},
            {"label": "D", "text": "One of the boys selected are my friend.", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- PLACEMENT-LEVEL & INVERSIONS (Q21 - Q30) ---
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct phrase: \"The company _____ operations globally next year.\"",
        "sample_answer": "The verb 'plans' is followed by the to-infinitive ('to expand').",
        "tips": "Plan + to + infinitive.",
        "options": [
            {"label": "A", "text": "plans expanding", "is_correct": False},
            {"label": "B", "text": "plans to expand", "is_correct": True},
            {"label": "C", "text": "plan to expanding", "is_correct": False},
            {"label": "D", "text": "planned expand", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct phrase: \"The report contains information _____ for all employees.\"",
        "sample_answer": "'Information' is uncountable singular; relative clause 'that is useful' correctly modifies it.",
        "tips": "Information is singular.",
        "options": [
            {"label": "A", "text": "contains information which are useful", "is_correct": False},
            {"label": "B", "text": "contains information that is useful", "is_correct": True},
            {"label": "C", "text": "contain information that useful", "is_correct": False},
            {"label": "D", "text": "contains informations that are useful", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct phrase: \"_____, the match continued as scheduled.\"",
        "sample_answer": "'Despite' functions as a preposition on its own and does not take 'of'.",
        "tips": "Despite + noun phrase (no 'of').",
        "options": [
            {"label": "A", "text": "Despite heavy rain", "is_correct": True},
            {"label": "B", "text": "Despite of the heavy rain", "is_correct": False},
            {"label": "C", "text": "In spite heavy rain", "is_correct": False},
            {"label": "D", "text": "Despite the heavily rain", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct phrase: \"The manager, along with his team members, _____ the meeting.\"",
        "sample_answer": "Phrases like 'along with' do not change the subject number. Singular 'manager' takes 'was attending'.",
        "tips": "Parenthetical phrase 'along with' does not affect singular subject.",
        "options": [
            {"label": "A", "text": "were attending", "is_correct": False},
            {"label": "B", "text": "was attending", "is_correct": True},
            {"label": "C", "text": "have attended", "is_correct": False},
            {"label": "D", "text": "attending", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Choose the correct phrase: \"Every student in the class _____ the assignment.\"",
        "sample_answer": "'Every + singular noun' takes a singular verb ('has submitted').",
        "tips": "Every + singular noun -> singular verb.",
        "options": [
            {"label": "A", "text": "have submitted", "is_correct": False},
            {"label": "B", "text": "has submitted", "is_correct": True},
            {"label": "C", "text": "had submit", "is_correct": False},
            {"label": "D", "text": "submit", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Seldom _____ such a talented employee.",
        "sample_answer": "Negative adverb 'Seldom' placed at sentence start triggers subject-auxiliary inversion ('have I seen').",
        "tips": "Seldom + auxiliary + subject + verb.",
        "options": [
            {"label": "A", "text": "I have seen", "is_correct": False},
            {"label": "B", "text": "have I seen", "is_correct": True},
            {"label": "C", "text": "I saw", "is_correct": False},
            {"label": "D", "text": "seen I have", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Only after the presentation _____ the importance of communication.",
        "sample_answer": "'Only after...' at sentence start triggers inversion in the main clause ('did he realize').",
        "tips": "Only after + clause + auxiliary + subject + verb.",
        "options": [
            {"label": "A", "text": "did he realize", "is_correct": True},
            {"label": "B", "text": "he realized", "is_correct": False},
            {"label": "C", "text": "realized he", "is_correct": False},
            {"label": "D", "text": "he did realize", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Little _____ that his decision would change his career.",
        "sample_answer": "Negative adverb 'Little' at sentence start requires inversion ('did he know').",
        "tips": "Little + did + subject + base verb.",
        "options": [
            {"label": "A", "text": "he knew", "is_correct": False},
            {"label": "B", "text": "did he know", "is_correct": True},
            {"label": "C", "text": "knew he", "is_correct": False},
            {"label": "D", "text": "he know", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Rarely _____ such dedication among employees.",
        "sample_answer": "Negative adverb 'Rarely' at sentence start triggers subject-auxiliary inversion ('do we see').",
        "tips": "Rarely + do + subject + verb.",
        "options": [
            {"label": "A", "text": "we see", "is_correct": False},
            {"label": "B", "text": "do we see", "is_correct": True},
            {"label": "C", "text": "we saw", "is_correct": False},
            {"label": "D", "text": "saw we", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction",
        "difficulty": "Hard",
        "question_text": "Not until the deadline approached _____ the project.",
        "sample_answer": "'Not until...' at sentence start triggers inversion in the main clause ('did they complete').",
        "tips": "Not until + clause + auxiliary + subject + verb.",
        "options": [
            {"label": "A", "text": "they completed", "is_correct": False},
            {"label": "B", "text": "did they complete", "is_correct": True},
            {"label": "C", "text": "they complete", "is_correct": False},
            {"label": "D", "text": "completed they", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_sentence_correction():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Sentence Correction'")
            print(f"Deleted old 'Sentence Correction' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Verbal Ability',
                    'Sentence Correction',
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
    seed_sentence_correction()
