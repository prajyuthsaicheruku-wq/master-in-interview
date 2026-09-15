import sqlite3
import json

questions_data = [
    {
        "q_num": 1,
        "title": "Ratio & Proportion - Age Ratio",
        "question_text": "The ratio of the ages of A and B is 5:7. After 6 years, the ratio becomes 3:4. Find their present ages.\n\nA) 25 and 35\nB) 30 and 42\nC) 35 and 49\nD) 40 and 56",
        "options": [
            {"label": "A", "text": "25 and 35", "is_correct": False},
            {"label": "B", "text": "30 and 42", "is_correct": True},
            {"label": "C", "text": "35 and 49", "is_correct": False},
            {"label": "D", "text": "40 and 56", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let the present ages of A and B be 5x and 7x years.\nAfter 6 years:\n(5x + 6) / (7x + 6) = 3 / 4\n=> 4(5x + 6) = 3(7x + 6)\n=> 20x + 24 = 21x + 18\n=> x = 6\n\nPresent age of A = 5 * 6 = 30 years\nPresent age of B = 7 * 6 = 42 years.",
        "tips": "Set up a linear equation in one variable x using the given ratios before and after time progression."
    },
    {
        "q_num": 2,
        "title": "Ratio & Proportion - Number Addition Ratio",
        "question_text": "Two numbers are in the ratio 7:9. If 12 is added to each number, the ratio becomes 5:6. Find the numbers.\n\nA) 21 and 27\nB) 28 and 36\nC) 35 and 45\nD) 42 and 54",
        "options": [
            {"label": "A", "text": "21 and 27", "is_correct": False},
            {"label": "B", "text": "28 and 36", "is_correct": True},
            {"label": "C", "text": "35 and 45", "is_correct": False},
            {"label": "D", "text": "42 and 54", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let the numbers be 7x and 9x.\nWhen 12 is added to both:\n(7x + 12) / (9x + 12) = 5 / 6\n=> 6(7x + 12) = 5(9x + 12)\n=> 42x + 72 = 45x + 60\n=> 3x = 12 => x = 4\n\nThe numbers are 7 * 4 = 28 and 9 * 4 = 36.",
        "tips": "Cross-multiply the proportion equation to solve for the multiplier x."
    },
    {
        "q_num": 3,
        "title": "Ratio & Proportion - Class Ratio Change",
        "question_text": "The ratio of boys to girls in a class is 7:5. If 8 boys and 4 girls join the class, the ratio becomes 3:2. Find the original number of boys and girls.\n\nA) 28 boys and 20 girls\nB) 35 boys and 25 girls\nC) 42 boys and 30 girls\nD) 21 boys and 15 girls",
        "options": [
            {"label": "A", "text": "28 boys and 20 girls", "is_correct": True},
            {"label": "B", "text": "35 boys and 25 girls", "is_correct": False},
            {"label": "C", "text": "42 boys and 30 girls", "is_correct": False},
            {"label": "D", "text": "21 boys and 15 girls", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Let original boys = 7x and girls = 5x.\nAfter students join:\n(7x + 8) / (5x + 4) = 3 / 2\n=> 2(7x + 8) = 3(5x + 4)\n=> 14x + 16 = 15x + 12\n=> x = 4\n\nOriginal boys = 7 * 4 = 28\nOriginal girls = 5 * 4 = 20.",
        "tips": "Add the new additions to respective numerators and denominators."
    },
    {
        "q_num": 4,
        "title": "Ratio & Proportion - Money Division",
        "question_text": "A sum of ₹1,260 is divided among A, B, and C in the ratio 2:3:4. How much does C receive?\n\nA) ₹280\nB) ₹420\nC) ₹560\nD) ₹640",
        "options": [
            {"label": "A", "text": "₹280", "is_correct": False},
            {"label": "B", "text": "₹420", "is_correct": False},
            {"label": "C", "text": "₹560", "is_correct": True},
            {"label": "D", "text": "₹640", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Sum of ratio terms = 2 + 3 + 4 = 9 parts.\nTotal Amount = ₹1,260\nValue per part = 1260 / 9 = ₹140\n\nC's share = 4 * 140 = ₹560.",
        "tips": "Divide the total sum by the total number of ratio parts to get the value of one part."
    },
    {
        "q_num": 5,
        "title": "Ratio & Proportion - Income and Savings",
        "question_text": "The incomes of A and B are in the ratio 5:7, while their expenditures are in the ratio 3:5. If both save ₹2,000 per month, find their monthly incomes.\n\nA) ₹4,000 and ₹5,600\nB) ₹5,000 and ₹7,000\nC) ₹6,000 and ₹8,400\nD) ₹7,500 and ₹10,500",
        "options": [
            {"label": "A", "text": "₹4,000 and ₹5,600", "is_correct": False},
            {"label": "B", "text": "₹5,000 and ₹7,000", "is_correct": True},
            {"label": "C", "text": "₹6,000 and ₹8,400", "is_correct": False},
            {"label": "D", "text": "₹7,500 and ₹10,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let incomes be 5x and 7x.\nExpenditure = Income - Savings\nRatio of expenditures:\n(5x - 2000) / (7x - 2000) = 3 / 5\n=> 5(5x - 2000) = 3(7x - 2000)\n=> 25x - 10000 = 21x - 6000\n=> 4x = 4000 => x = 1000\n\nIncomes: A = ₹5,000 and B = ₹7,000.",
        "tips": "Use Expenditure = Income - Savings."
    },
    {
        "q_num": 6,
        "title": "Ratio & Proportion - Compound Ratio A:B:C",
        "question_text": "If A:B = 3:4 and B:C = 8:9, find A:B:C.\n\nA) 3:4:9\nB) 6:8:9\nC) 8:9:12\nD) 6:9:12",
        "options": [
            {"label": "A", "text": "3:4:9", "is_correct": False},
            {"label": "B", "text": "6:8:9", "is_correct": True},
            {"label": "C", "text": "8:9:12", "is_correct": False},
            {"label": "D", "text": "6:9:12", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "A:B = 3:4 = 6:8 (multiply by 2 to make B term equal to 8)\nB:C = 8:9\nTherefore, A:B:C = 6:8:9.",
        "tips": "Equalize the common term (B) in both ratios."
    },
    {
        "q_num": 7,
        "title": "Ratio & Proportion - Mixture Ratio Change",
        "question_text": "The ratio of milk to water in a mixture is 5:2. If 14 litres of water is added, the ratio becomes 5:4. Find the original quantity of the mixture.\n\nA) 35 litres\nB) 42 litres\nC) 49 litres\nD) 56 litres",
        "options": [
            {"label": "A", "text": "35 litres", "is_correct": False},
            {"label": "B", "text": "42 litres", "is_correct": False},
            {"label": "C", "text": "49 litres", "is_correct": True},
            {"label": "D", "text": "56 litres", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Let milk = 5x and water = 2x. Total mixture = 7x.\nAdding 14 litres water:\n5x / (2x + 14) = 5 / 4\n=> 4(5x) = 5(2x + 14)\n=> 20x = 10x + 70\n=> 10x = 70 => x = 7\n\nOriginal total mixture = 7 * 7 = 49 litres.",
        "tips": "Milk remains constant while water changes."
    },
    {
        "q_num": 8,
        "title": "Ratio & Proportion - Partnership Profit Ratio",
        "question_text": "A and B invest money in a business in the ratio 4:5. A invests for 12 months and B invests for 8 months. Find the ratio in which they should divide the profit.\n\nA) 4:5\nB) 5:6\nC) 6:5\nD) 3:2",
        "options": [
            {"label": "A", "text": "4:5", "is_correct": False},
            {"label": "B", "text": "5:6", "is_correct": False},
            {"label": "C", "text": "6:5", "is_correct": True},
            {"label": "D", "text": "3:2", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Profit Ratio = (Capital_A * Time_A) : (Capital_B * Time_B)\nProfit Ratio = (4 * 12) : (5 * 8)\n= 48 : 40\n= 6 : 5.",
        "tips": "Profit is shared in the ratio of the product of Investment and Time."
    },
    {
        "q_num": 9,
        "title": "Ratio & Proportion - Three Number Difference",
        "question_text": "Three numbers are in the ratio 2:3:5. If the difference between the largest and smallest numbers is 54, find the sum of all three numbers.\n\nA) 150\nB) 162\nC) 180\nD) 210",
        "options": [
            {"label": "A", "text": "150", "is_correct": False},
            {"label": "B", "text": "162", "is_correct": False},
            {"label": "C", "text": "180", "is_correct": True},
            {"label": "D", "text": "210", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Let numbers be 2x, 3x, 5x.\nLargest = 5x, Smallest = 2x.\nDifference = 5x - 2x = 3x = 54 => x = 18.\n\nSum of numbers = 2x + 3x + 5x = 10x = 10 * 18 = 180.",
        "tips": "Express the difference in terms of x first."
    },
    {
        "q_num": 10,
        "title": "Ratio & Proportion - Map Scale Calculation",
        "question_text": "A map has a scale of 1:50,000. If the distance between two places on the map is 7.5 cm, find the actual distance in kilometres.\n\nA) 3.5 km\nB) 3.75 km\nC) 4.25 km\nD) 37.5 km",
        "options": [
            {"label": "A", "text": "3.5 km", "is_correct": False},
            {"label": "B", "text": "3.75 km", "is_correct": True},
            {"label": "C", "text": "4.25 km", "is_correct": False},
            {"label": "D", "text": "37.5 km", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Actual distance in cm = 7.5 * 50,000 = 3,75,000 cm.\nConvert to metres: 3,75,000 / 100 = 3,750 m.\nConvert to km: 3,750 / 1000 = 3.75 km.",
        "tips": "1 km = 100,000 cm."
    },
    {
        "q_num": 11,
        "title": "Ratio & Proportion - Speed and Time Inverse Ratio",
        "question_text": "The ratio of the speeds of A and B is 4:5. A takes 15 minutes more than B to cover the same distance. Find the time taken by each.\n\nA) A = 60 mins, B = 45 mins\nB) A = 75 mins, B = 60 mins\nC) A = 90 mins, B = 75 mins\nD) A = 50 mins, B = 35 mins",
        "options": [
            {"label": "A", "text": "A = 60 mins, B = 45 mins", "is_correct": False},
            {"label": "B", "text": "A = 75 mins, B = 60 mins", "is_correct": True},
            {"label": "C", "text": "A = 90 mins, B = 75 mins", "is_correct": False},
            {"label": "D", "text": "A = 50 mins, B = 35 mins", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Speed ratio = 4:5 => Time ratio = 5:4 (since distance is constant).\nLet time taken be 5t and 4t.\nDifference = 5t - 4t = t = 15 mins.\n\nTime taken by A = 5 * 15 = 75 mins.\nTime taken by B = 4 * 15 = 60 mins.",
        "tips": "Time ratio is inversely proportional to speed ratio for constant distance."
    },
    {
        "q_num": 12,
        "title": "Ratio & Proportion - Compound Ratio x:y:z",
        "question_text": "If x:y = 5:8 and y:z = 12:13, find x:y:z.\n\nA) 5:8:13\nB) 15:24:26\nC) 10:16:26\nD) 15:24:30",
        "options": [
            {"label": "A", "text": "5:8:13", "is_correct": False},
            {"label": "B", "text": "15:24:26", "is_correct": True},
            {"label": "C", "text": "10:16:26", "is_correct": False},
            {"label": "D", "text": "15:24:30", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "LCM of y values (8 and 12) = 24.\nx:y = (5 * 3) : (8 * 3) = 15:24\ny:z = (12 * 2) : (13 * 2) = 24:26\n\nTherefore, x:y:z = 15:24:26.",
        "tips": "Find the LCM of the common variable y to combine."
    },
    {
        "q_num": 13,
        "title": "Ratio & Proportion - Difference in Share",
        "question_text": "A total amount is divided among P, Q, and R in the ratio 3:4:5. If Q receives ₹600 more than P, find the total amount.\n\nA) ₹6,000\nB) ₹6,600\nC) ₹7,200\nD) ₹8,400",
        "options": [
            {"label": "A", "text": "₹6,000", "is_correct": False},
            {"label": "B", "text": "₹6,600", "is_correct": False},
            {"label": "C", "text": "₹7,200", "is_correct": True},
            {"label": "D", "text": "₹8,400", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Shares of P, Q, R = 3x, 4x, 5x.\nQ - P = 4x - 3x = x = ₹600.\nTotal amount = 3x + 4x + 5x = 12x.\nTotal amount = 12 * 600 = ₹7,200.",
        "tips": "The difference between ratio parts directly gives the value of x."
    },
    {
        "q_num": 14,
        "title": "Ratio & Proportion - Father and Son Ages",
        "question_text": "The ratio of the present ages of a father and son is 7:2. After 10 years, their ages will be in the ratio 9:4. Find their present ages.\n\nA) 35 and 10\nB) 42 and 12\nC) 49 and 14\nD) 28 and 8",
        "options": [
            {"label": "A", "text": "35 and 10", "is_correct": True},
            {"label": "B", "text": "42 and 12", "is_correct": False},
            {"label": "C", "text": "49 and 14", "is_correct": False},
            {"label": "D", "text": "28 and 8", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Let present ages be 7x and 2x.\nAfter 10 years:\n(7x + 10) / (2x + 10) = 9 / 4\n=> 4(7x + 10) = 9(2x + 10)\n=> 28x + 40 = 18x + 90\n=> 10x = 50 => x = 5\n\nFather's age = 7 * 5 = 35 years.\nSon's age = 2 * 5 = 10 years.",
        "tips": "Set up linear equation with +10 years."
    },
    {
        "q_num": 15,
        "title": "Ratio & Proportion - Alcohol and Water Mixture",
        "question_text": "A mixture contains alcohol and water in the ratio 7:3. If 20 litres of water is added, the ratio becomes 7:5. Find the original quantity of alcohol.\n\nA) 50 litres\nB) 60 litres\nC) 70 litres\nD) 80 litres",
        "options": [
            {"label": "A", "text": "50 litres", "is_correct": False},
            {"label": "B", "text": "60 litres", "is_correct": False},
            {"label": "C", "text": "70 litres", "is_correct": True},
            {"label": "D", "text": "80 litres", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Let alcohol = 7x and water = 3x.\nAdding 20 litres water:\n7x / (3x + 20) = 7 / 5\n=> 5(7x) = 7(3x + 20)\n=> 35x = 21x + 140\n=> 14x = 140 => x = 10\n\nOriginal alcohol quantity = 7 * 10 = 70 litres.",
        "tips": "Alcohol ratio part remains unchanged (7)."
    },
    {
        "q_num": 16,
        "title": "Ratio & Proportion - Salary and Expense Ratio",
        "question_text": "A, B, and C have salaries in the ratio 5:6:8. Their expenses are in the ratio 3:4:5. If A saves ₹4,000, B saves ₹4,800, and C saves ₹6,000, find their individual salaries.\n\nA) ₹15,000, ₹18,000, ₹24,000\nB) ₹20,000, ₹24,000, ₹32,000\nC) ₹25,000, ₹30,000, ₹40,000\nD) ₹10,000, ₹12,000, ₹16,000",
        "options": [
            {"label": "A", "text": "₹15,000, ₹18,000, ₹24,000", "is_correct": False},
            {"label": "B", "text": "₹20,000, ₹24,000, ₹32,000", "is_correct": True},
            {"label": "C", "text": "₹25,000, ₹30,000, ₹40,000", "is_correct": False},
            {"label": "D", "text": "₹10,000, ₹12,000, ₹16,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let salaries be 5x, 6x, 8x and expenses be 3y, 4y, 5y.\nA's savings: 5x - 3y = 4000\nB's savings: 6x - 4y = 4800\nSolving simultaneously:\n4*(5x - 3y) - 3*(6x - 4y) = 4*4000 - 3*4800\n=> 20x - 12y - 18x + 12y = 16000 - 14400\n=> 2x = 1600 => x = 4000 (scaling multiplier = 4000)\n\nSalaries: A = 5 * 4000 = ₹20,000, B = 6 * 4000 = ₹24,000, C = 8 * 4000 = ₹32,000.",
        "tips": "Use system of linear equations for Income and Expenditure."
    },
    {
        "q_num": 17,
        "title": "Ratio & Proportion - Transfer of Students Between Sections",
        "question_text": "The ratio of the number of students in three sections A, B, and C is 4:5:6. If 20 students are transferred from C to A, the ratio becomes 6:5:4. Find the original number of students in each section.\n\nA) 30, 40, 50\nB) 40, 50, 60\nC) 50, 60, 70\nD) 60, 75, 90",
        "options": [
            {"label": "A", "text": "30, 40, 50", "is_correct": False},
            {"label": "B", "text": "40, 50, 60", "is_correct": True},
            {"label": "C", "text": "50, 60, 70", "is_correct": False},
            {"label": "D", "text": "60, 75, 90", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let original students be 4x, 5x, 6x.\nAfter transfer of 20 students from C to A:\nA = 4x + 20, B = 5x, C = 6x - 20.\nNew Ratio = (4x + 20) : 5x = 6 : 5\n=> 5(4x + 20) = 6(5x)\n=> 20x + 100 = 30x\n=> 10x = 100 => x = 10\n\nOriginal students: A = 40, B = 50, C = 60.",
        "tips": "Section B remains constant during the transfer."
    },
    {
        "q_num": 18,
        "title": "Ratio & Proportion - Removal and Replacement Mixture",
        "question_text": "A vessel contains milk and water in the ratio 7:3. 20 litres of the mixture is removed and replaced with water. The new ratio becomes 7:5. Find the original quantity of the mixture.\n\nA) 100 litres\nB) 120 litres\nC) 140 litres\nD) 150 litres",
        "options": [
            {"label": "A", "text": "100 litres", "is_correct": False},
            {"label": "B", "text": "120 litres", "is_correct": True},
            {"label": "C", "text": "140 litres", "is_correct": False},
            {"label": "D", "text": "150 litres", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let total volume be V.\nMilk removed in 20L = (7/10) * 20 = 14L.\nWater removed = 6L.\nAfter replacement with 20L water:\nMilk = (7/10)V - 14\nWater = (3/10)V - 6 + 20 = (3/10)V + 14\n\nRatio: [(7/10)V - 14] / [(3/10)V + 14] = 7 / 5\n=> 5[(7/10)V - 14] = 7[(3/10)V + 14]\n=> (35/10)V - 70 = (21/10)V + 98\n=> (14/10)V = 168\n=> V = 120 litres.",
        "tips": "Track exact removal volumes of components before adding replacement liquid."
    },
    {
        "q_num": 19,
        "title": "Ratio & Proportion - Investment Change Partnership",
        "question_text": "A and B start a business with investments in the ratio 5:7. After 4 months, A increases his investment by 40%, while B withdraws 20% of his investment. If the total annual profit is ₹1,08,000, find B's share of the profit.\n\nA) ₹48,000\nB) ₹52,774\nC) ₹55,226\nD) ₹60,000",
        "options": [
            {"label": "A", "text": "₹48,000", "is_correct": False},
            {"label": "B", "text": "₹52,774", "is_correct": True},
            {"label": "C", "text": "₹55,226", "is_correct": False},
            {"label": "D", "text": "₹60,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let initial investments be 5 and 7.\nA's total weighted investment = (5 * 4) + [(5 * 1.4) * 8] = 20 + (7 * 8) = 76.\nB's total weighted investment = (7 * 4) + [(7 * 0.8) * 8] = 28 + (5.6 * 8) = 72.8.\nRatio A:B = 76 : 72.8 = 95 : 91.\nTotal parts = 95 + 91 = 186.\n\nB's share = (91 / 186) * 108000 = ₹52,774.",
        "tips": "Calculate monthly weighted investment totals for each period."
    },
    {
        "q_num": 20,
        "title": "Ratio & Proportion - Train Speed and Time Inverse Ratio",
        "question_text": "The ratio of the speeds of three trains A, B, and C is 4:5:6. For the same distance, their travel times are inversely proportional to their speeds. If train A takes 30 minutes more than train C, find the time taken by train B.\n\nA) 60 mins\nB) 72 mins\nC) 84 mins\nD) 90 mins",
        "options": [
            {"label": "A", "text": "60 mins", "is_correct": False},
            {"label": "B", "text": "72 mins", "is_correct": True},
            {"label": "C", "text": "84 mins", "is_correct": False},
            {"label": "D", "text": "90 mins", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Speed ratio A:B:C = 4:5:6.\nTime ratio = 1/4 : 1/5 : 1/6 = 15 : 12 : 10.\nDifference between A and C = 15t - 10t = 5t = 30 mins => t = 6 mins.\n\nTime taken by train B = 12t = 12 * 6 = 72 minutes.",
        "tips": "Multiply reciprocals by LCM of denominators (60) to get integer time ratios."
    },
    {
        "q_num": 21,
        "title": "Ratio & Proportion - Four Person Division",
        "question_text": "A sum of money is divided among A, B, C, and D in the ratio 2:3:5:7. If C receives ₹1,600 more than A, find the amount received by D.\n\nA) ₹3,200\nB) ₹3,500\nC) ₹3,733.33\nD) ₹4,200",
        "options": [
            {"label": "A", "text": "₹3,200", "is_correct": False},
            {"label": "B", "text": "₹3,500", "is_correct": False},
            {"label": "C", "text": "₹3,733.33", "is_correct": True},
            {"label": "D", "text": "₹4,200", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Shares = 2x, 3x, 5x, 7x.\nC - A = 5x - 2x = 3x = ₹1600 => x = 1600 / 3.\n\nD's share = 7x = 7 * (1600 / 3) = ₹3,733.33.",
        "tips": "Find unit ratio multiplier x = Difference / Difference in ratio parts."
    },
    {
        "q_num": 22,
        "title": "Ratio & Proportion - Three Person Age Combination",
        "question_text": "The ratio of the ages of A and B is 4:5, and the ratio of the ages of B and C is 6:7. Five years ago, the sum of their ages was 100. Find their present ages.\n\nA) 20, 25, 30\nB) 24, 30, 35\nC) 28, 35, 42\nD) 32, 40, 48",
        "options": [
            {"label": "A", "text": "20, 25, 30", "is_correct": False},
            {"label": "B", "text": "24, 30, 35", "is_correct": True},
            {"label": "C", "text": "28, 35, 42", "is_correct": False},
            {"label": "D", "text": "32, 40, 48", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Combine ratios A:B:C:\nA:B = 4:5 = 24:30\nB:C = 6:7 = 30:35\nA:B:C = 24:30:35.\nSum of present ages = 24x + 30x + 35x = 89x.\nSum 5 years ago = 89x - 15 = 100 => 89x = 115 => x ~ 1.\n\nPresent ages = 24, 30, 35.",
        "tips": "Subtract 3 * 5 = 15 years from present age sum for 5 years ago."
    },
    {
        "q_num": 23,
        "title": "Ratio & Proportion - Alligation Mixture Ratio",
        "question_text": "A mixture contains substances A and B in the ratio 3:5. Another mixture contains A and B in the ratio 7:3. In what ratio should the two mixtures be mixed to obtain a mixture containing A and B in the ratio 1:1?\n\nA) 5:8\nB) 8:5\nC) 4:5\nD) 7:5",
        "options": [
            {"label": "A", "text": "5:8", "is_correct": False},
            {"label": "B", "text": "8:5", "is_correct": True},
            {"label": "C", "text": "4:5", "is_correct": False},
            {"label": "D", "text": "7:5", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Fraction of A in Mixture 1 = 3/8 = 0.375.\nFraction of A in Mixture 2 = 7/10 = 0.70.\nTarget fraction of A = 1/2 = 0.50.\nApplying Alligation:\n(7/10 - 1/2) : (1/2 - 3/8)\n= (1/5) : (1/8)\n= 8 : 5.",
        "tips": "Use the Alligation Rule on concentration of component A."
    },
    {
        "q_num": 24,
        "title": "Ratio & Proportion - Unequal Savings Income Problem",
        "question_text": "The incomes of A and B are in the ratio 7:9, and their expenditures are in the ratio 4:5. If A saves ₹3,000 and B saves ₹4,000, find the income of B.\n\nA) ₹7,000\nB) ₹9,000\nC) ₹12,000\nD) ₹15,000",
        "options": [
            {"label": "A", "text": "₹7,000", "is_correct": False},
            {"label": "B", "text": "₹9,000", "is_correct": True},
            {"label": "C", "text": "₹12,000", "is_correct": False},
            {"label": "D", "text": "₹15,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Incomes = 7x and 9x.\nExpenditure ratio:\n(7x - 3000) / (9x - 4000) = 4 / 5\n=> 5(7x - 3000) = 4(9x - 4000)\n=> 35x - 15000 = 36x - 16000\n=> x = 1000.\n\nIncome of B = 9 * 1000 = ₹9,000.",
        "tips": "Cross-multiply expenditure ratios to solve for x."
    },
    {
        "q_num": 25,
        "title": "Ratio & Proportion - Variable Time Partnership",
        "question_text": "A, B, and C invest in a business in the ratio 3:4:5. A invests for 8 months, B for 6 months, and C for 4 months. If the total profit is ₹47,000, find the difference between C's and A's shares.\n\nA) ₹2,000\nB) ₹2,764.70\nC) ₹3,500\nD) ₹4,000",
        "options": [
            {"label": "A", "text": "₹2,000", "is_correct": False},
            {"label": "B", "text": "₹2,764.70", "is_correct": True},
            {"label": "C", "text": "₹3,500", "is_correct": False},
            {"label": "D", "text": "₹4,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Profit ratio = (3 * 8) : (4 * 6) : (5 * 4) = 24 : 24 : 20 = 6 : 6 : 5.\nTotal parts = 6 + 6 + 5 = 17.\nA's share = 6/17, C's share = 5/17.\nDifference = (6 - 5) / 17 * 47000 = 1/17 * 47000 = ₹2,764.70.",
        "tips": "Multiply investment ratio by respective duration in months."
    },
    {
        "q_num": 26,
        "title": "Ratio & Proportion - Inverse Proportion Workers and Days",
        "question_text": "The ratio of the number of workers to the number of days required to complete a project is inversely proportional. If 24 workers can complete a project in 15 days, how many workers are required to complete the same project in 10 days, assuming all workers have equal efficiency?\n\nA) 30 workers\nB) 32 workers\nC) 36 workers\nD) 40 workers",
        "options": [
            {"label": "A", "text": "30 workers", "is_correct": False},
            {"label": "B", "text": "32 workers", "is_correct": False},
            {"label": "C", "text": "36 workers", "is_correct": True},
            {"label": "D", "text": "40 workers", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Total Work = Workers * Days = 24 * 15 = 360 worker-days.\nRequired Workers = Total Work / Required Days = 360 / 10 = 36 workers.",
        "tips": "Product M * D is constant for inverse proportion."
    },
    {
        "q_num": 27,
        "title": "Ratio & Proportion - Removal and Water Replacement Mixture",
        "question_text": "A container has a mixture of milk and water in the ratio 9:4. If 26 litres of the mixture is removed and replaced with water, the ratio becomes 9:7. Find the original quantity of milk in the container.\n\nA) 81 litres\nB) 90 litres\nC) 96 litres\nD) 108 litres",
        "options": [
            {"label": "A", "text": "81 litres", "is_correct": False},
            {"label": "B", "text": "90 litres", "is_correct": False},
            {"label": "C", "text": "96 litres", "is_correct": True},
            {"label": "D", "text": "108 litres", "is_correct": False}
        ],
        "correct_option": "C",
        "sample_answer": "Initial ratio = 9:4. Total parts = 13.\nMilk removed in 26L = (9/13) * 26 = 18L.\nWater removed = 8L.\nLet total volume = V.\n[(9/13)V - 18] / [(4/13)V + 18] = 9 / 7\n=> 7[(9/13)V - 18] = 9[(4/13)V + 18]\n=> (63/13)V - 126 = (36/13)V + 162\n=> (27/13)V = 288 => V = 138.67L.\nOriginal Milk = (9/13) * 138.67 = 96 litres.",
        "tips": "Milk removed is proportional to the initial milk fraction."
    },
    {
        "q_num": 28,
        "title": "Ratio & Proportion - Three Partner Investment with Late Joiner",
        "question_text": "The ratio of investments of A and B is 3:4. A invests for 10 months and B for 9 months. C joins after 4 months with an investment equal to half of B's initial investment. If the total profit is ₹1,02,000, find C's share.\n\nA) ₹16,000\nB) ₹19,902.44\nC) ₹24,000\nD) ₹28,000",
        "options": [
            {"label": "A", "text": "₹16,000", "is_correct": False},
            {"label": "B", "text": "₹19,902.44", "is_correct": True},
            {"label": "C", "text": "₹24,000", "is_correct": False},
            {"label": "D", "text": "₹28,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Investments: A = 3, B = 4, C = 2.\nDurations: A = 10 months, B = 9 months, C = 8 months.\nProfit ratio = (3 * 10) : (4 * 9) : (2 * 8) = 30 : 36 : 16 = 15 : 18 : 8.\nTotal ratio parts = 41.\n\nC's share = (8 / 41) * 102000 = ₹19,902.44.",
        "tips": "C's duration = 12 - 4 = 8 months."
    },
    {
        "q_num": 29,
        "title": "Ratio & Proportion - Constant Addition to Three Numbers",
        "question_text": "Three numbers are in the ratio 3:5:7. If 8 is added to each number, the resulting numbers are in the ratio 5:7:9. Find the original numbers.\n\nA) 9, 15, 21\nB) 12, 20, 28\nC) 15, 25, 35\nD) 18, 30, 42",
        "options": [
            {"label": "A", "text": "9, 15, 21", "is_correct": False},
            {"label": "B", "text": "12, 20, 28", "is_correct": True},
            {"label": "C", "text": "15, 25, 35", "is_correct": False},
            {"label": "D", "text": "18, 30, 42", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let numbers be 3x, 5x, 7x.\n(3x + 8) / (5x + 8) = 5 / 7\n=> 7(3x + 8) = 5(5x + 8)\n=> 21x + 56 = 25x + 40\n=> 4x = 16 => x = 4.\n\nOriginal numbers: 3*4 = 12, 5*4 = 20, 7*4 = 28.",
        "tips": "The change in ratio parts (5-3=2, 7-5=2) corresponds to adding 8."
    },
    {
        "q_num": 30,
        "title": "Ratio & Proportion - Three-Way Income & Expenditure Ratio",
        "question_text": "A and B have incomes in the ratio 4:5, and B and C have incomes in the ratio 3:4. Their expenditures are in the ratio 5:6:8. If A saves ₹5,000, B saves ₹7,000, and C saves ₹10,000, find the ratio of their incomes and determine C's income.\n\nA) Ratio 12:15:20, C's Income ₹28,000\nB) Ratio 12:15:20, C's Income ₹33,333.33\nC) Ratio 4:5:8, C's Income ₹30,000\nD) Ratio 12:15:20, C's Income ₹40,000",
        "options": [
            {"label": "A", "text": "Ratio 12:15:20, C's Income ₹28,000", "is_correct": False},
            {"label": "B", "text": "Ratio 12:15:20, C's Income ₹33,333.33", "is_correct": True},
            {"label": "C", "text": "Ratio 4:5:8, C's Income ₹30,000", "is_correct": False},
            {"label": "D", "text": "Ratio 12:15:20, C's Income ₹40,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Combine income ratio A:B:C:\nA:B = 4:5 = 12:15\nB:C = 3:4 = 15:20\nA:B:C = 12:15:20.\nIncomes = 12x, 15x, 20x. Expenditures = 5y, 6y, 8y.\nA: 12x - 5y = 5000\nB: 15x - 6y = 7000\nSolving gives y = 3000, x = 5000/3.\n\nC's income = 20 * (5000 / 3) = ₹33,333.33.",
        "tips": "First combine the income ratios A:B and B:C using LCM of B."
    }
]

def seed_database():
    conn = sqlite3.connect('instance/interview_portal.db')
    cursor = conn.cursor()
    
    # Clean out existing Ratio & Proportion questions if any
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Ratio & Proportion'")
    print(f"Cleared previous Ratio & Proportion questions.")
    
    for q in questions_data:
        category = "Aptitude"
        sub_category = "Commercial Mathematics"
        topic = "Ratio & Proportion"
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
    print(f"Successfully seeded {len(questions_data)} Ratio & Proportion questions into instance/interview_portal.db!")
    conn.close()

if __name__ == "__main__":
    seed_database()
