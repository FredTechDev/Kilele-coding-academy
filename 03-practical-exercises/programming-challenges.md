# Level 3 — Programming Challenges

> **Kilele Python Learning Pack · Practical Practice**  
> *Target: Grades 7–10 / Advanced Independent Coders*  
> *Concepts: Multi-Step Algorithms, Data Modeling, Defensive Design*

---

## 🎯 Purpose of These Challenges
Level 3 challenges are independent, multi-step programming tasks. They do not tell you which specific loop or variable to write line-by-line; instead, they define real engineering requirements and expect you to architect the solution.

Plan your code using pseudocode or a flowchart before typing! Check [`solutions/challenge_solutions.py`](./solutions/challenge_solutions.py) when complete.

---

### Challenge 1: The Caesar Cipher Secret Messenger
**Scenario:** Julius Caesar protected his confidential letters by shifting every letter of the alphabet forward by a fixed number of positions (e.g. with a shift of 3, `A` becomes `D`, `B` becomes `E`, `X` becomes `A`).  
**Requirements:**
1. Write a function `encrypt(message, shift_key)` that returns the scrambled text.
2. Write a function `decrypt(ciphertext, shift_key)` that recovers the original text.
3. Preserve spaces and punctuation unchanged.
4. Support both lowercase and uppercase letters cleanly.

---

### Challenge 2: Smart Number Guessing AI (Binary Search)
**Scenario:** In the traditional number guessing game, a human guesses a computer's secret number. In this challenge, flip the roles!  
**Requirements:**
1. The human chooses a secret whole number between 1 and 100 in their mind.
2. The computer program guesses the number using **Binary Search** (guessing the midpoint between its lowest and highest possible bounds).
3. After each guess, the user types:
   - `"h"` if the computer's guess was too high.
   - `"l"` if the computer's guess was too low.
   - `"c"` if the computer guessed correctly!
4. The computer must find any secret number in 7 guesses or fewer!

---

### Challenge 3: School Tuck Shop POS (Point of Sale)
**Scenario:** Build a terminal cash register for the Kilele Academy Tuck Shop.  
**Requirements:**
1. Store an inventory dictionary mapping item codes to product details:
   ```python
   inventory = {
       "A1": {"name": "Granola Bar", "price": 1.50, "stock": 10},
       "B2": {"name": "Fruit Juice", "price": 2.00, "stock": 8},
       "C3": {"name": "Apple",       "price": 0.75, "stock": 15}
   }
   ```
2. Allow a customer to add items to their shopping cart by code.
3. Automatically decrement available stock when an item is added.
4. If an item is out of stock, reject the addition gracefully.
5. Print an itemized receipt with item names, quantities, unit prices, subtotal, 8% tax, and total.

---

### Challenge 4: Morse Code Audio/Text Transmitter
**Scenario:** Morse code represents alphabet characters using dots (`.`) and dashes (`-`).  
**Requirements:**
1. Create a dictionary mapping letters `A-Z` and numbers `0-9` to their Morse representations:
   ```python
   MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', ...}
   ```
2. Write a function `text_to_morse(text)` that converts English sentences into space-separated Morse symbols (with `" / "` separating words).
3. Write a function `morse_to_text(morse_code)` that reverses the process.

---

### Challenge 5: Student Attendance & Perfect Streak Analyzer
**Scenario:** A teacher tracks 5 days of school attendance for 4 students using a matrix (list of lists or dictionary).  
**Requirements:**
1. Data format:
   ```python
   attendance_log = {
       "Amina":  ["P", "P", "P", "P", "P"],   # P = Present
       "Kofi":   ["P", "A", "P", "P", "P"],   # A = Absent
       "Zawadi": ["P", "P", "P", "P", "P"],
       "Juma":   ["A", "P", "P", "A", "P"]
   }
   ```
2. Calculate each student's attendance percentage (`(P_count / total_days) * 100`).
3. Identify students who achieved a **"Perfect 100% Attendance Streak"**.
4. Identify days with the lowest overall attendance.
