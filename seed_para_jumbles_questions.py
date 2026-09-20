"""
Seed script for Para Jumbles (Verbal Ability)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Para Jumbles - Solar Energy",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Solar energy is rapidly becoming one of the most accessible sources of clean power.\n(Q) This transformation is driven by steep reductions in the cost of photovoltaic panels.\n(R) Consequently, both households and businesses are installing rooftop arrays in record numbers.\n(S) This shift reduces dependence on fossil fuels and helps curb global carbon emissions.",
        "sample_answer": "P introduces the topic of solar energy. Q explains what drives this (cost reduction). R provides the consequence (installation in record numbers). S concludes with the broader impact.",
        "tips": "Start with the broad introductory statement (P).",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "S-P-Q-R",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Electric Vehicles",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) The transition toward electric vehicles has gathered tremendous momentum globally.\n(Q) Major automakers are committing billions of dollars toward developing long-range batteries.\n(R) At the same time, governments are rolling out charging networks across major highway corridors.\n(S) Together, these dual efforts are easing consumer concerns about driving range.",
        "sample_answer": "P states the trend. Q and R describe the actions taken by automakers and governments. S summarizes their combined effect.",
        "tips": "Notice 'Together, these dual efforts' in S refers back to Q and R.",
        "options": [
            {
                "label": "A",
                "text": "S-Q-R-P",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-R-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Machine Learning",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Machine learning relies heavily on vast volumes of high-quality data.\n(Q) Algorithms analyze this data to identify hidden trends and statistical correlations.\n(R) Once trained, these models can make accurate predictions on previously unseen information.\n(S) Thus, the predictive accuracy of any model depends directly on the quality of training data.",
        "sample_answer": "P introduces data dependency. Q explains algorithmic pattern extraction. R discusses trained model prediction. S concludes with 'Thus'.",
        "tips": "Follow the logical chronological pipeline of machine learning.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Water Conservation",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Freshwater scarcity is emerging as an urgent humanitarian and ecological threat.\n(Q) Inefficient irrigation techniques in agriculture account for a significant fraction of water waste.\n(R) Adopting precision drip irrigation can cut water consumption by more than half.\n(S) Therefore, modernizing farming practices is vital for conserving global water reserves.",
        "sample_answer": "P presents the global problem. Q highlights agriculture's role. R offers drip irrigation as a solution. S concludes.",
        "tips": "Problem -> Cause -> Solution -> Conclusion.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Q-R-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Remote Work Culture",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Remote work arrangements have reshaped the conventional corporate workplace.\n(Q) Employees enjoy flexible working hours and no longer endure exhausting daily commutes.\n(R) However, maintaining team cohesion and informal spontaneous communication remains difficult.\n(S) To address this, hybrid work policies are being implemented to blend flexibility with collaboration.",
        "sample_answer": "P introduces remote work. Q highlights the primary benefit. R presents the contrasting challenge ('However'). S provides the resolution.",
        "tips": "Look for the contrast marker 'However' in R.",
        "options": [
            {
                "label": "A",
                "text": "R-S-P-Q",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "P-Q-S-R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-P-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Financial Literacy",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Financial literacy is an essential life skill that is rarely taught in primary schools.\n(Q) Without proper guidance, many young adults fall into cycles of high-interest consumer debt.\n(R) Understanding basic concepts like compound interest and budgeting can prevent these pitfalls.\n(S) Educational institutions should therefore integrate financial literacy into their core curriculum.",
        "sample_answer": "P introduces financial literacy. Q outlines the danger of lacking it. R explains how understanding key concepts prevents debt. S concludes with policy advice.",
        "tips": "Trace the progression from lack of education to suggested curriculum change.",
        "options": [
            {
                "label": "A",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Space Exploration",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Commercial space companies have dramatically slashed the cost of sending payloads into orbit.\n(Q) Reusability of rocket boosters has been the single most revolutionary breakthrough.\n(R) Lower launch costs have made satellite constellations financially viable for global internet access.\n(S) As a result, remote regions around the globe are gaining high-speed broadband connectivity.",
        "sample_answer": "P establishes commercial launch cost reductions. Q explains the technological reason (reusable boosters). R links to satellite constellations. S shows resulting global internet.",
        "tips": "Notice cause-and-effect chaining across P, Q, R, and S.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-R-Q-P",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Cybersecurity Best Practices",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Cyber threats have evolved from simple spam emails to targeted spear-phishing attacks.\n(Q) Attackers craft convincing deceptive messages mimicking trusted institutions to steal credentials.\n(R) Implementing multi-factor authentication creates a strong secondary line of defense.\n(S) Even if passwords are compromised, unauthorized access is effectively blocked.",
        "sample_answer": "P states threat evolution. Q explains spear-phishing mechanism. R presents MFA defense. S explains why MFA protects against stolen credentials.",
        "tips": "S directly builds upon the defense established in R.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Mindfulness and Mental Health",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Chronic stress has become a widespread epidemic in modern high-pressure work environments.\n(Q) Mindfulness meditation has gained scientific endorsement as an effective coping mechanism.\n(R) Practicing mindful breathing for just ten minutes daily reduces cortisol and calms the nervous system.\n(S) Consequently, many leading corporations now offer structured mindfulness sessions to their staff.",
        "sample_answer": "P introduces workplace stress. Q suggests mindfulness as a remedy. R explains the biological mechanism. S illustrates corporate adoption.",
        "tips": "P is the introductory problem; S is the final societal outcome.",
        "options": [
            {
                "label": "A",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Q-P-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Urban Green Spaces",
        "difficulty": "Easy",
        "question_text": "Rearrange the following sentences (P, Q, R, S) in a coherent logical sequence:\n\n(P) Rapid urbanization often replaces lush natural landscapes with concrete and asphalt.\n(Q) This concrete concentration creates 'urban heat islands' that elevate city temperatures significantly.\n(R) Integrating parks, rooftop gardens, and tree-lined avenues counteracts this warming phenomenon.\n(S) Urban planners must therefore prioritize green infrastructure in future master plans.",
        "sample_answer": "P depicts concrete expansion. Q identifies heat islands. R presents green space solutions. S gives final planning recommendation.",
        "tips": "Q connects directly to 'concrete' mentioned in P.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Cloud Computing 11",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Companies no longer need to invest heavily in expensive physical server rooms.\n(Q) Instead, they pay only for the storage and compute capacity they actually consume.\n(R) Cloud infrastructure provides scalable on-demand computing resources.\n(S) This financial and operational agility accelerates software development cycles.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "S-R-P-Q",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-R-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Renewable Wind Power 12",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Wind turbines harness kinetic atmospheric energy to generate clean electricity.\n(Q) Modern turbine designs feature taller towers and longer aerodynamic blades.\n(R) These design innovations allow turbines to capture steady winds even at lower altitudes.\n(S) Consequently, wind farm capacity factors have increased significantly over the past decade.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-P-Q-R",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Microbiome Health 13",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) These microbes assist in digesting fiber and synthesizing vital vitamins.\n(Q) The human gut houses trillions of symbiotic microorganisms essential for health.\n(R) A diet rich in diverse plant-based foods nourishes this complex microbial ecosystem.\n(S) Conversely, ultra-processed foods diminish beneficial bacteria and trigger inflammation.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "S-Q-P-R",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "R-Q-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - E-Commerce Logistics 14",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) E-commerce expansion has heightened customer expectations for rapid delivery.\n(Q) Automated robotics within these urban warehouses sort and package orders within minutes.\n(R) To fulfill same-day deliveries, retailers are building micro-fulfillment centers inside cities.\n(S) This localized fulfillment drastically shortens the final-mile transit duration.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Digital Payments 15",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Smartphone apps using QR codes have replaced physical paper cash across millions of vendor stalls.\n(Q) Transactions settle instantly into merchant accounts with minimal processing friction.\n(R) Digital payment ecosystems have revolutionized retail financial transactions.\n(S) This seamless financial inclusion empowers small informal vendors into the formal economy.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "S-R-P-Q",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Q-R-P-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Biodiversity Conservation 16",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Tropical rainforests harbor more than half of the planet's terrestrial species.\n(Q) Deforestation for cattle ranching and palm oil plantations threatens this rich biodiversity.\n(R) Loss of forest cover eliminates habitats and disrupts global rainfall patterns.\n(S) Conserving remaining primary forests is therefore essential to prevent mass species extinctions.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-P-Q-R",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Autonomous Driving 17",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Onboard machine learning processors analyze sensor feeds in real time to steer and brake.\n(Q) Autonomous vehicles utilize sensors, cameras, and lidar to perceive their surroundings.\n(R) Eliminating human error could theoretically avert millions of traffic collisions annually.\n(S) However, complex edge-case weather conditions still present formidable engineering hurdles.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "S-Q-P-R",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Stem Education 18",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Encouraging young students to pursue STEM disciplines is crucial for technological progress.\n(Q) Early positive exposure builds lasting problem-solving confidence among young learners.\n(R) Hands-on robotics clubs and coding camps introduce complex ideas through playful engagement.\n(S) Schools that adopt experiential learning report higher enrollment in advanced science courses.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Plastic Pollution 19",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Discarded plastic packaging breaks down into microplastics that contaminate marine food webs.\n(Q) Marine organisms ingest these toxic particles, which subsequently enter the human diet.\n(R) Single-use plastics take hundreds of years to decompose in natural ecosystems.\n(S) Banning disposable plastics and developing biodegradable alternatives is imperative.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-P-Q-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "S-R-P-Q",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Q-R-P-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-R-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Telemedicine Services 20",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Telemedicine has fundamentally transformed how patients receive basic healthcare.\n(Q) Individuals can consult medical specialists remotely via encrypted video consultations.\n(R) This remote accessibility saves rural patients hundreds of travel hours each year.\n(S) As virtual diagnostic tools improve, telemedicine will become a mainstay of primary healthcare.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Cloud Computing 21",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Companies no longer need to invest heavily in expensive physical server rooms.\n(Q) Cloud infrastructure provides scalable on-demand computing resources.\n(R) Instead, they pay only for the storage and compute capacity they actually consume.\n(S) This financial and operational agility accelerates software development cycles.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-Q-P-R",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Renewable Wind Power 22",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Wind turbines harness kinetic atmospheric energy to generate clean electricity.\n(Q) These design innovations allow turbines to capture steady winds even at lower altitudes.\n(R) Modern turbine designs feature taller towers and longer aerodynamic blades.\n(S) Consequently, wind farm capacity factors have increased significantly over the past decade.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-R-Q-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Microbiome Health 23",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) These microbes assist in digesting fiber and synthesizing vital vitamins.\n(Q) A diet rich in diverse plant-based foods nourishes this complex microbial ecosystem.\n(R) The human gut houses trillions of symbiotic microorganisms essential for health.\n(S) Conversely, ultra-processed foods diminish beneficial bacteria and trigger inflammation.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-R-P-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "S-R-P-Q",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - E-Commerce Logistics 24",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) E-commerce expansion has heightened customer expectations for rapid delivery.\n(Q) To fulfill same-day deliveries, retailers are building micro-fulfillment centers inside cities.\n(R) Automated robotics within these urban warehouses sort and package orders within minutes.\n(S) This localized fulfillment drastically shortens the final-mile transit duration.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Digital Payments 25",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Smartphone apps using QR codes have replaced physical paper cash across millions of vendor stalls.\n(Q) Digital payment ecosystems have revolutionized retail financial transactions.\n(R) Transactions settle instantly into merchant accounts with minimal processing friction.\n(S) This seamless financial inclusion empowers small informal vendors into the formal economy.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-Q-P-R",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Biodiversity Conservation 26",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Tropical rainforests harbor more than half of the planet's terrestrial species.\n(Q) Loss of forest cover eliminates habitats and disrupts global rainfall patterns.\n(R) Deforestation for cattle ranching and palm oil plantations threatens this rich biodiversity.\n(S) Conserving remaining primary forests is therefore essential to prevent mass species extinctions.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Autonomous Driving 27",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Onboard machine learning processors analyze sensor feeds in real time to steer and brake.\n(Q) Eliminating human error could theoretically avert millions of traffic collisions annually.\n(R) Autonomous vehicles utilize sensors, cameras, and lidar to perceive their surroundings.\n(S) However, complex edge-case weather conditions still present formidable engineering hurdles.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-R-P-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-R-P-Q",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Stem Education 28",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Encouraging young students to pursue STEM disciplines is crucial for technological progress.\n(Q) Hands-on robotics clubs and coding camps introduce complex ideas through playful engagement.\n(R) Early positive exposure builds lasting problem-solving confidence among young learners.\n(S) Schools that adopt experiential learning report higher enrollment in advanced science courses.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-P-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Plastic Pollution 29",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Discarded plastic packaging breaks down into microplastics that contaminate marine food webs.\n(Q) Single-use plastics take hundreds of years to decompose in natural ecosystems.\n(R) Marine organisms ingest these toxic particles, which subsequently enter the human diet.\n(S) Banning disposable plastics and developing biodegradable alternatives is imperative.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "S-Q-P-R",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-P-R-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Telemedicine Services 30",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Telemedicine has fundamentally transformed how patients receive basic healthcare.\n(Q) This remote accessibility saves rural patients hundreds of travel hours each year.\n(R) Individuals can consult medical specialists remotely via encrypted video consultations.\n(S) As virtual diagnostic tools improve, telemedicine will become a mainstay of primary healthcare.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Cloud Computing 31",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Companies no longer need to invest heavily in expensive physical server rooms.\n(Q) Instead, they pay only for the storage and compute capacity they actually consume.\n(R) Cloud infrastructure provides scalable on-demand computing resources.\n(S) This financial and operational agility accelerates software development cycles.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "S-R-P-Q",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-R-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Renewable Wind Power 32",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Wind turbines harness kinetic atmospheric energy to generate clean electricity.\n(Q) Modern turbine designs feature taller towers and longer aerodynamic blades.\n(R) These design innovations allow turbines to capture steady winds even at lower altitudes.\n(S) Consequently, wind farm capacity factors have increased significantly over the past decade.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-P-Q-R",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Microbiome Health 33",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) These microbes assist in digesting fiber and synthesizing vital vitamins.\n(Q) The human gut houses trillions of symbiotic microorganisms essential for health.\n(R) A diet rich in diverse plant-based foods nourishes this complex microbial ecosystem.\n(S) Conversely, ultra-processed foods diminish beneficial bacteria and trigger inflammation.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-Q-P-R",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - E-Commerce Logistics 34",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) E-commerce expansion has heightened customer expectations for rapid delivery.\n(Q) Automated robotics within these urban warehouses sort and package orders within minutes.\n(R) To fulfill same-day deliveries, retailers are building micro-fulfillment centers inside cities.\n(S) This localized fulfillment drastically shortens the final-mile transit duration.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Q-P-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Digital Payments 35",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Smartphone apps using QR codes have replaced physical paper cash across millions of vendor stalls.\n(Q) Transactions settle instantly into merchant accounts with minimal processing friction.\n(R) Digital payment ecosystems have revolutionized retail financial transactions.\n(S) This seamless financial inclusion empowers small informal vendors into the formal economy.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-R-P-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "S-R-P-Q",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Biodiversity Conservation 36",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Tropical rainforests harbor more than half of the planet's terrestrial species.\n(Q) Deforestation for cattle ranching and palm oil plantations threatens this rich biodiversity.\n(R) Loss of forest cover eliminates habitats and disrupts global rainfall patterns.\n(S) Conserving remaining primary forests is therefore essential to prevent mass species extinctions.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Autonomous Driving 37",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Onboard machine learning processors analyze sensor feeds in real time to steer and brake.\n(Q) Autonomous vehicles utilize sensors, cameras, and lidar to perceive their surroundings.\n(R) Eliminating human error could theoretically avert millions of traffic collisions annually.\n(S) However, complex edge-case weather conditions still present formidable engineering hurdles.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "S-Q-P-R",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-Q-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Stem Education 38",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Encouraging young students to pursue STEM disciplines is crucial for technological progress.\n(Q) Early positive exposure builds lasting problem-solving confidence among young learners.\n(R) Hands-on robotics clubs and coding camps introduce complex ideas through playful engagement.\n(S) Schools that adopt experiential learning report higher enrollment in advanced science courses.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Plastic Pollution 39",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Discarded plastic packaging breaks down into microplastics that contaminate marine food webs.\n(Q) Marine organisms ingest these toxic particles, which subsequently enter the human diet.\n(R) Single-use plastics take hundreds of years to decompose in natural ecosystems.\n(S) Banning disposable plastics and developing biodegradable alternatives is imperative.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-P-Q-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "S-R-P-Q",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-R-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Telemedicine Services 40",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Telemedicine has fundamentally transformed how patients receive basic healthcare.\n(Q) Individuals can consult medical specialists remotely via encrypted video consultations.\n(R) This remote accessibility saves rural patients hundreds of travel hours each year.\n(S) As virtual diagnostic tools improve, telemedicine will become a mainstay of primary healthcare.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-P-Q-R",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Cloud Computing 41",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Companies no longer need to invest heavily in expensive physical server rooms.\n(Q) Cloud infrastructure provides scalable on-demand computing resources.\n(R) Instead, they pay only for the storage and compute capacity they actually consume.\n(S) This financial and operational agility accelerates software development cycles.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "S-Q-P-R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Renewable Wind Power 42",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Wind turbines harness kinetic atmospheric energy to generate clean electricity.\n(Q) These design innovations allow turbines to capture steady winds even at lower altitudes.\n(R) Modern turbine designs feature taller towers and longer aerodynamic blades.\n(S) Consequently, wind farm capacity factors have increased significantly over the past decade.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Microbiome Health 43",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) These microbes assist in digesting fiber and synthesizing vital vitamins.\n(Q) A diet rich in diverse plant-based foods nourishes this complex microbial ecosystem.\n(R) The human gut houses trillions of symbiotic microorganisms essential for health.\n(S) Conversely, ultra-processed foods diminish beneficial bacteria and trigger inflammation.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-R-P-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "S-R-P-Q",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - E-Commerce Logistics 44",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) E-commerce expansion has heightened customer expectations for rapid delivery.\n(Q) To fulfill same-day deliveries, retailers are building micro-fulfillment centers inside cities.\n(R) Automated robotics within these urban warehouses sort and package orders within minutes.\n(S) This localized fulfillment drastically shortens the final-mile transit duration.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-P-Q-R",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Digital Payments 45",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Smartphone apps using QR codes have replaced physical paper cash across millions of vendor stalls.\n(Q) Digital payment ecosystems have revolutionized retail financial transactions.\n(R) Transactions settle instantly into merchant accounts with minimal processing friction.\n(S) This seamless financial inclusion empowers small informal vendors into the formal economy.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "S-Q-P-R",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "R-Q-P-S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles - Biodiversity Conservation 46",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Tropical rainforests harbor more than half of the planet's terrestrial species.\n(Q) Loss of forest cover eliminates habitats and disrupts global rainfall patterns.\n(R) Deforestation for cattle ranching and palm oil plantations threatens this rich biodiversity.\n(S) Conserving remaining primary forests is therefore essential to prevent mass species extinctions.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "R-P-Q-S",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Para Jumbles - Autonomous Driving 47",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Onboard machine learning processors analyze sensor feeds in real time to steer and brake.\n(Q) Eliminating human error could theoretically avert millions of traffic collisions annually.\n(R) Autonomous vehicles utilize sensors, cameras, and lidar to perceive their surroundings.\n(S) However, complex edge-case weather conditions still present formidable engineering hurdles.",
        "sample_answer": "The correct logical sequence is R-P-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Q-R-P-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "S-R-P-Q",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles - Stem Education 48",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Encouraging young students to pursue STEM disciplines is crucial for technological progress.\n(Q) Hands-on robotics clubs and coding camps introduce complex ideas through playful engagement.\n(R) Early positive exposure builds lasting problem-solving confidence among young learners.\n(S) Schools that adopt experiential learning report higher enrollment in advanced science courses.",
        "sample_answer": "The correct logical sequence is P-Q-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "S-P-Q-R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Plastic Pollution 49",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Discarded plastic packaging breaks down into microplastics that contaminate marine food webs.\n(Q) Single-use plastics take hundreds of years to decompose in natural ecosystems.\n(R) Marine organisms ingest these toxic particles, which subsequently enter the human diet.\n(S) Banning disposable plastics and developing biodegradable alternatives is imperative.",
        "sample_answer": "The correct logical sequence is Q-P-R-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-Q-R-S",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "R-Q-P-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "S-Q-P-R",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Q-P-R-S",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Para Jumbles - Telemedicine Services 50",
        "difficulty": "Medium",
        "question_text": "Rearrange the four sentences to form a meaningful, coherent paragraph:\n\n(P) Telemedicine has fundamentally transformed how patients receive basic healthcare.\n(Q) This remote accessibility saves rural patients hundreds of travel hours each year.\n(R) Individuals can consult medical specialists remotely via encrypted video consultations.\n(S) As virtual diagnostic tools improve, telemedicine will become a mainstay of primary healthcare.",
        "sample_answer": "The correct logical sequence is P-R-Q-S. It logically flows from introduction to elaboration to conclusion.",
        "tips": "Look for chronological development and transition words.",
        "options": [
            {
                "label": "A",
                "text": "P-R-Q-S",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Q-P-R-S",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "R-P-Q-S",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "P-Q-R-S",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Para Jumbles').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Para Jumbles').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Verbal Ability',
                    topic='Para Jumbles',
                    title=q.get('title', 'Para Jumbles'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Para Jumbles via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Para Jumbles: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Para Jumbles',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Verbal Ability', 'Para Jumbles',
                        q.get('title', 'Para Jumbles'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Para Jumbles into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
