"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: conditionals.py
Description: Decision making and branching flow using if, elif, and else
=============================================================================

Learning Objectives:
1. Master if, elif, and else branching logic.
2. Understand Python block structure via indentation (4 spaces).
3. Build multi-way decision systems (e.g. grading scales).
4. Learn nested conditionals and combined conditions.
5. Identify boundary / edge case bugs.
"""

print("==================================================")
print("           LESSON 06: CONDITIONALS                ")
print("==================================================")

# ==========================================
# 1. BASIC if STATEMENT
# ==========================================
# An 'if' statement checks a condition. If it evaluates to True,
# Python runs the indented block of code underneath.
print("\n--- 1. Simple if ---")
temperature = 32

if temperature > 30:
    print(f"It is {temperature}°C — Drink plenty of water! 🥤")
print("This line runs regardless, because it is not indented.")


# ==========================================
# 2. TWO-WAY BRANCHING: if - else
# ==========================================
# 'else' provides a fallback path when the 'if' condition is False.
print("\n--- 2. if - else ---")
battery_percentage = 18

if battery_percentage >= 20:
    print("Battery level is healthy.")
else:
    print(f"Low battery warning: {battery_percentage}%! Please plug in your charger. ⚡")


# ==========================================
# 3. MULTI-WAY BRANCHING: if - elif - else
# ==========================================
# 'elif' stands for "else if". Python tests each condition in order from top to bottom.
# The FIRST condition that evaluates to True executes, and the rest are skipped!
print("\n--- 3. Academic Grading Scale (if - elif - else) ---")
test_scores = [92, 78, 64, 45]

for mark in test_scores:
    if mark >= 90:
        grade = "A (Distinction) 🌟"
    elif mark >= 80:
        grade = "B (Exceeding Expectations) 👍"
    elif mark >= 70:
        grade = "C (Meeting Expectations) ✔"
    elif mark >= 50:
        grade = "D (Approaching Standard) ⚠️"
    else:
        grade = "E (Needs Targeted Support) 📚"
    
    print(f"Score: {mark} ──▶ Grade: {grade}")


# ==========================================
# 4. NESTED CONDITIONS VS COMBINED CONDITIONS
# ==========================================
print("\n--- 4. Nested vs Combined Conditions ---")
student_age = 15
has_permission_slip = True

# Approach A: Nested conditionals (an if inside an if)
if student_age >= 13:
    if has_permission_slip:
        print("Approach A: Approved for the science field trip! 🚌")
    else:
        print("Approach A: Missing permission slip.")

# Approach B: Combined conditional using 'and' (cleaner & preferred when possible)
if student_age >= 13 and has_permission_slip:
    print("Approach B: Approved for the science field trip! 🚌")


# ==========================================
# 5. COMMON PITFALLS
# ==========================================
# Pitfall 1: Forgetting the colon ':' at the end of the if/elif/else line:
#   if age >= 18   --> SyntaxError: expected ':'
#
# Pitfall 2: Inconsistent indentation:
#   if age >= 18:
#   print("Adult") --> IndentationError: expected an indented block
#
# Pitfall 3: Wrong order in elif statements:
#   if mark >= 50: grade = "D"  # If this comes first, an 95 gets grade D!
#   Always check from most specific / highest threshold downward!
