"""
Seed script for Discount (Commercial Mathematics)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Discount - Marked Price & Single Discount 1",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b91,700. If a shopkeeper offers a discount of 20%, what is the selling price?",
        "sample_answer": "Discount = 20% of \u20b91,700 = \u20b9340.\nSelling Price = Marked Price - Discount = \u20b91,360.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,210",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,510",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,610",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,360",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Marked Price & Single Discount 2",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b93,300. If a shopkeeper offers a discount of 25%, what is the selling price?",
        "sample_answer": "Discount = 25% of \u20b93,300 = \u20b9825.\nSelling Price = Marked Price - Discount = \u20b92,475.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,475",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,625",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,725",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,325",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 3",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b94,700. If a shopkeeper offers a discount of 20%, what is the selling price?",
        "sample_answer": "Discount = 20% of \u20b94,700 = \u20b9940.\nSelling Price = Marked Price - Discount = \u20b93,760.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,760",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b94,010",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,910",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,610",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 4",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b92,000. If a shopkeeper offers a discount of 15%, what is the selling price?",
        "sample_answer": "Discount = 15% of \u20b92,000 = \u20b9300.\nSelling Price = Marked Price - Discount = \u20b91,700.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,700",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b91,550",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,950",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b91,850",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 5",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b93,800. If a shopkeeper offers a discount of 15%, what is the selling price?",
        "sample_answer": "Discount = 15% of \u20b93,800 = \u20b9570.\nSelling Price = Marked Price - Discount = \u20b93,230.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,480",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,080",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,230",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b93,380",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Marked Price & Single Discount 6",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b94,900. If a shopkeeper offers a discount of 20%, what is the selling price?",
        "sample_answer": "Discount = 20% of \u20b94,900 = \u20b9980.\nSelling Price = Marked Price - Discount = \u20b93,920.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,920",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,770",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b94,170",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,070",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 7",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b93,300. If a shopkeeper offers a discount of 30%, what is the selling price?",
        "sample_answer": "Discount = 30% of \u20b93,300 = \u20b9990.\nSelling Price = Marked Price - Discount = \u20b92,310.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,460",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,310",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b92,560",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,160",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Marked Price & Single Discount 8",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b94,500. If a shopkeeper offers a discount of 15%, what is the selling price?",
        "sample_answer": "Discount = 15% of \u20b94,500 = \u20b9675.\nSelling Price = Marked Price - Discount = \u20b93,825.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,825",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,675",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,975",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,075",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 9",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b94,000. If a shopkeeper offers a discount of 25%, what is the selling price?",
        "sample_answer": "Discount = 25% of \u20b94,000 = \u20b91,000.\nSelling Price = Marked Price - Discount = \u20b93,000.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,150",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,000",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b93,250",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,850",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Marked Price & Single Discount 10",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b94,900. If a shopkeeper offers a discount of 20%, what is the selling price?",
        "sample_answer": "Discount = 20% of \u20b94,900 = \u20b9980.\nSelling Price = Marked Price - Discount = \u20b93,920.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,070",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,170",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,920",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b93,770",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Marked Price & Single Discount 11",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b93,200. If a shopkeeper offers a discount of 30%, what is the selling price?",
        "sample_answer": "Discount = 30% of \u20b93,200 = \u20b9960.\nSelling Price = Marked Price - Discount = \u20b92,240.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,490",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,090",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,390",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,240",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Marked Price & Single Discount 12",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b95,000. If a shopkeeper offers a discount of 30%, what is the selling price?",
        "sample_answer": "Discount = 30% of \u20b95,000 = \u20b91,500.\nSelling Price = Marked Price - Discount = \u20b93,500.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,500",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,750",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,650",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,350",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 13",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b94,900. If a shopkeeper offers a discount of 10%, what is the selling price?",
        "sample_answer": "Discount = 10% of \u20b94,900 = \u20b9490.\nSelling Price = Marked Price - Discount = \u20b94,410.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,660",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,410",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b94,560",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,260",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Marked Price & Single Discount 14",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b93,100. If a shopkeeper offers a discount of 25%, what is the selling price?",
        "sample_answer": "Discount = 25% of \u20b93,100 = \u20b9775.\nSelling Price = Marked Price - Discount = \u20b92,325.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,575",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b92,325",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b92,175",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,475",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Marked Price & Single Discount 15",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b93,200. If a shopkeeper offers a discount of 30%, what is the selling price?",
        "sample_answer": "Discount = 30% of \u20b93,200 = \u20b9960.\nSelling Price = Marked Price - Discount = \u20b92,240.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b92,240",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b92,490",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b92,390",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b92,090",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 16",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b91,800. If a shopkeeper offers a discount of 20%, what is the selling price?",
        "sample_answer": "Discount = 20% of \u20b91,800 = \u20b9360.\nSelling Price = Marked Price - Discount = \u20b91,440.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,690",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b91,290",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,440",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b91,590",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Marked Price & Single Discount 17",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b93,500. If a shopkeeper offers a discount of 10%, what is the selling price?",
        "sample_answer": "Discount = 10% of \u20b93,500 = \u20b9350.\nSelling Price = Marked Price - Discount = \u20b93,150.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,150",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "\u20b93,300",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,400",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b93,000",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Marked Price & Single Discount 18",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b91,200. If a shopkeeper offers a discount of 20%, what is the selling price?",
        "sample_answer": "Discount = 20% of \u20b91,200 = \u20b9240.\nSelling Price = Marked Price - Discount = \u20b9960.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b91,110",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b9810",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b91,210",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b9960",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Marked Price & Single Discount 19",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b95,000. If a shopkeeper offers a discount of 25%, what is the selling price?",
        "sample_answer": "Discount = 25% of \u20b95,000 = \u20b91,250.\nSelling Price = Marked Price - Discount = \u20b93,750.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b93,900",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b93,600",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "\u20b93,750",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "\u20b94,000",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Marked Price & Single Discount 20",
        "difficulty": "Easy",
        "question_text": "The marked price of an article is \u20b94,900. If a shopkeeper offers a discount of 10%, what is the selling price?",
        "sample_answer": "Discount = 10% of \u20b94,900 = \u20b9490.\nSelling Price = Marked Price - Discount = \u20b94,410.",
        "tips": "SP = MP * (1 - Discount%/100).",
        "options": [
            {
                "label": "A",
                "text": "\u20b94,560",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "\u20b94,410",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "\u20b94,260",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "\u20b94,660",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Successive Discount Equivalence 21",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 20%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 20 - (20 \u00d7 20 / 100) = 36.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "36.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "38.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "40%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Successive Discount Equivalence 22",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 15%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 15 - (20 \u00d7 15 / 100) = 32.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "35%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Successive Discount Equivalence 23",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 10% and 10%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 10 + 10 - (10 \u00d7 10 / 100) = 19.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "19.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "21.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Successive Discount Equivalence 24",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 15%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 15 - (20 \u00d7 15 / 100) = 32.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "35%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Successive Discount Equivalence 25",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 10%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 10 - (20 \u00d7 10 / 100) = 28.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "26.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Successive Discount Equivalence 26",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 10%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 10 - (20 \u00d7 10 / 100) = 28.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "26.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28.0%",
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
        "title": "Discount - Successive Discount Equivalence 27",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 10% and 20%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 10 + 20 - (10 \u00d7 20 / 100) = 28.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "26.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "28.0%",
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
        "title": "Discount - Successive Discount Equivalence 28",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 10% and 15%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 10 + 15 - (10 \u00d7 15 / 100) = 23.5%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "23.5%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "25%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "25.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "21.5%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Successive Discount Equivalence 29",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 10% and 15%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 10 + 15 - (10 \u00d7 15 / 100) = 23.5%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "25%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "25.5%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "21.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "23.5%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Successive Discount Equivalence 30",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 10%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 10 - (20 \u00d7 10 / 100) = 28.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "26.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "28.0%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Successive Discount Equivalence 31",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 10% and 20%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 10 + 20 - (10 \u00d7 20 / 100) = 28.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "28.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "26.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Successive Discount Equivalence 32",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 15%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 15 - (20 \u00d7 15 / 100) = 32.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "34.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "35%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Successive Discount Equivalence 33",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 10%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 10 - (20 \u00d7 10 / 100) = 28.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "26.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "28.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30.0%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Successive Discount Equivalence 34",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 10%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 10 - (20 \u00d7 10 / 100) = 28.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "26.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "28.0%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30.0%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Successive Discount Equivalence 35",
        "difficulty": "Medium",
        "question_text": "Find the single discount equivalent to two successive discounts of 20% and 15%.",
        "sample_answer": "Equivalent discount = d1 + d2 - (d1 \u00d7 d2 / 100) = 20 + 15 - (20 \u00d7 15 / 100) = 32.0%.",
        "tips": "Formula: Single Equivalent Discount = d1 + d2 - (d1 * d2)/100.",
        "options": [
            {
                "label": "A",
                "text": "32.0%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "35%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30.0%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "34.0%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Markup for Desired Profit 36",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 110 / 0.80 = 137.5.\nMarkup % = 37.5%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "37.5%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "32.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "42.5%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Markup for Desired Profit 37",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 110 / 0.80 = 137.5.\nMarkup % = 37.5%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "37.5%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "42.5%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32.5%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Markup for Desired Profit 38",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 10%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 10/100) = 0.90 \u00d7 MP,\nMP = 110 / 0.90 = 122.2.\nMarkup % = 22.2%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "22.2%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "27.2%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17.2%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "20%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Markup for Desired Profit 39",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 20%?",
        "sample_answer": "Let CP = 100. Desired SP = 120.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 120 / 0.80 = 150.0.\nMarkup % = 50.0%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "55.0%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "45.0%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "50.0%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "40%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Markup for Desired Profit 40",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 10%, he still gains 20%?",
        "sample_answer": "Let CP = 100. Desired SP = 120.\nSince SP = MP \u00d7 (1 - 10/100) = 0.90 \u00d7 MP,\nMP = 120 / 0.90 = 133.3.\nMarkup % = 33.3%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "28.3%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "33.3%",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "38.3%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "30%",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Discount - Markup for Desired Profit 41",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 110 / 0.80 = 137.5.\nMarkup % = 37.5%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "37.5%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "42.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "32.5%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Markup for Desired Profit 42",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 110 / 0.80 = 137.5.\nMarkup % = 37.5%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "32.5%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "42.5%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "37.5%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Markup for Desired Profit 43",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 10%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 10/100) = 0.90 \u00d7 MP,\nMP = 110 / 0.90 = 122.2.\nMarkup % = 22.2%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "22.2%",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "17.2%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "20%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "27.2%",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Discount - Markup for Desired Profit 44",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 10%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 10/100) = 0.90 \u00d7 MP,\nMP = 110 / 0.90 = 122.2.\nMarkup % = 22.2%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "20%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "27.2%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22.2%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "17.2%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Markup for Desired Profit 45",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 110 / 0.80 = 137.5.\nMarkup % = 37.5%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "32.5%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "42.5%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "37.5%",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Discount - Markup for Desired Profit 46",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 20%?",
        "sample_answer": "Let CP = 100. Desired SP = 120.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 120 / 0.80 = 150.0.\nMarkup % = 50.0%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "40%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "45.0%",
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
        "title": "Discount - Markup for Desired Profit 47",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 10%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 10/100) = 0.90 \u00d7 MP,\nMP = 110 / 0.90 = 122.2.\nMarkup % = 22.2%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "20%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.2%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22.2%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "27.2%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Markup for Desired Profit 48",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 110 / 0.80 = 137.5.\nMarkup % = 37.5%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "42.5%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "30%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "37.5%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "32.5%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Markup for Desired Profit 49",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 10%, he still gains 10%?",
        "sample_answer": "Let CP = 100. Desired SP = 110.\nSince SP = MP \u00d7 (1 - 10/100) = 0.90 \u00d7 MP,\nMP = 110 / 0.90 = 122.2.\nMarkup % = 22.2%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "20%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17.2%",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "22.2%",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "27.2%",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Discount - Markup for Desired Profit 50",
        "difficulty": "Medium",
        "question_text": "By what percentage should a trader mark goods above the cost price so that after allowing a discount of 20%, he still gains 20%?",
        "sample_answer": "Let CP = 100. Desired SP = 120.\nSince SP = MP \u00d7 (1 - 20/100) = 0.80 \u00d7 MP,\nMP = 120 / 0.80 = 150.0.\nMarkup % = 50.0%.",
        "tips": "MP / CP = (100 + Profit%) / (100 - Discount%).",
        "options": [
            {
                "label": "A",
                "text": "40%",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "45.0%",
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
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Discount').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Discount').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Commercial Mathematics',
                    topic='Discount',
                    title=q.get('title', 'Discount'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Discount via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Discount: {e}")

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
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Discount',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Commercial Mathematics', 'Discount',
                        q.get('title', 'Discount'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Discount into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
