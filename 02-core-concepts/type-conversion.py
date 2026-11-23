"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: type-conversion.py
Description: Converting data between types (Type Casting) safely
=============================================================================

Learning Objectives:
1. Understand explicit type casting with int(), float(), str(), and bool().
2. Differentiate between implicit conversion and explicit casting.
3. Master converting user input strings into calculable numbers.
4. Understand Truthy and Falsy values in Python.
5. Prevent ValueError crashes using .isdigit().
"""

print("==================================================")
print("         LESSON 04: TYPE CONVERSION              ")
print("==================================================")

# ==========================================
# 1. EXPLICIT CONVERSION FUNCTIONS
# ==========================================
# Python provides built-in functions named after the target type:
# - int(x):   converts x to an integer
# - float(x): converts x to a floating-point number
# - str(x):   converts x to a string
# - bool(x):  converts x to a boolean

print("\n--- 1. Basic Type Casting ---")
text_number = "50"
converted_int = int(text_number)
print(f"Original: '{text_number}' ({type(text_number).__name__}) ──▶ Converted: {converted_int} ({type(converted_int).__name__})")
print(f"Now we can do math: {converted_int} + 25 = {converted_int + 25}")

# Converting to float:
price_text = "19.95"
price_float = float(price_text)
print(f"Float price: ${price_float:.2f} | With tax (+1.00): ${price_float + 1.00:.2f}")

# Converting integer to string:
score = 98
score_message = "Your exam score is " + str(score) + "%!"
print(score_message)


# ==========================================
# 2. IMPLICIT CONVERSION (AUTOMATIC CASTING)
# ==========================================
# When combining an integer and a float, Python automatically promotes the result to float:
print("\n--- 2. Implicit Conversion ---")
whole_num = 10         # int
decimal_num = 4.5      # float
result = whole_num + decimal_num
print(f"{whole_num} (int) + {decimal_num} (float) = {result} ({type(result).__name__})")


# ==========================================
# 3. TRUTHY AND FALSY VALUES
# ==========================================
# In Python, almost every value can be evaluated as a Boolean:
# FALSY values (evaluate to False):
#   - Number 0, 0.0
#   - Empty string ""
#   - Empty list [], empty dict {}
#   - None
# TRUTHY values (evaluate to True):
#   - Any non-zero number (e.g. 1, -5, 3.14)
#   - Any non-empty string (e.g. "hello", " ")

print("\n--- 3. Truthy vs Falsy ---")
print("bool(0):          ", bool(0))             # False
print("bool(42):         ", bool(42))            # True
print("bool(''):         ", bool(""))            # False (empty string)
print("bool('Kilele'):   ", bool("Kilele"))      # True


# ==========================================
# 4. PREVENTING ValueError WITH .isdigit()
# ==========================================
# What happens if a user types 'banana' when you ask for an age?
# int("banana") causes a ValueError crash!
# We can validate using .isdigit() before converting:

print("\n--- 4. Safe Input Validation ---")
test_inputs = ["14", "twenty", " 25 "]

for user_entry in test_inputs:
    cleaned = user_entry.strip()
    if cleaned.isdigit():
        validated_age = int(cleaned)
        print(f"SUCCESS: '{user_entry}' is numeric! Converted to int: {validated_age}")
    else:
        print(f"REJECTED: '{user_entry}' contains non-digits. Cannot safely convert to int.")


# ==========================================
# 5. COMMON PITFALLS
# ==========================================
# Pitfall 1: Truncation when casting float to int:
#   int(9.99) becomes 9, NOT 10! It simply chops off the decimal part.
#   If you want rounding, use round(9.99) -> 10.
#
# Pitfall 2: Converting a decimal string directly with int():
#   int("19.95")  --> ValueError: invalid literal for int()!
#   Fix: Convert to float first: int(float("19.95")) -> 19
