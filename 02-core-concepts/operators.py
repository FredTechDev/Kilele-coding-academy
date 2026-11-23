"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: operators.py
Description: Mathematical calculations, comparisons, and boolean logic
=============================================================================

Learning Objectives:
1. Master all 7 arithmetic operators (+, -, *, /, //, %, **).
2. Understand comparison operators (==, !=, <, >, <=, >=).
3. Evaluate compound boolean logic using and, or, not.
4. Understand operator precedence (BODMAS / PEMDAS).
"""

print("==================================================")
print("             LESSON 05: OPERATORS                 ")
print("==================================================")

# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================
print("\n--- 1. Arithmetic Operators ---")
a = 17
b = 5

print(f"a = {a}, b = {b}")
print(f"Addition (a + b):         {a + b}")    # 22
print(f"Subtraction (a - b):      {a - b}")    # 12
print(f"Multiplication (a * b):   {a * b}")    # 85
print(f"Standard Division (a / b): {a / b}")   # 3.4 (Always yields a float!)
print(f"Floor Division (a // b):  {a // b}")   # 3   (Discards remainder)
print(f"Modulus / Remainder (a % b): {a % b}") # 2   (17 divided by 5 is 3 with remainder 2)
print(f"Exponent / Power (a ** 2): {a ** 2}")  # 289 (17 squared)

# Modulus Superpower: Checking if a number is even or odd!
number = 14
if number % 2 == 0:
    print(f"Bonus: {number} is EVEN because {number} % 2 == 0")
else:
    print(f"Bonus: {number} is ODD")


# ==========================================
# 2. COMPARISON OPERATORS
# ==========================================
# Comparison operators test relationships and ALWAYS return a Boolean (True or False):
print("\n--- 2. Comparison Operators ---")
score = 85
pass_mark = 70

print(f"score == pass_mark (Equal to):              {score == pass_mark}")  # False
print(f"score != pass_mark (Not equal to):          {score != pass_mark}")  # True
print(f"score > pass_mark  (Greater than):          {score > pass_mark}")   # True
print(f"score < 100        (Less than):              {score < 100}")         # True
print(f"score >= 85        (Greater than or equal): {score >= 85}")         # True
print(f"score <= 50        (Less than or equal):    {score <= 50}")         # False


# ==========================================
# 3. LOGICAL OPERATORS: and, or, not
# ==========================================
print("\n--- 3. Logical Operators ---")
has_ticket = True
has_student_id = False
is_banned = False

# 'and' requires BOTH conditions to be True:
can_get_student_discount = has_ticket and has_student_id
print("Ticket AND Student ID (Student Discount):", can_get_student_discount)

# 'or' requires AT LEAST ONE condition to be True:
can_enter = has_ticket or has_student_id
print("Ticket OR Student ID (Can Enter):       ", can_enter)

# 'not' reverses the truth value:
print("Is NOT banned (Allowed on campus):      ", not is_banned)


# ==========================================
# 4. OPERATOR PRECEDENCE (BODMAS / PEMDAS)
# ==========================================
# Order of evaluation:
# 1. Parentheses ( )
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor //, Modulus %
# 4. Addition +, Subtraction -
# 5. Comparisons (==, <, >)
# 6. Logical not, then and, then or

print("\n--- 4. Operator Precedence ---")
without_parentheses = 10 + 5 * 2    # 5 * 2 evaluated first -> 10 + 10 = 20
with_parentheses = (10 + 5) * 2       # (10 + 5) evaluated first -> 15 * 2 = 30

print("10 + 5 * 2   =", without_parentheses)
print("(10 + 5) * 2 =", with_parentheses)


# ==========================================
# 5. COMMON PITFALLS
# ==========================================
# Pitfall 1: Confusing '=' with '==':
#   if score = 100:  --> SyntaxError: invalid syntax (cannot assign inside condition)
#   Always use '==' for comparison!
#
# Pitfall 2: Chaining logic incorrectly:
#   if age == 14 or 15:  --> WRONG! '15' is truthy, so this is ALWAYS True!
#   Correct: if age == 14 or age == 15: OR if age in (14, 15):
