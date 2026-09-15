import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

p1_text = "Passage 1: Artificial Intelligence\n\nArtificial Intelligence (AI) is transforming industries across the world. From healthcare to finance, AI-powered systems help organizations automate repetitive tasks, improve decision-making, and increase efficiency. However, the rapid adoption of AI has also raised concerns about job displacement and ethical issues. Experts believe that while some traditional jobs may disappear, new opportunities requiring advanced technical and analytical skills will emerge. Therefore, continuous learning and skill development are essential for professionals to remain competitive in the evolving job market."

p2_text = "Passage 2: Time Management\n\nTime management is one of the most valuable skills for students and professionals. Effective time management helps individuals prioritize tasks, reduce stress, and achieve goals more efficiently. People who plan their daily activities often complete more work in less time compared to those who work without a schedule. Developing habits such as setting deadlines, avoiding distractions, and maintaining a to-do list can significantly improve productivity."

p3_text = "Passage 3: Online Learning\n\nOnline learning has gained popularity due to its flexibility and accessibility. Students can access educational resources from anywhere and learn at their own pace. However, online learning requires self-discipline and effective time management. Without proper motivation, learners may struggle to complete courses successfully. Institutions are increasingly using technology to create interactive learning experiences that engage students and improve outcomes."

p4_text = "Passage 4: Environmental Conservation\n\nEnvironmental conservation involves protecting natural resources such as forests, water, and wildlife. Human activities, including deforestation and pollution, have significantly impacted ecosystems. Governments and organizations worldwide are promoting sustainable practices to reduce environmental damage. Individuals can also contribute by reducing waste, conserving energy, and supporting eco-friendly initiatives."

p5_text = "Passage 5: Remote Work\n\nRemote work has become increasingly common in recent years. It offers employees flexibility and reduces commuting time. Many organizations have adopted remote work policies to improve employee satisfaction and productivity. However, remote work can also create challenges such as communication gaps and feelings of isolation. Successful remote workers often develop strong communication skills and maintain a structured routine."

p6_text = "Passage 6: Technology and Society\n\nTechnology has revolutionized communication, transportation, and healthcare. While technological advancements have improved quality of life, they have also introduced challenges such as privacy concerns and cybersecurity threats. As society becomes increasingly dependent on technology, balancing innovation with ethical responsibility becomes more important."

questions = [
    # --- PASSAGE 1: ARTIFICIAL INTELLIGENCE (Q1 - Q5) ---
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": p1_text + "\n\nQuestion: What is the primary benefit of AI mentioned in the passage?",
        "sample_answer": "According to Passage 1, AI-powered systems help organizations automate repetitive tasks, improve decision-making, and increase efficiency.",
        "tips": "Look for benefits of AI listed in the passage.",
        "options": [
            {"label": "A", "text": "Reducing internet usage", "is_correct": False},
            {"label": "B", "text": "Automating repetitive tasks", "is_correct": True},
            {"label": "C", "text": "Increasing manual work", "is_correct": False},
            {"label": "D", "text": "Eliminating technology", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "Which industry is NOT mentioned in the passage?",
        "sample_answer": "Passage 1 explicitly mentions 'healthcare' and 'finance'. 'Agriculture' is not mentioned.",
        "tips": "Refer to Passage 1 industries.",
        "options": [
            {"label": "A", "text": "Healthcare", "is_correct": False},
            {"label": "B", "text": "Finance", "is_correct": False},
            {"label": "C", "text": "Agriculture", "is_correct": True},
            {"label": "D", "text": "None of the above", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "What concern is associated with AI adoption?",
        "sample_answer": "Passage 1 states that rapid adoption has raised concerns about job displacement and ethical issues.",
        "tips": "Refer to concerns in Passage 1.",
        "options": [
            {"label": "A", "text": "Higher salaries", "is_correct": False},
            {"label": "B", "text": "Job displacement", "is_correct": True},
            {"label": "C", "text": "Reduced efficiency", "is_correct": False},
            {"label": "D", "text": "Increased paperwork", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "According to experts, AI will:",
        "sample_answer": "Experts believe new opportunities requiring advanced technical and analytical skills will emerge.",
        "tips": "Refer to expert predictions in Passage 1.",
        "options": [
            {"label": "A", "text": "Remove all jobs", "is_correct": False},
            {"label": "B", "text": "Create new opportunities", "is_correct": True},
            {"label": "C", "text": "Stop technological growth", "is_correct": False},
            {"label": "D", "text": "Reduce innovation", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "What is essential for professionals according to the passage?",
        "sample_answer": "Passage 1 highlights continuous learning and skill development as essential.",
        "tips": "Refer to the conclusion of Passage 1.",
        "options": [
            {"label": "A", "text": "Continuous learning", "is_correct": True},
            {"label": "B", "text": "Avoiding technology", "is_correct": False},
            {"label": "C", "text": "Working fewer hours", "is_correct": False},
            {"label": "D", "text": "Changing careers frequently", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- PASSAGE 2: TIME MANAGEMENT (Q6 - Q10) ---
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": p2_text + "\n\nQuestion: What is the main topic of the passage?",
        "sample_answer": "Passage 2 focuses on time management and its benefits.",
        "tips": "Identify the central theme of Passage 2.",
        "options": [
            {"label": "A", "text": "Communication Skills", "is_correct": False},
            {"label": "B", "text": "Time Management", "is_correct": True},
            {"label": "C", "text": "Leadership", "is_correct": False},
            {"label": "D", "text": "Marketing", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "Effective time management helps reduce:",
        "sample_answer": "Passage 2 states that time management helps prioritize tasks, reduce stress, and achieve goals.",
        "tips": "Refer to Passage 2 benefits.",
        "options": [
            {"label": "A", "text": "Knowledge", "is_correct": False},
            {"label": "B", "text": "Income", "is_correct": False},
            {"label": "C", "text": "Stress", "is_correct": True},
            {"label": "D", "text": "Motivation", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "People with a schedule generally:",
        "sample_answer": "Passage 2 notes that people who plan daily activities complete more work in less time.",
        "tips": "Refer to Passage 2 scheduling facts.",
        "options": [
            {"label": "A", "text": "Complete less work", "is_correct": False},
            {"label": "B", "text": "Complete more work", "is_correct": True},
            {"label": "C", "text": "Avoid responsibilities", "is_correct": False},
            {"label": "D", "text": "Work slower", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "Which habit improves productivity?",
        "sample_answer": "Passage 2 mentions maintaining a to-do list, setting deadlines, and avoiding distractions.",
        "tips": "Refer to productive habits in Passage 2.",
        "options": [
            {"label": "A", "text": "Ignoring deadlines", "is_correct": False},
            {"label": "B", "text": "Maintaining a to-do list", "is_correct": True},
            {"label": "C", "text": "Avoiding planning", "is_correct": False},
            {"label": "D", "text": "Delaying tasks", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "The passage suggests that planning:",
        "sample_answer": "Planning daily activities helps complete tasks faster, thereby improving overall efficiency.",
        "tips": "Refer to planning efficiency in Passage 2.",
        "options": [
            {"label": "A", "text": "Wastes time", "is_correct": False},
            {"label": "B", "text": "Improves efficiency", "is_correct": True},
            {"label": "C", "text": "Is unnecessary", "is_correct": False},
            {"label": "D", "text": "Increases distractions", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- PASSAGE 3: ONLINE LEARNING (Q11 - Q15) ---
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": p3_text + "\n\nQuestion: Why has online learning become popular?",
        "sample_answer": "Passage 3 states online learning gained popularity due to its flexibility and accessibility.",
        "tips": "Refer to sentence 1 of Passage 3.",
        "options": [
            {"label": "A", "text": "High costs", "is_correct": False},
            {"label": "B", "text": "Flexibility and accessibility", "is_correct": True},
            {"label": "C", "text": "Strict schedules", "is_correct": False},
            {"label": "D", "text": "Physical attendance", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "What challenge do online learners often face?",
        "sample_answer": "Without proper motivation and self-discipline, learners struggle to complete courses successfully.",
        "tips": "Refer to challenges in Passage 3.",
        "options": [
            {"label": "A", "text": "Lack of textbooks", "is_correct": False},
            {"label": "B", "text": "Struggling to complete courses without self-discipline and motivation", "is_correct": True},
            {"label": "C", "text": "Too much classroom noise", "is_correct": False},
            {"label": "D", "text": "Limited internet access", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "What skills are necessary for successful online learning?",
        "sample_answer": "Passage 3 states online learning requires self-discipline and effective time management.",
        "tips": "Refer to required skills in Passage 3.",
        "options": [
            {"label": "A", "text": "Graphic design", "is_correct": False},
            {"label": "B", "text": "Self-discipline and effective time management", "is_correct": True},
            {"label": "C", "text": "Public speaking", "is_correct": False},
            {"label": "D", "text": "Speed reading", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "How are institutions improving online learning?",
        "sample_answer": "Institutions use technology to create interactive learning experiences that engage students.",
        "tips": "Refer to institutional action in Passage 3.",
        "options": [
            {"label": "A", "text": "By raising fees", "is_correct": False},
            {"label": "B", "text": "By using technology to create interactive learning experiences", "is_correct": True},
            {"label": "C", "text": "By shortening semesters", "is_correct": False},
            {"label": "D", "text": "By eliminating teachers", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Medium",
        "question_text": "What is the main idea of the passage?",
        "sample_answer": "Online learning offers great flexibility and accessibility but requires self-discipline, time management, and motivation for success.",
        "tips": "Summarize Passage 3.",
        "options": [
            {"label": "A", "text": "Online learning is unnecessary", "is_correct": False},
            {"label": "B", "text": "Online learning offers flexibility but requires self-discipline and motivation", "is_correct": True},
            {"label": "C", "text": "Online degrees are not recognized", "is_correct": False},
            {"label": "D", "text": "Traditional schools are closing", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- PASSAGE 4: ENVIRONMENTAL CONSERVATION (Q16 - Q20) ---
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": p4_text + "\n\nQuestion: What is environmental conservation?",
        "sample_answer": "Environmental conservation involves protecting natural resources such as forests, water, and wildlife.",
        "tips": "Refer to sentence 1 of Passage 4.",
        "options": [
            {"label": "A", "text": "Building industrial factories", "is_correct": False},
            {"label": "B", "text": "Protecting natural resources such as forests, water, and wildlife", "is_correct": True},
            {"label": "C", "text": "Increasing urban pollution", "is_correct": False},
            {"label": "D", "text": "Harvesting natural resources without limits", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "Name two human activities that harm ecosystems.",
        "sample_answer": "Deforestation and pollution are mentioned as harmful human activities in Passage 4.",
        "tips": "Refer to sentence 2 of Passage 4.",
        "options": [
            {"label": "A", "text": "Recycling and composting", "is_correct": False},
            {"label": "B", "text": "Deforestation and pollution", "is_correct": True},
            {"label": "C", "text": "Solar power and wind energy", "is_correct": False},
            {"label": "D", "text": "Tree planting and water harvesting", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What are governments promoting?",
        "sample_answer": "Governments and organizations promote sustainable practices to reduce environmental damage.",
        "tips": "Refer to sentence 3 of Passage 4.",
        "options": [
            {"label": "A", "text": "Higher fossil fuel usage", "is_correct": False},
            {"label": "B", "text": "Sustainable practices to reduce environmental damage", "is_correct": True},
            {"label": "C", "text": "Deforestation for farming", "is_correct": False},
            {"label": "D", "text": "Increased industrial waste", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "How can individuals contribute to conservation?",
        "sample_answer": "Individuals can contribute by reducing waste, conserving energy, and supporting eco-friendly initiatives.",
        "tips": "Refer to sentence 4 of Passage 4.",
        "options": [
            {"label": "A", "text": "By increasing energy consumption", "is_correct": False},
            {"label": "B", "text": "By reducing waste, conserving energy, and supporting eco-friendly initiatives", "is_correct": True},
            {"label": "C", "text": "By ignoring environmental laws", "is_correct": False},
            {"label": "D", "text": "By using plastic bags", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What is the central theme of the passage?",
        "sample_answer": "The central theme is protecting ecosystems through conservation and sustainable actions at all levels.",
        "tips": "Summarize Passage 4.",
        "options": [
            {"label": "A", "text": "Space exploration", "is_correct": False},
            {"label": "B", "text": "Protecting ecosystems through conservation and sustainable actions", "is_correct": True},
            {"label": "C", "text": "Economic growth of industries", "is_correct": False},
            {"label": "D", "text": "History of agriculture", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- PASSAGE 5: REMOTE WORK (Q21 - Q25) ---
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": p5_text + "\n\nQuestion: What is one benefit of remote work?",
        "sample_answer": "Passage 5 states remote work offers employees flexibility and reduces commuting time.",
        "tips": "Refer to sentence 2 of Passage 5.",
        "options": [
            {"label": "A", "text": "Mandatory travel", "is_correct": False},
            {"label": "B", "text": "Flexibility and reduced commuting time", "is_correct": True},
            {"label": "C", "text": "Lower productivity", "is_correct": False},
            {"label": "D", "text": "Strict office hours", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "Why have organizations adopted remote work policies?",
        "sample_answer": "Organizations adopted remote work policies to improve employee satisfaction and productivity.",
        "tips": "Refer to sentence 3 of Passage 5.",
        "options": [
            {"label": "A", "text": "To close down offices permanently", "is_correct": False},
            {"label": "B", "text": "To improve employee satisfaction and productivity", "is_correct": True},
            {"label": "C", "text": "To reduce salaries", "is_correct": False},
            {"label": "D", "text": "To increase travel budgets", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What challenges are associated with remote work?",
        "sample_answer": "Remote work creates challenges such as communication gaps and feelings of isolation.",
        "tips": "Refer to sentence 4 of Passage 5.",
        "options": [
            {"label": "A", "text": "High travel expenses", "is_correct": False},
            {"label": "B", "text": "Communication gaps and feelings of isolation", "is_correct": True},
            {"label": "C", "text": "Too many office meetings", "is_correct": False},
            {"label": "D", "text": "Overcrowded desks", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What qualities help remote workers succeed?",
        "sample_answer": "Successful remote workers develop strong communication skills and maintain a structured routine.",
        "tips": "Refer to sentence 5 of Passage 5.",
        "options": [
            {"label": "A", "text": "Avoiding communication", "is_correct": False},
            {"label": "B", "text": "Strong communication skills and a structured routine", "is_correct": True},
            {"label": "C", "text": "Working without breaks", "is_correct": False},
            {"label": "D", "text": "Changing work hours daily", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What is the main idea of the passage?",
        "sample_answer": "Remote work offers key advantages like flexibility and higher productivity, but success requires overcoming communication gaps and isolation.",
        "tips": "Summarize Passage 5.",
        "options": [
            {"label": "A", "text": "Remote work should be banned", "is_correct": False},
            {"label": "B", "text": "Remote work provides benefits like flexibility but requires overcoming communication and isolation challenges", "is_correct": True},
            {"label": "C", "text": "Remote work eliminates the need for teams", "is_correct": False},
            {"label": "D", "text": "All companies must become remote", "is_correct": False}
        ],
        "correct_option": "B"
    },

    # --- PASSAGE 6: TECHNOLOGY AND SOCIETY (Q26 - Q30) ---
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": p6_text + "\n\nQuestion: Which of the following best describes the author's tone?",
        "sample_answer": "The tone is balanced because the author highlights both positive advancements and negative challenges.",
        "tips": "Recognize that both pros and cons are discussed objectively in Passage 6.",
        "options": [
            {"label": "A", "text": "Optimistic", "is_correct": False},
            {"label": "B", "text": "Critical", "is_correct": False},
            {"label": "C", "text": "Balanced", "is_correct": True},
            {"label": "D", "text": "Emotional", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What challenge is NOT mentioned in the passage?",
        "sample_answer": "Privacy concerns and cybersecurity threats are explicitly mentioned. Climate change is not mentioned.",
        "tips": "Check sentence 2 of Passage 6.",
        "options": [
            {"label": "A", "text": "Privacy concerns", "is_correct": False},
            {"label": "B", "text": "Cybersecurity threats", "is_correct": False},
            {"label": "C", "text": "Climate change", "is_correct": True},
            {"label": "D", "text": "None of the above", "is_correct": False}
        ],
        "correct_option": "C"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "Why is ethical responsibility important?",
        "sample_answer": "Passage 6 notes that balancing innovation with ethical responsibility is increasingly important.",
        "tips": "Refer to the final sentence of Passage 6.",
        "options": [
            {"label": "A", "text": "To balance innovation", "is_correct": True},
            {"label": "B", "text": "To reduce communication", "is_correct": False},
            {"label": "C", "text": "To slow development", "is_correct": False},
            {"label": "D", "text": "To avoid technology", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What has technology improved?",
        "sample_answer": "Technology has revolutionized communication, transportation, and healthcare.",
        "tips": "Refer to sentence 1 of Passage 6.",
        "options": [
            {"label": "A", "text": "Healthcare", "is_correct": False},
            {"label": "B", "text": "Transportation", "is_correct": False},
            {"label": "C", "text": "Communication", "is_correct": False},
            {"label": "D", "text": "All of the above", "is_correct": True}
        ],
        "correct_option": "D"
    },
    {
        "title": "Reading Comprehension",
        "difficulty": "Hard",
        "question_text": "What is the main purpose of the passage?",
        "sample_answer": "The main purpose is to discuss both the benefits and challenges of technology in modern society.",
        "tips": "Identify the main purpose of Passage 6.",
        "options": [
            {"label": "A", "text": "To criticize technology", "is_correct": False},
            {"label": "B", "text": "To discuss benefits and challenges of technology", "is_correct": True},
            {"label": "C", "text": "To discourage innovation", "is_correct": False},
            {"label": "D", "text": "To promote a specific product", "is_correct": False}
        ],
        "correct_option": "B"
    }
]

def seed_reading_comprehension():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Reading Comprehension'")
            print(f"Deleted old 'Reading Comprehension' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Verbal Ability',
                    'Reading Comprehension',
                    q['title'],
                    q['difficulty'],
                    q['question_text'],
                    q['sample_answer'],
                    q['tips'],
                    json.dumps(q['options']),
                    q['correct_option'],
                    json.dumps({
                        'options': q['options'],
                        'correct_option': q['correct_option']
                    })
                ))
                inserted_count += 1

            conn.commit()
            conn.close()
            print(f"Successfully inserted {inserted_count} questions into {db_path}.")
        except Exception as e:
            print(f"Skipping {db_path}: {e}")

if __name__ == '__main__':
    seed_reading_comprehension()
