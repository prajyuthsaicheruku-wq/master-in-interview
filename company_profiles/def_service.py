# -*- coding: utf-8 -*-
"""
Verified and distinct profiles for Service & IT Companies:
- TCS (TCS Digital / TCS Prime / TCS Ninja)
- Infosys (Infosys SP / DSE / SE)
- Wipro (Wipro Elite / Turbo)
- Capgemini (Capgemini Exceller)
- Cognizant (Cognizant GenC / GenC Next)
- Tech Mahindra
- HCLTech
- LTIMindtree
- Mphasis
- Hexaware
- Persistent Systems
"""

SERVICE_COMPANIES = {
    'tcs digital': {
        'canonical_name': 'TCS Digital',
        'total_mins': 165,
        'total_qs': 84,
        'roles': 'Systems Engineer (Ninja ₹3.36 LPA) / Digital Innovator (₹7.0 LPA) / TCS Prime (₹9.0 - ₹11.5 LPA)',
        'ctc': '₹3.36 - ₹11.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA / M.Sc (60% or 6.0 CGPA throughout 10th, 12th, UG/PG, max 1 active backlog)',
        'difficulty': 'Moderate - High / TCS NQT Pattern',
        'difficulty_class': 'badge-warning',
        'tagline': 'TCS NQT National Qualifier Test pattern, Foundation & Advanced sections, Advanced Quant, Reasoning & 2 Coding questions.',
        'brand_color': '#1f2937',
        'accent_bg': 'linear-gradient(135deg, #1f2937 0%, #111827 100%)',
        'logo_icon': '💼',
        'logo_image': 'images/tcs.svg',
        'selection_stages': [
            {'step': 1, 'title': 'TCS NQT (Foundation + Advanced)', 'desc': '82 MCQs + 2 Coding Problems | 165 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview (TR)', 'desc': 'Projects, Core CS, DSA, SQL & Cloud | 45 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Managerial Interview (MR)', 'desc': 'Problem Solving & Situational Handling | 30 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'HR Interview', 'desc': 'Document Verification, Relocation & Fit | 20 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: TCS NQT Foundation Section (75 Mins)',
                'sections': [
                    {'name': 'Numerical Ability (Foundation)', 'qs': '20 Qs', 'time': '25 Mins'},
                    {'name': 'Verbal Ability (Foundation)', 'qs': '25 Qs', 'time': '25 Mins'},
                    {'name': 'Reasoning Ability (Foundation)', 'qs': '20 Qs', 'time': '25 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: TCS NQT Advanced Section (90 Mins)',
                'sections': [
                    {'name': 'Advanced Quantitative Ability', 'qs': '10 Qs', 'time': '20 Mins'},
                    {'name': 'Advanced Reasoning Ability', 'qs': '10 Qs', 'time': '15 Mins'},
                    {'name': 'Hands-on Coding (1 Medium + 1 Hard)', 'qs': '2 Qs', 'time': '55 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical & HR Interviews',
                'sections': [
                    {'name': 'TR (DSA, SQL, OOP) + MR + HR Discussion', 'qs': 'Panel', 'time': '60 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Advanced Quantitative Ability', 'icon': '🧮', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['Permutations, Combinations & Probability', 'Geometry, Mensuration & Trigonometry', 'Progressions (AP, GP, HP) & Number Series', 'Mixtures, Allegations, Time & Work']},
            {'category': 'Advanced Reasoning & Logic', 'icon': '🧠', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Complex Seating Arrangements & Puzzles', 'Statement Assumptions & Conclusions', 'Data Sufficiency & Venn Diagrams', 'Flowcharts & Visual Reasoning']},
            {'category': 'Verbal Ability & English', 'icon': '📝', 'qs': '25 Qs', 'time': '25 Mins', 'topics': ['Reading Comprehension & Inferences', 'Sentence Completion & Para Jumbles', 'Error Spotting & Grammar Correction', 'Contextual Phrasal Verbs & Vocabulary']},
            {'category': 'Hands-on Algorithmic Coding', 'icon': '💻', 'qs': '2 Qs', 'time': '55 Mins', 'topics': ['Dynamic Programming & Memoization', 'Array Subarray Sum & Sliding Window', 'Matrix Transformations & Spirals', 'String Palindromes & Anagram Groups']}
        ],
        'faqs': [
            {'q': 'What is the difference between TCS Ninja, Digital, and Prime?', 'a': 'TCS NQT top rankers are interviewed for the TCS Prime (₹9-11.5 LPA) or Digital (₹7.0 LPA) role. Candidates clearing only the Foundation section cutoff qualify for the Ninja (₹3.36 LPA) role.'},
            {'q': 'Is there negative marking in TCS NQT?', 'a': 'No, there is no negative marking in the TCS NQT online exam, but there are strict sectional timers, and you cannot jump between sections.'}
        ],
        'past_papers': [
            {
                'paper_id': 'tcs-set-1',
                'title': 'TCS NQT Advanced Digital & Prime 2025 Model Paper',
                'description': 'Real TCS NQT model paper featuring Advanced Quant and competitive coding problems.',
                'sections': [
                    {
                        'section_name': 'Advanced Quant & Coding',
                        'desc': 'High-weightage TCS NQT exam questions.',
                        'time': '50 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'TCS Advanced Probability Problem',
                                'text': 'A bag contains 5 red, 4 green, and 3 blue balls. If 3 balls are drawn at random without replacement, what is the probability that all 3 balls are of different colors?',
                                'marks': '2 Marks',
                                'options': ['3/11', '5/22', '3/22', '6/11'],
                                'correct': '3/11',
                                'explanation': 'Total balls = 5 + 4 + 3 = 12. Total ways to choose 3 balls = 12C3 = (12 * 11 * 10) / (3 * 2 * 1) = 220. Ways to pick 1 ball of each color = 5C1 * 4C1 * 3C1 = 5 * 4 * 3 = 60. Probability = 60 / 220 = 6 / 22 = 3 / 11.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Equilibrium Index of an Array',
                                'text': 'Given an array of integers `nums`, return the leftmost equilibrium index (an index where the sum of elements to its left equals the sum of elements to its right). Return -1 if no such index exists.',
                                'marks': '4 Marks',
                                'sample_answer': 'def find_middle_index(nums: list[int]) -> int:\n    total_sum = sum(nums)\n    left_sum = 0\n    for i, num in enumerate(nums):\n        if left_sum == total_sum - left_sum - num:\n            return i\n        left_sum += num\n    return -1',
                                'explanation': 'Compute total sum in O(n). Iterate through array maintaining running `left_sum`. The right sum is `total_sum - left_sum - num`. When both match, return current index.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'infosys': {
        'canonical_name': 'Infosys',
        'total_mins': 180,
        'total_qs': 57,
        'roles': 'Specialist Programmer (SP ₹9.5 LPA) / Digital Specialist Engineer (DSE ₹6.25 LPA) / Systems Engineer (SE ₹3.6 LPA)',
        'ctc': '₹3.6 - ₹9.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA / M.Sc in all streams (60% or 6.0 CGPA in 10th, 12th & Graduation)',
        'difficulty': 'Moderate - High / SP & DSE Coding Track',
        'difficulty_class': 'badge-warning',
        'tagline': 'Infosys test pattern, Specialist Programmer (SP) dynamic programming, DSE trees & graphs, and SE aptitude.',
        'brand_color': '#007cc3',
        'accent_bg': 'linear-gradient(135deg, #007cc3 0%, #002e6e 100%)',
        'logo_icon': '🔷',
        'logo_image': 'images/infosys.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Infosys Online Assessment (HackWithInfy / OA)', 'desc': '3 Coding Problems (SP/DSE) OR 54 MCQs (SE) | 180 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (DSA & Projects)', 'desc': 'Algorithms, Complexity, SQL & System Concepts | 45 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'HR & Behavioral Interview', 'desc': 'Values, Communication & Relocation Fit | 20 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Specialist Programmer (SP) & DSE Coding (180 Mins)',
                'sections': [
                    {'name': 'Question 1: Greedy / Strings / Prefix Sums (Easy-Medium)', 'qs': '1 Problem', 'time': '40 Mins'},
                    {'name': 'Question 2: Dynamic Programming / Trees (Medium-Hard)', 'qs': '1 Problem', 'time': '65 Mins'},
                    {'name': 'Question 3: Graphs / Disjoint Set / Hard DP (Hard)', 'qs': '1 Problem', 'time': '75 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Systems Engineer (SE) Aptitude Track (100 Mins)',
                'sections': [
                    {'name': 'Reasoning Ability', 'qs': '15 Qs', 'time': '25 Mins'},
                    {'name': 'Mathematical Ability', 'qs': '10 Qs', 'time': '35 Mins'},
                    {'name': 'Verbal Ability', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'Pseudocode Analysis', 'qs': '5 Qs', 'time': '10 Mins'},
                    {'name': 'Puzzle Solving', 'qs': '4 Qs', 'time': '10 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical & HR Interview',
                'sections': [
                    {'name': 'Code Optimization, Edge Cases & Behavioral Fit', 'qs': 'Interview', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Competitive Coding & DP (SP/DSE)', 'icon': '💻', 'qs': '3 Qs', 'time': '180 Mins', 'topics': ['0/1 Knapsack & Longest Common Subsequence', 'Shortest Path (Dijkstra, Bellman-Ford)', 'Disjoint Set Union (DSU) & Minimum Spanning Tree', 'Bitmask DP & Tree Re-rooting']},
            {'category': 'Mathematical & Quantitative Ability (SE)', 'icon': '🧮', 'qs': '10 Qs', 'time': '35 Mins', 'topics': ['Percentages, Profit & Loss, Simple/Compound Interest', 'Time, Speed & Distance / Train & Boat Problems', 'Permutations & Combinations / Probability', 'Logarithms & Modular Arithmetic']},
            {'category': 'Reasoning & Puzzle Solving', 'icon': '🧠', 'qs': '19 Qs', 'time': '35 Mins', 'topics': ['Grid Logic Puzzles & Cryptarithmetic', 'Data Sufficiency & Seating Arrangements', 'Syllogisms & Logical Deductions', 'Direction Sense & Blood Relations']},
            {'category': 'Verbal Ability & Pseudocode', 'icon': '📝', 'qs': '25 Qs', 'time': '30 Mins', 'topics': ['Reading Comprehension & Critical Analysis', 'Error Correction & Sentence Completion', 'Recursive Function Trace in Pseudocode', 'Array & Pointer Indexing Logic']}
        ],
        'faqs': [
            {'q': 'How many questions must be solved to get an SP (Specialist Programmer) interview?', 'a': 'Solving 2 to 3 coding questions with all test cases passing usually secures an SP (₹9.5 LPA) interview call. Solving 1.5 to 2 questions secures a DSE (₹6.25 LPA) call.'},
            {'q': 'What compiler platform does Infosys use for coding?', 'a': 'Infosys hosts its coding tests on its proprietary platform, supporting C, C++, Java, and Python.'}
        ],
        'past_papers': [
            {
                'paper_id': 'infosys-set-1',
                'title': 'Infosys SP & DSE Coding 2025 Model Paper',
                'description': 'Real Infosys Specialist Programmer dynamic programming and competitive coding challenges.',
                'sections': [
                    {
                        'section_name': 'Advanced Coding Challenge',
                        'desc': 'Dynamic programming and algorithmic problem solving.',
                        'time': '60 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'coding',
                                'title': 'Coin Change Minimum Coins Problem',
                                'text': 'You are given an integer array `coins` representing coins of different denominations and an integer `amount`. Return the fewest number of coins that you need to make up that amount. If not possible, return -1.',
                                'marks': '4 Marks',
                                'sample_answer': 'def coin_change(coins: list[int], amount: int) -> int:\n    dp = [float("inf")] * (amount + 1)\n    dp[0] = 0\n    for coin in coins:\n        for x in range(coin, amount + 1):\n            dp[x] = min(dp[x], dp[x - coin] + 1)\n    return dp[amount] if dp[amount] != float("inf") else -1',
                                'explanation': 'Dynamic programming array `dp[x]` stores the minimum coins needed for amount x. Runs in O(amount * len(coins)) time and O(amount) space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'wipro': {
        'canonical_name': 'Wipro',
        'total_mins': 128,
        'total_qs': 55,
        'roles': 'Project Engineer (Elite ₹3.5 LPA) / Turbo Developer (₹6.5 LPA)',
        'ctc': '₹3.5 - ₹6.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60% or 6.0 CGPA throughout 10th, 12th & Graduation, max 1 backlog)',
        'difficulty': 'Moderate / Elite NTH Pattern',
        'difficulty_class': 'badge-info',
        'tagline': 'Wipro Elite National Talent Hunt (NTH) test pattern, AMCAT Aptitude, Essay Writing & 2 Coding questions.',
        'brand_color': '#341a41',
        'accent_bg': 'linear-gradient(135deg, #341a41 0%, #1e1b4b 100%)',
        'logo_icon': '🟣',
        'logo_image': 'images/wipro.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Wipro Elite Online Assessment', 'desc': '52 MCQs + 1 Essay + 2 Coding | 128 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview (TR)', 'desc': 'OOPs, Java/C++, DBMS & Projects | 30 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'HR Interview', 'desc': 'Work Shift Flexibility & Document Check | 15 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Aptitude Test (48 Mins)',
                'sections': [
                    {'name': 'Quantitative Ability', 'qs': '16 Qs', 'time': '16 Mins'},
                    {'name': 'Logical Reasoning', 'qs': '14 Qs', 'time': '14 Mins'},
                    {'name': 'English Comprehension', 'qs': '22 Qs', 'time': '18 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Written Communication (20 Mins)',
                'sections': [
                    {'name': 'Essay Writing on Current Technology/Social Theme', 'qs': '1 Essay', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Online Coding Test (60 Mins)',
                'sections': [
                    {'name': 'Automata Coding Challenge (1 Easy + 1 Medium)', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Technical & HR Interview',
                'sections': [
                    {'name': 'TR & HR Combined Interview Panel', 'qs': 'Panel', 'time': '35 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative Ability (AMCAT)', 'icon': '🧮', 'qs': '16 Qs', 'time': '16 Mins', 'topics': ['HCF, LCM & Divisibility Rules', 'Percentages, Profit & Loss, Discounts', 'Time & Work, Pipes & Cisterns', 'Speed, Distance & Relative Motion']},
            {'category': 'Logical Reasoning', 'icon': '🧠', 'qs': '14 Qs', 'time': '14 Mins', 'topics': ['Coding-Decoding & Number Series', 'Blood Relations & Direction Sense', 'Data Sufficiency & Statement Assumptions', 'Seating Arrangement Puzzles']},
            {'category': 'Written Communication (Essay)', 'icon': '📝', 'qs': '1 Essay', 'time': '20 Mins', 'topics': ['Grammar & Punctuation Precision', 'Vocabulary & Sentence Structuring', 'Coherent Paragraph Organization (150-400 words)', 'Topical Essay Arguments']},
            {'category': 'Automata Coding (C/C++/Java/Python)', 'icon': '💻', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['Array Operations & Frequency Maps', 'String Pattern Matching & Reversals', 'Matrix Traversals & Sum Calculations', 'Basic Number Theory (GCD, Prime Factors)']}
        ],
        'faqs': [
            {'q': 'What is Wipro Turbo upgrade test?', 'a': 'Candidates who clear the Elite NTH offer are invited to an advanced coding assessment (Turbo test) with a CTC upgrade to ₹6.5 LPA.'}
        ],
        'past_papers': [
            {
                'paper_id': 'wipro-set-1',
                'title': 'Wipro Elite NTH 2025 Model Paper',
                'description': 'Real Wipro Elite assessment with AMCAT quantitative problems and Automata coding.',
                'sections': [
                    {
                        'section_name': 'Aptitude & Coding',
                        'desc': 'Core quantitative ability and coding challenge.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Wipro Quantitative Speed & Distance',
                                'text': 'A train traveling at 72 km/h crosses a 200m long platform in 22 seconds. What is the length of the train?',
                                'marks': '2 Marks',
                                'options': ['240 meters', '200 meters', '220 meters', '260 meters'],
                                'correct': '240 meters',
                                'explanation': 'Speed in m/s = 72 * (5/18) = 20 m/s. Total distance covered in 22 seconds = Speed * Time = 20 * 22 = 440 meters. Distance = Train Length + Platform Length => Train Length = 440 - 200 = 240 meters.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Count Common Elements in Two Sorted Arrays',
                                'text': 'Given two sorted integer arrays `a` and `b`, find the count of elements that appear in both arrays.',
                                'marks': '4 Marks',
                                'sample_answer': 'def count_intersection(a: list[int], b: list[int]) -> int:\n    i = j = count = 0\n    while i < len(a) and j < len(b):\n        if a[i] == b[j]:\n            count += 1\n            i += 1\n            j += 1\n        elif a[i] < b[j]:\n            i += 1\n        else:\n            j += 1\n    return count',
                                'explanation': 'Using two pointers on both sorted arrays allows linear traversal in O(len(a) + len(b)) time and O(1) auxiliary space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'capgemini': {
        'canonical_name': 'Capgemini',
        'total_mins': 120,
        'total_qs': 66,
        'roles': 'Analyst (₹4.25 LPA) / Senior Analyst (₹7.5 LPA)',
        'ctc': '₹4.25 - ₹7.5 LPA',
        'eligibility': 'B.Tech / MCA / M.Tech (60% or 6.0 CGPA throughout 10th, 12th & Graduation, max 1 active backlog)',
        'difficulty': 'Moderate / Exceller Multi-Stage Pattern',
        'difficulty_class': 'badge-info',
        'tagline': 'Capgemini Exceller recruitment pattern, Game-Based Aptitude, Pseudocode, English & Coding assessment.',
        'brand_color': '#0070ad',
        'accent_bg': 'linear-gradient(135deg, #0070ad 0%, #082f49 100%)',
        'logo_icon': '♠️',
        'logo_image': 'images/capgemini.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Capgemini Exceller Online Test', 'desc': 'English + Games + Pseudocode + Coding | 120 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Spoken English Assessment (Versant)', 'desc': 'Pronunciation & Listening Test | 25 Mins', 'icon': '🗣️'},
            {'step': 3, 'title': 'Technical & HR Interview (Combined)', 'desc': 'OOP, SQL, DSA & Behavioral Scenarios | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Technical & Cognitive Assessment',
                'sections': [
                    {'name': 'Technical Pseudocode', 'qs': '30 Qs', 'time': '30 Mins'},
                    {'name': 'English Communication MCQs', 'qs': '30 Qs', 'time': '30 Mins'},
                    {'name': 'Game-Based Aptitude (Grid, Motion, Inductive)', 'qs': '4 Games', 'time': '24 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Hands-on Coding Challenge',
                'sections': [
                    {'name': 'Algorithmic Problem Solving (2 Questions)', 'qs': '2 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Versant English Test',
                'sections': [
                    {'name': 'AI Spoken English Evaluation', 'qs': 'Audio Tasks', 'time': '25 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Technical & HR Interview',
                'sections': [
                    {'name': 'Domain Technical Discussion & HR Fitment', 'qs': 'Interview', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Technical Pseudocode', 'icon': '💻', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Bitwise Operations (&, |, ^, >>, <<)', 'Recursion & Base Cases Tracing', 'Loop Step Counters & Nested Iteration', 'Array & Matrix Index Operations']},
            {'category': 'Game-Based Aptitude', 'icon': '🎮', 'qs': '4 Games', 'time': '24 Mins', 'topics': ['Grid Challenge (Spatial Working Memory)', 'Motion Challenge (Path Obstacle Planning)', 'Inductive Reasoning (Abstract Geometry Patterns)', 'Deductive Reasoning (Switch Challenge)']},
            {'category': 'English Communication', 'icon': '📝', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Reading Comprehension & Critical Analysis', 'Prepositions, Articles & Subject-Verb Agreement', 'Sentence Correction & Idiomatic Phrases', 'Vocabulary In-Context']},
            {'category': 'Hands-on Coding', 'icon': '🎯', 'qs': '2 Qs', 'time': '45 Mins', 'topics': ['Array Sum & Pair Finding', 'String Palindromes & Substring Anagrams', 'Prime Factorization & Modular Math', 'Matrix Diagonal & Spiral Traversals']}
        ],
        'faqs': [
            {'q': 'What are the 4 games in Capgemini Game-Based Aptitude?', 'a': 'The 4 games are Grid Challenge (working memory), Motion Challenge (planning shortest moves), Deductive Switch Challenge, and Inductive Digit Challenge.'}
        ],
        'past_papers': [
            {
                'paper_id': 'capgemini-set-1',
                'title': 'Capgemini Exceller 2025 Model Paper',
                'description': 'Real Capgemini Exceller assessment with Pseudocode questions and hands-on coding.',
                'sections': [
                    {
                        'section_name': 'Pseudocode & Coding',
                        'desc': 'Bitwise pseudocode tracing and string algorithm problem.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Capgemini Bitwise Pseudocode',
                                'text': 'What is the output of the following pseudocode?\n\nInteger p, q, r\nSet p = 5, q = 3, r = 8\np = (p ^ q) + (r >> 2)\nPrint p',
                                'marks': '2 Marks',
                                'options': ['8', '6', '10', '12'],
                                'correct': '8',
                                'explanation': 'p ^ q = 5 ^ 3 = (101 ^ 011) = 110 (6). r >> 2 = 8 >> 2 = 2. So p = 6 + 2 = 8.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Check If String is Anagram',
                                'text': 'Given two strings `s` and `t`, return True if `t` is an anagram of `s`, and False otherwise.',
                                'marks': '4 Marks',
                                'sample_answer': 'def is_anagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    counts = {}\n    for char in s:\n        counts[char] = counts.get(char, 0) + 1\n    for char in t:\n        if char not in counts or counts[char] == 0:\n            return False\n        counts[char] -= 1\n    return True',
                                'explanation': 'Using a character frequency map, verify character counts match exactly across both strings in O(n) time and O(1) space (26 English lowercase letters).'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'cognizant genc': {
        'canonical_name': 'Cognizant GenC',
        'total_mins': 120,
        'total_qs': 67,
        'roles': 'GenC (₹4.0 LPA) / GenC Elevate (₹4.5 LPA) / GenC Next (₹6.75 - ₹9.0 LPA)',
        'ctc': '₹4.0 - ₹9.0 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60% or 6.0 CGPA throughout 10th, 12th & Graduation, max 1 standing backlog)',
        'difficulty': 'Moderate - High / GenC Next Coding Track',
        'difficulty_class': 'badge-warning',
        'tagline': 'Cognizant GenC Next test pattern, Quantitative, Logical, Verbal, CS Fundamentals & HackerEarth Coding.',
        'brand_color': '#0033a0',
        'accent_bg': 'linear-gradient(135deg, #0033a0 0%, #0f172a 100%)',
        'logo_icon': '🔷',
        'logo_image': 'images/cognizant.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Cognizant Online Assessment (AMCAT/HackerEarth)', 'desc': '65 MCQs + 2 Coding Problems | 120 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Communication Assessment (Versant)', 'desc': 'Reading, Listening & Story Retelling | 25 Mins', 'icon': '🗣️'},
            {'step': 3, 'title': 'Technical Interview (TR)', 'desc': 'OOPs, DBMS, Web/Cloud & Projects | 40 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'HR Interview', 'desc': 'Work Location, Shift Readiness & Fitment | 15 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (GenC Next Track)',
                'sections': [
                    {'name': 'Quantitative Aptitude', 'qs': '25 Qs', 'time': '35 Mins'},
                    {'name': 'Logical Reasoning', 'qs': '20 Qs', 'time': '25 Mins'},
                    {'name': 'Verbal Ability', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'Hands-on Coding Challenge (2 Questions)', 'qs': '2 Qs', 'time': '40 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Versant Communication Test',
                'sections': [
                    {'name': 'Spoken English & Listening Comprehension', 'qs': 'Audio Tasks', 'time': '25 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical & HR Interviews',
                'sections': [
                    {'name': 'DSA, Database Queries, System Basics & HR Fit', 'qs': 'Interview', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative Aptitude', 'icon': '🧮', 'qs': '25 Qs', 'time': '35 Mins', 'topics': ['Percentages, Profit & Loss, Simple/Compound Interest', 'Time & Work, Pipes & Cisterns, Work Equivalents', 'Permutations, Combinations & Probability', 'Number Systems, Remainders & LCM/HCF']},
            {'category': 'Logical Reasoning', 'icon': '🧠', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Coding-Decoding & Analogy Series', 'Blood Relations & Direction Vectors', 'Syllogisms & Statement Inferences', 'Seating Arrangement Matrices']},
            {'category': 'Verbal Ability', 'icon': '📝', 'qs': '20 Qs', 'time': '20 Mins', 'topics': ['Reading Comprehension & Central Ideas', 'Sentence Correction & Preposition Usage', 'Synonyms, Antonyms & Contextual Fillers', 'Para Jumbles & Transition Words']},
            {'category': 'Hands-on Coding (DSA)', 'icon': '💻', 'qs': '2 Qs', 'time': '40 Mins', 'topics': ['Two Pointer & Sliding Window Techniques', 'Hash Maps & Subarray Frequency Arrays', 'Matrix Transformations & Spirals', 'Binary Search & Prefix Sums']}
        ],
        'faqs': [
            {'q': 'What is Cognizant GenC Next?', 'a': 'GenC Next is Cognizant\'s premier campus hiring role for full-stack developers and algorithmic engineers offering ₹6.75 to ₹9.0 LPA.'}
        ],
        'past_papers': [
            {
                'paper_id': 'cognizant-set-1',
                'title': 'Cognizant GenC Next 2025 Model Paper',
                'description': 'Real Cognizant GenC Next recruitment test covering Quantitative Aptitude and Coding.',
                'sections': [
                    {
                        'section_name': 'Aptitude & Coding',
                        'desc': 'Core quantitative ability and array coding.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Cognizant Time & Work Problem',
                                'text': 'A can complete a project in 12 days, and B can complete it in 18 days. If they work together for 4 days, what fraction of the project remains incomplete?',
                                'marks': '2 Marks',
                                'options': ['4/9', '5/9', '2/9', '1/3'],
                                'correct': '4/9',
                                'explanation': 'Work done per day by (A + B) = (1/12) + (1/18) = (3 + 2)/36 = 5/36. In 4 days, work completed = 4 * (5/36) = 20/36 = 5/9. Remaining work = 1 - 5/9 = 4/9.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Rotate Array by K Positions',
                                'text': 'Given an array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.',
                                'marks': '4 Marks',
                                'sample_answer': 'def rotate_array(nums: list[int], k: int) -> None:\n    k %= len(nums)\n    def reverse(l, r):\n        while l < r:\n            nums[l], nums[r] = nums[r], nums[l]\n            l += 1\n            r -= 1\n    reverse(0, len(nums) - 1)\n    reverse(0, k - 1)\n    reverse(k, len(nums) - 1)',
                                'explanation': 'Reversing the whole array, then the first k elements, and finally the remaining elements rotates the array in O(n) time and O(1) in-place space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'tech mahindra': {
        'canonical_name': 'Tech Mahindra',
        'total_mins': 100,
        'total_qs': 77,
        'roles': 'Associate Software Engineer (ASE) / SuperCoder (₹5.5 LPA)',
        'ctc': '₹3.25 - ₹5.5 LPA',
        'eligibility': 'B.Tech / MCA (60% or 6.0 CGPA in 10th, 12th & Graduation with no active backlogs)',
        'difficulty': 'Moderate / TechM National Assessment',
        'difficulty_class': 'badge-info',
        'tagline': 'Tech Mahindra test pattern, English essay, CS fundamentals, Quantitative Aptitude & SuperCoder coding.',
        'brand_color': '#d2232a',
        'accent_bg': 'linear-gradient(135deg, #d2232a 0%, #1c1917 100%)',
        'logo_icon': '🔴',
        'logo_image': 'images/techmahindra.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Tech Mahindra Online Assessment', 'desc': '75 MCQs + 2 Coding Problems | 100 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Conversational Test (AI Speech)', 'desc': 'Pronunciation & Reading Assessment | 20 Mins', 'icon': '🗣️'},
            {'step': 3, 'title': 'Technical Interview (TR)', 'desc': 'Programming, OOP, SQL & Web Tech | 30 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'HR Interview', 'desc': 'Fitment, Communication & Relocation | 15 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Aptitude & Technical Assessment',
                'sections': [
                    {'name': 'English Essay & Verbal Ability', 'qs': '25 Qs', 'time': '25 Mins'},
                    {'name': 'Quantitative & Logical Aptitude', 'qs': '35 Qs', 'time': '35 Mins'},
                    {'name': 'CS Fundamentals & Tech MCQs', 'qs': '15 Qs', 'time': '15 Mins'},
                    {'name': 'Hands-on Coding Challenge', 'qs': '2 Qs', 'time': '25 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Conversational Versant Test',
                'sections': [
                    {'name': 'Sentence Mastery & Spoken Fluency', 'qs': 'Audio Tasks', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical & HR Interviews',
                'sections': [
                    {'name': 'Technical TR & Behavioral HR Panel', 'qs': 'Interview', 'time': '35 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative & Logical Aptitude', 'icon': '🧮', 'qs': '35 Qs', 'time': '35 Mins', 'topics': ['Percentages, Profit & Loss, Simple Interest', 'Speed, Time & Distance / Work Formulas', 'Series Completion & Blood Relations', 'Syllogisms & Visual Puzzles']},
            {'category': 'CS Fundamentals & OOPs', 'icon': '💻', 'qs': '15 Qs', 'time': '15 Mins', 'topics': ['C/C++ & Java Core Syntax', 'OOP Concepts (Encapsulation, Polymorphism)', 'Database Normalization & SQL Queries', 'Data Structures (Arrays, Linked Lists, Stacks)']},
            {'category': 'Verbal Ability & Essay', 'icon': '📝', 'qs': '25 Qs', 'time': '25 Mins', 'topics': ['Reading Comprehension & Critical Grammar', 'Error Spotting & Sentence Correction', 'Synonyms & Antonyms', 'Topical Essay Writing']},
            {'category': 'SuperCoder Coding Challenge', 'icon': '🎯', 'qs': '2 Qs', 'time': '25 Mins', 'topics': ['Array Frequency Arrays & Duplicate Removal', 'String Reversals & Vowel Transformations', 'Number Theory (Armstrong, Fibonacci, Palindrome)', 'Matrix Row/Column Sums']}
        ],
        'faqs': [
            {'q': 'What is the SuperCoder track in Tech Mahindra?', 'a': 'Candidates who excel in the hands-on coding section receive a SuperCoder package offer of ₹5.5 LPA instead of the standard ASE ₹3.25 LPA package.'}
        ],
        'past_papers': [
            {
                'paper_id': 'techm-set-1',
                'title': 'Tech Mahindra SuperCoder 2025 Model Paper',
                'description': 'Real Tech Mahindra assessment covering quantitative ability and coding challenges.',
                'sections': [
                    {
                        'section_name': 'Aptitude & Coding',
                        'desc': 'Core quantitative and algorithmic problems.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Tech Mahindra Profit & Loss Problem',
                                'text': 'A merchant sells an article at ₹840, making a profit of 20%. What was the original cost price (CP) of the article?',
                                'marks': '2 Marks',
                                'options': ['₹700', '₹720', '₹680', '₹750'],
                                'correct': '₹700',
                                'explanation': 'Selling Price (SP) = CP * (1 + Profit%) => 840 = CP * 1.20 => CP = 840 / 1.20 = ₹700.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Check If Number is Armstrong Number',
                                'text': 'Write a function to check whether a given positive integer `n` is an Armstrong number (where the sum of its digits raised to the power of the number of digits equals the number itself).',
                                'marks': '4 Marks',
                                'sample_answer': 'def is_armstrong(n: int) -> bool:\n    digits = [int(d) for d in str(n)]\n    num_digits = len(digits)\n    return sum(d ** num_digits for d in digits) == n',
                                'explanation': 'Extract each digit, compute the sum of digits raised to power len(digits), and compare with original integer n.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'hcltech': {
        'canonical_name': 'HCLTech',
        'total_mins': 90,
        'total_qs': 62,
        'roles': 'Graduate Engineer Trainee (GET) / Software Engineer',
        'ctc': '₹4.25 - ₹6.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60% or 6.0 CGPA throughout 10th, 12th & Graduation, no standing backlogs)',
        'difficulty': 'Moderate / First Careers Assessment',
        'difficulty_class': 'badge-info',
        'tagline': 'HCLTech test pattern, Quantitative, Logical, Computer Programming & 2 hands-on coding challenges.',
        'brand_color': '#0066b2',
        'accent_bg': 'linear-gradient(135deg, #0066b2 0%, #0c2d48 100%)',
        'logo_icon': '🌐',
        'logo_image': 'images/hcltech.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HCLTech Online Assessment (Mettl)', 'desc': '60 MCQs + 2 Coding Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview (TR)', 'desc': 'OOPs, Java/C++, SQL, Operating Systems | 35 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'HR Interview', 'desc': 'Communication, Adaptability & Culture Fit | 15 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (Mettl Platform)',
                'sections': [
                    {'name': 'Quantitative Ability', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Logical Reasoning', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Verbal Ability', 'qs': '15 Qs', 'time': '15 Mins'},
                    {'name': 'Technical Domain (CS/IT)', 'qs': '15 Qs', 'time': '15 Mins'},
                    {'name': 'Hands-on Algorithmic Coding', 'qs': '2 Qs', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical & HR Interviews',
                'sections': [
                    {'name': 'Technical TR & Behavioral HR Panel', 'qs': 'Interview', 'time': '40 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative & Logical Ability', 'icon': '🧮', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Percentages, Ratios, Profit & Loss', 'Time & Work, Speed, Distance & Boats', 'Coding-Decoding, Series Completion', 'Blood Relations & Direction Sense']},
            {'category': 'Technical Domain (CS Fundamentals)', 'icon': '💻', 'qs': '15 Qs', 'time': '15 Mins', 'topics': ['OOP Principles (Classes, Objects, Inheritance)', 'DBMS (Keys, Normalization, SQL Joins)', 'Operating Systems (Processes, Paging, Threads)', 'Data Structures (Stack, Queue, Tree Basics)']},
            {'category': 'Verbal Ability', 'icon': '📝', 'qs': '15 Qs', 'time': '15 Mins', 'topics': ['Reading Comprehension & Critical Inferences', 'Sentence Rearrangement & Para Jumbles', 'Grammar Correction & Tenses', 'Vocabulary & Phrasal Idioms']},
            {'category': 'Hands-on Coding', 'icon': '🎯', 'qs': '2 Qs', 'time': '20 Mins', 'topics': ['Array Reversals & Maximum Subarrays', 'String Vowel Counting & Palindromes', 'Binary Number & Bitwise Operations', 'Searching & Sorting Applications']}
        ],
        'faqs': [
            {'q': 'What platform is used for HCLTech online assessment?', 'a': 'HCLTech conducts its first-round online assessments primarily on Mercer Mettl.'}
        ],
        'past_papers': [
            {
                'paper_id': 'hcl-set-1',
                'title': 'HCLTech GET 2025 Model Paper',
                'description': 'Real HCLTech assessment covering CS fundamentals and coding.',
                'sections': [
                    {
                        'section_name': 'Technical & Coding',
                        'desc': 'Core DBMS questions and string coding.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'DBMS Primary Key Constraint',
                                'text': 'Which of the following statements is strictly TRUE regarding a Primary Key in a relational database?',
                                'marks': '2 Marks',
                                'options': [
                                    'A Primary Key uniquely identifies each row and CANNOT contain NULL values.',
                                    'A table can have multiple Primary Keys.',
                                    'A Primary Key allows multiple NULL entries.',
                                    'Primary Keys cannot be referenced by Foreign Keys.'
                                ],
                                'correct': 'A Primary Key uniquely identifies each row and CANNOT contain NULL values.',
                                'explanation': 'By relational database definitions, a table can only have one Primary Key, which must enforce uniqueness and cannot store NULL values.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Remove Duplicates from Sorted Array',
                                'text': 'Given an integer array `nums` sorted in non-decreasing order, remove duplicates in-place such that each unique element appears only once. Return the number of unique elements.',
                                'marks': '4 Marks',
                                'sample_answer': 'def remove_duplicates(nums: list[int]) -> int:\n    if not nums:\n        return 0\n    write_idx = 1\n    for i in range(1, len(nums)):\n        if nums[i] != nums[i - 1]:\n            nums[write_idx] = nums[i]\n            write_idx += 1\n    return write_idx',
                                'explanation': 'Two-pointer approach modifies the array in-place in O(n) time and O(1) auxiliary space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'ltimindtree': {
        'canonical_name': 'LTIMindtree',
        'total_mins': 120,
        'total_qs': 67,
        'roles': 'Graduate Engineer Trainee (GET ₹4.0 LPA) / Software Engineer (₹6.5 LPA)',
        'ctc': '₹4.0 - ₹6.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60% or 6.0 CGPA throughout 10th, 12th & Graduation)',
        'difficulty': 'Moderate / Early Career Hiring Track',
        'difficulty_class': 'badge-info',
        'tagline': 'LTIMindtree recruitment test pattern, Quantitative, Logical, Technical MCQs, Coding & Spoken English test.',
        'brand_color': '#e31b23',
        'accent_bg': 'linear-gradient(135deg, #e31b23 0%, #1f2937 100%)',
        'logo_icon': '🔴',
        'logo_image': 'images/ltimindtree.svg',
        'selection_stages': [
            {'step': 1, 'title': 'LTIMindtree Online Assessment', 'desc': '65 MCQs + 2 Coding Problems | 120 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Spoken English Assessment', 'desc': 'Pronunciation & Listening Test | 20 Mins', 'icon': '🗣️'},
            {'step': 3, 'title': 'Technical Interview (TR)', 'desc': 'Data Structures, Java/Python, DB & Cloud | 35 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'HR Interview', 'desc': 'Values, Communication & Flexibility | 15 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (Superset/Mettl)',
                'sections': [
                    {'name': 'Quantitative Aptitude', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'Logical Reasoning', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'Verbal Ability', 'qs': '15 Qs', 'time': '15 Mins'},
                    {'name': 'Technical MCQs (CS/Cloud)', 'qs': '10 Qs', 'time': '15 Mins'},
                    {'name': 'Hands-on Algorithmic Coding', 'qs': '2 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical & HR Interviews',
                'sections': [
                    {'name': 'Technical Discussion & HR Fitment Panel', 'qs': 'Interview', 'time': '40 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative Aptitude', 'icon': '🧮', 'qs': '20 Qs', 'time': '20 Mins', 'topics': ['Percentages, Profit & Loss, Ratios', 'Time, Speed & Distance / Work', 'Permutations & Combinations', 'Data Interpretation & Graphs']},
            {'category': 'Logical Reasoning', 'icon': '🧠', 'qs': '20 Qs', 'time': '20 Mins', 'topics': ['Coding-Decoding & Series', 'Syllogisms & Analytical Puzzles', 'Blood Relations & Direction Vectors', 'Statement & Assumptions']},
            {'category': 'Technical CS & Cloud MCQs', 'icon': '💻', 'qs': '10 Qs', 'time': '15 Mins', 'topics': ['OOP Concepts & Java/Python Syntax', 'SQL Queries & ACID Properties', 'Cloud Computing Basics (AWS/Azure)', 'Data Structures (Arrays, Linked Lists)']},
            {'category': 'Hands-on Coding', 'icon': '🎯', 'qs': '2 Qs', 'time': '45 Mins', 'topics': ['Array Difference & Sorting', 'String Character Counting & Inversions', 'Matrix Operations', 'Prefix Sums & Sliding Windows']}
        ],
        'faqs': [
            {'q': 'What role packages does LTIMindtree offer on campus?', 'a': 'LTIMindtree offers the Level 1 GET role (₹4.0 LPA) and Level 2 high-performer coding role (₹6.5 LPA).'}
        ],
        'past_papers': [
            {
                'paper_id': 'lti-set-1',
                'title': 'LTIMindtree GET 2025 Model Paper',
                'description': 'Real LTIMindtree campus placement test covering aptitude, CS core, and coding.',
                'sections': [
                    {
                        'section_name': 'Aptitude & Coding',
                        'desc': 'Core quantitative and coding questions.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'LTIMindtree Ratio & Proportion',
                                'text': 'The ratio of boys to girls in a class is 4 : 5. If 6 boys join and 6 girls leave, the ratio becomes 1 : 1. How many total students were initially in the class?',
                                'marks': '2 Marks',
                                'options': ['108', '90', '72', '54'],
                                'correct': '108',
                                'explanation': 'Let initial boys = 4x and girls = 5x. According to the problem: (4x + 6) / (5x - 6) = 1/1 => 4x + 6 = 5x - 6 => 5x - 4x = 6 + 6 => x = 12. Total initial students = 4x + 5x = 9x = 9 * 12 = 108.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Find Maximum Product of Two Elements',
                                'text': 'Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`.',
                                'marks': '4 Marks',
                                'sample_answer': 'def max_product(nums: list[int]) -> int:\n    m1 = m2 = 0\n    for n in nums:\n        if n > m1:\n            m2 = m1\n            m1 = n\n        elif n > m2:\n            m2 = n\n    return (m1 - 1) * (m2 - 1)',
                                'explanation': 'Find the two largest numbers in the array in a single pass O(n) time and O(1) space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'mphasis': {
        'canonical_name': 'Mphasis',
        'total_mins': 105,
        'total_qs': 72,
        'roles': 'Associate Software Engineer (₹3.5 - ₹5.0 LPA)',
        'ctc': '₹3.5 - ₹5.0 LPA',
        'eligibility': 'B.Tech / MCA (60% or 6.0 CGPA in 10th, 12th & Graduation)',
        'difficulty': 'Moderate / AMCAT Test Pattern',
        'difficulty_class': 'badge-info',
        'tagline': 'Mphasis recruitment test pattern, Quantitative, Logical, Computer Programming & Automata coding.',
        'brand_color': '#0f4c81',
        'accent_bg': 'linear-gradient(135deg, #0f4c81 0%, #1e293b 100%)',
        'logo_icon': '🔷',
        'logo_image': 'images/mphasis.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Mphasis Online Assessment (AMCAT)', 'desc': '70 MCQs + 2 Coding Problems | 105 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview (TR)', 'desc': 'OOPs, Java/C, SQL & Basic DSA | 30 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'HR Interview', 'desc': 'Communication, Shift Flexibility & Fit | 15 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (AMCAT Platform)',
                'sections': [
                    {'name': 'Quantitative Ability', 'qs': '25 Qs', 'time': '25 Mins'},
                    {'name': 'Logical Reasoning', 'qs': '25 Qs', 'time': '25 Mins'},
                    {'name': 'English Comprehension', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'Automata Coding (2 Questions)', 'qs': '2 Qs', 'time': '35 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical & HR Interviews',
                'sections': [
                    {'name': 'Technical Project Review & HR Fitment', 'qs': 'Interview', 'time': '35 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative Ability', 'icon': '🧮', 'qs': '25 Qs', 'time': '25 Mins', 'topics': ['LCM, HCF & Number Divisibility', 'Percentages, Profit & Loss', 'Time, Work, Speed & Distance', 'Permutations & Probability']},
            {'category': 'Logical Reasoning', 'icon': '🧠', 'qs': '25 Qs', 'time': '25 Mins', 'topics': ['Coding-Decoding & Analogies', 'Blood Relations & Direction Sense', 'Data Sufficiency & Seating Puzzles', 'Statement Arguments & Assumptions']},
            {'category': 'English Comprehension', 'icon': '📝', 'qs': '20 Qs', 'time': '20 Mins', 'topics': ['Short Passage Reading Comprehension', 'Sentence Correction & Grammar', 'Synonyms & Antonyms', 'Vocabulary In-Context']},
            {'category': 'Automata Coding', 'icon': '💻', 'qs': '2 Qs', 'time': '35 Mins', 'topics': ['Array Transformations & Counts', 'String Palindromes & Formatting', 'Matrix Rotations', 'Basic Arithmetic Algorithms']}
        ],
        'faqs': [
            {'q': 'What platform is used for Mphasis campus test?', 'a': 'Mphasis uses the Aspiring Minds AMCAT assessment platform.'}
        ],
        'past_papers': [
            {
                'paper_id': 'mphasis-set-1',
                'title': 'Mphasis AMCAT 2025 Model Paper',
                'description': 'Real Mphasis assessment covering AMCAT aptitude and Automata coding.',
                'sections': [
                    {
                        'section_name': 'AMCAT Quantitative & Coding',
                        'desc': 'Core quantitative and coding questions.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'AMCAT Number Divisibility',
                                'text': 'What is the least number which when divided by 6, 9, 12, and 18 leaves a remainder of 2 in each case?',
                                'marks': '2 Marks',
                                'options': ['38', '36', '74', '56'],
                                'correct': '38',
                                'explanation': 'LCM(6, 9, 12, 18) = 36. Required least number = LCM + Remainder = 36 + 2 = 38.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Check If Array is Monotonic',
                                'text': 'An array is monotonic if it is either monotone increasing or monotone decreasing. Return True if the given array `nums` is monotonic, or False otherwise.',
                                'marks': '4 Marks',
                                'sample_answer': 'def is_monotonic(nums: list[int]) -> bool:\n    increasing = decreasing = True\n    for i in range(len(nums) - 1):\n        if nums[i] > nums[i + 1]:\n            increasing = False\n        if nums[i] < nums[i + 1]:\n            decreasing = False\n    return increasing or decreasing',
                                'explanation': 'Track both increasing and decreasing flags in a single pass O(n) time and O(1) space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'hexaware': {
        'canonical_name': 'Hexaware',
        'total_mins': 100,
        'total_qs': 62,
        'roles': 'Graduate Engineer Trainee (GET ₹4.0 LPA) / Premier Candidate (₹6.0 LPA)',
        'ctc': '₹4.0 - ₹6.0 LPA',
        'eligibility': 'B.Tech / MCA (60% or 6.0 CGPA throughout 10th, 12th & Graduation, no active backlogs)',
        'difficulty': 'Moderate / Hexaware Premier Track',
        'difficulty_class': 'badge-info',
        'tagline': 'Hexaware Premier Graduate test pattern, Aptitude, Domain CS, 2 Coding questions & Communication test.',
        'brand_color': '#e84d0e',
        'accent_bg': 'linear-gradient(135deg, #e84d0e 0%, #1c1917 100%)',
        'logo_icon': '🟠',
        'logo_image': 'images/hexaware.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Hexaware Online Assessment (Mettl)', 'desc': '60 MCQs + 2 Coding Problems | 100 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Communication Assessment (Mettl Speech)', 'desc': 'Fluency, Reading & Pronunciation | 20 Mins', 'icon': '🗣️'},
            {'step': 3, 'title': 'Technical Interview (TR)', 'desc': 'Java/Python, OOP, Database & Projects | 35 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'HR Interview', 'desc': 'Values, Communication & Flexibility | 15 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (Mettl Platform)',
                'sections': [
                    {'name': 'Aptitude (Quant, Logical, Verbal)', 'qs': '40 Qs', 'time': '40 Mins'},
                    {'name': 'Domain Technical MCQs (CS/IT)', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'Hands-on Algorithmic Coding Challenge', 'qs': '2 Qs', 'time': '40 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Communication Test',
                'sections': [
                    {'name': 'Audio Evaluation & Spoken Fluency', 'qs': 'Audio Tasks', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical & HR Interviews',
                'sections': [
                    {'name': 'Technical Project Review & HR Fitment Panel', 'qs': 'Interview', 'time': '40 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative & Logical Aptitude', 'icon': '🧮', 'qs': '40 Qs', 'time': '40 Mins', 'topics': ['Percentages, Profit & Loss, Simple Interest', 'Speed, Time & Distance / Work', 'Coding-Decoding & Analytical Puzzles', 'Syllogisms & Blood Relations']},
            {'category': 'Domain Technical (CS Fundamentals)', 'icon': '💻', 'qs': '20 Qs', 'time': '20 Mins', 'topics': ['OOP Principles (Java / C++)', 'Database Normalization & SQL Queries', 'Data Structures (Arrays, Trees, Hash Tables)', 'Web Fundamentals & REST APIs']},
            {'category': 'Hands-on Coding Challenges', 'icon': '🎯', 'qs': '2 Qs', 'time': '40 Mins', 'topics': ['Array Sum Pairs & Duplicate Elimination', 'String Anagrams & Reversals', 'Matrix Traversals', 'Sorting & Binary Searching']}
        ],
        'faqs': [
            {'q': 'What packages does Hexaware offer?', 'a': 'Hexaware offers the Standard GET role (₹4.0 LPA) and the Premier Graduate role (₹6.0 LPA) for top coding performers.'}
        ],
        'past_papers': [
            {
                'paper_id': 'hex-set-1',
                'title': 'Hexaware Premier Graduate 2025 Model Paper',
                'description': 'Real Hexaware recruitment test covering CS fundamentals and coding.',
                'sections': [
                    {
                        'section_name': 'Domain CS & Coding',
                        'desc': 'Core OOP and coding questions.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'OOP Polymorphism in Java',
                                'text': 'Which of the following demonstrates Runtime (Dynamic) Polymorphism in Java?',
                                'marks': '2 Marks',
                                'options': [
                                    'Method Overriding',
                                    'Method Overloading',
                                    'Operator Overloading',
                                    'Encapsulation using private variables'
                                ],
                                'correct': 'Method Overriding',
                                'explanation': 'Method overriding is resolved at runtime via the dynamic method dispatch mechanism in Java.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Find First Unique Character in a String',
                                'text': 'Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.',
                                'marks': '4 Marks',
                                'sample_answer': 'def first_unique_char(s: str) -> int:\n    counts = {}\n    for char in s:\n        counts[char] = counts.get(char, 0) + 1\n    for i, char in enumerate(s):\n        if counts[char] == 1:\n            return i\n    return -1',
                                'explanation': 'Use a hash map to count character frequencies, then scan the string to return the first index with frequency 1. Runs in O(n) time.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'persistent systems': {
        'canonical_name': 'Persistent Systems',
        'total_mins': 110,
        'total_qs': 62,
        'roles': 'Software Engineer (₹5.0 LPA) / Lead Engineer Track (₹9.0 LPA)',
        'ctc': '₹5.0 - ₹9.0 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60% or 6.0 CGPA throughout 10th, 12th & Graduation, no standing backlogs)',
        'difficulty': 'Moderate - High / CS Core & Algorithmic Track',
        'difficulty_class': 'badge-warning',
        'tagline': 'Persistent Systems placement test pattern, CS Core (OS, DBMS, Networks), Aptitude & 2 DSA coding questions.',
        'brand_color': '#f26522',
        'accent_bg': 'linear-gradient(135deg, #f26522 0%, #1e293b 100%)',
        'logo_icon': '⚡',
        'logo_image': 'images/persistent.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Persistent Online Technical Assessment', 'desc': '60 MCQs (CS Core & Apti) + 2 Coding | 110 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (Core CS & DSA)', 'desc': 'Data Structures, OS, DBMS & Algorithms | 45 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Interview 2 (System Design & Projects)', 'desc': 'Architecture, OOP & Problem Solving | 45 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'HR Fitment Round', 'desc': 'Culture, Communication & Career Goals | 20 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (Wheebox/HackerEarth)',
                'sections': [
                    {'name': 'CS Core (OS, DBMS, CN, Data Structures)', 'qs': '40 Qs', 'time': '45 Mins'},
                    {'name': 'Quantitative & Logical Aptitude', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'Hands-on Algorithmic Coding (2 Questions)', 'qs': '2 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview 1',
                'sections': [
                    {'name': 'Deep DSA, Complexity Analysis & Database Indexing', 'qs': 'Technical', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical Interview 2 & HR',
                'sections': [
                    {'name': 'System Scenarios, Web Architecture & HR Fitment', 'qs': 'Panel', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Computer Science Core Fundamentals', 'icon': '💻', 'qs': '40 Qs', 'time': '45 Mins', 'topics': ['OS: Deadlocks, Virtual Memory, Scheduling Algorithms', 'DBMS: B+ Tree Indexing, Transactions, Normal Forms', 'CN: TCP 3-Way Handshake, DNS, Subnetting', 'Data Structures: Hash Tables, Binary Trees, Heaps']},
            {'category': 'Quantitative & Analytical Aptitude', 'icon': '🧮', 'qs': '20 Qs', 'time': '20 Mins', 'topics': ['Permutations, Combinations & Probability', 'Time & Work, Speed, Distance & Clocks', 'Data Sufficiency & Analytical Reasoning', 'Puzzles & Syllogisms']},
            {'category': 'Algorithmic Coding (DSA)', 'icon': '🎯', 'qs': '2 Qs', 'time': '45 Mins', 'topics': ['Binary Tree Traversal (Inorder, Level Order)', 'Dynamic Programming (Knapsack, Subsets)', 'Graph BFS/DFS & Cycle Detection', 'Array Sliding Window & Two Pointers']}
        ],
        'faqs': [
            {'q': 'What does Persistent Systems test most heavily?', 'a': 'Persistent Systems tests Computer Science fundamentals (OS, DBMS, Networks, Data Structures) much more deeply than standard IT service companies.'},
            {'q': 'What roles are offered by Persistent Systems?', 'a': 'Persistent offers the Software Engineer role (₹5.0 LPA) and higher packages (₹7.0 - ₹9.0 LPA) for candidates who clear advanced DSA coding rounds.'}
        ],
        'past_papers': [
            {
                'paper_id': 'persistent-set-1',
                'title': 'Persistent Systems CS Core & DSA 2025 Model Paper',
                'description': 'Real Persistent Systems assessment covering OS/DBMS fundamentals and DSA coding.',
                'sections': [
                    {
                        'section_name': 'CS Core & Coding',
                        'desc': 'Core OS scheduling and binary tree coding.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'OS Deadlock Necessary Conditions',
                                'text': 'Which of the following is NOT one of Coffman\'s four necessary conditions for deadlock in an operating system?',
                                'marks': '2 Marks',
                                'options': [
                                    'Preemption Allowed',
                                    'Mutual Exclusion',
                                    'Hold and Wait',
                                    'Circular Wait'
                                ],
                                'correct': 'Preemption Allowed',
                                'explanation': 'The four Coffman conditions for deadlock are: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. If preemption is allowed, deadlock cannot occur.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Maximum Depth of Binary Tree',
                                'text': 'Given the root of a binary tree, return its maximum depth (the number of nodes along the longest path from root down to the farthest leaf node).',
                                'marks': '4 Marks',
                                'sample_answer': 'def max_depth(root) -> int:\n    if not root:\n        return 0\n    return 1 + max(max_depth(root.left), max_depth(root.right))',
                                'explanation': 'Recursive post-order traversal computes 1 + max(left_depth, right_depth) in O(n) time and O(height) call-stack space.'
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
