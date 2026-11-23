# Kilele Code Studio — Instructor & Teaching Guide

> **Pedagogical Strategy & Classroom Delivery for Grades 7–10 Python Education**  
> *Kilele Code Studio · 2026*

---

## 🎯 1. Instructional Philosophy: "Code With Them, Not At Them"

Teaching text-based programming to middle and early high school students (Grades 7–10) requires a fundamental shift away from static slide presentations toward **active, visible problem solving**.

### The 3 Core Pillars:
1. **Live-Coding Demonstrations:** Open an empty file in VS Code and build code line-by-line while narrating your thought process aloud. When you inevitably make a typing mistake or miss a colon, do not panic—use it as a teachable moment! Let students see how an experienced developer diagnoses and fixes syntax errors.
2. **Predict Before Running (The "Pause & Predict" Habit):** Before running any demonstration script in the terminal, pause and ask the classroom: *"Look at line 14. What will appear on the screen when I press Enter?"* This builds the mental execution model inside their heads.
3. **The 7-Step Active Learning Cycle:** Every lesson must follow:
   ```
   [1. Concept Hook] ──▶ [2. Explanation] ──▶ [3. Live Demo] ──▶ [4. Guided Drill]
                                                                        │
   [7. Reflection]   ◀── [6. Mini-Project] ◀── [5. Independent Task] ◀──┘
   ```

---

## 🌉 2. Bridging from Scratch (Block Coding) to Python

Many students in Grades 7–10 come with prior experience in Scratch or block-based tools. Leverage their visual intuition:

| Scratch Concept | Python Equivalent | Teaching Analogy |
| :--- | :--- | :--- |
| `say [Hello] for 2 secs` | `print("Hello")` | Sending a message to the terminal console |
| `set [score] to (0)` | `score = 0` | Labeling a box in memory and storing a value |
| `ask [Name?] and wait` | `name = input("Name: ")` | Pausing the program until the user presses Enter |
| `if < > then ... else` | `if ... : ... else:` | A fork in the road depending on True or False |
| `repeat (10)` | `for i in range(10):` | Definite loop counting up to 10 |
| `forever` | `while True:` | An indefinite game loop that runs until stopped |

---

## 👥 3. Pair Programming: Driver & Navigator

Pair programming is one of the most effective strategies for preventing lab frustration. Assign students in pairs with defined roles rotated every 20 minutes:

```
  ┌─────────────────────────────┐        ┌─────────────────────────────┐
  │         THE DRIVER          │        │        THE NAVIGATOR        │
  │  - Hands on the keyboard    │  🤝   │  - Reads the instructions   │
  │  - Types the code           │        │  - Watches for typos & bugs │
  │  - Focuses on mechanics     │        │  - Thinks about next steps  │
  └─────────────────────────────┘        └─────────────────────────────┘
```

**Rule:** The Navigator is never allowed to touch the keyboard! They must guide the Driver using verbal instructions.

---

## 🐛 4. The 4-Step Student Debugging Protocol

When students encounter a bug, they instinctively raise their hands and say *"Teacher, it doesn't work!"*  
Teach them the **Kilele Debugging Protocol** before answering:

1. **Step 1: Read the Last Line of the Traceback:** Python almost always tells you the exact problem on the final line (e.g. `NameError: name 'scor' is not defined on line 12`).
2. **Step 2: Check the "Big Three" Syntax Traps:**
   - Did you forget a colon `:` at the end of an `if`, `for`, `while`, or `def` line?
   - Are your parentheses `()` and quotation marks `""` matched in pairs?
   - Is your indentation strictly 4 spaces without mixing tabs?
3. **Step 3: Rubber-Duck to Your Partner:** Explain what the line is supposed to do out loud to your partner or a desktop mascot.
4. **Step 4: Ask 3 Before Me:** Check the lesson notes, check the error message, consult your partner, and only then call the instructor.

---

## ⚡ 5. Differentiating Instruction in Mixed-Ability Labs

In any coding classroom, some students will complete tasks in 10 minutes while others need 40 minutes.

### For Fast Finishers (Extension Challenges):
- Never give them busywork! Direct them to the **Extension Challenges** in the lesson files.
- Challenge them to add colorful terminal ASCII art, sound effects (using terminal bells `\a`), or input defense so their program never crashes if someone enters gibberish.
- Invite them to act as a **"Junior Teaching Assistant"** to mentor a struggling peer.

### For Struggling Learners:
- Provide starter "scaffolding" code where variable structures are already created and they only fill in the logic conditions.
- Have them draw the program flow on paper using arrows and boxes before typing any code.
