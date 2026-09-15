import sqlite3
import json

questions_data = [
    {
        "q_num": 1,
        "title": "Profit & Loss - Profit Percentage Calculation",
        "question_text": "A shopkeeper buys an item for ₹800 and sells it for ₹920. Find the profit percentage.\n\nA) 12%\nB) 15%\nC) 18%\nD) 20%",
        "options": [
            {"label": "A", "text": "12%", "is_correct": False},
            {"label": "B", "text": "15%", "is_correct": True},
            {"label": "C", "text": "18%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "CP = ₹800, SP = ₹920\nProfit = SP - CP = 920 - 800 = ₹120\nProfit % = (Profit / CP) * 100\n= (120 / 800) * 100 = 15%.",
        "tips": "Profit percentage is always calculated on the Cost Price (CP)."
    },
    {
        "q_num": 2,
        "title": "Profit & Loss - CP from SP and Loss %",
        "question_text": "A trader sells a product for ₹1,350 at a loss of 10%. Find the cost price.\n\nA) ₹1,450\nB) ₹1,500\nC) ₹1,550\nD) ₹1,600",
        "options": [
            {"label": "A", "text": "₹1,450", "is_correct": False},
            {"label": "B", "text": "₹1,500", "is_correct": True},
            {"label": "C", "text": "₹1,550", "is_correct": False},
            {"label": "D", "text": "₹1,600", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹1,350, Loss = 10%\nSP = CP * (100 - Loss%)/100\n=> 1350 = CP * (90 / 100)\n=> CP = (1350 * 100) / 90 = ₹1,500.",
        "tips": "CP = SP / (1 - Loss_decimal)."
    },
    {
        "q_num": 3,
        "title": "Profit & Loss - CP from SP and Profit %",
        "question_text": "An article is sold for ₹2,400 with a profit of 20%. Find the cost price.\n\nA) ₹1,800\nB) ₹2,000\nC) ₹2,100\nD) ₹2,200",
        "options": [
            {"label": "A", "text": "₹1,800", "is_correct": False},
            {"label": "B", "text": "₹2,000", "is_correct": True},
            {"label": "C", "text": "₹2,100", "is_correct": False},
            {"label": "D", "text": "₹2,200", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹2,400, Profit = 20%\nSP = CP * (100 + Profit%)/100\n=> 2400 = CP * (120 / 100)\n=> CP = (2400 * 100) / 120 = ₹2,000.",
        "tips": "CP = SP / (1 + Profit_decimal)."
    },
    {
        "q_num": 4,
        "title": "Profit & Loss - Marked Price, Discount & Profit %",
        "question_text": "A shopkeeper marks an item at ₹1,500 and gives a discount of 10%. If the cost price is ₹1,200, find the profit percentage.\n\nA) 10%\nB) 12.5%\nC) 15%\nD) 17.5%",
        "options": [
            {"label": "A", "text": "10%", "is_correct": False},
            {"label": "B", "text": "12.5%", "is_correct": True},
            {"label": "C", "text": "15%", "is_correct": False},
            {"label": "D", "text": "17.5%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹1,500, Discount = 10%\nSelling Price = 1500 * (90/100) = ₹1,350.\nCP = ₹1,200\nProfit = 1350 - 1200 = ₹150.\nProfit % = (150 / 1200) * 100 = 12.5%.",
        "tips": "Discount is calculated on Marked Price (MP), Profit % on Cost Price (CP)."
    },
    {
        "q_num": 5,
        "title": "Profit & Loss - SP from CP and Loss %",
        "question_text": "A product is sold at a loss of 15%. If the cost price is ₹2,000, find the selling price.\n\nA) ₹1,650\nB) ₹1,700\nC) ₹1,750\nD) ₹1,800",
        "options": [
            {"label": "A", "text": "₹1,650", "is_correct": False},
            {"label": "B", "text": "₹1,700", "is_correct": True},
            {"label": "C", "text": "₹1,750", "is_correct": False},
            {"label": "D", "text": "₹1,800", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "CP = ₹2,000, Loss = 15%\nSP = CP * (1 - 0.15)\n= 2000 * 0.85 = ₹1,700.",
        "tips": "SP = CP * (100 - Loss%) / 100."
    },
    {
        "q_num": 6,
        "title": "Profit & Loss - CP from SP and 25% Profit",
        "question_text": "A trader earns a profit of 25% by selling an article for ₹3,750. Find the cost price.\n\nA) ₹2,800\nB) ₹3,000\nC) ₹3,200\nD) ₹3,400",
        "options": [
            {"label": "A", "text": "₹2,800", "is_correct": False},
            {"label": "B", "text": "₹3,000", "is_correct": True},
            {"label": "C", "text": "₹3,200", "is_correct": False},
            {"label": "D", "text": "₹3,400", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹3,750, Profit = 25%\nCP = 3750 / 1.25 = ₹3,000.",
        "tips": "25% profit multiplier is 1.25."
    },
    {
        "q_num": 7,
        "title": "Profit & Loss - CP from SP and 12% Loss",
        "question_text": "An item is sold for ₹1,760 at a loss of 12%. Find its cost price.\n\nA) ₹1,900\nB) ₹2,000\nC) ₹2,100\nD) ₹2,200",
        "options": [
            {"label": "A", "text": "₹1,900", "is_correct": False},
            {"label": "B", "text": "₹2,000", "is_correct": True},
            {"label": "C", "text": "₹2,100", "is_correct": False},
            {"label": "D", "text": "₹2,200", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹1,760, Loss = 12%\nCP = 1760 / (1 - 0.12) = 1760 / 0.88 = ₹2,000.",
        "tips": "12% loss multiplier is 0.88."
    },
    {
        "q_num": 8,
        "title": "Profit & Loss - Bulk Purchase and Individual Sale",
        "question_text": "A shopkeeper buys 50 pens for ₹500 and sells each pen for ₹12. Find the profit percentage.\n\nA) 15%\nB) 20%\nC) 25%\nD) 30%",
        "options": [
            {"label": "A", "text": "15%", "is_correct": False},
            {"label": "B", "text": "20%", "is_correct": True},
            {"label": "C", "text": "25%", "is_correct": False},
            {"label": "D", "text": "30%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "CP of 1 pen = 500 / 50 = ₹10.\nSP of 1 pen = ₹12.\nProfit per pen = 12 - 10 = ₹2.\nProfit % = (2 / 10) * 100 = 20%.",
        "tips": "Calculate cost price and selling price per single unit."
    },
    {
        "q_num": 9,
        "title": "Profit & Loss - Overhead Expenses included in Cost Price",
        "question_text": "A man purchased a bicycle for ₹8,000 and spent ₹500 on repairs. He sold it for ₹9,900. Find the profit percentage.\n\nA) 15.5%\nB) 16.47%\nC) 18.2%\nD) 20%",
        "options": [
            {"label": "A", "text": "15.5%", "is_correct": False},
            {"label": "B", "text": "16.47%", "is_correct": True},
            {"label": "C", "text": "18.2%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Effective CP = Purchase Price + Repairs = 8000 + 500 = ₹8,500.\nSP = ₹9,900.\nProfit = 9900 - 8500 = ₹1,400.\nProfit % = (1400 / 8500) * 100 = 16.47%.",
        "tips": "Always add repair/transportation overhead costs to purchase price to find total CP."
    },
    {
        "q_num": 10,
        "title": "Profit & Loss - Markup and Discount Profit %",
        "question_text": "A trader marks an article 40% above cost price and gives a discount of 20%. Find the profit percentage.\n\nA) 10%\nB) 12%\nC) 15%\nD) 20%",
        "options": [
            {"label": "A", "text": "10%", "is_correct": False},
            {"label": "B", "text": "12%", "is_correct": True},
            {"label": "C", "text": "15%", "is_correct": False},
            {"label": "D", "text": "20%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100.\nMP = 100 + 40% = 140.\nDiscount = 20% on MP = 140 * 0.20 = 28.\nSP = 140 - 28 = 112.\nNet Profit % = 112 - 100 = 12%.",
        "tips": "Net % Change Formula = Markup - Discount - (Markup * Discount / 100)."
    },
    {
        "q_num": 11,
        "title": "Profit & Loss - Profit % Increase with SP Increase",
        "question_text": "An article is sold at 10% profit. If the selling price is increased by ₹120, the profit becomes 20%. Find the cost price.\n\nA) ₹1,000\nB) ₹1,200\nC) ₹1,400\nD) ₹1,500",
        "options": [
            {"label": "A", "text": "₹1,000", "is_correct": False},
            {"label": "B", "text": "₹1,200", "is_correct": True},
            {"label": "C", "text": "₹1,400", "is_correct": False},
            {"label": "D", "text": "₹1,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Difference in profit percentage = 20% - 10% = 10%.\n10% of CP = ₹120.\nCP = (120 * 100) / 10 = ₹1,200.",
        "tips": "The change in SP equals the difference in percentage of CP."
    },
    {
        "q_num": 12,
        "title": "Profit & Loss - Successive Discounts",
        "question_text": "A seller gives two successive discounts of 10% and 20% on a marked price of ₹2,500. Find the final selling price.\n\nA) ₹1,750\nB) ₹1,800\nC) ₹1,850\nD) ₹1,900",
        "options": [
            {"label": "A", "text": "₹1,750", "is_correct": False},
            {"label": "B", "text": "₹1,800", "is_correct": True},
            {"label": "C", "text": "₹1,850", "is_correct": False},
            {"label": "D", "text": "₹1,900", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "MP = ₹2,500.\nPrice after 1st discount (10%) = 2500 * 0.90 = ₹2,250.\nPrice after 2nd discount (20%) = 2250 * 0.80 = ₹1,800.",
        "tips": "Final SP = MP * (1 - d1) * (1 - d2)."
    },
    {
        "q_num": 13,
        "title": "Profit & Loss - Price per kg and Gain %",
        "question_text": "A shopkeeper sells sugar at ₹54 per kg and gains 20%. Find the cost price per kg.\n\nA) ₹42\nB) ₹45\nC) ₹48\nD) ₹50",
        "options": [
            {"label": "A", "text": "₹42", "is_correct": False},
            {"label": "B", "text": "₹45", "is_correct": True},
            {"label": "C", "text": "₹48", "is_correct": False},
            {"label": "D", "text": "₹50", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹54, Gain = 20%\nCP = SP / 1.20 = 54 / 1.20 = ₹45 per kg.",
        "tips": "Divide SP by 1.20 to reverse a 20% gain."
    },
    {
        "q_num": 14,
        "title": "Profit & Loss - Watch Loss Calculation",
        "question_text": "A trader sells a watch for ₹2,160 and incurs a loss of 10%. Find the cost price.\n\nA) ₹2,300\nB) ₹2,400\nC) ₹2,500\nD) ₹2,600",
        "options": [
            {"label": "A", "text": "₹2,300", "is_correct": False},
            {"label": "B", "text": "₹2,400", "is_correct": True},
            {"label": "C", "text": "₹2,500", "is_correct": False},
            {"label": "D", "text": "₹2,600", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SP = ₹2,160, Loss = 10%\nCP = 2160 / 0.90 = ₹2,400.",
        "tips": "Divide SP by 0.90 to reverse a 10% loss."
    },
    {
        "q_num": 15,
        "title": "Profit & Loss - Cost Price Change with Constant SP",
        "question_text": "A product is sold at a profit of 15%. If the cost price increases by 20% and the selling price remains the same, find the new profit/loss percentage.\n\nA) 4.17% Loss\nB) 5% Profit\nC) 2.5% Loss\nD) 5% Loss",
        "options": [
            {"label": "A", "text": "4.17% Loss", "is_correct": True},
            {"label": "B", "text": "5% Profit", "is_correct": False},
            {"label": "C", "text": "2.5% Loss", "is_correct": False},
            {"label": "D", "text": "5% Loss", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Let initial CP = 100 => SP = 115.\nNew CP = 100 * 1.20 = 120.\nNew SP = 115 (unchanged).\nSince New CP > New SP, it is a Loss = 120 - 115 = ₹5.\nNew Loss % = (5 / 120) * 100 = 4.17% Loss.",
        "tips": "Calculate new percentage using new CP as denominator."
    },
    {
        "q_num": 16,
        "title": "Profit & Loss - Markup and Discount Net Profit %",
        "question_text": "A trader marks his goods 50% above cost price and allows a discount of 20%. Find the profit percentage.\n\nA) 15%\nB) 20%\nC) 25%\nD) 30%",
        "options": [
            {"label": "A", "text": "15%", "is_correct": False},
            {"label": "B", "text": "20%", "is_correct": True},
            {"label": "C", "text": "25%", "is_correct": False},
            {"label": "D", "text": "30%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 150.\nDiscount = 20% of 150 = 30.\nSP = 150 - 30 = 120.\nProfit % = 120 - 100 = 20%.",
        "tips": "Net % = Markup - Discount - (Markup * Discount / 100) = 50 - 20 - 10 = 20%."
    },
    {
        "q_num": 17,
        "title": "Profit & Loss - Gain Equal to Cost Price of N Articles",
        "question_text": "By selling an article for ₹3,600, a trader gains the same amount as the cost price of 20 such articles. If he sold 25 articles, find the cost price per article.\n\nA) ₹60\nB) ₹80\nC) ₹90\nD) ₹100",
        "options": [
            {"label": "A", "text": "₹60", "is_correct": False},
            {"label": "B", "text": "₹80", "is_correct": True},
            {"label": "C", "text": "₹90", "is_correct": False},
            {"label": "D", "text": "₹100", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP per article = C.\nTotal SP of 25 articles = ₹3,600.\nTotal Gain = CP of 20 articles = 20C.\nTotal SP - Total CP = Total Gain\n=> 3600 - 25C = 20C\n=> 45C = 3600 => C = ₹80 per article.",
        "tips": "Equate Total SP - Total CP to given Gain."
    },
    {
        "q_num": 18,
        "title": "Profit & Loss - Same SP with Equal Gain and Loss %",
        "question_text": "A shopkeeper sells two articles for ₹1,000 each. On one he gains 20% and on the other he loses 20%. Find the overall profit or loss percentage.\n\nA) 4% Profit\nB) 4% Loss\nC) 2% Loss\nD) No profit no loss",
        "options": [
            {"label": "A", "text": "4% Profit", "is_correct": False},
            {"label": "B", "text": "4% Loss", "is_correct": True},
            {"label": "C", "text": "2% Loss", "is_correct": False},
            {"label": "D", "text": "No profit no loss", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "When two items are sold at the same price, one at x% profit and another at x% loss:\nOverall Loss % = (x / 10)^2 = (20 / 10)^2 = 4% Loss.",
        "tips": "When SP is same for both items, equal gain and loss % always results in a net loss."
    },
    {
        "q_num": 19,
        "title": "Profit & Loss - Mixture Profit Percentage",
        "question_text": "A trader mixes two varieties of rice costing ₹40/kg and ₹60/kg in the ratio 3:2. He sells the mixture at ₹58/kg. Find his profit percentage.\n\nA) 18.5%\nB) 20.83%\nC) 22.5%\nD) 25%",
        "options": [
            {"label": "A", "text": "18.5%", "is_correct": False},
            {"label": "B", "text": "20.83%", "is_correct": True},
            {"label": "C", "text": "22.5%", "is_correct": False},
            {"label": "D", "text": "25%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Average CP of mixture = [(3 * 40) + (2 * 60)] / (3 + 2)\n= (120 + 120) / 5 = 240 / 5 = ₹48 per kg.\nSelling Price = ₹58 per kg.\nProfit = 58 - 48 = ₹10.\nProfit % = (10 / 48) * 100 = 20.83%.",
        "tips": "Calculate weighted average cost price per kg first."
    },
    {
        "q_num": 20,
        "title": "Profit & Loss - Profit Shift with Extra Selling Price",
        "question_text": "A man sells a TV at 15% profit. Had he sold it for ₹3,000 more, he would have gained 25%. Find the cost price.\n\nA) ₹25,000\nB) ₹30,000\nC) ₹35,000\nD) ₹40,000",
        "options": [
            {"label": "A", "text": "₹25,000", "is_correct": False},
            {"label": "B", "text": "₹30,000", "is_correct": True},
            {"label": "C", "text": "₹35,000", "is_correct": False},
            {"label": "D", "text": "₹40,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Difference in gain % = 25% - 15% = 10%.\n10% of CP = ₹3,000.\nCP = (3000 * 100) / 10 = ₹30,000.",
        "tips": "Extra SP amount corresponds to the difference in profit percentages."
    },
    {
        "q_num": 21,
        "title": "Profit & Loss - Markup with Two Successive Discounts",
        "question_text": "A dealer marks an article 25% above cost price and offers two successive discounts of 10% and 8%. Find the profit or loss percentage.\n\nA) 2.5% Profit\nB) 3.5% Profit\nC) 4% Loss\nD) 5% Profit",
        "options": [
            {"label": "A", "text": "2.5% Profit", "is_correct": False},
            {"label": "B", "text": "3.5% Profit", "is_correct": True},
            {"label": "C", "text": "4% Loss", "is_correct": False},
            {"label": "D", "text": "5% Profit", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 125.\nPrice after 1st discount (10%) = 125 * 0.90 = 112.5.\nPrice after 2nd discount (8%) = 112.5 * 0.92 = 103.5.\nNet Profit % = 103.5 - 100 = 3.5% Profit.",
        "tips": "Final SP = CP * (1 + Markup) * (1 - d1) * (1 - d2)."
    },
    {
        "q_num": 22,
        "title": "Profit & Loss - Reduced CP with Same SP",
        "question_text": "A trader buys an article and sells it at a profit of 20%. If the cost price had been 10% less and the selling price remained unchanged, what would have been the profit percentage?\n\nA) 30%\nB) 33.33%\nC) 35%\nD) 40%",
        "options": [
            {"label": "A", "text": "30%", "is_correct": False},
            {"label": "B", "text": "33.33%", "is_correct": True},
            {"label": "C", "text": "35%", "is_correct": False},
            {"label": "D", "text": "40%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let original CP = 100 => SP = 120.\nNew CP = 100 - 10% = 90.\nNew SP = 120 (unchanged).\nNew Profit = 120 - 90 = 30.\nNew Profit % = (30 / 90) * 100 = 33.33%.",
        "tips": "New Profit % = (SP - New CP) / New CP * 100."
    },
    {
        "q_num": 23,
        "title": "Profit & Loss - Dishonest Dealer False Weight",
        "question_text": "A seller uses a false weight of 900 g instead of 1 kg and sells goods at cost price. Find his profit percentage.\n\nA) 10%\nB) 11.11%\nC) 12.5%\nD) 15%",
        "options": [
            {"label": "A", "text": "10%", "is_correct": False},
            {"label": "B", "text": "11.11%", "is_correct": True},
            {"label": "C", "text": "12.5%", "is_correct": False},
            {"label": "D", "text": "15%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Error in weight = 1000g - 900g = 100g.\nTrue value used = 900g.\nProfit % = [Error / (True Value - Error)] * 100\n= (100 / 900) * 100 = 11.11%.",
        "tips": "Profit % for false weight = (Error / Weight Given) * 100."
    },
    {
        "q_num": 24,
        "title": "Profit & Loss - Equal Increment to CP and SP",
        "question_text": "An article is sold at a profit of 25%. If both the cost price and selling price increase by ₹200, the profit percentage becomes 20%. Find the original cost price.\n\nA) ₹600\nB) ₹800\nC) ₹1,000\nD) ₹1,200",
        "options": [
            {"label": "A", "text": "₹600", "is_correct": False},
            {"label": "B", "text": "₹800", "is_correct": True},
            {"label": "C", "text": "₹1,000", "is_correct": False},
            {"label": "D", "text": "₹1,200", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let original CP = 4x => original SP = 5x (since profit is 25%).\nNew CP = 4x + 200, New SP = 5x + 200.\nNew Profit % = 20% => (5x + 200) / (4x + 200) = 1.20 = 6 / 5.\n=> 5(5x + 200) = 6(4x + 200)\n=> 25x + 1000 = 24x + 1200 => x = 200.\nOriginal CP = 4x = 4 * 200 = ₹800.",
        "tips": "Express ratio of SP to CP as 5/4 initially."
    },
    {
        "q_num": 25,
        "title": "Profit & Loss - Loss to Profit Transition",
        "question_text": "A trader sells an article at a loss of 10%. If he had sold it for ₹180 more, he would have gained 5%. Find the cost price.\n\nA) ₹1,000\nB) ₹1,200\nC) ₹1,400\nD) ₹1,500",
        "options": [
            {"label": "A", "text": "₹1,000", "is_correct": False},
            {"label": "B", "text": "₹1,200", "is_correct": True},
            {"label": "C", "text": "₹1,400", "is_correct": False},
            {"label": "D", "text": "₹1,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Total shift in percentage = 5% gain - (-10% loss) = 15%.\n15% of CP = ₹180.\nCP = (180 * 100) / 15 = ₹1,200.",
        "tips": "Loss to profit shift equals sum of loss % and profit %."
    },
    {
        "q_num": 26,
        "title": "Profit & Loss - Markup 60% and 25% Discount",
        "question_text": "A shopkeeper marks goods 60% above cost price and gives a discount of 25%. Find the net profit percentage.\n\nA) 15%\nB) 20%\nC) 25%\nD) 30%",
        "options": [
            {"label": "A", "text": "15%", "is_correct": False},
            {"label": "B", "text": "20%", "is_correct": True},
            {"label": "C", "text": "25%", "is_correct": False},
            {"label": "D", "text": "30%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 160.\nDiscount = 25% of 160 = 40.\nSP = 160 - 40 = 120.\nNet Profit % = 120 - 100 = 20%.",
        "tips": "SP = 1.60 * 0.75 * CP = 1.20 * CP."
    },
    {
        "q_num": 27,
        "title": "Profit & Loss - Spoiled Goods Overall Profit",
        "question_text": "A trader buys 100 mangoes for ₹2,000. He finds that 20 mangoes are spoiled. At what price per mango should he sell the remaining mangoes to gain 25% overall?\n\nA) ₹28.50\nB) ₹31.25\nC) ₹32.50\nD) ₹35.00",
        "options": [
            {"label": "A", "text": "₹28.50", "is_correct": False},
            {"label": "B", "text": "₹31.25", "is_correct": True},
            {"label": "C", "text": "₹32.50", "is_correct": False},
            {"label": "D", "text": "₹35.00", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Total CP = ₹2,000.\nTarget Total SP = 2000 * 1.25 = ₹2,500.\nRemaining good mangoes = 100 - 20 = 80.\nSP per remaining mango = 2500 / 80 = ₹31.25.",
        "tips": "Divide target total SP by number of non-spoiled items."
    },
    {
        "q_num": 28,
        "title": "Profit & Loss - Total Acquisition Costs with Profit",
        "question_text": "A dealer purchases a machine for ₹48,000. He spends ₹2,000 on transportation and ₹5,000 on installation. He sells it at a profit of 20%. Find the selling price.\n\nA) ₹62,000\nB) ₹66,000\nC) ₹68,000\nD) ₹70,000",
        "options": [
            {"label": "A", "text": "₹62,000", "is_correct": False},
            {"label": "B", "text": "₹66,000", "is_correct": True},
            {"label": "C", "text": "₹68,000", "is_correct": False},
            {"label": "D", "text": "₹70,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Total Cost Price = Purchase + Transportation + Installation\n= 48000 + 2000 + 5000 = ₹55,000.\nProfit = 20%\nSP = 55000 * 1.20 = ₹66,000.",
        "tips": "All overhead costs must be summed to find total CP before applying profit multiplier."
    },
    {
        "q_num": 29,
        "title": "Profit & Loss - Loss to Gain with Dual Output",
        "question_text": "A trader sells an article at 10% loss. If the selling price is increased by ₹300, he gains 5%. Find the cost price and original selling price.\n\nA) CP = ₹1,800, SP = ₹1,620\nB) CP = ₹2,000, SP = ₹1,800\nC) CP = ₹2,200, SP = ₹1,980\nD) CP = ₹2,500, SP = ₹2,250",
        "options": [
            {"label": "A", "text": "CP = ₹1,800, SP = ₹1,620", "is_correct": False},
            {"label": "B", "text": "CP = ₹2,000, SP = ₹1,800", "is_correct": True},
            {"label": "C", "text": "CP = ₹2,200, SP = ₹1,980", "is_correct": False},
            {"label": "D", "text": "CP = ₹2,500, SP = ₹2,250", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Percentage shift = 5% gain - (-10% loss) = 15%.\n15% of CP = ₹300 => CP = (300 * 100) / 15 = ₹2,000.\nOriginal SP = 2000 * 0.90 = ₹1,800.",
        "tips": "Original SP = CP * (1 - original loss%)."
    },
    {
        "q_num": 30,
        "title": "Profit & Loss - Markup, Discount, Profit Amount and Dual Output",
        "question_text": "A shopkeeper marks an article 80% above cost price. He gives a discount of 20% and still earns ₹240 profit. Find the cost price and selling price of the article.\n\nA) CP = ₹500, SP = ₹740\nB) CP = ₹545.45, SP = ₹785.45\nC) CP = ₹600, SP = ₹840\nD) CP = ₹650, SP = ₹890",
        "options": [
            {"label": "A", "text": "CP = ₹500, SP = ₹740", "is_correct": False},
            {"label": "B", "text": "CP = ₹545.45, SP = ₹785.45", "is_correct": True},
            {"label": "C", "text": "CP = ₹600, SP = ₹840", "is_correct": False},
            {"label": "D", "text": "CP = ₹650, SP = ₹890", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let CP = 100 => MP = 180.\nSP = 180 * (80/100) = 144.\nProfit % = 144 - 100 = 44%.\n44% of CP = ₹240 => CP = (240 / 44) * 100 = ₹545.45.\nSP = 545.45 + 240 = ₹785.45.",
        "tips": "Calculate profit percentage from markup and discount first."
    }
]

def seed_database():
    conn = sqlite3.connect('instance/interview_portal.db')
    cursor = conn.cursor()
    
    # Clean out existing Profit & Loss questions if any
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Profit & Loss'")
    print(f"Cleared previous Profit & Loss questions.")
    
    for q in questions_data:
        category = "Aptitude"
        sub_category = "Commercial Mathematics"
        topic = "Profit & Loss"
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
    print(f"Successfully seeded {len(questions_data)} Profit & Loss questions into instance/interview_portal.db!")
    conn.close()

if __name__ == "__main__":
    seed_database()
