"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 2
Project: Smart Calculator
File: smart-calculator.py
Concepts Applied: User input, arithmetic operators, functions, conditionals
=============================================================================
"""

import sys

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a // b
def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a % b
def power(a, b): return a ** b

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return demo_val

def run_smart_calculator():
    print("=" * 55)
    print("           KILELE SMART TERMINAL CALCULATOR             ")
    print("=" * 55)

    operations = {
        "1": ("Addition (+)", add),
        "2": ("Subtraction (-)", subtract),
        "3": ("Multiplication (*)", multiply),
        "4": ("Standard Division (/)", divide),
        "5": ("Floor Division (//)", floor_divide),
        "6": ("Modulus / Remainder (%)", modulus),
        "7": ("Exponent / Power (**)", power)
    }

    demo_steps = [
        ("1", "45", "15"),      # 45 + 15 = 60
        ("4", "100", "4"),      # 100 / 4 = 25
        ("7", "2", "8"),        # 2 ** 8 = 256
        ("quit", "0", "0")
    ]
    step_idx = 0

    while True:
        print("\nSelect an Operation:")
        for key, (label, _) in operations.items():
            print(f"  [{key}] {label}")
        print("  [quit] Exit Calculator")

        if "--demo" in sys.argv:
            choice, num1_demo, num2_demo = demo_steps[step_idx]
            step_idx = min(step_idx + 1, len(demo_steps) - 1)
            print(f"\nEnter choice: [Auto-demo]: {choice}")
        else:
            choice = get_input("\nEnter choice: ", "quit")

        if choice.lower() in ["quit", "q", "exit"]:
            print("Thank you for using Kilele Smart Calculator! Goodbye. 👋")
            break

        if choice not in operations:
            print("⚠️ Invalid menu selection! Please choose a number from 1 to 7.")
            continue

        op_name, op_func = operations[choice]

        if "--demo" in sys.argv:
            n1_raw = num1_demo
            n2_raw = num2_demo
            print(f"Enter first number:  [Auto-demo]: {n1_raw}")
            print(f"Enter second number: [Auto-demo]: {n2_raw}")
        else:
            n1_raw = get_input("Enter first number:  ", "10")
            n2_raw = get_input("Enter second number: ", "5")

        try:
            num1 = float(n1_raw)
            num2 = float(n2_raw)
            calc_result = op_func(num1, num2)
            print("\n" + "-" * 35)
            print(f"Computation: {num1} via {op_name}")
            print(f"RESULT:      {calc_result:.4f}".rstrip('0').rstrip('.'))
            print("-" * 35)
        except ValueError:
            print("⚠️ Error: Please enter valid numerical digits!")
        except ZeroDivisionError as err:
            print(f"⚠️ Math Error: {err}")

        if "--demo" in sys.argv and step_idx >= 3:
            print("\n[Auto-demo completed test runs. Exiting cleanly.]")
            break

if __name__ == "__main__":
    run_smart_calculator()
