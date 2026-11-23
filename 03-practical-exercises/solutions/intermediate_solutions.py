"""
=============================================================================
Kilele Python Learning Pack — Solutions
File: intermediate_solutions.py
Description: Reference solutions for Level 2 Intermediate Exercises (1 to 10)
=============================================================================
"""

import random

# Exercise 1: Custom Multiplication Table Generator
def print_multiplication_table(base_number, up_to=10):
    print(f"\n--- Exercise 1: {base_number} Times Table ---")
    for multiplier in range(1, up_to + 1):
        print(f"{base_number} x {multiplier:2d} = {base_number * multiplier}")


# Exercise 2: Vowel and Consonant Counter
def analyze_text(text):
    print(f"\n--- Exercise 2: Text Analysis for '{text}' ---")
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Vowels:     {vowel_count}")
    print(f"Consonants: {consonant_count}")
    return {"vowels": vowel_count, "consonants": consonant_count}


# Exercise 3: Scoreboard Analyzer
def analyze_scores(scores_list):
    print(f"\n--- Exercise 3: Score Analysis for {scores_list} ---")
    highest = max(scores_list)
    lowest = min(scores_list)
    average = round(sum(scores_list) / len(scores_list), 1)
    passed = sum(1 for s in scores_list if s >= 50)

    summary = {
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "passed": passed
    }
    print("Summary:", summary)
    return summary


# Exercise 4: Grocery List Manager Simulation
def demo_grocery_manager():
    print("\n--- Exercise 4: Grocery List Manager ---")
    groceries = ["Apples", "Bread", "Milk"]
    print("Initial items:", groceries)

    # Adding an item:
    groceries.append("Eggs")
    print("Added 'Eggs':", groceries)

    # Removing an item safely:
    item_to_remove = "Bread"
    if item_to_remove in groceries:
        groceries.remove(item_to_remove)
        print(f"Removed '{item_to_remove}':", groceries)
    
    print("Final sorted list:", sorted(groceries))


# Exercise 5: ATM PIN Lockout System
def verify_pin_attempts(entered_pins):
    print("\n--- Exercise 5: 3-Attempt PIN Verification ---")
    CORRECT_PIN = "2026"
    attempts_remaining = 3

    for entry in entered_pins:
        attempts_remaining -= 1
        if entry == CORRECT_PIN:
            print(f"Entry '{entry}': Access Granted! Welcome to your account. 💳")
            return True
        else:
            print(f"Entry '{entry}': Incorrect PIN! Attempts left: {attempts_remaining}")
            if attempts_remaining == 0:
                print("Account locked due to 3 incorrect attempts. Contact your bank.")
                return False
    return False


# Exercise 6: Student Gradebook Dictionary
def analyze_gradebook(grades):
    print("\n--- Exercise 6: Gradebook Honors Review ---")
    for name, score in grades.items():
        honors_badge = "🌟 Honors" if score >= 85 else "Standard"
        print(f"Student: {name:<8} | Score: {score}% | Status: {honors_badge}")


# Exercise 7: Dice Frequency Tracker
def simulate_dice_rolls(num_rolls=60):
    print(f"\n--- Exercise 7: Rolling a 6-Sided Die {num_rolls} Times ---")
    frequencies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(num_rolls):
        face = random.randint(1, 6)
        frequencies[face] += 1

    for face, count in frequencies.items():
        bar = "*" * count
        print(f"Face {face}: {bar:<15} ({count})")


# Exercise 8: Palindrome Tester
def is_palindrome(word):
    cleaned = "".join(c.lower() for c in word if c.isalnum())
    result = cleaned == cleaned[::-1]
    print(f"Is '{word}' a palindrome? ──▶ {result}")
    return result


# Exercise 9: Temperature Anomaly Filter
def filter_temperature_anomalies(readings):
    print(f"\n--- Exercise 9: Filtering Anomalies from {readings} ---")
    valid_readings = [temp for temp in readings if 0.0 <= temp <= 40.0]
    print("Valid Room Temperatures:", valid_readings)
    return valid_readings


# Exercise 10: Crash-Proof Division Calculator
def safe_divide_calculator(num1_str, num2_str):
    print(f"\n--- Exercise 10: Safe Division of '{num1_str}' / '{num2_str}' ---")
    try:
        n1 = float(num1_str)
        n2 = float(num2_str)
        result = n1 / n2
        print(f"Result: {n1} / {n2} = {result:.2f}")
        return result
    except ValueError:
        print("⚠️ Error: Please enter valid numbers only.")
    except ZeroDivisionError:
        print("⚠️ Error: Cannot divide by zero!")
    return None


if __name__ == "__main__":
    print("==================================================")
    print("    LEVEL 2 INTERMEDIATE SOLUTIONS DEMONSTRATION  ")
    print("==================================================")
    print_multiplication_table(7, up_to=5)
    analyze_text("Python is powerful!")
    analyze_scores([65, 88, 42, 95, 73, 50])
    demo_grocery_manager()
    verify_pin_attempts(["1111", "9999", "2026"])
    analyze_gradebook({"Zawadi": 92, "Faraji": 78, "Amani": 88, "Zuri": 64})
    simulate_dice_rolls(60)
    print("\n--- Exercise 8: Palindrome Check ---")
    is_palindrome("radar")
    is_palindrome("python")
    is_palindrome("Racecar")
    filter_temperature_anomalies([21.5, 23.0, 48.9, 22.1, -15.0, 24.2, 22.8])
    safe_divide_calculator("100", "4")
    safe_divide_calculator("50", "0")
    safe_divide_calculator("abc", "2")
