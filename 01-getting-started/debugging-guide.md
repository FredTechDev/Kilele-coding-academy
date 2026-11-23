# The Junior Coder's Debugging Handbook

> **Kilele Code Studio · Error Diagnosis & Problem-Solving**  
> *"Errors are not failures. They are the computer's polite way of showing you where to look!"*

---

## 🔍 1. Anatomy of a Python Traceback

When your program crashes, Python doesn't just shut down; it prints a **Traceback**.  
Beginners often panic when they see red text in their terminal. Here is how to read it calmly:

```text
Traceback (most recent call last):
  File "game.py", line 18, in calculate_score
    total = score + bonus
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### The 3 Secrets to Reading Any Traceback:
1. **Look at the VERY LAST LINE first:**  
   `TypeError: unsupported operand type(s) for +: 'int' and 'str'`  
   *This tells you the exact problem: Python tried to add an integer to a string.*
2. **Look at the line number right above it:**  
   `File "game.py", line 18`  
   *This tells you where Python gave up. Look at line 18 in your editor!*
3. **Trace back upwards if functions were called:**  
   The top lines show which function called which other function.

---

## ⚠️ 2. The "Top 7" Python Beginner Errors & Fixes

### 1. `SyntaxError: invalid syntax` or `SyntaxError: expected ':'`
- **Cause:** You broke a basic grammar rule of Python (e.g., forgot a colon, unclosed quotation mark, or misspelled a keyword).
```python
# ❌ BROKEN:
if score >= 50
    print("Pass")

# ✔ FIXED:
if score >= 50:
    print("Pass")
```

---

### 2. `IndentationError: expected an indented block`
- **Cause:** You promised Python a code block (with an `if`, `for`, `while`, or `def` line), but didn't indent the next line.
```python
# ❌ BROKEN:
for i in range(3):
print(i)

# ✔ FIXED (Indented 4 spaces):
for i in range(3):
    print(i)
```

---

### 3. `NameError: name '...' is not defined`
- **Cause:** You referred to a variable or function that Python has never seen before (often caused by typos or case differences).
```python
# ❌ BROKEN:
user_name = "Faraji"
print(User_name)  # Capital 'U' instead of lowercase!

# ✔ FIXED:
print(user_name)
```

---

### 4. `TypeError: can only concatenate str (not "int") to str`
- **Cause:** You tried to glue a number directly to text using `+`.
```python
# ❌ BROKEN:
age = 14
print("I am " + age + " years old.")

# ✔ FIXED (Use f-strings or commas):
print(f"I am {age} years old.")
# OR: print("I am", age, "years old.")
```

---

### 5. `IndexError: list index out of range`
- **Cause:** You asked for an index position that does not exist in the collection. Remember, Python indexing starts at 0!
```python
# ❌ BROKEN (Length is 3, indexes are 0, 1, 2):
horses = ["Thunder", "Lightning", "Shadow"]
print(horses[3])  # There is no index 3!

# ✔ FIXED:
print(horses[2])  # Prints 'Shadow'
```

---

### 6. `KeyError: '...'`
- **Cause:** You asked a dictionary for a key using square brackets `[]` that isn't inside the dictionary.
```python
# ❌ BROKEN:
student = {"name": "Amina", "grade": 9}
print(student["email"])  # 'email' key doesn't exist!

# ✔ FIXED (Use .get() with a default fallback):
print(student.get("email", "No email provided"))
```

---

### 7. `ValueError: invalid literal for int() with base 10: 'abc'`
- **Cause:** You attempted to cast non-numeric text into an integer.
```python
# ❌ BROKEN:
user_entry = "abc"
number = int(user_entry)

# ✔ FIXED (Validate with .isdigit() or try...except):
if user_entry.isdigit():
    number = int(user_entry)
else:
    print("Please enter digits only!")
```

---

## 🛠 3. Strategic "Print Debugging"

When your program runs without crashing but gives the wrong answer (a **Logical Bug**), become a detective using temporary print statements:

```python
def calculate_discount(price, is_member):
    print(f"[DEBUG]: price={price}, is_member={is_member}")  # Check inputs
    if is_member:
        discount = price * 0.20
    else:
        discount = 0.0
    print(f"[DEBUG]: calculated discount={discount}")        # Check logic
    return price - discount
```
Once your logic is confirmed, simply remove the `[DEBUG]` print lines!

---

## 🐞 4. Using the VS Code Debugger

VS Code includes an interactive visual debugger:
1. Open any Python file.
2. Click just to the left of any line number to set a **Red Dot (Breakpoint)**.
3. Press **F5** (or click `Run > Start Debugging`).
4. The program will pause at your red dot!
5. In the left panel, you can inspect the exact value of every variable in RAM at that split second!
6. Use the **Step Over (F10)** button to execute your program one single line at a time.
