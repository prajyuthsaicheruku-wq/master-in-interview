"""
Seed script for Fill in the Blanks (Verbal Ability)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Fill in the Blanks 1",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The sudden outbreak of the pandemic caused severe ______ to global supply chains.\"",
        "sample_answer": "Disruption means an interruption in the normal operation or activity of a process.",
        "tips": "Negative event causing interruption to supply chains.",
        "options": [
            {
                "label": "A",
                "text": "prosperity",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "disruption",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "stagnation",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "enhancement",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks 2",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Despite facing overwhelming odds, the young entrepreneur remained ______ and refused to surrender.\"",
        "sample_answer": "Tenacious means persistent, determined, and refusing to give up.",
        "tips": "Context indicates persistence despite hardship.",
        "options": [
            {
                "label": "A",
                "text": "tenacious",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "lethargic",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "indifferent",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "hesitant",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 3",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The new environmental policy aims to ______ greenhouse gas emissions by forty percent over the next decade.\"",
        "sample_answer": "Curb means to restrain, check, or reduce something undesirable.",
        "tips": "Policies aim to reduce emissions.",
        "options": [
            {
                "label": "A",
                "text": "elevate",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "proliferate",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "ignite",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "curb",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 4",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"His explanations were so ______ that even non-technical stakeholders easily understood the software architecture.\"",
        "sample_answer": "Lucid means clear and easy to understand.",
        "tips": "Contrasts with difficult technical jargon.",
        "options": [
            {
                "label": "A",
                "text": "obscure",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "lucid",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "convoluted",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "ambiguous",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks 5",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The committee found the proposed budget ______ and requested a comprehensive revision before approval.\"",
        "sample_answer": "Exorbitant means unreasonably high or excessive in cost.",
        "tips": "Reason for requesting revision.",
        "options": [
            {
                "label": "A",
                "text": "nominal",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "negligible",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "frugal",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "exorbitant",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 6",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"She was ______ by the overwhelming support and gratitude showered upon her by the local community.\"",
        "sample_answer": "Humbled in this context means feeling deeply touched, appreciative, and modest.",
        "tips": "Positive emotional response to community support.",
        "options": [
            {
                "label": "A",
                "text": "alienated",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "irritated",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "humiliated",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "humbled",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 7",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Due to the economic downturn, several companies had to ______ their non-essential expansion projects.\"",
        "sample_answer": "Defer means to postpone or put off to a later time.",
        "tips": "Cost-cutting measure in a downturn.",
        "options": [
            {
                "label": "A",
                "text": "accelerate",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "execute",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "defer",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "instigate",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 8",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The scientist's groundbreaking discovery was ______ by international peers at the annual conference.\"",
        "sample_answer": "Acclaimed means welcomed with enthusiastic praise and approval.",
        "tips": "Groundbreaking discoveries receive praise.",
        "options": [
            {
                "label": "A",
                "text": "rebuked",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "acclaimed",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "discounted",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "censured",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks 9",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"He has an ______ appetite for reading historical biographies and ancient literature.\"",
        "sample_answer": "Insatiable means impossible to satisfy; having an unquenchable desire.",
        "tips": "Describes an intense, unending passion for reading.",
        "options": [
            {
                "label": "A",
                "text": "indifferent",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "insatiable",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "apathetic",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "ephemeral",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks 10",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The government launched a public campaign to ______ awareness regarding water conservation.\"",
        "sample_answer": "Foster means to encourage, promote, or nurture the development of something.",
        "tips": "Campaigns seek to encourage awareness.",
        "options": [
            {
                "label": "A",
                "text": "dampen",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "stifle",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "foster",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "negate",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 11",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The manager was known for his ______ decision-making, never showing bias toward any particular team member.\"",
        "sample_answer": "Equitable means fair, just, and impartial.",
        "tips": "Absence of bias points to equity.",
        "options": [
            {
                "label": "A",
                "text": "prejudiced",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "erratic",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "equitable",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "partial",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 12",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Her ______ response during the crisis prevented panic among the building's occupants.\"",
        "sample_answer": "Composed means calm, serene, and in control of one's emotions.",
        "tips": "Calm response prevents panic.",
        "options": [
            {
                "label": "A",
                "text": "frantic",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "hysterical",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "reckless",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "composed",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 13",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Because the evidence presented by the prosecution was ______, the judge had no choice but to dismiss the charges.\"",
        "sample_answer": "Flimsy means weak, inadequate, or lacking substance.",
        "tips": "Weak evidence leads to case dismissal.",
        "options": [
            {
                "label": "A",
                "text": "flimsy",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "robust",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "indisputable",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "conclusive",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 14",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The CEO delivered a ______ speech outlining the company's five-year strategic vision.\"",
        "sample_answer": "Compelling means captivating, persuasive, and convincing.",
        "tips": "Positive characteristic of visionary speeches.",
        "options": [
            {
                "label": "A",
                "text": "compelling",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "tedious",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "monotonous",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "vacuous",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 15",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"In order to ______ the harsh pain of the injury, the doctor administered a mild analgesic.\"",
        "sample_answer": "Alleviate means to make suffering or pain less severe.",
        "tips": "Pain medication is given to reduce pain.",
        "options": [
            {
                "label": "A",
                "text": "aggravate",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "exacerbate",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "intensify",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "alleviate",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 16",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The antique vase was so ______ that museum curators handled it with utmost caution.\"",
        "sample_answer": "Fragile means delicate and easily broken.",
        "tips": "Need for utmost caution indicates fragility.",
        "options": [
            {
                "label": "A",
                "text": "fragile",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "sturdy",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "durable",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "resilient",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 17",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"He managed to ______ a potentially explosive argument between two colleagues with tact and humor.\"",
        "sample_answer": "Defuse means to make a dangerous or tense situation calmer.",
        "tips": "Tact and humor calm arguments.",
        "options": [
            {
                "label": "A",
                "text": "defuse",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "escalate",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "ignite",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "provoke",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 18",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Her meticulous attention to detail made her an ______ candidate for the quality auditing role.\"",
        "sample_answer": "Exemplary means serving as a desirable model; outstanding.",
        "tips": "Meticulous detail makes a person outstanding for auditing.",
        "options": [
            {
                "label": "A",
                "text": "exemplary",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "ordinary",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "ineligible",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "incompetent",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 19",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The project was halted temporarily due to a ______ of skilled electrical engineers in the region.\"",
        "sample_answer": "Scarcity means a state of being in short supply; shortage.",
        "tips": "Shortage causes projects to pause.",
        "options": [
            {
                "label": "A",
                "text": "scarcity",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "surplus",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "plethora",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "glut",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 20",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The diplomat spoke with great ______, carefully choosing words that would not offend either delegation.\"",
        "sample_answer": "Prudence means caution, wisdom, and good judgment in practical affairs.",
        "tips": "Diplomatic tact aligns with prudence.",
        "options": [
            {
                "label": "A",
                "text": "indiscretion",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "prudence",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "recklessness",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "audacity",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks 21",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The company's swift transition to cloud software proved ______ during unexpected lockdowns.\"",
        "sample_answer": "Fortuitous means happening by chance in a lucky or beneficial way.",
        "tips": "Happening luckily in hindsight.",
        "options": [
            {
                "label": "A",
                "text": "calamitous",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "detrimental",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "fortuitous",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "disastrous",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 22",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"His arguments were backed by ______ data collected over a three-year longitudinal study.\"",
        "sample_answer": "Empirical means based on observation, experiment, or practical experience.",
        "tips": "Real research data is empirical.",
        "options": [
            {
                "label": "A",
                "text": "hypothetical",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "empirical",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "speculative",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "mythical",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks 23",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The mentor offered ______ advice that guided the student throughout her academic career.\"",
        "sample_answer": "Invaluable means extremely useful; indispensable.",
        "tips": "Priceless guidance.",
        "options": [
            {
                "label": "A",
                "text": "dispensable",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "invaluable",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "trivial",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "worthless",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Fill in the Blanks 24",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"She felt ______ after spending two consecutive weeks working sixteen-hour shifts.\"",
        "sample_answer": "Exhausted means completely drained of physical or mental energy.",
        "tips": "Result of prolonged long hours.",
        "options": [
            {
                "label": "A",
                "text": "invigorated",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "refreshed",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "energized",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "exhausted",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 25",
        "difficulty": "Easy",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The treaty brought a ______ peace that allowed neighboring nations to rebuild trade ties.\"",
        "sample_answer": "Lasting means enduring over a long period.",
        "tips": "Enables rebuilding of trade ties.",
        "options": [
            {
                "label": "A",
                "text": "momentary",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "fleeting",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "lasting",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "transient",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 26",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"He gave a ______ summary of the three-hundred-page audit report in just ten minutes.\"",
        "sample_answer": "Concise means brief but comprehensive in expression.",
        "tips": "Short summary of a long report.",
        "options": [
            {
                "label": "A",
                "text": "rambling",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "redundant",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "verbose",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "concise",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 27",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The company adopted a ______ approach, testing new software prototypes on small focus groups first.\"",
        "sample_answer": "Cautious means careful to avoid potential problems or risks.",
        "tips": "Small testing first indicates care.",
        "options": [
            {
                "label": "A",
                "text": "cautious",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "precipitous",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "reckless",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "hasty",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 28",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Her remarkable resilience in recovering from the setback ______ everyone on the team.\"",
        "sample_answer": "Inspired means filled with the urge to do something positive.",
        "tips": "Resilience motivates others.",
        "options": [
            {
                "label": "A",
                "text": "demoralized",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "depressed",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "discouraged",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "inspired",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 29",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The software engineers worked tirelessly to ______ the critical bug before public launch.\"",
        "sample_answer": "Resolve means to settle, fix, or find a solution to a problem.",
        "tips": "Fixing a bug.",
        "options": [
            {
                "label": "A",
                "text": "compound",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "replicate",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "prolong",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "resolve",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 30",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Excessive sugar consumption is known to have ______ effects on metabolic health.\"",
        "sample_answer": "Adverse means harmful, unfavorable, or hostile.",
        "tips": "Harmful health consequence.",
        "options": [
            {
                "label": "A",
                "text": "adverse",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "salutary",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "beneficial",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "constructive",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 31",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The novel's plot was so ______ that readers could not guess the killer until the final chapter.\"",
        "sample_answer": "Intricate means very complicated or detailed.",
        "tips": "Unpredictable mystery plot.",
        "options": [
            {
                "label": "A",
                "text": "simplistic",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "predictable",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "obvious",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "intricate",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 32",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"A good leader must lead by ______, demonstrating integrity in every action.\"",
        "sample_answer": "Lead by example means inspiring others by one's own ethical conduct.",
        "tips": "Common leadership idiom.",
        "options": [
            {
                "label": "A",
                "text": "force",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "intimidation",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "decree",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "example",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 33",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The teacher commended the student for her ______ handwriting and immaculate notebooks.\"",
        "sample_answer": "Neat means cleanly arranged and tidy.",
        "tips": "Positive commendation for notebooks.",
        "options": [
            {
                "label": "A",
                "text": "neat",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "sloppy",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "untidy",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "shabby",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 34",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The board decided to ______ the annual meeting until the CEO recovered from illness.\"",
        "sample_answer": "Postpone means to delay or reschedule to a later date.",
        "tips": "Rescheduling due to illness.",
        "options": [
            {
                "label": "A",
                "text": "accelerate",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "conclude",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "postpone",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "cancel",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 35",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The new railway link provides a ______ connection between agricultural hubs and coastal ports.\"",
        "sample_answer": "Vital means absolutely necessary or essential.",
        "tips": "Essential economic connection.",
        "options": [
            {
                "label": "A",
                "text": "futile",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "pointless",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "trivial",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "vital",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 36",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Despite the intense interrogation, the suspect remained ______ and refused to confess.\"",
        "sample_answer": "Adamant means refusing to be persuaded or to change one's mind.",
        "tips": "Refusal to confess despite pressure.",
        "options": [
            {
                "label": "A",
                "text": "yielding",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "pliable",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "submissive",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "adamant",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 37",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The newly built solar farm will ______ thousands of homes with clean electricity.\"",
        "sample_answer": "Supply means to provide or make available.",
        "tips": "Providing homes with electricity.",
        "options": [
            {
                "label": "A",
                "text": "drain",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "deprive",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "supply",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "starve",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 38",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The team expressed ______ gratitude to the donors who funded their research lab.\"",
        "sample_answer": "Profound means deeply felt, significant, or intense.",
        "tips": "Deeply felt gratitude.",
        "options": [
            {
                "label": "A",
                "text": "insincere",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "superficial",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "feigned",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "profound",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 39",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The instructions in the manual were straightforward and ______ for beginners to assemble.\"",
        "sample_answer": "Simple means easily understood or done.",
        "tips": "Accessible for beginners.",
        "options": [
            {
                "label": "A",
                "text": "cumbersome",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "perplexing",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "simple",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "baffling",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 40",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Regular physical exercise is known to ______ mental focus and mood throughout the workday.\"",
        "sample_answer": "Boost means to help or encourage to increase or improve.",
        "tips": "Positive health impact.",
        "options": [
            {
                "label": "A",
                "text": "stifle",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "diminish",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "boost",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "deplete",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 41",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The candidate's resume was ______ with relevant internship experiences and coding awards.\"",
        "sample_answer": "Replete means filled or well-supplied with something.",
        "tips": "Full of good achievements.",
        "options": [
            {
                "label": "A",
                "text": "replete",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "devoid",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "bereft",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "lacking",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 42",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"She tackled the complex algorithm with ______ determination and solved it in an hour.\"",
        "sample_answer": "Unwavering means steady, firm, and not shaking.",
        "tips": "Firm determination.",
        "options": [
            {
                "label": "A",
                "text": "fickle",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "vacillating",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "unwavering",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "hesitant",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 43",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The unexpected rainstorm caused ______ delays for evening commuters at the metro station.\"",
        "sample_answer": "Significant means sufficiently great or important to be worthy of attention.",
        "tips": "Noticeable commuter delays.",
        "options": [
            {
                "label": "A",
                "text": "inconsequential",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "trifling",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "significant",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "negligible",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 44",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The architect created a design that seamlessly ______ modern glass with historic brickwork.\"",
        "sample_answer": "Blends means harmoniously combines different elements.",
        "tips": "Harmonious architectural fusion.",
        "options": [
            {
                "label": "A",
                "text": "separates",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "clashes",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "detaches",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "blends",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 45",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"Her ______ demeanor made all newcomers feel welcomed and comfortable immediately.\"",
        "sample_answer": "Genial means friendly, cheerful, and affable.",
        "tips": "Friendly welcoming attitude.",
        "options": [
            {
                "label": "A",
                "text": "antagonistic",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "aloof",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "genial",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "hostile",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 46",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The research team published their ______ findings in an internationally peer-reviewed journal.\"",
        "sample_answer": "Seminal means strongly influencing later developments; groundbreaking.",
        "tips": "Pioneering research papers.",
        "options": [
            {
                "label": "A",
                "text": "spurious",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "flawed",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "seminal",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "derivative",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 47",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"He was ______ for his outstanding bravery during the rescue operation.\"",
        "sample_answer": "Commended means formally praised or lauded.",
        "tips": "Praise for bravery.",
        "options": [
            {
                "label": "A",
                "text": "commended",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "admonished",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "penalized",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "reprimanded",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Fill in the Blanks 48",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"A balanced diet and adequate hydration are ______ for sustaining high energy levels.\"",
        "sample_answer": "Indispensable means absolutely necessary; essential.",
        "tips": "Must-haves for high energy.",
        "options": [
            {
                "label": "A",
                "text": "redundant",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "superfluous",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "unnecessary",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "indispensable",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Fill in the Blanks 49",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"The new safety policy was ______ across all regional production facilities starting today.\"",
        "sample_answer": "Implemented means put into practical effect or execution.",
        "tips": "Enacting a policy.",
        "options": [
            {
                "label": "A",
                "text": "vetoed",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "repealed",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "implemented",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "abandoned",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Fill in the Blanks 50",
        "difficulty": "Medium",
        "question_text": "Select the most appropriate word to fill in the blank:\n\n\"His ______ nature made him popular among peers who valued honest and direct feedback.\"",
        "sample_answer": "Candid means truthful, straightforward, and sincere.",
        "tips": "Honest and direct.",
        "options": [
            {
                "label": "A",
                "text": "deceitful",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "evasive",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "guileful",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "candid",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Fill in the Blanks').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Fill in the Blanks').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Verbal Ability',
                    topic='Fill in the Blanks',
                    title=q.get('title', 'Fill in the Blanks'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Fill in the Blanks via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Fill in the Blanks: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Fill in the Blanks',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Verbal Ability', 'Fill in the Blanks',
                        q.get('title', 'Fill in the Blanks'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Fill in the Blanks into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
