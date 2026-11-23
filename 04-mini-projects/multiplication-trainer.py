"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 5
Project: Speed Multiplication Trainer
File: multiplication-trainer.py
Concepts Applied: for loops, random number generation, scoring, time tracking
=============================================================================
"""

import sys
import random
import time

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return demo_val

def run_math_trainer():
    print("=" * 60)
    print("       ⚡ KILELE SPEED MULTIPLICATION MATH TRAINER ⚡      ")
    print("=" * 60)
    print("Sharpen your mental math! Answer 5 rapid multiplication drills.\n")

    rounds = 5
    score = 0

    # In demo mode, use pre-determined problem pairs for testing:
    demo_problems = [(6, 7, "42"), (9, 8, "72"), (12, 5, "60"), (7, 7, "49"), (8, 4, "32")]

    start_time = time.time()

    for round_num in range(1, rounds + 1):
        if "--demo" in sys.argv:
            n1, n2, ans_str = demo_problems[round_num - 1]
        else:
            n1 = random.randint(2, 12)
            n2 = random.randint(2, 12)
            ans_str = str(n1 * n2)

        correct_answer = n1 * n2

        prompt = f"Question {round_num}/{rounds}: What is {n1} x {n2}? "
        user_answer_raw = get_input(prompt, ans_str)

        try:
            user_answer = int(user_answer_raw)
            if user_answer == correct_answer:
                print("  ✔ Correct! +10 points 🌟")
                score += 1
            else:
                print(f"  ❌ Incorrect. {n1} x {n2} = {correct_answer}")
        except ValueError:
            print(f"  ⚠️ Invalid input. Correct answer was {correct_answer}")

    elapsed_time = round(time.time() - start_time, 1)

    print("\n" + "=" * 50)
    print("                 TRAINING SUMMARY                 ")
    print("=" * 50)
    print(f"Total Score:     {score} out of {rounds} correct ({int((score/rounds)*100)}%)")
    print(f"Time Taken:      {elapsed_time} seconds")

    if score == rounds:
        print("Rating:          🏆 Math Grandmaster! Perfect accuracy!")
    elif score >= 3:
        print("Rating:          👍 Solid Performance! Keep sharpening.")
    else:
        print("Rating:          📚 Needs Practice. Try again to build speed!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    run_math_trainer()
