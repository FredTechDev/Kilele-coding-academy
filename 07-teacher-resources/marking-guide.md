# Kilele Code Studio — Assessment Marking Guide & Answer Keys

> **Standardized Evaluation Criteria & Solutions for Instructors**  
> *Kilele Code Studio · 2026*

---

## 🧭 Evaluation Standards

When evaluating student submissions, balance **functional correctness** with **clean coding habits**. A program that works but uses cryptic single-letter variable names and no comments should not receive full marks.

### 4-Tier Assessment Rubric:

| Rating | Criterion | Marks % |
| :--- | :--- | :---: |
| **Exemplary (4)** | Code is completely functional, handles edge cases, adheres to PEP 8, uses meaningful names and comments, and the learner can explain every line. | 90–100% |
| **Proficient (3)** | Code meets all core functional requirements; minor style inconsistencies or unhandled edge cases; learner can explain general flow. | 75–89% |
| **Developing (2)** | Code runs partially or with occasional runtime errors; logic requires revision; learner needs prompting to explain decisions. | 50–74% |
| **Beginning (1)** | Code does not compile or run; fundamental misconceptions of syntax or logic; heavy scaffolding needed. | Below 50% |

---

## 🔑 Milestone Assessment 1: Answer Key (Fundamentals)

### Part A: Multiple Choice (10 Marks)
1. **b** (RAM is temporary working memory; Storage is persistent long-term disk).
2. **c** (`student_score` adheres to PEP 8 snake_case; `2nd_place_score` starts with a number; `student-score` has hyphens; `class` is a reserved keyword).
3. **c** (`<class 'str'>` because `"42.0"` is enclosed in quotes).
4. **b** (`HiHiHi` because string multiplication repeats the text).
5. **b** (`String ('str')` — `input()` always returns text).

### Part B: Output Tracing (10 Marks)
- **Trace 1:**
  ```text
  x: 15 y: 12
  ```
  *(Explanation: `x` becomes 10 + 5 = 15; `y` becomes 15 - 3 = 12).*
- **Trace 2:**
  ```text
  Kilele 2026
  ```
  *(Explanation: Text concatenation with a space and string-cast 26).*

### Part C: Bug Hunting (10 Marks)
- **Bug 1:** Cannot subtract string from int (`TypeError`).  
  *Fix:* `years_to_eighteen = 18 - int(user_age)`
- **Bug 2:** Missing comma between print arguments (`SyntaxError`).  
  *Fix:* `print("Welcome to Python, ", student_name)` or `print(f"Welcome to Python, {student_name}")`

### Part D: Live Challenge Model Solution (15 Marks)
```python
name = input("Enter buyer name: ").strip().title()
tickets = int(input("Enter number of tickets: "))
price = float(input("Enter price per ticket: "))

subtotal = tickets * price
levy = subtotal * 0.10
total = subtotal + levy

print("\n" + "=" * 40)
print(f"Buyer:            {name}")
print(f"Tickets:          {tickets} @ ${price:.2f}")
print(f"Subtotal:         ${subtotal:.2f}")
print(f"School Levy (10%): ${levy:.2f}")
print("-" * 40)
print(f"Total Amount Due: ${total:.2f}")
print("=" * 40)
```

### Part E: Viva Voce (5 Marks)
- *Expected response:* Text `"twenty"` contains alphabetical letters, which have no mathematical numeric value for base-10 calculation. `"20"` contains ASCII digits `2` and `0`, which the computer can convert into binary representation in RAM.

---

## 🔑 Milestone Assessment 2: Answer Key (Control Flow)

### Part A: Multiple Choice (10 Marks)
1. **b** (`4` — Floor division discards the fractional decimal).
2. **a** (`True` — `not False` is `True`, so `False or True` evaluates to `True`).
3. **c** (`3 times` — Generates 2, 5, 8; stops before 10).
4. **c** (Skips the rest of current cycle and proceeds to the next iteration).
5. **a** (Condition never changes to `False`).

### Part B: Output Tracing (10 Marks)
- **Trace 1:** `Even Sum: 6` (even numbers are 2 and 4; 2 + 4 = 6).
- **Trace 2:** `Final Count: 4` (starts at 10; decrements to 7, then 4; hits `break` when `count == 4`).

### Part C: Bug Hunting (10 Marks)
- **Bug 1:** Missing colons after `if` and `else`.  
  *Fix:* `if temperature > 30:` and `else:`
- **Bug 2:** Missing loop variable increment (`i += 1`), causing an infinite loop.  
  *Fix:* Add `i += 1` inside the loop body.

---

## 🔑 Milestone Assessment 3: Answer Key (Functions & Data)

### Part A: Multiple Choice (10 Marks)
1. **c** (`None` is returned implicitly by Python).
2. **c** (Lists are mutable; tuples are immutable).
3. **b** (`"YTH"` — indexes 1, 2, and 3; index 4 is excluded).
4. **c** (`d.get("b", 0)` returns 0 if key `"b"` is not found).
5. **a** (`random.randint(1, 6)` includes 6; `range(1, 6)` excludes 6).

### Part B: Output Tracing (10 Marks)
- **Trace 1:** `Original: 50 | Returned: 55` (variable inside function is local; original integer is immutable).
- **Trace 2:** `Lightning` (after popping index 1 "Lightning" from original `["Thunder", "Lightning", "Shadow", "Tornado"]`, the list becomes `["Thunder", "Shadow", "Tornado"]`, so index 1 is now `"Shadow"`).
