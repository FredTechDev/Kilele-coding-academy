"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: variables.py
Description: Storing and updating information in computer memory
=============================================================================

Learning Objectives:
1. Understand variables as labeled containers in memory.
2. Master variable assignment (=) and updating.
3. Learn Python naming conventions (snake_case) and legal variable rules.
4. Understand constants as a programmer convention (UPPER_CASE).
"""

print("==================================================")
print("             LESSON 01: VARIABLES                ")
print("==================================================")

# ==========================================
# 1. WHAT IS A VARIABLE?
# ==========================================
# Think of a variable as a labeled storage box in the computer's RAM.
# You give the box a name, and place a value inside it.

student_name = "Baraka"    # Storing text in a box named 'student_name'
student_age = 14          # Storing a whole number in 'student_age'
student_grade = 9         # Storing grade level

print("\n--- 1. Variable Assignment ---")
print("Student:", student_name)
print("Age:", student_age)
print("Grade:", student_grade)


# ==========================================
# 2. UPDATING AND REASSIGNING VARIABLES
# ==========================================
# The value inside a variable can change (it is "variable"!).
# Python evaluates the right side of the '=' first, then stores the result in the left side.

print("\n--- 2. Updating Variables ---")
game_score = 0
print("Initial Score:", game_score)

game_score = game_score + 10  # Add 10 points
print("After scoring a goal:", game_score)

# Shortcut assignment operators:
game_score += 15             # Same as: game_score = game_score + 15
print("After bonus points (+= 15):", game_score)


# ==========================================
# 3. VARIABLE NAMING RULES & PEP 8 CONVENTIONS
# ==========================================
print("\n--- 3. Python Naming Conventions ---")
# LEGAL RULES (Enforced by Python):
# 1. Must start with a letter (a-z, A-Z) or underscore (_).
# 2. Cannot start with a number (e.g. 2nd_place is ILLEGAL).
# 3. Can only contain letters, numbers, and underscores (no spaces, dashes, or symbols).
# 4. Cannot use Python reserved keywords (like 'print', 'if', 'while', 'for').

# PEP 8 STYLE CONVENTION (Best Practice for humans):
# In Python, multi-word variables use 'snake_case' (lowercase words with underscores):
favorite_sport = "Basketball"
player_health_points = 100
is_logged_in = True

print("Clean snake_case names:", favorite_sport, player_health_points, is_logged_in)


# ==========================================
# 4. CONSTANTS: VALUES THAT SHOULD NOT CHANGE
# ==========================================
print("\n--- 4. Constants ---")
# Python does not have a special 'locked' constant keyword,
# but programmers use ALL_CAPS to signal: "Please do NOT change this value!"
MAX_CLASS_SIZE = 30
DAYS_IN_A_WEEK = 7
ACADEMY_NAME = "Kilele Code Studio"

print("Max Class Size:", MAX_CLASS_SIZE)
print("Academy:", ACADEMY_NAME)


# ==========================================
# 5. MULTIPLE ASSIGNMENT
# ==========================================
print("\n--- 5. Multiple Assignment ---")
# You can assign multiple variables in one clean line:
x, y, z = 10, 20, 30
print("x:", x, "| y:", y, "| z:", z)

# Swapping two variables without a temporary helper variable:
a = "First"
b = "Second"
print("Before swap: a =", a, ", b =", b)
a, b = b, a
print("After swap:  a =", a, ", b =", b)


# ==========================================
# 6. COMMON PITFALLS & MISTAKES
# ==========================================
# Mistake 1: Using a variable before assigning it:
#   print(unassigned_score)  --> NameError: name 'unassigned_score' is not defined
#
# Mistake 2: Confusing '=' with '==':
#   '=' means ASSIGN (store value in box).
#   '==' means COMPARE (are these two things equal?).
#
# Mistake 3: Starting with a number:
#   1st_place = "Gold"  --> SyntaxError: invalid decimal literal


# ==========================================
# 7. PRACTICE EXERCISE
# ==========================================
print("\n--- Practice Exercise ---")
# Create variables for a library book:
# - book_title (string)
# - author_name (string)
# - publication_year (integer)
# - is_available (boolean)
# Print them in a formatted sentence!
book_title = "Adventures in Coding"
author_name = "Kilele Mentor"
publication_year = 2026
is_available = True

print(f"'{book_title}' by {author_name} ({publication_year}) - Available: {is_available}")
