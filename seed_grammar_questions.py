import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- SPOTTING ERRORS (Q1 - Q5) ---
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Identify the error in the sentence:\n\n\"Neither of the students have submitted the assignment.\"",
        "sample_answer": "'Neither of + plural noun' takes a singular verb. 'have' should be replaced with 'has'.",
        "tips": "Neither of + plural noun requires a singular verb.",
        "options": [
            {"label": "A", "text": "Neither", "is_correct": False},
            {"label": "B", "text": "students", "is_correct": False},
            {"label": "C", "text": "have", "is_correct": True},
            {"label": "D", "text": "assignment", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Identify the error in the sentence:\n\n\"Each of the players were given a certificate.\"",
        "sample_answer": "'Each of + plural noun' takes a singular verb. 'were' should be replaced with 'was'.",
        "tips": "Each of requires a singular verb.",
        "options": [
            {"label": "A", "text": "Each", "is_correct": False},
            {"label": "B", "text": "players", "is_correct": False},
            {"label": "C", "text": "were", "is_correct": True},
            {"label": "D", "text": "certificate", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Identify the error in the sentence:\n\n\"The quality of the products are excellent.\"",
        "sample_answer": "The subject is 'quality' (singular), not 'products'. The verb should be 'is' instead of 'are'.",
        "tips": "Subject-verb agreement: verb agrees with head noun 'quality'.",
        "options": [
            {"label": "A", "text": "quality", "is_correct": False},
            {"label": "B", "text": "products", "is_correct": False},
            {"label": "C", "text": "are", "is_correct": True},
            {"label": "D", "text": "excellent", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Identify the error in the sentence:\n\n\"One of my friends don't like coffee.\"",
        "sample_answer": "'One of my friends' is a singular subject. The verb should be 'doesn't' instead of 'don't'.",
        "tips": "One of + plural noun takes a singular verb (doesn't).",
        "options": [
            {"label": "A", "text": "One", "is_correct": False},
            {"label": "B", "text": "friends", "is_correct": False},
            {"label": "C", "text": "don't", "is_correct": True},
            {"label": "D", "text": "coffee", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Identify the error in the sentence:\n\n\"She is senior than me.\"",
        "sample_answer": "Adjectives ending in '-ior' (senior, junior, superior, inferior) are followed by 'to', not 'than'.",
        "tips": "Senior is followed by 'to' instead of 'than'.",
        "options": [
            {"label": "A", "text": "She", "is_correct": False},
            {"label": "B", "text": "is", "is_correct": False},
            {"label": "C", "text": "senior than", "is_correct": True},
            {"label": "D", "text": "me", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # --- FILL IN THE BLANKS (Q6 - Q10) ---
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "He has been working here _____ 2022.",
        "sample_answer": "'Since' is used for a specific starting point in time in present perfect continuous tense.",
        "tips": "Since + specific year/time point.",
        "options": [
            {"label": "A", "text": "for", "is_correct": False},
            {"label": "B", "text": "since", "is_correct": True},
            {"label": "C", "text": "from", "is_correct": False},
            {"label": "D", "text": "by", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "I prefer tea _____ coffee.",
        "sample_answer": "The verb 'prefer' takes the preposition 'to' when comparing two items.",
        "tips": "Prefer X to Y.",
        "options": [
            {"label": "A", "text": "than", "is_correct": False},
            {"label": "B", "text": "to", "is_correct": True},
            {"label": "C", "text": "over", "is_correct": False},
            {"label": "D", "text": "with", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "The meeting will start _____ 10 AM.",
        "sample_answer": "Preposition 'at' is used for specific clock times.",
        "tips": "At + specific time.",
        "options": [
            {"label": "A", "text": "at", "is_correct": True},
            {"label": "B", "text": "on", "is_correct": False},
            {"label": "C", "text": "in", "is_correct": False},
            {"label": "D", "text": "for", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "She is interested _____ learning Python.",
        "sample_answer": "The adjective 'interested' is followed by preposition 'in'.",
        "tips": "Interested in + gerund/noun.",
        "options": [
            {"label": "A", "text": "on", "is_correct": False},
            {"label": "B", "text": "at", "is_correct": False},
            {"label": "C", "text": "in", "is_correct": True},
            {"label": "D", "text": "with", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "The train arrived _____ time.",
        "sample_answer": "'On time' means punctual according to the schedule.",
        "tips": "On time = at the planned schedule time.",
        "options": [
            {"label": "A", "text": "at", "is_correct": False},
            {"label": "B", "text": "on", "is_correct": True},
            {"label": "C", "text": "in", "is_correct": False},
            {"label": "D", "text": "by", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- SENTENCE IMPROVEMENT (Q11 - Q15) ---
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Choose the grammatically correct sentence.",
        "sample_answer": "Third person singular 'He' takes auxiliary 'doesn't' followed by base verb 'know'.",
        "tips": "He/She/It + doesn't + base verb.",
        "options": [
            {"label": "A", "text": "He don't know the answer.", "is_correct": False},
            {"label": "B", "text": "He doesn't knows the answer.", "is_correct": False},
            {"label": "C", "text": "He doesn't know the answer.", "is_correct": True},
            {"label": "D", "text": "He not know the answer.", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Choose the grammatically correct sentence.",
        "sample_answer": "An action starting in the past and continuing to present with 'since' requires Present Perfect Continuous ('have been living').",
        "tips": "Present Perfect Continuous with 'since'.",
        "options": [
            {"label": "A", "text": "I am living here since 2020.", "is_correct": False},
            {"label": "B", "text": "I have been living here since 2020.", "is_correct": True},
            {"label": "C", "text": "I live here since 2020.", "is_correct": False},
            {"label": "D", "text": "I was living here since 2020.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Choose the grammatically correct sentence.",
        "sample_answer": "'One of the + superlative adjective' requires a plural noun ('students').",
        "tips": "One of the + superlative + plural noun.",
        "options": [
            {"label": "A", "text": "She is one of the best student.", "is_correct": False},
            {"label": "B", "text": "She is one of the best students.", "is_correct": True},
            {"label": "C", "text": "She is one of best students.", "is_correct": False},
            {"label": "D", "text": "She is best students.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Choose the grammatically correct sentence.",
        "sample_answer": "'News' is an uncountable singular noun and takes a singular verb ('is').",
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
        "title": "Grammar",
        "difficulty": "Medium",
        "question_text": "Choose the grammatically correct sentence.",
        "sample_answer": "Names of academic subjects (Mathematics, Physics) take singular verbs ('is').",
        "tips": "Subject names ending in '-s' take singular verb.",
        "options": [
            {"label": "A", "text": "Mathematics are difficult.", "is_correct": False},
            {"label": "B", "text": "Mathematics is difficult.", "is_correct": True},
            {"label": "C", "text": "Mathematics were difficult.", "is_correct": False},
            {"label": "D", "text": "Mathematics have difficult.", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- ACTIVE & PASSIVE VOICE (Q16 - Q20) ---
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Change into passive voice: \"They completed the project.\"",
        "sample_answer": "Simple past active (V2 'completed') changes to passive 'was/were + V3' → 'The project was completed by them.'",
        "tips": "Simple past passive: Object + was/were + V3.",
        "options": [
            {"label": "A", "text": "The project was completed by them.", "is_correct": True},
            {"label": "B", "text": "The project is completed by them.", "is_correct": False},
            {"label": "C", "text": "The project had completed by them.", "is_correct": False},
            {"label": "D", "text": "The project has been completed by them.", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Change into passive voice: \"The manager approved the proposal.\"",
        "sample_answer": "Simple past active becomes 'was approved by the manager'.",
        "tips": "Object + was/were + V3 + by agent.",
        "options": [
            {"label": "A", "text": "The proposal is approved by the manager.", "is_correct": False},
            {"label": "B", "text": "The proposal was approved by the manager.", "is_correct": True},
            {"label": "C", "text": "The proposal had been approved by the manager.", "is_correct": False},
            {"label": "D", "text": "The proposal has approved by the manager.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Change into active voice: \"The letter was written by John.\"",
        "sample_answer": "Passive 'was written' in simple past converts to active 'wrote' → 'John wrote the letter.'",
        "tips": "was/were + V3 → Simple Past V2.",
        "options": [
            {"label": "A", "text": "John writes the letter.", "is_correct": False},
            {"label": "B", "text": "John wrote the letter.", "is_correct": True},
            {"label": "C", "text": "John has written the letter.", "is_correct": False},
            {"label": "D", "text": "John had written the letter.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Change into passive voice: \"She is preparing the report.\"",
        "sample_answer": "Present continuous active ('is preparing') converts to passive 'is being prepared'.",
        "tips": "Present continuous passive: is/am/are + being + V3.",
        "options": [
            {"label": "A", "text": "The report was prepared by her.", "is_correct": False},
            {"label": "B", "text": "The report is prepared by her.", "is_correct": False},
            {"label": "C", "text": "The report is being prepared by her.", "is_correct": True},
            {"label": "D", "text": "The report has been prepared by her.", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Change into active voice: \"The cake was baked by my mother.\"",
        "sample_answer": "Passive 'was baked' converts to simple past active 'baked'.",
        "tips": "Simple past active form.",
        "options": [
            {"label": "A", "text": "My mother bakes the cake.", "is_correct": False},
            {"label": "B", "text": "My mother baked the cake.", "is_correct": True},
            {"label": "C", "text": "My mother has baked the cake.", "is_correct": False},
            {"label": "D", "text": "My mother was baking the cake.", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- DIRECT & INDIRECT SPEECH (Q21 - Q25) ---
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Convert into indirect speech: He said, \"I am busy.\"",
        "sample_answer": "Simple present tense 'am' changes to simple past 'was' in indirect speech → 'He said that he was busy.'",
        "tips": "Present continuous/simple shifts to past.",
        "options": [
            {"label": "A", "text": "He said that he is busy.", "is_correct": False},
            {"label": "B", "text": "He said that he was busy.", "is_correct": True},
            {"label": "C", "text": "He says that he was busy.", "is_correct": False},
            {"label": "D", "text": "He told he is busy.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Convert into indirect speech: She said, \"I have completed my work.\"",
        "sample_answer": "Present perfect 'have completed' shifts to past perfect 'had completed'.",
        "tips": "Present perfect -> Past perfect.",
        "options": [
            {"label": "A", "text": "She said that she has completed her work.", "is_correct": False},
            {"label": "B", "text": "She said that she had completed her work.", "is_correct": True},
            {"label": "C", "text": "She told that she completed her work.", "is_correct": False},
            {"label": "D", "text": "She says she had completed her work.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Convert into indirect speech: Ravi said, \"I will attend the meeting.\"",
        "sample_answer": "Future auxiliary 'will' changes to modal 'would' in reported speech.",
        "tips": "will -> would.",
        "options": [
            {"label": "A", "text": "Ravi said that he will attend the meeting.", "is_correct": False},
            {"label": "B", "text": "Ravi said that he would attend the meeting.", "is_correct": True},
            {"label": "C", "text": "Ravi says that he will attend the meeting.", "is_correct": False},
            {"label": "D", "text": "Ravi told that he can attend the meeting.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Convert into indirect speech: The teacher said, \"Work hard.\"",
        "sample_answer": "Imperative statements convert using reporting verbs like 'advised' followed by infinitive 'to work hard'.",
        "tips": "Imperative: reporting verb + to + infinitive.",
        "options": [
            {"label": "A", "text": "The teacher said to work hard.", "is_correct": False},
            {"label": "B", "text": "The teacher advised to work hard.", "is_correct": True},
            {"label": "C", "text": "The teacher told working hard.", "is_correct": False},
            {"label": "D", "text": "The teacher ordered that work hard.", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Convert into indirect speech: He said, \"Where are you going?\"",
        "sample_answer": "Interrogative sentences change reporting verb to 'asked' and word order becomes assertive ('where I was going').",
        "tips": "Interrogative: reporting verb 'asked', assertive word order.",
        "options": [
            {"label": "A", "text": "He asked where I am going.", "is_correct": False},
            {"label": "B", "text": "He asked where I was going.", "is_correct": True},
            {"label": "C", "text": "He said where I was going.", "is_correct": False},
            {"label": "D", "text": "He asked where was I going.", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- ADVANCED PLACEMENT GRAMMAR (Q26 - Q30) ---
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Choose the correct option: Hardly had he entered the room _____ the phone rang.",
        "sample_answer": "The correlative conjunction pair is 'Hardly ... when'.",
        "tips": "Hardly is paired with 'when'.",
        "options": [
            {"label": "A", "text": "when", "is_correct": True},
            {"label": "B", "text": "than", "is_correct": False},
            {"label": "C", "text": "then", "is_correct": False},
            {"label": "D", "text": "and", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Choose the correct option: No sooner had she arrived _____ it started raining.",
        "sample_answer": "The correlative conjunction pair is 'No sooner ... than'.",
        "tips": "No sooner is paired with 'than'.",
        "options": [
            {"label": "A", "text": "then", "is_correct": False},
            {"label": "B", "text": "than", "is_correct": True},
            {"label": "C", "text": "when", "is_correct": False},
            {"label": "D", "text": "and", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Choose the correct option: Scarcely had the train left the station _____ it stopped again.",
        "sample_answer": "The correlative conjunction pair is 'Scarcely ... when'.",
        "tips": "Scarcely is paired with 'when'.",
        "options": [
            {"label": "A", "text": "when", "is_correct": True},
            {"label": "B", "text": "than", "is_correct": False},
            {"label": "C", "text": "then", "is_correct": False},
            {"label": "D", "text": "and", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Choose the correct option: If I _____ rich, I would travel the world.",
        "sample_answer": "In second conditional (unreal present condition), the subjunctive verb 'were' is used for all subjects.",
        "tips": "Unreal conditional takes 'were' regardless of subject.",
        "options": [
            {"label": "A", "text": "am", "is_correct": False},
            {"label": "B", "text": "was", "is_correct": False},
            {"label": "C", "text": "were", "is_correct": True},
            {"label": "D", "text": "will be", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Grammar",
        "difficulty": "Hard",
        "question_text": "Choose the correct option: Neither the manager nor the employees _____ willing to compromise.",
        "sample_answer": "With 'Neither ... nor', the verb agrees with the subject closest to it ('employees' -> plural -> 'are').",
        "tips": "Proximity rule: verb agrees with subject closest to it.",
        "options": [
            {"label": "A", "text": "is", "is_correct": False},
            {"label": "B", "text": "was", "is_correct": False},
            {"label": "C", "text": "are", "is_correct": True},
            {"label": "D", "text": "has", "is_correct": False}
        ],
        "correct_option": "C"
    }
]

def seed_grammar():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Grammar'")
            print(f"Deleted old 'Grammar' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Verbal Ability',
                    'Grammar',
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
    seed_grammar()
