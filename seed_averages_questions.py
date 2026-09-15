import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db')

questions = [
    {
        "title": "Averages - Salary of New Employee",
        "difficulty": "Medium",
        "question_text": "The average salary of 8 employees in a company is ₹32,000. If a new employee joins the company, the average salary becomes ₹33,500. Find the salary of the new employee.",
        "sample_answer": "Total salary of 8 employees = 8 × 32,000 = ₹2,56,000.\nTotal salary of 9 employees = 9 × 33,500 = ₹3,01,500.\nNew employee's salary = 3,01,500 − 2,56,000 = ₹45,500.",
        "tips": "New Total − Old Total.",
        "options": [
            {"label": "A", "text": "₹42,000", "is_correct": False},
            {"label": "B", "text": "₹44,000", "is_correct": False},
            {"label": "C", "text": "₹45,500", "is_correct": True},
            {"label": "D", "text": "₹46,000", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Student Marks Replacement",
        "difficulty": "Medium",
        "question_text": "The average marks of 12 students is 68. If one student who scored 74 is replaced by another student, the average becomes 70. Find the marks of the new student.",
        "sample_answer": "Old total = 12 × 68 = 816.\nNew total = 12 × 70 = 840.\nIncrease = 840 − 816 = 24.\nNew student's marks = 74 + 24 = 98.",
        "tips": "New Marks = Old Marks + (Total Count × Increase in Average).",
        "options": [
            {"label": "A", "text": "96", "is_correct": False},
            {"label": "B", "text": "98", "is_correct": True},
            {"label": "C", "text": "100", "is_correct": False},
            {"label": "D", "text": "102", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Largest of Five Consecutive Integers",
        "difficulty": "Medium",
        "question_text": "The average of five consecutive integers is 42. What is the largest number?",
        "sample_answer": "For an odd number of consecutive integers, the average is the middle number.\nMiddle number = 42.\nFive numbers: 40, 41, 42, 43, 44.\nLargest number = 44.",
        "tips": "Middle term is 42.",
        "options": [
            {"label": "A", "text": "43", "is_correct": False},
            {"label": "B", "text": "44", "is_correct": True},
            {"label": "C", "text": "45", "is_correct": False},
            {"label": "D", "text": "46", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Age after Person Leaves",
        "difficulty": "Medium",
        "question_text": "The average age of 6 people is 24 years. If one person aged 30 leaves the group, what will be the new average age?",
        "sample_answer": "Total age = 6 × 24 = 144.\nRemaining age = 144 − 30 = 114.\nNew average = 114 / 5 = 22.8 years.",
        "tips": "Divide remaining age sum by 5.",
        "options": [
            {"label": "A", "text": "22.2 years", "is_correct": False},
            {"label": "B", "text": "22.4 years", "is_correct": False},
            {"label": "C", "text": "22.8 years", "is_correct": True},
            {"label": "D", "text": "23 years", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Average of First 20 Natural Numbers",
        "difficulty": "Medium",
        "question_text": "What is the average of the first 20 natural numbers?",
        "sample_answer": "Formula: (n + 1) / 2 = (20 + 1) / 2 = 21 / 2 = 10.5.",
        "tips": "Average of first n natural numbers is (n+1)/2.",
        "options": [
            {"label": "A", "text": "10", "is_correct": False},
            {"label": "B", "text": "10.5", "is_correct": True},
            {"label": "C", "text": "11", "is_correct": False},
            {"label": "D", "text": "11.5", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Average Speed for Equal Distances",
        "difficulty": "Medium",
        "question_text": "A person travels 120 km at 40 km/h and another 120 km at 60 km/h. What is the average speed for the entire journey?",
        "sample_answer": "Total distance = 120 + 120 = 240 km.\nTotal time = (120 / 40) + (120 / 60) = 3 + 2 = 5 hours.\nAverage speed = 240 / 5 = 48 km/h.",
        "tips": "Harmonic Mean: 2ab / (a + b).",
        "options": [
            {"label": "A", "text": "45 km/h", "is_correct": False},
            {"label": "B", "text": "48 km/h", "is_correct": True},
            {"label": "C", "text": "50 km/h", "is_correct": False},
            {"label": "D", "text": "52 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Weight of Teacher Included",
        "difficulty": "Medium",
        "question_text": "The average weight of 15 students is 48 kg. If the teacher's weight is included, the average increases to 50 kg. Find the teacher's weight.",
        "sample_answer": "Students' total weight = 15 × 48 = 720 kg.\nNew total = 16 × 50 = 800 kg.\nTeacher's weight = 800 − 720 = 80 kg.",
        "tips": "New total − Students' total.",
        "options": [
            {"label": "A", "text": "75 kg", "is_correct": False},
            {"label": "B", "text": "78 kg", "is_correct": False},
            {"label": "C", "text": "80 kg", "is_correct": True},
            {"label": "D", "text": "82 kg", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Average of Even Numbers from 12 to 40",
        "difficulty": "Medium",
        "question_text": "What is the average of all even numbers from 12 to 40?",
        "sample_answer": "For an AP, Average = (First term + Last term) / 2 = (12 + 40) / 2 = 52 / 2 = 26.",
        "tips": "(12 + 40) / 2.",
        "options": [
            {"label": "A", "text": "24", "is_correct": False},
            {"label": "B", "text": "25", "is_correct": False},
            {"label": "C", "text": "26", "is_correct": True},
            {"label": "D", "text": "27", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - New Number Added to 7 Numbers",
        "difficulty": "Medium",
        "question_text": "The average of 7 numbers is 25. If another number is added, the average becomes 28. Find the new number.",
        "sample_answer": "Old total = 7 × 25 = 175.\nNew total = 8 × 28 = 224.\nNew number = 224 − 175 = 49.",
        "tips": "8 * 28 - 7 * 25.",
        "options": [
            {"label": "A", "text": "45", "is_correct": False},
            {"label": "B", "text": "46", "is_correct": False},
            {"label": "C", "text": "47", "is_correct": False},
            {"label": "D", "text": "49", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - Largest of Three Related Numbers",
        "difficulty": "Medium",
        "question_text": "The average of three numbers is 42. The first number is twice the second, and the second is twice the third. Find the largest number.",
        "sample_answer": "Let third number = x, second = 2x, first = 4x.\nSum = 4x + 2x + x = 7x.\nAverage = 7x / 3 = 42 => 7x = 126 => x = 18.\nLargest number = 4x = 4(18) = 72.",
        "tips": "7x = 126.",
        "options": [
            {"label": "A", "text": "60", "is_correct": False},
            {"label": "B", "text": "72", "is_correct": True},
            {"label": "C", "text": "84", "is_correct": False},
            {"label": "D", "text": "96", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Marks Needed for Desired Average",
        "difficulty": "Medium",
        "question_text": "A student scored 72, 68, 81, 75 and 84 in five subjects. What minimum mark must the student score in the sixth subject to obtain an average of 75?",
        "sample_answer": "Current total = 72 + 68 + 81 + 75 + 84 = 380.\nRequired total for 6 subjects = 6 × 75 = 450.\nRequired mark = 450 − 380 = 70.",
        "tips": "450 - 380.",
        "options": [
            {"label": "A", "text": "70", "is_correct": True},
            {"label": "B", "text": "72", "is_correct": False},
            {"label": "C", "text": "74", "is_correct": False},
            {"label": "D", "text": "75", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Averages - Age after Student Replacement",
        "difficulty": "Medium",
        "question_text": "The average age of 10 students is 18 years. One student aged 16 leaves and another student joins. The new average is 18.5 years. Find the age of the new student.",
        "sample_answer": "Old total = 10 × 18 = 180.\nNew total = 10 × 18.5 = 185.\nIncrease = 5.\nNew student's age = 16 + 5 = 21 years.",
        "tips": "16 + 10 * (18.5 - 18).",
        "options": [
            {"label": "A", "text": "20", "is_correct": False},
            {"label": "B", "text": "21", "is_correct": True},
            {"label": "C", "text": "22", "is_correct": False},
            {"label": "D", "text": "23", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Increasing Each Number by a Constant",
        "difficulty": "Medium",
        "question_text": "The average of 9 numbers is 45. If each number is increased by 5, what will be the new average?",
        "sample_answer": "If every number in a data set is increased by a constant k, the average also increases by k.\nNew average = 45 + 5 = 50.",
        "tips": "New Average = Old Average + Constant.",
        "options": [
            {"label": "A", "text": "45", "is_correct": False},
            {"label": "B", "text": "48", "is_correct": False},
            {"label": "C", "text": "50", "is_correct": True},
            {"label": "D", "text": "55", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Monthly Expenditure Target",
        "difficulty": "Medium",
        "question_text": "A person spends ₹8,000, ₹9,500, ₹7,500 and ₹10,000 in four months. How much should he spend in the fifth month so that his average monthly expenditure becomes ₹9,000?",
        "sample_answer": "Required total = 5 × 9000 = ₹45,000.\nExisting total = 8000 + 9500 + 7500 + 10000 = ₹35,000.\nFifth month expenditure = 45,000 − 35,000 = ₹10,000.",
        "tips": "45000 - 35000.",
        "options": [
            {"label": "A", "text": "₹9,000", "is_correct": False},
            {"label": "B", "text": "₹9,500", "is_correct": False},
            {"label": "C", "text": "₹10,000", "is_correct": True},
            {"label": "D", "text": "₹10,500", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Smallest of Seven Consecutive Odd Numbers",
        "difficulty": "Medium",
        "question_text": "The average of seven consecutive odd numbers is 35. Find the smallest number.",
        "sample_answer": "Middle (4th) number = 35.\nSeven numbers: 29, 31, 33, 35, 37, 39, 41.\nSmallest number = 29.",
        "tips": "Smallest = Middle − 3 × 2 = 35 − 6 = 29.",
        "options": [
            {"label": "A", "text": "27", "is_correct": False},
            {"label": "B", "text": "29", "is_correct": True},
            {"label": "C", "text": "31", "is_correct": False},
            {"label": "D", "text": "33", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # QUESTIONS 16 TO 30
    {
        "title": "Averages - Weight Replacement in Group of 20",
        "difficulty": "Hard",
        "question_text": "The average weight of 20 students is 55 kg. One student weighing 45 kg leaves the group and another student joins. The average increases by 1.5 kg. Find the weight of the new student.",
        "sample_answer": "Old total = 20 × 55 = 1100 kg.\nNew average = 55 + 1.5 = 56.5 kg.\nNew total = 20 × 56.5 = 1130 kg.\nDifference = 1130 − 1100 = 30 kg.\nNew student's weight = 45 + 30 = 75 kg.",
        "tips": "45 + (20 * 1.5) = 75.",
        "options": [
            {"label": "A", "text": "72 kg", "is_correct": False},
            {"label": "B", "text": "74 kg", "is_correct": False},
            {"label": "C", "text": "75 kg", "is_correct": True},
            {"label": "D", "text": "76 kg", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Combined Average of Two Groups",
        "difficulty": "Hard",
        "question_text": "The average age of 20 boys is 18 years and the average age of 30 girls is 16 years. Find the average age of the entire group.",
        "sample_answer": "Total age of boys = 20 × 18 = 360.\nTotal age of girls = 30 × 16 = 480.\nCombined total = 360 + 480 = 840.\nTotal students = 20 + 30 = 50.\nCombined average = 840 / 50 = 16.8 years.",
        "tips": "Weighted average formula.",
        "options": [
            {"label": "A", "text": "16.4 years", "is_correct": False},
            {"label": "B", "text": "16.6 years", "is_correct": False},
            {"label": "C", "text": "16.8 years", "is_correct": True},
            {"label": "D", "text": "17 years", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Average Speed for Two Equal Halves",
        "difficulty": "Hard",
        "question_text": "A car travels the first half of a journey at 40 km/h and the second half at 60 km/h. Find the average speed.",
        "sample_answer": "For equal distances, Average speed = 2ab / (a + b) = 2(40)(60) / (40 + 60) = 4800 / 100 = 48 km/h.",
        "tips": "Harmonic Mean formula.",
        "options": [
            {"label": "A", "text": "45 km/h", "is_correct": False},
            {"label": "B", "text": "48 km/h", "is_correct": True},
            {"label": "C", "text": "50 km/h", "is_correct": False},
            {"label": "D", "text": "52 km/h", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Manager's Income Included",
        "difficulty": "Hard",
        "question_text": "The average income of 8 employees is ₹25,000. If the manager's income is included, the average becomes ₹32,000. Find the manager's income.",
        "sample_answer": "Old total = 8 × 25,000 = ₹2,00,000.\nNew total = 9 × 32,000 = ₹2,88,000.\nManager's income = 2,88,000 − 2,00,000 = ₹88,000.",
        "tips": "9 * 32000 - 8 * 25000.",
        "options": [
            {"label": "A", "text": "₹80,000", "is_correct": False},
            {"label": "B", "text": "₹82,000", "is_correct": False},
            {"label": "C", "text": "₹84,000", "is_correct": False},
            {"label": "D", "text": "₹88,000", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Averages - Average of First 30 Multiples of 7",
        "difficulty": "Hard",
        "question_text": "Find the average of the first 30 multiples of 7.",
        "sample_answer": "First multiple = 7, 30th multiple = 7 × 30 = 210.\nAverage = (7 + 210) / 2 = 217 / 2 = 108.5.",
        "tips": "(7 + 210) / 2.",
        "options": [
            {"label": "A", "text": "105", "is_correct": False},
            {"label": "B", "text": "107.5", "is_correct": False},
            {"label": "C", "text": "108.5", "is_correct": True},
            {"label": "D", "text": "109", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Correct Average after Misread Mark",
        "difficulty": "Hard",
        "question_text": "The average marks of 25 students is 64. If the marks of one student were wrongly recorded as 48 instead of 84, what is the correct average?",
        "sample_answer": "Recorded total = 25 × 64 = 1600.\nCorrection = 84 − 48 = +36.\nCorrect total = 1600 + 36 = 1636.\nCorrect average = 1636 / 25 = 65.44.",
        "tips": "Old Average + (Difference / Count) = 64 + 36/25 = 65.44.",
        "options": [
            {"label": "A", "text": "64.44", "is_correct": False},
            {"label": "B", "text": "65.12", "is_correct": False},
            {"label": "C", "text": "65.44", "is_correct": True},
            {"label": "D", "text": "66.44", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Product of Smallest and Largest of 11 Integers",
        "difficulty": "Hard",
        "question_text": "The average of 11 consecutive integers is 56. What is the product of the smallest and largest integers?",
        "sample_answer": "Middle (6th) number = 56.\nSmallest = 56 − 5 = 51.\nLargest = 56 + 5 = 61.\nProduct = 51 × 61 = 3111.",
        "tips": "51 * 61 = 3111.",
        "options": [
            {"label": "A", "text": "3011", "is_correct": False},
            {"label": "B", "text": "3111", "is_correct": True},
            {"label": "C", "text": "3211", "is_correct": False},
            {"label": "D", "text": "3311", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Average after Removing Two Numbers",
        "difficulty": "Hard",
        "question_text": "The average of 12 numbers is 40. If two numbers, 48 and 52, are removed, what will be the average of the remaining numbers?",
        "sample_answer": "Original total = 12 × 40 = 480.\nSum of removed numbers = 48 + 52 = 100.\nRemaining sum = 480 − 100 = 380.\nRemaining numbers = 10.\nNew average = 380 / 10 = 38.",
        "tips": "380 / 10.",
        "options": [
            {"label": "A", "text": "36", "is_correct": False},
            {"label": "B", "text": "37", "is_correct": False},
            {"label": "C", "text": "38", "is_correct": True},
            {"label": "D", "text": "39", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Teacher's Age with Double Inclusion",
        "difficulty": "Hard",
        "question_text": "The average age of 15 students is 20 years. When the teacher's age is included, the average becomes 22 years. Find the age of the teacher.",
        "sample_answer": "Students' total age = 15 × 20 = 300.\nTotal with teacher = 16 × 22 = 352.\nTeacher's age = 352 − 300 = 52 years.",
        "tips": "352 - 300.",
        "options": [
            {"label": "A", "text": "50", "is_correct": False},
            {"label": "B", "text": "51", "is_correct": False},
            {"label": "C", "text": "52", "is_correct": True},
            {"label": "D", "text": "53", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Largest of 8 Consecutive Even Numbers",
        "difficulty": "Hard",
        "question_text": "The average of 8 consecutive even numbers is 31. What is the largest number?",
        "sample_answer": "The average 31 lies midway between the 4th (30) and 5th (32) even numbers.\nEight numbers: 24, 26, 28, 30, 32, 34, 36, 38.\nLargest number = 38.",
        "tips": "31 + 7 = 38.",
        "options": [
            {"label": "A", "text": "36", "is_correct": False},
            {"label": "B", "text": "37", "is_correct": False},
            {"label": "C", "text": "38", "is_correct": True},
            {"label": "D", "text": "39", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Salary of Third New Employee",
        "difficulty": "Hard",
        "question_text": "The average salary of 12 employees is ₹28,000. When 3 new employees join, the average salary becomes ₹30,000. If two of the new employees earn ₹32,000 and ₹35,000 respectively, find the salary of the third employee.",
        "sample_answer": "Old total = 12 × 28,000 = ₹3,36,000.\nNew total = 15 × 30,000 = ₹4,50,000.\nTotal of 3 new employees = 4,50,000 − 3,36,000 = ₹1,14,000.\nThird employee's salary = 1,14,000 − 32,000 − 35,000 = ₹47,000.",
        "tips": "114000 - 32000 - 35000.",
        "options": [
            {"label": "A", "text": "₹45,000", "is_correct": False},
            {"label": "B", "text": "₹46,000", "is_correct": False},
            {"label": "C", "text": "₹47,000", "is_correct": True},
            {"label": "D", "text": "₹48,000", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Average Speed for Three Equal Distances",
        "difficulty": "Hard",
        "question_text": "A person travels equal distances at 30 km/h, 40 km/h and 60 km/h. What is his average speed?",
        "sample_answer": "Harmonic Mean = 3 / (1/30 + 1/40 + 1/60).\nLCM of denominators = 120.\nSum = (4 + 3 + 2) / 120 = 9 / 120.\nAverage speed = 3 / (9/120) = 360 / 9 = 40 km/h.",
        "tips": "3 * 120 / 9 = 40.",
        "options": [
            {"label": "A", "text": "38.18 km/h", "is_correct": False},
            {"label": "B", "text": "39.18 km/h", "is_correct": False},
            {"label": "C", "text": "40 km/h", "is_correct": True},
            {"label": "D", "text": "42 km/h", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Averages - Larger Number from Ratio and Average",
        "difficulty": "Hard",
        "question_text": "The average of two numbers is 36. If the ratio of the two numbers is 5:7, find the larger number.",
        "sample_answer": "Let numbers be 5x and 7x.\nSum = 5x + 7x = 12x.\nAverage = 12x / 2 = 6x = 36 => x = 6.\nLarger number = 7x = 7(6) = 42.",
        "tips": "6x = 36.",
        "options": [
            {"label": "A", "text": "40", "is_correct": False},
            {"label": "B", "text": "42", "is_correct": True},
            {"label": "C", "text": "44", "is_correct": False},
            {"label": "D", "text": "46", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Combined Average of Two Classes",
        "difficulty": "Hard",
        "question_text": "The average marks of 15 students is 72 and the average marks of another 25 students is 64. Find the average marks of all 40 students.",
        "sample_answer": "Group 1 total = 15 × 72 = 1080.\nGroup 2 total = 25 × 64 = 1600.\nTotal marks = 1080 + 1600 = 2680.\nOverall average = 2680 / 40 = 67.",
        "tips": "2680 / 40.",
        "options": [
            {"label": "A", "text": "66", "is_correct": False},
            {"label": "B", "text": "67", "is_correct": True},
            {"label": "C", "text": "67.5", "is_correct": False},
            {"label": "D", "text": "68", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Averages - Age of Third New Student after Multiple Replacement",
        "difficulty": "Hard",
        "question_text": "The average age of 30 students is 18 years. If three students aged 16, 18 and 20 leave the class and three new students join, the average age increases by 1.2 years. If two of the new students are aged 22 and 25 years, find the age of the third student.",
        "sample_answer": "Old total = 30 × 18 = 540.\nSum of leaving students = 16 + 18 + 20 = 54.\nRemaining total = 540 − 54 = 486.\nNew average = 18 + 1.2 = 19.2.\nNew total of 30 students = 30 × 19.2 = 576.\nSum of 3 new students = 576 − 486 = 90.\nThird student's age = 90 − 22 − 25 = 43 years.",
        "tips": "90 - 22 - 25 = 43.",
        "options": [
            {"label": "A", "text": "41 years", "is_correct": False},
            {"label": "B", "text": "43 years", "is_correct": True},
            {"label": "C", "text": "45 years", "is_correct": False},
            {"label": "D", "text": "47 years", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete old Averages questions to replace with exact 30 questions requested by user
    cursor.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = 'Averages'")
    print("Cleared existing Averages questions.")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'Aptitude',
            'Number & Arithmetic',
            'Averages',
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
    print(f"Successfully seeded {len(questions)} Averages questions into SQLite DB!")

if __name__ == '__main__':
    seed_db()
