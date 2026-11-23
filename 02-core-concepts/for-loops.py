"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: for-loops.py
Description: Definite iteration and repeating instructions using for loops
=============================================================================

Learning Objectives:
1. Understand iteration and when to use for loops.
2. Master the range(start, stop, step) function.
3. Iterate over sequences (lists, strings).
4. Use accumulator variables to calculate totals and averages.
5. Apply break and continue control statements.
6. Build nested for loops.
"""

print("==================================================")
print("             LESSON 07: FOR LOOPS                 ")
print("==================================================")

# ==========================================
# 1. THE range() FUNCTION
# ==========================================
# range() generates a sequence of numbers on the fly.
# Syntax: range(start, stop, step)
# NOTE: The 'stop' number is NEVER included! range(1, 6) gives 1, 2, 3, 4, 5.

print("\n--- 1. Using range() ---")

# A. range(stop): starts at 0 by default
print("range(4):", end=" ")
for i in range(4):
    print(i, end=" ")
print()

# B. range(start, stop): explicit starting point
print("range(5, 10):", end=" ")
for i in range(5, 10):
    print(i, end=" ")
print()

# C. range(start, stop, step): custom count intervals
print("Even numbers (2 to 10):", end=" ")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# D. Counting backwards with a negative step:
print("Countdown:", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print("Lift off! 🚀")


# ==========================================
# 2. ITERATING OVER SEQUENCES
# ==========================================
print("\n--- 2. Iterating Over Lists and Strings ---")
subjects = ["Math", "Python", "Physics", "Robotics"]
for subject in subjects:
    print(f"I enjoy studying: {subject}")

# Looping over characters in a string:
word = "KILELE"
print("Spelling out:", end=" ")
for char in word:
    print(char, end="-")
print()


# ==========================================
# 3. ACCUMULATOR PATTERN
# ==========================================
# An accumulator is a variable initialized outside the loop that gathers
# results (e.g. running sum, product, or count).
print("\n--- 3. Accumulator Pattern ---")
weekly_study_hours = [2.5, 3.0, 1.5, 4.0, 2.0]
total_hours = 0.0

for hours in weekly_study_hours:
    total_hours += hours

average_hours = total_hours / len(weekly_study_hours)
print(f"Total study hours: {total_hours} hrs")
print(f"Average study per day: {average_hours:.1f} hrs")


# ==========================================
# 4. break AND continue
# ==========================================
print("\n--- 4. break and continue ---")
print("Searching for the number 7:")
for num in [2, 4, 6, 7, 8, 10]:
    if num == 7:
        print("  Found 7! Stopping search with break.")
        break  # Immediately exits the entire loop
    print(f"  Checked {num}... not 7.")

print("\nSkipping even numbers with continue:")
for num in range(1, 7):
    if num % 2 == 0:
        continue  # Skips the rest of this iteration and goes to the next
    print(f"  Odd number: {num}")


# ==========================================
# 5. NESTED FOR LOOPS (MULTIPLICATION TABLE)
# ==========================================
print("\n--- 5. Nested Loops: 3x3 Multiplication Grid ---")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:3}", end=" ")
    print()  # Newline after each row


# ==========================================
# 6. COMMON PITFALLS
# ==========================================
# Pitfall 1: Off-by-one error with range():
#   range(1, 5) generates 1, 2, 3, 4 (it stops BEFORE 5).
#   If you want 1 through 5, use range(1, 6).
#
# Pitfall 2: Modifying a list while looping over it:
#   Removing elements from a list while iterating over it causes skipped items.
