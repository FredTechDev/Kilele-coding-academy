"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: user-input.py
Description: Interacting with users via the terminal using input()
=============================================================================

Learning Objectives:
1. Receive input from the keyboard using the input() function.
2. Understand the Golden Rule: input() ALWAYS returns a string (str).
3. Sanitize and clean user text with .strip(), .lower(), .upper(), and .title().
4. Format output dynamically using modern f-strings.
"""

import sys

print("==================================================")
print("            LESSON 03: USER INPUT                ")
print("==================================================")

# ==========================================
# 1. HOW input() WORKS
# ==========================================
# The input() function pauses your program and waits for the user to type something
# in the terminal and press Enter.
# The prompt message inside the parentheses is displayed to the user.

print("\n--- 1. The input() Function ---")

# Helper for demo / automated testing without blocking:
def get_user_input(prompt, demo_fallback):
    if "--demo" in sys.argv:
        print(f"{prompt}[Demo mode auto-fill]: '{demo_fallback}'")
        return demo_fallback
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print(f"\n[Default applied]: '{demo_fallback}'")
        return demo_fallback

user_name = get_user_input("Enter your name: ", "Nia")
print(f"Hello, {user_name}! Welcome to Python.")


# ==========================================
# 2. THE GOLDEN RULE OF input()
# ==========================================
# CRITICAL CONCEPT: No matter what the user types (even numbers like 42),
# input() ALWAYS captures it as a String ('str')!
print("\n--- 2. The Golden Rule of input() ---")
entered_number = get_user_input("Enter a number: ", "25")
print(f"You entered: {entered_number}")
print(f"Data type is: {type(entered_number)}")  # Always <class 'str'>!

# To do math with user input, we must convert it (covered in Lesson 04).


# ==========================================
# 3. CLEANING USER INPUT (SANITIZATION)
# ==========================================
# Users often make accidental typos, like adding extra spaces or wrong casing.
# Python gives us helpful string methods to clean up input:

print("\n--- 3. Cleaning User Input ---")
raw_input = "   kilele student   "

# .strip(): removes accidental spaces from the beginning and end
cleaned_input = raw_input.strip()
print(f"Original: '{raw_input}'")
print(f"After .strip(): '{cleaned_input}'")

# .lower() and .upper(): converts case
print(f".lower(): '{cleaned_input.lower()}'")
print(f".upper(): '{cleaned_input.upper()}'")

# .title(): capitalizes the first letter of each word (great for names!)
print(f".title(): '{cleaned_input.title()}'")


# ==========================================
# 4. PRACTICAL MINI-INTERACTION
# ==========================================
print("\n--- 4. Mini Profile Generator ---")
city = get_user_input("What city are you coding from? ", "Nairobi").strip().title()
dream_project = get_user_input("What do you want to build with code? ", "Video Games").strip()

print("\n" + "=" * 40)
print(f"Coder Profile: {user_name.strip().title()}")
print(f"Location:      {city}")
print(f"Vision:        Building {dream_project}")
print("=" * 40)


# ==========================================
# 5. COMMON PITFALLS
# ==========================================
# Pitfall 1: Forgetting a space at the end of the prompt:
#   name = input("Enter name:")   --> User types right against the colon: Enter name:Alice
#   Better: input("Enter name: ")  --> Clean separation: Enter name: Alice
#
# Pitfall 2: Trying to do math directly on input():
#   age = input("Age: ")
#   print(age + 1)  --> TypeError: can only concatenate str to str!
