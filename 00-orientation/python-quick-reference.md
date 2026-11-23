# Python 3 Quick Reference & Cheat Sheet

> **Kilele Code Studio · Student Reference Guide**  
> *Keep this file handy or bookmarked as you work through the curriculum!*

---

## 🔤 1. Fundamental Syntax & Output

```python
# Single-line comment
"""Multi-line docstring / commentary"""

# Output to terminal
print("Hello, Kilele!")              # Basic print
print("Name:", "Amani", "Age:", 14)  # Multiple items (separated by space)
print("Item", end=" ")               # Stay on same line (no newline)
print("A", "B", "C", sep=" | ")      # Custom separator: A | B | C

# Modern f-strings (formatted text)
score = 95
name = "Zawadi"
print(f"Student: {name} scored {score}%")
print(f"Price with two decimals: ${19.9:0.2f}")
```

---

## 📦 2. Data Types & Type Conversion

| Type | Name | Example | Notes |
| :--- | :--- | :--- | :--- |
| `str` | String | `"Python"`, `'code'` | Text inside quotes |
| `int` | Integer | `42`, `-7`, `0` | Whole numbers (no decimals) |
| `float` | Float | `3.14`, `-0.5`, `10.0` | Decimal numbers |
| `bool` | Boolean | `True`, `False` | Must be capitalized `True`/`False` |

```python
# Type Casting (Explicit Conversion)
int("25")       # ──▶ 25 (integer)
float("19.99")  # ──▶ 19.99 (float)
str(100)        # ──▶ "100" (string)
bool(1)         # ──▶ True (0 and "" are False; non-zero is True)

# Safe Input with conversion
raw_age = input("Enter your age: ").strip()
if raw_age.isdigit():
    age = int(raw_age)
```

---

## 🔢 3. Operators & Arithmetic

```python
# Arithmetic
10 + 3   # Addition ──▶ 13
10 - 3   # Subtraction ──▶ 7
10 * 3   # Multiplication ──▶ 30
10 / 3   # Division (always yields float) ──▶ 3.3333...
10 // 3  # Floor Division (discards remainder) ──▶ 3
10 % 3   # Modulus (returns remainder) ──▶ 1
2 ** 4   # Exponent / Power (2 to the power 4) ──▶ 16

# Comparisons (returns True or False)
x == y   # Equal to
x != y   # Not equal to
x > y    # Greater than
x < y    # Less than
x >= y   # Greater than or equal to
x <= y   # Less than or equal to

# Boolean Logic
x and y  # True ONLY if BOTH conditions are True
x or y   # True if AT LEAST ONE condition is True
not x    # Reverses the boolean truth state
```

---

## 🔀 4. Conditional Statements (Branching)

```python
score = 82

if score >= 90:
    print("Grade: A (Distinction)")
elif score >= 75:
    print("Grade: B (Merit)")
elif score >= 60:
    print("Grade: C (Credit)")
elif score >= 50:
    print("Grade: D (Pass)")
else:
    print("Grade: E (Referral)")
```

---

## 🔁 5. Loops (Iteration)

```python
# For Loop with range(start, stop, step)
for i in range(5):          # Generates: 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11, 2):   # Generates: 1, 3, 5, 7, 9
    print(i)

# While Loop with Counter
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1              # Essential: update condition variable!

# Infinite Game Loop pattern with break
while True:
    choice = input("Enter 'q' to quit: ")
    if choice.lower() == "q":
        break               # Immediately exits the loop
```

---

## 🧩 6. Functions

```python
def calculate_rectangle(width, height=5):
    """Calculates perimeter and area of a rectangle."""
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area  # Returns a tuple of two values

# Calling the function
p, a = calculate_rectangle(10, 4)
print(f"Perimeter: {p}, Area: {a}")
```

---

## 🗃 7. Collections Comparison

| Collection | Syntax | Mutable? | Ordered? | Duplicates? | Common Use Case |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **List** | `[1, 2, 3]` | Yes | Yes | Yes | Dynamic collections (rosters, items) |
| **Tuple** | `(1, 2, 3)` | No | Yes | Yes | Fixed records, (x, y) coordinates |
| **Dictionary**| `{"a": 1}` | Yes | Keys: Unique | Values: Yes | Key-value mapping, database records |
| **Set** | `{1, 2, 3}` | Yes | No | **No** | Unique items, tags, Venn diagrams |

```python
# List Operations
items = ["apple", "banana"]
items.append("orange")      # Add to end
items.pop(0)                # Remove by index
items.remove("banana")      # Remove by value

# Dictionary Operations
student = {"name": "Amina", "score": 92}
student["grade"] = 9        # Add or update key
print(student.get("age", 14)) # Safe lookup with fallback

# Set Operations
group_a = {"Amani", "Zawadi"}
group_b = {"Zawadi", "Kofi"}
print(group_a | group_b)    # Union (all unique students)
print(group_a & group_b)    # Intersection (students in both groups)
```

---

## 🛡 8. Error Handling & Files

```python
# Defensive Error Handling
try:
    number = int(input("Enter number: "))
    result = 100 / number
except ValueError:
    print("That was not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Done handling operation.")

# Safe File Handling with context manager
with open("notes.txt", "w") as f:
    f.write("Line 1\nLine 2\n")

with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())
```
