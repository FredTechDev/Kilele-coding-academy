# Milestone Assessment 1 — Python Fundamentals

> **Kilele Python Learning Pack · Formal Assessment**  
> *Coverage: Modules 01 to 04 (Introduction, Syntax, Variables, Data Types, I/O)*  
> *Target: Grades 7–10 / Introductory Programmers*  
> *Time Allowed: 45 minutes | Total Marks: 50*

---

## 🎯 Purpose of This Assessment
This assessment evaluates your grasp of computational thinking, Python grammar, memory allocation with variables, data types, type conversion, and console I/O.

---

## Part A: Multiple Choice & Syntax Rules (10 Marks)
*Choose the single best answer for each question (2 marks each).*

**1. What is the fundamental difference between RAM and Storage (SSD/Hard Drive)?**  
a) RAM is permanent; Storage is wiped when power is turned off.  
b) RAM holds temporary variables during active execution; Storage saves files long-term.  
c) RAM is only used for video games; Storage runs the Python interpreter.  
d) There is no difference; they are two names for the same chip.

**2. Which of the following is a legal Python variable identifier under PEP 8 conventions?**  
a) `2nd_place_score`  
b) `student-score`  
c) `student_score`  
d) `class`

**3. What does the `type()` function return for the value `"42.0"`?**  
a) `<class 'int'>`  
b) `<class 'float'>`  
c) `<class 'str'>`  
d) `<class 'bool'>`

**4. What is the output of the following statement: `print("Hi" * 3)`?**  
a) `Hi 3`  
b) `HiHiHi`  
c) `SyntaxError`  
d) `Hi, Hi, Hi`

**5. What is the data type returned by `input("Enter your age: ")` if the user types `15`?**  
a) Integer (`int`)  
b) String (`str`)  
c) Boolean (`bool`)  
d) Float (`float`)

---

## Part B: Code Output Tracing (10 Marks)
*Predict the exact output printed on the terminal without running the code (5 marks each).*

### Trace 1:
```python
x = 10
y = 3
x = x + 5
y = x - y
print("x:", x, "y:", y)
```
*Write your predicted output here:*

---

### Trace 2:
```python
first = "Kilele"
second = "20"
third = 26
print(first + " " + second + str(third))
```
*Write your predicted output here:*

---

## Part C: Bug Hunting & Debugging (10 Marks)
*Each snippet below has one fatal error that prevents it from running. Identify the bug and write the corrected line (5 marks each).*

### Bug 1:
```python
user_age = input("Enter your age: ")
years_to_eighteen = 18 - user_age
print("Years until 18:", years_to_eighteen)
```
- **Error Type:** `TypeError`
- **Why it failed:** __________________________________________________
- **Corrected Code:** __________________________________________________

### Bug 2:
```python
student_name = "Zawadi"
print("Welcome to Python, " student_name)
```
- **Error Type:** `SyntaxError`
- **Why it failed:** __________________________________________________
- **Corrected Code:** __________________________________________________

---

## Part D: Live Programming Challenge (15 Marks)
**Task: The School Event Ticket Invoice Generator**  
Write a complete, working script named `ticket_invoice.py` that fulfills these requirements:
1. Prompts the buyer for their name.
2. Prompts for the number of tickets desired (whole number).
3. Prompts for the price per single ticket (allowing decimals, e.g. `$12.50`).
4. Calculates:
   - Subtotal (`tickets * price_per_ticket`)
   - 10% School Development Levy (`subtotal * 0.10`)
   - Final Total Invoice (`subtotal + levy`)
5. Displays a neat, aligned ASCII receipt with clear dollar formatting.

---

## Part E: Conceptual Explanation / Viva Voce (5 Marks)
*Answer in 2 to 3 complete, thoughtful sentences:*

> *"Why does Python stop and raise a `ValueError` when you try to execute `int('twenty')`, but it successfully converts `int('20')`? What is the computer actually doing during type conversion?"*
