import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: A, C, E, G, I, ?",
        "sample_answer": "Letter positions: A(1), C(3), E(5), G(7), I(9)\nPattern: Adding +2 at each step.\nNext position = 9 + 2 = 11 (K).",
        "tips": "Add +2 to position at each step.",
        "options": [
            {"label": "A", "text": "J", "is_correct": False},
            {"label": "B", "text": "K", "is_correct": True},
            {"label": "C", "text": "L", "is_correct": False},
            {"label": "D", "text": "M", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: B, E, H, K, N, ?",
        "sample_answer": "Letter positions: B(2), E(5), H(8), K(11), N(14)\nPattern: Adding +3 at each step.\nNext position = 14 + 3 = 17 (Q).",
        "tips": "Add +3 to position at each step.",
        "options": [
            {"label": "A", "text": "O", "is_correct": False},
            {"label": "B", "text": "P", "is_correct": False},
            {"label": "C", "text": "Q", "is_correct": True},
            {"label": "D", "text": "R", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: Z, X, V, T, R, ?",
        "sample_answer": "Letter positions: Z(26), X(24), V(22), T(20), R(18)\nPattern: Subtracting -2 at each step.\nNext position = 18 − 2 = 16 (P).",
        "tips": "Reverse alphabetical order with -2 step.",
        "options": [
            {"label": "A", "text": "N", "is_correct": False},
            {"label": "B", "text": "O", "is_correct": False},
            {"label": "C", "text": "P", "is_correct": True},
            {"label": "D", "text": "Q", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: A, D, G, J, M, ?",
        "sample_answer": "Letter positions: A(1), D(4), G(7), J(10), M(13)\nPattern: Adding +3 at each step.\nNext position = 13 + 3 = 16 (P).",
        "tips": "Add +3 to position at each step.",
        "options": [
            {"label": "A", "text": "O", "is_correct": False},
            {"label": "B", "text": "P", "is_correct": True},
            {"label": "C", "text": "Q", "is_correct": False},
            {"label": "D", "text": "R", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: C, F, I, L, O, ?",
        "sample_answer": "Letter positions: C(3), F(6), I(9), L(12), O(15)\nPattern: Multiples of 3 (+3 at each step).\nNext position = 15 + 3 = 18 (R).",
        "tips": "Multiples of 3 in alphabet positions.",
        "options": [
            {"label": "A", "text": "P", "is_correct": False},
            {"label": "B", "text": "Q", "is_correct": False},
            {"label": "C", "text": "R", "is_correct": True},
            {"label": "D", "text": "S", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: A, C, F, J, O, ?",
        "sample_answer": "Letter positions: A(1), C(3), F(6), J(10), O(15)\nPattern: Differences increase (+2, +3, +4, +5, +6).\nNext position = 15 + 6 = 21 (U).",
        "tips": "Differences are +2, +3, +4, +5, +6.",
        "options": [
            {"label": "A", "text": "S", "is_correct": False},
            {"label": "B", "text": "T", "is_correct": False},
            {"label": "C", "text": "U", "is_correct": True},
            {"label": "D", "text": "V", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: Z, W, S, N, H, ?",
        "sample_answer": "Letter positions: Z(26), W(23), S(19), N(14), H(8)\nPattern: Decreasing steps (−3, −4, −5, −6, −7).\nNext position = 8 − 7 = 1 (A).",
        "tips": "Subtractions increase: -3, -4, -5, -6, -7.",
        "options": [
            {"label": "A", "text": "A", "is_correct": True},
            {"label": "B", "text": "B", "is_correct": False},
            {"label": "C", "text": "C", "is_correct": False},
            {"label": "D", "text": "D", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: B, F, J, N, R, ?",
        "sample_answer": "Letter positions: B(2), F(6), J(10), N(14), R(18)\nPattern: Adding +4 at each step.\nNext position = 18 + 4 = 22 (V).",
        "tips": "Add +4 to position at each step.",
        "options": [
            {"label": "A", "text": "T", "is_correct": False},
            {"label": "B", "text": "U", "is_correct": False},
            {"label": "C", "text": "V", "is_correct": True},
            {"label": "D", "text": "W", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: A, D, H, M, S, ?",
        "sample_answer": "Letter positions: A(1), D(4), H(8), M(13), S(19)\nPattern: Differences increase (+3, +4, +5, +6, +7).\nNext position = 19 + 7 = 26 (Z).",
        "tips": "Differences are +3, +4, +5, +6, +7.",
        "options": [
            {"label": "A", "text": "X", "is_correct": False},
            {"label": "B", "text": "Y", "is_correct": False},
            {"label": "C", "text": "Z", "is_correct": True},
            {"label": "D", "text": "A", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter in the series: C, G, L, R, Y, ?",
        "sample_answer": "Letter positions: C(3), G(7), L(12), R(18), Y(25)\nPattern: Differences increase (+4, +5, +6, +7, +8).\nNext position = 25 + 8 = 33 (33 mod 26 = 7 -> G).",
        "tips": "Differences are +4, +5, +6, +7, +8.",
        "options": [
            {"label": "A", "text": "E", "is_correct": False},
            {"label": "B", "text": "F", "is_correct": False},
            {"label": "C", "text": "G", "is_correct": True},
            {"label": "D", "text": "H", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next pair of letters in the series: AB, DE, GH, JK, ?",
        "sample_answer": "Pattern: Consecutive pairs of letters with 1 skipped letter in between.\nAB (C skipped) DE (F skipped) GH (I skipped) JK (L skipped) MN.",
        "tips": "Skip 1 letter between consecutive pairs.",
        "options": [
            {"label": "A", "text": "LM", "is_correct": False},
            {"label": "B", "text": "MN", "is_correct": True},
            {"label": "C", "text": "NO", "is_correct": False},
            {"label": "D", "text": "MP", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next letter pair: AZ, BY, CX, DW, ?",
        "sample_answer": "Pattern: Opposite letter pairs (1st & 26th, 2nd & 25th, etc.)\nA-Z, B-Y, C-X, D-W, E-V.",
        "tips": "Opposite alphabetical positions.",
        "options": [
            {"label": "A", "text": "EV", "is_correct": True},
            {"label": "B", "text": "FU", "is_correct": False},
            {"label": "C", "text": "GT", "is_correct": False},
            {"label": "D", "text": "HS", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next pair of letters: AD, BE, CF, DG, ?",
        "sample_answer": "Pattern: 1st letter +1 (A,B,C,D -> E), 2nd letter +1 (D,E,F,G -> H).\nNext pair = EH.",
        "tips": "Advance both letters by +1.",
        "options": [
            {"label": "A", "text": "EF", "is_correct": False},
            {"label": "B", "text": "EG", "is_correct": False},
            {"label": "C", "text": "EH", "is_correct": True},
            {"label": "D", "text": "EI", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next pair of letters: AC, DF, GI, JL, ?",
        "sample_answer": "Pattern: 1st letter +3 (A,D,G,J -> M), 2nd letter +3 (C,F,I,L -> O).\nNext pair = MO.",
        "tips": "Advance both letters by +3.",
        "options": [
            {"label": "A", "text": "LN", "is_correct": False},
            {"label": "B", "text": "MO", "is_correct": True},
            {"label": "C", "text": "NP", "is_correct": False},
            {"label": "D", "text": "OQ", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Medium",
        "question_text": "Find the next pair of letters: BA, DC, FE, HG, ?",
        "sample_answer": "Pattern: Reversed consecutive letter pairs.\n(2,1) BA, (4,3) DC, (6,5) FE, (8,7) HG, (10,9) JI.",
        "tips": "Reversed consecutive pairs.",
        "options": [
            {"label": "A", "text": "IH", "is_correct": False},
            {"label": "B", "text": "JI", "is_correct": True},
            {"label": "C", "text": "KJ", "is_correct": False},
            {"label": "D", "text": "LK", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next letter in the series: A, D, I, P, Y, ?",
        "sample_answer": "Letter positions: A(1), D(4), I(9), P(16), Y(25)\nPattern: Perfect squares n² for n = 1, 2, 3, 4, 5, 6.\nNext position = 6² = 36 ≡ 10 mod 26 -> (J).",
        "tips": "Alphabet positions correspond to perfect squares.",
        "options": [
            {"label": "A", "text": "H", "is_correct": False},
            {"label": "B", "text": "I", "is_correct": False},
            {"label": "C", "text": "J", "is_correct": True},
            {"label": "D", "text": "K", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next letter in the series: B, E, J, Q, Z, ?",
        "sample_answer": "Letter positions: B(2), E(5), J(10), Q(17), Z(26)\nPattern: n² + 1 for n = 1, 2, 3, 4, 5, 6.\nNext position = 6² + 1 = 37 ≡ 11 mod 26 -> (K).",
        "tips": "Alphabet positions correspond to n² + 1.",
        "options": [
            {"label": "A", "text": "J", "is_correct": False},
            {"label": "B", "text": "K", "is_correct": True},
            {"label": "C", "text": "L", "is_correct": False},
            {"label": "D", "text": "M", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next letter in the series: A, B, D, G, K, P, ?",
        "sample_answer": "Letter positions: A(1), B(2), D(4), G(7), K(11), P(16)\nPattern: Differences increase (+1, +2, +3, +4, +5, +6).\nNext position = 16 + 6 = 22 (V).",
        "tips": "Differences increase by +1 at each step.",
        "options": [
            {"label": "A", "text": "T", "is_correct": False},
            {"label": "B", "text": "U", "is_correct": False},
            {"label": "C", "text": "V", "is_correct": True},
            {"label": "D", "text": "W", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next letter in the series: Z, X, U, Q, L, ?",
        "sample_answer": "Letter positions: Z(26), X(24), U(21), Q(17), L(12)\nPattern: Subtractions increase (−2, −3, −4, −5, −6).\nNext position = 12 − 6 = 6 (F).",
        "tips": "Subtractions increase by -1 at each step.",
        "options": [
            {"label": "A", "text": "D", "is_correct": False},
            {"label": "B", "text": "E", "is_correct": False},
            {"label": "C", "text": "F", "is_correct": True},
            {"label": "D", "text": "G", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next letter in the series: A, E, J, P, W, ?",
        "sample_answer": "Letter positions: A(1), E(5), J(10), P(16), W(23)\nPattern: Differences increase (+4, +5, +6, +7, +8).\nNext position = 23 + 8 = 31 ≡ 5 mod 26 -> (E).",
        "tips": "Differences are +4, +5, +6, +7, +8.",
        "options": [
            {"label": "A", "text": "D", "is_correct": False},
            {"label": "B", "text": "E", "is_correct": True},
            {"label": "C", "text": "F", "is_correct": False},
            {"label": "D", "text": "G", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next alpha-numeric term: A1, C3, E5, G7, I9, ?",
        "sample_answer": "Pattern: Letter advances by +2 (A,C,E,G,I -> K), number is letter position (1,3,5,7,9 -> 11).\nNext term = K11.",
        "tips": "Letter position +2, number matches letter position.",
        "options": [
            {"label": "A", "text": "J10", "is_correct": False},
            {"label": "B", "text": "K11", "is_correct": True},
            {"label": "C", "text": "L12", "is_correct": False},
            {"label": "D", "text": "M13", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next alpha-numeric term: B2, E4, H6, K8, N10, ?",
        "sample_answer": "Pattern: Letter +3 (B,E,H,K,N -> Q), Number +2 (2,4,6,8,10 -> 12).\nNext term = Q12.",
        "tips": "Letter +3, Number +2.",
        "options": [
            {"label": "A", "text": "P11", "is_correct": False},
            {"label": "B", "text": "Q12", "is_correct": True},
            {"label": "C", "text": "R13", "is_correct": False},
            {"label": "D", "text": "S14", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next alpha-numeric term: Z26, Y25, X24, W23, ?",
        "sample_answer": "Pattern: Reverse alphabetical letter (-1) and position number (-1).\nNext term = V22.",
        "tips": "Reverse alphabet order with matching position number.",
        "options": [
            {"label": "A", "text": "U21", "is_correct": False},
            {"label": "B", "text": "V22", "is_correct": True},
            {"label": "C", "text": "W21", "is_correct": False},
            {"label": "D", "text": "V23", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next alpha-numeric term: A2, C4, F7, J11, O16, ?",
        "sample_answer": "Pattern: Letter +2, +3, +4, +5, +6 (O(15) + 6 = 21 -> U), Number +2, +3, +4, +5, +6 (16 + 6 = 22).\nNext term = U22.",
        "tips": "Letter advances by +2, +3, +4, +5, +6; number increases by +2, +3, +4, +5, +6.",
        "options": [
            {"label": "A", "text": "T21", "is_correct": False},
            {"label": "B", "text": "U22", "is_correct": True},
            {"label": "C", "text": "V23", "is_correct": False},
            {"label": "D", "text": "W24", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Alphabet Series",
        "difficulty": "Hard",
        "question_text": "Find the next alpha-numeric term: B3, F6, K10, Q15, X21, ?",
        "sample_answer": "Pattern: Letter +4, +5, +6, +7, +8 (X(24) + 8 = 32 ≡ 6 mod 26 -> F), Number +3, +4, +5, +6, +7 (21 + 7 = 28).\nNext term = F28.",
        "tips": "Letter steps: +4, +5, +6, +7, +8; Number steps: +3, +4, +5, +6, +7.",
        "options": [
            {"label": "A", "text": "E27", "is_correct": False},
            {"label": "B", "text": "F28", "is_correct": True},
            {"label": "C", "text": "G29", "is_correct": False},
            {"label": "D", "text": "H30", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_alphabet_series():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Alphabet Series'")
            print(f"Deleted old 'Alphabet Series' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Logical Reasoning',
                    'Alphabet Series',
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
    seed_alphabet_series()
