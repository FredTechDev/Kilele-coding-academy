# Milestone Assessment 3 — Functions & Data Structures

> **Kilele Python Learning Pack · Formal Assessment**  
> *Coverage: Modules 08 to 10 (Functions, Scope, Lists, Tuples, Dictionaries, Randomness)*  
> *Target: Grades 7–10 / Advancing Programmers*  
> *Time Allowed: 60 minutes | Total Marks: 50*

---

## 🎯 Purpose of This Assessment
This assessment evaluates your ability to structure code into modular, reusable functions, manage data using Python's core collections (lists, tuples, dictionaries), and apply randomness and standard libraries.

---

## Part A: Multiple Choice (10 Marks)
*Choose the single best answer for each question (2 marks each).*

**1. What happens when a function finishes executing without an explicit `return` statement?**  
a) It raises a `ReturnError`.  
b) It automatically returns `0`.  
c) It returns `None`.  
d) It re-executes itself from the beginning.

**2. Which statement correctly distinguishes lists from tuples?**  
a) Lists are immutable; Tuples are mutable.  
b) Lists are created with parentheses `()`; Tuples with square brackets `[]`.  
c) Lists can be modified after creation; Tuples cannot be modified after creation.  
d) Lists can only hold numbers; Tuples can only hold text.

**3. What does `word[1:4]` return if `word = "PYTHON"`?**  
a) `"PYT"`  
b) `"YTH"`  
c) `"YTHO"`  
d) `"PYTHON"`

**4. How do you safely retrieve a value from dictionary `d = {"a": 1}` with a fallback if key `"b"` is missing?**  
a) `d["b"]`  
b) `d.fetch("b", 0)`  
c) `d.get("b", 0)`  
d) `d.search("b")`

**5. What is the difference between `random.randint(1, 6)` and `range(1, 6)`?**  
a) `randint` includes 6; `range` stops before 6 (at 5).  
b) `randint` only returns floats; `range` returns integers.  
c) `range` is random; `randint` is sequential.  
d) There is no difference.

---

## Part B: Code Output Tracing (10 Marks)

### Trace 1:
```python
def modify_score(score):
    bonus = 5
    score += bonus
    return score

score = 50
new_score = modify_score(score)
print(f"Original: {score} | Returned: {new_score}")
```
*Write your predicted output here:*

---

### Trace 2:
```python
horses = ["Thunder", "Lightning", "Shadow"]
horses.append("Tornado")
horses.pop(1)
print(horses[1])
```
*Write your predicted output here:*

---

## Part C: Bug Hunting (10 Marks)

### Bug 1:
```python
def compute_area(width, height):
    area = width * height

result = compute_area(5, 4)
print("Area:", result + 10)  # Crashes with TypeError!
```
- **Error Type:** `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`
- **Why it failed:** __________________________________________________
- **Corrected Code:** __________________________________________________

### Bug 2:
```python
racer = ("Lightning", 88)
racer[1] = 95  # Crashes with TypeError!
```
- **Error Type:** `TypeError: 'tuple' object does not support item assignment`
- **Why it failed:** __________________________________________________
- **Corrected Code:** __________________________________________________

---

## Part D: Live Programming Challenge (15 Marks)
**Task: Classroom Lucky Draw Lottery Simulator**  
Write a modular Python script `lucky_draw.py` that:
1. Defines a function `draw_winners(participants_list, winner_count)` that takes a list of student names and returns a list of randomly chosen winners without duplicates (Hint: `random.sample` or copying & `.pop()`).
2. Defines a function `award_prizes(winners_list)` that pairs each winner with a randomly selected prize from a prizes tuple: `("Coding Stickers", "10 Classroom Credits", "Micro:bit Starter Kit")`.
3. Demonstrates the system with a test class list of at least 6 students.
4. Prints an attractive winner announcement banner.

---

## Part E: Code Explanation / Viva Voce (5 Marks)
*Answer in 2 to 3 complete sentences:*

> *"Why is local variable scope important in software engineering? What disaster might occur in a large 5,000-line program if every variable created inside every function were automatically global?"*
