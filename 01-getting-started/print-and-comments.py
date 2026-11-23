"""
=============================================================================
Kilele Python Learning Pack — Lesson 1.2
File: print-and-comments.py
Description: Mastering console output with print() and documenting with comments
=============================================================================

Learning Objectives:
1. Master the print() function: strings, numbers, multiple items, and formatting.
2. Understand how to use single-line comments (#) and docstrings.
3. Understand escape sequences like \\n (new line) and \\t (tab).
4. Discover separator (sep) and ending (end) parameters in print().
"""

# ==========================================
# 1. COMMENTS: NOTES FOR HUMANS
# ==========================================
# This line is a single-line comment.
# The Python interpreter completely ignores anything after the '#' symbol.
# Comments exist to explain WHY you wrote something, helping other humans (and future you).

print("--- Part 1: Comments ---")
print("Comments are invisible to Python execution, but vital for humans!")

# You can also add comments at the end of a line (inline comment):
print("Python executes this line.")  # This note explains the line


# ==========================================
# 2. PRINTING NUMBERS AND CALCULATIONS
# ==========================================
# Unlike text, numbers do NOT need quotes around them.
print("\n--- Part 2: Printing Numbers and Math ---")
print(42)           # An integer (whole number)
print(3.14159)      # A float (decimal number)

# Python can do arithmetic directly inside print():
print(10 + 5)       # Addition: 15
print(20 - 4)       # Subtraction: 16
print(6 * 7)        # Multiplication: 42
print(100 / 4)      # Division: 25.0


# ==========================================
# 3. PRINTING MULTIPLE ITEMS
# ==========================================
# You can pass multiple values separated by commas.
# By default, Python puts a single space between them.
print("\n--- Part 3: Multiple Arguments ---")
print("Student Name:", "Zawadi", "| Grade:", 8)
print("Math score:", 95, "out of", 100)


# ==========================================
# 4. SPECIAL CHARACTERS (ESCAPE SEQUENCES)
# ==========================================
# \n creates a brand new line.
# \t inserts a tab indentation.
print("\n--- Part 4: Escape Sequences ---")
print("Line 1\nLine 2\nLine 3")
print("Item\tQuantity\tPrice")
print("Pen\t10\t\t$2.00")
print("Book\t3\t\t$15.00")


# ==========================================
# 5. CUSTOMIZING PRINT: sep AND end
# ==========================================
print("\n--- Part 5: Custom Separators & Endings ---")

# Using 'sep' to change what separates the values:
print("2026", "11", "23", sep="-")          # 2026-11-23
print("apple", "banana", "mango", sep=" | ") # apple | banana | mango

# By default, print() ends with a new line (\n).
# We can change 'end' to stay on the same line:
print("Counting down: 3... ", end="")
print("2... ", end="")
print("1... ", end="")
print("BLAST OFF! 🚀")


# ==========================================
# 6. TRY IT YOURSELF! (EXERCISES)
# ==========================================
print("\n--- Practice Challenge ---")
# Task 1: Print your name, age, and favorite subject on one line separated by ' -- '.
# Task 2: Print a 3x3 tic-tac-toe grid using print() statements!
# Example solution for Task 2:
print(" X | O | X ")
print("---+---+---")
print(" O | X | O ")
print("---+---+---")
print(" X |   | O ")
