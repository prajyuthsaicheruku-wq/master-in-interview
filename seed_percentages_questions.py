import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db')

questions = [
    {
        "title": "Percentages - 25% of 480",
        "difficulty": "Medium",
        "question_text": "What is 25% of 480?",
        "sample_answer": "25% of 480 = (25 / 100) × 480 = 120.",
        "tips": "25% = 1/4th of 480.",
        "options": [
            {"label": "A", "text": "100", "is_correct": False},
            {"label": "B", "text": "110", "is_correct": False},
            {"label": "C", "text": "120", "is_correct": True},
            {"label": "D", "text": "125", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - 12% Salary Increase",
        "difficulty": "Medium",
        "question_text": "A person's salary is ₹25,000. If it is increased by 12%, what will be the new salary?",
        "sample_answer": "Increase = 12% of 25000 = ₹3,000.\nNew salary = 25000 + 3000 = ₹28,000.",
        "tips": "25000 × 1.12.",
        "options": [
            {"label": "A", "text": "₹27,500", "is_correct": False},
            {"label": "B", "text": "₹28,000", "is_correct": True},
            {"label": "C", "text": "₹28,500", "is_correct": False},
            {"label": "D", "text": "₹29,000", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - 15% Price Reduction",
        "difficulty": "Medium",
        "question_text": "The price of a laptop is ₹60,000. If its price is reduced by 15%, what is the new price?",
        "sample_answer": "Discount = 15% of 60000 = ₹9,000.\nNew price = 60000 − 9000 = ₹51,000.",
        "tips": "60000 × 0.85.",
        "options": [
            {"label": "A", "text": "₹49,000", "is_correct": False},
            {"label": "B", "text": "₹50,000", "is_correct": False},
            {"label": "C", "text": "₹51,000", "is_correct": True},
            {"label": "D", "text": "₹52,000", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Find Original Number from 40% = 96",
        "difficulty": "Medium",
        "question_text": "If 40% of a number is 96, find the number.",
        "sample_answer": "0.40 × N = 96 => N = 96 / 0.40 = 240.",
        "tips": "(96 / 40) × 100.",
        "options": [
            {"label": "A", "text": "220", "is_correct": False},
            {"label": "B", "text": "230", "is_correct": False},
            {"label": "C", "text": "240", "is_correct": True},
            {"label": "D", "text": "250", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Student Marks Percentage (420 / 600)",
        "difficulty": "Medium",
        "question_text": "A student scores 420 marks out of 600. What percentage did the student score?",
        "sample_answer": "Percentage = (420 / 600) × 100 = 70%.",
        "tips": "420 / 6.",
        "options": [
            {"label": "A", "text": "65%", "is_correct": False},
            {"label": "B", "text": "68%", "is_correct": False},
            {"label": "C", "text": "70%", "is_correct": True},
            {"label": "D", "text": "72%", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - 10% Population Growth from 80,000",
        "difficulty": "Medium",
        "question_text": "The population of a town is 80,000. It increases by 10% in one year. Find the new population.",
        "sample_answer": "Increase = 10% of 80000 = 8000.\nNew population = 80000 + 8000 = 88,000.",
        "tips": "80000 × 1.10.",
        "options": [
            {"label": "A", "text": "86,000", "is_correct": False},
            {"label": "B", "text": "87,000", "is_correct": False},
            {"label": "C", "text": "88,000", "is_correct": True},
            {"label": "D", "text": "90,000", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - 25% More Than 200",
        "difficulty": "Medium",
        "question_text": "A number is 25% more than 200. What is the number?",
        "sample_answer": "200 + (25% of 200) = 200 + 50 = 250.",
        "tips": "200 × 1.25.",
        "options": [
            {"label": "A", "text": "225", "is_correct": False},
            {"label": "B", "text": "240", "is_correct": False},
            {"label": "C", "text": "250", "is_correct": True},
            {"label": "D", "text": "275", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - 40% Passing Marks out of 500",
        "difficulty": "Medium",
        "question_text": "A candidate needs 40% marks to pass an examination of 500 marks. How many marks are required to pass?",
        "sample_answer": "Passing marks = 40% of 500 = (40 / 100) × 500 = 200.",
        "tips": "500 × 0.40.",
        "options": [
            {"label": "A", "text": "180", "is_correct": False},
            {"label": "B", "text": "190", "is_correct": False},
            {"label": "C", "text": "200", "is_correct": True},
            {"label": "D", "text": "220", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - 15% Reduction in Rice Consumption",
        "difficulty": "Medium",
        "question_text": "A family consumes 80 kg of rice per month. If consumption is reduced by 15%, how much rice will they consume now?",
        "sample_answer": "Reduction = 15% of 80 = 12 kg.\nNew consumption = 80 − 12 = 68 kg.",
        "tips": "80 × 0.85.",
        "options": [
            {"label": "A", "text": "66 kg", "is_correct": False},
            {"label": "B", "text": "68 kg", "is_correct": True},
            {"label": "C", "text": "70 kg", "is_correct": False},
            {"label": "D", "text": "72 kg", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - A is 20% More Than B = 150",
        "difficulty": "Medium",
        "question_text": "A is 20% more than B. If B = 150, find A.",
        "sample_answer": "A = 150 + (20% of 150) = 150 + 30 = 180.",
        "tips": "150 × 1.20.",
        "options": [
            {"label": "A", "text": "170", "is_correct": False},
            {"label": "B", "text": "175", "is_correct": False},
            {"label": "C", "text": "180", "is_correct": True},
            {"label": "D", "text": "185", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Girls Count in Class of 50 (60% Boys)",
        "difficulty": "Medium",
        "question_text": "In a class of 50 students, 60% are boys. How many girls are there?",
        "sample_answer": "Girls percentage = 100% − 60% = 40%.\nNumber of girls = 40% of 50 = 20.",
        "tips": "50 × 0.40.",
        "options": [
            {"label": "A", "text": "15", "is_correct": False},
            {"label": "B", "text": "20", "is_correct": True},
            {"label": "C", "text": "25", "is_correct": False},
            {"label": "D", "text": "30", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Profit Percentage on ₹800 to ₹920",
        "difficulty": "Medium",
        "question_text": "A shopkeeper buys an article for ₹800 and sells it for ₹920. Find the profit percentage.",
        "sample_answer": "Profit = 920 − 800 = ₹120.\nProfit percentage = (120 / 800) × 100 = 15%.",
        "tips": "(120 / 800) × 100.",
        "options": [
            {"label": "A", "text": "12%", "is_correct": False},
            {"label": "B", "text": "15%", "is_correct": True},
            {"label": "C", "text": "18%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Loss Percentage on ₹1,500 to ₹1,275",
        "difficulty": "Medium",
        "question_text": "An article bought for ₹1,500 is sold for ₹1,275. Find the loss percentage.",
        "sample_answer": "Loss = 1500 − 1275 = ₹225.\nLoss percentage = (225 / 1500) × 100 = 15%.",
        "tips": "(225 / 1500) × 100.",
        "options": [
            {"label": "A", "text": "12%", "is_correct": False},
            {"label": "B", "text": "15%", "is_correct": True},
            {"label": "C", "text": "18%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Percentage Increase from 50,000 to 57,500",
        "difficulty": "Medium",
        "question_text": "The population of a city increases from 50,000 to 57,500. Find the percentage increase.",
        "sample_answer": "Increase = 57500 − 50000 = 7500.\nPercentage increase = (7500 / 50000) × 100 = 15%.",
        "tips": "(7500 / 50000) × 100.",
        "options": [
            {"label": "A", "text": "12%", "is_correct": False},
            {"label": "B", "text": "15%", "is_correct": True},
            {"label": "C", "text": "17.5%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - 20% of 30% of 500",
        "difficulty": "Medium",
        "question_text": "What is 20% of 30% of 500?",
        "sample_answer": "30% of 500 = 150.\n20% of 150 = 30.\n(Alternatively: 0.20 × 0.30 × 500 = 0.06 × 500 = 30).",
        "tips": "0.06 × 500 = 30.",
        "options": [
            {"label": "A", "text": "20", "is_correct": False},
            {"label": "B", "text": "25", "is_correct": False},
            {"label": "C", "text": "30", "is_correct": True},
            {"label": "D", "text": "35", "is_correct": False}
        ],
        "correct_option": "C"
    },

    # QUESTIONS 16 TO 30
    {
        "title": "Percentages - Successive Increase 20% and 25%",
        "difficulty": "Hard",
        "question_text": "The price of an article is increased by 20% and then by another 25%. What is the overall percentage increase?",
        "sample_answer": "Formula: a + b + (ab / 100) = 20 + 25 + (20 × 25 / 100) = 45 + 5 = 50%.",
        "tips": "1.20 × 1.25 = 1.50.",
        "options": [
            {"label": "A", "text": "40%", "is_correct": False},
            {"label": "B", "text": "45%", "is_correct": False},
            {"label": "C", "text": "50%", "is_correct": True},
            {"label": "D", "text": "55%", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Successive Decrease 20% and 10%",
        "difficulty": "Hard",
        "question_text": "The price of an article is decreased by 20% and then by 10%. What is the overall percentage decrease?",
        "sample_answer": "Multiplier = (1 − 0.20)(1 − 0.10) = 0.80 × 0.90 = 0.72.\nOverall decrease = 100% − 72% = 28%.",
        "tips": "100 - (80 * 0.90) = 28%.",
        "options": [
            {"label": "A", "text": "26%", "is_correct": False},
            {"label": "B", "text": "28%", "is_correct": True},
            {"label": "C", "text": "30%", "is_correct": False},
            {"label": "D", "text": "32%", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Increase 25% and Decrease 20%",
        "difficulty": "Hard",
        "question_text": "A number is increased by 25% and then decreased by 20%. What is the net percentage change?",
        "sample_answer": "Multiplier = 1.25 × 0.80 = 1.00.\nNet percentage change = 0%.",
        "tips": "1.25 × 0.80 = 1.00.",
        "options": [
            {"label": "A", "text": "0%", "is_correct": True},
            {"label": "B", "text": "5% increase", "is_correct": False},
            {"label": "C", "text": "5% decrease", "is_correct": False},
            {"label": "D", "text": "10% increase", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Percentages - Two-Year Population Growth 10% and 20%",
        "difficulty": "Hard",
        "question_text": "The population of a city is 2,00,000. It increases by 10% in the first year and 20% in the second year. What is the population after two years?",
        "sample_answer": "After Year 1 = 2,00,000 × 1.10 = 2,20,000.\nAfter Year 2 = 2,20,000 × 1.20 = 2,64,000.",
        "tips": "200000 × 1.10 × 1.20.",
        "options": [
            {"label": "A", "text": "2,50,000", "is_correct": False},
            {"label": "B", "text": "2,60,000", "is_correct": False},
            {"label": "C", "text": "2,64,000", "is_correct": True},
            {"label": "D", "text": "2,70,000", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Percentage Increase in Savings",
        "difficulty": "Hard",
        "question_text": "A person's income increases by 20%, while his expenditure increases by 10%. Initially, his income is ₹40,000 and expenditure is ₹30,000. Find the percentage increase in his savings.",
        "sample_answer": "Initial savings = 40000 − 30000 = ₹10,000.\nNew income = 40000 × 1.20 = ₹48,000.\nNew expenditure = 30000 × 1.10 = ₹33,000.\nNew savings = 48000 − 33000 = ₹15,000.\nIncrease in savings = 15000 − 10000 = ₹5,000.\nPercentage increase = (5000 / 10000) × 100 = 50%.",
        "tips": "(5000 / 10000) × 100.",
        "options": [
            {"label": "A", "text": "40%", "is_correct": False},
            {"label": "B", "text": "45%", "is_correct": False},
            {"label": "C", "text": "50%", "is_correct": True},
            {"label": "D", "text": "60%", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Reverse Percentage (20% Increase to ₹1,440)",
        "difficulty": "Hard",
        "question_text": "After a 20% increase, the price of an article becomes ₹1,440. What was its original price?",
        "sample_answer": "1.20 × P = 1440 => P = 1440 / 1.20 = ₹1,200.",
        "tips": "1440 / 1.2.",
        "options": [
            {"label": "A", "text": "₹1,100", "is_correct": False},
            {"label": "B", "text": "₹1,150", "is_correct": False},
            {"label": "C", "text": "₹1,200", "is_correct": True},
            {"label": "D", "text": "₹1,250", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Marked Price from 25% Discount to ₹900",
        "difficulty": "Hard",
        "question_text": "After a 25% discount, the selling price of an article is ₹900. Find its marked price.",
        "sample_answer": "0.75 × MP = 900 => MP = 900 / 0.75 = ₹1,200.",
        "tips": "900 / 0.75.",
        "options": [
            {"label": "A", "text": "₹1,100", "is_correct": False},
            {"label": "B", "text": "₹1,150", "is_correct": False},
            {"label": "C", "text": "₹1,200", "is_correct": True},
            {"label": "D", "text": "₹1,250", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Two-Year Population Decrease 10% and 20%",
        "difficulty": "Hard",
        "question_text": "The population of a town decreases by 10% in the first year and by 20% in the second year. If the initial population was 50,000, find the population after two years.",
        "sample_answer": "After Year 1 = 50000 × 0.90 = 45000.\nAfter Year 2 = 45000 × 0.80 = 36,000.",
        "tips": "50000 × 0.90 × 0.80.",
        "options": [
            {"label": "A", "text": "35,000", "is_correct": False},
            {"label": "B", "text": "36,000", "is_correct": True},
            {"label": "C", "text": "37,000", "is_correct": False},
            {"label": "D", "text": "40,000", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - More Than to Less Than Comparison",
        "difficulty": "Hard",
        "question_text": "A's salary is 25% more than B's salary. By what percentage is B's salary less than A's salary?",
        "sample_answer": "Let B = 100 => A = 125.\nPercentage less = ((125 − 100) / 125) × 100 = (25 / 125) × 100 = 20%.",
        "tips": "[R / (100 + R)] × 100.",
        "options": [
            {"label": "A", "text": "15%", "is_correct": False},
            {"label": "B", "text": "18%", "is_correct": False},
            {"label": "C", "text": "20%", "is_correct": True},
            {"label": "D", "text": "25%", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Maximum Marks from Fail and Pass Differences",
        "difficulty": "Hard",
        "question_text": "A student scored 30% marks and failed by 24 marks. Another student scored 42% marks and obtained 48 marks more than the passing marks. Find the maximum marks.",
        "sample_answer": "Difference in percentage = 42% − 30% = 12%.\nDifference in marks = 48 − (−24) = 72.\n12% of Maximum Marks = 72 => Maximum Marks = (72 / 12) × 100 = 600.",
        "tips": "(72 / 12) × 100.",
        "options": [
            {"label": "A", "text": "500", "is_correct": False},
            {"label": "B", "text": "600", "is_correct": True},
            {"label": "C", "text": "700", "is_correct": False},
            {"label": "D", "text": "800", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Total Valid Votes in Election",
        "difficulty": "Hard",
        "question_text": "In an election, a candidate receives 55% of the valid votes and wins by 2,000 votes. Find the total number of valid votes.",
        "sample_answer": "Winner = 55%, Loser = 45%.\nMargin = 55% − 45% = 10%.\n10% of Total Votes = 2000 => Total Votes = 20,000.",
        "tips": "2000 / 0.10.",
        "options": [
            {"label": "A", "text": "15,000", "is_correct": False},
            {"label": "B", "text": "18,000", "is_correct": False},
            {"label": "C", "text": "20,000", "is_correct": True},
            {"label": "D", "text": "25,000", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Price Increase and Consumption Reduction",
        "difficulty": "Hard",
        "question_text": "The price of sugar increases by 25%. By what percentage should a family reduce its consumption so that its expenditure on sugar remains unchanged?",
        "sample_answer": "Formula: [R / (100 + R)] × 100 = [25 / (100 + 25)] × 100 = (25 / 125) × 100 = 20%.",
        "tips": "25 / 125 = 20%.",
        "options": [
            {"label": "A", "text": "15%", "is_correct": False},
            {"label": "B", "text": "20%", "is_correct": True},
            {"label": "C", "text": "25%", "is_correct": False},
            {"label": "D", "text": "30%", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Savings Increase (Income +20%, Expenditure +15%)",
        "difficulty": "Hard",
        "question_text": "A person's income is ₹50,000 and his expenditure is ₹40,000. His income increases by 20% and expenditure increases by 15%. Find the percentage increase in his savings.",
        "sample_answer": "Initial savings = 50000 − 40000 = ₹10,000.\nNew income = 50000 × 1.20 = ₹60,000.\nNew expenditure = 40000 × 1.15 = ₹46,000.\nNew savings = 60000 − 46000 = ₹14,000.\nIncrease in savings = 14000 − 10000 = ₹4,000.\nPercentage increase = (4000 / 10000) × 100 = 40%.",
        "tips": "(4000 / 10000) × 100.",
        "options": [
            {"label": "A", "text": "30%", "is_correct": False},
            {"label": "B", "text": "35%", "is_correct": False},
            {"label": "C", "text": "40%", "is_correct": True},
            {"label": "D", "text": "45%", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Percentages - Successive Discounts 20% and 10% on ₹5,000",
        "difficulty": "Hard",
        "question_text": "An article is marked at ₹5,000. Two successive discounts of 20% and 10% are offered. Find the final selling price.",
        "sample_answer": "Price after 1st discount = 5000 × 0.80 = ₹4,000.\nPrice after 2nd discount = 4000 × 0.90 = ₹3,600.",
        "tips": "5000 × 0.80 × 0.90.",
        "options": [
            {"label": "A", "text": "₹3,500", "is_correct": False},
            {"label": "B", "text": "₹3,600", "is_correct": True},
            {"label": "C", "text": "₹3,700", "is_correct": False},
            {"label": "D", "text": "₹4,000", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Percentages - Three-Year Population Variation (+20%, -10%, +25%)",
        "difficulty": "Hard",
        "question_text": "The population of a town increases by 20% in the first year, decreases by 10% in the second year, and increases by 25% in the third year. If the initial population was 80,000, what is the population after three years?",
        "sample_answer": "After Year 1 = 80000 × 1.20 = 96000.\nAfter Year 2 = 96000 × 0.90 = 86400.\nAfter Year 3 = 86400 × 1.25 = 1,08,000.",
        "tips": "80000 × 1.20 × 0.90 × 1.25.",
        "options": [
            {"label": "A", "text": "100,000", "is_correct": False},
            {"label": "B", "text": "105,000", "is_correct": False},
            {"label": "C", "text": "108,000", "is_correct": True},
            {"label": "D", "text": "110,000", "is_correct": False}
        ],
        "correct_option": "C"
    }
]

def seed_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete old Percentages questions to replace with exact 30 questions requested by user
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Percentages'")
    print("Cleared existing Percentages questions.")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'Aptitude',
            'Percentage & Interest',
            'Percentages',
            q['title'],
            q['difficulty'],
            q['question_text'],
            q['sample_answer'],
            q['tips'],
            json.dumps(q['options']),
            q['correct_option']
        ))
        
    conn.commit()
    conn.close()
    print(f"Successfully seeded {len(questions)} Percentages questions into SQLite DB!")

if __name__ == '__main__':
    seed_db()
