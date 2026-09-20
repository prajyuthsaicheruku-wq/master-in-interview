"""
Seed script for Profit & Loss (Commercial Mathematics)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Profit & Loss - Selling Price with Gain 1",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b94,800 and sells it at a profit of 15%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b94,800.\nProfit = 15% of \u20b94,800 = \u20b9720.\nSelling Price (SP) = CP + Profit = \u20b95,520.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b96,020",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b95,520",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b95,320",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b95,720",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 2",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,600 and sells it at a profit of 10%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,600.\nProfit = 10% of \u20b92,600 = \u20b9260.\nSelling Price (SP) = CP + Profit = \u20b92,860.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,060",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,360",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,860",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b92,660",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 3",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b91,400 and sells it at a profit of 10%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b91,400.\nProfit = 10% of \u20b91,400 = \u20b9140.\nSelling Price (SP) = CP + Profit = \u20b91,540.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,540",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b91,740",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,340",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,040",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 4",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b94,700 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b94,700.\nProfit = 25% of \u20b94,700 = \u20b91,175.\nSelling Price (SP) = CP + Profit = \u20b95,875.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b96,375",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b95,875",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b95,675",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b96,075",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 5",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,300 and sells it at a profit of 30%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,300.\nProfit = 30% of \u20b92,300 = \u20b9690.\nSelling Price (SP) = CP + Profit = \u20b92,990.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,990",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,490",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,190",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,790",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 6",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,600 and sells it at a profit of 30%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,600.\nProfit = 30% of \u20b92,600 = \u20b9780.\nSelling Price (SP) = CP + Profit = \u20b93,380.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,880",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,180",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,580",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,380",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 7",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b95,000 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b95,000.\nProfit = 25% of \u20b95,000 = \u20b91,250.\nSelling Price (SP) = CP + Profit = \u20b96,250.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b96,450",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b96,250",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b96,750",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b96,050",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 8",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b93,500 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b93,500.\nProfit = 25% of \u20b93,500 = \u20b9875.\nSelling Price (SP) = CP + Profit = \u20b94,375.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,575",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,375",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b94,875",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,175",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 9",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,000 and sells it at a profit of 30%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,000.\nProfit = 30% of \u20b92,000 = \u20b9600.\nSelling Price (SP) = CP + Profit = \u20b92,600.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,800",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,100",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,600",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b92,400",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 10",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b94,300 and sells it at a profit of 10%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b94,300.\nProfit = 10% of \u20b94,300 = \u20b9430.\nSelling Price (SP) = CP + Profit = \u20b94,730.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,930",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,730",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b95,230",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,530",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 11",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,400 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,400.\nProfit = 25% of \u20b92,400 = \u20b9600.\nSelling Price (SP) = CP + Profit = \u20b93,000.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,800",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,200",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,000",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b93,500",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 12",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,600 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,600.\nProfit = 25% of \u20b92,600 = \u20b9650.\nSelling Price (SP) = CP + Profit = \u20b93,250.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,250",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,450",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,050",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,750",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 13",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b91,900 and sells it at a profit of 20%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b91,900.\nProfit = 20% of \u20b91,900 = \u20b9380.\nSelling Price (SP) = CP + Profit = \u20b92,280.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,080",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,780",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,480",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,280",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 14",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,700 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,700.\nProfit = 25% of \u20b92,700 = \u20b9675.\nSelling Price (SP) = CP + Profit = \u20b93,375.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,875",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,175",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,375",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b93,575",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 15",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b93,100 and sells it at a profit of 15%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b93,100.\nProfit = 15% of \u20b93,100 = \u20b9464.\nSelling Price (SP) = CP + Profit = \u20b93,564.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,564",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b94,064",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,764",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,364",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 16",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b93,100 and sells it at a profit of 15%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b93,100.\nProfit = 15% of \u20b93,100 = \u20b9464.\nSelling Price (SP) = CP + Profit = \u20b93,564.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,364",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,764",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,564",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b94,064",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 17",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b92,200 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b92,200.\nProfit = 25% of \u20b92,200 = \u20b9550.\nSelling Price (SP) = CP + Profit = \u20b92,750.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,550",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,750",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b93,250",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,950",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 18",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b93,700 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b93,700.\nProfit = 25% of \u20b93,700 = \u20b9925.\nSelling Price (SP) = CP + Profit = \u20b94,625.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,425",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,625",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b94,825",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b95,125",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 19",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b94,600 and sells it at a profit of 30%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b94,600.\nProfit = 30% of \u20b94,600 = \u20b91,380.\nSelling Price (SP) = CP + Profit = \u20b95,980.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b95,780",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b96,480",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b96,180",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b95,980",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Selling Price with Gain 20",
        "difficulty": "Easy",
        "question_text": "A shopkeeper purchases an item for \u20b91,100 and sells it at a profit of 25%. What is the selling price?",
        "sample_answer": "Cost Price (CP) = \u20b91,100.\nProfit = 25% of \u20b91,100 = \u20b9275.\nSelling Price (SP) = CP + Profit = \u20b91,375.",
        "tips": "SP = CP * (1 + Gain%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,175",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,375",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b91,575",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,875",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Find Cost Price 21",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,840 at a loss of 20%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,840 = CP \u00d7 80 / 100\nCP = \u20b91,840 \u00d7 100 / 80 = \u20b92,300.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,100",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,700",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,500",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,300",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Find Cost Price 22",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b92,610 at a loss of 10%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b92,610 = CP \u00d7 90 / 100\nCP = \u20b92,610 \u00d7 100 / 90 = \u20b92,900.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,300",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,700",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,900",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b93,100",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Find Cost Price 23",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,440 at a loss of 10%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,440 = CP \u00d7 90 / 100\nCP = \u20b91,440 \u00d7 100 / 90 = \u20b91,600.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,800",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,000",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,400",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,600",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Find Cost Price 24",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b92,520 at a loss of 10%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b92,520 = CP \u00d7 90 / 100\nCP = \u20b92,520 \u00d7 100 / 90 = \u20b92,800.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,600",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,000",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,800",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b93,200",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Find Cost Price 25",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,260 at a loss of 10%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,260 = CP \u00d7 90 / 100\nCP = \u20b91,260 \u00d7 100 / 90 = \u20b91,400.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,200",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,600",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,800",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,400",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Find Cost Price 26",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b9990 at a loss of 10%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b9990 = CP \u00d7 90 / 100\nCP = \u20b9990 \u00d7 100 / 90 = \u20b91,100.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b9900",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,100",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b91,500",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,300",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Find Cost Price 27",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,875 at a loss of 25%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,875 = CP \u00d7 75 / 100\nCP = \u20b91,875 \u00d7 100 / 75 = \u20b92,500.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,300",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,700",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,500",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b92,900",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Find Cost Price 28",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b9825 at a loss of 25%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b9825 = CP \u00d7 75 / 100\nCP = \u20b9825 \u00d7 100 / 75 = \u20b91,100.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b9900",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,100",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b91,500",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,300",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Find Cost Price 29",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b92,700 at a loss of 10%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b92,700 = CP \u00d7 90 / 100\nCP = \u20b92,700 \u00d7 100 / 90 = \u20b93,000.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,000",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,400",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,800",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,200",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - Find Cost Price 30",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,440 at a loss of 20%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,440 = CP \u00d7 80 / 100\nCP = \u20b91,440 \u00d7 100 / 80 = \u20b91,800.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,000",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,200",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,600",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,800",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Find Cost Price 31",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,520 at a loss of 20%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,520 = CP \u00d7 80 / 100\nCP = \u20b91,520 \u00d7 100 / 80 = \u20b91,900.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,100",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,900",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b92,300",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,700",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - Find Cost Price 32",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,710 at a loss of 10%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,710 = CP \u00d7 90 / 100\nCP = \u20b91,710 \u00d7 100 / 90 = \u20b91,900.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,900",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,100",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,300",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,700",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - Find Cost Price 33",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b92,160 at a loss of 20%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b92,160 = CP \u00d7 80 / 100\nCP = \u20b92,160 \u00d7 100 / 80 = \u20b92,700.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,100",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,900",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,500",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,700",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - Find Cost Price 34",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,350 at a loss of 25%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,350 = CP \u00d7 75 / 100\nCP = \u20b91,350 \u00d7 100 / 75 = \u20b91,800.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,200",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,600",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,800",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b92,000",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - Find Cost Price 35",
        "difficulty": "Medium",
        "question_text": "An article is sold for \u20b91,125 at a loss of 25%. Find the cost price of the article.",
        "sample_answer": "SP = CP \u00d7 (100 - Loss%) / 100\n\u20b91,125 = CP \u00d7 75 / 100\nCP = \u20b91,125 \u00d7 100 / 75 = \u20b91,500.",
        "tips": "CP = (SP * 100) / (100 - Loss%).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,500",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b91,700",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,900",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,300",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 36",
        "difficulty": "Medium",
        "question_text": "If the cost price of 25 articles is equal to the selling price of 20 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 25 articles = \u20b925.\nSP of 20 articles = \u20b925.\nProfit on 20 articles = \u20b925 - \u20b920 = \u20b95.\nProfit % = (5 / 20) \u00d7 100 = 25.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 37",
        "difficulty": "Medium",
        "question_text": "If the cost price of 20 articles is equal to the selling price of 15 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 20 articles = \u20b920.\nSP of 15 articles = \u20b920.\nProfit on 15 articles = \u20b920 - \u20b915 = \u20b95.\nProfit % = (5 / 15) \u00d7 100 = 33.3%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "43.3%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "33.3%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "28.3%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "38.3%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 38",
        "difficulty": "Medium",
        "question_text": "If the cost price of 20 articles is equal to the selling price of 15 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 20 articles = \u20b920.\nSP of 15 articles = \u20b920.\nProfit on 15 articles = \u20b920 - \u20b915 = \u20b95.\nProfit % = (5 / 15) \u00d7 100 = 33.3%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "28.3%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "38.3%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "33.3%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "43.3%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 39",
        "difficulty": "Medium",
        "question_text": "If the cost price of 15 articles is equal to the selling price of 10 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 15 articles = \u20b915.\nSP of 10 articles = \u20b915.\nProfit on 10 articles = \u20b915 - \u20b910 = \u20b95.\nProfit % = (5 / 10) \u00d7 100 = 50.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "45.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "55.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "60.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 40",
        "difficulty": "Medium",
        "question_text": "If the cost price of 30 articles is equal to the selling price of 25 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 30 articles = \u20b930.\nSP of 25 articles = \u20b930.\nProfit on 25 articles = \u20b930 - \u20b925 = \u20b95.\nProfit % = (5 / 25) \u00d7 100 = 20.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "25.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 41",
        "difficulty": "Medium",
        "question_text": "If the cost price of 25 articles is equal to the selling price of 20 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 25 articles = \u20b925.\nSP of 20 articles = \u20b925.\nProfit on 20 articles = \u20b925 - \u20b920 = \u20b95.\nProfit % = (5 / 20) \u00d7 100 = 25.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "35.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 42",
        "difficulty": "Medium",
        "question_text": "If the cost price of 25 articles is equal to the selling price of 20 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 25 articles = \u20b925.\nSP of 20 articles = \u20b925.\nProfit on 20 articles = \u20b925 - \u20b920 = \u20b95.\nProfit % = (5 / 20) \u00d7 100 = 25.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "20.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "35.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 43",
        "difficulty": "Medium",
        "question_text": "If the cost price of 25 articles is equal to the selling price of 20 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 25 articles = \u20b925.\nSP of 20 articles = \u20b925.\nProfit on 20 articles = \u20b925 - \u20b920 = \u20b95.\nProfit % = (5 / 20) \u00d7 100 = 25.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "20.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "30.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 44",
        "difficulty": "Medium",
        "question_text": "If the cost price of 30 articles is equal to the selling price of 25 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 30 articles = \u20b930.\nSP of 25 articles = \u20b930.\nProfit on 25 articles = \u20b930 - \u20b925 = \u20b95.\nProfit % = (5 / 25) \u00d7 100 = 20.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "20.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "15.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "25.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 45",
        "difficulty": "Medium",
        "question_text": "If the cost price of 30 articles is equal to the selling price of 25 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 30 articles = \u20b930.\nSP of 25 articles = \u20b930.\nProfit on 25 articles = \u20b930 - \u20b925 = \u20b95.\nProfit % = (5 / 25) \u00d7 100 = 20.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "20.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "25.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 46",
        "difficulty": "Medium",
        "question_text": "If the cost price of 25 articles is equal to the selling price of 20 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 25 articles = \u20b925.\nSP of 20 articles = \u20b925.\nProfit on 20 articles = \u20b925 - \u20b920 = \u20b95.\nProfit % = (5 / 20) \u00d7 100 = 25.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "20.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "35.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 47",
        "difficulty": "Medium",
        "question_text": "If the cost price of 30 articles is equal to the selling price of 25 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 30 articles = \u20b930.\nSP of 25 articles = \u20b930.\nProfit on 25 articles = \u20b930 - \u20b925 = \u20b95.\nProfit % = (5 / 25) \u00d7 100 = 20.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "25.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 48",
        "difficulty": "Medium",
        "question_text": "If the cost price of 15 articles is equal to the selling price of 10 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 15 articles = \u20b915.\nSP of 10 articles = \u20b915.\nProfit on 10 articles = \u20b915 - \u20b910 = \u20b95.\nProfit % = (5 / 10) \u00d7 100 = 50.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "45.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "60.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "55.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "50.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 49",
        "difficulty": "Medium",
        "question_text": "If the cost price of 30 articles is equal to the selling price of 25 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 30 articles = \u20b930.\nSP of 25 articles = \u20b930.\nProfit on 25 articles = \u20b930 - \u20b925 = \u20b95.\nProfit % = (5 / 25) \u00d7 100 = 20.0%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "25.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "15.0%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Profit & Loss - CP of X equals SP of Y 50",
        "difficulty": "Medium",
        "question_text": "If the cost price of 20 articles is equal to the selling price of 15 articles, what is the profit percentage?",
        "sample_answer": "Let CP of 1 article = \u20b91. Total CP of 20 articles = \u20b920.\nSP of 15 articles = \u20b920.\nProfit on 15 articles = \u20b920 - \u20b915 = \u20b95.\nProfit % = (5 / 15) \u00d7 100 = 33.3%.",
        "tips": "Profit % = ((Articles bought - Articles sold) / Articles sold) * 100.",
        "options": [
            {
                "label": "A",
                "text": "33.3%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "38.3%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "43.3%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28.3%",
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
            old_qs = Question.query.filter_by(category='Aptitude', topic='Profit & Loss').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Profit & Loss').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Commercial Mathematics',
                    topic='Profit & Loss',
                    title=q.get('title', 'Profit & Loss'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Profit & Loss via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Profit & Loss: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Profit & Loss',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Commercial Mathematics', 'Profit & Loss',
                        q.get('title', 'Profit & Loss'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Profit & Loss into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
