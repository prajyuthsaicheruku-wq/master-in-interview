import sys
import random
import json
from app import app
from models import db, Question

topics_map = {
    "Number & Arithmetic": [
        "Number System",
        "HCF & LCM",
        "Divisibility",
        "Simplification",
        "Averages",
        "Percentages",
        "Ratio & Proportion",
        "Problems on Ages"
    ],
    "Commercial Mathematics": [
        "Profit & Loss",
        "Simple Interest",
        "Compound Interest",
        "Discount"
    ],
    "Time-Based Problems": [
        "Time & Work",
        "Pipes & Cisterns",
        "Time, Speed & Distance",
        "Boats & Streams",
        "Trains"
    ],
    "Logical Reasoning": [
        "Number Series",
        "Alphabet Series",
        "Coding & Decoding",
        "Blood Relations",
        "Direction Sense"
    ],
    "Verbal Ability": [
        "Reading Comprehension",
        "Grammar",
        "Sentence Correction",
        "Para Jumbles",
        "Fill in the Blanks"
    ]
}

def build_options(correct_val, distractors):
    clean_distractors = []
    for d in distractors:
        if str(d) != str(correct_val) and str(d) not in [str(x) for x in clean_distractors]:
            clean_distractors.append(d)
    
    fallback = ["Option A", "Option B", "Option C", "Option D"]
    for f in fallback:
        if len(clean_distractors) >= 3:
            break
        if str(f) != str(correct_val) and str(f) not in [str(x) for x in clean_distractors]:
            clean_distractors.append(f)
            
    all_vals = [correct_val] + clean_distractors[:3]
    random.shuffle(all_vals)
    
    labels = ['A', 'B', 'C', 'D']
    options_list = []
    correct_label = 'A'
    
    for idx, val in enumerate(all_vals):
        lbl = labels[idx]
        is_corr = (str(val) == str(correct_val))
        if is_corr:
            correct_label = lbl
        options_list.append({
            'label': lbl,
            'text': str(val),
            'is_correct': is_corr
        })
        
    return json.dumps(options_list), correct_label

def generate_questions():
    questions = []
    
    # 1. NUMBER SYSTEM (11 Questions)
    for i in range(1, 12):
        base = random.choice([2, 3, 7, 8])
        pwr = random.choice([21, 31, 43, 65, 87, 103])
        divisor = 5
        cyclicity = 4
        rem = (base ** (pwr % 4 if pwr % 4 != 0 else 4)) % divisor
        
        c_val = str(rem)
        dist = [str((rem + 1) % 5), str((rem + 2) % 5), str((rem + 3) % 5)]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "Number System",
            "title": f"Number System - Remainder Theorem Problem {i}",
            "difficulty": random.choice(["Easy", "Medium", "Hard"]),
            "question_text": f"Find the remainder when {base}^{pwr} is divided by {divisor}.",
            "sample_answer": f"Notice cyclicity of powers of {base} mod {divisor} repeats in cycles of {cyclicity}.\n{pwr} mod 4 = {pwr % 4}.\nRemainder = ({base}^{pwr % 4 if pwr % 4 != 0 else 4}) mod {divisor} = {rem}.",
            "tips": "Unit digits and remainders for powers follow periodic cyclicity patterns of 4.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 2. HCF & LCM (11 Questions)
    for i in range(1, 12):
        r1, r2 = random.choice([(2,3), (3,4), (4,5), (3,5), (5,6)])
        hcf = random.choice([6, 12, 15, 18, 24])
        lcm = r1 * r2 * hcf
        n1 = r1 * hcf
        n2 = r2 * hcf
        
        c_val = f"HCF = {hcf}"
        dist = [f"HCF = {hcf - 2}", f"HCF = {hcf + 3}", f"HCF = {hcf * 2}"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "HCF & LCM",
            "title": f"HCF & LCM - Ratio & Product Problem {i}",
            "difficulty": random.choice(["Easy", "Medium"]),
            "question_text": f"Two numbers are in the ratio {r1}:{r2}. If their LCM is {lcm}, find their HCF.",
            "sample_answer": f"Let HCF = x. The numbers are {r1}x and {r2}x.\nLCM({r1}x, {r2}x) = {r1*r2}x = {lcm} => x = {hcf}.\nHence, HCF = {hcf}.\nThe two numbers are {n1} and {n2}.",
            "tips": "Formula: Product of Two Numbers = HCF * LCM.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 3. DIVISIBILITY (11 Questions)
    for i in range(1, 12):
        d1, d2, d3, d4 = random.sample(range(1, 9), 4)
        div = 9
        digit_sum = d1 + d2 + d3 + d4
        x_val = (div - (digit_sum % div)) % div
        
        c_val = f"x = {x_val}"
        dist = [f"x = {(x_val + 2) % 9}", f"x = {(x_val + 4) % 9}", f"x = {(x_val + 7) % 9}"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "Divisibility",
            "title": f"Divisibility Rules - Missing Digit Problem {i}",
            "difficulty": "Easy",
            "question_text": f"Find the value of x such that the number {d1}{d2}{d3}x{d4} is divisible by 9.",
            "sample_answer": f"Divisibility rule for 9: Sum of digits must be divisible by 9.\nSum of known digits = {d1} + {d2} + {d3} + {d4} = {d1+d2+d3+d4}.\nx = {x_val}.",
            "tips": "A number is divisible by 9 if the sum of all its digits is divisible by 9.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 4. SIMPLIFICATION (11 Questions)
    for i in range(1, 12):
        a = random.choice([60, 120, 180, 240, 300])
        b = random.choice([4, 5, 6, 10])
        c = random.choice([2, 3, 4])
        d = random.choice([20, 30, 40, 50])
        e = random.choice([5, 10])
        res = (a // b) * c + (d // e)
        
        c_val = f"{res}"
        dist = [f"{res - 5}", f"{res + 10}", f"{res + 20}"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "Simplification",
            "title": f"Simplification - BODMAS Rule Problem {i}",
            "difficulty": "Easy",
            "question_text": f"Evaluate the expression: {a} / {b} * {c} + {d} / {e}.",
            "sample_answer": f"Apply BODMAS order:\n1. Division: {a}/{b} = {a//b} and {d}/{e} = {d//e}.\n2. Multiplication: {a//b} * {c} = {(a//b)*c}.\n3. Addition: {(a//b)*c} + {d//e} = {res}.",
            "tips": "Always evaluate Brackets first, then Division and Multiplication from left to right.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 5. AVERAGES (11 Questions)
    for i in range(1, 12):
        n = random.choice([10, 15, 20, 25])
        old_avg = random.choice([40, 45, 50, 55, 60])
        inc = random.choice([1, 2, 3])
        new_count = n + 1
        new_avg = old_avg + inc
        teacher_wt = (new_count * new_avg) - (n * old_avg)
        
        c_val = f"{teacher_wt} kg"
        dist = [f"{teacher_wt - 5} kg", f"{teacher_wt + 10} kg", f"{teacher_wt - 12} kg"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "Averages",
            "title": f"Averages - Inclusion Weight Problem {i}",
            "difficulty": "Medium",
            "question_text": f"The average weight of {n} students is {old_avg} kg. When the teacher's weight is included, the average increases by {inc} kg. Find the weight of the teacher.",
            "sample_answer": f"Total weight of {n} students = {n} * {old_avg} = {n*old_avg} kg.\nNew total count = {new_count}.\nNew average weight = {new_avg} kg.\nTeacher Weight = {new_count*new_avg} - {n*old_avg} = {teacher_wt} kg.",
            "tips": "Teacher Weight = Old Average + (New Count * Increase in Average).",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 6. PERCENTAGES (11 Questions)
    for i in range(1, 12):
        r = random.choice([10, 20, 25, 50])
        ans_pct = round((r / (100 + r)) * 100, 2)
        
        c_val = f"{ans_pct}%"
        dist = [f"{round(ans_pct - 3.5, 2)}%", f"{round(ans_pct + 4.2, 2)}%", f"{r}%"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "Percentages",
            "title": f"Percentages - Income Comparison Problem {i}",
            "difficulty": "Easy",
            "question_text": f"If A's salary is {r}% more than B's salary, by what percentage is B's salary less than A's salary?",
            "sample_answer": f"Let B's salary = 100.\nA's salary = {100+r}.\nPercentage B is less than A = ({r} / {100+r}) * 100 = {ans_pct}%.",
            "tips": "Formula: Percentage Less = [R / (100 + R)] * 100.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 7. RATIO & PROPORTION (11 Questions)
    for i in range(1, 12):
        a, b, c = random.choice([(2,3,5), (1,2,4), (3,4,5), (2,5,8)])
        tot = random.choice([1000, 1400, 2000, 3000, 5000])
        sum_r = a + b + c
        val_b = (b * tot) // sum_r
        
        c_val = f"${val_b}"
        dist = [f"${val_b - 100}", f"${val_b + 200}", f"${val_b + 500}"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "Ratio & Proportion",
            "title": f"Ratio & Proportion - Amount Share Problem {i}",
            "difficulty": "Easy",
            "question_text": f"Divide ${tot} among A, B, and C in the ratio {a}:{b}:{c}. Find the share of B.",
            "sample_answer": f"Sum of ratios = {a} + {b} + {c} = {sum_r}.\nB's share = ({b} / {sum_r}) * ${tot} = ${val_b}.",
            "tips": "B's Share = (B's Ratio / Total Ratio Sum) * Total Amount.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 8. PROBLEMS ON AGES (11 Questions)
    for i in range(1, 12):
        r_f, r_s = random.choice([(7,2), (5,2), (4,1), (6,1)])
        yrs = random.choice([5, 10, 12, 15])
        new_f, new_s = random.choice([(2,1), (3,1)])
        father_age = 7 * yrs
        
        c_val = f"{father_age} years"
        dist = [f"{father_age - 7} years", f"{father_age + 7} years", f"{father_age + 14} years"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Number & Arithmetic",
            "topic": "Problems on Ages",
            "title": f"Problems on Ages - Ratio Comparison Problem {i}",
            "difficulty": "Medium",
            "question_text": f"The ratio of present ages of Father and Son is {r_f}:{r_s}. After {yrs} years, the ratio of their ages becomes {new_f}:{new_s}. Find the present age of the Father.",
            "sample_answer": f"Let present ages be {r_f}x and {r_s}x.\nEquation after {yrs} years: ({r_f}x + {yrs}) / ({r_s}x + {yrs}) = {new_f} / {new_s}.\nPresent age of Father = {father_age} years.",
            "tips": "Formulate linear equations comparing present ages and future ages.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 9. PROFIT & LOSS (11 Questions)
    for i in range(1, 12):
        cp = random.choice([400, 500, 800, 1000, 1200])
        profit_pct = random.choice([10, 15, 20, 25, 30])
        sp = cp + (cp * profit_pct // 100)
        
        c_val = f"{profit_pct}%"
        dist = [f"{profit_pct - 5}%", f"{profit_pct + 5}%", f"{profit_pct + 10}%"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Commercial Mathematics",
            "topic": "Profit & Loss",
            "title": f"Profit & Loss - Profit Percentage Problem {i}",
            "difficulty": "Easy",
            "question_text": f"An item bought for ${cp} is sold for ${sp}. Calculate the profit percentage.",
            "sample_answer": f"Cost Price CP = ${cp}. Selling Price SP = ${sp}.\nProfit = SP - CP = ${sp - cp}.\nProfit % = (Profit / CP) * 100 = {profit_pct}%.",
            "tips": "Profit % is always calculated on the Cost Price (CP).",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 10. SIMPLE INTEREST (11 Questions)
    for i in range(1, 12):
        p = random.choice([2000, 5000, 8000, 10000, 15000])
        r = random.choice([5, 6, 8, 10, 12])
        t = random.choice([2, 3, 4, 5])
        si = (p * r * t) // 100
        
        c_val = f"${si}"
        dist = [f"${si - 100}", f"${si + 200}", f"${si + 500}"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Commercial Mathematics",
            "topic": "Simple Interest",
            "title": f"Simple Interest - Interest Calculation Problem {i}",
            "difficulty": "Easy",
            "question_text": f"Calculate the Simple Interest on ${p} at an annual rate of {r}% for {t} years.",
            "sample_answer": f"Formula: SI = (P * R * T) / 100.\nSI = ({p} * {r} * {t}) / 100 = ${si}.\nTotal Amount = ${p + si}.",
            "tips": "SI = (Principal * Rate * Time) / 100.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 11. COMPOUND INTEREST (11 Questions)
    for i in range(1, 12):
        p = random.choice([5000, 10000, 20000])
        r = random.choice([5, 10, 20])
        t = 2
        amount = round(p * ((1 + r/100) ** t), 2)
        ci = round(amount - p, 2)
        
        c_val = f"${ci}"
        dist = [f"${round(ci - 150, 2)}", f"${round(ci + 250, 2)}", f"${round(ci * 1.25, 2)}"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Commercial Mathematics",
            "topic": "Compound Interest",
            "title": f"Compound Interest - Annual Compound Problem {i}",
            "difficulty": "Medium",
            "question_text": f"Find the Compound Interest on ${p} at {r}% per annum compounded annually for {t} years.",
            "sample_answer": f"Formula: A = P * (1 + R/100)^n.\nA = {p} * (1 + {r}/100)^{t} = ${amount}.\nCompound Interest CI = A - P = ${ci}.",
            "tips": "Compound Interest compounds on accumulated principal each period.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 12. DISCOUNT (11 Questions)
    for i in range(1, 12):
        d1 = random.choice([10, 20, 25])
        d2 = random.choice([5, 10, 15, 20])
        eq_disc = round(d1 + d2 - (d1 * d2 / 100), 2)
        
        c_val = f"{eq_disc}%"
        dist = [f"{d1 + d2}%", f"{round(eq_disc - 4.5, 2)}%", f"{round(eq_disc + 3.2, 2)}%"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Commercial Mathematics",
            "topic": "Discount",
            "title": f"Discount - Successive Discount Problem {i}",
            "difficulty": "Medium",
            "question_text": f"Successive discounts of {d1}% and {d2}% are equivalent to what single discount percentage?",
            "sample_answer": f"Formula: Single Discount = d1 + d2 - (d1*d2)/100.\n= {d1} + {d2} - ({d1}*{d2})/100 = {eq_disc}%.",
            "tips": "Single Equivalent Discount Formula = d1 + d2 - (d1*d2)/100.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 13. TIME & WORK (11 Questions)
    for i in range(1, 12):
        a_days = random.choice([10, 12, 15, 20])
        b_days = random.choice([15, 20, 30])
        tot_days = round((a_days * b_days) / (a_days + b_days), 2)
        
        c_val = f"{tot_days} days"
        dist = [f"{round(tot_days + 2.5, 2)} days", f"{round(tot_days - 1.5, 2)} days", f"{a_days + b_days} days"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Time-Based Problems",
            "topic": "Time & Work",
            "title": f"Time & Work - Work Rate Problem {i}",
            "difficulty": "Easy",
            "question_text": f"A can finish a work in {a_days} days and B can finish the same work in {b_days} days. Working together, in how many days will they finish the work?",
            "sample_answer": f"Combined 1-day work = (1/{a_days}) + (1/{b_days}).\nDays taken = ({a_days} * {b_days}) / ({a_days} + {b_days}) = {tot_days} days.",
            "tips": "Formula: Total Days = (A * B) / (A + B).",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 14. PIPES & CISTERNS (11 Questions)
    for i in range(1, 12):
        p1 = random.choice([12, 15, 20])
        p2 = random.choice([20, 30, 40])
        leak = random.choice([40, 60])
        net_rate = (1/p1) + (1/p2) - (1/leak)
        fill_time = round(1 / net_rate, 2)
        
        c_val = f"{fill_time} mins"
        dist = [f"{round(fill_time - 3.5, 2)} mins", f"{round(fill_time + 4.2, 2)} mins", f"{round(fill_time + 8, 2)} mins"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Time-Based Problems",
            "topic": "Pipes & Cisterns",
            "title": f"Pipes & Cisterns - Leak Rate Problem {i}",
            "difficulty": "Medium",
            "question_text": f"Pipe A fills a tank in {p1} mins, Pipe B fills in {p2} mins, and Pipe C empties in {leak} mins. If all 3 are opened together, how long to fill the tank?",
            "sample_answer": f"Net rate = (1/{p1}) + (1/{p2}) - (1/{leak}) = {net_rate:.4f}.\nTotal time to fill = 1 / {net_rate:.4f} = {fill_time} mins.",
            "tips": "Filling rates add (+); draining/leak rates subtract (-).",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 15. TIME, SPEED & DISTANCE (11 Questions)
    for i in range(1, 12):
        s1 = random.choice([40, 50, 60])
        s2 = random.choice([20, 30, 40])
        avg_s = round((2 * s1 * s2) / (s1 + s2), 2)
        
        c_val = f"{avg_s} km/h"
        dist = [f"{round((s1 + s2)/2, 2)} km/h", f"{round(avg_s - 5.5, 2)} km/h", f"{round(avg_s + 8, 2)} km/h"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Time-Based Problems",
            "topic": "Time, Speed & Distance",
            "title": f"Time, Speed & Distance - Average Speed Problem {i}",
            "difficulty": "Medium",
            "question_text": f"A vehicle travels to a destination at {s1} km/h and returns along the same route at {s2} km/h. Find the average speed.",
            "sample_answer": f"Average Speed = (2 * s1 * s2) / (s1 + s2) = (2 * {s1} * {s2}) / ({s1} + {s2}) = {avg_s} km/h.",
            "tips": "Average speed for equal distance = (2 * s1 * s2) / (s1 + s2).",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 16. BOATS & STREAMS (11 Questions)
    for i in range(1, 12):
        b_speed = random.choice([10, 12, 15, 18])
        s_speed = random.choice([2, 3, 4, 5])
        dist = random.choice([30, 45, 60])
        down_s = b_speed + s_speed
        up_s = b_speed - s_speed
        t_down = round(dist / down_s, 2)
        t_up = round(dist / up_s, 2)
        tot_t = round(t_down + t_up, 2)
        
        c_val = f"{tot_t} hours"
        dist = [f"{round(tot_t + 1.8, 2)} hours", f"{round(tot_t - 1.2, 2)} hours", f"{round(t_down, 2)} hours"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Time-Based Problems",
            "topic": "Boats & Streams",
            "title": f"Boats & Streams - Upstream/Downstream Problem {i}",
            "difficulty": "Medium",
            "question_text": f"Boat speed in still water is {b_speed} km/h and stream speed is {s_speed} km/h. Find total time to travel {dist} km downstream and {dist} km upstream.",
            "sample_answer": f"Downstream Speed = {down_s} km/h. Upstream Speed = {up_s} km/h.\nDownstream Time = {t_down} hrs. Upstream Time = {t_up} hrs.\nTotal Time = {tot_t} hours.",
            "tips": "Downstream Speed = Boat + Stream. Upstream Speed = Boat - Stream.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 17. TRAINS (11 Questions)
    for i in range(1, 12):
        t_len = random.choice([150, 180, 200, 250])
        speed_kmh = random.choice([36, 54, 72, 90])
        speed_ms = speed_kmh * 5 // 18
        time_sec = random.choice([15, 20, 25, 30])
        tot_dist = speed_ms * time_sec
        plat_len = max(0, tot_dist - t_len)
        
        c_val = f"{plat_len} meters"
        dist = [f"{plat_len + 50} meters", f"{plat_len - 30} meters", f"{tot_dist} meters"]
        opts_json, corr_lbl = build_options(c_val, dist)
        
        questions.append({
            "category": "Aptitude",
            "sub_category": "Time-Based Problems",
            "topic": "Trains",
            "title": f"Trains - Train Crossing Platform Problem {i}",
            "difficulty": "Medium",
            "question_text": f"A {t_len}m long train running at {speed_kmh} km/h crosses a platform in {time_sec} seconds. Find the length of the platform.",
            "sample_answer": f"Speed in m/s = {speed_kmh} * (5/18) = {speed_ms} m/s.\nTotal distance = {speed_ms} * {time_sec} = {tot_dist}m.\nPlatform Length = {tot_dist} - {t_len} = {plat_len}m.",
            "tips": "Convert km/h to m/s by multiplying by 5/18.",
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 18. NUMBER SERIES (11 Questions - MEDIUM & HARD)
    ns_medium_hard = [
        ("Find the next number in the series: 2, 10, 30, 68, 130, 222, ?", "350", ["336", "342", "364"], "Hard", "Pattern: n^3 + n (1^3+1=2, 2^3+2=10, 3^3+3=30, 4^3+4=68, 5^3+5=130, 6^3+6=222, 7^3+7=350).", "Recognize cubic progression n^3 + n."),
        ("Find the next number in the series: 3, 7, 16, 35, 74, ?", "153", ["148", "150", "160"], "Medium", "Pattern: *2 + 1, *2 + 2, *2 + 3, *2 + 4, *2 + 5.\n74 * 2 + 5 = 153.", "Look for multiplying factor plus increasing integer constants."),
        ("Find the next prime square in the series: 4, 9, 25, 49, 121, 169, ?", "289", ["225", "256", "361"], "Hard", "Pattern: Squares of consecutive prime numbers (2^2, 3^2, 5^2, 7^2, 11^2, 13^2, 17^2 = 289).", "Identify prime number sequences squared."),
        ("Find the missing number: 6, 13, 28, 59, 122, ?", "249", ["244", "248", "254"], "Medium", "Pattern: *2 + 1, *2 + 2, *2 + 3, *2 + 4, *2 + 5.\n122 * 2 + 5 = 249.", "Check double plus incremental integer addition."),
        ("Find the missing term: 1, 4, 27, 25, 3125, ?", "36", ["49", "64", "216"], "Hard", "Pattern: Alternating powers: 1^1=1, 2^2=4, 3^3=27, 5^2=25... Even positions are n^2, odd positions are n^3.", "Alternating squares and cubes.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = ns_medium_hard[(i-1) % len(ns_medium_hard)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Logical Reasoning",
            "topic": "Number Series",
            "title": f"Number Series - Advanced Pattern Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 19. ALPHABET SERIES (11 Questions - MEDIUM & HARD)
    as_medium_hard = [
        ("Find the next letter pair in the series: AZ, CX, EV, GT, IR, ?", "KP", ["JQ", "LO", "MN"], "Medium", "Opposite alphabet pairs: A(1)-Z(26), C(3)-X(24), E(5)-V(22), G(7)-T(20), I(9)-R(18), K(11)-P(16).", "A+Z=27, C+X=27. Opposite pairs sum to 27."),
        ("Find the next term in the series: C4X, F9U, I16R, L25O, ?", "O36L", ["N36M", "P49K", "O49L"], "Hard", "First letters: C, F, I, L, (+3) -> O.\nNumbers: 2^2, 3^2, 4^2, 5^2 -> 6^2 = 36.\nLast letters: X, U, R, O (-3) -> L.", "Deconstruct alphanumeric terms into 3 separate progressions."),
        ("Find the next cluster in the series: BCF, CDG, DEH, EFI, ?", "FGJ", ["FGI", "GHK", "EFJ"], "Medium", "First letters: B, C, D, E -> F.\nSecond letters: C, D, E, F -> G.\nThird letters: F, G, H, I -> J.", "Track relative letter shifts across letter positions."),
        ("Find the next pair: ZA, YB, XC, WD, ?", "VE", ["UF", "TG", "SH"], "Hard", "First letter decreases: Z, Y, X, W -> V.\nSecond letter increases: A, B, C, D -> E.", "Opposite letter movements from ends of alphabet.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = as_medium_hard[(i-1) % len(as_medium_hard)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Logical Reasoning",
            "topic": "Alphabet Series",
            "title": f"Alphabet Series - Alphanumeric Matrix Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 20. CODING & DECODING (11 Questions - MEDIUM & HARD)
    cd_medium_hard = [
        ("In a certain code language, 'COMPUTER' is coded as 'RFUVQNPC'. How is 'MEDICINE' written in that code?", "EOJDJEFM", ["EOJDEJFM", "MFEJDJOE", "FNEJPIDM"], "Hard", "Reverse 'COMPUTER' -> 'RETUPMOC', then shift each letter by +1 -> R+1=S, E+1=F... -> 'RFUVQNPC'.\nApplying to 'MEDICINE': Reverse -> 'ENICIDEM', shift +1 -> 'EOJDJEFM'.", "Reverse the word first, then apply letter position shift."),
        ("If 'pit dar na' means 'good morning sir', 'na tok ja' means 'sir is great', and 'tok pit' means 'good is', which word stands for 'sir'?", "na", ["pit", "tok", "dar"], "Medium", "'sir' appears in statements 1 and 2. Common code word in both is 'na'.", "Find intersecting words across coded sentences."),
        ("In a code, 'DELHI' is coded as '25' (sum of alphabet positions: D=4, E=5, L=12, H=8, I=9 = 38? Wait: 4+5+12+8+9 = 38). If 'DELHI' = 38, what is the code for 'MUMBAI'?", "73", ["65", "68", "80"], "Hard", "Sum of letter positions: M(13) + U(21) + M(13) + B(2) + A(1) + I(9) = 73.", "Sum alphabetical positions of letters (A=1...Z=26).")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = cd_medium_hard[(i-1) % len(cd_medium_hard)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Logical Reasoning",
            "topic": "Coding & Decoding",
            "title": f"Coding & Decoding - Matrix Cipher Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 21. BLOOD RELATIONS (11 Questions - MEDIUM & HARD)
    br_medium_hard = [
        ("If 'A + B' means A is father of B; 'A - B' means A is sister of B; 'A * B' means A is brother of B. Which equation proves P is the nephew of Q?", "Q * R + P", ["Q + R - P", "P + Q * R", "Q - R * P"], "Hard", "Q * R => Q is brother of R. R + P => R is father of P. Thus P is child of R, making P the nephew of Q.", "Use operator symbols (+, -, *) to build genealogical equations."),
        ("In a family of 6 persons (A, B, C, D, E, F), D is grandmother of A and mother of B. C is wife of B and mother of F. How is C related to D?", "Daughter-in-law", ["Daughter", "Mother", "Sister-in-law"], "Hard", "D is mother of B. B is married to C. Therefore C is the wife of D's son B => Daughter-in-law.", "Build generational levels (Grandparents -> Parents -> Children)."),
        ("Pointing to a man, a woman says: 'His mother is the only daughter of my mother.' How is the woman related to the man?", "Mother", ["Sister", "Grandmother", "Aunt"], "Medium", "'Only daughter of my mother' = The woman herself. Thus 'His mother' = The woman. She is his Mother.", "Deconstruct possessive clauses starting from 'my mother'.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = br_medium_hard[(i-1) % len(br_medium_hard)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Logical Reasoning",
            "topic": "Blood Relations",
            "title": f"Blood Relations - Coded Family Tree Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 22. DIRECTION SENSE (11 Questions - MEDIUM & HARD)
    ds_medium_hard = [
        ("A man is facing West. He turns 45° clockwise, then 180° in the same direction, and then 270° anti-clockwise. Which direction is he facing now?", "South-West", ["North-West", "South-East", "North-East"], "Hard", "Initial = 270° (West).\nClockwise turns = +45° + 180° = +225°.\nAnti-clockwise turn = -270°.\nNet turn = +225° - 270° = -45° (Anti-clockwise 45° from West) = South-West.", "Add clockwise (+) and subtract anti-clockwise (-) angles."),
        ("One morning after sunrise, Suresh was facing a pole. The shadow of the pole fell exactly to his right. Which direction was Suresh facing?", "South", ["North", "East", "West"], "Hard", "In morning, Sun is in East, so shadows fall towards West.\nIf shadow falls to Suresh's right, his right is West. Thus he is facing South.", "Morning shadow falls WEST; evening shadow falls EAST."),
        ("A person walks 8 km South, turns West and walks 6 km, then turns North and walks 16 km, and finally turns East and walks 12 km to reach point B. What is the shortest distance between start point A and B?", "10 km", ["14 km", "12 km", "8 km"], "Hard", "Net North-South displacement = 16 N - 8 S = 8 km North.\nNet East-West displacement = 12 E - 6 W = 6 km East.\nShortest distance = sqrt(8^2 + 6^2) = sqrt(64 + 36) = sqrt(100) = 10 km.", "Use Pythagoras Theorem sqrt(x^2 + y^2) for net vector displacement.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = ds_medium_hard[(i-1) % len(ds_medium_hard)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Logical Reasoning",
            "topic": "Direction Sense",
            "title": f"Direction Sense - Vector & Angle Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 23. READING COMPREHENSION (11 Questions)
    rc_questions = [
        ("Passage: Artificial Intelligence is reshaping modern industries by automating repetitive tasks and driving data-driven decisions. However, ethical concerns regarding data privacy and job displacement remain paramount.\n\nQuestion: What is the main theme of the passage?", "AI offers industry innovation alongside privacy and job displacement concerns", ["AI will eliminate all human employment within five years", "Data privacy is no longer a concern in modern technology", "Automation is inefficient in corporate environments"], "Medium", "The passage highlights both the advantages (automation) and critical ethical concerns (privacy & displacement).", "Identify the balanced central theme combining main ideas."),
        ("Passage: Renewable energy sources, such as solar and wind, have experienced exponential growth due to falling hardware costs and global climate policies. Despite these advances, grid storage capacity remains a critical bottleneck.\n\nQuestion: What obstacle is hindering full renewable energy adoption?", "Insufficient grid storage capacity", ["High manufacturing costs of solar panels", "Lack of public interest in clean energy", "Restrictive international trade policies"], "Hard", "The passage explicitly states 'grid storage capacity remains a critical bottleneck'.", "Scan for key terms like 'obstacle', 'bottleneck', or 'limitation'."),
        ("Passage: Remote work has fundamentally altered urban economics, reducing commercial real estate demand while boosting suburban housing markets. Companies now emphasize output over desk presence.\n\nQuestion: Which shift is highlighted in corporate strategy?", "Focusing on output rather than physical presence", ["Mandating 5-day office attendance", "Increasing commercial real estate investment", "Reducing employee compensation"], "Medium", "The passage notes companies 'emphasize output over desk presence'.", "Match paraphrased statements to explicit passage facts.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = rc_questions[(i-1) % len(rc_questions)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Verbal Ability",
            "topic": "Reading Comprehension",
            "title": f"Reading Comprehension - Passage Analysis Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 24. GRAMMAR (11 Questions)
    grammar_questions = [
        ("Choose the correct word to complete the sentence: 'Neither the manager nor the employees ___ present at the emergency briefing.'", "were", ["was", "is", "are being"], "Medium", "When subjects are joined by 'neither... nor', the verb agrees with the subject closer to it ('employees' is plural => 'were').", "Rule of Proximity: Verb agrees with the nearest subject in 'neither/nor' structures."),
        ("Choose the correct tense: 'By the time the train arrived at the station, we ___ for over two hours.'", "had been waiting", ["waited", "have waited", "are waiting"], "Hard", "Past Perfect Continuous tense ('had been waiting') expresses an action continuing up to a specific past event.", "Use Past Perfect Continuous for ongoing past actions prior to another past moment."),
        ("Select the correct preposition: 'The candidate was thoroughly proficient ___ three programming languages.'", "in", ["at", "with", "on"], "Easy", "The adjective 'proficient' is correctly followed by the preposition 'in'.", "Common Collocation: Proficient IN a subject or skill.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = grammar_questions[(i-1) % len(grammar_questions)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Verbal Ability",
            "topic": "Grammar",
            "title": f"Grammar - Rules & Agreement Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 25. SENTENCE CORRECTION (11 Questions)
    sc_questions = [
        ("Improve the underlined phrase: 'He had scarcely entered the room *than the fire alarm rang*.'", "when the fire alarm rang", ["than the fire alarm rang", "and then the alarm rang", "while the alarm rang"], "Medium", "'Scarcely' and 'Hardly' are paired with 'when', not 'than'. Correct expression: 'when the fire alarm rang'.", "Correlative conjunction rule: Scarcely... when / Hardly... when."),
        ("Choose the error-free version of the sentence:", "The committee has submitted its recommendations to the board.", ["The committee have submitted its recommendations to the board.", "The committee has submitted their recommendations to the board.", "The committee are submitted its recommendations to the board."], "Hard", "Collective noun 'committee' acting as a unified body takes singular verb 'has' and singular pronoun 'its'.", "Unified collective nouns take singular verbs and singular pronouns."),
        ("Correct the sentence: 'One of the student in our class have won the national award.'", "One of the students in our class has won the national award.", ["One of the student in our class has won the national award.", "One of the students in our class have won the national award.", "One of the student in our class have won the national award."], "Medium", "'One of the' is followed by a plural noun ('students') and a singular verb ('has').", "'One of the + Plural Noun + Singular Verb'.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = sc_questions[(i-1) % len(sc_questions)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Verbal Ability",
            "topic": "Sentence Correction",
            "title": f"Sentence Correction - Idiomatic Improvement Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 26. PARA JUMBLES (11 Questions)
    pj_questions = [
        ("Rearrange the sentences into a coherent paragraph:\nP: This rapid development has transformed human communication.\nQ: Technology has advanced at an unprecedented rate over the past decade.\nR: Consequently, individuals across the globe can connect instantly.\nS: Moreover, it has unlocked new avenues in international trade.", "QPSR", ["PQRS", "RQPS", "SQPR"], "Hard", "Sentence Q introduces the general theme (Technology advance). P elaborates on communication. S adds 'Moreover' for business. R concludes with 'Consequently'. Correct order: QPSR.", "Identify the independent opening sentence introducing the topic."),
        ("Rearrange the sentences:\nP: Furthermore, regular physical exercise reduces stress levels.\nQ: Maintaining a balanced lifestyle is essential for overall well-being.\nR: Healthy nutrition provides the body with necessary nutrients.\nS: Together, these habits promote long-term vitality.", "QRPS", ["QRP-S", "PQRS", "SRQP"], "Medium", "Q sets topic. R discusses nutrition. P adds exercise with 'Furthermore'. S summarizes with 'Together'. Correct order: QRPS.", "Look for connecting transition words like 'Furthermore' and 'Together'."),
        ("Rearrange the sentences:\nP: As a result, renewable energy is becoming cost-competitive.\nQ: Solar and wind technologies have seen major efficiency gains.\nR: Governments worldwide are increasing subsidies for clean power.\nS: This shift is reducing reliance on fossil fuels.", "RQPS", ["PQRS", "QPSR", "SQPR"], "Hard", "R sets government action. Q elaborates technology gains. P states 'As a result'. S concludes 'This shift'. Correct order: RQPS.", "Trace cause-and-effect relationships across sentences.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = pj_questions[(i-1) % len(pj_questions)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Verbal Ability",
            "topic": "Para Jumbles",
            "title": f"Para Jumbles - Paragraph Sequence Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    # 27. FILL IN THE BLANKS (11 Questions)
    fib_questions = [
        ("Fill in the blank with the most appropriate word: 'The executive was reluctant to ___ confidential financial audits to the press.'", "divulge", ["conceal", "suppress", "withhold"], "Medium", "'Divulge' means to disclose or make known private/confidential information.", "Choose words that match the context of revealing secrets."),
        ("Fill in the blank: 'Despite facing fierce competition, the startup managed to ___ a lucrative niche in the market.'", "carve out", ["give up", "break down", "turn off"], "Medium", "The phrasal verb 'carve out' means to establish or create a unique position/niche through effort.", "Contextual phrasal verb collocation: Carve out a niche."),
        ("Fill in the blank: 'The scientist's groundbreaking research provided a ___ solution to a long-standing environmental challenge.'", "viable", ["futile", "redundant", "trivial"], "Hard", "'Viable' means capable of working successfully or feasible.", "Antonym clue: 'Groundbreaking research' demands a positive, practical adjective like 'viable'.")
    ]
    for i in range(1, 12):
        q_txt, c_val, dist, diff, ans, tip = fib_questions[(i-1) % len(fib_questions)]
        opts_json, corr_lbl = build_options(c_val, dist)
        questions.append({
            "category": "Aptitude",
            "sub_category": "Verbal Ability",
            "topic": "Fill in the Blanks",
            "title": f"Fill in the Blanks - Vocabulary & Collocation Problem {i}",
            "difficulty": diff,
            "question_text": q_txt,
            "sample_answer": ans,
            "tips": tip,
            "options": opts_json,
            "correct_option": corr_lbl
        })

    return questions

def seed_generated_questions():
    with app.app_context():
        # First run seed.py to create tables and seed non-aptitude questions
        try:
            from seed import seed_db
            seed_db()
        except Exception as e:
            print("Note: seed_db error:", e)

        # Remove default placeholder aptitude questions from seed.py
        Question.query.filter_by(category='Aptitude').delete()
        db.session.commit()

        # Seed full 297 Aptitude, Reasoning & Verbal questions across all 27 sub-topics
        qs = generate_questions()
        print(f"Generated {len(qs)} Aptitude, Reasoning & Verbal questions with realistic multiple choice options!")
        for q_data in qs:
            q = Question(**q_data)
            db.session.add(q)
        db.session.commit()
        print("Successfully committed 297 Aptitude, Reasoning & Verbal questions with realistic options!")

if __name__ == "__main__":
    seed_generated_questions()
