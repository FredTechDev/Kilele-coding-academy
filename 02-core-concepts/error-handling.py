"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: error-handling.py
Description: Handling runtime errors gracefully using try, except, else, finally
=============================================================================

Learning Objectives:
1. Differentiate between Syntax, Runtime, and Logical errors.
2. Read and interpret Python tracebacks calmly.
3. Catch specific exceptions with try and except blocks.
4. Understand the purpose of else and finally clauses.
5. Implement crash-proof input validation loops.
"""

print("==================================================")
print("          LESSON 15: ERROR HANDLING               ")
print("==================================================")

# ==========================================
# 1. THE THREE KINDS OF PROGRAM ERRORS
# ==========================================
# 1. Syntax Error: Grammatical violation (e.g. missing colon, typo in keyword).
#    Python refuses to run the program at all.
#
# 2. Runtime Error (Exception): Occurs while running when an illegal operation is attempted
#    (e.g. dividing by zero, converting 'abc' to int, accessing missing key).
#
# 3. Logical Error: The code runs without crashing, but the math or logic is wrong,
#    producing incorrect answers (e.g. using + instead of -).


# ==========================================
# 2. THE try / except BLOCK
# ==========================================
# Instead of letting runtime exceptions crash your application, you intercept them:
print("\n--- 2. Catching a ZeroDivisionError ---")

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("  ⚠️ Warning: Attempted division by zero! Returning 0.0.")
        return 0.0

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))


# ==========================================
# 3. CATCHING MULTIPLE SPECIFIC EXCEPTIONS
# ==========================================
print("\n--- 3. Multiple Specific Exception Handlers ---")

def process_stake(user_text):
    try:
        amount = int(user_text)
        if amount <= 0:
            raise ValueError("Stake must be a positive integer!")
        print(f"  Valid stake accepted: ${amount}")
    except ValueError as err:
        print(f"  Rejected: Invalid entry '{user_text}' -> {err}")

process_stake("50")       # Valid
process_stake("-10")      # Caught by ValueError
process_stake("fifty")    # Caught by ValueError


# ==========================================
# 4. try - except - else - finally
# ==========================================
# - 'else' runs ONLY if NO exceptions were raised.
# - 'finally' ALWAYS runs no matter what (ideal for closing files or cleanup).
print("\n--- 4. Full try-except-else-finally Flow ---")

def complete_flow_demo(number_str):
    print(f"\nTesting with input: '{number_str}'")
    try:
        val = int(number_str)
        reciprocal = 100 / val
    except ValueError:
        print("  [except]: Could not convert text to integer.")
    except ZeroDivisionError:
        print("  [except]: Cannot calculate 100 / 0.")
    else:
        print(f"  [else]: Calculation succeeded! Result: {reciprocal}")
    finally:
        print("  [finally]: Cleanup finished. Moving on...")

complete_flow_demo("25")
complete_flow_demo("0")
complete_flow_demo("abc")
