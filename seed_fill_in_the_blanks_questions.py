import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- PREPOSITIONAL & BASIC GRAMMAR BLANKS (Q1 - Q5) ---
    {
        "title": "Fill in the Blanks",
        "difficulty": "Medium",
        "question_text": "The manager congratulated the team _____ their success.",
        "sample_answer": "The verb 'congratulate' is followed by the preposition 'on'.",
        "tips": "Congratulate someone on something.",
        "options": [
            {"label": "A", "text": "for", "is_correct": False},
            {"label": "B", "text": "on", "is_correct": True},
            {"label": "C", "text": "in", "is_correct": False},
            {"label": "D", "text": "with", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Medium",
        "question_text": "The project was completed _____ the deadline.",
        "sample_answer": "Finishing before schedule means completing 'before' the deadline.",
        "tips": "Before + deadline.",
        "options": [
            {"label": "A", "text": "before", "is_correct": True},
            {"label": "B", "text": "after", "is_correct": False},
            {"label": "C", "text": "during", "is_correct": False},
            {"label": "D", "text": "between", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Medium",
        "question_text": "She is responsible _____ maintaining the records.",
        "sample_answer": "The adjective 'responsible' is followed by preposition 'for'.",
        "tips": "Responsible for + V-ing.",
        "options": [
            {"label": "A", "text": "in", "is_correct": False},
            {"label": "B", "text": "for", "is_correct": True},
            {"label": "C", "text": "with", "is_correct": False},
            {"label": "D", "text": "on", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Medium",
        "question_text": "The company specializes _____ software development.",
        "sample_answer": "The verb 'specialize' is followed by preposition 'in'.",
        "tips": "Specialize in + domain.",
        "options": [
            {"label": "A", "text": "at", "is_correct": False},
            {"label": "B", "text": "in", "is_correct": True},
            {"label": "C", "text": "on", "is_correct": False},
            {"label": "D", "text": "for", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Medium",
        "question_text": "The students were excited _____ the trip.",
        "sample_answer": "The adjective 'excited' takes preposition 'about' when anticipating an event.",
        "tips": "Excited about + event.",
        "options": [
            {"label": "A", "text": "about", "is_correct": True},
            {"label": "B", "text": "on", "is_correct": False},
            {"label": "C", "text": "with", "is_correct": False},
            {"label": "D", "text": "by", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- HARD LEVEL GRAMMAR BLANKS (Q6 - Q15) ---
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Neither the manager nor the employees _____ willing to compromise.",
        "sample_answer": "With 'Neither ... nor', the verb agrees with the subject closest to it ('employees' -> plural -> 'are').",
        "tips": "Proximity rule: verb agrees with closer subject.",
        "options": [
            {"label": "A", "text": "is", "is_correct": False},
            {"label": "B", "text": "was", "is_correct": False},
            {"label": "C", "text": "are", "is_correct": True},
            {"label": "D", "text": "has", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Hardly had he entered the room _____ the phone rang.",
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
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "No sooner had she arrived _____ it started raining.",
        "sample_answer": "The correlative conjunction pair is 'No sooner ... than'.",
        "tips": "No sooner is paired with 'than'.",
        "options": [
            {"label": "A", "text": "when", "is_correct": False},
            {"label": "B", "text": "then", "is_correct": False},
            {"label": "C", "text": "than", "is_correct": True},
            {"label": "D", "text": "and", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "If I _____ rich, I would travel the world.",
        "sample_answer": "Subjunctive mood for unreal present conditions requires 'were' for all subjects.",
        "tips": "Subjunctive conditional takes 'were'.",
        "options": [
            {"label": "A", "text": "am", "is_correct": False},
            {"label": "B", "text": "was", "is_correct": False},
            {"label": "C", "text": "were", "is_correct": True},
            {"label": "D", "text": "be", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "One of the students who _____ selected for the competition is my friend.",
        "sample_answer": "Relative pronoun 'who' refers to plural antecedent 'students', requiring plural verb 'were'.",
        "tips": "Relative clause verb agrees with antecedent 'students'.",
        "options": [
            {"label": "A", "text": "was", "is_correct": False},
            {"label": "B", "text": "were", "is_correct": True},
            {"label": "C", "text": "is", "is_correct": False},
            {"label": "D", "text": "are", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The committee _____ divided in its opinion.",
        "sample_answer": "Singular pronoun 'its' indicates the collective noun 'committee' is acting as a singular unit → 'is'.",
        "tips": "Singular pronoun 'its' requires singular verb 'is'.",
        "options": [
            {"label": "A", "text": "is", "is_correct": True},
            {"label": "B", "text": "are", "is_correct": False},
            {"label": "C", "text": "were", "is_correct": False},
            {"label": "D", "text": "have", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Not only the students but also the teacher _____ present.",
        "sample_answer": "With 'Not only ... but also', the verb agrees with the closer subject ('teacher' -> singular -> 'was').",
        "tips": "Proximity rule for not only/but also.",
        "options": [
            {"label": "A", "text": "was", "is_correct": True},
            {"label": "B", "text": "were", "is_correct": False},
            {"label": "C", "text": "are", "is_correct": False},
            {"label": "D", "text": "have", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Scarcely had the train left the station _____ it stopped again.",
        "sample_answer": "The correlative conjunction pair is 'Scarcely ... when'.",
        "tips": "Scarcely is paired with 'when'.",
        "options": [
            {"label": "A", "text": "than", "is_correct": False},
            {"label": "B", "text": "when", "is_correct": True},
            {"label": "C", "text": "then", "is_correct": False},
            {"label": "D", "text": "and", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Had I known the truth, I _____ acted differently.",
        "sample_answer": "Inverted third conditional structure: 'Had + V3 ..., would have + V3'.",
        "tips": "Had + V3 requires 'would have' in main clause.",
        "options": [
            {"label": "A", "text": "would have", "is_correct": True},
            {"label": "B", "text": "will have", "is_correct": False},
            {"label": "C", "text": "would", "is_correct": False},
            {"label": "D", "text": "shall have", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Seldom _____ such a beautiful sight.",
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

    # --- PLACEMENT-LEVEL VOCABULARY & PARTS OF SPEECH (Q16 - Q25) ---
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The company plans to expand its operations globally _____ year.",
        "sample_answer": "The verb 'plans' indicates future intention → 'next year'.",
        "tips": "Future plan + next year.",
        "options": [
            {"label": "A", "text": "previous", "is_correct": False},
            {"label": "B", "text": "next", "is_correct": True},
            {"label": "C", "text": "last", "is_correct": False},
            {"label": "D", "text": "before", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Artificial Intelligence is becoming increasingly _____ in modern industries.",
        "sample_answer": "Adverb 'increasingly' modifies predicate adjective 'relevant'.",
        "tips": "Adverb + adjective.",
        "options": [
            {"label": "A", "text": "relevant", "is_correct": True},
            {"label": "B", "text": "relevance", "is_correct": False},
            {"label": "C", "text": "relevantly", "is_correct": False},
            {"label": "D", "text": "relevancy", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The candidate demonstrated excellent problem-solving _____ during the interview.",
        "sample_answer": "The modifier 'problem-solving' modifies noun 'ability'.",
        "tips": "Requires noun 'ability'.",
        "options": [
            {"label": "A", "text": "ability", "is_correct": True},
            {"label": "B", "text": "abilities", "is_correct": False},
            {"label": "C", "text": "capable", "is_correct": False},
            {"label": "D", "text": "capable of", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The report provides a comprehensive _____ of market trends.",
        "sample_answer": "The adjective 'comprehensive' modifies noun 'analysis'.",
        "tips": "Comprehensive + noun (analysis).",
        "options": [
            {"label": "A", "text": "analyze", "is_correct": False},
            {"label": "B", "text": "analysis", "is_correct": True},
            {"label": "C", "text": "analytical", "is_correct": False},
            {"label": "D", "text": "analyzed", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Employees are encouraged to participate _____ training programs.",
        "sample_answer": "The verb 'participate' takes preposition 'in'.",
        "tips": "Participate in + activity.",
        "options": [
            {"label": "A", "text": "in", "is_correct": True},
            {"label": "B", "text": "on", "is_correct": False},
            {"label": "C", "text": "at", "is_correct": False},
            {"label": "D", "text": "by", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The CEO's decision was highly _____ and resulted in significant growth.",
        "sample_answer": "Adverb 'highly' modifies predicate adjective 'strategic'.",
        "tips": "Highly + adjective (strategic).",
        "options": [
            {"label": "A", "text": "strategic", "is_correct": True},
            {"label": "B", "text": "strategy", "is_correct": False},
            {"label": "C", "text": "strategically", "is_correct": False},
            {"label": "D", "text": "strategist", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The new software greatly improved operational _____.",
        "sample_answer": "Adjective 'operational' modifies noun 'efficiency'.",
        "tips": "Operational + noun (efficiency).",
        "options": [
            {"label": "A", "text": "efficient", "is_correct": False},
            {"label": "B", "text": "efficiency", "is_correct": True},
            {"label": "C", "text": "efficiently", "is_correct": False},
            {"label": "D", "text": "efficiencies", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The scientist's findings were considered _____ because they challenged existing theories.",
        "sample_answer": "The predicate adjective modifying 'findings' is 'revolutionary'.",
        "tips": "Requires adjective 'revolutionary'.",
        "options": [
            {"label": "A", "text": "revolutionary", "is_correct": True},
            {"label": "B", "text": "revolution", "is_correct": False},
            {"label": "C", "text": "revolved", "is_correct": False},
            {"label": "D", "text": "revolutionize", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The company faced several _____ while implementing the new policy.",
        "sample_answer": "Determiner 'several' requires plural noun 'challenges'.",
        "tips": "Several + plural noun (challenges).",
        "options": [
            {"label": "A", "text": "challenge", "is_correct": False},
            {"label": "B", "text": "challenged", "is_correct": False},
            {"label": "C", "text": "challenges", "is_correct": True},
            {"label": "D", "text": "challenging", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "Continuous learning is essential for professional _____.",
        "sample_answer": "Adjective 'professional' modifies noun 'growth'.",
        "tips": "Professional + noun (growth).",
        "options": [
            {"label": "A", "text": "grow", "is_correct": False},
            {"label": "B", "text": "growth", "is_correct": True},
            {"label": "C", "text": "growing", "is_correct": False},
            {"label": "D", "text": "grown", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- DOUBLE FILL IN THE BLANKS (Q26 - Q30) ---
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The manager was _____ with the team's performance and decided to _____ them.",
        "sample_answer": "First blank requires adjective 'pleased'; second blank requires base infinitive 'reward'.",
        "tips": "Pleased (adj) + to reward (infinitive).",
        "options": [
            {"label": "A", "text": "pleased, reward", "is_correct": True},
            {"label": "B", "text": "please, rewarded", "is_correct": False},
            {"label": "C", "text": "pleasing, rewarding", "is_correct": False},
            {"label": "D", "text": "pleased, rewarded", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The project was completed _____ budget and _____ schedule.",
        "sample_answer": "Standard corporate collocation: 'within budget and ahead of schedule'.",
        "tips": "Within budget, ahead of schedule.",
        "options": [
            {"label": "A", "text": "within, ahead of", "is_correct": True},
            {"label": "B", "text": "within, behind", "is_correct": False},
            {"label": "C", "text": "outside, ahead", "is_correct": False},
            {"label": "D", "text": "above, after", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The candidate not only demonstrated technical expertise _____ excellent communication skills.",
        "sample_answer": "Correlative conjunction pair: 'not only ... but also'.",
        "tips": "Not only is followed by 'but also'.",
        "options": [
            {"label": "A", "text": "and", "is_correct": False},
            {"label": "B", "text": "but also", "is_correct": True},
            {"label": "C", "text": "therefore", "is_correct": False},
            {"label": "D", "text": "because", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The company aims to reduce costs _____ maintaining high-quality standards.",
        "sample_answer": "Conjunction 'while' expresses simultaneous action with present participle 'maintaining'.",
        "tips": "While + V-ing.",
        "options": [
            {"label": "A", "text": "while", "is_correct": True},
            {"label": "B", "text": "during", "is_correct": False},
            {"label": "C", "text": "despite", "is_correct": False},
            {"label": "D", "text": "unless", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks",
        "difficulty": "Hard",
        "question_text": "The training program was designed to _____ employees' skills and _____ productivity.",
        "sample_answer": "Parallel infinitives after 'to': 'to enhance ... and increase ...'",
        "tips": "Parallel structure: to enhance and increase.",
        "options": [
            {"label": "A", "text": "enhance, increase", "is_correct": True},
            {"label": "B", "text": "enhancing, increasing", "is_correct": False},
            {"label": "C", "text": "enhanced, increased", "is_correct": False},
            {"label": "D", "text": "enhancement, increase", "is_correct": False}
        ],
        "correct_option": "A"
    }
]

def seed_fill_in_the_blanks():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Fill in the Blanks'")
            print(f"Deleted old 'Fill in the Blanks' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Verbal Ability',
                    'Fill in the Blanks',
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
    seed_fill_in_the_blanks()
