# How Programs Work

> **Module 00: Orientation** · Lesson 2  
> *Kilele Code Studio · 2026*

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
1. Explain the roles of the CPU, RAM, and Storage during program execution.
2. Differentiate between human-readable source code and binary machine code.
3. Understand how the Python Interpreter translates instructions so hardware can carry them out.
4. Describe the exact step-by-step lifecycle of running a Python script.

---

## 🖥 1. The Computer's Anatomy

To understand programming, you don't need an engineering degree, but you do need a mental model of four basic computer hardware components:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │                           HARDWARE                              │
  │                                                                 │
  │  ┌──────────────┐     loads into      ┌──────────────────────┐  │
  │  │ Storage      │ ──────────────────▶ │ Memory (RAM)         │  │
  │  │ (SSD / Disk) │                     │ (Short-term storage) │  │
  │  │ Saves files  │                     └──────────┬───────────┘  │
  │  └──────────────┘                                │              │
  │                                                  │ fetches &    │
  │                                                  ▼ executes     │
  │  ┌──────────────┐     displays to     ┌──────────────────────┐  │
  │  │ Screen /     │ ◀────────────────── │ Processor (CPU)      │  │
  │  │ Terminal     │                     │ (The brain)          │  │
  │  └──────────────┘                     └──────────────────────┘  │
  └─────────────────────────────────────────────────────────────────┘
```

1. **Storage (Hard Drive / SSD):** Long-term file storage. When you write a Python file (`script.py`) and click save, it sits securely on your storage drive even when your computer is powered off.
2. **RAM (Random Access Memory):** High-speed temporary workspace. When you run a program, instructions and variables are loaded into RAM so the computer can access them at lightning speed. When the computer shuts down, RAM is wiped clean.
3. **CPU (Central Processing Unit):** The central brain. The CPU performs billions of tiny mathematical and logical calculations every second.
4. **Input & Output (I/O):** Devices you use to send data in (keyboard, mouse) and get information out (monitor screen, terminal output).

---

## 0️⃣ 1️⃣ 2. Source Code vs. Machine Code

The CPU inside your computer is an electronic circuit made up of billions of microscopic transistors acting as microscopic switches. Because of this electrical nature, the CPU does **not** understand English words like `print`, `while`, or `calculate`.

- **Machine Code (Binary):** Strings of electrical signals represented as `0`s (off) and `1`s (on), such as `10110000 01100001`. Extremely difficult and tedious for humans to write directly.
- **Source Code:** High-level human-readable text that you write in a file, such as `print("Welcome to Kilele!")`.

Because humans think in words and ideas, and CPUs calculate in binary, we need an automated translator: **The Interpreter**.

---

## ⚙️ 3. The Python Interpreter

Python is an **interpreted language**. When you type `python3 script.py` into your terminal:

```
  [ Your Script: hello.py ]
              │
              ▼ (Python Interpreter reads text)
     [ Syntax Verification ] ──▶ (Any typos? If yes, report SyntaxError)
              │ (No typos)
              ▼
       [ Bytecode (.pyc) ]    ──▶ (Intermediate instructions optimized for machines)
              │
              ▼
   [ Python Virtual Machine ] ──▶ (Translates bytecode into native CPU operations)
              │
              ▼
      [ CPU Execution ]       ──▶ (Text appears on your terminal screen!)
```

### Steps in the Lifecycle:
1. **Source Code Reading:** Python opens your file and reads it line-by-line.
2. **Parsing & Syntax Check:** It checks whether your code follows Python's grammar rules. If you missed a parenthesis or misformatted indentation, it immediately stops and prints a `SyntaxError`.
3. **Bytecode Compilation:** Python converts your code into an efficient intermediate format called **bytecode**.
4. **Virtual Machine Execution (PVM):** The Python Virtual Machine coordinates with your computer's operating system (Linux, macOS, Windows) and CPU to carry out the actions and print results.

---

## 🧠 4. A Key Truth: Computers Are Not Psychic!

One of the most important lessons every programmer learns is:

> **"Computers do not do what you *wanted* them to do. They do exactly what you *told* them to do."**

If your program gives the wrong answer, it is almost never because the computer made a mistake. It is usually because of a small logical slip in the sequence of instructions given to the computer. Programmers call these slips **bugs**, and the process of finding and fixing them is called **debugging**.

---

## ⚠️ 5. Common Misconceptions

| Misconception | Reality |
| :--- | :--- |
| *"The computer knows what I meant even if I spelled a variable slightly wrong."* | The computer cannot guess intent. If you declare `score = 10` and later ask for `scor`, Python will halt and report `NameError`. |
| *"Variables are permanently saved on my hard drive automatically."* | Variables live in temporary RAM memory. When your program finishes running, those variables disappear unless you deliberately save them to a file. |
| *"Coding requires you to be an absolute genius at complex math."* | Coding is primarily about **logical sequence**, breaking large problems into smaller steps, and clear thinking. |

---

## ✏️ 6. Independent Exercises

1. Which hardware component holds active variables while a program is running? (Storage, RAM, or CPU?)
2. What is the difference between source code and machine code?
3. What is the role of the Python Interpreter when you execute `python3 my_code.py`?
4. If Python encounters a spelling mistake in your code, does it try to guess the right word or does it stop and show an error? Why is this helpful?

---

## 🏆 7. Extension Challenge

Find out what the term **"bug"** in computer programming actually originated from. (Hint: In 1947, computer pioneer Grace Hopper and her team found an actual physical moth trapped in a relay of the Harvard Mark II computer!) Write two sentences explaining how that story gave us the term "debugging".

---

## 📌 Lesson Recap

- **Hardware roles:** Programs are stored on the **disk**, loaded into **RAM**, and executed by the **CPU**.
- **Translation:** The CPU only executes binary machine code (`0`s and `1`s).
- **The Interpreter:** Python transforms your human-readable **source code** into **bytecode**, which is executed step-by-step by the Python Virtual Machine.
- **Literal obedience:** The computer executes your exact commands without guessing your intentions.
