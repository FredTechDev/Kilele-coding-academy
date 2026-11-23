"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: functions.py
Description: Creating reusable, modular blocks of code with def and return
=============================================================================

Learning Objectives:
1. Define and call functions using the def keyword.
2. Pass arguments into parameters, including default values.
3. Understand return values vs console printing.
4. Grasp variable scope: local vs global variables.
5. Decompose complex problems into clean, single-responsibility functions.
"""

print("==================================================")
print("             LESSON 09: FUNCTIONS                 ")
print("==================================================")

# ==========================================
# 1. DEFINING AND CALLING A FUNCTION
# ==========================================
# A function is a named block of code that performs a specific task.
# Defining a function does NOT run it; you must call it by name.

def greet_learner():
    """Prints a friendly greeting to a new coder."""
    print("Habari! Welcome to Kilele Code Studio.")

# Calling (invoking) the function:
print("\n--- 1. Calling a Basic Function ---")
greet_learner()


# ==========================================
# 2. PARAMETERS AND ARGUMENTS
# ==========================================
# Parameters are the placeholder variables declared inside the function's parentheses.
# Arguments are the actual values passed in when the function is called.

def personalized_welcome(student_name, cohort_year=2026):
    """Greets a student by name with a default cohort year."""
    print(f"Welcome, {student_name}! You are enrolled in Class of {cohort_year}.")

print("\n--- 2. Parameters & Default Arguments ---")
personalized_welcome("Zawadi")                # Uses default cohort_year: 2026
personalized_welcome("Faraji", cohort_year=2027) # Overrides cohort_year


# ==========================================
# 3. RETURN VALUES VS PRINT
# ==========================================
# CRITICAL CONCEPT:
# - print() displays text on the screen for the human to see.
# - return sends data back to the calling code so it can be saved or used in further calculations!

def calculate_rectangle_area(width, height):
    """Calculates and returns the area of a rectangle."""
    area = width * height
    return area  # Sends the calculated number back

print("\n--- 3. Using Return Values ---")
room_area = calculate_rectangle_area(5, 4)
print(f"Room area: {room_area} square meters")

# Using the returned value in another calculation:
cost_per_sqm = 15.00
total_flooring_cost = room_area * cost_per_sqm
print(f"Total flooring cost: ${total_flooring_cost:.2f}")


# ==========================================
# 4. VARIABLE SCOPE (LOCAL VS GLOBAL)
# ==========================================
# Variables created inside a function are LOCAL to that function.
# They do not exist outside the function!

global_school_motto = "Excellence in Code"  # GLOBAL variable

def demo_scope():
    local_secret = "Only inside demo_scope!"  # LOCAL variable
    print("Inside function: Can see global motto:", global_school_motto)
    print("Inside function: Can see local secret:", local_secret)

print("\n--- 4. Variable Scope ---")
demo_scope()
# print(local_secret)  --> NameError! local_secret does not exist out here.


# ==========================================
# 5. MODULAR DECOMPOSITION
# ==========================================
# Professional software breaks large tasks into small, dedicated functions:
print("\n--- 5. Decomposition Example ---")

def calculate_average(scores):
    """Returns the arithmetic mean of a list of scores."""
    return sum(scores) / len(scores)

def assign_grade(average):
    """Returns a letter grade based on an average mark."""
    if average >= 80:
        return "Distinction"
    elif average >= 65:
        return "Credit"
    elif average >= 50:
        return "Pass"
    return "Referral"

def print_student_report(name, scores):
    """Coordinates reporting for a student."""
    avg = calculate_average(scores)
    grade = assign_grade(avg)
    print(f"Student: {name} | Average: {avg:.1f}% | Outcome: {grade}")

print_student_report("Amina", [88, 92, 79, 95])
print_student_report("Kofi", [55, 62, 58, 60])
