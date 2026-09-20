"""
Seed script for Reading Comprehension (Verbal Ability)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Reading Comprehension - Renewable Energy and Solar Power",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Solar energy is one of the most promising renewable energy sources available today. By capturing sunlight using photovoltaic cells, solar panels convert solar radiation directly into electricity. Unlike fossil fuels, solar energy produces zero greenhouse gas emissions during operation, making it a critical tool in combating climate change. Additionally, the cost of manufacturing solar panels has decreased dramatically over the past decade, enabling wider adoption across residential, commercial, and industrial sectors. However, solar energy generation depends on daylight and weather conditions, necessitating efficient energy storage solutions like lithium-ion batteries to ensure uninterrupted power supply.\"\n\nQuestion: What is the primary method solar panels use to generate electricity?",
        "sample_answer": "Photovoltaic cells convert sunlight directly into electricity.",
        "tips": "Refer to the first sentence.",
        "options": [
            {
                "label": "A",
                "text": "Harnessing geothermal heat",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Burning fossil fuels",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Using photovoltaic cells",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Utilizing wind turbines",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Renewable Energy and Solar Power",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Solar energy is one of the most promising renewable energy sources available today. By capturing sunlight using photovoltaic cells, solar panels convert solar radiation directly into electricity. Unlike fossil fuels, solar energy produces zero greenhouse gas emissions during operation, making it a critical tool in combating climate change. Additionally, the cost of manufacturing solar panels has decreased dramatically over the past decade, enabling wider adoption across residential, commercial, and industrial sectors. However, solar energy generation depends on daylight and weather conditions, necessitating efficient energy storage solutions like lithium-ion batteries to ensure uninterrupted power supply.\"\n\nQuestion: Why is solar energy considered crucial in fighting climate change?",
        "sample_answer": "It produces zero greenhouse gas emissions during operation.",
        "tips": "Look for climate change mention in the text.",
        "options": [
            {
                "label": "A",
                "text": "It relies entirely on non-renewable sources",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "It increases atmospheric carbon",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "It produces zero greenhouse gas emissions",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "It generates excess industrial waste",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Renewable Energy and Solar Power",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Solar energy is one of the most promising renewable energy sources available today. By capturing sunlight using photovoltaic cells, solar panels convert solar radiation directly into electricity. Unlike fossil fuels, solar energy produces zero greenhouse gas emissions during operation, making it a critical tool in combating climate change. Additionally, the cost of manufacturing solar panels has decreased dramatically over the past decade, enabling wider adoption across residential, commercial, and industrial sectors. However, solar energy generation depends on daylight and weather conditions, necessitating efficient energy storage solutions like lithium-ion batteries to ensure uninterrupted power supply.\"\n\nQuestion: What has enabled wider adoption of solar panels recently?",
        "sample_answer": "A dramatic decrease in manufacturing costs over the past decade.",
        "tips": "Notice the cost trend mentioned.",
        "options": [
            {
                "label": "A",
                "text": "Scarcity of raw silicon",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Government prohibitions on other fuels",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Dramatic decrease in manufacturing costs",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Higher installation taxes",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Renewable Energy and Solar Power",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Solar energy is one of the most promising renewable energy sources available today. By capturing sunlight using photovoltaic cells, solar panels convert solar radiation directly into electricity. Unlike fossil fuels, solar energy produces zero greenhouse gas emissions during operation, making it a critical tool in combating climate change. Additionally, the cost of manufacturing solar panels has decreased dramatically over the past decade, enabling wider adoption across residential, commercial, and industrial sectors. However, solar energy generation depends on daylight and weather conditions, necessitating efficient energy storage solutions like lithium-ion batteries to ensure uninterrupted power supply.\"\n\nQuestion: What is a major limitation of solar power mentioned in the passage?",
        "sample_answer": "It depends on daylight and weather conditions.",
        "tips": "Check the challenges noted towards the end.",
        "options": [
            {
                "label": "A",
                "text": "Incompatibility with residential homes",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Extremely high operational emissions",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Dependence on daylight and weather conditions",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Complete inability to store energy",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Renewable Energy and Solar Power",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Solar energy is one of the most promising renewable energy sources available today. By capturing sunlight using photovoltaic cells, solar panels convert solar radiation directly into electricity. Unlike fossil fuels, solar energy produces zero greenhouse gas emissions during operation, making it a critical tool in combating climate change. Additionally, the cost of manufacturing solar panels has decreased dramatically over the past decade, enabling wider adoption across residential, commercial, and industrial sectors. However, solar energy generation depends on daylight and weather conditions, necessitating efficient energy storage solutions like lithium-ion batteries to ensure uninterrupted power supply.\"\n\nQuestion: What technology is recommended to address the intermittency of solar energy?",
        "sample_answer": "Lithium-ion batteries for efficient energy storage.",
        "tips": "See the final sentence about storage.",
        "options": [
            {
                "label": "A",
                "text": "Hydraulic pumps",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Coal backup generators",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Lithium-ion battery storage",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Steam turbines",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Importance of Sleep",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Sleep plays an indispensable role in maintaining physical health and cognitive function. During sleep, the brain consolidates memories, processes emotions, and removes toxic waste products accumulated throughout the day. Physically, the body repairs cellular tissues, synthesizes hormones, and strengthens the immune system. Chronic sleep deprivation has been linked to severe health risks, including cardiovascular disease, diabetes, obesity, and impaired mental performance. Health experts generally recommend that adults get between seven and nine hours of quality sleep each night to ensure optimal recovery and sustained alertness.\"\n\nQuestion: What cognitive benefit occurs during sleep according to the passage?",
        "sample_answer": "The brain consolidates memories and clears toxic waste products.",
        "tips": "Look for brain and cognitive functions.",
        "options": [
            {
                "label": "A",
                "text": "Complete cessation of brain waves",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Rapid reduction of vocabulary",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Consolidation of memories and removal of toxins",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Loss of prior memories",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Importance of Sleep",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Sleep plays an indispensable role in maintaining physical health and cognitive function. During sleep, the brain consolidates memories, processes emotions, and removes toxic waste products accumulated throughout the day. Physically, the body repairs cellular tissues, synthesizes hormones, and strengthens the immune system. Chronic sleep deprivation has been linked to severe health risks, including cardiovascular disease, diabetes, obesity, and impaired mental performance. Health experts generally recommend that adults get between seven and nine hours of quality sleep each night to ensure optimal recovery and sustained alertness.\"\n\nQuestion: Which of the following physical benefits is facilitated by sleep?",
        "sample_answer": "Repairing cellular tissues and strengthening the immune system.",
        "tips": "Check physical repairs in the text.",
        "options": [
            {
                "label": "A",
                "text": "Permanent loss of muscle mass",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Dehydration of organs",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Tissue repair and immune system strengthening",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Decreased antibody production",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Importance of Sleep",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Sleep plays an indispensable role in maintaining physical health and cognitive function. During sleep, the brain consolidates memories, processes emotions, and removes toxic waste products accumulated throughout the day. Physically, the body repairs cellular tissues, synthesizes hormones, and strengthens the immune system. Chronic sleep deprivation has been linked to severe health risks, including cardiovascular disease, diabetes, obesity, and impaired mental performance. Health experts generally recommend that adults get between seven and nine hours of quality sleep each night to ensure optimal recovery and sustained alertness.\"\n\nQuestion: What is a known consequence of chronic sleep deprivation?",
        "sample_answer": "Increased risk of cardiovascular disease, diabetes, and impaired performance.",
        "tips": "Look for long-term health risks.",
        "options": [
            {
                "label": "A",
                "text": "Guaranteed weight reduction",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Immunity to viral infections",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Increased risk of cardiovascular disease and diabetes",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Enhanced athletic endurance",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Importance of Sleep",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Sleep plays an indispensable role in maintaining physical health and cognitive function. During sleep, the brain consolidates memories, processes emotions, and removes toxic waste products accumulated throughout the day. Physically, the body repairs cellular tissues, synthesizes hormones, and strengthens the immune system. Chronic sleep deprivation has been linked to severe health risks, including cardiovascular disease, diabetes, obesity, and impaired mental performance. Health experts generally recommend that adults get between seven and nine hours of quality sleep each night to ensure optimal recovery and sustained alertness.\"\n\nQuestion: How many hours of sleep do health experts recommend for adults?",
        "sample_answer": "Between seven and nine hours each night.",
        "tips": "Check the expert recommendation at the end.",
        "options": [
            {
                "label": "A",
                "text": "10 to 12 hours",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Less than 6 hours",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "7 to 9 hours",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "4 to 5 hours",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Importance of Sleep",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Sleep plays an indispensable role in maintaining physical health and cognitive function. During sleep, the brain consolidates memories, processes emotions, and removes toxic waste products accumulated throughout the day. Physically, the body repairs cellular tissues, synthesizes hormones, and strengthens the immune system. Chronic sleep deprivation has been linked to severe health risks, including cardiovascular disease, diabetes, obesity, and impaired mental performance. Health experts generally recommend that adults get between seven and nine hours of quality sleep each night to ensure optimal recovery and sustained alertness.\"\n\nQuestion: What is the central message of the passage?",
        "sample_answer": "Sleep is vital for both cognitive and physiological health.",
        "tips": "Identify the overarching main idea.",
        "options": [
            {
                "label": "A",
                "text": "Adults need only 4 hours of rest",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Diet is the sole factor in immune strength",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Sleep is essential for physical and cognitive well-being",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Sleep should be minimized to boost productivity",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Artificial Intelligence in Medicine",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Artificial intelligence (AI) is transforming modern healthcare by accelerating diagnosis and personalizing treatment plans. Machine learning algorithms trained on millions of medical images can detect early signs of diseases such as cancer and retinal degeneration with accuracy comparable to experienced radiologists. Moreover, predictive AI models assist doctors in anticipating patient complications before they occur, allowing for proactive interventions. While AI serves as a powerful diagnostic aid, medical professionals emphasize that algorithms are designed to augment, not replace, human doctors, whose empathy and clinical judgment remain irreplaceable.\"\n\nQuestion: In what way does AI primarily aid medical diagnosis?",
        "sample_answer": "By analyzing medical images to detect early signs of diseases.",
        "tips": "Check the second sentence on imaging.",
        "options": [
            {
                "label": "A",
                "text": "Replacing laboratory technicians entirely",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Performing open-heart surgeries autonomously",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Analyzing medical images with high accuracy",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Eliminating the need for medical imaging",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Artificial Intelligence in Medicine",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Artificial intelligence (AI) is transforming modern healthcare by accelerating diagnosis and personalizing treatment plans. Machine learning algorithms trained on millions of medical images can detect early signs of diseases such as cancer and retinal degeneration with accuracy comparable to experienced radiologists. Moreover, predictive AI models assist doctors in anticipating patient complications before they occur, allowing for proactive interventions. While AI serves as a powerful diagnostic aid, medical professionals emphasize that algorithms are designed to augment, not replace, human doctors, whose empathy and clinical judgment remain irreplaceable.\"\n\nQuestion: How do predictive AI models assist healthcare practitioners?",
        "sample_answer": "By forecasting patient complications before they arise.",
        "tips": "Look for predictive models in the passage.",
        "options": [
            {
                "label": "A",
                "text": "Automating patient billing exclusively",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Prescribing generic drugs randomly",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Anticipating patient complications proactively",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Discharging patients without evaluation",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Artificial Intelligence in Medicine",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Artificial intelligence (AI) is transforming modern healthcare by accelerating diagnosis and personalizing treatment plans. Machine learning algorithms trained on millions of medical images can detect early signs of diseases such as cancer and retinal degeneration with accuracy comparable to experienced radiologists. Moreover, predictive AI models assist doctors in anticipating patient complications before they occur, allowing for proactive interventions. While AI serves as a powerful diagnostic aid, medical professionals emphasize that algorithms are designed to augment, not replace, human doctors, whose empathy and clinical judgment remain irreplaceable.\"\n\nQuestion: According to experts, what role is AI intended to serve in relation to doctors?",
        "sample_answer": "To augment human doctors rather than replace them.",
        "tips": "See the concluding sentence.",
        "options": [
            {
                "label": "A",
                "text": "To make medical judgment obsolete",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "To fully replace all human physicians",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "To augment and assist human clinicians",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "To limit patient access to doctors",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Artificial Intelligence in Medicine",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Artificial intelligence (AI) is transforming modern healthcare by accelerating diagnosis and personalizing treatment plans. Machine learning algorithms trained on millions of medical images can detect early signs of diseases such as cancer and retinal degeneration with accuracy comparable to experienced radiologists. Moreover, predictive AI models assist doctors in anticipating patient complications before they occur, allowing for proactive interventions. While AI serves as a powerful diagnostic aid, medical professionals emphasize that algorithms are designed to augment, not replace, human doctors, whose empathy and clinical judgment remain irreplaceable.\"\n\nQuestion: Which unique human qualities cannot be replaced by AI according to the text?",
        "sample_answer": "Empathy and clinical judgment.",
        "tips": "Read the last phrase carefully.",
        "options": [
            {
                "label": "A",
                "text": "Image pixel scanning",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Data calculation speed",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Empathy and clinical judgment",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Algorithmic consistency",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Artificial Intelligence in Medicine",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Artificial intelligence (AI) is transforming modern healthcare by accelerating diagnosis and personalizing treatment plans. Machine learning algorithms trained on millions of medical images can detect early signs of diseases such as cancer and retinal degeneration with accuracy comparable to experienced radiologists. Moreover, predictive AI models assist doctors in anticipating patient complications before they occur, allowing for proactive interventions. While AI serves as a powerful diagnostic aid, medical professionals emphasize that algorithms are designed to augment, not replace, human doctors, whose empathy and clinical judgment remain irreplaceable.\"\n\nQuestion: What is the primary tone of the passage regarding AI in healthcare?",
        "sample_answer": "Optimistic yet balanced about human-AI collaboration.",
        "tips": "Analyze the author's balanced perspective.",
        "options": [
            {
                "label": "A",
                "text": "Dismissive and indifferent",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Hostile and skeptical",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Constructive and collaborative",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Purely speculative",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Microfinance and Economic Empowerment",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Microfinance refers to the provision of small financial services, such as microloans and savings accounts, to low-income individuals and entrepreneurs who lack access to conventional banking services. By providing initial working capital, microfinance enables individuals to launch small businesses, purchase agricultural supplies, or invest in education. Studies show that female entrepreneurs constitute a large majority of microfinance borrowers, often reinvesting their earnings into household nutrition and children's schooling. However, critics caution that excessively high interest rates charged by some microfinance institutions can lead to over-indebtedness among vulnerable communities.\"\n\nQuestion: Who is the primary target demographic for microfinance services?",
        "sample_answer": "Low-income individuals and small entrepreneurs lacking conventional banking.",
        "tips": "Check the opening sentence.",
        "options": [
            {
                "label": "A",
                "text": "Low-income individuals lacking regular banking access",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Multinational corporate directors",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "High-net-worth investors",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Commercial real estate developers",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Microfinance and Economic Empowerment",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Microfinance refers to the provision of small financial services, such as microloans and savings accounts, to low-income individuals and entrepreneurs who lack access to conventional banking services. By providing initial working capital, microfinance enables individuals to launch small businesses, purchase agricultural supplies, or invest in education. Studies show that female entrepreneurs constitute a large majority of microfinance borrowers, often reinvesting their earnings into household nutrition and children's schooling. However, critics caution that excessively high interest rates charged by some microfinance institutions can lead to over-indebtedness among vulnerable communities.\"\n\nQuestion: What is a common use of microloans highlighted in the passage?",
        "sample_answer": "Starting small enterprises or purchasing agricultural inputs.",
        "tips": "Refer to the second sentence.",
        "options": [
            {
                "label": "A",
                "text": "Launching small businesses or buying supplies",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Speculative cryptocurrency trading",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Purchasing luxury goods abroad",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Funding heavy industrial factories",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Microfinance and Economic Empowerment",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Microfinance refers to the provision of small financial services, such as microloans and savings accounts, to low-income individuals and entrepreneurs who lack access to conventional banking services. By providing initial working capital, microfinance enables individuals to launch small businesses, purchase agricultural supplies, or invest in education. Studies show that female entrepreneurs constitute a large majority of microfinance borrowers, often reinvesting their earnings into household nutrition and children's schooling. However, critics caution that excessively high interest rates charged by some microfinance institutions can lead to over-indebtedness among vulnerable communities.\"\n\nQuestion: Why is the high participation of female borrowers significant?",
        "sample_answer": "They tend to reinvest income in household health and children's schooling.",
        "tips": "Look for female entrepreneur impact.",
        "options": [
            {
                "label": "A",
                "text": "They reinvest earnings into household welfare and education",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "They avoid taking any loans",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "They migrate to foreign markets",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "They close down small businesses",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Microfinance and Economic Empowerment",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Microfinance refers to the provision of small financial services, such as microloans and savings accounts, to low-income individuals and entrepreneurs who lack access to conventional banking services. By providing initial working capital, microfinance enables individuals to launch small businesses, purchase agricultural supplies, or invest in education. Studies show that female entrepreneurs constitute a large majority of microfinance borrowers, often reinvesting their earnings into household nutrition and children's schooling. However, critics caution that excessively high interest rates charged by some microfinance institutions can lead to over-indebtedness among vulnerable communities.\"\n\nQuestion: What concern do critics raise regarding some microfinance practices?",
        "sample_answer": "High interest rates potentially leading to excessive debt.",
        "tips": "Notice the critique in the last sentence.",
        "options": [
            {
                "label": "A",
                "text": "High interest rates leading to over-indebtedness",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Complete lack of collateral requirements",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Too much government oversight",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Excessive transparency in lending",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Microfinance and Economic Empowerment",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Microfinance refers to the provision of small financial services, such as microloans and savings accounts, to low-income individuals and entrepreneurs who lack access to conventional banking services. By providing initial working capital, microfinance enables individuals to launch small businesses, purchase agricultural supplies, or invest in education. Studies show that female entrepreneurs constitute a large majority of microfinance borrowers, often reinvesting their earnings into household nutrition and children's schooling. However, critics caution that excessively high interest rates charged by some microfinance institutions can lead to over-indebtedness among vulnerable communities.\"\n\nQuestion: What is the main goal of microfinance as described in the text?",
        "sample_answer": "Fostering financial inclusion and grassroot economic empowerment.",
        "tips": "Synthesize the overarching goal.",
        "options": [
            {
                "label": "A",
                "text": "Promoting financial inclusion and poverty alleviation",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Replacing central banks completely",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Maximizing corporate profits",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Discouraging small private enterprise",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - The Water Cycle and Climate",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The hydrological cycle is a continuous natural process through which water circulates between the Earth's oceans, atmosphere, and land surfaces. Evaporation driven by solar heat turns liquid water into vapor, which ascends into the cooler atmosphere and condenses into clouds. Precipitation then returns water to the surface in the form of rain or snow, replenishing rivers, lakes, and underground aquifers. Climate change disrupts this delicate cycle by raising global temperatures, which accelerates evaporation rates and leads to more intense rainfall events as well as prolonged periods of drought.\"\n\nQuestion: What drives the process of evaporation in the hydrological cycle?",
        "sample_answer": "Solar heat warming water surfaces.",
        "tips": "Check the sentence describing evaporation.",
        "options": [
            {
                "label": "A",
                "text": "Wind velocity alone",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Subterranean pressure",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Solar heat warming liquid water",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Geomagnetic fields",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Water Cycle and Climate",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The hydrological cycle is a continuous natural process through which water circulates between the Earth's oceans, atmosphere, and land surfaces. Evaporation driven by solar heat turns liquid water into vapor, which ascends into the cooler atmosphere and condenses into clouds. Precipitation then returns water to the surface in the form of rain or snow, replenishing rivers, lakes, and underground aquifers. Climate change disrupts this delicate cycle by raising global temperatures, which accelerates evaporation rates and leads to more intense rainfall events as well as prolonged periods of drought.\"\n\nQuestion: What happens during the condensation phase of the water cycle?",
        "sample_answer": "Water vapor cools and condenses into clouds.",
        "tips": "Check condensation details.",
        "options": [
            {
                "label": "A",
                "text": "Clouds turn into vapor",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Oceans absorb rainfall directly",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Water vapor cools and forms clouds",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Ice sublimates instantly into steam",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Water Cycle and Climate",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The hydrological cycle is a continuous natural process through which water circulates between the Earth's oceans, atmosphere, and land surfaces. Evaporation driven by solar heat turns liquid water into vapor, which ascends into the cooler atmosphere and condenses into clouds. Precipitation then returns water to the surface in the form of rain or snow, replenishing rivers, lakes, and underground aquifers. Climate change disrupts this delicate cycle by raising global temperatures, which accelerates evaporation rates and leads to more intense rainfall events as well as prolonged periods of drought.\"\n\nQuestion: How does precipitation benefit terrestrial water bodies?",
        "sample_answer": "By replenishing lakes, rivers, and underground aquifers.",
        "tips": "Look for precipitation effects.",
        "options": [
            {
                "label": "A",
                "text": "Draining freshwater reserves",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Increasing surface water salinity to sea level",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Replenishing lakes, rivers, and aquifers",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Preventing plant germination",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Water Cycle and Climate",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The hydrological cycle is a continuous natural process through which water circulates between the Earth's oceans, atmosphere, and land surfaces. Evaporation driven by solar heat turns liquid water into vapor, which ascends into the cooler atmosphere and condenses into clouds. Precipitation then returns water to the surface in the form of rain or snow, replenishing rivers, lakes, and underground aquifers. Climate change disrupts this delicate cycle by raising global temperatures, which accelerates evaporation rates and leads to more intense rainfall events as well as prolonged periods of drought.\"\n\nQuestion: How does climate change impact the water cycle?",
        "sample_answer": "It intensifies evaporation and causes both extreme storms and severe droughts.",
        "tips": "See the final sentence on climate effects.",
        "options": [
            {
                "label": "A",
                "text": "Freezes all global precipitation",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Stabilizes global rainfall permanently",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Accelerates evaporation, causing extreme rain and droughts",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Completely stops evaporation worldwide",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Water Cycle and Climate",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The hydrological cycle is a continuous natural process through which water circulates between the Earth's oceans, atmosphere, and land surfaces. Evaporation driven by solar heat turns liquid water into vapor, which ascends into the cooler atmosphere and condenses into clouds. Precipitation then returns water to the surface in the form of rain or snow, replenishing rivers, lakes, and underground aquifers. Climate change disrupts this delicate cycle by raising global temperatures, which accelerates evaporation rates and leads to more intense rainfall events as well as prolonged periods of drought.\"\n\nQuestion: The word 'replenishing' in the passage is closest in meaning to:",
        "sample_answer": "'Replenishing' means refilling or restoring supplies.",
        "tips": "Vocabulary in context.",
        "options": [
            {
                "label": "A",
                "text": "Depleting",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Contaminating",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Restoring or refilling",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Evaporating",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Cybersecurity in the Digital Era",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"As businesses and governments transition their operations to cloud platforms, cybersecurity has emerged as a fundamental operational imperative. Cyber threats have evolved from simple viruses into sophisticated multi-vector attacks, including ransomware, phishing, and supply chain compromises. A single security breach can result in massive financial losses, intellectual property theft, and reputational damage. To safeguard critical data, organizations adopt a 'Zero Trust' architecture, which requires strict identity verification for every person and device attempting to access private network resources, regardless of whether they are inside or outside the network perimeter.\"\n\nQuestion: What has accelerated the urgency of robust cybersecurity?",
        "sample_answer": "The migration of organizational operations to cloud platforms.",
        "tips": "Refer to the opening sentence.",
        "options": [
            {
                "label": "A",
                "text": "Transition of operations to cloud environments",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Decreased dependence on internet connectivity",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "The complete eradication of malware",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Reduction in online financial transactions",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cybersecurity in the Digital Era",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"As businesses and governments transition their operations to cloud platforms, cybersecurity has emerged as a fundamental operational imperative. Cyber threats have evolved from simple viruses into sophisticated multi-vector attacks, including ransomware, phishing, and supply chain compromises. A single security breach can result in massive financial losses, intellectual property theft, and reputational damage. To safeguard critical data, organizations adopt a 'Zero Trust' architecture, which requires strict identity verification for every person and device attempting to access private network resources, regardless of whether they are inside or outside the network perimeter.\"\n\nQuestion: Which of the following is listed as a sophisticated modern cyber threat?",
        "sample_answer": "Ransomware, phishing, and supply chain breaches.",
        "tips": "Check the threats mentioned.",
        "options": [
            {
                "label": "A",
                "text": "Ransomware and phishing attacks",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Manual paper shredding",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Analog wiretapping",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Physical lock picking",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cybersecurity in the Digital Era",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"As businesses and governments transition their operations to cloud platforms, cybersecurity has emerged as a fundamental operational imperative. Cyber threats have evolved from simple viruses into sophisticated multi-vector attacks, including ransomware, phishing, and supply chain compromises. A single security breach can result in massive financial losses, intellectual property theft, and reputational damage. To safeguard critical data, organizations adopt a 'Zero Trust' architecture, which requires strict identity verification for every person and device attempting to access private network resources, regardless of whether they are inside or outside the network perimeter.\"\n\nQuestion: What is a major consequence of a cybersecurity breach?",
        "sample_answer": "Financial losses, intellectual property theft, and brand damage.",
        "tips": "Look for breach consequences in text.",
        "options": [
            {
                "label": "A",
                "text": "Financial loss and reputational damage",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Increased server bandwidth",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Guaranteed insurance payouts",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Automatic system hardware upgrades",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cybersecurity in the Digital Era",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"As businesses and governments transition their operations to cloud platforms, cybersecurity has emerged as a fundamental operational imperative. Cyber threats have evolved from simple viruses into sophisticated multi-vector attacks, including ransomware, phishing, and supply chain compromises. A single security breach can result in massive financial losses, intellectual property theft, and reputational damage. To safeguard critical data, organizations adopt a 'Zero Trust' architecture, which requires strict identity verification for every person and device attempting to access private network resources, regardless of whether they are inside or outside the network perimeter.\"\n\nQuestion: What is the core principle of a 'Zero Trust' security model?",
        "sample_answer": "Strict verification of all users and devices regardless of network location.",
        "tips": "See the definition of Zero Trust.",
        "options": [
            {
                "label": "A",
                "text": "Verifying every user and device whether inside or outside",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Disabling multi-factor authentication",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Trusting internal employees implicitly",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Leaving corporate Wi-Fi open",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cybersecurity in the Digital Era",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"As businesses and governments transition their operations to cloud platforms, cybersecurity has emerged as a fundamental operational imperative. Cyber threats have evolved from simple viruses into sophisticated multi-vector attacks, including ransomware, phishing, and supply chain compromises. A single security breach can result in massive financial losses, intellectual property theft, and reputational damage. To safeguard critical data, organizations adopt a 'Zero Trust' architecture, which requires strict identity verification for every person and device attempting to access private network resources, regardless of whether they are inside or outside the network perimeter.\"\n\nQuestion: The term 'perimeter' in the context of network security refers to:",
        "sample_answer": "The boundary dividing an internal network from external networks.",
        "tips": "Vocabulary context.",
        "options": [
            {
                "label": "A",
                "text": "The boundary between secure internal and external networks",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "The length of server cables",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "The physical size of a computer monitor",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The total number of connected users",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Urban Public Transportation",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Urban centers across the globe face acute challenges from vehicular traffic congestion and air pollution. Investing in reliable public transportation systems, such as metro trains and rapid bus corridors, offers a viable pathway to sustainable urban growth. Efficient mass transit reduces the number of private cars on city roads, decreasing carbon monoxide emissions and conserving non-renewable fossil fuels. Furthermore, accessible public transit enhances social mobility by connecting low-income residents with distant employment and educational centers. Urban planners stress that for public transit to be successful, it must be affordable, punctual, and safely integrated with pedestrian infrastructure.\"\n\nQuestion: What primary urban problem does mass transit help alleviate?",
        "sample_answer": "Traffic congestion and vehicular air pollution.",
        "tips": "Check the first two sentences.",
        "options": [
            {
                "label": "A",
                "text": "Shortage of rural farmland",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Excessive pedestrian pathways",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Overabundance of parking lots",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Traffic congestion and harmful air emissions",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Urban Public Transportation",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Urban centers across the globe face acute challenges from vehicular traffic congestion and air pollution. Investing in reliable public transportation systems, such as metro trains and rapid bus corridors, offers a viable pathway to sustainable urban growth. Efficient mass transit reduces the number of private cars on city roads, decreasing carbon monoxide emissions and conserving non-renewable fossil fuels. Furthermore, accessible public transit enhances social mobility by connecting low-income residents with distant employment and educational centers. Urban planners stress that for public transit to be successful, it must be affordable, punctual, and safely integrated with pedestrian infrastructure.\"\n\nQuestion: How does mass transit contribute to social mobility?",
        "sample_answer": "By linking lower-income communities to jobs and educational opportunities.",
        "tips": "Look for social mobility benefits.",
        "options": [
            {
                "label": "A",
                "text": "Restricting travel to private vehicle owners",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Charging premium fares for distant stops",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Encouraging suburban isolation",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Connecting marginalized citizens to jobs and education",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Urban Public Transportation",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Urban centers across the globe face acute challenges from vehicular traffic congestion and air pollution. Investing in reliable public transportation systems, such as metro trains and rapid bus corridors, offers a viable pathway to sustainable urban growth. Efficient mass transit reduces the number of private cars on city roads, decreasing carbon monoxide emissions and conserving non-renewable fossil fuels. Furthermore, accessible public transit enhances social mobility by connecting low-income residents with distant employment and educational centers. Urban planners stress that for public transit to be successful, it must be affordable, punctual, and safely integrated with pedestrian infrastructure.\"\n\nQuestion: Which factor is essential for mass transit success according to planners?",
        "sample_answer": "Affordability, punctuality, and safe pedestrian connectivity.",
        "tips": "See the final sentence.",
        "options": [
            {
                "label": "A",
                "text": "High luxury fares",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Complete ban on walking",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Irregular unpredictable schedules",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Affordability, punctuality, and pedestrian integration",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Urban Public Transportation",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Urban centers across the globe face acute challenges from vehicular traffic congestion and air pollution. Investing in reliable public transportation systems, such as metro trains and rapid bus corridors, offers a viable pathway to sustainable urban growth. Efficient mass transit reduces the number of private cars on city roads, decreasing carbon monoxide emissions and conserving non-renewable fossil fuels. Furthermore, accessible public transit enhances social mobility by connecting low-income residents with distant employment and educational centers. Urban planners stress that for public transit to be successful, it must be affordable, punctual, and safely integrated with pedestrian infrastructure.\"\n\nQuestion: What environmental benefit is directly derived from fewer private vehicles?",
        "sample_answer": "Reduced carbon emissions and fuel conservation.",
        "tips": "Refer to paragraph 1.",
        "options": [
            {
                "label": "A",
                "text": "Increased smog formation",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Depletion of ozone layers",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Higher street noise",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Lower carbon emissions and fossil fuel conservation",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Urban Public Transportation",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Urban centers across the globe face acute challenges from vehicular traffic congestion and air pollution. Investing in reliable public transportation systems, such as metro trains and rapid bus corridors, offers a viable pathway to sustainable urban growth. Efficient mass transit reduces the number of private cars on city roads, decreasing carbon monoxide emissions and conserving non-renewable fossil fuels. Furthermore, accessible public transit enhances social mobility by connecting low-income residents with distant employment and educational centers. Urban planners stress that for public transit to be successful, it must be affordable, punctual, and safely integrated with pedestrian infrastructure.\"\n\nQuestion: What is the main purpose of the passage?",
        "sample_answer": "To highlight the economic and environmental benefits of urban public transit.",
        "tips": "Synthesize central theme.",
        "options": [
            {
                "label": "A",
                "text": "Promoting private car manufacturing",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Discouraging city migration",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Critiquing pedestrian walkways",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Advocating for robust and accessible public transit systems",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Cognitive Benefits of Bilingualism",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Acquiring fluency in more than one language confers significant cognitive advantages beyond social communication. Neuroscientific research shows that bilingual individuals constantly switch between linguistic systems, which exercises the brain's executive control center. As a result, bilingual speakers often exhibit superior multitasking abilities, enhanced problem-solving skills, and better attentional focus. Furthermore, longitudinal studies suggest that lifelong bilingualism delays the onset of age-related cognitive decline and symptoms of dementia by several years, reinforcing the concept that linguistic learning acts as cognitive resistance training.\"\n\nQuestion: What brain area is strengthened through bilingual language switching?",
        "sample_answer": "The executive control center.",
        "tips": "Check sentence 2.",
        "options": [
            {
                "label": "A",
                "text": "The brain's executive control center",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "The spinal reflex pathways",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "The optic sensory tract",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The auditory balance canals",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cognitive Benefits of Bilingualism",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Acquiring fluency in more than one language confers significant cognitive advantages beyond social communication. Neuroscientific research shows that bilingual individuals constantly switch between linguistic systems, which exercises the brain's executive control center. As a result, bilingual speakers often exhibit superior multitasking abilities, enhanced problem-solving skills, and better attentional focus. Furthermore, longitudinal studies suggest that lifelong bilingualism delays the onset of age-related cognitive decline and symptoms of dementia by several years, reinforcing the concept that linguistic learning acts as cognitive resistance training.\"\n\nQuestion: Which cognitive skill is enhanced in bilingual individuals?",
        "sample_answer": "Multitasking, problem-solving, and focused attention.",
        "tips": "Look for cognitive advantages listed.",
        "options": [
            {
                "label": "A",
                "text": "Superior multitasking and attentional focus",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Difficulty concentrating",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Reduced memory retention",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Inability to learn mathematics",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cognitive Benefits of Bilingualism",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Acquiring fluency in more than one language confers significant cognitive advantages beyond social communication. Neuroscientific research shows that bilingual individuals constantly switch between linguistic systems, which exercises the brain's executive control center. As a result, bilingual speakers often exhibit superior multitasking abilities, enhanced problem-solving skills, and better attentional focus. Furthermore, longitudinal studies suggest that lifelong bilingualism delays the onset of age-related cognitive decline and symptoms of dementia by several years, reinforcing the concept that linguistic learning acts as cognitive resistance training.\"\n\nQuestion: What health advantage in older adults is associated with bilingualism?",
        "sample_answer": "Delayed onset of cognitive decline and dementia symptoms.",
        "tips": "Check longitudinal study findings.",
        "options": [
            {
                "label": "A",
                "text": "Delay in symptoms of dementia and cognitive decline",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Accelerated memory loss",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Complete immunity to physical aging",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Reduction in total sleep requirement",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cognitive Benefits of Bilingualism",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Acquiring fluency in more than one language confers significant cognitive advantages beyond social communication. Neuroscientific research shows that bilingual individuals constantly switch between linguistic systems, which exercises the brain's executive control center. As a result, bilingual speakers often exhibit superior multitasking abilities, enhanced problem-solving skills, and better attentional focus. Furthermore, longitudinal studies suggest that lifelong bilingualism delays the onset of age-related cognitive decline and symptoms of dementia by several years, reinforcing the concept that linguistic learning acts as cognitive resistance training.\"\n\nQuestion: In the passage, linguistic learning is metaphorically compared to:",
        "sample_answer": "Cognitive resistance training or physical exercise for the brain.",
        "tips": "Check the concluding sentence metaphor.",
        "options": [
            {
                "label": "A",
                "text": "Cognitive resistance training",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "A mechanical clockwork",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "A musical symphony",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "A financial investment portfolio",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - Cognitive Benefits of Bilingualism",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"Acquiring fluency in more than one language confers significant cognitive advantages beyond social communication. Neuroscientific research shows that bilingual individuals constantly switch between linguistic systems, which exercises the brain's executive control center. As a result, bilingual speakers often exhibit superior multitasking abilities, enhanced problem-solving skills, and better attentional focus. Furthermore, longitudinal studies suggest that lifelong bilingualism delays the onset of age-related cognitive decline and symptoms of dementia by several years, reinforcing the concept that linguistic learning acts as cognitive resistance training.\"\n\nQuestion: What can be inferred about monolingual individuals compared to bilinguals?",
        "sample_answer": "They may have fewer daily opportunities to exercise executive control through language switching.",
        "tips": "Inference based on text.",
        "options": [
            {
                "label": "A",
                "text": "They do not regularly exercise the same linguistic switching mechanisms",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "They cannot learn technical subjects",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "They have lower general intelligence",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "They never experience memory issues",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension - The Ethics of Gene Editing",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"CRISPR-Cas9 technology has revolutionized genetic engineering by providing scientists with an accessible tool to modify DNA sequences with unprecedented precision. This capability holds immense potential for eradicating hereditary disorders like sickle cell anemia and cystic fibrosis. However, the prospect of germline gene editing\u2014making modifications that are inheritable by future generations\u2014has ignited heated bioethical debates. Critics express grave concerns regarding unintended genetic mutations, unknown long-term health risks, and the socio-economic disparities that could arise if genetic enhancements become available only to wealthy elites.\"\n\nQuestion: What is the primary breakthrough offered by CRISPR-Cas9?",
        "sample_answer": "Precise and accessible modification of DNA sequences.",
        "tips": "Check sentence 1.",
        "options": [
            {
                "label": "A",
                "text": "Eliminating all viral infections worldwide",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Curing infectious diseases through radiation",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "High-precision genetic sequence modification",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Cloning entire human organs in days",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Ethics of Gene Editing",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"CRISPR-Cas9 technology has revolutionized genetic engineering by providing scientists with an accessible tool to modify DNA sequences with unprecedented precision. This capability holds immense potential for eradicating hereditary disorders like sickle cell anemia and cystic fibrosis. However, the prospect of germline gene editing\u2014making modifications that are inheritable by future generations\u2014has ignited heated bioethical debates. Critics express grave concerns regarding unintended genetic mutations, unknown long-term health risks, and the socio-economic disparities that could arise if genetic enhancements become available only to wealthy elites.\"\n\nQuestion: Which diseases are mentioned as candidates for gene editing therapies?",
        "sample_answer": "Hereditary disorders like sickle cell anemia and cystic fibrosis.",
        "tips": "Look for disease examples.",
        "options": [
            {
                "label": "A",
                "text": "Type-2 diabetes and osteoarthritis",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Bacterial pneumonia and flu",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Sickle cell anemia and cystic fibrosis",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Common cold and seasonal allergies",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Ethics of Gene Editing",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"CRISPR-Cas9 technology has revolutionized genetic engineering by providing scientists with an accessible tool to modify DNA sequences with unprecedented precision. This capability holds immense potential for eradicating hereditary disorders like sickle cell anemia and cystic fibrosis. However, the prospect of germline gene editing\u2014making modifications that are inheritable by future generations\u2014has ignited heated bioethical debates. Critics express grave concerns regarding unintended genetic mutations, unknown long-term health risks, and the socio-economic disparities that could arise if genetic enhancements become available only to wealthy elites.\"\n\nQuestion: Why does germline editing provoke particular ethical scrutiny?",
        "sample_answer": "Because genetic changes are passed down to future generations.",
        "tips": "Check definition of germline editing.",
        "options": [
            {
                "label": "A",
                "text": "It only affects elderly patients",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "It cannot be tested in laboratory settings",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Changes are inheritable by future generations",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "It takes decades to perform single edits",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Ethics of Gene Editing",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"CRISPR-Cas9 technology has revolutionized genetic engineering by providing scientists with an accessible tool to modify DNA sequences with unprecedented precision. This capability holds immense potential for eradicating hereditary disorders like sickle cell anemia and cystic fibrosis. However, the prospect of germline gene editing\u2014making modifications that are inheritable by future generations\u2014has ignited heated bioethical debates. Critics express grave concerns regarding unintended genetic mutations, unknown long-term health risks, and the socio-economic disparities that could arise if genetic enhancements become available only to wealthy elites.\"\n\nQuestion: What socio-economic fear is raised regarding genetic enhancements?",
        "sample_answer": "Enhancements might become exclusive privileges for wealthy elites.",
        "tips": "Check the concluding warnings.",
        "options": [
            {
                "label": "A",
                "text": "Global economies will crash",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Medical research will be banned completely",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Genetic enhancements might widen inequality between rich and poor",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "All private healthcare providers will shut down",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - The Ethics of Gene Editing",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"CRISPR-Cas9 technology has revolutionized genetic engineering by providing scientists with an accessible tool to modify DNA sequences with unprecedented precision. This capability holds immense potential for eradicating hereditary disorders like sickle cell anemia and cystic fibrosis. However, the prospect of germline gene editing\u2014making modifications that are inheritable by future generations\u2014has ignited heated bioethical debates. Critics express grave concerns regarding unintended genetic mutations, unknown long-term health risks, and the socio-economic disparities that could arise if genetic enhancements become available only to wealthy elites.\"\n\nQuestion: The word 'unprecedented' in the passage means:",
        "sample_answer": "Never known or achieved before.",
        "tips": "Vocabulary definition.",
        "options": [
            {
                "label": "A",
                "text": "Completely accidental",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Standard and routine",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Never done or known before",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Extremely slow",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension - Remote Work and Corporate Culture",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The rapid expansion of remote work has fundamentally altered traditional workplace dynamics. For employees, the elimination of daily commutes translates into substantial time savings and improved work-life balance. For employers, geographical barriers are removed, allowing organizations to recruit top talent from an international candidate pool while reducing real estate costs. Nonetheless, sustaining organizational culture and team cohesion presents real hurdles in a distributed environment. Companies are increasingly adopting hybrid operational models, blending remote autonomy with structured in-person gatherings to cultivate belonging and creative collaboration.\"\n\nQuestion: What is a primary individual benefit of remote work cited in the passage?",
        "sample_answer": "Elimination of commute time and improved work-life balance.",
        "tips": "Check paragraph 1 employee benefits.",
        "options": [
            {
                "label": "A",
                "text": "Mandatory overtime compensation",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Exemption from team deadlines",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Guaranteed company vehicles",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Time savings and improved work-life balance",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Remote Work and Corporate Culture",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The rapid expansion of remote work has fundamentally altered traditional workplace dynamics. For employees, the elimination of daily commutes translates into substantial time savings and improved work-life balance. For employers, geographical barriers are removed, allowing organizations to recruit top talent from an international candidate pool while reducing real estate costs. Nonetheless, sustaining organizational culture and team cohesion presents real hurdles in a distributed environment. Companies are increasingly adopting hybrid operational models, blending remote autonomy with structured in-person gatherings to cultivate belonging and creative collaboration.\"\n\nQuestion: How do companies benefit from hiring in a remote work model?",
        "sample_answer": "Access to a global talent pool and reduced office real estate costs.",
        "tips": "Look for employer advantages.",
        "options": [
            {
                "label": "A",
                "text": "Zero payroll tax liabilities",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Total freedom from labor regulations",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Elimination of IT infrastructure",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Access to international talent and lower real estate expenses",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Remote Work and Corporate Culture",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The rapid expansion of remote work has fundamentally altered traditional workplace dynamics. For employees, the elimination of daily commutes translates into substantial time savings and improved work-life balance. For employers, geographical barriers are removed, allowing organizations to recruit top talent from an international candidate pool while reducing real estate costs. Nonetheless, sustaining organizational culture and team cohesion presents real hurdles in a distributed environment. Companies are increasingly adopting hybrid operational models, blending remote autonomy with structured in-person gatherings to cultivate belonging and creative collaboration.\"\n\nQuestion: What is a notable challenge associated with fully distributed teams?",
        "sample_answer": "Maintaining organizational culture and interpersonal cohesion.",
        "tips": "Check hurdles mentioned.",
        "options": [
            {
                "label": "A",
                "text": "Slow home internet speeds worldwide",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Lack of computing devices",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Inability to send digital messages",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Sustaining corporate culture and team cohesion",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Remote Work and Corporate Culture",
        "difficulty": "Easy",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The rapid expansion of remote work has fundamentally altered traditional workplace dynamics. For employees, the elimination of daily commutes translates into substantial time savings and improved work-life balance. For employers, geographical barriers are removed, allowing organizations to recruit top talent from an international candidate pool while reducing real estate costs. Nonetheless, sustaining organizational culture and team cohesion presents real hurdles in a distributed environment. Companies are increasingly adopting hybrid operational models, blending remote autonomy with structured in-person gatherings to cultivate belonging and creative collaboration.\"\n\nQuestion: What operational solution are many enterprises embracing to balance these needs?",
        "sample_answer": "Hybrid models combining remote flexibility with periodic in-person interaction.",
        "tips": "See the concluding sentence.",
        "options": [
            {
                "label": "A",
                "text": "Permanent 7-day office mandates",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Complete outsourcing to third parties",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Total cessation of digital meetings",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Hybrid models combining remote autonomy with in-person sessions",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension - Remote Work and Corporate Culture",
        "difficulty": "Medium",
        "question_text": "Read the following passage carefully and answer the question:\n\n\"The rapid expansion of remote work has fundamentally altered traditional workplace dynamics. For employees, the elimination of daily commutes translates into substantial time savings and improved work-life balance. For employers, geographical barriers are removed, allowing organizations to recruit top talent from an international candidate pool while reducing real estate costs. Nonetheless, sustaining organizational culture and team cohesion presents real hurdles in a distributed environment. Companies are increasingly adopting hybrid operational models, blending remote autonomy with structured in-person gatherings to cultivate belonging and creative collaboration.\"\n\nQuestion: The phrase 'geographical barriers' refers to:",
        "sample_answer": "Obstacles imposed by distance and location.",
        "tips": "Contextual understanding.",
        "options": [
            {
                "label": "A",
                "text": "Mountain ranges separating internet cables",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Legal borders requiring physical passports",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Weather conditions halting trains",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Limitations imposed by physical distance and location",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Reading Comprehension').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Reading Comprehension').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Verbal Ability',
                    topic='Reading Comprehension',
                    title=q.get('title', 'Reading Comprehension'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Reading Comprehension via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Reading Comprehension: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Reading Comprehension',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Verbal Ability', 'Reading Comprehension',
                        q.get('title', 'Reading Comprehension'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Reading Comprehension into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
