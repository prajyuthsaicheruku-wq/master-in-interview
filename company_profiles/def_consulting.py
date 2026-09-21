# -*- coding: utf-8 -*-
"""
Verified and distinct profiles for Consulting Companies:
- McKinsey & Company
- Boston Consulting Group (BCG)
- EY
- PwC
- KPMG
- Deloitte NLA
- Accenture
"""

CONSULTING_COMPANIES = {
    'mckinsey & company': {
        'canonical_name': 'McKinsey & Company',
        'total_mins': 70,
        'total_qs': 25,
        'roles': 'Business Analyst / Junior Associate / Technology Consultant',
        'ctc': '₹22.0 - ₹32.0 LPA',
        'eligibility': 'All engineering branches & quantitative degrees (No backlogs, strong leadership record)',
        'difficulty': 'Extremely High / Strategic Reasoning & Case Math',
        'difficulty_class': 'badge-danger',
        'tagline': 'McKinsey Solve / Imbellus game prep, profitability frameworks, market sizing, PEI leadership & case studies.',
        'brand_color': '#051c2c',
        'accent_bg': 'linear-gradient(135deg, #051c2c 0%, #1e3a8a 100%)',
        'logo_icon': '📊',
        'logo_image': 'images/mckinsey.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Solve Assessment (Imbellus Game)', 'desc': 'Ecosystem & Plant Defense Games | 70 Mins', 'icon': '🎮'},
            {'step': 2, 'title': 'First Round Case Interview 1', 'desc': 'Market Entry & Profitability Framework | 45 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'First Round Case Interview 2', 'desc': 'Guesstimates & PEI Personal Story | 45 Mins', 'icon': '💡'},
            {'step': 4, 'title': 'Partner Round 1 (Strategy Case)', 'desc': 'C-Suite Tech Strategy & Math Synthesis | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Partner Round 2 & Final PEI', 'desc': 'Leadership, Personal Impact & Fit | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: McKinsey Solve (Imbellus)',
                'sections': [
                    {'name': 'Ecosystem Creation (Food Web Optimization)', 'qs': '1 Scenario', 'time': '35 Mins'},
                    {'name': 'Plant Defense / Disease Outbreak Simulation', 'qs': '1 Scenario', 'time': '35 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: First Round Cases (Associate)',
                'sections': [
                    {'name': 'Personal Experience Interview (PEI) Story', 'qs': 'Deep Dive', 'time': '15 Mins'},
                    {'name': 'Interactive Business Case (Profitability / Pricing)', 'qs': '1 Full Case', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Partner Final Round',
                'sections': [
                    {'name': 'Partner Case & Digital Transformation Strategy', 'qs': 'Complex Case', 'time': '45 Mins'},
                    {'name': 'Executive Fitment & Personal Leadership Impact', 'qs': 'Leadership', 'time': '15 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Solve Game / Imbellus Logic', 'icon': '🎮', 'qs': '2 Games', 'time': '70 Mins', 'topics': ['Ecosystem Calorie & Predator-Prey Balance', 'Grid Terrain Optimization & Plant Defense', 'Environmental Variable Constraints', 'Data-Driven Multi-Variable Decision Trees']},
            {'category': 'Business Case Frameworks', 'icon': '📊', 'qs': '15 Qs', 'time': '45 Mins', 'topics': ['Profitability (Revenue vs Fixed & Variable Costs)', 'Market Entry & TAM (Total Addressable Market)', 'Mergers & Acquisitions (M&A) Due Diligence', 'Pricing Strategy (Cost-Plus, Value-Based, Dynamic)']},
            {'category': 'Market Sizing & Quantitative Math', 'icon': '🧮', 'qs': '10 Qs', 'time': '30 Mins', 'topics': ['Top-Down vs Bottom-Up Market Sizing', 'Unit Economics & Break-Even Analysis', 'CAGR & Margin Percentage Calculations', 'Fast Mental Math with Large Numbers (Millions/Billions)']},
            {'category': 'Personal Experience Interview (PEI)', 'icon': '🤝', 'qs': 'Behavioral', 'time': '30 Mins', 'topics': ['Inclusive Leadership & Conflict Resolution', 'Personal Impact & Driving Measurable Change', 'Entrepreneurial Drive & Overcoming Obstacles', 'Structured STAR (Situation, Task, Action, Result) Format']}
        ],
        'faqs': [
            {'q': 'What is McKinsey Solve (Imbellus)?', 'a': 'Solve is McKinsey\'s proprietary gamified cognitive assessment that evaluates critical thinking, systems thinking, meta-cognition, and decision making in complex dynamic environments.'},
            {'q': 'What are the 3 pillars of McKinsey PEI?', 'a': 'The 3 core dimensions tested in PEI are Personal Impact (influencing others), Inclusive Leadership (building team alignment), and Entrepreneurial Drive (innovating and persisting against barriers).'},
            {'q': 'How do I structure a profitability case interview?', 'a': 'Break down Profit into Profit = (Revenues) - (Costs). Revenues = Price * Volume (segment by customer type, channel, geography). Costs = Fixed Costs + Variable Costs (segment by value chain stages).'}
        ],
        'past_papers': [
            {
                'paper_id': 'mckinsey-set-1',
                'title': 'McKinsey Case Math & Sizing 2025 Model Paper',
                'description': 'Real McKinsey quantitative business case and market sizing estimation assessment.',
                'sections': [
                    {
                        'section_name': 'Quantitative Case Math & Market Sizing',
                        'desc': 'Fast mental math, market sizing estimation, and unit economics.',
                        'time': '35 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Market Sizing: Daily Coffee Consumption',
                                'text': 'Estimate the annual market size (in INR) for specialty coffee retail in a city of 10 million people. Assume 40% of the population drinks coffee outside the home, averaging 2 cups per week at an average price of ₹150 per cup.',
                                'marks': '2 Marks',
                                'options': ['₹6,240 Crore', '₹624 Crore', '₹3,120 Crore', '₹1,248 Crore'],
                                'correct': '₹6,240 Crore',
                                'explanation': 'Target population = 10,000,000 * 40% = 4,000,000 consumers. Annual cups = 4,000,000 * (2 cups/week * 52 weeks) = 416,000,000 cups. Total Market Value = 416,000,000 * ₹150 = ₹62,400,000,000 = ₹6,240 Crore.'
                            },
                            {
                                'q_num': 2,
                                'type': 'mcq',
                                'title': 'Unit Economics & Break-Even Analysis',
                                'text': 'A SaaS startup incurs fixed costs of ₹1,200,000 per month. Each active subscriber pays ₹500/month, with variable server and support costs of ₹100/user/month. What is the minimum monthly subscriber count needed to break even?',
                                'marks': '2 Marks',
                                'options': ['2,400 users', '3,000 users', '4,000 users', '1,500 users'],
                                'correct': '3,000 users',
                                'explanation': 'Contribution Margin per subscriber = Price - Variable Cost = ₹500 - ₹100 = ₹400/user. Break-even quantity = Fixed Costs / Contribution Margin = 1,200,000 / 400 = 3,000 subscribers.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'boston consulting group (bcg)': {
        'canonical_name': 'Boston Consulting Group (BCG)',
        'total_mins': 75,
        'total_qs': 30,
        'roles': 'Associate / Junior Consultant / BCG Platinion Technology Consultant',
        'ctc': '₹22.0 - ₹32.0 LPA',
        'eligibility': 'Undergraduate / Dual Degree from top engineering/commerce schools (Strong analytical background)',
        'difficulty': 'Extremely High / Business Analytics & Case Logic',
        'difficulty_class': 'badge-danger',
        'tagline': 'BCG Casey chatbot simulation prep, Growth-Share matrix, pricing frameworks, unit economics & partner cases.',
        'brand_color': '#008542',
        'accent_bg': 'linear-gradient(135deg, #008542 0%, #064e3b 100%)',
        'logo_icon': '💡',
        'logo_image': 'images/bcg.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Casey Chatbot Case Assessment', 'desc': 'AI Case Chatbot & Quantitative Test | 75 Mins', 'icon': '🤖'},
            {'step': 2, 'title': 'Round 1 Case Interview (Associate)', 'desc': 'Market Sizing & Profitability Analysis | 45 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Round 1 Case Interview (Project Leader)', 'desc': 'Supply Chain Optimization & Pricing | 45 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Managing Director & Partner (MDP) Round 1', 'desc': 'Executive Strategy & Business Synthesis | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Managing Director & Partner (MDP) Round 2', 'desc': 'Cultural Fit, Leadership & Career Goals | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: BCG Casey AI Case Assessment',
                'sections': [
                    {'name': 'Quantitative & Chart Interpretation', 'qs': '15 Qs', 'time': '30 Mins'},
                    {'name': 'Casey AI Conversational Business Case', 'qs': '1 Case + Audio Synthesis', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: First Round Case Interviews',
                'sections': [
                    {'name': 'Case Study 1: Market Growth & Profitability', 'qs': '1 Full Case', 'time': '45 Mins'},
                    {'name': 'Case Study 2: Digital Operations & Cost Cutting', 'qs': '1 Full Case', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Partner Final Round',
                'sections': [
                    {'name': 'Unstructured C-Suite Advisory & Behavioral Fit', 'qs': 'Complex Advisory', 'time': '60 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'BCG Frameworks & Strategy', 'icon': '📈', 'qs': '10 Qs', 'time': '30 Mins', 'topics': ['BCG Growth-Share Matrix (Stars, Cash Cows, Dogs, Question Marks)', 'Value Chain & Operational Efficiency', 'Cost Synergy & Post-Merger Integration', 'Market Entry Barriers (Porter\'s Five Forces)']},
            {'category': 'Data Interpretation & Chart Analysis', 'icon': '📊', 'qs': '10 Qs', 'time': '25 Mins', 'topics': ['Waterfall Charts & Margin Decomposition', 'Cohort Retention & Customer Lifetime Value (LTV)', 'Price Elasticity of Demand & Revenue Optimization', 'Sensitivity Analysis on Financial Projections']},
            {'category': 'Guesstimates & Quantitative Sizing', 'icon': '🧮', 'qs': '10 Qs', 'time': '20 Mins', 'topics': ['Population Demographic Segmentation', 'B2B vs B2C Market Estimation Formulas', 'Turnaround Rate & Capacity Utilization Math', 'Unit Contribution Margin Calculation']},
            {'category': 'Casey AI & Video Case Synthesis', 'icon': '🤖', 'qs': 'Synthesis', 'time': '20 Mins', 'topics': ['1-Minute Video Summary Synthesis', 'Structuring Recommendations (Top-down Pyramid Principle)', 'Synthesizing Tradeoffs and Risk Factors', 'Actionable Next Steps Formulation']}
        ],
        'faqs': [
            {'q': 'What is the BCG Casey Chatbot test?', 'a': 'Casey is BCG\'s interactive AI chatbot that gives candidates a 25-30 minute live business case with charts, dynamic data, and questions, followed by a 1-minute video recording where you present your final strategic recommendation.'},
            {'q': 'What is the BCG Growth-Share Matrix?', 'a': 'It categorizes business units by market growth rate and relative market share into Stars (high growth, high share), Cash Cows (low growth, high share), Question Marks (high growth, low share), and Dogs (low growth, low share).'}
        ],
        'past_papers': [
            {
                'paper_id': 'bcg-set-1',
                'title': 'BCG Casey Quantitative & Strategy 2025 Model Paper',
                'description': 'Real BCG business analytics, chart analysis, and profitability optimization model questions.',
                'sections': [
                    {
                        'section_name': 'Business Analytics & Profit Optimization',
                        'desc': 'Data interpretation, CAC-to-LTV ratios, and strategy frameworks.',
                        'time': '35 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Customer Lifetime Value (LTV) Calculation',
                                'text': 'A subscription box service has an average monthly revenue of ₹1,000 per user, with a gross margin of 60%. The monthly churn rate is 5%. What is the estimated Customer Lifetime Value (LTV)?',
                                'marks': '2 Marks',
                                'options': ['₹12,000', '₹20,000', '₹6,000', '₹15,000'],
                                'correct': '₹12,000',
                                'explanation': 'Average Customer Lifetime (in months) = 1 / Churn Rate = 1 / 0.05 = 20 months. LTV = Monthly Gross Profit * Customer Lifetime = (₹1,000 * 60%) * 20 = ₹600 * 20 = ₹12,000.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'ey': {
        'canonical_name': 'EY',
        'total_mins': 75,
        'total_qs': 55,
        'roles': 'Consultant / Technology Risk Consultant / Business Analyst',
        'ctc': '₹8.0 - ₹12.5 LPA',
        'eligibility': 'B.Tech / MCA / MBA / Finance graduates (6.0+ CGPA with no active backlogs)',
        'difficulty': 'Moderate / Cognitive & Business Tech',
        'difficulty_class': 'badge-warning',
        'tagline': 'EY assessment pattern, numerical reasoning, data analytics, SQL, case scenarios & partner interviews.',
        'brand_color': '#ffe600',
        'accent_bg': 'linear-gradient(135deg, #ffe600 0%, #2e2e38 100%)',
        'logo_icon': '💼',
        'logo_image': 'images/ey.svg',
        'selection_stages': [
            {'step': 1, 'title': 'EY Cognitive & Business OA', 'desc': '55 MCQs (Quant, Logic, Verbal, SQL) | 75 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Group Discussion / Business Case Study', 'desc': 'Team Problem Solving & Presentation | 45 Mins', 'icon': '👥'},
            {'step': 3, 'title': 'Technical Round 1 (Data & Tech Consulting)', 'desc': 'SQL, Python/Excel Analytics, Cloud | 45 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Managerial Round (Case Discussion)', 'desc': 'Risk Assessment & Client Scenarios | 45 Mins', 'icon': '🧠'},
            {'step': 5, 'title': 'Partner & HR Fitment Round', 'desc': 'EY Values, Culture & Career Vision | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (Aon/CoCubes)',
                'sections': [
                    {'name': 'Numerical & Data Interpretation', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Logical & Inductive Reasoning', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Verbal Ability & Business English', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Domain Tech & SQL / Analytics MCQs', 'qs': '10 Qs', 'time': '15 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Case Study & Technical',
                'sections': [
                    {'name': 'Client Case Study Presentation & SQL Queries', 'qs': 'Case + Tech', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Partner & HR',
                'sections': [
                    {'name': 'Partner Fitment & Consulting Behavioral Scenarios', 'qs': 'Behavioral', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Numerical Reasoning & Financial Math', 'icon': '🧮', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Percentages, Profit & Loss, Ratios', 'Compound Interest & Present Value Math', 'Data Tables, Pie Charts & Trend Analysis', 'Probability & Basic Statistics (Mean, Median, StdDev)']},
            {'category': 'Logical & Analytical Reasoning', 'icon': '🧠', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['Syllogisms & Statement Assumptions', 'Seating Arrangements & Blood Relations', 'Data Sufficiency & Critical Thinking', 'Inductive Logic & Series Patterns']},
            {'category': 'Technology & Data Consulting (SQL)', 'icon': '💻', 'qs': '10 Qs', 'time': '15 Mins', 'topics': ['SQL JOINS (Inner, Left, Cross)', 'GROUP BY, HAVING & Aggregate Functions', 'Window Functions (RANK, DENSE_RANK)', 'Data Warehouse & ETL Fundamentals']},
            {'category': 'Business Communication & Verbal', 'icon': '📝', 'qs': '10 Qs', 'time': '15 Mins', 'topics': ['Reading Comprehension on Corporate Cases', 'Sentence Correction & Grammar Error Spotting', 'Vocabulary & Contextual Phrasing', 'Professional Email & Report Writing Etiquette']}
        ],
        'faqs': [
            {'q': 'What tools/skills does EY emphasize in Technology Consulting?', 'a': 'SQL, Advanced Excel (VLOOKUP, Pivot Tables), Power BI/Tableau, Python for data analytics, and cloud basics (AWS/Azure).'},
            {'q': 'Is there negative marking in the EY Online Assessment?', 'a': 'Usually there is no negative marking in the EY online assessment, but sectional cutoffs must be cleared across Numerical, Logical, and Tech sections.'}
        ],
        'past_papers': [
            {
                'paper_id': 'ey-set-1',
                'title': 'EY Consulting & Analytics 2025 Model Paper',
                'description': 'Real EY campus recruitment test covering numerical logic, SQL analytics, and situational case reasoning.',
                'sections': [
                    {
                        'section_name': 'Numerical & Data Analytics',
                        'desc': 'Core business math and SQL querying.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'SQL Second Highest Salary Query',
                                'text': 'Which SQL query correctly retrieves the 2nd highest distinct salary from an `Employees` table?',
                                'marks': '2 Marks',
                                'options': [
                                    'SELECT DISTINCT salary FROM Employees ORDER BY salary DESC LIMIT 1 OFFSET 1;',
                                    'SELECT MAX(salary) FROM Employees WHERE salary < (SELECT MIN(salary) FROM Employees);',
                                    'SELECT salary FROM Employees WHERE rank = 2;',
                                    'SELECT TOP 2 salary FROM Employees;'
                                ],
                                'correct': 'SELECT DISTINCT salary FROM Employees ORDER BY salary DESC LIMIT 1 OFFSET 1;',
                                'explanation': 'Ordering distinct salaries descending and skipping 1 row (`OFFSET 1 LIMIT 1`) precisely yields the second highest salary.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'pwc': {
        'canonical_name': 'PwC',
        'total_mins': 80,
        'total_qs': 60,
        'roles': 'Associate / Technology Consultant / Cybersecurity Associate',
        'ctc': '₹8.5 - ₹13.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60% or 6.5+ CGPA throughout 10th, 12th & Graduation)',
        'difficulty': 'Moderate / Cognitive & Gamified Logic',
        'difficulty_class': 'badge-warning',
        'tagline': 'PwC Elevate test pattern, game-based cognitive tests, numerical reasoning, cloud systems & partner interview.',
        'brand_color': '#d04a02',
        'accent_bg': 'linear-gradient(135deg, #d04a02 0%, #1c1917 100%)',
        'logo_icon': '📈',
        'logo_image': 'images/pwc.svg',
        'selection_stages': [
            {'step': 1, 'title': 'PwC Elevate Online Assessment', 'desc': '60 MCQs / Cognitive Games | 80 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (Tech & Architecture)', 'desc': 'OOPs, DBMS, Python/Java, Cloud | 45 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Interview 2 (Consulting Case)', 'desc': 'Case Simulation & Risk Analysis | 45 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Managerial & Fitment Round', 'desc': 'Leadership Scenarios & Team Fit | 30 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Partner Interview', 'desc': 'PwC Professional Framework & Vision | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (SHL/Mettl)',
                'sections': [
                    {'name': 'Numerical Reasoning', 'qs': '18 Qs', 'time': '25 Mins'},
                    {'name': 'Inductive & Deductive Logic', 'qs': '18 Qs', 'time': '25 Mins'},
                    {'name': 'Technical / CS Fundamentals', 'qs': '24 Qs', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview',
                'sections': [
                    {'name': 'Data Modeling, Cloud Fundamentals & Algorithms', 'qs': 'Tech Concepts', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Partner & HR',
                'sections': [
                    {'name': 'PwC Professional 5 Attributes & Case Defense', 'qs': 'Fitment', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Numerical Reasoning & Data Interpretation', 'icon': '🧮', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Profit Margins & Price-Volume Analysis', 'Ratio Proportions & Percent Change', 'Financial Statement Interpretation', 'Probability & Combinatorics']},
            {'category': 'Logical & Game-Based Cognition', 'icon': '🧠', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Pattern Matrix Completion', 'Spatial & Deductive Problem Solving', 'Situational Judgement in Client Settings', 'Decision Trees under Time Constraints']},
            {'category': 'Computer Science & Cloud Core', 'icon': '💻', 'qs': '20 Qs', 'time': '30 Mins', 'topics': ['Relational DB & SQL Query Optimization', 'Cloud Architecture (IaaS vs PaaS vs SaaS)', 'OOP Principles (Inheritance, Polymorphism)', 'Cybersecurity & Encryption Basics']},
            {'category': 'PwC Professional Framework', 'icon': '🤝', 'qs': 'Behavioral', 'time': '30 Mins', 'topics': ['Whole Leadership', 'Business Acumen', 'Technical and Digital Capabilities', 'Global & Inclusive Perspective', 'Relationships & Trust']}
        ],
        'faqs': [
            {'q': 'What is the PwC Professional Framework?', 'a': 'It is PwC\'s global leadership development framework assessing 5 attributes: Whole Leadership, Business Acumen, Technical Capabilities, Global & Inclusive Perspective, and Relationships.'}
        ],
        'past_papers': [
            {
                'paper_id': 'pwc-set-1',
                'title': 'PwC Consulting & Technology 2025 Model Paper',
                'description': 'Real PwC recruitment assessment on numerical logic, database queries, and situational decision making.',
                'sections': [
                    {
                        'section_name': 'Quantitative & Technical Aptitude',
                        'desc': 'Core numerical calculations and CS fundamentals.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Cloud Computing Service Models',
                                'text': 'In which cloud computing model does the vendor provide the hardware, OS, and runtime environment while the customer only manages their application code and data?',
                                'marks': '2 Marks',
                                'options': ['PaaS (Platform as a Service)', 'IaaS (Infrastructure as a Service)', 'SaaS (Software as a Service)', 'FaaS only'],
                                'correct': 'PaaS (Platform as a Service)',
                                'explanation': 'PaaS provides the underlying hardware, OS, and application runtime, freeing developers to build and manage only the application code and data.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'kpmg': {
        'canonical_name': 'KPMG',
        'total_mins': 70,
        'total_qs': 50,
        'roles': 'Analyst / Technology Enablement Consultant / Risk Advisory Associate',
        'ctc': '₹8.0 - ₹12.5 LPA',
        'eligibility': 'B.Tech / MCA / B.Sc / MBA (60% or 6.0+ CGPA in all academics)',
        'difficulty': 'Moderate / Analytical & Situational Judgement',
        'difficulty_class': 'badge-warning',
        'tagline': 'KPMG LaunchPad assessment pattern, Situational Judgement Test (SJT), numerical logic & case interviews.',
        'brand_color': '#00338d',
        'accent_bg': 'linear-gradient(135deg, #00338d 0%, #0c1c4d 100%)',
        'logo_icon': '⚖️',
        'logo_image': 'images/kpmg.svg',
        'selection_stages': [
            {'step': 1, 'title': 'KPMG LaunchPad Online Assessment', 'desc': '50 MCQs (SJT, Numerical, Critical Thinking) | 70 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Group Activity / Micro Case Presentation', 'desc': 'Team Problem Solving & Strategy | 40 Mins', 'icon': '👥'},
            {'step': 3, 'title': 'Technical Interview (Domain & SQL/Tech)', 'desc': 'Data Systems, Analytics & Process Flows | 45 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Managerial Interview', 'desc': 'Risk Management & Client Problem Scenarios | 30 Mins', 'icon': '🧠'},
            {'step': 5, 'title': 'Partner & HR Fitment Round', 'desc': 'KPMG Values & Professional Integrity | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment (LaunchPad)',
                'sections': [
                    {'name': 'Numerical & Data Reasoning', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Verbal & Critical Thinking', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Situational Judgement Test (SJT)', 'qs': '20 Qs', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical & Case Discussion',
                'sections': [
                    {'name': 'Business Problem Solving & Data Analytics', 'qs': 'Case + Tech', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Partner & HR',
                'sections': [
                    {'name': 'Partner Discussion & Ethics / Integrity Scenarios', 'qs': 'Fitment', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Situational Judgement Tests (SJT)', 'icon': '⚖️', 'qs': '20 Qs', 'time': '30 Mins', 'topics': ['Prioritization of Conflicting Deadlines', 'Client Conflict Resolution & Confidentiality', 'Ethical Dilemmas & Regulatory Compliance', 'Collaborative Teamwork & Delegation']},
            {'category': 'Numerical & Statistical Analysis', 'icon': '🧮', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['Financial Ratios (ROI, Operating Margin)', 'Bar/Line Chart & Tabular Interpretation', 'Percentages, Growth Rates & Variances', 'Data-Driven Business Forecasting']},
            {'category': 'Critical Thinking & Verbal Reasoning', 'icon': '📝', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['Argument Strength & Deductive Inference', 'Assumptions vs Conclusions in Case Texts', 'Fact-Finding & Logical Fallacy Identification', 'Professional Communication Syntax']},
            {'category': 'Technology Advisory Basics', 'icon': '💻', 'qs': '10 Qs', 'time': '15 Mins', 'topics': ['SQL Querying & Normalization', 'ERP / CRM Systems Overview (SAP, Salesforce)', 'IT Risk Management & Cybersecurity Controls', 'Business Process Flowcharting']}
        ],
        'faqs': [
            {'q': 'What is the Situational Judgement Test (SJT) in KPMG?', 'a': 'SJT presents realistic workplace scenarios with multiple potential actions. You must rate each action from Most Effective to Least Effective based on KPMG\'s ethical guidelines and client service standards.'}
        ],
        'past_papers': [
            {
                'paper_id': 'kpmg-set-1',
                'title': 'KPMG Situational Judgement & Logic 2025 Model Paper',
                'description': 'Real KPMG LaunchPad assessment covering situational workplace judgement and numerical reasoning.',
                'sections': [
                    {
                        'section_name': 'SJT & Numerical Analysis',
                        'desc': 'Client scenario judgement and quantitative analysis.',
                        'time': '35 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'SJT: Handling an Unrealistic Client Deadline',
                                'text': 'A high-profile client requests an exhaustive audit report in 24 hours, which typically takes 4 days. What is the most effective professional action?',
                                'marks': '2 Marks',
                                'options': [
                                    'Consult with your Engagement Manager immediately, identify key urgent high-priority deliverables for tomorrow, and propose a phased delivery schedule with quality assurance.',
                                    'Accept the deadline immediately without asking team members and submit an incomplete draft.',
                                    'Refuse the request flatly stating standard audit guidelines prohibit quick turnarounds.',
                                    'Ignore the client email until the standard 4 days elapse.'
                                ],
                                'correct': 'Consult with your Engagement Manager immediately, identify key urgent high-priority deliverables for tomorrow, and propose a phased delivery schedule with quality assurance.',
                                'explanation': 'Demonstrates structured stakeholder management, escalation to leadership, client empathy, and uncompromised deliverable quality.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'deloitte nla': {
        'canonical_name': 'Deloitte NLA',
        'total_mins': 115,
        'total_qs': 78,
        'roles': 'Analyst (Consulting & Advisory / Cyber / Technology Track)',
        'ctc': '₹7.6 - ₹13.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60% or 6.5 CGPA throughout, no active backlogs)',
        'difficulty': 'Moderate - High / Comprehensive NLA Pattern',
        'difficulty_class': 'badge-warning',
        'tagline': 'Deloitte National Level Assessment (NLA) pattern, Versant English, Quant, Logical, CS & hands-on coding.',
        'brand_color': '#86bc25',
        'accent_bg': 'linear-gradient(135deg, #86bc25 0%, #1e293b 100%)',
        'logo_icon': '🟢',
        'logo_image': 'images/deloitte.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Deloitte NLA Online Test', 'desc': '76 MCQs + 2 Hands-on Coding | 115 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Versant English Communication Assessment', 'desc': 'Spoken English & Pronunciation | 25 Mins', 'icon': '🗣️'},
            {'step': 3, 'title': 'Technical Interview 1 (Core CS & Coding)', 'desc': 'OOP, SQL, DSA & Web Architecture | 45 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Techno-Managerial & Case Interview', 'desc': 'Client Problem Scenarios & Projects | 45 Mins', 'icon': '🧠'},
            {'step': 5, 'title': 'HR Fitment Round', 'desc': 'Culture, Relocation & Career Growth | 20 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Deloitte NLA Online Test',
                'sections': [
                    {'name': 'Quantitative Ability', 'qs': '14 Qs', 'time': '15 Mins'},
                    {'name': 'Logical Reasoning', 'qs': '14 Qs', 'time': '15 Mins'},
                    {'name': 'Verbal Ability', 'qs': '22 Qs', 'time': '20 Mins'},
                    {'name': 'Computer Fundamentals (CS Core)', 'qs': '26 Qs', 'time': '30 Mins'},
                    {'name': 'Hands-on Algorithmic Coding Challenge', 'qs': '2 Qs', 'time': '35 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Versant Communication Test',
                'sections': [
                    {'name': 'Reading, Repeat Sentences, Short Answers & Story Retelling', 'qs': 'Audio Tasks', 'time': '25 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical & Techno-Managerial Interview',
                'sections': [
                    {'name': 'Algorithms, SQL Queries, Cloud Concepts & Project Scenarios', 'qs': 'Technical', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: HR Round',
                'sections': [
                    {'name': 'Deloitte Culture, Values & Behavioral Competencies', 'qs': 'Behavioral', 'time': '20 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative & Logical Ability', 'icon': '🧮', 'qs': '28 Qs', 'time': '30 Mins', 'topics': ['Time, Speed & Distance / Work Formulas', 'Permutations, Combinations & Probability', 'Data Interpretation & Logical Puzzles', 'Syllogisms & Direction Sense']},
            {'category': 'Computer Fundamentals & CS Core', 'icon': '💻', 'qs': '26 Qs', 'time': '30 Mins', 'topics': ['OOPs (Inheritance, Polymorphism, Abstraction)', 'DBMS (ACID properties, Normal Forms, Indexing)', 'Operating Systems (Processes, Deadlocks, Paging)', 'Computer Networks (OSI layers, TCP/UDP, DNS)']},
            {'category': 'Hands-on Coding Challenges', 'icon': '🎯', 'qs': '2 Qs', 'time': '35 Mins', 'topics': ['String Manipulation & Palindrome Substrings', 'Array Sliding Window & Prefix Sums', 'Matrix Operations & Diagonal Traversal', 'Hash Maps & Two Sum Variations']},
            {'category': 'Verbal & Versant Communication', 'icon': '🗣️', 'qs': '22 Qs', 'time': '20 Mins', 'topics': ['Reading Comprehension & Grammar Correction', 'Active/Passive Voice & Sentence Rearrangement', 'Pronunciation, Fluency & Voice Clarity in Versant', 'Spontaneous 45-second Speech on Topics']}
        ],
        'faqs': [
            {'q': 'What is Deloitte NLA?', 'a': 'Deloitte National Level Assessment (NLA) is Deloitte India\'s flagship campus assessment covering Aptitude, CS Fundamentals, Hands-on Coding, and the Versant spoken English test.'},
            {'q': 'Are there sectional cutoffs in Deloitte NLA?', 'a': 'Yes, you must pass all sections including Quantitative, Logical, Verbal, Computer Fundamentals, and Coding to qualify for the interview rounds.'}
        ],
        'past_papers': [
            {
                'paper_id': 'deloitte-set-1',
                'title': 'Deloitte NLA 2025 Model Paper',
                'description': 'Real Deloitte NLA assessment with Computer Fundamentals and Hands-on Coding.',
                'sections': [
                    {
                        'section_name': 'Computer Fundamentals & Coding',
                        'desc': 'Core DBMS and array coding challenges.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'DBMS ACID Property Durability',
                                'text': 'Which component of a DBMS ensures the Durability property in ACID transactions even after sudden system failure or crash?',
                                'marks': '2 Marks',
                                'options': [
                                    'Write-Ahead Logging (WAL) and Recovery Manager',
                                    'Query Optimizer',
                                    'Lock Manager for concurrency',
                                    'Foreign Key Integrity Constraint'
                                ],
                                'correct': 'Write-Ahead Logging (WAL) and Recovery Manager',
                                'explanation': 'Write-Ahead Logging (WAL) records transactions on non-volatile disk before committing, allowing the recovery manager to restore committed transactions after crash.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Longest Substring Without Repeating Characters',
                                'text': 'Given a string `s`, find the length of the longest substring without repeating characters.',
                                'marks': '4 Marks',
                                'sample_answer': 'def length_of_longest_substring(s: str) -> int:\n    char_map = {}\n    left = 0\n    max_len = 0\n    for right, char in enumerate(s):\n        if char in char_map and char_map[char] >= left:\n            left = char_map[char] + 1\n        char_map[char] = right\n        max_len = max(max_len, right - left + 1)\n    return max_len',
                                'explanation': 'Using a sliding window with two pointers and a hash map of character indices, we adjust the left pointer when duplicates are detected. Runs in O(n) time and O(min(m, n)) space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'accenture': {
        'canonical_name': 'Accenture',
        'total_mins': 135,
        'total_qs': 92,
        'roles': 'Associate Software Engineer (ASE) / Advanced Associate Software Engineer (AASE)',
        'ctc': '₹4.5 - ₹11.5 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA / M.Sc (6.5+ CGPA or 65% aggregate with no standing backlogs)',
        'difficulty': 'Moderate / Multi-Stage Elimination',
        'difficulty_class': 'badge-info',
        'tagline': 'Accenture recruitment test pattern, Cognitive, Technical MCQs, Pseudocode, Coding & Communication assessment.',
        'brand_color': '#a100ff',
        'accent_bg': 'linear-gradient(135deg, #a100ff 0%, #1e1b4b 100%)',
        'logo_icon': '🟣',
        'logo_image': 'images/accenture.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Cognitive & Technical Assessment', 'desc': '90 MCQs (Elimination Round) | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Hands-on Coding Assessment', 'desc': '2 Algorithmic Coding Problems | 45 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Communication Assessment (Versant)', 'desc': 'Pronunciation, Fluency & Listening | 20 Mins', 'icon': '🗣️'},
            {'step': 4, 'title': 'Technical & HR Interview (Combined)', 'desc': 'Projects, CS Core & Behavioral Scenarios | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Cognitive Assessment',
                'sections': [
                    {'name': 'Critical Thinking & Problem Solving', 'qs': '18 Qs', 'time': '30 Mins'},
                    {'name': 'Abstract Reasoning', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'English Ability', 'qs': '17 Qs', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Assessment',
                'sections': [
                    {'name': 'Pseudocode Analysis', 'qs': '18 Qs', 'time': '20 Mins'},
                    {'name': 'Common Application & MS Office', 'qs': '12 Qs', 'time': '15 Mins'},
                    {'name': 'Cloud, Networking & Security Fundamentals', 'qs': '10 Qs', 'time': '15 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Coding Challenge',
                'sections': [
                    {'name': 'Hands-on Algorithmic Coding (2 Questions)', 'qs': '2 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Communication Assessment',
                'sections': [
                    {'name': 'Versant Audio Reading, Repeats & Story Retell', 'qs': 'Audio Tests', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 5: Interview',
                'sections': [
                    {'name': 'Technical Project Deep Dive & HR Fitment', 'qs': 'Interview', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Pseudocode & Logical Tracing', 'icon': '💻', 'qs': '18 Qs', 'time': '20 Mins', 'topics': ['Bitwise Operations (XOR, AND, OR, Shifts) in Pseudocode', 'Nested Loops & Conditionals Execution', 'Recursive Function Call Stack Tracing', 'Variable Scope and Array Indexing']},
            {'category': 'Technical & Cloud / Security', 'icon': '⚡', 'qs': '22 Qs', 'time': '30 Mins', 'topics': ['Cloud Service Models (IaaS, PaaS, SaaS)', 'Network Topologies & IP Subnetting Basics', 'Cybersecurity (Malware, Phishing, Symmetric Encryption)', 'MS Office Formulas (VLOOKUP, SUMIF, Macros)']},
            {'category': 'Cognitive & Critical Thinking', 'icon': '🧠', 'qs': '50 Qs', 'time': '40 Mins', 'topics': ['Data Arrangement & Visual Logic Matrices', 'Flowcharts & Statement-Assumption Arguments', 'Reading Comprehension & Vocabulary In-Context', 'Sentence Correction & Prepositions']},
            {'category': 'Algorithmic Coding (C/C++/Java/Python)', 'icon': '🎯', 'qs': '2 Qs', 'time': '45 Mins', 'topics': ['Array Operations & Difference Calculations', 'String Reversals & Vowel Counting', 'Binary / Bitwise Operations & Base Conversion', 'Sorting & Searching Applications']}
        ],
        'faqs': [
            {'q': 'What is the format of Accenture Pseudocode questions?', 'a': 'Pseudocode questions show C/Python-like code snippets with bitwise operators (&, ^, |), modulo operations, and recursive loops. You must determine the exact output value.'},
            {'q': 'Is the Coding round mandatory for all candidates?', 'a': 'Yes, candidates who pass the Cognitive + Technical test unlock the Coding Assessment immediately on the same platform.'}
        ],
        'past_papers': [
            {
                'paper_id': 'accenture-set-1',
                'title': 'Accenture ASE & AASE 2025 Model Paper',
                'description': 'Real Accenture assessment with Pseudocode questions and hands-on coding.',
                'sections': [
                    {
                        'section_name': 'Pseudocode & Hands-on Coding',
                        'desc': 'Bitwise pseudocode tracing and algorithmic problem solving.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Accenture Bitwise Pseudocode',
                                'text': 'What will be the output of the following pseudocode?\n\nInteger a, b, c\nSet a = 4, b = 6, c = 2\nif ((a ^ b) > (b & c))\n    a = a + (b ^ c)\nEnd if\nPrint a',
                                'marks': '2 Marks',
                                'options': ['4', '8', '10', '12'],
                                'correct': '4',
                                'explanation': 'a ^ b = 4 ^ 6 = 2. b & c = 6 & 2 = 2. Condition ((a ^ b) > (b & c)) evaluates to (2 > 2), which is False. Therefore, the if-block does not execute, and a remains 4.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Find Count of Elements Greater Than Prior Maximum',
                                'text': 'Given an integer array `arr` representing daily stock prices, find the count of elements that are strictly greater than all prior elements in the array.',
                                'marks': '4 Marks',
                                'sample_answer': 'def count_record_breakers(arr: list[int]) -> int:\n    if not arr:\n        return 0\n    count = 1\n    max_so_far = arr[0]\n    for val in arr[1:]:\n        if val > max_so_far:\n            count += 1\n            max_so_far = val\n    return count',
                                'explanation': 'Track `max_so_far` starting with the first element. Iterate through the array once in O(n) time and O(1) space, incrementing count whenever an element exceeds `max_so_far`.'
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
