"""
Seed script for Sentence Correction (Verbal Ability)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Sentence Correction 1",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The committee have reached an unanimous decision on the matter.\"",
        "sample_answer": "'Committee' acting as a unified unit is singular ('has reached'), and 'unanimous' begins with a consonant sound /ju\u02d0/, requiring 'a' not 'an'.",
        "tips": "Collective noun unity + article before consonant sound.",
        "options": [
            {
                "label": "A",
                "text": "The committee have reached a unanimous decision on the matter.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "The committee has reached a unanimous decision on the matter.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "The committee has reached an unanimous decision on the matter.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The committee are reaching an unanimous decision on the matter.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 2",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"She does not know how to swim, isn't it?\"",
        "sample_answer": "A negative statement with auxiliary 'does' takes a positive question tag: 'does she?'.",
        "tips": "Negative statement requires a positive question tag.",
        "options": [
            {
                "label": "A",
                "text": "She does not know how to swim, is it?",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "She does not know how to swim, does she?",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "She does not know how to swim, doesn't she?",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "She does not know how to swim, hasn't she?",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 3",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He is more superior than any other player in the team.\"",
        "sample_answer": "Adjectives like superior, inferior, senior, junior take 'to', not 'than', and cannot take 'more'.",
        "tips": "Superior takes 'to', never 'than' or 'more'.",
        "options": [
            {
                "label": "A",
                "text": "He is more superior to any other player in the team.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He is superior to any other player in the team.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "He is very superior than any other player in the team.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He is superior than any other player in the team.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 4",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Unless you do not work hard, you will not clear the examination.\"",
        "sample_answer": "'Unless' already conveys a negative condition ('if not'); using 'do not' creates a double negative.",
        "tips": "Avoid double negative after 'unless'.",
        "options": [
            {
                "label": "A",
                "text": "Until you do not work hard, you will not clear the examination.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Unless you cannot work hard, you will not clear the examination.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Unless you work hard, you will not clear the examination.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Unless you did not work hard, you will not clear the examination.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 5",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He insisted to pay for the dinner at the restaurant.\"",
        "sample_answer": "The verb 'insist' is followed by the preposition 'on' and a gerund ('on paying').",
        "tips": "Insist + on + verb-ing.",
        "options": [
            {
                "label": "A",
                "text": "He insisted for paying for the dinner at the restaurant.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He insisted in paying for the dinner at the restaurant.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He insisted on paying for the dinner at the restaurant.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "He insisted to paying for the dinner at the restaurant.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 6",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The climate of Shimla is cooler than Delhi.\"",
        "sample_answer": "In logical comparisons, compare climate with climate ('that of Delhi'), not climate with the city Delhi itself.",
        "tips": "Ensure parallel comparison with 'that of'.",
        "options": [
            {
                "label": "A",
                "text": "The climate of Shimla is more cooler than Delhi.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "The climate of Shimla is cooler than that of Delhi.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "The climate of Shimla is cooler than Delhi's climate are.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The climate of Shimla is cooler compared to Delhi.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 7",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Being a rainy day, I decided to stay indoors.\"",
        "sample_answer": "'Being a rainy day' creates an unattached dangling participle making 'I' seem like the rainy day. Provide an overt subject: 'As it was a rainy day' or 'It being a rainy day'.",
        "tips": "Watch out for dangling participles.",
        "options": [
            {
                "label": "A",
                "text": "Having been a rainy day, I decided to stay indoors.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Being that it was a rainy day, I decided to stay indoors.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "As it was a rainy day, I decided to stay indoors.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "It being that a rainy day, I decided to stay indoors.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 8",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Scarcely had I entered the station than the train departed.\"",
        "sample_answer": "'Scarcely' pairs with the correlative conjunction 'when', not 'than'.",
        "tips": "Scarcely... when correlative pair.",
        "options": [
            {
                "label": "A",
                "text": "Scarcely had I entered the station then the train departed.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Scarcely did I entered the station when the train departed.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Scarcely had I entered the station after the train departed.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Scarcely had I entered the station when the train departed.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 9",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He told to me that he would visit tomorrow.\"",
        "sample_answer": "'Told' takes a direct personal object without 'to', and 'tomorrow' shifts to 'the next day' in indirect speech.",
        "tips": "Tell takes a direct object without preposition 'to'.",
        "options": [
            {
                "label": "A",
                "text": "He told me that he will visit the next day.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He told me that he would visit the next day.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "He said me that he would visit tomorrow.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He told to me that he would visit the following day.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 10",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"I prefer coffee more than tea in the morning.\"",
        "sample_answer": "The verb 'prefer' takes the preposition 'to', not 'more than'.",
        "tips": "Prefer X to Y.",
        "options": [
            {
                "label": "A",
                "text": "I prefer coffee rather than tea in the morning.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "I prefer coffee more to tea in the morning.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "I prefer coffee to tea in the morning.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "I prefer coffee over than tea in the morning.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 11",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"If he had invited me, I would attend the wedding.\"",
        "sample_answer": "Third Conditional: 'If + past perfect' requires 'would have + past participle' in the main clause.",
        "tips": "Third conditional: If + had + V3, would have + V3.",
        "options": [
            {
                "label": "A",
                "text": "If he invited me, I would have attended the wedding.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "If he had invited me, I would attended the wedding.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "If he had invited me, I will attend the wedding.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "If he had invited me, I would have attended the wedding.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 12",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"She is looking forward to meet her old classmates.\"",
        "sample_answer": "In the phrase 'look forward to', 'to' is a preposition and must be followed by a gerund (-ing form).",
        "tips": "Look forward to + gerund (-ing).",
        "options": [
            {
                "label": "A",
                "text": "She is looking forward to meeting her old classmates.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "She looks forward to meet her old classmates.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "She is looking forward to have met her old classmates.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "She is looking forward for meeting her old classmates.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 13",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The manager asked Rahul that why he was late to office.\"",
        "sample_answer": "Do not use 'that' before an interrogative wh-word ('why') in indirect questions.",
        "tips": "Omit 'that' before wh-question words in reported speech.",
        "options": [
            {
                "label": "A",
                "text": "The manager asked Rahul why he was late to office.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "The manager asked to Rahul why he was late to office.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "The manager asked Rahul that why was he late to office.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The manager asked Rahul why was he late to office.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 14",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He ran as fastly as he could to catch the departing bus.\"",
        "sample_answer": "'Fast' functions as both an adjective and an adverb; 'fastly' does not exist in standard English.",
        "tips": "'Fast' is both adjective and adverb; 'fastly' is incorrect.",
        "options": [
            {
                "label": "A",
                "text": "He ran so fastly that he could catch the bus.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He ran as faster as he could to catch the departing bus.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He ran more fastly as he could to catch the departing bus.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He ran as fast as he could to catch the departing bus.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 15",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"No sooner had the teacher entered the classroom when the students stood up.\"",
        "sample_answer": "'No sooner' is always paired with 'than', never with 'when' or 'then'.",
        "tips": "No sooner... than correlative pair.",
        "options": [
            {
                "label": "A",
                "text": "No sooner had the teacher entered the classroom then the students stood up.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "No sooner did the teacher entered the classroom than the students stood up.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "No sooner had the teacher entered the classroom after the students stood up.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "No sooner had the teacher entered the classroom than the students stood up.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 16",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"All the furnitures in the office were replaced with ergonomic chairs.\"",
        "sample_answer": "'Furniture' is an uncountable noun with no plural 'furnitures', and takes a singular verb 'was'.",
        "tips": "Furniture is uncountable; takes singular verb.",
        "options": [
            {
                "label": "A",
                "text": "All furniture in the office were replaced with ergonomic chairs.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "All the furniture in the office was replaced with ergonomic chairs.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "All the pieces of furnitures in the office were replaced.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "All the furnitures in the office was replaced with ergonomic chairs.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 17",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Despite of the heavy traffic, we reached the airport on time.\"",
        "sample_answer": "'Despite' is used without 'of'. 'In spite of' uses 'of', but 'despite' does not.",
        "tips": "Despite takes no preposition (do not write 'despite of').",
        "options": [
            {
                "label": "A",
                "text": "In despite of the heavy traffic, we reached the airport on time.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Despite for the heavy traffic, we reached the airport on time.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Despite with the heavy traffic, we reached the airport on time.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Despite the heavy traffic, we reached the airport on time.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 18",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He is addicted of playing online video games late at night.\"",
        "sample_answer": "The correct preposition after 'addicted' is 'to' followed by a gerund.",
        "tips": "Addicted + to + gerund.",
        "options": [
            {
                "label": "A",
                "text": "He is addicted to playing online video games late at night.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "He is addicted with playing online video games late at night.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He is addicted about playing online video games late at night.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He is addicted for playing online video games late at night.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 19",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The train had left before I have reached the platform.\"",
        "sample_answer": "In past sequence of events, the earlier event uses past perfect ('had left') and the later event uses simple past ('reached').",
        "tips": "Combine past perfect with simple past.",
        "options": [
            {
                "label": "A",
                "text": "The train has left before I reached the platform.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "The train had left before I reached the platform.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "The train had left before I had reached the platform.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The train left before I have reached the platform.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 20",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"She has been studying since three hours without taking a break.\"",
        "sample_answer": "'For' is used for a duration or period of time ('three hours'), whereas 'since' marks a starting point.",
        "tips": "Use 'for' for duration and 'since' for starting point.",
        "options": [
            {
                "label": "A",
                "text": "She has been studying for three hours without taking a break.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "She has been studying from three hours without taking a break.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "She is studying since three hours without taking a break.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "She was studying for three hours without taking a break.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 21",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Neither John or his cousins have arrived for the ceremony.\"",
        "sample_answer": "'Neither' is paired with 'nor', and the verb agrees with plural 'cousins'.",
        "tips": "Neither pairs with nor.",
        "options": [
            {
                "label": "A",
                "text": "Neither John and his cousins have arrived for the ceremony.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Neither John nor his cousins have arrived for the ceremony.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Neither John nor his cousins has arrived for the ceremony.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Neither John or his cousins has arrived for the ceremony.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 22",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He gave me many advices regarding career planning.\"",
        "sample_answer": "'Advice' is an uncountable noun. Use 'much advice' or 'pieces of advice', never 'advices'.",
        "tips": "Advice is uncountable.",
        "options": [
            {
                "label": "A",
                "text": "He gave me several advices regarding career planning.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He gave me many advice regarding career planning.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He gave me a lots of advices regarding career planning.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He gave me much advice regarding career planning.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 23",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Supposing if it rains, what will we do about the outdoor barbecue?\"",
        "sample_answer": "'Supposing' and 'if' mean the same thing; using both together is redundant.",
        "tips": "Do not combine 'supposing' and 'if'.",
        "options": [
            {
                "label": "A",
                "text": "Supposing that if it rains, what will we do about the outdoor barbecue?",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Supposing whether it rains, what will we do about the outdoor barbecue?",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Supposing if that it rains, what will we do about the outdoor barbecue?",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "If it rains, what will we do about the outdoor barbecue?",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 24",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Hardly he had finished his dinner when someone knocked on the door.\"",
        "sample_answer": "When negative/restrictive adverbs like 'Hardly' begin a sentence, inversion of auxiliary verb and subject is required: 'Hardly had he...'",
        "tips": "Negative adverb at the start requires subject-verb inversion.",
        "options": [
            {
                "label": "A",
                "text": "Hardly had he finished his dinner when someone knocked on the door.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Hardly did he finished his dinner when someone knocked on the door.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Hardly he finished his dinner when someone knocked on the door.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Hardly had he finish his dinner when someone knocked on the door.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 25",
        "difficulty": "Easy",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"She is one of the brightest girls who has passed the entrance exam.\"",
        "sample_answer": "The relative pronoun 'who' refers to the plural antecedent 'girls', so the relative clause requires a plural verb 'have passed'.",
        "tips": "Relative clause agrees with the plural antecedent 'girls'.",
        "options": [
            {
                "label": "A",
                "text": "She is one of the brightest girl who has passed the entrance exam.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "She is one of the brightest girls who had passed the entrance exam.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "She is one of the brighter girls who has passed the entrance exam.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "She is one of the brightest girls who have passed the entrance exam.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 26",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"I would rather to study coding than watching television.\"",
        "sample_answer": "'Would rather' is followed by the bare infinitive ('study') and maintains parallel structure with 'than watch'.",
        "tips": "Would rather + bare infinitive... than + bare infinitive.",
        "options": [
            {
                "label": "A",
                "text": "I would rather study coding than watch television.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "I would rather study coding then watch television.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "I would rather to study coding than to watch television.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "I would rather studying coding than watching television.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 27",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The news are too good to be true.\"",
        "sample_answer": "'News' looks plural but is singular in meaning and takes a singular verb.",
        "tips": "News is an uncountable singular noun.",
        "options": [
            {
                "label": "A",
                "text": "The news were too good to be true.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "The news is too good to be true.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "The news have been too good to be true.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The news are being too good to be true.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 28",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He is confident to win the badminton tournament this year.\"",
        "sample_answer": "'Confident' is followed by the preposition 'of' and a gerund ('of winning').",
        "tips": "Confident + of + gerund.",
        "options": [
            {
                "label": "A",
                "text": "He is confident for winning the badminton tournament this year.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He is confident about to win the badminton tournament this year.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He is confident of winning the badminton tournament this year.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "He is confident in winning the badminton tournament this year.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 29",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"One should keep his promises if he wants respect.\"",
        "sample_answer": "The indefinite pronoun 'one' must be maintained consistently with 'one's' and 'one'.",
        "tips": "Maintain consistency with 'one' -> 'one's'.",
        "options": [
            {
                "label": "A",
                "text": "One should keep one's promises if one wants respect.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "One should keep her promises if one wants respect.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "One should keep his promises if one wants respect.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "One should keep their promises if they want respect.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 30",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He did not wrote the test yesterday because he was sick.\"",
        "sample_answer": "Auxiliary 'did not' must always be followed by the base form of the verb ('write').",
        "tips": "Did + base form of verb.",
        "options": [
            {
                "label": "A",
                "text": "He did not writing the test yesterday because he was sick.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He did not write the test yesterday because he was sick.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "He had not wrote the test yesterday because he was sick.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He did not written the test yesterday because he was sick.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 31",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Although he worked hard, but he failed to secure the top rank.\"",
        "sample_answer": "Do not use coordinating conjunction 'but' after subordinating conjunction 'although'.",
        "tips": "Do not pair 'although' with 'but'.",
        "options": [
            {
                "label": "A",
                "text": "Although he worked hard, so he failed to secure the top rank.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Although he worked hard, yet but he failed to secure the top rank.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Although he worked hard, he failed to secure the top rank.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "Though he worked hard, but he failed to secure the top rank.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 32",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The scissors is kept on the top drawer of the desk.\"",
        "sample_answer": "'Scissors' is a plural noun taking a plural verb 'are', and items inside a drawer are 'in' the drawer.",
        "tips": "Scissors is plural; use 'are'.",
        "options": [
            {
                "label": "A",
                "text": "The scissors are kept in the top drawer of the desk.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "The pair of scissor is kept on the top drawer of the desk.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "The scissors is kept in the top drawer of the desk.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The scissor are kept on the top drawer of the desk.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 33",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"My brother-in-laws have arrived from London for the reunion.\"",
        "sample_answer": "Compound nouns pluralize the primary noun element ('brothers', not 'laws').",
        "tips": "Plural of brother-in-law is brothers-in-law.",
        "options": [
            {
                "label": "A",
                "text": "My brother-in-law has arrived from London for the reunion.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "My brothers-in-laws have arrived from London for the reunion.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "My brothers-in-law have arrived from London for the reunion.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "My brother-ins-law have arrived from London for the reunion.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 34",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"She has visited five different countries since she has graduated.\"",
        "sample_answer": "When 'since' introduces a specific starting event in time, the clause uses simple past ('graduated').",
        "tips": "Since-clause takes simple past.",
        "options": [
            {
                "label": "A",
                "text": "She visited five different countries since she has graduated.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "She has visited five different countries since she had graduated.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "She is visiting five different countries since she graduated.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "She has visited five different countries since she graduated.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 35",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He is very senior than me in this organization.\"",
        "sample_answer": "'Senior' takes 'to' rather than 'than', and degree is modified by 'much' or simply 'senior to me'.",
        "tips": "Senior + to.",
        "options": [
            {
                "label": "A",
                "text": "He is more senior to me in this organization.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He is very senior to me in this organization.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He is much senior to me in this organization.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "He is senior than me in this organization.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 36",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The boy was punished for creating a ruckus in the class, wasn't he?\"",
        "sample_answer": "The sentence uses 'was' in a positive statement, so the correct tag is 'wasn't he?'. The original sentence is already correct.",
        "tips": "Tag matches auxiliary 'was'.",
        "options": [
            {
                "label": "A",
                "text": "The boy was punished for creating a ruckus in the class, hasn't he?",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "The boy was punished for creating a ruckus in the class, isn't he?",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "The boy was punished for creating a ruckus in the class, didn't he?",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The boy was punished for creating a ruckus in the class, wasn't he?",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 37",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Neither of the two candidates have sufficient experience for the role.\"",
        "sample_answer": "'Neither of + plural noun' takes a singular verb 'has'.",
        "tips": "Neither of takes a singular verb.",
        "options": [
            {
                "label": "A",
                "text": "Neither of both candidates has sufficient experience for the role.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Neither of the two candidates has sufficient experience for the role.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "Neither of the two candidate have sufficient experience for the role.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Neither of the two candidates are having sufficient experience for the role.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 38",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"I am having three laptops at home for work and study.\"",
        "sample_answer": "Verbs expressing possession ('have', 'own') are stative and cannot be used in continuous tenses.",
        "tips": "Stative verbs of possession cannot be used in continuous tenses.",
        "options": [
            {
                "label": "A",
                "text": "I have had three laptops at home for work and study.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "I have three laptops at home for work and study.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "I am owning three laptops at home for work and study.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "I had having three laptops at home for work and study.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 39",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He walked five miles on foot everyday to keep himself fit.\"",
        "sample_answer": "The verb 'walked' already implies moving on foot; adding 'on foot' is redundant.",
        "tips": "Avoid redundant 'on foot' with walked.",
        "options": [
            {
                "label": "A",
                "text": "He walked on his feet five miles everyday to keep himself fit.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He walked five miles everyday to keep himself fit.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "He walked five miles with foot everyday to keep himself fit.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He walked five miles by foot everyday to keep himself fit.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 40",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"If I was the Prime Minister, I would prioritize public healthcare.\"",
        "sample_answer": "In an unreal conditional or subjunctive mood, use 'were' for all persons.",
        "tips": "Subjunctive mood requires 'were'.",
        "options": [
            {
                "label": "A",
                "text": "If I would be the Prime Minister, I would prioritize public healthcare.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "If I had been the Prime Minister, I will prioritize public healthcare.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "If I am the Prime Minister, I would prioritize public healthcare.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "If I were the Prime Minister, I would prioritize public healthcare.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 41",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The reason why he failed the test is because he did not revise.\"",
        "sample_answer": "'The reason is' must be followed by 'that', not 'because' (which creates redundancy).",
        "tips": "'The reason is' pairs with 'that'.",
        "options": [
            {
                "label": "A",
                "text": "The reason why he failed the test is that he did not revise.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "The reason why he failed the test is due to he did not revise.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "The reason because he failed the test is that he did not revise.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The reason why he failed the test was because he did not revise.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 42",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Each boy and each girl were presented with a medal of honor.\"",
        "sample_answer": "Subjects preceded by 'each' or 'every' take a singular verb 'was'.",
        "tips": "Each... and each... takes singular verb.",
        "options": [
            {
                "label": "A",
                "text": "Each boy and each girl was presented with a medal of honor.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Each boys and each girls were presented with a medal of honor.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Each boy and each girl have been presented with a medal of honor.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Every boy and every girl were presented with a medal of honor.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 43",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He is one of those employees who always performs exceptionally well.\"",
        "sample_answer": "'Who' refers to plural antecedent 'employees', so the verb must be plural 'perform'.",
        "tips": "Agreement with plural antecedent 'employees'.",
        "options": [
            {
                "label": "A",
                "text": "He is one of those employee who always perform exceptionally well.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He is one of those employees who is always performing exceptionally well.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "He is one of those employees who always perform exceptionally well.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "He is one of that employees who always perform exceptionally well.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 44",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Between you and I, the decision made by the board was biased.\"",
        "sample_answer": "Prepositions govern objective pronouns ('me', not 'I').",
        "tips": "Between you and me.",
        "options": [
            {
                "label": "A",
                "text": "Between you with me, the decision made by the board was biased.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "Between you and myself, the decision made by the board was biased.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Among you and I, the decision made by the board was biased.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Between you and me, the decision made by the board was biased.",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Sentence Correction 45",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"The teacher asked the student to explain why was he late.\"",
        "sample_answer": "Indirect embedded clauses must use subject-verb declarative word order ('why he was late').",
        "tips": "Declarative word order in indirect clauses.",
        "options": [
            {
                "label": "A",
                "text": "The teacher asked to the student to explain why he was late.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "The teacher asked the student to explain why he was late.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "The teacher asked the student to explain that why was he late.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "The teacher asked the student to explain that why he was late.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 46",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"She has received a letter from her father yesterday.\"",
        "sample_answer": "Definite past time markers like 'yesterday' require the Simple Past tense, not the Present Perfect.",
        "tips": "Past time adverbial requires simple past.",
        "options": [
            {
                "label": "A",
                "text": "She had received a letter from her father yesterday.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "She was received a letter from her father yesterday.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "She received a letter from her father yesterday.",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "She has been receiving a letter from her father yesterday.",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Sentence Correction 47",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"Not only the students but also the instructor were present at the seminar.\"",
        "sample_answer": "With 'not only... but also', the verb agrees with the closer subject ('instructor' is singular).",
        "tips": "Verb agrees with the nearer subject.",
        "options": [
            {
                "label": "A",
                "text": "Not only the students but also the instructor was present at the seminar.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "Not only the students but also the instructor have been present at the seminar.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "Not only the students but also the instructor are present at the seminar.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "Not only the student but also the instructor were present at the seminar.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 48",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"He works hardly to support his family in times of crisis.\"",
        "sample_answer": "'Hardly' means barely or scarcely, whereas 'hard' is the adverb meaning with great effort.",
        "tips": "Hard = with effort; hardly = scarcely.",
        "options": [
            {
                "label": "A",
                "text": "He is working hardly to support his family in times of crisis.",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "He works hard to support his family in times of crisis.",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "He works more hardly to support his family in times of crisis.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "He works with hardly to support his family in times of crisis.",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Sentence Correction 49",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"None of the information provided by the witness were accurate.\"",
        "sample_answer": "'Information' is an uncountable singular noun, so 'none of the information' takes a singular verb 'was'.",
        "tips": "Information is uncountable singular.",
        "options": [
            {
                "label": "A",
                "text": "None of the information provided by the witness was accurate.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "None of the informations provided by the witness was accurate.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "None of the information provided by the witness are accurate.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "None of the informations provided by the witness were accurate.",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Sentence Correction 50",
        "difficulty": "Medium",
        "question_text": "Select the most grammatically correct replacement for the underlined or erroneous sentence:\n\nOriginal: \"They discussed about the new project proposal in detail.\"",
        "sample_answer": "The transitive verb 'discuss' directly takes an object without the preposition 'about'.",
        "tips": "Discuss takes a direct object (omit 'about').",
        "options": [
            {
                "label": "A",
                "text": "They discussed the new project proposal in detail.",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "They discussed regarding the new project proposal in detail.",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "They discussed on the new project proposal in detail.",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "They discussed over the new project proposal in detail.",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Sentence Correction').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Sentence Correction').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Verbal Ability',
                    topic='Sentence Correction',
                    title=q.get('title', 'Sentence Correction'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Sentence Correction via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Sentence Correction: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Sentence Correction',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Verbal Ability', 'Sentence Correction',
                        q.get('title', 'Sentence Correction'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Sentence Correction into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
