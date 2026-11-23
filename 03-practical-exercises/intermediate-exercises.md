# Level 2 — Intermediate Exercises

> **Kilele Python Learning Pack · Practical Practice**  
> *Target: Grades 7–10 / Advancing Programmers*  
> *Concepts: Loops, Functions, Lists, Tuples, Dictionaries, Basic Error Handling*

---

## 🎯 Purpose of These Exercises
Level 2 exercises challenge you to combine multiple Python concepts together. Instead of writing isolated lines, you will construct reusable functions, navigate data structures, and handle repetitive logic with loops.

Attempt every exercise on your own before checking [`solutions/intermediate_solutions.py`](./solutions/intermediate_solutions.py).

---

### Exercise 1: Custom Multiplication Table Generator
**Problem:** Write a function `print_multiplication_table(base_number, up_to=10)` that uses a `for` loop to print a formatted times table for any given number up to a specified limit.  
**Sample Output:**
```text
=== 7 Times Table ===
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

### Exercise 2: Vowel and Consonant Counter
**Problem:** Write a function `analyze_text(text)` that counts how many vowels (`a, e, i, o, u`) and consonants are in a string. The function should ignore spaces and punctuation and be case-insensitive.  
**Sample Output:**
```text
Text: "Python is powerful!"
Vowels:     5
Consonants: 11
```

---

### Exercise 3: Scoreboard Analyzer
**Problem:** Write a function `analyze_scores(scores_list)` that takes a list of exam scores and returns a dictionary with:
- `"highest"`: Maximum score
- `"lowest"`: Minimum score
- `"average"`: Mean score rounded to 1 decimal place
- `"passed"`: Count of scores >= 50  
**Sample Output:**
```python
scores = [65, 88, 42, 95, 73, 50]
# Returns: {'highest': 95, 'lowest': 42, 'average': 68.8, 'passed': 5}
```

---

### Exercise 4: Interactive Grocery List Manager
**Problem:** Build an interactive terminal list manager that lets a user:
1. Add an item to their grocery list (`.append()`).
2. Remove an item by name (`.remove()` if present).
3. Display the sorted list.
4. Exit the program.  
Guard against removing items that are not in the list!

---

### Exercise 5: ATM 3-Attempt PIN Lockout System
**Problem:** Write a program with a secret 4-digit PIN stored in a constant `CORRECT_PIN = "2026"`.
- Use a `while` loop that gives the user a maximum of 3 attempts.
- If they enter the correct PIN, print `"Access Granted!"` and exit immediately.
- If they fail 3 times, print `"Account locked due to 3 incorrect attempts. Contact bank."`

---

### Exercise 6: Student Gradebook Dictionary
**Problem:** Create a dictionary where keys are student names and values are their assignment scores:
```python
grades = {"Zawadi": 92, "Faraji": 78, "Amani": 88, "Zuri": 64}
```
Write a loop that prints each student's name, their score, and whether they received Honors (score >= 85).

---

### Exercise 7: Dice Frequency Tracker
**Problem:** Write a function `simulate_dice_rolls(num_rolls)` that uses `random.randint(1, 6)` to roll a 6-sided die `num_rolls` times. Track the frequency of each face (1 through 6) using a dictionary or list, and print the results as a text bar chart.  
**Sample Output:**
```text
Rolling 100 times:
Face 1: ***************** (17)
Face 2: *************** (15)
Face 3: ****************** (18)
...
```

---

### Exercise 8: Palindrome Tester
**Problem:** A palindrome is a word or phrase that reads the same forwards and backwards (like `"radar"`, `"level"`, or `"racecar"`).  
Write a function `is_palindrome(word)` that returns `True` if a word is a palindrome and `False` otherwise. (Hint: Use string slicing `[::-1]` and `.lower()`).

---

### Exercise 9: Temperature Anomaly Filter
**Problem:** You are given a list of sensor temperature readings:
```python
readings = [21.5, 23.0, 48.9, 22.1, -15.0, 24.2, 22.8]
```
Write a function that filters out anomalies (readings lower than 0°C or higher than 40°C) and returns a clean list of valid room temperatures.

---

### Exercise 10: Crash-Proof Division Calculator
**Problem:** Write an interactive division calculator function that prompts for two numbers and divides them. Wrap the code in a `try...except` block that:
- Catches `ValueError` if the user types non-numeric text.
- Catches `ZeroDivisionError` if the second number is 0.
- Prints a clear, friendly error message instead of letting Python crash!
