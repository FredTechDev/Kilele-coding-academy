"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: strings.py
Description: Manipulating text, string slicing, methods, and formatting
=============================================================================

Learning Objectives:
1. Master zero-based indexing and negative indexing for strings.
2. Extract substrings using slicing [start:stop:step].
3. Understand that strings are immutable.
4. Utilize core string methods (.split(), .join(), .replace(), .count(), etc.).
5. Master modern f-string formatting.
"""

print("==================================================")
print("             LESSON 10: STRINGS                   ")
print("==================================================")

text = "Python Programming"

# ==========================================
# 1. ZERO-BASED & NEGATIVE INDEXING
# ==========================================
# In Python, indexing starts at 0!
# Positive indexes count from the front: 0, 1, 2...
# Negative indexes count from the back: -1, -2, -3...
print("\n--- 1. String Indexing ---")
print("Full string:        ", text)
print("First character [0]: ", text[0])    # 'P'
print("Second character [1]:", text[1])    # 'y'
print("Last character [-1]: ", text[-1])   # 'g'
print("Second to last [-2]: ", text[-2])   # 'n'


# ==========================================
# 2. STRING SLICING [start:stop:step]
# ==========================================
# Slicing extracts a range of characters.
# The 'stop' index is NOT included!
print("\n--- 2. String Slicing ---")
print("Characters 0 to 6 [0:6]:   ", text[0:6])     # 'Python'
print("From index 7 to end [7:]:  ", text[7:])      # 'Programming'
print("Every second letter [::2]: ", text[::2])     # 'Pto rgamn'
print("Reverse the string [::-1]: ", text[::-1])    # 'gnimmargorP nohtyP'


# ==========================================
# 3. STRINGS ARE IMMUTABLE
# ==========================================
# You cannot change a character inside an existing string:
#   text[0] = "J"  --> TypeError: 'str' object does not support item assignment
# To modify text, you create a new string:
modified_text = "J" + text[1:]
print("\n--- 3. Immutability ---")
print("New string created: ", modified_text)


# ==========================================
# 4. ESSENTIAL STRING METHODS
# ==========================================
print("\n--- 4. String Methods ---")
sentence = "  kilele students build real-world software solutions!  "

print("Trimmed (.strip()):        ", sentence.strip())
print("Word Count of 'software':  ", sentence.count("software"))
print("Starts with '  kilele':    ", sentence.startswith("  kilele"))
print("Replaced word (.replace()):", sentence.replace("software", "AI").strip())

# Splitting and Joining:
words_list = sentence.strip().split(" ")
print("Split into list of words:  ", words_list)
reconnected = "-".join(words_list)
print("Reconnected with hyphens:  ", reconnected)


# ==========================================
# 5. MODERN F-STRING FORMATTING
# ==========================================
print("\n--- 5. Advanced f-String Tricks ---")
item = "Microcontroller Kit"
qty = 3
unit_cost = 45.50
total = qty * unit_cost

# Aligning and formatting decimals with f-strings:
print(f"Item: {item:<25} | Qty: {qty:02d} | Total: ${total:>7.2f}")
