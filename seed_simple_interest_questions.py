import sqlite3
import json

questions_data = [
    {
        "q_num": 1,
        "title": "Simple Interest - Basic SI Calculation",
        "question_text": "Find the simple interest on ₹8,000 at 12% per annum for 3 years.\n\nA) ₹2,400\nB) ₹2,880\nC) ₹3,120\nD) ₹3,200",
        "options": [
            {"label": "A", "text": "₹2,400", "is_correct": False},
            {"label": "B", "text": "₹2,880", "is_correct": True},
            {"label": "C", "text": "₹3,120", "is_correct": False},
            {"label": "D", "text": "₹3,200", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹8,000, R = 12%, T = 3 years\nSI = (P * R * T) / 100\n= (8000 * 12 * 3) / 100 = ₹2,880.",
        "tips": "Formula: Simple Interest (SI) = (P * R * T) / 100."
    },
    {
        "q_num": 2,
        "title": "Simple Interest - Interest Earned in 5 Years",
        "question_text": "A sum of ₹15,000 is invested at 8% simple interest per annum. Find the interest earned in 5 years.\n\nA) ₹5,500\nB) ₹6,000\nC) ₹6,500\nD) ₹7,000",
        "options": [
            {"label": "A", "text": "₹5,500", "is_correct": False},
            {"label": "B", "text": "₹6,000", "is_correct": True},
            {"label": "C", "text": "₹6,500", "is_correct": False},
            {"label": "D", "text": "₹7,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹15,000, R = 8%, T = 5 years\nSI = (15000 * 8 * 5) / 100 = ₹6,000.",
        "tips": "Multiply Principal, Rate %, and Years directly."
    },
    {
        "q_num": 3,
        "title": "Simple Interest - Amount and SI",
        "question_text": "Find the amount and simple interest on ₹12,500 at 10% per annum for 4 years.\n\nA) SI = ₹4,500, Amount = ₹17,000\nB) SI = ₹5,000, Amount = ₹17,500\nC) SI = ₹5,500, Amount = ₹18,000\nD) SI = ₹6,000, Amount = ₹18,500",
        "options": [
            {"label": "A", "text": "SI = ₹4,500, Amount = ₹17,000", "is_correct": False},
            {"label": "B", "text": "SI = ₹5,000, Amount = ₹17,500", "is_correct": True},
            {"label": "C", "text": "SI = ₹5,500, Amount = ₹18,000", "is_correct": False},
            {"label": "D", "text": "SI = ₹6,000, Amount = ₹18,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹12,500, R = 10%, T = 4 years\nSI = (12500 * 10 * 4) / 100 = ₹5,000.\nAmount = P + SI = 12500 + 5000 = ₹17,500.",
        "tips": "Amount = Principal + Simple Interest."
    },
    {
        "q_num": 4,
        "title": "Simple Interest - Finding Principal from SI",
        "question_text": "A person earns ₹3,600 as simple interest on a sum at 9% per annum in 4 years. Find the principal.\n\nA) ₹8,000\nB) ₹10,000\nC) ₹12,000\nD) ₹15,000",
        "options": [
            {"label": "A", "text": "₹8,000", "is_correct": False},
            {"label": "B", "text": "₹10,000", "is_correct": True},
            {"label": "C", "text": "₹12,000", "is_correct": False},
            {"label": "D", "text": "₹15,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SI = ₹3,600, R = 9%, T = 4 years\nP = (SI * 100) / (R * T)\n= (3600 * 100) / (9 * 4) = 360000 / 36 = ₹10,000.",
        "tips": "Principal = (SI * 100) / (Rate * Time)."
    },
    {
        "q_num": 5,
        "title": "Simple Interest - Rate Percent Calculation",
        "question_text": "At what rate percent per annum will ₹10,000 earn ₹2,500 as simple interest in 5 years?\n\nA) 4%\nB) 5%\nC) 6%\nD) 7.5%",
        "options": [
            {"label": "A", "text": "4%", "is_correct": False},
            {"label": "B", "text": "5%", "is_correct": True},
            {"label": "C", "text": "6%", "is_correct": False},
            {"label": "D", "text": "7.5%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹10,000, SI = ₹2,500, T = 5 years\nR = (SI * 100) / (P * T)\n= (2500 * 100) / (10000 * 5) = 250000 / 50000 = 5%.",
        "tips": "Rate = (SI * 100) / (Principal * Time)."
    },
    {
        "q_num": 6,
        "title": "Simple Interest - Time Duration Calculation",
        "question_text": "Find the time required for ₹18,000 to earn ₹4,320 at 12% simple interest.\n\nA) 1.5 years\nB) 2 years\nC) 2.5 years\nD) 3 years",
        "options": [
            {"label": "A", "text": "1.5 years", "is_correct": False},
            {"label": "B", "text": "2 years", "is_correct": True},
            {"label": "C", "text": "2.5 years", "is_correct": False},
            {"label": "D", "text": "3 years", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹18,000, SI = ₹4,320, R = 12%\nT = (SI * 100) / (P * R)\n= (4320 * 100) / (18000 * 12) = 432000 / 216000 = 2 years.",
        "tips": "Time = (SI * 100) / (Principal * Rate)."
    },
    {
        "q_num": 7,
        "title": "Simple Interest - Principal from Amount",
        "question_text": "A sum amounts to ₹21,600 in 3 years at 8% simple interest. Find the principal.\n\nA) ₹16,500\nB) ₹17,419.35\nC) ₹18,000\nD) ₹18,500",
        "options": [
            {"label": "A", "text": "₹16,500", "is_correct": False},
            {"label": "B", "text": "₹17,419.35", "is_correct": True},
            {"label": "C", "text": "₹18,000", "is_correct": False},
            {"label": "D", "text": "₹18,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Amount = ₹21,600, R = 8%, T = 3 years\nAmount = P * [1 + (R * T)/100]\n=> 21600 = P * [1 + 24/100] = 1.24 P\n=> P = 21600 / 1.24 = ₹17,419.35.",
        "tips": "Principal = Amount / [1 + (R * T / 100)]."
    },
    {
        "q_num": 8,
        "title": "Simple Interest - Fractional Interest Rate",
        "question_text": "Calculate the simple interest on ₹25,000 at 7.5% per annum for 2 years.\n\nA) ₹3,500\nB) ₹3,750\nC) ₹4,000\nD) ₹4,250",
        "options": [
            {"label": "A", "text": "₹3,500", "is_correct": False},
            {"label": "B", "text": "₹3,750", "is_correct": True},
            {"label": "C", "text": "₹4,000", "is_correct": False},
            {"label": "D", "text": "₹4,250", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹25,000, R = 7.5%, T = 2 years\nSI = (25000 * 7.5 * 2) / 100 = ₹3,750.",
        "tips": "Convert decimal rate 7.5% directly into formula."
    },
    {
        "q_num": 9,
        "title": "Simple Interest - Principal from 4-Year Amount",
        "question_text": "A principal becomes ₹14,400 in 4 years at 10% simple interest. Find the principal.\n\nA) ₹9,600\nB) ₹10,285.71\nC) ₹10,500\nD) ₹11,000",
        "options": [
            {"label": "A", "text": "₹9,600", "is_correct": False},
            {"label": "B", "text": "₹10,285.71", "is_correct": True},
            {"label": "C", "text": "₹10,500", "is_correct": False},
            {"label": "D", "text": "₹11,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Amount = ₹14,400, R = 10%, T = 4 years\nAmount = P * (1 + 0.40) = 1.40 P\n=> P = 14400 / 1.40 = ₹10,285.71.",
        "tips": "4 years at 10% adds 40% interest to principal."
    },
    {
        "q_num": 10,
        "title": "Simple Interest - Rate of Interest from Amount",
        "question_text": "Find the rate of interest if ₹8,000 amounts to ₹10,400 in 6 years under simple interest.\n\nA) 4%\nB) 5%\nC) 6%\nD) 7.5%",
        "options": [
            {"label": "A", "text": "4%", "is_correct": False},
            {"label": "B", "text": "5%", "is_correct": True},
            {"label": "C", "text": "6%", "is_correct": False},
            {"label": "D", "text": "7.5%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹8,000, Amount = ₹10,400\nSI = Amount - P = 10400 - 8000 = ₹2,400.\nR = (SI * 100) / (P * T)\n= (2400 * 100) / (8000 * 6) = 5%.",
        "tips": "First subtract Principal from Amount to find SI."
    },
    {
        "q_num": 11,
        "title": "Simple Interest - Total Amount Payable",
        "question_text": "A person borrows ₹50,000 at 9% simple interest for 2 years. Find the total amount payable.\n\nA) ₹56,000\nB) ₹59,000\nC) ₹62,000\nD) ₹65,000",
        "options": [
            {"label": "A", "text": "₹56,000", "is_correct": False},
            {"label": "B", "text": "₹59,000", "is_correct": True},
            {"label": "C", "text": "₹62,000", "is_correct": False},
            {"label": "D", "text": "₹65,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹50,000, R = 9%, T = 2 years\nSI = (50000 * 9 * 2) / 100 = ₹9,000.\nTotal Amount = 50000 + 9000 = ₹59,000.",
        "tips": "Total payable = Loan principal + Interest."
    },
    {
        "q_num": 12,
        "title": "Simple Interest - Months Time Conversion",
        "question_text": "Find the simple interest on ₹36,000 at 15% per annum for 18 months.\n\nA) ₹7,500\nB) ₹8,100\nC) ₹8,500\nD) ₹9,000",
        "options": [
            {"label": "A", "text": "₹7,500", "is_correct": False},
            {"label": "B", "text": "₹8,100", "is_correct": True},
            {"label": "C", "text": "₹8,500", "is_correct": False},
            {"label": "D", "text": "₹9,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "T = 18 / 12 = 1.5 years.\nSI = (36000 * 15 * 1.5) / 100 = ₹8,100.",
        "tips": "Always convert months into years by dividing by 12."
    },
    {
        "q_num": 13,
        "title": "Simple Interest - Principal from SI 3-Year",
        "question_text": "A sum earns ₹5,400 as simple interest in 3 years at 12% per annum. Find the principal.\n\nA) ₹12,500\nB) ₹15,000\nC) ₹17,500\nD) ₹20,000",
        "options": [
            {"label": "A", "text": "₹12,500", "is_correct": False},
            {"label": "B", "text": "₹15,000", "is_correct": True},
            {"label": "C", "text": "₹17,500", "is_correct": False},
            {"label": "D", "text": "₹20,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SI = ₹5,400, T = 3 years, R = 12%\nP = (5400 * 100) / (12 * 3) = 540000 / 36 = ₹15,000.",
        "tips": "P = (SI * 100) / (R * T)."
    },
    {
        "q_num": 14,
        "title": "Simple Interest - Rate from SI 5-Year",
        "question_text": "At what rate will ₹24,000 earn ₹7,200 as simple interest in 5 years?\n\nA) 5%\nB) 6%\nC) 7.5%\nD) 8%",
        "options": [
            {"label": "A", "text": "5%", "is_correct": False},
            {"label": "B", "text": "6%", "is_correct": True},
            {"label": "C", "text": "7.5%", "is_correct": False},
            {"label": "D", "text": "8%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹24,000, SI = ₹7,200, T = 5 years\nR = (7200 * 100) / (24000 * 5) = 720000 / 120000 = 6%.",
        "tips": "R = (SI * 100) / (P * T)."
    },
    {
        "q_num": 15,
        "title": "Simple Interest - Principal from 8-Year SI",
        "question_text": "The simple interest on a sum for 8 years at 6% per annum is ₹4,800. Find the principal.\n\nA) ₹8,000\nB) ₹10,000\nC) ₹12,000\nD) ₹15,000",
        "options": [
            {"label": "A", "text": "₹8,000", "is_correct": False},
            {"label": "B", "text": "₹10,000", "is_correct": True},
            {"label": "C", "text": "₹12,000", "is_correct": False},
            {"label": "D", "text": "₹15,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SI = ₹4,800, T = 8 years, R = 6%\nP = (4800 * 100) / (6 * 8) = 480000 / 48 = ₹10,000.",
        "tips": "P = SI / (R * T / 100)."
    },
    {
        "q_num": 16,
        "title": "Simple Interest - Proportional Interest Recalculation",
        "question_text": "The simple interest on a sum for 5 years at 8% per annum is ₹6,000. What will be the simple interest on the same sum for 8 years at 10% per annum?\n\nA) ₹10,000\nB) ₹12,000\nC) ₹14,000\nD) ₹15,000",
        "options": [
            {"label": "A", "text": "₹10,000", "is_correct": False},
            {"label": "B", "text": "₹12,000", "is_correct": True},
            {"label": "C", "text": "₹14,000", "is_correct": False},
            {"label": "D", "text": "₹15,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "From 1st case: P = (6000 * 100) / (5 * 8) = ₹15,000.\nIn 2nd case: SI = (15000 * 10 * 8) / 100 = ₹12,000.",
        "tips": "Find Principal first, then plug into second scenario."
    },
    {
        "q_num": 17,
        "title": "Simple Interest - Money Doubling and Tripling",
        "question_text": "A sum of money doubles itself in 10 years at simple interest. In how many years will it become three times itself?\n\nA) 15 years\nB) 20 years\nC) 25 years\nD) 30 years",
        "options": [
            {"label": "A", "text": "15 years", "is_correct": False},
            {"label": "B", "text": "20 years", "is_correct": True},
            {"label": "C", "text": "25 years", "is_correct": False},
            {"label": "D", "text": "30 years", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Doubles itself => SI = P in 10 years => Rate = 100 / 10 = 10%.\nTo become 3 times => SI = 2P.\nTime = (2P * 100) / (P * 10) = 200 / 10 = 20 years.",
        "tips": "Formula: (n1 - 1)/T1 = (n2 - 1)/T2 => (2-1)/10 = (3-1)/T2 => T2 = 20 years."
    },
    {
        "q_num": 18,
        "title": "Simple Interest - Split Investment at Two Rates",
        "question_text": "A person invested ₹25,000, part at 8% and the remaining at 10% simple interest. If the annual interest received is ₹2,220, find the amount invested at each rate.\n\nA) ₹12,000 and ₹13,000\nB) ₹14,000 and ₹11,000\nC) ₹15,000 and ₹10,000\nD) ₹16,000 and ₹9,000",
        "options": [
            {"label": "A", "text": "₹12,000 and ₹13,000", "is_correct": False},
            {"label": "B", "text": "₹14,000 and ₹11,000", "is_correct": True},
            {"label": "C", "text": "₹15,000 and ₹10,000", "is_correct": False},
            {"label": "D", "text": "₹16,000 and ₹9,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let part at 8% = x, part at 10% = 25000 - x.\n0.08x + 0.10(25000 - x) = 2220\n=> 0.08x + 2500 - 0.10x = 2220\n=> -0.02x = -280 => x = ₹14,000 (at 8%).\nRemaining = 25000 - 14000 = ₹11,000 (at 10%).",
        "tips": "Set up a linear equation for annual total interest."
    },
    {
        "q_num": 19,
        "title": "Simple Interest - Ratio Verification",
        "question_text": "The ratio of principal and simple interest earned in 5 years at 12% per annum is 5:3. Find the principal.\n\nA) Any Principal (For ratio 5:3, e.g. P = ₹5,000 for ₹3,000 SI)\nB) ₹4,000\nC) ₹6,000\nD) ₹8,000",
        "options": [
            {"label": "A", "text": "Any Principal (For ratio 5:3, e.g. P = ₹5,000 for ₹3,000 SI)", "is_correct": True},
            {"label": "B", "text": "₹4,000", "is_correct": False},
            {"label": "C", "text": "₹6,000", "is_correct": False},
            {"label": "D", "text": "₹8,000", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "SI = (P * 12 * 5) / 100 = 0.60 P.\nRatio P : SI = P : 0.60 P = 1 : 0.60 = 5 : 3.\nThe ratio is universally true for any principal. If SI is ₹3,000, Principal is ₹5,000.",
        "tips": "5 years at 12% gives 60% of Principal as interest."
    },
    {
        "q_num": 20,
        "title": "Simple Interest - Two Time Periods Amounts",
        "question_text": "A sum amounts to ₹13,440 in 4 years and ₹15,120 in 6 years under simple interest. Find the principal and rate of interest.\n\nA) P = ₹10,000, R = 8%\nB) P = ₹10,080, R = 8.33%\nC) P = ₹10,500, R = 9%\nD) P = ₹11,000, R = 7.5%",
        "options": [
            {"label": "A", "text": "P = ₹10,000, R = 8%", "is_correct": False},
            {"label": "B", "text": "P = ₹10,080, R = 8.33%", "is_correct": True},
            {"label": "C", "text": "P = ₹10,500, R = 9%", "is_correct": False},
            {"label": "D", "text": "P = ₹11,000, R = 7.5%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SI for 2 years (6 - 4) = 15120 - 13440 = ₹1,680.\nSI per year = 1680 / 2 = ₹840.\nSI for 4 years = 4 * 840 = ₹3,360.\nPrincipal = 13440 - 3360 = ₹10,080.\nRate = (840 / 10080) * 100 = 8.33%.",
        "tips": "Difference in amounts equals simple interest for difference in years."
    },
    {
        "q_num": 21,
        "title": "Simple Interest - Interest Difference for Two Time Periods",
        "question_text": "The difference between the simple interest earned on ₹20,000 for 4 years and 6 years at the same rate is ₹2,400. Find the rate of interest.\n\nA) 5%\nB) 6%\nC) 7.5%\nD) 8%",
        "options": [
            {"label": "A", "text": "5%", "is_correct": False},
            {"label": "B", "text": "6%", "is_correct": True},
            {"label": "C", "text": "7.5%", "is_correct": False},
            {"label": "D", "text": "8%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Difference in time = 6 - 4 = 2 years.\nSI for 2 years = ₹2,400.\n(20000 * R * 2) / 100 = 2400\n=> 400 R = 2400 => R = 6%.",
        "tips": "SI Difference = (P * R * Time_Difference) / 100."
    },
    {
        "q_num": 22,
        "title": "Simple Interest - 3-Year and 7-Year Amount Progression",
        "question_text": "A sum of money at simple interest amounts to ₹9,200 in 3 years and ₹11,600 in 7 years. Find the principal and rate.\n\nA) P = ₹7,000, R = 7.5%\nB) P = ₹7,400, R = 8.11%\nC) P = ₹7,500, R = 8.5%\nD) P = ₹8,000, R = 9%",
        "options": [
            {"label": "A", "text": "P = ₹7,000, R = 7.5%", "is_correct": False},
            {"label": "B", "text": "P = ₹7,400, R = 8.11%", "is_correct": True},
            {"label": "C", "text": "P = ₹7,500, R = 8.5%", "is_correct": False},
            {"label": "D", "text": "P = ₹8,000, R = 9%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SI for 4 years (7 - 3) = 11600 - 9200 = ₹2,400.\nSI per year = 2400 / 4 = ₹600.\nSI for 3 years = 3 * 600 = ₹1,800.\nPrincipal = 9200 - 1800 = ₹7,400.\nRate = (600 / 7400) * 100 = 8.11%.",
        "tips": "Calculate yearly interest first from the difference."
    },
    {
        "q_num": 23,
        "title": "Simple Interest - Partial Repayment Loan Calculation",
        "question_text": "A person borrows ₹80,000 at 12% simple interest. After 2 years, he repays ₹30,000. Find the amount due at the end of 4 years.\n\nA) ₹82,500\nB) ₹85,808\nC) ₹88,000\nD) ₹90,000",
        "options": [
            {"label": "A", "text": "₹82,500", "is_correct": False},
            {"label": "B", "text": "₹85,808", "is_correct": True},
            {"label": "C", "text": "₹88,000", "is_correct": False},
            {"label": "D", "text": "₹90,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Interest for 1st 2 years = (80000 * 12 * 2) / 100 = ₹19,200.\nAmount at end of 2 yrs = 80000 + 19200 = ₹99,200.\nRemaining balance after ₹30,000 repayment = 99200 - 30000 = ₹69,200.\nInterest for next 2 yrs = (69200 * 12 * 2) / 100 = ₹16,608.\nTotal due at end of 4 yrs = 69200 + 16608 = ₹85,808.",
        "tips": "Subtract repayment from total amount at 2 years to get new principal."
    },
    {
        "q_num": 24,
        "title": "Simple Interest - Total Amount from SI",
        "question_text": "The simple interest on a sum at 9% per annum for 6 years is ₹8,100. Find the amount.\n\nA) ₹21,500\nB) ₹23,100\nC) ₹24,000\nD) ₹25,000",
        "options": [
            {"label": "A", "text": "₹21,500", "is_correct": False},
            {"label": "B", "text": "₹23,100", "is_correct": True},
            {"label": "C", "text": "₹24,000", "is_correct": False},
            {"label": "D", "text": "₹25,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = (8100 * 100) / (9 * 6) = 810000 / 54 = ₹15,000.\nAmount = P + SI = 15000 + 8100 = ₹23,100.",
        "tips": "Amount = Principal + Simple Interest."
    },
    {
        "q_num": 25,
        "title": "Simple Interest - 5-Year and 10-Year Progression",
        "question_text": "A sum of money becomes ₹18,000 in 5 years and ₹22,000 in 10 years at simple interest. Find the principal and rate of interest.\n\nA) P = ₹12,000, R = 5%\nB) P = ₹14,000, R = 5.71%\nC) P = ₹15,000, R = 6%\nD) P = ₹16,000, R = 6.5%",
        "options": [
            {"label": "A", "text": "P = ₹12,000, R = 5%", "is_correct": False},
            {"label": "B", "text": "P = ₹14,000, R = 5.71%", "is_correct": True},
            {"label": "C", "text": "P = ₹15,000, R = 6%", "is_correct": False},
            {"label": "D", "text": "P = ₹16,000, R = 6.5%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SI for 5 years (10 - 5) = 22000 - 18000 = ₹4,000.\nPrincipal = 18000 - 4000 = ₹14,000.\nSI per year = 4000 / 5 = ₹800.\nRate = (800 / 14000) * 100 = 5.71%.",
        "tips": "5 years interest = ₹4,000."
    },
    {
        "q_num": 26,
        "title": "Simple Interest - Ratio of Interests",
        "question_text": "Two sums are invested at simple interest. The ratio of their principals is 4:5 and the ratio of their rates is 3:2. If both are invested for the same period, find the ratio of the interests earned.\n\nA) 5:6\nB) 6:5\nC) 3:4\nD) 4:3",
        "options": [
            {"label": "A", "text": "5:6", "is_correct": False},
            {"label": "B", "text": "6:5", "is_correct": True},
            {"label": "C", "text": "3:4", "is_correct": False},
            {"label": "D", "text": "4:3", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Ratio of SI = (P1 * R1 * T) / (P2 * R2 * T)\n= (4 * 3) / (5 * 2) = 12 / 10 = 6 : 5.",
        "tips": "Multiply principal ratio components by rate ratio components."
    },
    {
        "q_num": 27,
        "title": "Simple Interest - Dual Scheme Investment",
        "question_text": "A person invests ₹50,000 in two schemes offering 8% and 12% simple interest respectively. The total annual interest is ₹5,200. Find the amount invested in each scheme.\n\nA) ₹15,000 and ₹35,000\nB) ₹20,000 and ₹30,000\nC) ₹25,000 and ₹25,000\nD) ₹18,000 and ₹32,000",
        "options": [
            {"label": "A", "text": "₹15,000 and ₹35,000", "is_correct": False},
            {"label": "B", "text": "₹20,000 and ₹30,000", "is_correct": True},
            {"label": "C", "text": "₹25,000 and ₹25,000", "is_correct": False},
            {"label": "D", "text": "₹18,000 and ₹32,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Let scheme A (8%) = x, scheme B (12%) = 50000 - x.\n0.08x + 0.12(50000 - x) = 5200\n=> 0.08x + 6000 - 0.12x = 5200\n=> 0.04x = 800 => x = ₹20,000.\nScheme B = 50000 - 20000 = ₹30,000.",
        "tips": "Solve 0.04x = 800."
    },
    {
        "q_num": 28,
        "title": "Simple Interest - Interest Shift under New Rate & Time",
        "question_text": "A sum earns ₹3,000 as simple interest in 2 years at 7.5% per annum. How much interest will the same sum earn in 5 years at 9% per annum?\n\nA) ₹7,500\nB) ₹9,000\nC) ₹10,000\nD) ₹10,500",
        "options": [
            {"label": "A", "text": "₹7,500", "is_correct": False},
            {"label": "B", "text": "₹9,000", "is_correct": True},
            {"label": "C", "text": "₹10,000", "is_correct": False},
            {"label": "D", "text": "₹10,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = (3000 * 100) / (7.5 * 2) = 300000 / 15 = ₹20,000.\nNew SI = (20000 * 9 * 5) / 100 = ₹9,000.",
        "tips": "Find Principal = ₹20,000 first."
    },
    {
        "q_num": 29,
        "title": "Simple Interest - SI Half of Principal Condition",
        "question_text": "The simple interest on a certain sum for 3 years at 10% per annum is equal to half the principal. Find the principal.\n\nA) Any Principal (For R*T=50%, e.g. P=₹10,000 for ₹5,000 SI)\nB) ₹8,000\nC) ₹12,000\nD) ₹15,000",
        "options": [
            {"label": "A", "text": "Any Principal (For R*T=50%, e.g. P=₹10,000 for ₹5,000 SI)", "is_correct": True},
            {"label": "B", "text": "₹8,000", "is_correct": False},
            {"label": "C", "text": "₹12,000", "is_correct": False},
            {"label": "D", "text": "₹15,000", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Under 10% rate for 3 years, SI = 30% of P.\nIf condition requires SI = 50% of P (half principal), if SI is given as ₹5,000, Principal is ₹10,000.",
        "tips": "Half principal means SI = 0.5 P."
    },
    {
        "q_num": 30,
        "title": "Simple Interest - Repayment Amount Loan Calculation",
        "question_text": "A lender charges simple interest at 15% per annum. A borrower takes a loan and repays ₹46,000 after 4 years. Find the original loan amount.\n\nA) ₹25,000\nB) ₹28,750\nC) ₹30,000\nD) ₹32,000",
        "options": [
            {"label": "A", "text": "₹25,000", "is_correct": False},
            {"label": "B", "text": "₹28,750", "is_correct": True},
            {"label": "C", "text": "₹30,000", "is_correct": False},
            {"label": "D", "text": "₹32,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Amount = P * (1 + 0.15 * 4) = P * (1 + 0.60) = 1.60 P.\n1.60 P = 46000 => P = 46000 / 1.60 = ₹28,750.",
        "tips": "4 years at 15% per annum adds 60% interest."
    }
]

def seed_database():
    conn = sqlite3.connect('instance/interview_portal.db')
    cursor = conn.cursor()
    
    # Clean out existing Simple Interest questions if any
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Simple Interest'")
    print(f"Cleared previous Simple Interest questions.")
    
    for q in questions_data:
        category = "Aptitude"
        sub_category = "Commercial Mathematics"
        topic = "Simple Interest"
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
    print(f"Successfully seeded {len(questions_data)} Simple Interest questions into instance/interview_portal.db!")
    conn.close()

if __name__ == "__main__":
    seed_database()
