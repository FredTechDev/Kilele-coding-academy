"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 4
Project: Number Guessing Game
File: number-guessing-game.py
Concepts Applied: random module, while loops, input validation, branching logic
=============================================================================
"""

import sys
import random

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return demo_val

def play_guessing_game():
    print("=" * 60)
    print("         🎯 THE SECRET NUMBER GUESSING CHALLENGE          ")
    print("=" * 60)
    print("I have generated a secret number between 1 and 100.")
    print("Can you crack it before running out of attempts?\n")

    diff_choice = get_input("Choose difficulty: [1] Easy (10)  [2] Medium (7)  [3] Hard (5): ", "2")
    max_attempts = 10 if diff_choice == "1" else (5 if diff_choice == "3" else 7)

    # In demo mode, fix target to 58 for predictable testing; otherwise random
    secret_target = 58 if "--demo" in sys.argv else random.randint(1, 100)
    demo_guesses = ["50", "75", "62", "58"]
    demo_idx = 0

    attempts_used = 0
    print(f"\nGame on! You have {max_attempts} attempts. Make your first guess:")

    while attempts_used < max_attempts:
        attempts_used += 1
        remaining = max_attempts - attempts_used

        if "--demo" in sys.argv:
            guess_str = demo_guesses[demo_idx]
            demo_idx = min(demo_idx + 1, len(demo_guesses) - 1)
            print(f"\n[Attempt {attempts_used}/{max_attempts}] Your guess: [Auto-demo]: {guess_str}")
        else:
            guess_str = get_input(f"\n[Attempt {attempts_used}/{max_attempts}] Your guess: ", "50")

        if not guess_str.isdigit():
            print("⚠️ Please enter a whole number between 1 and 100!")
            continue

        guess = int(guess_str)

        if guess == secret_target:
            print("\n" + "🎉" * 25)
            print(f"BINGO! You found the secret number {secret_target} in {attempts_used} attempts!")
            print("Score Rating: " + ("⭐⭐⭐ Superb!" if attempts_used <= 4 else "⭐⭐ Well Done!"))
            print("🎉" * 25 + "\n")
            return

        elif guess < secret_target:
            diff = secret_target - guess
            hint = " (Very close!)" if diff <= 5 else ""
            print(f"📈 TOO LOW!{hint} Attempts remaining: {remaining}")
        else:
            diff = guess - secret_target
            hint = " (Very close!)" if diff <= 5 else ""
            print(f"📉 TOO HIGH!{hint} Attempts remaining: {remaining}")

    print(f"\n💀 GAME OVER! You ran out of guesses. The secret number was: {secret_target}\n")

if __name__ == "__main__":
    play_guessing_game()
