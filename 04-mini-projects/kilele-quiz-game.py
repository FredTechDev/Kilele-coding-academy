"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 8
Project: The Kilele Python Master Quiz Challenge
File: kilele-quiz-game.py
Concepts Applied: Functions, collections (dicts & lists), loops, scoring, timing
=============================================================================
"""

import sys

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip().upper()
    except (EOFError, KeyboardInterrupt):
        return demo_val

QUIZ_QUESTIONS = [
    {
        "question": "What is the primary design philosophy of Python?",
        "options": {
            "A": "Writing as few characters as possible",
            "B": "Code readability and clean syntax",
            "C": "Requiring semicolons at the end of every line",
            "D": "Running only on supercomputers"
        },
        "answer": "B",
        "explanation": "Python prioritizes human readability ('Readability counts')."
    },
    {
        "question": "What does the input() function ALWAYS return?",
        "options": {
            "A": "An integer (int)",
            "B": "A boolean (bool)",
            "C": "A string (str)",
            "D": "A float (float)"
        },
        "answer": "C",
        "explanation": "No matter what the user types, input() always captures it as a string."
    },
    {
        "question": "Which operator returns the remainder of a division?",
        "options": {
            "A": "// (Floor division)",
            "B": "** (Exponent)",
            "C": "% (Modulus)",
            "D": "/ (Standard division)"
        },
        "answer": "C",
        "explanation": "The modulus operator (%) returns the remainder (e.g. 10 % 3 = 1)."
    },
    {
        "question": "What will range(1, 5) produce when iterated over?",
        "options": {
            "A": "1, 2, 3, 4, 5",
            "B": "1, 2, 3, 4",
            "C": "0, 1, 2, 3, 4",
            "D": "2, 3, 4, 5"
        },
        "answer": "B",
        "explanation": "The stop parameter in range(start, stop) is exclusive (stops before 5)."
    },
    {
        "question": "What keyword is used to send a value back from a function?",
        "options": {
            "A": "send",
            "B": "output",
            "C": "print",
            "D": "return"
        },
        "answer": "D",
        "explanation": "return sends data back to the calling code for further use."
    }
]

def run_quiz():
    print("=" * 65)
    print("        🏆 THE KILELE PYTHON JUNIOR MASTERY TRIVIA 🏆        ")
    print("=" * 65)
    print("Test your Python knowledge! 5 multiple-choice questions.\n")

    score = 0
    total_q = len(QUIZ_QUESTIONS)
    demo_answers = ["B", "C", "C", "B", "D"]  # 100% correct answers for testing

    for idx, q_data in enumerate(QUIZ_QUESTIONS):
        print(f"Question {idx + 1} of {total_q}:")
        print(f"  {q_data['question']}")
        print("-" * 55)
        for opt_key, opt_text in q_data["options"].items():
            print(f"    [{opt_key}] {opt_text}")

        correct_opt = q_data["answer"]
        auto_ans = demo_answers[idx]
        user_choice = get_input("\nYour Answer (A, B, C, or D): ", auto_ans)

        if user_choice == correct_opt:
            print("  ✔ Correct! +20 Points! 🌟")
            score += 1
        else:
            print(f"  ❌ Incorrect. The correct answer was [{correct_opt}].")
        print(f"  💡 Insight: {q_data['explanation']}\n")

    percent = int((score / total_q) * 100)
    print("=" * 65)
    print(f"{'QUIZ RESULTS SUMMARY':^65}")
    print("=" * 65)
    print(f"Score:            {score} / {total_q} correct ({percent}%)")

    if percent == 100:
        badge = "🥇 Grandmaster Scholar (Perfect Score!)"
    elif percent >= 80:
        badge = "🥈 Certified Python Builder"
    elif percent >= 60:
        badge = "🥉 Junior Developer (Passing Standard)"
    else:
        badge = "📚 Apprentice (Review Core Concepts)"

    print(f"Certificate Rank: {badge}")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_quiz()
