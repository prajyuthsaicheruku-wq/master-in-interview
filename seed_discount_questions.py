import sqlite3
import json

questions_data = [
    {
        "q_num": 1,
        "title": "Discount - Selling Price after Discount",
        "question_text": "A shirt is marked at ₹2,000 and sold at a discount of 15%. Find the selling price.\n\nA) ₹1,650\nB) ₹1,700\nC) ₹1,750\nD) ₹1,800",
        "options": [
            {"label": "A", "text": "₹1,650", "is_correct": False},
            {"label": "B", "text": "₹1,700", "is_correct": True},
            {"label": "C", "text": "₹1,750", "is_correct": False},
            {"label": "D", "text": "₹1,800", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹2,000, Discount = 15%\nSelling Price = MP * (1 - Discount/100)\n= 2000 * (1 - 0.15) = 2000 * 0.85 = ₹1,700.",
        "tips": "SP = MP * (100 - Discount%) / 100."
    },
    {
        "q_num": 2,
        "title": "Discount - Discount Amount and SP",
        "question_text": "A shopkeeper offers a 20% discount on an item marked ₹1,500. Find the discount amount and selling price.\n\nA) Discount = ₹250, SP = ₹1,250\nB) Discount = ₹300, SP = ₹1,200\nC) Discount = ₹350, SP = ₹1,150\nD) Discount = ₹400, SP = ₹1,100",
        "options": [
            {"label": "A", "text": "Discount = ₹250, SP = ₹1,250", "is_correct": False},
            {"label": "B", "text": "Discount = ₹300, SP = ₹1,200", "is_correct": True},
            {"label": "C", "text": "Discount = ₹350, SP = ₹1,150", "is_correct": False},
            {"label": "D", "text": "Discount = ₹400, SP = ₹1,100", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹1,500, Discount % = 20%\nDiscount Amount = 1500 * (20/100) = ₹300.\nSelling Price = 1500 - 300 = ₹1,200.",
        "tips": "Discount Amount = MP * (Discount % / 100)."
    },
    {
        "q_num": 3,
        "title": "Discount - Marked Price from SP and Discount %",
        "question_text": "An article is sold for ₹2,400 after a discount of 25%. Find its marked price.\n\nA) ₹3,000\nB) ₹3,200\nC) ₹3,500\nD) ₹3,600",
        "options": [
            {"label": "A", "text": "₹3,000", "is_correct": False},
            {"label": "B", "text": "₹3,200", "is_correct": True},
            {"label": "C", "text": "₹3,500", "is_correct": False},
            {"label": "D", "text": "₹3,600", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹2,400, Discount = 25%\nSP = MP * (1 - 0.25) = 0.75 MP\n=> MP = 2400 / 0.75 = ₹3,200.",
        "tips": "MP = SP / (1 - Discount_decimal)."
    },
    {
        "q_num": 4,
        "title": "Discount - Discount Percentage Calculation",
        "question_text": "A watch marked at ₹3,200 is sold for ₹2,720. Find the discount percentage.\n\nA) 12%\nB) 15%\nC) 18%\nD) 20%",
        "options": [
            {"label": "A", "text": "12%", "is_correct": False},
            {"label": "B", "text": "15%", "is_correct": True},
            {"label": "C", "text": "18%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹3,200, SP = ₹2,720\nDiscount Amount = 3200 - 2720 = ₹480.\nDiscount % = (480 / 3200) * 100 = 15%.",
        "tips": "Discount % = (Discount Amount / MP) * 100."
    },
    {
        "q_num": 5,
        "title": "Discount - SP after 10% Discount",
        "question_text": "A retailer gives a discount of 10% on a product marked at ₹5,000. Find the selling price.\n\nA) ₹4,250\nB) ₹4,500\nC) ₹4,750\nD) ₹4,800",
        "options": [
            {"label": "A", "text": "₹4,250", "is_correct": False},
            {"label": "B", "text": "₹4,500", "is_correct": True},
            {"label": "C", "text": "₹4,750", "is_correct": False},
            {"label": "D", "text": "₹4,800", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹5,000, Discount = 10%\nSP = 5000 * 0.90 = ₹4,500.",
        "tips": "10% discount leaves 90% of marked price."
    },
    {
        "q_num": 6,
        "title": "Discount - Discount Percentage from Amount",
        "question_text": "A mobile phone is marked at ₹18,000 and sold at a discount of ₹2,700. Find the discount percentage.\n\nA) 12.5%\nB) 15%\nC) 17.5%\nD) 20%",
        "options": [
            {"label": "A", "text": "12.5%", "is_correct": False},
            {"label": "B", "text": "15%", "is_correct": True},
            {"label": "C", "text": "17.5%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹18,000, Discount Amount = ₹2,700\nDiscount % = (2700 / 18000) * 100 = 15%.",
        "tips": "Divide discount amount by MP."
    },
    {
        "q_num": 7,
        "title": "Discount - Marked Price from 10% Discount",
        "question_text": "A customer pays ₹4,500 after getting a 10% discount. Find the marked price.\n\nA) ₹4,800\nB) ₹5,000\nC) ₹5,200\nD) ₹5,500",
        "options": [
            {"label": "A", "text": "₹4,800", "is_correct": False},
            {"label": "B", "text": "₹5,000", "is_correct": True},
            {"label": "C", "text": "₹5,200", "is_correct": False},
            {"label": "D", "text": "₹5,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹4,500, Discount = 10%\nMP = 4500 / 0.90 = ₹5,000.",
        "tips": "Divide SP by 0.90."
    },
    {
        "q_num": 8,
        "title": "Discount - SP after 15% Discount",
        "question_text": "An article marked at ₹2,800 is sold after a 15% discount. Find the selling price.\n\nA) ₹2,300\nB) ₹2,380\nC) ₹2,420\nD) ₹2,500",
        "options": [
            {"label": "A", "text": "₹2,300", "is_correct": False},
            {"label": "B", "text": "₹2,380", "is_correct": True},
            {"label": "C", "text": "₹2,420", "is_correct": False},
            {"label": "D", "text": "₹2,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹2,800, Discount = 15%\nSP = 2800 * 0.85 = ₹2,380.",
        "tips": "Multiply MP by 0.85."
    },
    {
        "q_num": 9,
        "title": "Discount - Two Successive Discounts",
        "question_text": "A shopkeeper offers two successive discounts of 10% and 5% on a product marked at ₹4,000. Find the final selling price.\n\nA) ₹3,350\nB) ₹3,420\nC) ₹3,500\nD) ₹3,600",
        "options": [
            {"label": "A", "text": "₹3,350", "is_correct": False},
            {"label": "B", "text": "₹3,420", "is_correct": True},
            {"label": "C", "text": "₹3,500", "is_correct": False},
            {"label": "D", "text": "₹3,600", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹4,000.\nAfter 1st discount (10%) = 4000 * 0.90 = ₹3,600.\nAfter 2nd discount (5%) = 3600 * 0.95 = ₹3,420.",
        "tips": "Final SP = MP * (1 - d1) * (1 - d2)."
    },
    {
        "q_num": 10,
        "title": "Discount - Refrigerator 12% Discount",
        "question_text": "A refrigerator marked at ₹25,000 is sold at a discount of 12%. Find the selling price.\n\nA) ₹21,500\nB) ₹22,000\nC) ₹22,500\nD) ₹23,000",
        "options": [
            {"label": "A", "text": "₹21,500", "is_correct": False},
            {"label": "B", "text": "₹22,000", "is_correct": True},
            {"label": "C", "text": "₹22,500", "is_correct": False},
            {"label": "D", "text": "₹23,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹25,000, Discount = 12%\nSP = 25000 * (1 - 0.12) = 25000 * 0.88 = ₹22,000.",
        "tips": "Multiply MP by 0.88."
    },
    {
        "q_num": 11,
        "title": "Discount - MP from SP and 20% Discount",
        "question_text": "A product is sold for ₹7,200 after a 20% discount. Find its marked price.\n\nA) ₹8,500\nB) ₹9,000\nC) ₹9,500\nD) ₹10,000",
        "options": [
            {"label": "A", "text": "₹8,500", "is_correct": False},
            {"label": "B", "text": "₹9,000", "is_correct": True},
            {"label": "C", "text": "₹9,500", "is_correct": False},
            {"label": "D", "text": "₹10,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹7,200, Discount = 20%\nMP = 7200 / 0.80 = ₹9,000.",
        "tips": "Divide SP by 0.80."
    },
    {
        "q_num": 12,
        "title": "Discount - Discount Amount 18%",
        "question_text": "A shopkeeper gives a discount of 18% on an item marked at ₹1,250. Find the discount amount.\n\nA) ₹200\nB) ₹225\nC) ₹250\nD) ₹275",
        "options": [
            {"label": "A", "text": "₹200", "is_correct": False},
            {"label": "B", "text": "₹225", "is_correct": True},
            {"label": "C", "text": "₹250", "is_correct": False},
            {"label": "D", "text": "₹275", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹1,250, Discount = 18%\nDiscount Amount = 1250 * (18/100) = ₹225.",
        "tips": "1250 * 0.18 = 225."
    },
    {
        "q_num": 13,
        "title": "Discount - SP after 25% Discount",
        "question_text": "An article marked at ₹6,000 is sold at a discount of 25%. Find the selling price.\n\nA) ₹4,200\nB) ₹4,500\nC) ₹4,800\nD) ₹5,000",
        "options": [
            {"label": "A", "text": "₹4,200", "is_correct": False},
            {"label": "B", "text": "₹4,500", "is_correct": True},
            {"label": "C", "text": "₹4,800", "is_correct": False},
            {"label": "D", "text": "₹5,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹6,000, Discount = 25%\nSP = 6000 * 0.75 = ₹4,500.",
        "tips": "25% off leaves 75% of MP."
    },
    {
        "q_num": 14,
        "title": "Discount - Discount Percentage from ₹800 Off",
        "question_text": "A customer receives a discount of ₹800 on a product marked at ₹4,000. Find the discount percentage.\n\nA) 15%\nB) 20%\nC) 25%\nD) 30%",
        "options": [
            {"label": "A", "text": "15%", "is_correct": False},
            {"label": "B", "text": "20%", "is_correct": True},
            {"label": "C", "text": "25%", "is_correct": False},
            {"label": "D", "text": "30%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹4,000, Discount Amount = ₹800\nDiscount % = (800 / 4000) * 100 = 20%.",
        "tips": "(800 / 4000) * 100 = 20%."
    },
    {
        "q_num": 15,
        "title": "Discount - Rate of Discount Bicycle",
        "question_text": "A bicycle marked at ₹12,500 is sold for ₹11,250. Find the rate of discount.\n\nA) 8%\nB) 10%\nC) 12%\nD) 15%",
        "options": [
            {"label": "A", "text": "8%", "is_correct": False},
            {"label": "B", "text": "10%", "is_correct": True},
            {"label": "C", "text": "12%", "is_correct": False},
            {"label": "D", "text": "15%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹12,500, SP = ₹11,250\nDiscount Amount = 12500 - 11250 = ₹1,250.\nDiscount % = (1250 / 12500) * 100 = 10%.",
        "tips": "Subtract SP from MP to get discount amount."
    },
    {
        "q_num": 16,
        "title": "Discount - Markup 25% and 10% Discount Profit %",
        "question_text": "A shopkeeper marks an article 25% above cost price and gives a discount of 10%. Find his profit percentage.\n\nA) 10%\nB) 12.5%\nC) 15%\nD) 17.5%",
        "options": [
            {"label": "A", "text": "10%", "is_correct": False},
            {"label": "B", "text": "12.5%", "is_correct": True},
            {"label": "C", "text": "15%", "is_correct": False},
            {"label": "D", "text": "17.5%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 125.\nDiscount = 10% of 125 = 12.5.\nSP = 125 - 12.5 = 112.5.\nProfit % = 112.5 - 100 = 12.5%.",
        "tips": "Net % = 25 - 10 - (250/100) = 12.5%."
    },
    {
        "q_num": 17,
        "title": "Discount - Two Successive Discounts & Equivalent Single Discount",
        "question_text": "Two successive discounts of 20% and 15% are offered on a product marked at ₹8,000. Find the final selling price and equivalent single discount percentage.\n\nA) SP = ₹5,200, Discount = 35%\nB) SP = ₹5,440, Discount = 32%\nC) SP = ₹5,600, Discount = 30%\nD) SP = ₹6,000, Discount = 25%",
        "options": [
            {"label": "A", "text": "SP = ₹5,200, Discount = 35%", "is_correct": False},
            {"label": "B", "text": "SP = ₹5,440, Discount = 32%", "is_correct": True},
            {"label": "C", "text": "SP = ₹5,600, Discount = 30%", "is_correct": False},
            {"label": "D", "text": "SP = ₹6,000, Discount = 25%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹8,000.\nSP = 8000 * 0.80 * 0.85 = ₹5,440.\nSingle Equivalent Discount % = 20 + 15 - (20*15)/100 = 35 - 3 = 32%.",
        "tips": "Single Equivalent Discount % = d1 + d2 - (d1*d2/100)."
    },
    {
        "q_num": 18,
        "title": "Discount - Three Successive Discounts",
        "question_text": "A retailer offers three successive discounts of 10%, 15%, and 20% on an item marked at ₹10,000. Find the final selling price.\n\nA) ₹5,800\nB) ₹6,120\nC) ₹6,400\nD) ₹6,500",
        "options": [
            {"label": "A", "text": "₹5,800", "is_correct": False},
            {"label": "B", "text": "₹6,120", "is_correct": True},
            {"label": "C", "text": "₹6,400", "is_correct": False},
            {"label": "D", "text": "₹6,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹10,000.\nSP = 10000 * (1 - 0.10) * (1 - 0.15) * (1 - 0.20)\n= 10000 * 0.90 * 0.85 * 0.80 = 10000 * 0.612 = ₹6,120.",
        "tips": "Multiply MP by product of all three discount multipliers."
    },
    {
        "q_num": 19,
        "title": "Discount - Markup 40% and 20% Discount Profit %",
        "question_text": "An article is marked 40% above its cost price and sold at a discount of 20%. Find the profit percentage.\n\nA) 10%\nB) 12%\nC) 15%\nD) 20%",
        "options": [
            {"label": "A", "text": "10%", "is_correct": False},
            {"label": "B", "text": "12%", "is_correct": True},
            {"label": "C", "text": "15%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 140.\nSP = 140 * 0.80 = 112.\nProfit % = 112 - 100 = 12%.",
        "tips": "Net % = Markup - Discount - (Markup * Discount / 100)."
    },
    {
        "q_num": 20,
        "title": "Discount - Marked Price from Two Successive Discounts",
        "question_text": "A product is sold at ₹5,440 after two successive discounts of 15% and 20%. Find the marked price.\n\nA) ₹7,500\nB) ₹8,000\nC) ₹8,500\nD) ₹9,000",
        "options": [
            {"label": "A", "text": "₹7,500", "is_correct": False},
            {"label": "B", "text": "₹8,000", "is_correct": True},
            {"label": "C", "text": "₹8,500", "is_correct": False},
            {"label": "D", "text": "₹9,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = MP * 0.85 * 0.80 = MP * 0.68\n=> 5440 = 0.68 MP\n=> MP = 5440 / 0.68 = ₹8,000.",
        "tips": "MP = SP / [(1 - d1) * (1 - d2)]."
    },
    {
        "q_num": 21,
        "title": "Discount - MP from Discount % and Profit %",
        "question_text": "A shopkeeper allows a discount of 12% and still earns a profit of 10%. If the cost price is ₹4,500, find the marked price.\n\nA) ₹5,200\nB) ₹5,625\nC) ₹5,800\nD) ₹6,000",
        "options": [
            {"label": "A", "text": "₹5,200", "is_correct": False},
            {"label": "B", "text": "₹5,625", "is_correct": True},
            {"label": "C", "text": "₹5,800", "is_correct": False},
            {"label": "D", "text": "₹6,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "CP = ₹4,500 => SP = 4500 * 1.10 = ₹4,950.\n0.88 MP = 4950 => MP = 4950 / 0.88 = ₹5,625.",
        "tips": "Formula: MP/CP = (100 + Profit%) / (100 - Discount%)."
    },
    {
        "q_num": 22,
        "title": "Discount - Markup 50% and 10% Discount",
        "question_text": "A dealer marks a product 50% above cost price and offers a discount of 10%. Find the profit percentage.\n\nA) 30%\nB) 35%\nC) 40%\nD) 45%",
        "options": [
            {"label": "A", "text": "30%", "is_correct": False},
            {"label": "B", "text": "35%", "is_correct": True},
            {"label": "C", "text": "40%", "is_correct": False},
            {"label": "D", "text": "45%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 150.\nSP = 150 * 0.90 = 135.\nProfit % = 135 - 100 = 35%.",
        "tips": "Net % = 50 - 10 - (500/100) = 35%."
    },
    {
        "q_num": 23,
        "title": "Discount - Successive 20% and 10% on TV",
        "question_text": "The marked price of a television is ₹36,000. During a sale, discounts of 20% and 10% are offered successively. Find the final selling price.\n\nA) ₹24,500\nB) ₹25,920\nC) ₹26,500\nD) ₹27,000",
        "options": [
            {"label": "A", "text": "₹24,500", "is_correct": False},
            {"label": "B", "text": "₹25,920", "is_correct": True},
            {"label": "C", "text": "₹26,500", "is_correct": False},
            {"label": "D", "text": "₹27,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹36,000.\nSP = 36000 * 0.80 * 0.90 = 36000 * 0.72 = ₹25,920.",
        "tips": "Net multiplier = 0.72."
    },
    {
        "q_num": 24,
        "title": "Discount - Cost Price from Discount % and Gain %",
        "question_text": "An article is sold for ₹3,060 after a discount of 15%. If the shopkeeper gains 20%, find the cost price.\n\nA) ₹2,400\nB) ₹2,550\nC) ₹2,700\nD) ₹2,800",
        "options": [
            {"label": "A", "text": "₹2,400", "is_correct": False},
            {"label": "B", "text": "₹2,550", "is_correct": True},
            {"label": "C", "text": "₹2,700", "is_correct": False},
            {"label": "D", "text": "₹2,800", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹3,060.\nSince SP = CP * (1 + 0.20) = 1.20 CP\n=> CP = 3060 / 1.20 = ₹2,550.",
        "tips": "CP = SP / (1 + Gain%)."
    },
    {
        "q_num": 25,
        "title": "Discount - MP from CP, Discount % and Gain %",
        "question_text": "A trader offers a discount of 25% and still gains 12.5%. If the cost price is ₹8,000, find the marked price.\n\nA) ₹10,000\nB) ₹12,000\nC) ₹13,500\nD) ₹14,000",
        "options": [
            {"label": "A", "text": "₹10,000", "is_correct": False},
            {"label": "B", "text": "₹12,000", "is_correct": True},
            {"label": "C", "text": "₹13,500", "is_correct": False},
            {"label": "D", "text": "₹14,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "CP = ₹8,000 => SP = 8000 * 1.125 = ₹9,000.\n0.75 MP = 9000 => MP = 9000 / 0.75 = ₹12,000.",
        "tips": "MP/CP = (100 + 12.5) / (100 - 25) = 112.5 / 75 = 1.5."
    },
    {
        "q_num": 26,
        "title": "Discount - Markup 60% and 25% Discount",
        "question_text": "A shopkeeper marks an item 60% above cost price and allows a discount of 25%. Find the profit percentage.\n\nA) 15%\nB) 20%\nC) 25%\nD) 30%",
        "options": [
            {"label": "A", "text": "15%", "is_correct": False},
            {"label": "B", "text": "20%", "is_correct": True},
            {"label": "C", "text": "25%", "is_correct": False},
            {"label": "D", "text": "30%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 160.\nSP = 160 * 0.75 = 120.\nProfit % = 120 - 100 = 20%.",
        "tips": "1.60 * 0.75 = 1.20."
    },
    {
        "q_num": 27,
        "title": "Discount - Three Successive Discounts 10%, 20%, 5%",
        "question_text": "A product marked at ₹15,000 is sold after successive discounts of 10%, 20%, and 5%. Find the final selling price.\n\nA) ₹9,800\nB) ₹10,260\nC) ₹10,500\nD) ₹11,000",
        "options": [
            {"label": "A", "text": "₹9,800", "is_correct": False},
            {"label": "B", "text": "₹10,260", "is_correct": True},
            {"label": "C", "text": "₹10,500", "is_correct": False},
            {"label": "D", "text": "₹11,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹15,000.\nSP = 15000 * 0.90 * 0.80 * 0.95 = 15000 * 0.684 = ₹10,260.",
        "tips": "Multiply MP by 0.684."
    },
    {
        "q_num": 28,
        "title": "Discount - Marked Price & Discount % from Discount Amount",
        "question_text": "A customer gets a discount of ₹1,875 on an item and pays ₹10,625. Find the marked price and discount percentage.\n\nA) MP = ₹12,000, Discount = 12%\nB) MP = ₹12,500, Discount = 15%\nC) MP = ₹13,000, Discount = 18%\nD) MP = ₹13,500, Discount = 20%",
        "options": [
            {"label": "A", "text": "MP = ₹12,000, Discount = 12%", "is_correct": False},
            {"label": "B", "text": "MP = ₹12,500, Discount = 15%", "is_correct": True},
            {"label": "C", "text": "MP = ₹13,000, Discount = 18%", "is_correct": False},
            {"label": "D", "text": "MP = ₹13,500, Discount = 20%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = SP + Discount = 10625 + 1875 = ₹12,500.\nDiscount % = (1875 / 12500) * 100 = 15%.",
        "tips": "MP = Amount Paid + Discount Received."
    },
    {
        "q_num": 29,
        "title": "Discount - Finding CP from Markup %, Discount % & Absolute Profit",
        "question_text": "An article is marked 30% above cost price. To give a customer a discount of 10% and still earn a profit of ₹468, find the cost price.\n\nA) ₹2,500\nB) ₹2,752.94\nC) ₹2,800\nD) ₹3,000",
        "options": [
            {"label": "A", "text": "₹2,500", "is_correct": False},
            {"label": "B", "text": "₹2,752.94", "is_correct": True},
            {"label": "C", "text": "₹2,800", "is_correct": False},
            {"label": "D", "text": "₹3,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100x => MP = 130x.\nSP = 130x * 0.90 = 117x.\nProfit = 117x - 100x = 17x = ₹468.\n=> x = 468 / 17 = 27.5294.\nCP = 100 * 27.5294 = ₹2,752.94.",
        "tips": "17% of CP = ₹468 => CP = 468 / 0.17."
    },
    {
        "q_num": 30,
        "title": "Discount - Multi-Output Comprehensive Problem",
        "question_text": "A dealer marks goods 80% above cost price and gives successive discounts of 20% and 10%. If the selling price is ₹12,960, find: Cost Price, Marked Price, Profit Percentage.\n\nA) CP = ₹9,000, MP = ₹16,200, Profit = 25%\nB) CP = ₹10,000, MP = ₹18,000, Profit = 29.6%\nC) CP = ₹11,000, MP = ₹19,800, Profit = 30%\nD) CP = ₹12,000, MP = ₹21,600, Profit = 32%",
        "options": [
            {"label": "A", "text": "CP = ₹9,000, MP = ₹16,200, Profit = 25%", "is_correct": False},
            {"label": "B", "text": "CP = ₹10,000, MP = ₹18,000, Profit = 29.6%", "is_correct": True},
            {"label": "C", "text": "CP = ₹11,000, MP = ₹19,800, Profit = 30%", "is_correct": False},
            {"label": "D", "text": "CP = ₹12,000, MP = ₹21,600, Profit = 32%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = x => MP = 1.80x.\nSP = 1.80x * 0.80 * 0.90 = 1.296x = 12960 => x = ₹10,000.\nCP = ₹10,000, MP = ₹18,000.\nProfit = 12960 - 10000 = ₹2,960.\nProfit % = (2960 / 10000) * 100 = 29.6%.",
        "tips": "1.80 * 0.80 * 0.90 = 1.296."
    }
]

def seed_database():
    conn = sqlite3.connect('instance/interview_portal.db')
    cursor = conn.cursor()
    
    # Clean out existing Discount questions if any
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Discount'")
    print(f"Cleared previous Discount questions.")
    
    for q in questions_data:
        category = "Aptitude"
        sub_category = "Commercial Mathematics"
        topic = "Discount"
        title = q["title"]
        difficulty = "Medium" if q["q_num"] <= 15 else "Hard"
        question_text = q["question_text"]
        sample_answer = q["sample_answer"]
        tips = q["tips"]
        options_json = json.dumps(q["options"])
        correct_option = q["correct_option"]
        
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options_json, correct_option))
        
    conn.commit()
    print(f"Successfully seeded {len(questions_data)} Discount questions into instance/interview_portal.db!")
    conn.close()

if __name__ == "__main__":
    seed_database()
