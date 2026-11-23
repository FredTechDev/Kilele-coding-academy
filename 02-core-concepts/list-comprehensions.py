"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: list-comprehensions.py
Description: Pythonic list and dictionary comprehensions for concise data mapping
=============================================================================

Learning Objectives:
1. Understand the syntax of list comprehensions: [expression for item in iterable].
2. Add conditional filters to comprehensions: [expr for item in iterable if condition].
3. Differentiate between standard for loops and comprehension syntax.
4. Construct dictionary comprehensions: {key_expr: val_expr for item in iterable}.
5. Learn when comprehensions improve readability and when standard loops are better.
"""

print("==================================================")
print("       LESSON 11B: LIST COMPREHENSIONS            ")
print("==================================================")

# ==========================================
# 1. TRADITIONAL LOOP VS COMPREHENSION
# ==========================================
# Suppose we want to square numbers from 1 to 5:

# Approach A: The traditional 4-line for loop:
squares_loop = []
for n in range(1, 6):
    squares_loop.append(n ** 2)

# Approach B: The elegant Pythonic list comprehension (1 line!):
# Formula: [WHAT_TO_DO_WITH_ITEM for ITEM in SEQUENCE]
squares_comp = [n ** 2 for n in range(1, 6)]

print("\n--- 1. Comparing Loop vs Comprehension ---")
print("Traditional Loop Output:       ", squares_loop)
print("List Comprehension Output:     ", squares_comp)


# ==========================================
# 2. FILTERING WITH AN if CLAUSE
# ==========================================
# Formula: [EXPRESSION for ITEM in SEQUENCE if CONDITION]
# Only items that satisfy the condition will be included in the new list!

numbers = [12, 5, 8, 19, 24, 7, 30, 3]

# Extract only even numbers:
even_numbers = [num for num in numbers if num % 2 == 0]
print("\n--- 2. Filtering Even Numbers ---")
print("Original numbers:   ", numbers)
print("Filtered even numbers:", even_numbers)

# Extract students who earned a Distinction (score >= 80):
scores = [72, 88, 95, 64, 82, 59, 90]
honors_scores = [s for s in scores if s >= 80]
print("Honors scores (>= 80):", honors_scores)


# ==========================================
# 3. TRANSFORMING STRINGS
# ==========================================
print("\n--- 3. Transforming Text ---")
raw_tags = ["  python ", "ROBOTICS", "  gamedev  ", "ai "]

# Strip whitespace and convert to lowercase in one clean line:
cleaned_tags = [tag.strip().lower() for tag in raw_tags]
print("Raw tags:    ", raw_tags)
print("Cleaned tags:", cleaned_tags)


# ==========================================
# 4. DICTIONARY COMPREHENSIONS
# ==========================================
# Syntax: {KEY_EXPR: VAL_EXPR for ITEM in SEQUENCE}
print("\n--- 4. Dictionary Comprehension ---")
students = ["Zawadi", "Faraji", "Amina", "Kofi"]

# Assign a starting default score of 100 credits to each student:
credit_balances = {name: 100 for name in students}
print("Initial credit balances:", credit_balances)

# Convert temperatures from Celsius to Fahrenheit:
celsius_temps = {"Nairobi": 24, "Mombasa": 30, "Nakuru": 21}
fahrenheit_temps = {city: round((c * 9/5) + 32, 1) for city, c in celsius_temps.items()}
print("Temperatures in °C:", celsius_temps)
print("Temperatures in °F:", fahrenheit_temps)


# ==========================================
# 5. BEST PRACTICES (WHEN NOT TO USE COMPREHENSIONS)
# ==========================================
# Rule of Thumb: If a list comprehension is longer than one line or has more than
# one 'for' or 'if', write a normal for loop!
# Readability always counts first in Python!
