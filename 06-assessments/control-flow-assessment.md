# Milestone Assessment 2 — Control Flow & Iteration

> **Kilele Python Learning Pack · Formal Assessment**  
> *Coverage: Modules 05 to 07 (Operators, Conditionals, For Loops, While Loops)*  
> *Target: Grades 7–10 / Intermediate Programmers*  
> *Time Allowed: 50 minutes | Total Marks: 50*

---

## 🎯 Purpose of This Assessment
This assessment evaluates your ability to implement computational branching (`if`/`elif`/`else`), arithmetic & boolean operations, loop iteration (`for`/`while`), accumulators, and loop control (`break`/`continue`).

---

## Part A: Multiple Choice (10 Marks)
*Choose the single best answer for each question (2 marks each).*

**1. What is the value of `19 // 4` in Python?**  
a) `4.75`  
b) `4`  
c) `3`  
d) `16`

**2. What is the result of the boolean expression: `(True and False) or (not False)`?**  
a) `True`  
b) `False`  
c) `SyntaxError`  
d) `None`

**3. How many times will this loop execute: `for i in range(2, 10, 3):`?**  
a) 8 times  
b) 4 times (numbers: 2, 5, 8)  
c) 3 times (numbers: 2, 5, 8)  
d) Infinite times

**4. What does the `continue` keyword do when encountered inside a loop?**  
a) Terminates the entire program immediately.  
b) Exits the loop and moves to the line below the loop.  
c) Skips the rest of the current iteration and jumps to the next cycle.  
d) Resets all loop variables to zero.

**5. What is the primary cause of an accidental infinite `while` loop?**  
a) The loop condition never changes to `False` inside the loop body.  
b) Using `int` instead of `float`.  
c) Having more than 10 lines of code inside the loop.  
d) Using capital letters in variable names.

---

## Part B: Code Output Tracing (10 Marks)

### Trace 1:
```python
total = 0
for n in range(1, 6):
    if n % 2 == 0:
        total += n
print("Even Sum:", total)
```
*Write your predicted output here:*

---

### Trace 2:
```python
count = 10
while count > 0:
    count -= 3
    if count == 4:
        break
print("Final Count:", count)
```
*Write your predicted output here:*

---

## Part C: Bug Hunting (10 Marks)

### Bug 1:
```python
temperature = 28
if temperature > 30
    print("Hot day!")
else
    print("Pleasant day.")
```
- **Error Type:** `SyntaxError`
- **What is missing:** __________________________________________________
- **Corrected Code:** __________________________________________________

### Bug 2:
```python
# Intended: Print numbers 1 through 5
i = 1
while i <= 5:
    print(i)
```
- **Error Type:** Infinite Loop Logic Bug
- **Why it failed:** __________________________________________________
- **Corrected Code:** __________________________________________________

---

## Part D: Live Programming Challenge (15 Marks)
**Task: The Student Grade Bagger & Average Analyzer**  
Write a script `grade_analyzer.py` that:
1. Asks the teacher how many student test scores they wish to enter.
2. Uses a `for` loop to collect each score.
3. Uses an accumulator variable to calculate the class average.
4. Uses conditionals to count:
   - How many students earned an **A** (80 or above).
   - How many students passed (50 to 79).
   - How many students failed (below 50).
5. Displays a neat summary report showing class average, highest score, and counts per grade bracket.

---

## Part E: Code Explanation / Viva Voce (5 Marks)
*Answer in 2 to 3 complete sentences:*

> *"Why is an `if - elif - else` ladder preferred over writing five separate independent `if` statements when evaluating a single student's letter grade? What difference does this make to how Python executes the program?"*
