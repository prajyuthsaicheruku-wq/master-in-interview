# -*- coding: utf-8 -*-
FINANCE_COMPANIES = {
    'goldman sachs': {
        'canonical_name': 'Goldman Sachs',
        'total_mins': 135,
        'total_qs': 66,
        'roles': 'New Analyst / Summer Analyst (Engineering & Global Investment Research)',
        'ctc': '₹24.0 - ₹34.0 LPA',
        'eligibility': 'B.Tech / Dual Degree in CS/IT/ECE/Math/Stats (7.0+ CGPA with no backlogs)',
        'difficulty': 'Hard / Quant & Systems',
        'difficulty_class': 'badge-danger',
        'tagline': 'Goldman Sachs recruitment test pattern, probability, advanced math, high-frequency algorithms & past papers.',
        'brand_color': '#7399c6',
        'accent_bg': 'linear-gradient(135deg, #7399c6 0%, #1e3a8a 100%)',
        'logo_icon': '💰',
        'logo_image': 'images/goldmansachs.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank Aptitude & Coding OA', 'desc': '66 Questions | 135 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (DSA & Math)', 'desc': 'Algorithms & Probability | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Round 2 (Systems & DB)', 'desc': 'Low-Level Design & Concurrency | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Techno-Financial Fitment', 'desc': 'Financial Markets Logic & Projects | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Managing Director (MD) Round', 'desc': 'Behavioral & Leadership Scenarios | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: HackerRank OA',
                'sections': [
                    {'name': 'Numerical & Probability Aptitude', 'qs': '8 Qs', 'time': '25 Mins'},
                    {'name': 'Computer Science Core MCQs', 'qs': '7 Qs', 'time': '20 Mins'},
                    {'name': 'Algorithmic Coding Challenge', 'qs': '2 Qs', 'time': '45 Mins'},
                    {'name': 'Advanced Quantitative / Subjective Math', 'qs': '1 Q', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA & Math',
                'sections': [
                    {'name': 'Binary Trees, Graphs & Dynamic Programming', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Systems & LLD',
                'sections': [
                    {'name': 'Order Book Matching Engine / Multi-threading', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: MD Round',
                'sections': [
                    {'name': 'Managing Director Behavioral & Analytical Fit', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Probability & Quantitative Math', 'icon': '🧠', 'qs': '35 Qs', 'time': '45 Mins', 'topics': ['Bayes Theorem & Conditional Probability', 'Combinatorics & Permutations', 'Markov Chains & Expected Values', 'Linear Algebra & Matrices']},
            {'category': 'Data Structures & Algorithms', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['Two Pointers & Sliding Window', 'Graph Shortest Path & Topo Sort', 'Dynamic Programming on Grids', 'Priority Queues & Heaps']},
            {'category': 'Core CS & Operating Systems', 'icon': '⚡', 'qs': '25 Qs', 'time': '30 Mins', 'topics': ['Mutexes, Semaphores & Deadlock', 'Memory Virtualization & Paging', 'Database Normalization & ACID', 'TCP/IP Sockets & Latency Optimization']},
            {'category': 'Financial Engineering & LLD', 'icon': '🎯', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['Limit Order Book Matching Engine', 'Portfolio Return Calculation', 'Stock Price Anomaly Detection', 'Thread-Safe Financial Ledger']}
        ],
        'faqs': [
            {'q': 'What is the format of the Goldman Sachs Online Assessment?', 'a': 'The HackerRank test lasts 135 minutes with 4 sections: Numerical Computation, CS MCQs, 2 Coding Questions, and an Advanced Math/Quant subjective section.'},
            {'q': 'Is there negative marking in Goldman Sachs OA?', 'a': 'Yes, MCQ sections carry negative marking (+5 for correct and -2 for incorrect answers).'},
            {'q': 'How important is probability and statistics for Goldman Sachs engineering roles?', 'a': 'Very important. Goldman Sachs heavily tests math puzzles, probability distributions, expected value problems, and combinatorics alongside DSA.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Goldman Sachs Global Analyst Test Model 1',
                'total_qs': 66,
                'duration': '135 Mins',
                'sample_coding': 'Given an array of stock trade timestamps and prices, find the maximum profit possible from executing up to K non-overlapping transactions in O(NK) time.',
                'sample_quant': 'A biased coin lands heads with probability 2/3. What is the expected number of tosses until two consecutive heads appear?',
                'sample_tech': 'Explain how a Limit Order Book matching engine is implemented using price-priority queues and hash maps for O(1) order execution.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Goldman Sachs Onsite Technical & Math Model 2',
                'total_qs': 66,
                'duration': '135 Mins',
                'sample_coding': 'Implement a thread-safe multi-currency exchange rate graph calculator finding the best arbitrage opportunity in O(V*E) time.',
                'sample_quant': 'There are 100 light bulbs and 100 people. Person K toggles every Kth bulb. Which bulbs remain on after all 100 people complete their turns?',
                'sample_tech': 'Describe the difference between optimistic concurrency control and two-phase locking in high-throughput trading databases.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Goldman Sachs University Solved Paper Model 3',
                'total_qs': 66,
                'duration': '135 Mins',
                'sample_coding': 'Find the median of two sorted arrays of different sizes in O(log(min(N, M))) logarithmic time.',
                'sample_quant': 'Calculate the probability that in a randomly selected group of 23 individuals, at least two share the exact same birthday.',
                'sample_tech': 'What is cache-friendly data alignment, and why is structure padding critical in ultra-low latency C++ trading systems?'
            }
        ]
    },

    'jpmorgan chase': {
        'canonical_name': 'JPMorgan Chase',
        'total_mins': 90,
        'total_qs': 2,
        'roles': 'Software Engineer (Code for Good / Campus Hire)',
        'ctc': '₹17.0 - ₹24.0 LPA',
        'eligibility': '7.0+ CGPA in B.E/B.Tech (CS/IT/ECE/EE with no active backlogs)',
        'difficulty': 'Moderate to Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'JPMorgan Chase recruitment test pattern, Code for Good hackathon, algorithms & solved papers.',
        'brand_color': '#1170cf',
        'accent_bg': 'linear-gradient(135deg, #1170cf 0%, #0369a1 100%)',
        'logo_icon': '🏦',
        'logo_image': 'images/jpmorgan.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank Online Coding Test', 'desc': '2 DSA Problems | 60 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'HireVue Video Interview', 'desc': '2 Behavioral Video Questions | 15 Mins', 'icon': '📹'},
            {'step': 3, 'title': 'Code for Good Hackathon', 'desc': '24-Hour Non-Profit Hackathon | 24 Hrs', 'icon': '⚡'},
            {'step': 4, 'title': 'SME Technical Interview', 'desc': 'System Design & Code Review | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Values & Leadership Round', 'desc': 'Business Principles & Fitment | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: HackerRank OA',
                'sections': [
                    {'name': 'Medium Algorithmic Problem', 'qs': '1 Q', 'time': '30 Mins'},
                    {'name': 'Hard Graph / DP Problem', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: HireVue',
                'sections': [
                    {'name': 'Behavioral & Situational Video Responses', 'qs': '2 Qs', 'time': '15 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Code for Good',
                'sections': [
                    {'name': '24-Hour Team Hackathon for NGO Problem Statements', 'qs': '1 Project', 'time': '24 Hrs'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Dynamic Programming Arrays', 'Graph Breadth/Depth Search', 'Tree Traversals & LCA', 'Hash Maps & Heaps']},
            {'category': 'Database & SQL Engineering', 'icon': '💻', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Relational Indexing & Joins', 'Transactions & Isolation Levels', 'Stored Procedures & Triggers', 'NoSQL vs RDBMS Trades']},
            {'category': 'Web & Software Engineering', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['RESTful Microservices Design', 'Spring Boot / Node.js Frameworks', 'Docker & Containerization', 'Git & CI/CD Pipelines']},
            {'category': 'Hackathon & Problem Solving', 'icon': '🎯', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['Payment Gateway Simulation', 'Charity Donation Allocation', 'Volunteer Matching Engine', 'Automated Financial Reporting']}
        ],
        'faqs': [
            {'q': 'What is JPMorgan Chase\'s Code for Good hackathon?', 'a': 'A prestigious 24-hour hackathon where selected students collaborate in teams of 5-7 to build tech solutions for non-profit organizations, with JPMC mentors evaluating code, teamwork, and leadership.'},
            {'q': 'How does HireVue video assessment work at JPMC?', 'a': 'Candidates record video responses to 2 situational behavioral questions (e.g. overcoming conflict, team collaboration) with 30 seconds prep and 2 minutes recording per question.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'JPMorgan Chase Code for Good OA Model 1',
                'total_qs': 2,
                'duration': '60 Mins',
                'sample_coding': 'Given an array of account transaction values, find the maximum sum contiguous subsegment with at most one value reduction operation.',
                'sample_quant': 'In an inter-bank payment settlement network, find if all accounts can achieve zero net balance using minimum currency transfers.',
                'sample_tech': 'Explain how Spring Boot handles dependency injection and lifecycle management for enterprise banking beans.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'JPMorgan Chase Technical Interview Model 2',
                'total_qs': 2,
                'duration': '60 Mins',
                'sample_coding': 'Implement an automated fraud detection filter that flags any user account making 3 transactions in distinct cities within 1 hour.',
                'sample_quant': 'Given a connected network of bank branch servers, find the minimum cost spanning tree using Kruskal\'s algorithm.',
                'sample_tech': 'Differentiate between optimistic locking and pessimistic row locks when updating bank balance records.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'JPMC Campus Drive Solved Paper Model 3',
                'total_qs': 2,
                'duration': '60 Mins',
                'sample_coding': 'Find the longest palindromic subsequence in a transaction reference string using Dynamic Programming in O(N^2) time.',
                'sample_quant': 'Calculate the total number of valid permutations for assigning 5 credit risk tiers to 10 loan applicants under order constraints.',
                'sample_tech': 'What are microservices design patterns for distributed transactions, and how does the Saga pattern ensure data consistency?'
            }
        ]
    },

    'morgan stanley': {
        'canonical_name': 'Morgan Stanley',
        'total_mins': 90,
        'total_qs': 23,
        'roles': 'Technology Analyst / Associate Software Engineer',
        'ctc': '₹20.0 - ₹28.0 LPA',
        'eligibility': '7.0+ CGPA in B.E/B.Tech (CS/IT/ECE) with strong CS core fundamentals',
        'difficulty': 'Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'Morgan Stanley Technology Analyst placement pattern, C++/Java internals, algorithms & solved papers.',
        'brand_color': '#002b49',
        'accent_bg': 'linear-gradient(135deg, #002b49 0%, #005088 100%)',
        'logo_icon': '📊',
        'logo_image': 'images/morganstanley.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Assessment (HackerRank)', 'desc': '20 MCQs + 3 Coding Qs | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (DSA)', 'desc': 'Trees, Graphs, Recursion | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Round 2 (OS/OOP)', 'desc': 'Multithreading & C++/Java Internals | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Technical Round 3 (LLD)', 'desc': 'Class Design & Database Schema | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Executive Director / HR', 'desc': 'Behavioral & Morgan Stanley Values | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'CS Core MCQs (OS, DBMS, OOP, Java/C++)', 'qs': '20 Qs', 'time': '30 Mins'},
                    {'name': 'Algorithmic Coding Challenge', 'qs': '3 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Interview',
                'sections': [
                    {'name': 'Binary Trees, BSTs & Dynamic Programming', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Systems & LLD',
                'sections': [
                    {'name': 'Multithreading, Deadlocks & Design Patterns', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Binary Trees & Graph Traversals', 'Dynamic Programming on Strings', 'Priority Queues & Disjoint Sets', 'Bit Manipulation & Math']},
            {'category': 'Object Oriented Programming & Java/C++', 'icon': '💻', 'qs': '35 Qs', 'time': '40 Mins', 'topics': ['Virtual Tables & Memory Layout', 'Garbage Collection Mechanisms', 'Generics & Templates', 'Design Patterns (Singleton, Factory)']},
            {'category': 'Operating Systems & DBMS', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Multithreading & Mutex Locks', 'Process vs Thread Memory Spaces', 'B+ Tree Indexing & SQL Joins', 'ACID Transactions & Isolation Levels']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '60 Mins', 'topics': ['Stock Ticker Real-Time Sliding Window', 'Currency Arbitrage Graph Cycle', 'Thread-Safe Fixed-Size Cache', 'Valid Parentheses String Optimization']}
        ],
        'faqs': [
            {'q': 'What programming languages are most valued at Morgan Stanley?', 'a': 'Java and C++ are the primary languages utilized in enterprise financial backends and algorithmic trading engines.'},
            {'q': 'Does Morgan Stanley test CS fundamentals in depth?', 'a': 'Yes, candidates are probed deeply on memory layout, virtual tables, synchronization primitives, garbage collection, and database indexes.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Morgan Stanley Technology Analyst OA Model 1',
                'total_qs': 23,
                'duration': '90 Mins',
                'sample_coding': 'Given a stream of real-time trade quotes with prices and timestamps, design a data structure that returns minimum, maximum, and average price in O(1) time.',
                'sample_quant': 'In an undirected graph with N vertices and M edges, find the number of connected components and return the largest component diameter.',
                'sample_tech': 'Explain how Java Garbage Collectors (G1 GC vs ZGC) manage heap memory and mitigate stop-the-world pauses.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Morgan Stanley Technical Onsite Model 2',
                'total_qs': 23,
                'duration': '90 Mins',
                'sample_coding': 'Implement a thread-safe singleton pattern using double-checked locking in Java/C++ and explain memory barriers.',
                'sample_quant': 'Find the maximum sum path from root to any leaf in a binary tree with positive and negative node weights.',
                'sample_tech': 'What is the difference between clustered and non-clustered indexes in Microsoft SQL Server / Oracle databases?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Morgan Stanley Campus Drive Solved Paper Model 3',
                'total_qs': 23,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of integer stock values, compute the longest increasing subsequence in O(N log N) time using binary search.',
                'sample_quant': 'Calculate the total number of distinct binary search trees that can be constructed with N unique keys using Catalan numbers.',
                'sample_tech': 'Explain deadlock conditions (Coffman conditions) and how the banker\'s algorithm prevents resource deadlocks in OS.'
            }
        ]
    },

    'american express': {
        'canonical_name': 'American Express',
        'total_mins': 90,
        'total_qs': 18,
        'roles': 'Engineer Trainee / Software Engineer - 1 (Payment & Risk Technologies)',
        'ctc': '₹16.0 - ₹24.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT/ECE (6.5+ CGPA with no active arrears)',
        'difficulty': 'Moderate to Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'American Express software engineering test pattern, payment systems, DSA & solved model papers.',
        'brand_color': '#006fcf',
        'accent_bg': 'linear-gradient(135deg, #006fcf 0%, #0284c7 100%)',
        'logo_icon': '💳',
        'logo_image': 'images/amex.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank Online Assessment', 'desc': '15 MCQs + 3 Coding Qs | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (DSA)', 'desc': 'Arrays, Trees & Graphs | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Round 2 (OOP & DB)', 'desc': 'SQL Optimization & LLD | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Techno-Managerial Round', 'desc': 'Scalability & Payment Security | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'HR Interview', 'desc': 'Amex Values & Culture Fit | 20 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'CS Fundamentals MCQs', 'qs': '15 Qs', 'time': '25 Mins'},
                    {'name': 'Algorithmic Coding Challenge', 'qs': '3 Qs', 'time': '65 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Interview',
                'sections': [
                    {'name': 'Problem Solving & Dynamic Programming', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: OOP & Databases',
                'sections': [
                    {'name': 'Payment Ledger Design & SQL Normalization', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Sliding Window & Hash Maps', 'Graph BFS/DFS & Dijkstra', 'Dynamic Programming Subsets', 'Tree Traversals & Heaps']},
            {'category': 'OOP & Low-Level Design', 'icon': '💻', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Credit Card Rewards Engine Design', 'Factory & Strategy Design Patterns', 'REST API Architecture', 'Concurrency & Thread Safety']},
            {'category': 'Databases & System Security', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['SQL Query Tuning & Joins', 'NoSQL vs RDBMS Architecture', 'Tokenization & Encryption (AES/RSA)', 'Kafka Event Driven Messaging']},
            {'category': 'Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '60 Mins', 'topics': ['Card Transaction Validation', 'Merchant Reward Points Optimization', 'Credit Limit Balance Rebalancer', 'Subarray Max Sum with Constraints']}
        ],
        'faqs': [
            {'q': 'What topics are most emphasized at American Express technical rounds?', 'a': 'Data structures (HashMaps, Trees, Graphs), SQL queries, OOP class design, and payment fraud security concepts.'},
            {'q': 'Does Amex allow candidates to code in any language?', 'a': 'Yes, supported languages include Java, Python, C++, and JavaScript.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'American Express Campus OA Model 1',
                'total_qs': 18,
                'duration': '90 Mins',
                'sample_coding': 'Design an algorithm that partitions customer rewards points among N eligible reward redemption catalogs to maximize overall discount value.',
                'sample_quant': 'Given credit card daily spend history, find the maximum consecutive days where total spend strictly increased.',
                'sample_tech': 'Explain how tokenization protects sensitive credit card numbers (PAN) in compliance with PCI-DSS standards.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'American Express SDE-1 Technical Round Model 2',
                'total_qs': 18,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of integer merchant transaction IDs, return all quadruplets that sum up to target credit transaction amount.',
                'sample_quant': 'Compute the probability that a customer card transaction triggers a 3D-secure fraud challenge given independent risk factor probabilities.',
                'sample_tech': 'How do you optimize slow running SQL queries with multiple table joins using compound indexes and explain plans?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'American Express University Drive Solved Paper Model 3',
                'total_qs': 18,
                'duration': '90 Mins',
                'sample_coding': 'Implement a thread-safe rate limiter for credit card swipe authentication requests using the Sliding Window Log algorithm.',
                'sample_quant': 'Find the shortest path in a weighted payment gateway network avoiding congested routing nodes.',
                'sample_tech': 'What are the trade-offs between monolithic payment architectures and microservice-based transaction processing?'
            }
        ]
    },

    'barclays': {
        'canonical_name': 'Barclays',
        'total_mins': 90,
        'total_qs': 32,
        'roles': 'Graduate Analyst (Technology & Operations)',
        'ctc': '₹14.0 - ₹20.0 LPA',
        'eligibility': '60% or 6.5 CGPA in B.E/B.Tech/MCA with no active backlogs',
        'difficulty': 'Moderate to Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'Barclays Graduate Analyst placement pattern, banking software, RISES values & solved model papers.',
        'brand_color': '#00aeef',
        'accent_bg': 'linear-gradient(135deg, #002d62 0%, #00aeef 100%)',
        'logo_icon': '🦅',
        'logo_image': 'images/barclays.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerEarth Online Test', 'desc': '30 MCQs + 2 Coding Qs | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1', 'desc': 'DSA, OOP & Database Queries | 45 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Interview 2', 'desc': 'System Architecture & Security | 45 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Barclays RISES Values', 'desc': 'Respect, Integrity, Service & Excellence | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Cognitive & Quantitative Aptitude', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Technical & CS Core MCQs', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Algorithmic Coding Challenge', 'qs': '2 Qs', 'time': '50 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview',
                'sections': [
                    {'name': 'Data Structures, Java/C++ OOP, SQL Queries', 'qs': '3 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Values & HR',
                'sections': [
                    {'name': 'Barclays RISES Values & Situational Judgement', 'qs': 'Behavioral', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative & Logical Aptitude', 'icon': '🧠', 'qs': '35 Qs', 'time': '40 Mins', 'topics': ['Percentages, Profit & Loss, Interest', 'Permutations & Probability', 'Data Interpretation Charts', 'Logical Syllogisms & Seating']},
            {'category': 'Technical & Computer Science', 'icon': '💻', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Object Oriented Programming (OOP)', 'SQL Queries, Joins & Normalization', 'Data Structures (Arrays, Trees, Hash)', 'Operating Systems (Threads, Memory)']},
            {'category': 'Coding Assessment', 'icon': '⚡', 'qs': '2 Qs', 'time': '50 Mins', 'topics': ['Account Balance Subsegment Sum', 'Graph Path Verification', 'String Character Reversal Logic', 'Dynamic Array Sorting & Search']},
            {'category': 'Barclays Values (RISES)', 'icon': '🎯', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['Respect for Colleagues', 'Integrity in Banking Operations', 'Service to Customers', 'Excellence & Stewardship']}
        ],
        'faqs': [
            {'q': 'What are the Barclays RISES values evaluated in the interview?', 'a': 'Respect, Integrity, Service, Excellence, and Stewardship. Candidates are evaluated on real-life ethical and team scenarios.'},
            {'q': 'What is the structure of the Barclays HackerEarth test?', 'a': 'It features 30 MCQs (15 Aptitude + 15 Tech) followed by 2 Coding questions over 90 minutes.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Barclays Graduate Analyst OA Model 1',
                'total_qs': 32,
                'duration': '90 Mins',
                'sample_coding': 'Write a program to validate if a series of bank account transfers can be processed without any account dropping below zero balance.',
                'sample_quant': 'A sum of money compounded annually triples itself in 4 years. In how many years will it become 9 times the principal?',
                'sample_tech': 'What is the difference between optimistic and pessimistic locking in relational database transactions?'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Barclays Technical Interview Model 2',
                'total_qs': 32,
                'duration': '90 Mins',
                'sample_coding': 'Given an integer array of account balances, find the longest contiguous subarray whose sum is divisible by K.',
                'sample_quant': 'Two trains 140m and 160m long run in opposite directions at 60 km/h and 40 km/h. How long do they take to cross each other?',
                'sample_tech': 'Explain polymorphism and how runtime method dispatch is achieved in Java via vtables.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Barclays Campus Drive Solved Paper Model 3',
                'total_qs': 32,
                'duration': '90 Mins',
                'sample_coding': 'Implement a function to check if a binary tree is a valid Binary Search Tree (BST).',
                'sample_quant': 'A shopkeeper marks an item 30% above cost price and offers a 10% cash discount. Find his net profit percentage.',
                'sample_tech': 'What is the purpose of database indexes and what are the trade-offs of having too many indexes on a table?'
            }
        ]
    }
}
