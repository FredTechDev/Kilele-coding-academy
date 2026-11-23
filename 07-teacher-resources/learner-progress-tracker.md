# Kilele Code Studio — Learner Progress Tracker

> **Cohort Mastery Matrix & Milestone Checklist (Grades 7–10)**  
> *Kilele Code Studio · 2026*

---

## 🧭 Instructions for Instructors

Use this matrix to track each student's progress through the **14 Curriculum Modules**, **Practice Exercises**, **Mini-Projects**, and **Capstone Deliverables**.

### Mastery Level Legend:
- `[🔴] Beginning`: Introduced to concept; requires significant guidance.
- `[🟡] Developing`: Understands mechanics; can write code with occasional syntax/logic bugs.
- `[🟢] Mastered`: Independently applies concept in new contexts and can debug errors.
- `[🌟] Advanced`: Excels beyond curriculum; assists peers or implements creative extensions.

---

## 📊 Class Roster Mastery Matrix Template

| Student Name | ID | Mod 1-4 (Foundations) | Mod 5-7 (Flow & Loops) | Mod 8-10 (Func & Data) | Mod 11-13 (Resilience/OOP) | Capstone Status | Final Grade |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Zawadi Baraka** | KCS-101 | 🟢 | 🟢 | 🟢 | 🟢 | 🏆 Completed (A) | Distinction |
| **Faraji Mwangi** | KCS-102 | 🟢 | 🟢 | 🟡 | 🟡 | 🛠 In Progress | Pending |
| **Amina Patel**   | KCS-103 | 🟢 | 🟢 | 🟢 | 🟢 | 🏆 Completed (B) | Distinction |
| **Kofi Mensah**   | KCS-104 | 🟢 | 🟡 | 🟡 | 🔴 | ⏳ Planning | Pending |
| *[Student 5]*     | ...     | ... | ... | ... | ... | ... | ... |

---

## 📋 Comprehensive 14-Module Competency Checklist

Use this checklist during 1-on-1 student conferences:

### Foundations (Modules 01–04)
- [ ] Understands top-to-bottom instruction execution and terminal command line.
- [ ] Uses `print()` with strings, numbers, custom separators (`sep`), and endings (`end`).
- [ ] Declares and updates variables using `snake_case` naming conventions.
- [ ] Distinguishes between `str`, `int`, `float`, and `bool`.
- [ ] Converts data types safely (`int()`, `float()`) and sanitizes user input with `.strip()`.

### Logic & Iteration (Modules 05–07)
- [ ] Applies arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`) with correct precedence.
- [ ] Evaluates comparison (`==`, `!=`, `<`, `>`) and compound boolean expressions (`and`, `or`, `not`).
- [ ] Constructs multi-way branching trees using `if - elif - else` ladders.
- [ ] Automates repetition using `for` loops and `range(start, stop, step)`.
- [ ] Uses accumulators to compute totals and averages.
- [ ] Controls `while` loops safely without triggering infinite loops.

### Modularity & Data Structures (Modules 08–10)
- [ ] Defines functions (`def`) with parameters, default arguments, and `return` values.
- [ ] Demonstrates understanding of local variable scope vs global scope.
- [ ] Slices strings `[start:stop:step]` and utilizes core methods (`.split()`, `.join()`).
- [ ] Creates and modifies lists (`.append()`, `.pop()`, `.insert()`, `.remove()`).
- [ ] Explains the immutability of tuples and unpacks values into variables.
- [ ] Maps data using dictionaries (`{key: value}`) and iterates with `.items()`.
- [ ] Generates random numbers and simulates games with `random.randint()` and `random.choice()`.

### Software Engineering & Capstones (Modules 11–14)
- [ ] Protects terminal programs against crashes using `try...except` exception handling.
- [ ] Reads and writes persistent data files using `with open(...)` and JSON.
- [ ] Models real-world entities into classes using `__init__()`, `self`, and methods.
- [ ] Delivers a working Capstone Project (Horse Racing, Student Results, or School Management).
- [ ] Explains and defends program architecture in an oral Viva Voce.

---

## 📈 Formative Intervention Triggers
If a student displays any of these warning signs, provide immediate scaffolding:
- **Trigger A (Persistent TypeErrors):** Student is trying to do math directly on `input()` without casting to `int` or `float`. (Review Module 04).
- **Trigger B (Off-by-One Loop Errors):** Student forgets that `range(1, 10)` stops at `9`. (Review Module 07).
- **Trigger C (Variable Scope Errors):** Student attempts to use a local variable outside its function definition. (Review Module 08).
