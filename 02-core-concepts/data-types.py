"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: data-types.py
Description: The four fundamental data types in Python: str, int, float, bool
=============================================================================

Learning Objectives:
1. Identify and use the 4 primitive Python data types: str, int, float, bool.
2. Inspect data types using the type() function.
3. Understand how data type affects operation behavior (e.g. text vs numbers).
4. Recognize type error scenarios.
"""

print("==================================================")
print("            LESSON 02: DATA TYPES                ")
print("==================================================")

# ==========================================
# 1. THE FOUR CORE PRIMITIVE TYPES
# ==========================================

# 1. String (str): Text enclosed in single, double, or triple quotes.
city = "Nairobi"
motto = 'Code the Future'

# 2. Integer (int): Whole numbers (positive, negative, or zero) with no decimal point.
students_count = 28
temperature_celsius = -4

# 3. Floating-point number (float): Numbers containing a decimal point.
item_price = 19.99
pi_value = 3.14159

# 4. Boolean (bool): Only two possible states: True or False (note capitalized T and F).
has_passed_exam = True
is_game_over = False

print("\n--- 1. Displaying Different Data Types ---")
print("String:  ", city, "|", motto)
print("Integer: ", students_count, "|", temperature_celsius)
print("Float:   ", item_price, "|", pi_value)
print("Boolean: ", has_passed_exam, "|", is_game_over)


# ==========================================
# 2. CHECKING TYPES WITH type()
# ==========================================
# Python knows the type of every piece of data. We can inspect it with type():
print("\n--- 2. Checking Types with type() ---")
print("Type of city:               ", type(city))               # <class 'str'>
print("Type of students_count:     ", type(students_count))     # <class 'int'>
print("Type of item_price:         ", type(item_price))         # <class 'float'>
print("Type of has_passed_exam:    ", type(has_passed_exam))    # <class 'bool'>


# ==========================================
# 3. WHY DATA TYPES MATTER!
# ==========================================
# The '+' operator does completely different things depending on data types!
print("\n--- 3. Behavior Depends on Data Type ---")

# Numbers: Performs mathematical addition
num1 = 10
num2 = 20
print("Integer Addition (10 + 20):", num1 + num2)               # 30

# Strings: Performs concatenation (gluing text together)
text1 = "10"
text2 = "20"
print("String Concatenation ('10' + '20'):", text1 + text2)     # "1020"


# ==========================================
# 4. COMMON PITFALLS
# ==========================================
# Pitfall 1: TypeError when combining incompatible types:
#   print("Total: " + 50)  --> TypeError: can only concatenate str (not "int") to str
#   Fix: Use a comma: print("Total:", 50) or an f-string: print(f"Total: {50}")
#
# Pitfall 2: Forgetting capitalization for Booleans:
#   active = true   --> NameError: name 'true' is not defined (must be True)
#
# Pitfall 3: Quotation marks around numbers:
#   age = "15"  --> This is a string, not a number! You cannot do math on it directly.


# ==========================================
# 5. PRACTICE EXERCISE
# ==========================================
print("\n--- Practice Exercise ---")
# Predict the data type of each variable:
val_a = "False"      # String (because it is wrapped in quotes!)
val_b = False        # Boolean
val_c = 100          # Integer
val_d = 100.0        # Float (even with .0, it's a float!)

print(f"val_a is {type(val_a).__name__}")
print(f"val_b is {type(val_b).__name__}")
print(f"val_c is {type(val_c).__name__}")
print(f"val_d is {type(val_d).__name__}")
