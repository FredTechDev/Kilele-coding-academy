# Practical Lab 01 — Your First Steps in Code

> **Module 01: Getting Started** · Hands-On Lab  
> *Kilele Code Studio · 2026*

---

## 🎯 Lab Objectives

In this hands-on lab, you will:
1. Run and modify real Python programs in your terminal.
2. Experiment with console output using `print()`.
3. Add explanatory comments to your code.
4. Practice identifying and fixing syntax errors.

---

## 🧪 Activity 1: Running the Starter Files

Open your terminal in VS Code and ensure you are in the project folder. Run both lesson scripts:

```bash
python3 01-getting-started/first-python-program.py
python3 01-getting-started/print-and-comments.py
```

### Observation Check:
- Notice how strings enclosed in double quotes `"..."` appear as readable text.
- Notice how numbers without quotes can be added, subtracted, and multiplied directly inside `print()`.
- Notice how lines starting with `#` produce no output in the terminal.

---

## 🛠 Activity 2: Modify the Code

Open [`first-python-program.py`](./first-python-program.py) in your editor:
1. Change the name in the welcome message to your own name.
2. Add two new `print()` statements listing:
   - Your favorite hobby.
   - Why you want to learn programming.
3. Save the file (`Ctrl + S`) and run it again in the terminal:
   ```bash
   python3 01-getting-started/first-python-program.py
   ```

---

## 🔍 Activity 3: The "Spot the Bug" Challenge

Below are three broken lines of Python. Study each line, identify why Python rejects it, and write down the corrected line:

### Bug #1:
```python
print("Hello World)
```
*Why it fails:* Mismatched quotes (the closing quotation mark is missing).  
*Correct fix:* `print("Hello World")`

### Bug #2:
```python
Print("Welcome to Kilele!")
```
*Why it fails:* Python is case-sensitive! `Print` with a capital `P` is not recognized.  
*Correct fix:* `print("Welcome to Kilele!")`

### Bug #3:
```python
print("My age is" 14)
```
*Why it fails:* When printing multiple items, you must separate them with a comma `,`.  
*Correct fix:* `print("My age is", 14)`

---

## ✏️ Activity 4: Independent Lab Tasks

Create a new file in your personal folder or scratchpad named `my_intro.py` and write a program that prints:
1. A decorative banner of asterisks: `****************************************`
2. Your name and grade level.
3. Three skills you hope to develop in this course.
4. A countdown line using `end=" "`: `3... 2... 1... Let's Code!`

---

## 📌 Lab Check-In

Before moving to `02-core-concepts/`, ensure you can answer:
- [ ] What function displays output to the screen? (`print()`)
- [ ] What symbol denotes a comment? (`#`)
- [ ] What escape code inserts a new line? (`\n`)
- [ ] Can Python perform math like `25 * 4` directly inside `print()`? (Yes!)
