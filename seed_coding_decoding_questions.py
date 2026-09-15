import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- LETTER & PATTERN CODING (Q1 - Q5) ---
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If MANGO is coded as NZSLT, then how is GRAPE coded?",
        "sample_answer": "Pattern: Letter shift pattern G(+1)=H, R(-1)=Q, A(+5)=F, P(+5)=U, E(+5)=J.\nHence, GRAPE is coded as HQFUJ.",
        "tips": "Check letter position shift patterns.",
        "options": [
            {"label": "A", "text": "HQFUJ", "is_correct": True},
            {"label": "B", "text": "TIZKV", "is_correct": False},
            {"label": "C", "text": "HSGVK", "is_correct": False},
            {"label": "D", "text": "GQFUI", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If FLOWER is coded as GMQZJX, then how is GARDEN coded?",
        "sample_answer": "Pattern: Fibonacci increments (+1, +1, +2, +3, +5, +8).\nG(+1)=H, A(+1)=B, R(+2)=T, D(+3)=G, E(+5)=J, N(+8)=V.\nHence, GARDEN is coded as HBTGJV.",
        "tips": "Increments follow the Fibonacci sequence (+1, +1, +2, +3, +5, +8).",
        "options": [
            {"label": "A", "text": "HBTGJV", "is_correct": True},
            {"label": "B", "text": "HBSFIW", "is_correct": False},
            {"label": "C", "text": "GATGJV", "is_correct": False},
            {"label": "D", "text": "HBTGJU", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If COMPUTER is coded as ERVQNPCV, then how is KEYBOARD coded?",
        "sample_answer": "Pattern: Positional shifts K(+2)=M, E(+3)=H, Y(+4)=C, B(+5)=G, O(+6)=U, A(+7)=H, R(+8)=Z, D(+9)=M.\nHence, KEYBOARD is coded as MHCGUHZM.",
        "tips": "Positions advance by +2, +3, +4, +5, +6, +7, +8, +9.",
        "options": [
            {"label": "A", "text": "LFCIPBSE", "is_correct": False},
            {"label": "B", "text": "MHCGUHZM", "is_correct": True},
            {"label": "C", "text": "NHDHVIAN", "is_correct": False},
            {"label": "D", "text": "MGCFTHYL", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If LANGUAGE is coded as OBPIZCJI, then how is DATABASE coded?",
        "sample_answer": "Pattern: Positional shift (+3, +1, +2, +2, +5, +2, +3, +4).\nD(+3)=G, A(+1)=B, T(+2)=V, A(+2)=C, B(+5)=G, A(+2)=C, S(+3)=V, E(+4)=I.\nHence, DATABASE is coded as GBVCGVI.",
        "tips": "Match corresponding positional shifts.",
        "options": [
            {"label": "A", "text": "GBVCGVI", "is_correct": True},
            {"label": "B", "text": "ECUBCFD", "is_correct": False},
            {"label": "C", "text": "FCVCDGE", "is_correct": False},
            {"label": "D", "text": "GBWCGVJ", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If NETWORK is coded as PGVYQTM, then how is PROGRAM coded?",
        "sample_answer": "Pattern: Every letter is shifted +2 forward.\nP(+2)=R, R(+2)=T, O(+2)=Q, G(+2)=I, R(+2)=T, A(+2)=C, M(+2)=O.\nHence, PROGRAM is coded as RTQITCO.",
        "tips": "Shift every letter by +2.",
        "options": [
            {"label": "A", "text": "QSHJUBN", "is_correct": False},
            {"label": "B", "text": "RTQITCO", "is_correct": True},
            {"label": "C", "text": "SURJUCP", "is_correct": False},
            {"label": "D", "text": "RTPISCN", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- NUMBER CODING (Q6 - Q10) ---
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "In a certain code language:\nTRAIN = 58\nPLANE = 48\nFind the code for HELICOPTER.",
        "sample_answer": "Pattern: Sum of alphabetical positions.\nH(8) + E(5) + L(12) + I(9) + C(3) + O(15) + P(16) + T(20) + E(5) + R(18) = 111.",
        "tips": "Sum the alphabetical positions of all letters.",
        "options": [
            {"label": "A", "text": "105", "is_correct": False},
            {"label": "B", "text": "111", "is_correct": True},
            {"label": "C", "text": "115", "is_correct": False},
            {"label": "D", "text": "120", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "In a certain code language:\nBOOK = 43\nNOTE = 58\nPAGE = 33\nFind the code for PENCIL.",
        "sample_answer": "Pattern: Sum of letter positions + Number of letters.\nPENCIL = (16 + 5 + 14 + 3 + 9 + 12) + 6 = 59 + 6 = 65.",
        "tips": "Total = (Sum of letter positions) + (Word Length).",
        "options": [
            {"label": "A", "text": "59", "is_correct": False},
            {"label": "B", "text": "62", "is_correct": False},
            {"label": "C", "text": "65", "is_correct": True},
            {"label": "D", "text": "68", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If COMPUTER = 120 and KEYBOARD = 108, find the code for MONITOR.",
        "sample_answer": "Pattern: Word Length × 13.5 (or Letter sum formula).\nMONITOR has 7 letters: 7 × 13 = 91.",
        "tips": "Multiply number of letters by 13.",
        "options": [
            {"label": "A", "text": "85", "is_correct": False},
            {"label": "B", "text": "91", "is_correct": True},
            {"label": "C", "text": "95", "is_correct": False},
            {"label": "D", "text": "100", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If CAT = 24, DOG = 26, BIRD = 33, find the code for HORSE.",
        "sample_answer": "Pattern: Direct sum of letter positions.\nHORSE = H(8) + O(15) + R(18) + S(19) + E(5) = 65.",
        "tips": "Sum the 1-based alphabetical values.",
        "options": [
            {"label": "A", "text": "60", "is_correct": False},
            {"label": "B", "text": "62", "is_correct": False},
            {"label": "C", "text": "65", "is_correct": True},
            {"label": "D", "text": "70", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "If MOBILE = 63 and LAPTOP = 74, find the code for TABLET.",
        "sample_answer": "Pattern: Sum of letter positions + Word length.\nTABLET = T(20) + A(1) + B(2) + L(12) + E(5) + T(20) = 60.\n60 + 6 (length) = 66.",
        "tips": "Sum of letter values + word length.",
        "options": [
            {"label": "A", "text": "60", "is_correct": False},
            {"label": "B", "text": "64", "is_correct": False},
            {"label": "C", "text": "66", "is_correct": True},
            {"label": "D", "text": "70", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # --- STATEMENT BASED CODING (Q11 - Q15) ---
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "In a certain language:\n'go to school' → na pa ki\n'school is good' → ki ma lo\n'go is nice' → na lo tu\nWhat is the code for school?",
        "sample_answer": "Comparing 'go to school' (na pa ki) and 'school is good' (ki ma lo):\nThe common word is 'school' and the common code is 'ki'.",
        "tips": "Compare common words between statements.",
        "options": [
            {"label": "A", "text": "na", "is_correct": False},
            {"label": "B", "text": "pa", "is_correct": False},
            {"label": "C", "text": "ki", "is_correct": True},
            {"label": "D", "text": "ma", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "In a certain language:\n'blue sky high' → da ka pa\n'high water level' → pa ta sa\n'blue water clear' → da sa la\nWhat is the code for water?",
        "sample_answer": "Comparing 'high water level' (pa ta sa) and 'blue water clear' (da sa la):\nThe common word is 'water' and the common code is 'sa'.",
        "tips": "Find the overlapping code word.",
        "options": [
            {"label": "A", "text": "da", "is_correct": False},
            {"label": "B", "text": "pa", "is_correct": False},
            {"label": "C", "text": "sa", "is_correct": True},
            {"label": "D", "text": "la", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "In a certain language:\n'apple mango orange' → ro ta ni\n'mango banana grape' → ta fi lo\n'banana orange kiwi' → ni fi sa\nWhat is the code for banana?",
        "sample_answer": "Comparing 'mango banana grape' (ta fi lo) and 'banana orange kiwi' (ni fi sa):\nThe common word is 'banana' and the common code is 'fi'.",
        "tips": "Match the common token in both statements.",
        "options": [
            {"label": "A", "text": "ta", "is_correct": False},
            {"label": "B", "text": "fi", "is_correct": True},
            {"label": "C", "text": "lo", "is_correct": False},
            {"label": "D", "text": "ni", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "In a certain language:\n'sun rises east' → ki pa lo\n'east west north' → lo ta ma\n'north south sun' → ma ri ki\nWhat is the code for south?",
        "sample_answer": "In 'north south sun' (ma ri ki):\n'north' = ma (from line 2 & 3)\n'sun' = ki (from line 1 & 3)\nRemaining code for 'south' = ri.",
        "tips": "Eliminate codes for known words to find the remaining word.",
        "options": [
            {"label": "A", "text": "ma", "is_correct": False},
            {"label": "B", "text": "ri", "is_correct": True},
            {"label": "C", "text": "ki", "is_correct": False},
            {"label": "D", "text": "lo", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Medium",
        "question_text": "In a certain language:\n'python java c' → ab cd ef\n'java sql html' → cd gh ij\n'python sql css' → ab gh kl\nWhat is the code for css?",
        "sample_answer": "In 'python sql css' (ab gh kl):\n'python' = ab (from line 1 & 3)\n'sql' = gh (from line 2 & 3)\nRemaining code for 'css' = kl.",
        "tips": "Eliminate common codes ab and gh.",
        "options": [
            {"label": "A", "text": "ab", "is_correct": False},
            {"label": "B", "text": "gh", "is_correct": False},
            {"label": "C", "text": "kl", "is_correct": True},
            {"label": "D", "text": "cd", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # --- MATRIX CODING (Q16 - Q20) ---
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If A=1, B=4, C=9, D=16, E=25, find the code for BAD.",
        "sample_answer": "Pattern: Position squared (n²).\nB = 2² = 4, A = 1² = 1, D = 4² = 16.\nCode for BAD = 4-1-16 (4116).",
        "tips": "Square of letter positions.",
        "options": [
            {"label": "A", "text": "214", "is_correct": False},
            {"label": "B", "text": "4116", "is_correct": True},
            {"label": "C", "text": "418", "is_correct": False},
            {"label": "D", "text": "4112", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "Using the same square pattern (A=1, B=4, C=9, D=16, E=25), find the code for FACE.",
        "sample_answer": "F = 6² = 36, A = 1² = 1, C = 3² = 9, E = 5² = 25.\nCode for FACE = 36-1-9-25 (361925).",
        "tips": "F=36, A=1, C=9, E=25.",
        "options": [
            {"label": "A", "text": "6135", "is_correct": False},
            {"label": "B", "text": "361925", "is_correct": True},
            {"label": "C", "text": "361920", "is_correct": False},
            {"label": "D", "text": "121925", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If A=2, B=6, C=12, D=20, E=30, find the code for BED.",
        "sample_answer": "Pattern: n(n + 1) where n is letter position.\nB = 2(3) = 6, E = 5(6) = 30, D = 4(5) = 20.\nCode for BED = 6-30-20 (63020).",
        "tips": "Formula: n × (n + 1).",
        "options": [
            {"label": "A", "text": "254", "is_correct": False},
            {"label": "B", "text": "63020", "is_correct": True},
            {"label": "C", "text": "62520", "is_correct": False},
            {"label": "D", "text": "43016", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If A = 1² + 1 = 2, B = 2² + 2 = 6, C = 3² + 3 = 12, find the code for CAB.",
        "sample_answer": "Pattern: n² + n.\nC = 12, A = 2, B = 6.\nCode for CAB = 12-2-6 (1226).",
        "tips": "Concatenate C(12), A(2), B(6).",
        "options": [
            {"label": "A", "text": "312", "is_correct": False},
            {"label": "B", "text": "1226", "is_correct": True},
            {"label": "C", "text": "914", "is_correct": False},
            {"label": "D", "text": "1216", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If A = 3, B = 8, C = 15, D = 24, find the code for DAC.",
        "sample_answer": "Pattern: (n + 1)² − 1 where n is position.\nD = (4+1)² - 1 = 24, A = 3, C = 15.\nCode for DAC = 24-3-15 (24315).",
        "tips": "Formula: (n + 1)² − 1.",
        "options": [
            {"label": "A", "text": "413", "is_correct": False},
            {"label": "B", "text": "24315", "is_correct": True},
            {"label": "C", "text": "16315", "is_correct": False},
            {"label": "D", "text": "24115", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- ADVANCED PLACEMENT LEVEL CODING (Q21 - Q25) ---
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If each letter is moved 3 positions forward, then the whole word is reversed, code INTERVIEW.",
        "sample_answer": "INTERVIEW +3 forward: I(12)=L, N(17)=Q, T(23)=W, E(8)=H, R(21)=U, V(25)=Y, I(12)=L, E(8)=H, W(26)=Z → LQWHUYLHZ.\nReversed → ZHLYUHWQL.",
        "tips": "Shift +3 forward, then reverse the entire string.",
        "options": [
            {"label": "A", "text": "LQWHUYLHZ", "is_correct": False},
            {"label": "B", "text": "ZHLYUHWQL", "is_correct": True},
            {"label": "C", "text": "ZHKXVGVQL", "is_correct": False},
            {"label": "D", "text": "YGLXTGVQK", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If vowels are replaced by the next vowel (A->E, E->I, I->O, O->U, U->A) and consonants by the next consonant, code PLACEMENT.",
        "sample_answer": "P->Q, L->M, A(vowel)->E, C->D, E(vowel)->I, M->N, E(vowel)->I, N->P, T->V.\nCode = QMEDINIPV.",
        "tips": "Vowel order: A->E->I->O->U->A. Consonants shift +1.",
        "options": [
            {"label": "A", "text": "QMEDINIPV", "is_correct": True},
            {"label": "B", "text": "QMBDFNIPT", "is_correct": False},
            {"label": "C", "text": "RMEDJOJPW", "is_correct": False},
            {"label": "D", "text": "QMEDJNIPV", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If odd-position letters move +2 and even-position letters move −1, code COMPUTER.",
        "sample_answer": "C(1, odd)+2=E, O(2, even)-1=N, M(3, odd)+2=O, P(4, even)-1=O, U(5, odd)+2=W, T(6, even)-1=S, E(7, odd)+2=G, R(8, even)-1=Q.\nCode = ENOOWSGQ.",
        "tips": "Odd index: +2, Even index: -1.",
        "options": [
            {"label": "A", "text": "DPNQVUFS", "is_correct": False},
            {"label": "B", "text": "ENOOWSGQ", "is_correct": True},
            {"label": "C", "text": "EONOWSGQ", "is_correct": False},
            {"label": "D", "text": "FNPOXTHR", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If every letter is replaced by its opposite alphabet letter (A↔Z, B↔Y, C↔X ...), code DATABASE.",
        "sample_answer": "D↔W, A↔Z, T↔G, A↔Z, B↔Y, A↔Z, S↔H, E↔V.\nCode = WZGYZYHV.",
        "tips": "Opposite letter sum = 27.",
        "options": [
            {"label": "A", "text": "WZGYZYHV", "is_correct": True},
            {"label": "B", "text": "EBUBCBTF", "is_correct": False},
            {"label": "C", "text": "CZSZARZD", "is_correct": False},
            {"label": "D", "text": "VZFXZXGU", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If every alternate letter (odd positions) is replaced by its opposite alphabet letter while even positions remain unchanged, code SOFTWARE.",
        "sample_answer": "S(1, odd)→H, O(2, even)→O, F(3, odd)→U, T(4, even)→T, W(5, odd)→D, A(6, even)→A, R(7, odd)→I, E(8, even)→E.\nCode = HOUTDAIE.",
        "tips": "Odd position -> opposite letter, Even position -> unchanged.",
        "options": [
            {"label": "A", "text": "HOUTDAIE", "is_correct": True},
            {"label": "B", "text": "HLOUTDAI", "is_correct": False},
            {"label": "C", "text": "TPGUXBSF", "is_correct": False},
            {"label": "D", "text": "HNOUTDIE", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- VERY HARD PATTERN-BASED CODING (Q26 - Q30) ---
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If CAT → 3120 and DOG → 4715, find BAT.",
        "sample_answer": "Pattern: Concatenate letter positions C(3), A(1), T(20) -> 3120.\nBAT = B(2), A(1), T(20) -> 2120.",
        "tips": "Concatenate position numbers.",
        "options": [
            {"label": "A", "text": "2120", "is_correct": True},
            {"label": "B", "text": "2119", "is_correct": False},
            {"label": "C", "text": "3120", "is_correct": False},
            {"label": "D", "text": "2012", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If PEN → 2552 and BOOK → 2151511, find NOTE.",
        "sample_answer": "Pattern: Concatenate direct alphabetical positions N(14), O(15), T(20), E(5).\nNOTE = 1415205.",
        "tips": "Concatenate 1-based positions: N=14, O=15, T=20, E=5.",
        "options": [
            {"label": "A", "text": "1415205", "is_correct": True},
            {"label": "B", "text": "1415195", "is_correct": False},
            {"label": "C", "text": "1315205", "is_correct": False},
            {"label": "D", "text": "1416205", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If APPLE → 11616125, find MANGO.",
        "sample_answer": "Pattern: Concatenate position numbers A(1), P(16), P(16), L(12), E(5).\nMANGO = M(13), A(1), N(14), G(7), O(15) -> 13114715.",
        "tips": "Concatenate letter values M=13, A=1, N=14, G=7, O=15.",
        "options": [
            {"label": "A", "text": "13114715", "is_correct": True},
            {"label": "B", "text": "13115715", "is_correct": False},
            {"label": "C", "text": "12114715", "is_correct": False},
            {"label": "D", "text": "13114815", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If TRAIN → 202118914, find PLANE.",
        "sample_answer": "Pattern: Concatenate alphabetical positions P(16), L(12), A(1), N(14), E(5).\nPLANE = 16121145.",
        "tips": "P=16, L=12, A=1, N=14, E=5.",
        "options": [
            {"label": "A", "text": "16121145", "is_correct": True},
            {"label": "B", "text": "16122145", "is_correct": False},
            {"label": "C", "text": "15121145", "is_correct": False},
            {"label": "D", "text": "16131145", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Coding & Decoding",
        "difficulty": "Hard",
        "question_text": "If COMPUTER → 3151316202151820, find KEYBOARD.",
        "sample_answer": "Pattern: Concatenate position numbers K(11), E(5), Y(25), B(2), O(15), A(1), R(18), D(4).\nKEYBOARD = 115252151184.",
        "tips": "Concatenate position values K=11, E=5, Y=25, B=2, O=15, A=1, R=18, D=4.",
        "options": [
            {"label": "A", "text": "115252151184", "is_correct": True},
            {"label": "B", "text": "115252152184", "is_correct": False},
            {"label": "C", "text": "105252151184", "is_correct": False},
            {"label": "D", "text": "115242151184", "is_correct": False}
        ],
        "correct_option": "A"
    }
]

def seed_coding_decoding():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Coding & Decoding'")
            print(f"Deleted old 'Coding & Decoding' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Logical Reasoning',
                    'Coding & Decoding',
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
    seed_coding_decoding()
