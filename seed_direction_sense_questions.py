"""
Seed script for Direction Sense (Logical Reasoning)
Contains exactly 50 easy-to-medium questions with detailed solutions and tips.
"""
import os
import json
import sqlite3

questions = [
    {
        "title": "Direction Sense - Final Facing Direction 1",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards North. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from North points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "North",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "West",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 2",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "North",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 3",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "North",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Final Facing Direction 4",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards East. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from East points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "West",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Final Facing Direction 5",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards North. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from North points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "East",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "North",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Final Facing Direction 6",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards South. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from South points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "West",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 7",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards South. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from South points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "West",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 8",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "North",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Final Facing Direction 9",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "North",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "South",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 10",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards East. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from East points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "West",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 11",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "North",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 12",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "North",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 13",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards South. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from South points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "West",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 14",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards East. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from East points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 15",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "North",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "South",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 16",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards North. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from North points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "North",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Final Facing Direction 17",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards North. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from North points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "North",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Final Facing Direction 18",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards South. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from South points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Final Facing Direction 19",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards East. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from East points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "South",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 20",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards South. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from South points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "West",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "South",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 21",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards East. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from East points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "South",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "West",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 22",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards East. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from East points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Final Facing Direction 23",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards West. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from West points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "North",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "East",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Final Facing Direction 24",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards South. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from South points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "West",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "None of these (2)",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Final Facing Direction 25",
        "difficulty": "Easy",
        "question_text": "A person starts walking towards North. He turns 90\u00b0 right, walks 10 meters, then turns 90\u00b0 right again, and finally turns 90\u00b0 left. In which direction is he facing now?",
        "sample_answer": "Net turns: Right (90\u00b0) + Right (90\u00b0) + Left (-90\u00b0) = 90\u00b0 Right.\nTurning 90\u00b0 clockwise from North points towards the final direction.",
        "tips": "Net angle = Sum of right turns (90\u00b0) - Sum of left turns (90\u00b0).",
        "options": [
            {
                "label": "A",
                "text": "South",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "East",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "West",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "North",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 26",
        "difficulty": "Medium",
        "question_text": "Ravi walks 3 km North, then turns right and walks 4 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(3\u00b2 + 4\u00b2) = \u221a(9 + 16) = \u221a25 = 5 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "3 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 27",
        "difficulty": "Medium",
        "question_text": "Ravi walks 6 km North, then turns right and walks 8 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(6\u00b2 + 8\u00b2) = \u221a(36 + 64) = \u221a100 = 10 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "8 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "10 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "14 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "12 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 28",
        "difficulty": "Medium",
        "question_text": "Ravi walks 5 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(5\u00b2 + 12\u00b2) = \u221a(25 + 144) = \u221a169 = 13 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "11 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "13 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "17 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Shortest Distance 29",
        "difficulty": "Medium",
        "question_text": "Ravi walks 9 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(9\u00b2 + 12\u00b2) = \u221a(81 + 144) = \u221a225 = 15 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "15 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "13 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "21 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Shortest Distance 30",
        "difficulty": "Medium",
        "question_text": "Ravi walks 8 km North, then turns right and walks 15 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(8\u00b2 + 15\u00b2) = \u221a(64 + 225) = \u221a289 = 17 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "17 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "23 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Shortest Distance 31",
        "difficulty": "Medium",
        "question_text": "Ravi walks 3 km North, then turns right and walks 4 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(3\u00b2 + 4\u00b2) = \u221a(9 + 16) = \u221a25 = 5 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "3 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 32",
        "difficulty": "Medium",
        "question_text": "Ravi walks 6 km North, then turns right and walks 8 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(6\u00b2 + 8\u00b2) = \u221a(36 + 64) = \u221a100 = 10 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "12 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "14 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "8 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Shortest Distance 33",
        "difficulty": "Medium",
        "question_text": "Ravi walks 5 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(5\u00b2 + 12\u00b2) = \u221a(25 + 144) = \u221a169 = 13 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "11 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Shortest Distance 34",
        "difficulty": "Medium",
        "question_text": "Ravi walks 9 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(9\u00b2 + 12\u00b2) = \u221a(81 + 144) = \u221a225 = 15 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "21 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "13 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Shortest Distance 35",
        "difficulty": "Medium",
        "question_text": "Ravi walks 8 km North, then turns right and walks 15 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(8\u00b2 + 15\u00b2) = \u221a(64 + 225) = \u221a289 = 17 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "19 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "23 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "17 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Shortest Distance 36",
        "difficulty": "Medium",
        "question_text": "Ravi walks 3 km North, then turns right and walks 4 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(3\u00b2 + 4\u00b2) = \u221a(9 + 16) = \u221a25 = 5 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "3 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "5 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "7 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 37",
        "difficulty": "Medium",
        "question_text": "Ravi walks 6 km North, then turns right and walks 8 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(6\u00b2 + 8\u00b2) = \u221a(36 + 64) = \u221a100 = 10 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "12 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "14 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "10 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Shortest Distance 38",
        "difficulty": "Medium",
        "question_text": "Ravi walks 5 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(5\u00b2 + 12\u00b2) = \u221a(25 + 144) = \u221a169 = 13 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "13 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "11 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 39",
        "difficulty": "Medium",
        "question_text": "Ravi walks 9 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(9\u00b2 + 12\u00b2) = \u221a(81 + 144) = \u221a225 = 15 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "13 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "21 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Shortest Distance 40",
        "difficulty": "Medium",
        "question_text": "Ravi walks 8 km North, then turns right and walks 15 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(8\u00b2 + 15\u00b2) = \u221a(64 + 225) = \u221a289 = 17 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "23 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "19 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 41",
        "difficulty": "Medium",
        "question_text": "Ravi walks 3 km North, then turns right and walks 4 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(3\u00b2 + 4\u00b2) = \u221a(9 + 16) = \u221a25 = 5 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "7 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "3 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "5 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Shortest Distance 42",
        "difficulty": "Medium",
        "question_text": "Ravi walks 6 km North, then turns right and walks 8 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(6\u00b2 + 8\u00b2) = \u221a(36 + 64) = \u221a100 = 10 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "10 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "14 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "12 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "8 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Shortest Distance 43",
        "difficulty": "Medium",
        "question_text": "Ravi walks 5 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(5\u00b2 + 12\u00b2) = \u221a(25 + 144) = \u221a169 = 13 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "11 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Shortest Distance 44",
        "difficulty": "Medium",
        "question_text": "Ravi walks 9 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(9\u00b2 + 12\u00b2) = \u221a(81 + 144) = \u221a225 = 15 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "13 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "21 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Shortest Distance 45",
        "difficulty": "Medium",
        "question_text": "Ravi walks 8 km North, then turns right and walks 15 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(8\u00b2 + 15\u00b2) = \u221a(64 + 225) = \u221a289 = 17 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "17 km",
                "is_correct": true
            },
            {
                "label": "B",
                "text": "23 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "19 km",
                "is_correct": false
            }
        ],
        "correct_option": "A"
    },
    {
        "title": "Direction Sense - Shortest Distance 46",
        "difficulty": "Medium",
        "question_text": "Ravi walks 3 km North, then turns right and walks 4 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(3\u00b2 + 4\u00b2) = \u221a(9 + 16) = \u221a25 = 5 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "3 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "None of these (2)",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "5 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "7 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Shortest Distance 47",
        "difficulty": "Medium",
        "question_text": "Ravi walks 6 km North, then turns right and walks 8 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(6\u00b2 + 8\u00b2) = \u221a(36 + 64) = \u221a100 = 10 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "12 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "8 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "10 km",
                "is_correct": true
            },
            {
                "label": "D",
                "text": "14 km",
                "is_correct": false
            }
        ],
        "correct_option": "C"
    },
    {
        "title": "Direction Sense - Shortest Distance 48",
        "difficulty": "Medium",
        "question_text": "Ravi walks 5 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(5\u00b2 + 12\u00b2) = \u221a(25 + 144) = \u221a169 = 13 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "11 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "C",
                "text": "15 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "13 km",
                "is_correct": true
            }
        ],
        "correct_option": "D"
    },
    {
        "title": "Direction Sense - Shortest Distance 49",
        "difficulty": "Medium",
        "question_text": "Ravi walks 9 km North, then turns right and walks 12 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(9\u00b2 + 12\u00b2) = \u221a(81 + 144) = \u221a225 = 15 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "17 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "15 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "13 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "21 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    },
    {
        "title": "Direction Sense - Shortest Distance 50",
        "difficulty": "Medium",
        "question_text": "Ravi walks 8 km North, then turns right and walks 15 km East. What is the shortest straight-line distance from his starting point?",
        "sample_answer": "Using the Pythagorean Theorem:\nDistance = \u221a(North\u00b2 + East\u00b2) = \u221a(8\u00b2 + 15\u00b2) = \u221a(64 + 225) = \u221a289 = 17 km.",
        "tips": "Use Pythagoras theorem: Shortest Distance = sqrt(x^2 + y^2).",
        "options": [
            {
                "label": "A",
                "text": "23 km",
                "is_correct": false
            },
            {
                "label": "B",
                "text": "17 km",
                "is_correct": true
            },
            {
                "label": "C",
                "text": "19 km",
                "is_correct": false
            },
            {
                "label": "D",
                "text": "15 km",
                "is_correct": false
            }
        ],
        "correct_option": "B"
    }
]

def seed_database():
    # 1. Update SQLAlchemy database if available
    try:
        from app import app, db
        from models import Question, UserProgress, Bookmark
        with app.app_context():
            old_qs = Question.query.filter_by(category='Aptitude', topic='Direction Sense').all()
            old_ids = [q.id for q in old_qs]
            if old_ids:
                UserProgress.query.filter(UserProgress.question_id.in_(old_ids)).delete(synchronize_session=False)
                Bookmark.query.filter(Bookmark.question_id.in_(old_ids)).delete(synchronize_session=False)
                db.session.commit()
            Question.query.filter_by(category='Aptitude', topic='Direction Sense').delete(synchronize_session=False)
            for q in questions:
                opts_json = json.dumps(q.get('options', []))
                new_q = Question(
                    category='Aptitude',
                    sub_category='Logical Reasoning',
                    topic='Direction Sense',
                    title=q.get('title', 'Direction Sense'),
                    difficulty=q.get('difficulty', 'Easy'),
                    question_text=q.get('question_text', ''),
                    sample_answer=q.get('sample_answer', ''),
                    tips=q.get('tips', ''),
                    options=opts_json,
                    correct_option=q.get('correct_option', 'A')
                )
                db.session.add(new_q)
            db.session.commit()
            print(f"Successfully seeded {len(questions)} questions for Direction Sense via SQLAlchemy.")
    except Exception as e:
        print(f"SQLAlchemy seeding error for Direction Sense: {e}")

    # 2. Update local SQLite database if present
    db_paths = [
        os.path.join(os.path.dirname(__file__), 'instance', 'interview_portal.db'),
        os.path.join(os.path.dirname(__file__), 'interview_portal.db')
    ]
    for p in db_paths:
        if os.path.exists(p):
            try:
                conn = sqlite3.connect(p)
                cur = conn.cursor()
                cur.execute("DELETE FROM questions WHERE category = 'Aptitude' AND topic = ?", ('Direction Sense',))
                for q in questions:
                    opts_json = json.dumps(q.get('options', []))
                    cur.execute("""
                        INSERT INTO questions (category, sub_category, topic, title, difficulty, question_text, sample_answer, tips, options, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        'Aptitude', 'Logical Reasoning', 'Direction Sense',
                        q.get('title', 'Direction Sense'), q.get('difficulty', 'Easy'),
                        q.get('question_text', ''), q.get('sample_answer', ''),
                        q.get('tips', ''), opts_json, q.get('correct_option', 'A')
                    ))
                conn.commit()
                conn.close()
                print(f"Successfully seeded {len(questions)} questions for Direction Sense into SQLite: {p}")
            except Exception as e:
                print(f"SQLite seeding error for {p}: {e}")

if __name__ == '__main__':
    seed_database()
