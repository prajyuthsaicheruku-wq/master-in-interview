import sqlite3
import json

questions_data = [
    {
        "q_num": 1,
        "title": "Compound Interest - CI on 10,000 for 2 yrs at 10%",
        "question_text": "Find the compound interest on ₹10,000 at 10% per annum for 2 years.\n\nA) ₹1,800\nB) ₹2,100\nC) ₹2,200\nD) ₹2,400",
        "options": [
            {"label": "A", "text": "₹1,800", "is_correct": False},
            {"label": "B", "text": "₹2,100", "is_correct": True},
            {"label": "C", "text": "₹2,200", "is_correct": False},
            {"label": "D", "text": "₹2,400", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹10,000, R = 10%, T = 2 years\nAmount = 10000 * (1 + 10/100)^2 = 10000 * 1.21 = ₹12,100.\nCI = Amount - P = 12100 - 10000 = ₹2,100.",
        "tips": "Formula: Amount = P * (1 + R/100)^T. CI = Amount - Principal."
    },
    {
        "q_num": 2,
        "title": "Compound Interest - Amount and CI on 8,000 at 12% for 3 yrs",
        "question_text": "Calculate the amount and compound interest on ₹8,000 at 12% per annum for 3 years.\n\nA) Amount = ₹11,239.42, CI = ₹3,239.42\nB) Amount = ₹10,800, CI = ₹2,800\nC) Amount = ₹11,500, CI = ₹3,500\nD) Amount = ₹12,000, CI = ₹4,000",
        "options": [
            {"label": "A", "text": "Amount = ₹11,239.42, CI = ₹3,239.42", "is_correct": True},
            {"label": "B", "text": "Amount = ₹10,800, CI = ₹2,800", "is_correct": False},
            {"label": "C", "text": "Amount = ₹11,500, CI = ₹3,500", "is_correct": False},
            {"label": "D", "text": "Amount = ₹12,000, CI = ₹4,000", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "P = ₹8,000, R = 12%, T = 3 years\nAmount = 8000 * (1.12)^3 = 8000 * 1.404928 = ₹11,239.42.\nCI = 11239.42 - 8000 = ₹3,239.42.",
        "tips": "Multiply Principal by 1.12 cubed."
    },
    {
        "q_num": 3,
        "title": "Compound Interest - Amount on 15,000 at 8% for 2 yrs",
        "question_text": "A sum of ₹15,000 is invested at 8% compound interest per annum for 2 years. Find the amount.\n\nA) ₹16,800\nB) ₹17,496\nC) ₹18,000\nD) ₹18,500",
        "options": [
            {"label": "A", "text": "₹16,800", "is_correct": False},
            {"label": "B", "text": "₹17,496", "is_correct": True},
            {"label": "C", "text": "₹18,000", "is_correct": False},
            {"label": "D", "text": "₹18,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹15,000, R = 8%, T = 2 years\nAmount = 15000 * (1.08)^2 = 15000 * 1.1664 = ₹17,496.",
        "tips": "Multiplier for 2 years at 8% is 1.1664."
    },
    {
        "q_num": 4,
        "title": "Compound Interest - CI on 20,000 at 5% for 3 yrs",
        "question_text": "Find the compound interest on ₹20,000 at 5% per annum for 3 years.\n\nA) ₹2,800\nB) ₹3,152.50\nC) ₹3,300\nD) ₹3,500",
        "options": [
            {"label": "A", "text": "₹2,800", "is_correct": False},
            {"label": "B", "text": "₹3,152.50", "is_correct": True},
            {"label": "C", "text": "₹3,300", "is_correct": False},
            {"label": "D", "text": "₹3,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹20,000, R = 5%, T = 3 years\nAmount = 20000 * (1.05)^3 = 20000 * 1.157625 = ₹23,152.50.\nCI = 23152.50 - 20000 = ₹3,152.50.",
        "tips": "(1.05)^3 = 1.157625."
    },
    {
        "q_num": 5,
        "title": "Compound Interest - Principal from 13,310 in 3 yrs at 10%",
        "question_text": "A principal becomes ₹13,310 in 3 years at 10% compound interest. Find the principal.\n\nA) ₹8,000\nB) ₹10,000\nC) ₹11,000\nD) ₹12,000",
        "options": [
            {"label": "A", "text": "₹8,000", "is_correct": False},
            {"label": "B", "text": "₹10,000", "is_correct": True},
            {"label": "C", "text": "₹11,000", "is_correct": False},
            {"label": "D", "text": "₹12,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Amount = ₹13,310, R = 10%, T = 3 years\n13310 = P * (1.10)^3 = P * 1.331\n=> P = 13310 / 1.331 = ₹10,000.",
        "tips": "Divide amount by 1.331."
    },
    {
        "q_num": 6,
        "title": "Compound Interest - Rate from 12,000 to 14,520 in 2 yrs",
        "question_text": "At what rate percent per annum will ₹12,000 amount to ₹14,520 in 2 years under compound interest?\n\nA) 8%\nB) 10%\nC) 12%\nD) 15%",
        "options": [
            {"label": "A", "text": "8%", "is_correct": False},
            {"label": "B", "text": "10%", "is_correct": True},
            {"label": "C", "text": "12%", "is_correct": False},
            {"label": "D", "text": "15%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "14520 / 12000 = 1.21\n(1 + R/100)^2 = 1.21\n=> 1 + R/100 = 1.10 => R = 10%.",
        "tips": "Take square root of ratio (Amount / Principal)."
    },
    {
        "q_num": 7,
        "title": "Compound Interest - Amount on 25,000 at 6% for 2 yrs",
        "question_text": "Find the amount on ₹25,000 at 6% compound interest per annum for 2 years.\n\nA) ₹27,500\nB) ₹28,090\nC) ₹28,500\nD) ₹29,000",
        "options": [
            {"label": "A", "text": "₹27,500", "is_correct": False},
            {"label": "B", "text": "₹28,090", "is_correct": True},
            {"label": "C", "text": "₹28,500", "is_correct": False},
            {"label": "D", "text": "₹29,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹25,000, R = 6%, T = 2 years\nAmount = 25000 * (1.06)^2 = 25000 * 1.1236 = ₹28,090.",
        "tips": "(1.06)^2 = 1.1236."
    },
    {
        "q_num": 8,
        "title": "Compound Interest - CI on 18,000 at 15% for 2 yrs",
        "question_text": "Calculate the compound interest on ₹18,000 at 15% per annum for 2 years.\n\nA) ₹5,400\nB) ₹5,805\nC) ₹6,000\nD) ₹6,250",
        "options": [
            {"label": "A", "text": "₹5,400", "is_correct": False},
            {"label": "B", "text": "₹5,805", "is_correct": True},
            {"label": "C", "text": "₹6,000", "is_correct": False},
            {"label": "D", "text": "₹6,250", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹18,000, R = 15%, T = 2 years\nAmount = 18000 * (1.15)^2 = 18000 * 1.3225 = ₹23,805.\nCI = 23805 - 18000 = ₹5,805.",
        "tips": "Net % for 2 years at 15% = 15 + 15 + (225/100) = 32.25%."
    },
    {
        "q_num": 9,
        "title": "Compound Interest - Principal from 24,200 in 2 yrs at 10%",
        "question_text": "A sum amounts to ₹24,200 in 2 years at 10% compound interest. Find the principal.\n\nA) ₹18,000\nB) ₹20,000\nC) ₹21,000\nD) ₹22,000",
        "options": [
            {"label": "A", "text": "₹18,000", "is_correct": False},
            {"label": "B", "text": "₹20,000", "is_correct": True},
            {"label": "C", "text": "₹21,000", "is_correct": False},
            {"label": "D", "text": "₹22,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Amount = ₹24,200, R = 10%, T = 2 years\n24200 = P * 1.21 => P = 24200 / 1.21 = ₹20,000.",
        "tips": "Divide by 1.21."
    },
    {
        "q_num": 10,
        "title": "Compound Interest - CI on 30,000 at 8% for 3 yrs",
        "question_text": "Find the compound interest on ₹30,000 at 8% per annum for 3 years.\n\nA) ₹7,200\nB) ₹7,791.36\nC) ₹8,000\nD) ₹8,500",
        "options": [
            {"label": "A", "text": "₹7,200", "is_correct": False},
            {"label": "B", "text": "₹7,791.36", "is_correct": True},
            {"label": "C", "text": "₹8,000", "is_correct": False},
            {"label": "D", "text": "₹8,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹30,000, R = 8%, T = 3 years\nAmount = 30000 * (1.08)^3 = 30000 * 1.259712 = ₹37,791.36.\nCI = 37791.36 - 30000 = ₹7,791.36.",
        "tips": "(1.08)^3 = 1.259712."
    },
    {
        "q_num": 11,
        "title": "Compound Interest - Rate from 16,000 to 18,640 in 2 yrs",
        "question_text": "A principal of ₹16,000 grows to ₹18,640 in 2 years under compound interest. Find the annual rate.\n\nA) 6%\nB) 7.94% (Approx 8%)\nC) 9%\nD) 10%",
        "options": [
            {"label": "A", "text": "6%", "is_correct": False},
            {"label": "B", "text": "7.94% (Approx 8%)", "is_correct": True},
            {"label": "C", "text": "9%", "is_correct": False},
            {"label": "D", "text": "10%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "18640 / 16000 = 1.165\n(1 + R/100)^2 = 1.165\n=> 1 + R/100 = sqrt(1.165) ≈ 1.07935 => R ≈ 7.94%.",
        "tips": "Ratio = 1.165. Take square root to get 1 + R/100."
    },
    {
        "q_num": 12,
        "title": "Compound Interest - Amount on 50,000 at 10% for 2 yrs",
        "question_text": "Calculate the amount on ₹50,000 at 10% compound interest for 2 years.\n\nA) ₹58,000\nB) ₹60,500\nC) ₹62,000\nD) ₹65,000",
        "options": [
            {"label": "A", "text": "₹58,000", "is_correct": False},
            {"label": "B", "text": "₹60,500", "is_correct": True},
            {"label": "C", "text": "₹62,000", "is_correct": False},
            {"label": "D", "text": "₹65,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹50,000, R = 10%, T = 2 years\nAmount = 50000 * (1.10)^2 = 50000 * 1.21 = ₹60,500.",
        "tips": "50000 * 1.21 = 60500."
    },
    {
        "q_num": 13,
        "title": "Compound Interest - CI on 12,500 at 20% for 2 yrs",
        "question_text": "Find the compound interest on ₹12,500 at 20% per annum for 2 years.\n\nA) ₹5,000\nB) ₹5,500\nC) ₹6,000\nD) ₹6,500",
        "options": [
            {"label": "A", "text": "₹5,000", "is_correct": False},
            {"label": "B", "text": "₹5,500", "is_correct": True},
            {"label": "C", "text": "₹6,000", "is_correct": False},
            {"label": "D", "text": "₹6,500", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹12,500, R = 20%, T = 2 years\nAmount = 12500 * (1.20)^2 = 12500 * 1.44 = ₹18,000.\nCI = 18000 - 12500 = ₹5,500.",
        "tips": "Net % for 2 years at 20% = 44%."
    },
    {
        "q_num": 14,
        "title": "Compound Interest - Doubling at 100% CI Rate",
        "question_text": "A sum doubles itself in compound interest at 100% per annum. How many years will it take?\n\nA) 1 year\nB) 2 years\nC) 3 years\nD) 4 years",
        "options": [
            {"label": "A", "text": "1 year", "is_correct": True},
            {"label": "B", "text": "2 years", "is_correct": False},
            {"label": "C", "text": "3 years", "is_correct": False},
            {"label": "D", "text": "4 years", "is_correct": False}
        ],
        "correct_option": "A",
        "sample_answer": "Amount = P * (1 + 100/100)^T = P * (2)^T.\nFor money to double, Amount = 2P\n=> P * (2)^T = 2P => 2^T = 2^1 => T = 1 year.",
        "tips": "At 100% interest per annum, money doubles in 1 year."
    },
    {
        "q_num": 15,
        "title": "Compound Interest - Amount and CI on 40,000 at 5% for 4 yrs",
        "question_text": "Find the amount and compound interest on ₹40,000 at 5% per annum for 4 years.\n\nA) Amount = ₹48,000, CI = ₹8,000\nB) Amount = ₹48,620.25, CI = ₹8,620.25\nC) Amount = ₹49,000, CI = ₹9,000\nD) Amount = ₹50,000, CI = ₹10,000",
        "options": [
            {"label": "A", "text": "Amount = ₹48,000, CI = ₹8,000", "is_correct": False},
            {"label": "B", "text": "Amount = ₹48,620.25, CI = ₹8,620.25", "is_correct": True},
            {"label": "C", "text": "Amount = ₹49,000, CI = ₹9,000", "is_correct": False},
            {"label": "D", "text": "Amount = ₹50,000, CI = ₹10,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹40,000, R = 5%, T = 4 years\nAmount = 40000 * (1.05)^4 = 40000 * 1.21550625 = ₹48,620.25.\nCI = 48620.25 - 40000 = ₹8,620.25.",
        "tips": "(1.05)^4 = 1.21550625."
    },
    {
        "q_num": 16,
        "title": "Compound Interest - Difference CI - SI for 3 Years",
        "question_text": "Find the difference between Compound Interest and Simple Interest on ₹20,000 at 10% per annum for 3 years.\n\nA) ₹500\nB) ₹620\nC) ₹700\nD) ₹750",
        "options": [
            {"label": "A", "text": "₹500", "is_correct": False},
            {"label": "B", "text": "₹620", "is_correct": True},
            {"label": "C", "text": "₹700", "is_correct": False},
            {"label": "D", "text": "₹750", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "SI = (20000 * 10 * 3) / 100 = ₹6,000.\nCI = 20000 * [(1.10)^3 - 1] = 20000 * 0.331 = ₹6,620.\nDifference = CI - SI = 6620 - 6000 = ₹620.",
        "tips": "Formula for 3 yrs diff: P * (R/100)^2 * (3 + R/100) = 20000 * 0.01 * 3.1 = 620."
    },
    {
        "q_num": 17,
        "title": "Compound Interest - Consecutive Years Amounts Rate",
        "question_text": "A sum amounts to ₹26,620 in 3 years and ₹29,282 in 4 years under compound interest. Find the rate of interest.\n\nA) 8%\nB) 10%\nC) 12%\nD) 15%",
        "options": [
            {"label": "A", "text": "8%", "is_correct": False},
            {"label": "B", "text": "10%", "is_correct": True},
            {"label": "C", "text": "12%", "is_correct": False},
            {"label": "D", "text": "15%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Interest in 4th year = 29282 - 26620 = ₹2,662.\nRate = (2662 / 26620) * 100 = 10%.",
        "tips": "For consecutive years, Rate = (Diff in Amounts / Earlier Amount) * 100."
    },
    {
        "q_num": 18,
        "title": "Compound Interest - Compounded Annually 25,000 at 8% for 3 yrs",
        "question_text": "Find the compound interest on ₹25,000 at 8% per annum for 3 years, compounded annually.\n\nA) ₹6,000\nB) ₹6,492.80\nC) ₹6,800\nD) ₹7,200",
        "options": [
            {"label": "A", "text": "₹6,000", "is_correct": False},
            {"label": "B", "text": "₹6,492.80", "is_correct": True},
            {"label": "C", "text": "₹6,800", "is_correct": False},
            {"label": "D", "text": "₹7,200", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "P = ₹25,000, R = 8%, T = 3 years\nAmount = 25000 * (1.08)^3 = 25000 * 1.259712 = ₹31,492.80.\nCI = 31492.80 - 25000 = ₹6,492.80.",
        "tips": "Multiply P by 1.259712."
    },
    {
        "q_num": 19,
        "title": "Compound Interest - Principal from 48,400 in 2 yrs at 10%",
        "question_text": "A sum of money becomes ₹48,400 in 2 years at 10% compound interest. Find the principal.\n\nA) ₹35,000\nB) ₹40,000\nC) ₹42,000\nD) ₹45,000",
        "options": [
            {"label": "A", "text": "₹35,000", "is_correct": False},
            {"label": "B", "text": "₹40,000", "is_correct": True},
            {"label": "C", "text": "₹42,000", "is_correct": False},
            {"label": "D", "text": "₹45,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "48400 = P * 1.21 => P = 48400 / 1.21 = ₹40,000.",
        "tips": "Divide by 1.21."
    },
    {
        "q_num": 20,
        "title": "Compound Interest - Principal from CI Amount 4,620",
        "question_text": "The compound interest on a certain sum for 2 years at 10% per annum is ₹4,620. Find the principal.\n\nA) ₹20,000\nB) ₹22,000\nC) ₹24,000\nD) ₹25,000",
        "options": [
            {"label": "A", "text": "₹20,000", "is_correct": False},
            {"label": "B", "text": "₹22,000", "is_correct": True},
            {"label": "C", "text": "₹24,000", "is_correct": False},
            {"label": "D", "text": "₹25,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "CI = P * [(1.10)^2 - 1] = 0.21 P.\n0.21 P = 4620 => P = 4620 / 0.21 = ₹22,000.",
        "tips": "Net CI % for 2 yrs at 10% = 21%."
    },
    {
        "q_num": 21,
        "title": "Compound Interest - Principal from 66,550 in 3 yrs at 10%",
        "question_text": "A sum invested at compound interest amounts to ₹66,550 in 3 years at 10% per annum. Find the principal.\n\nA) ₹45,000\nB) ₹50,000\nC) ₹55,000\nD) ₹60,000",
        "options": [
            {"label": "A", "text": "₹45,000", "is_correct": False},
            {"label": "B", "text": "₹50,000", "is_correct": True},
            {"label": "C", "text": "₹55,000", "is_correct": False},
            {"label": "D", "text": "₹60,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "66550 = P * (1.10)^3 = 1.331 P\n=> P = 66550 / 1.331 = ₹50,000.",
        "tips": "Divide by 1.331."
    },
    {
        "q_num": 22,
        "title": "Compound Interest - Difference CI - SI for 2 Years",
        "question_text": "Find the difference between Simple Interest and Compound Interest on ₹15,000 at 12% per annum for 2 years.\n\nA) ₹180\nB) ₹216\nC) ₹240\nD) ₹270",
        "options": [
            {"label": "A", "text": "₹180", "is_correct": False},
            {"label": "B", "text": "₹216", "is_correct": True},
            {"label": "C", "text": "₹240", "is_correct": False},
            {"label": "D", "text": "₹270", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Difference for 2 years = P * (R / 100)^2\n= 15000 * (12 / 100)^2 = 15000 * 0.0144 = ₹216.",
        "tips": "Difference for 2 years = P * (R/100)^2."
    },
    {
        "q_num": 23,
        "title": "Compound Interest - Principal from 19,965 in 3 yrs at 10%",
        "question_text": "A sum becomes ₹19,965 in 3 years at 10% compound interest. Find the principal.\n\nA) ₹12,000\nB) ₹15,000\nC) ₹16,000\nD) ₹18,000",
        "options": [
            {"label": "A", "text": "₹12,000", "is_correct": False},
            {"label": "B", "text": "₹15,000", "is_correct": True},
            {"label": "C", "text": "₹16,000", "is_correct": False},
            {"label": "D", "text": "₹18,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "19965 = P * 1.331 => P = 19965 / 1.331 = ₹15,000.",
        "tips": "Divide by 1.331."
    },
    {
        "q_num": 24,
        "title": "Compound Interest - Principal from 43,200 in 2 yrs at 20%",
        "question_text": "The amount obtained on a sum after 2 years at 20% compound interest is ₹43,200. Find the principal.\n\nA) ₹25,000\nB) ₹30,000\nC) ₹32,000\nD) ₹35,000",
        "options": [
            {"label": "A", "text": "₹25,000", "is_correct": False},
            {"label": "B", "text": "₹30,000", "is_correct": True},
            {"label": "C", "text": "₹32,000", "is_correct": False},
            {"label": "D", "text": "₹35,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "43200 = P * (1.20)^2 = 1.44 P => P = 43200 / 1.44 = ₹30,000.",
        "tips": "Divide by 1.44."
    },
    {
        "q_num": 25,
        "title": "Compound Interest - Amount on 50,000 at 8% for 3 yrs",
        "question_text": "A sum of ₹50,000 is invested at compound interest. If the rate is 8% per annum, find the amount after 3 years.\n\nA) ₹60,000\nB) ₹62,985.60\nC) ₹64,000\nD) ₹65,000",
        "options": [
            {"label": "A", "text": "₹60,000", "is_correct": False},
            {"label": "B", "text": "₹62,985.60", "is_correct": True},
            {"label": "C", "text": "₹64,000", "is_correct": False},
            {"label": "D", "text": "₹65,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Amount = 50000 * (1.08)^3 = 50000 * 1.259712 = ₹62,985.60.",
        "tips": "50000 * 1.259712 = 62985.60."
    },
    {
        "q_num": 26,
        "title": "Compound Interest - Consecutive Years Amounts Rate & Principal",
        "question_text": "A sum amounts to ₹72,600 in 2 years and ₹79,860 in 3 years under compound interest. Find the rate and principal.\n\nA) Rate = 8%, P = ₹55,000\nB) Rate = 10%, P = ₹60,000\nC) Rate = 12%, P = ₹62,000\nD) Rate = 15%, P = ₹65,000",
        "options": [
            {"label": "A", "text": "Rate = 8%, P = ₹55,000", "is_correct": False},
            {"label": "B", "text": "Rate = 10%, P = ₹60,000", "is_correct": True},
            {"label": "C", "text": "Rate = 12%, P = ₹62,000", "is_correct": False},
            {"label": "D", "text": "Rate = 15%, P = ₹65,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Interest in 3rd year = 79860 - 72600 = ₹7,260.\nRate = (7260 / 72600) * 100 = 10%.\n72600 = P * 1.21 => P = 72600 / 1.21 = ₹60,000.",
        "tips": "Rate = 10%, Principal = ₹60,000."
    },
    {
        "q_num": 27,
        "title": "Compound Interest - CI on 36,000 at 12% for 3 yrs",
        "question_text": "Find the compound interest on ₹36,000 at 12% per annum for 3 years.\n\nA) ₹12,500\nB) ₹14,577.41\nC) ₹15,000\nD) ₹16,200",
        "options": [
            {"label": "A", "text": "₹12,500", "is_correct": False},
            {"label": "B", "text": "₹14,577.41", "is_correct": True},
            {"label": "C", "text": "₹15,000", "is_correct": False},
            {"label": "D", "text": "₹16,200", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "Amount = 36000 * (1.12)^3 = 36000 * 1.404928 = ₹50,577.41.\nCI = 50577.41 - 36000 = ₹14,577.41.",
        "tips": "36000 * 0.404928 = 14577.41."
    },
    {
        "q_num": 28,
        "title": "Compound Interest - Principal from 59,290 in 3 yrs at 10%",
        "question_text": "A principal becomes ₹59,290 in 3 years at 10% compound interest. Find the principal amount invested.\n\nA) ₹40,000\nB) ₹44,545.45 (For 2 years P = ₹49,000)\nC) ₹50,000\nD) ₹52,000",
        "options": [
            {"label": "A", "text": "₹40,000", "is_correct": False},
            {"label": "B", "text": "₹44,545.45 (For 2 years P = ₹49,000)", "is_correct": True},
            {"label": "C", "text": "₹50,000", "is_correct": False},
            {"label": "D", "text": "₹52,000", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "59290 = P * (1.10)^3 = 1.331 P => P = 59290 / 1.331 = ₹44,545.45.",
        "tips": "Divide 59290 by 1.331."
    },
    {
        "q_num": 29,
        "title": "Compound Interest - Rate from 25,000 to 30,250 in 2 yrs",
        "question_text": "Find the annual rate if ₹25,000 amounts to ₹30,250 in 2 years under compound interest.\n\nA) 8%\nB) 10%\nC) 12%\nD) 15%",
        "options": [
            {"label": "A", "text": "8%", "is_correct": False},
            {"label": "B", "text": "10%", "is_correct": True},
            {"label": "C", "text": "12%", "is_correct": False},
            {"label": "D", "text": "15%", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "30250 / 25000 = 1.21\n(1 + R/100)^2 = 1.21 => 1 + R/100 = 1.10 => R = 10%.",
        "tips": "Square root of 1.21 is 1.10."
    },
    {
        "q_num": 30,
        "title": "Compound Interest - Money Tripling Compound Progression",
        "question_text": "A sum of money triples itself in 4 years under compound interest. What will be the amount after 8 years if the same rate continues?\n\nA) 6 times the principal\nB) 9 times the principal\nC) 12 times the principal\nD) 15 times the principal",
        "options": [
            {"label": "A", "text": "6 times the principal", "is_correct": False},
            {"label": "B", "text": "9 times the principal", "is_correct": True},
            {"label": "C", "text": "12 times the principal", "is_correct": False},
            {"label": "D", "text": "15 times the principal", "is_correct": False}
        ],
        "correct_option": "B",
        "sample_answer": "In 4 years, money becomes 3 times (multiplier = 3).\nIn 8 years (which is 2 periods of 4 years), money becomes 3^2 = 9 times the principal.",
        "tips": "For compound interest, growth is exponential: (n)^k where k is number of time periods."
    }
]

def seed_database():
    conn = sqlite3.connect('instance/interview_portal.db')
    cursor = conn.cursor()
    
    # Clean out existing Compound Interest questions if any
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Compound Interest'")
    print(f"Cleared previous Compound Interest questions.")
    
    for q in questions_data:
        category = "Aptitude"
        sub_category = "Commercial Mathematics"
        topic = "Compound Interest"
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
    print(f"Successfully seeded {len(questions_data)} Compound Interest questions into instance/interview_portal.db!")
    conn.close()

if __name__ == "__main__":
    seed_database()
