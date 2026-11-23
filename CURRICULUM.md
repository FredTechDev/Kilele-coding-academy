# Kilele Python Learning Pack — Curriculum Framework

> **Kilele Code Studio · 2026**  
> *Syllabus and Modular Learning Progression for Python Programming (Grades 7–10 / Beginners)*

---

## 🎯 Curriculum Philosophy

The Kilele Python curriculum bridges the gap between abstract computer science concepts and tangible software creation. Each module builds logically upon preceding concepts, avoiding cognitive overload while introducing authentic software engineering practices.

### Core Progression Milestones
1. **Foundation (Modules 1–4):** From hardware awareness and basic syntax to variables, types, and terminal interaction.
2. **Logic & Flow (Modules 5–7):** Computational reasoning with operators, conditions, and iteration loops.
3. **Modularity & Data (Modules 8–10):** Functional decomposition, data structures, and standard libraries.
4. **Resilience & Storage (Modules 11–13):** Exception handling, persistent file I/O, and introductory object modeling.
5. **Applied Engineering (Module 14 & Capstones):** Architecture, validation, testing, and independent project delivery.

---

## 📚 Detailed Module Breakdown

### Module 01: Introduction to Programming
- **Focus:** Understanding computers, execution, and software roles.
- **Topics:**
  - What is programming and what does a software developer do?
  - Low-level machine execution vs. high-level interpreted languages.
  - Why Python? Readable syntax, widespread adoption, versatility.
  - Setting up the local environment: Installing Python 3 and Visual Studio Code.
  - The terminal interface: Basic commands (`ls`/`dir`, `cd`, `python3`).
- **Learning Outcome:** Explain the execution path of a Python script and comfortably navigate the developer terminal.
- **Folder Reference:** `00-orientation/`

---

### Module 02: Python Fundamentals
- **Focus:** Core syntax rules, comments, and program layout.
- **Topics:**
  - Python statements and line-by-line interpretation.
  - The `print()` function: displaying text, numbers, and multiple arguments.
  - Code readability: single-line comments (`#`) and docstrings.
  - The significance of indentation in Python (whitespace as syntax).
  - Variable declaration and assignment basics.
  - PEP 8 naming conventions: `snake_case` for variables and descriptive identifiers.
  - Constants as an engineering convention (uppercase identifiers like `MAX_LIMIT`).
- **Learning Outcome:** Write valid, clean Python instructions with clear comments and compliant formatting.
- **Folder Reference:** `01-getting-started/` & `02-core-concepts/variables.py`

---

### Module 03: Variables and Data Types
- **Focus:** Working with information stored in computer memory.
- **Topics:**
  - Primitive types: String (`str`), Integer (`int`), Float (`float`), Boolean (`bool`).
  - Checking types with `type()`.
  - Type conversion (casting): `int()`, `float()`, `str()`, `bool()`.
  - Common casting pitfalls (e.g. converting non-numeric text to `int`).
  - Primitive immutability and memory updates.
  - Data validation basics: checking whether input is numeric before conversion.
- **Learning Outcome:** Select appropriate data types, prevent type mismatch bugs, and cast values predictably.
- **Folder Reference:** `02-core-concepts/data-types.py`, `type-conversion.py`

---

### Module 04: Input and Output (I/O)
- **Focus:** Building interactive programs that communicate with humans.
- **Topics:**
  - The `input()` function and the default string return type.
  - Crafting user-friendly prompt instructions.
  - Cleaning input: `.strip()`, `.lower()`, `.upper()`.
  - Output formatting techniques: comma separation, concatenation, and f-strings (`f"Hello, {name}"`).
  - Creating multi-line interactive menus and banners.
- **Learning Outcome:** Build interactive terminal programs that collect, sanitize, and format user input.
- **Folder Reference:** `02-core-concepts/user-input.py`, `04-mini-projects/personal-introduction.py`

---

### Module 05: Operators and Expressions
- **Focus:** Performing arithmetic calculations and logical evaluations.
- **Topics:**
  - Arithmetic operators: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponent).
  - Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`.
  - Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.
  - Logical operators: `and`, `or`, `not`.
  - Operator precedence (BODMAS / PEMDAS) and using parentheses for explicit evaluation.
- **Learning Outcome:** Construct mathematical formulas and logical evaluation statements in Python.
- **Folder Reference:** `02-core-concepts/operators.py`, `04-mini-projects/smart-calculator.py`

---

### Module 06: Conditional Statements
- **Focus:** Branching logic and computational decision making.
- **Topics:**
  - The structure of `if` statements.
  - Mutual exclusion with `if` - `else`.
  - Multi-way branching with `if` - `elif` - `else`.
  - Nested conditionals vs. combined conditions using boolean operators (`and`/`or`).
  - Edge cases, boundary testing (e.g. checking age limits, thresholds).
- **Learning Outcome:** Write programs that evaluate dynamic states and execute distinct paths accordingly.
- **Folder Reference:** `02-core-concepts/conditionals.py`, `04-mini-projects/age-eligibility-checker.py`

---

### Module 07: Loops and Iteration
- **Focus:** Automating repetitive tasks and controlling loops.
- **Topics:**
  - Definite iteration with `for` loops and `range(start, stop, step)`.
  - Indefinite iteration with `while` loops based on state conditions.
  - Accumulator variables (e.g. running totals, counters).
  - Loop interruption: `break` to exit and `continue` to skip an iteration.
  - Guarding against accidental infinite loops.
  - Nested loops: generating grids, tables, and multi-step cycles.
- **Learning Outcome:** Automate repetitive calculations and construct robust game/menu loops.
- **Folder Reference:** `02-core-concepts/for-loops.py`, `while-loops.py`, `04-mini-projects/multiplication-trainer.py`

---

### Module 08: Functions and Modularity
- **Focus:** Code reusability, scoping rules, and functional decomposition.
- **Topics:**
  - Function definition (`def`) and function invocation.
  - Positional parameters vs. arguments.
  - Return values (`return`) vs. console output (`print()`).
  - Default parameter values.
  - Variable scope: understanding local vs. global variables.
  - Designing pure functions that take inputs and yield outputs without side effects.
  - Decomposition: breaking complex procedures into compact, single-responsibility functions.
- **Learning Outcome:** Organize code into reusable, modular functions with clean parameters and return values.
- **Folder Reference:** `02-core-concepts/functions.py`, `04-mini-projects/student-performance-checker.py`

---

### Module 09: Strings and Collections
- **Focus:** Managing structured groups of data.
- **Topics:**
  - String manipulation: indexing `[0]`, slicing `[start:stop:step]`, and methods (`.split()`, `.join()`, `.replace()`).
  - Lists (`list`): zero-indexed ordered sequences, indexing, `.append()`, `.pop()`, `.insert()`, `.remove()`.
  - Tuples (`tuple`): immutable sequences and unpacking.
  - Dictionaries (`dict`): key-value pairs, accessing keys, `.get()`, updating values, iterating items.
  - Sets (`set`): unique elements, duplicate elimination, union (`|`), intersection (`&`), difference (`-`).
  - Searching, filtering, and transforming elements in a collection.
- **Learning Outcome:** Store, retrieve, update, and iterate over collections of data effectively.
- **Folder Reference:** `02-core-concepts/strings.py`, `lists.py`, `tuples.py`, `dictionaries.py`, `sets.py`

---

### Module 10: Modules and Randomisation
- **Focus:** Utilizing Python's rich standard library.
- **Topics:**
  - The `import` statement and namespace awareness.
  - The `random` module: `random.randint()`, `random.choice()`, `random.shuffle()`.
  - The `time` module: pauses with `time.sleep()`, elapsed timing.
  - The `math` module: ceiling, floor, square roots, and constants.
  - Creating and importing custom local helper modules.
- **Learning Outcome:** Incorporate standard libraries to build dynamic, randomized simulations and games.
- **Folder Reference:** `02-core-concepts/random-module.py`, `04-mini-projects/number-guessing-game.py`

---

### Module 11: Error Handling and Debugging
- **Focus:** Building crash-resistant software and diagnosing bugs.
- **Topics:**
  - Three categories of errors: Syntax, Runtime, and Semantic/Logical.
  - Reading tracebacks and error messages without fear.
  - Defensive coding with `try` and `except` blocks.
  - Catching specific exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`).
  - Using `else` and `finally` blocks appropriately.
  - Input validation loops: prompting until valid data is entered.
- **Learning Outcome:** Write resilient code that gracefully handles unexpected user inputs and runtime faults.
- **Folder Reference:** `02-core-concepts/error-handling.py`

---

### Module 12: File Handling and Persistence
- **Focus:** Saving and retrieving application data on disk.
- **Topics:**
  - Volatile memory (RAM) vs. non-volatile storage (disk files).
  - Opening files in read (`"r"`), write (`"w"`), and append (`"a"`) modes.
  - The `with open(...) as f:` context manager for safe file lifecycle management.
  - Reading text lines with `.readline()` and `.readlines()`.
  - Storing structured data using basic line formats and JSON (`import json`).
- **Learning Outcome:** Persist application state, user preferences, and records across program executions.
- **Folder Reference:** `02-core-concepts/file-handling.py`, `04-mini-projects/student-record-manager.py`

---

### Module 13: Introduction to Object-Oriented Programming (OOP)
- **Focus:** Modeling entities with states and behaviors.
- **Topics:**
  - What are objects and why use them?
  - Defining classes with the `class` keyword.
  - The initializer method: `__init__()`.
  - Instance attributes vs. class attributes.
  - The purpose of `self`.
  - Defining instance methods and behavior.
  - Instantiating and managing multiple objects.
- **Learning Outcome:** Model real-world entities into Python classes containing state and behaviors.
- **Folder Reference:** `02-core-concepts/introduction-to-classes.py`

---

### Module 14: Project Development and Software Engineering
- **Focus:** End-to-end software creation process.
- **Topics:**
  - Understanding product requirements and user stories.
  - Problem decomposition: pseudocode and flowcharts.
  - Designing clean terminal user interfaces (TUI).
  - Iterative testing, manual edge-case testing, and unit testing concepts.
  - Refactoring: improving code structure without altering behavior.
  - Documenting projects: writing READMEs and user guides.
- **Learning Outcome:** Take a software idea from requirements through design, coding, testing, and presentation.
- **Folder Reference:** `05-capstone-projects/`

---

## 🗺 Curriculum to Repository Mapping

| Learning Phase | Repository Directory | Key Deliverables |
| :--- | :--- | :--- |
| **Setup & Orientation** | `00-orientation/` | VS Code guide, setup steps, how code executes |
| **Foundations & First Steps** | `01-getting-started/` | First programs, `print()`, basic comments |
| **Syntax & Concepts** | `02-core-concepts/` | 17 comprehensive concept scripts + guides |
| **Drills & Homework** | `03-practical-exercises/` | Beginner, Intermediate, Challenge exercises + solutions |
| **Hands-On Mini-Apps** | `04-mini-projects/` | 8 complete terminal mini-projects |
| **Capstone Applications** | `05-capstone-projects/` | Horse Racing Game, Student Results, School Management |
| **Testing & Milestones** | `06-assessments/` | 4 formal assessment modules and rubrics |
| **Educator Tooling** | `07-teacher-resources/` | Lesson templates, progress tracker, marking guide |
