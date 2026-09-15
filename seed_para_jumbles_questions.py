import json
import sqlite3
import os

DB_PATHS = [
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
    os.path.join(os.path.dirname(__file__), 'instance', 'interview_master.db'),
    os.path.join(os.path.dirname(__file__), 'interview_portal.db')
]

questions = [
    # --- BASIC LOGICAL PARAGRAPH RECONSTRUCTION (Q1 - Q5) ---
    {
        "title": "Para Jumbles",
        "difficulty": "Medium",
        "question_text": "Arrange the following sentences in a logical order to form a coherent paragraph:\n\nA. He worked hard every day.\nB. As a result, he secured the first rank.\nC. Ravi wanted to excel in his exams.\nD. He followed a strict study schedule.",
        "sample_answer": "Logical sequence: C introduces subject and goal (Ravi wanted to excel) -> D action taken (followed study schedule) -> A continuous effort (worked hard every day) -> B outcome (As a result, first rank).\nCorrect Order: CDAB.",
        "tips": "Identify the introductory sentence (C) establishing the subject and goal.",
        "options": [
            {"label": "A", "text": "CADB", "is_correct": False},
            {"label": "B", "text": "CDAB", "is_correct": True},
            {"label": "C", "text": "CBDA", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Medium",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. The company introduced a new policy.\nB. Employees welcomed the change.\nC. It aimed to improve work-life balance.\nD. Productivity increased significantly.",
        "sample_answer": "Sequence: A introduces event -> C describes policy goal -> B shows employee reaction -> D states overall productivity increase.\nCorrect Order: ACBD.",
        "tips": "'It' in C refers to the new policy introduced in A.",
        "options": [
            {"label": "A", "text": "ACBD", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "ADBC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Medium",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Trees play an important role in maintaining ecological balance.\nB. Therefore, afforestation programs are necessary.\nC. They absorb carbon dioxide from the atmosphere.\nD. Deforestation has become a major concern.",
        "sample_answer": "Sequence: A states main role -> C elaborates function -> D introduces deforestation concern -> B concludes with necessity of afforestation.\nCorrect Order: ACDB.",
        "tips": "Connect 'Trees' (A) with pronoun 'They' (C).",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": False},
            {"label": "B", "text": "ACDB", "is_correct": True},
            {"label": "C", "text": "CDAB", "is_correct": False},
            {"label": "D", "text": "BDAC", "is_correct": False}
        ],
        "correct_option": "B"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Medium",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Online learning has become popular.\nB. Students can learn from anywhere.\nC. Technology has transformed education.\nD. It offers flexibility and convenience.",
        "sample_answer": "Sequence: C provides broad theme -> A narrows to online learning -> D explains general benefits -> B specifies student flexibility.\nCorrect Order: CADB.",
        "tips": "Start with general statement C before specific application A.",
        "options": [
            {"label": "A", "text": "CADB", "is_correct": True},
            {"label": "B", "text": "ACDB", "is_correct": False},
            {"label": "C", "text": "ABCD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Medium",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. The scientist conducted several experiments.\nB. Finally, he published his findings.\nC. He analyzed the collected data carefully.\nD. The results supported his hypothesis.",
        "sample_answer": "Sequence: A experiment -> C data analysis -> D hypothesis validation -> B final publication ('Finally').\nCorrect Order: ACDB.",
        "tips": "'Finally' signals the concluding sentence B.",
        "options": [
            {"label": "A", "text": "ACDB", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "BACD", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- HARD LEVEL (Q6 - Q10) ---
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. However, this growth has also created environmental challenges.\nB. Industrialization has contributed significantly to economic development.\nC. Sustainable practices can help address these issues.\nD. Pollution levels have increased in many regions.",
        "sample_answer": "Sequence: B positive impact -> A contrast 'However' -> D specific challenge -> C solution.\nCorrect Order: BADC.",
        "tips": "'However' transition in A sets up contrast following B.",
        "options": [
            {"label": "A", "text": "BADC", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "ADBC", "is_correct": False},
            {"label": "D", "text": "CBAD", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. As a result, organizations invest heavily in cybersecurity.\nB. Cyberattacks are becoming increasingly sophisticated.\nC. Sensitive information can be compromised.\nD. Businesses rely heavily on digital infrastructure.",
        "sample_answer": "Sequence: D context -> B threat -> C risk -> A conclusion ('As a result').\nCorrect Order: DBCA.",
        "tips": "'As a result' indicates conclusion A.",
        "options": [
            {"label": "A", "text": "DBCA", "is_correct": True},
            {"label": "B", "text": "BCDA", "is_correct": False},
            {"label": "C", "text": "ABCD", "is_correct": False},
            {"label": "D", "text": "ADBC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Innovation drives business growth.\nB. Companies that embrace change often outperform competitors.\nC. Market demands continue to evolve rapidly.\nD. Therefore, adaptability is essential.",
        "sample_answer": "Sequence: A core driver -> C external market condition -> B competitive advantage -> D conclusion ('Therefore').\nCorrect Order: ACBD.",
        "tips": "'Therefore' marks concluding statement D.",
        "options": [
            {"label": "A", "text": "ACBD", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DBAC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. The project faced several challenges during development.\nB. The team worked collaboratively to solve them.\nC. Their efforts resulted in successful completion.\nD. Effective communication played a key role.",
        "sample_answer": "Sequence: A problem -> D key enabler -> B team collaboration -> C successful result.\nCorrect Order: ADBC.",
        "tips": "'them' in B refers to 'challenges' in A.",
        "options": [
            {"label": "A", "text": "ADBC", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "CDAB", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Climate change affects ecosystems worldwide.\nB. Rising temperatures impact biodiversity.\nC. Immediate action is necessary.\nD. Scientists continue to study its long-term effects.",
        "sample_answer": "Sequence: A general phenomenon -> B specific impact -> D scientific monitoring -> C call to action.\nCorrect Order: ABDC.",
        "tips": "Immediate action call C forms a strong closing.",
        "options": [
            {"label": "A", "text": "ABDC", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DCBA", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- PLACEMENT-LEVEL PARA JUMBLES (Q11 - Q15) ---
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Artificial Intelligence is transforming industries.\nB. Many organizations use AI to automate processes.\nC. This improves efficiency and reduces costs.\nD. Consequently, demand for AI professionals is growing.",
        "sample_answer": "Sequence: A introduction -> B practical usage -> C direct benefit ('This') -> D industry outcome ('Consequently').\nCorrect Order: ABCD.",
        "tips": "'Consequently' sets D as concluding sentence.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Reading regularly improves vocabulary.\nB. It also enhances critical thinking skills.\nC. Therefore, students should cultivate a reading habit.\nD. Books expose readers to diverse perspectives.",
        "sample_answer": "Sequence: A primary benefit -> B secondary benefit ('also') -> D tertiary benefit -> C conclusion ('Therefore').\nCorrect Order: ABDC.",
        "tips": "'also' in B links directly after benefit A.",
        "options": [
            {"label": "A", "text": "ABDC", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "CDAB", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. The startup initially struggled to attract customers.\nB. It focused on improving product quality.\nC. Positive reviews gradually increased its popularity.\nD. Sales grew steadily over time.",
        "sample_answer": "Sequence: A problem -> B strategy -> C early traction -> D sustained growth.\nCorrect Order: ABCD.",
        "tips": "Follow chronological progression from struggle to growth.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Renewable energy sources are gaining importance.\nB. They help reduce dependence on fossil fuels.\nC. Governments are promoting clean energy initiatives.\nD. This contributes to environmental sustainability.",
        "sample_answer": "Sequence: A trend -> B core reason -> D environmental outcome -> C policy response.\nCorrect Order: ABDC.",
        "tips": "'They' in B refers to renewable energy sources in A.",
        "options": [
            {"label": "A", "text": "ABDC", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DBAC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Communication skills are essential in the workplace.\nB. They help employees collaborate effectively.\nC. Strong communication reduces misunderstandings.\nD. As a result, organizational productivity improves.",
        "sample_answer": "Sequence: A importance -> B collaboration benefit -> C misunderstanding reduction -> D productivity outcome ('As a result').\nCorrect Order: ABCD.",
        "tips": "'As a result' marks final sentence D.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- ADVANCED HARD QUESTIONS (Q16 - Q20) ---
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Research plays a crucial role in innovation.\nB. It helps identify new opportunities and challenges.\nC. Organizations use research findings to make informed decisions.\nD. This ultimately contributes to long-term success.",
        "sample_answer": "Sequence: A main role -> B specific function -> C practical application -> D final long-term benefit ('ultimately').\nCorrect Order: ABCD.",
        "tips": "'ultimately' points to final sentence D.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Social media has changed the way people communicate.\nB. Information can be shared instantly across the globe.\nC. However, misinformation can spread just as quickly.\nD. Users must evaluate sources critically.",
        "sample_answer": "Sequence: A premise -> B positive feature -> C negative contrast 'However' -> D practical advice.\nCorrect Order: ABCD.",
        "tips": "'However' in C contrasts with positive feature B.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DCBA", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Effective leadership inspires teams.\nB. Leaders provide guidance and direction.\nC. Employees feel motivated to achieve goals.\nD. This contributes to organizational success.",
        "sample_answer": "Sequence: A premise -> B leadership action -> C employee response -> D organizational impact.\nCorrect Order: ABCD.",
        "tips": "Follow chain: Leadership -> Action -> Employee Motivation -> Organizational Success.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Data analytics helps organizations make better decisions.\nB. Large amounts of information can be processed efficiently.\nC. Insights derived from data improve performance.\nD. Businesses increasingly rely on analytical tools.",
        "sample_answer": "Sequence: A main utility -> B processing capacity -> C performance impact -> D industry adoption.\nCorrect Order: ABCD.",
        "tips": "Connect data analytics (A) with data processing (B).",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Technological advancements have improved healthcare.\nB. Medical professionals can diagnose diseases more accurately.\nC. Patients benefit from better treatment options.\nD. Overall healthcare outcomes have improved significantly.",
        "sample_answer": "Sequence: A general claim -> B doctor perspective -> C patient perspective -> D overall summary.\nCorrect Order: ABCD.",
        "tips": "D summarizes doctor (B) and patient (C) improvements.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- CAT / BANKING VERY HARD PARA JUMBLES (Q21 - Q25) ---
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Yet many organizations fail to utilize it effectively.\nB. Data has become one of the most valuable resources.\nC. As a result, opportunities for growth are often missed.\nD. Proper analysis can reveal meaningful insights.",
        "sample_answer": "Sequence: B assertion -> D potential benefit -> A contrast 'Yet' -> C negative outcome 'As a result'.\nCorrect Order: BDAC.",
        "tips": "'Yet' A introduces contrast after potential D.",
        "options": [
            {"label": "A", "text": "BDAC", "is_correct": True},
            {"label": "B", "text": "BADC", "is_correct": False},
            {"label": "C", "text": "ABCD", "is_correct": False},
            {"label": "D", "text": "CABD", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. The internet has revolutionized access to information.\nB. Users can obtain knowledge instantly.\nC. Nevertheless, information overload has become a concern.\nD. Critical evaluation skills are increasingly important.",
        "sample_answer": "Sequence: A revolution -> B instant knowledge -> C contrast 'Nevertheless' -> D imperative skill.\nCorrect Order: ABCD.",
        "tips": "'Nevertheless' C signals contrast following B.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Urbanization continues to increase globally.\nB. This creates pressure on infrastructure and resources.\nC. City planners must develop sustainable solutions.\nD. Effective planning can improve quality of life.",
        "sample_answer": "Sequence: A trend -> B problem ('This') -> C planner responsibility -> D positive result.\nCorrect Order: ABCD.",
        "tips": "'This' in B refers directly to urbanization growth A.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Employee engagement is crucial for organizational success.\nB. Motivated employees tend to be more productive.\nC. Organizations implement various strategies to improve engagement.\nD. This often leads to better business outcomes.",
        "sample_answer": "Sequence: A premise -> B worker rationale -> C strategy implementation -> D final business result.\nCorrect Order: ABCD.",
        "tips": "Connect engagement importance A with productivity B.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. E-commerce has transformed retail industries.\nB. Consumers can shop conveniently from anywhere.\nC. Businesses must adapt to changing customer expectations.\nD. Companies that innovate often gain a competitive advantage.",
        "sample_answer": "Sequence: A macro shift -> B consumer perspective -> C business imperative -> D innovation benefit.\nCorrect Order: ABCD.",
        "tips": "Follow industry transformation A to business adaptation C.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },

    # --- CHALLENGING MIXED PARA JUMBLES (Q26 - Q30) ---
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. He started learning programming in college.\nB. Eventually, he became a software engineer.\nC. His dedication helped him master several technologies.\nD. He spent countless hours practicing coding.",
        "sample_answer": "Sequence: A start of journey -> D effort (practicing) -> C mastery (dedication) -> B ultimate outcome ('Eventually').\nCorrect Order: ADCB.",
        "tips": "'Eventually' in B signals conclusion.",
        "options": [
            {"label": "A", "text": "ADCB", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "ACDB", "is_correct": False},
            {"label": "D", "text": "BADC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. The economy experienced rapid growth.\nB. Investments increased significantly.\nC. This created new employment opportunities.\nD. Consumer spending also rose.",
        "sample_answer": "Sequence: A catalyst -> B investment boost -> C job creation -> D consumer spending boost ('also').\nCorrect Order: ABCD.",
        "tips": "'also' in D links after employment opportunities C.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Water conservation is becoming increasingly important.\nB. Many regions face water shortages.\nC. Individuals can adopt responsible usage habits.\nD. Collective efforts can make a significant difference.",
        "sample_answer": "Sequence: A premise -> B reason (shortages) -> C individual habits -> D collective impact.\nCorrect Order: ABCD.",
        "tips": "Transition from individual habits C to collective efforts D.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. The athlete trained rigorously for the competition.\nB. He followed a strict fitness routine.\nC. His efforts improved his performance.\nD. He eventually won the championship.",
        "sample_answer": "Sequence: A initial training -> B specific routine -> C performance improvement -> D final victory ('eventually').\nCorrect Order: ABCD.",
        "tips": "Chronological progression to winning championship D.",
        "options": [
            {"label": "A", "text": "ABCD", "is_correct": True},
            {"label": "B", "text": "ACBD", "is_correct": False},
            {"label": "C", "text": "BACD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    },
    {
        "title": "Para Jumbles",
        "difficulty": "Hard",
        "question_text": "Arrange the following sentences in a logical order:\n\nA. Space exploration continues to advance rapidly.\nB. Scientists are discovering new possibilities.\nC. Technological innovations support these missions.\nD. Future discoveries may transform our understanding of the universe.",
        "sample_answer": "Sequence: A general advancement -> C technological support -> B scientific discoveries -> D future impact.\nCorrect Order: ACBD.",
        "tips": "Future discoveries D concludes paragraph.",
        "options": [
            {"label": "A", "text": "ACBD", "is_correct": True},
            {"label": "B", "text": "ABCD", "is_correct": False},
            {"label": "C", "text": "CABD", "is_correct": False},
            {"label": "D", "text": "DABC", "is_correct": False}
        ],
        "correct_option": "A"
    }
]

def seed_para_jumbles():
    for db_path in DB_PATHS:
        if not os.path.exists(db_path):
            continue
        print(f"Seeding database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM questions WHERE topic = 'Para Jumbles'")
            print(f"Deleted old 'Para Jumbles' questions.")

            inserted_count = 0
            for q in questions:
                cursor.execute("""
                    INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option, star_guide)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    'Aptitude',
                    'Verbal Ability',
                    'Para Jumbles',
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
    seed_para_jumbles()
