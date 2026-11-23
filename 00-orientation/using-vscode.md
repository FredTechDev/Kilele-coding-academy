# Using Visual Studio Code

> **Module 00: Orientation** · Lesson 4  
> *Kilele Code Studio · 2026*

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
1. Explain why developers use dedicated code editors instead of word processors like Microsoft Word or Notepad.
2. Install and configure Visual Studio Code with the official Python extension.
3. Open a project workspace folder and navigate the file explorer.
4. Launch and use the integrated terminal inside VS Code to run Python scripts.

---

## 🛠 1. Why a Code Editor?

Why can't we just write Python in Microsoft Word or Google Docs?

1. **Word Processors format text for printing:** They insert hidden formatting characters, smart curly quotes (`“ ”` instead of clean straight quotes `""`), and page margins that break computer code.
2. **Code Editors are built for developers:**
   - **Syntax Highlighting:** Colors keywords, numbers, and strings differently so you can read code at a glance.
   - **Auto-Indentation:** Automatically indents 4 spaces when you start a code block.
   - **Error Underlines:** Highlights syntax errors with red squiggles before you even run the script.
   - **Integrated Terminal:** Gives you an active command line right under your code.

**Visual Studio Code (VS Code)** by Microsoft is currently the most popular, free, open-source editor used by professional developers worldwide.

---

## 📥 2. Installing VS Code and the Python Extension

### Step 1: Install the Editor
1. Download VS Code for your operating system from: [code.visualstudio.com](https://code.visualstudio.com/).
2. Run the installer with default recommendations.

### Step 2: Install the Python Extension
1. Open VS Code.
2. Click the **Extensions** icon on the left Activity Bar (looks like 4 building blocks, or press `Ctrl + Shift + X`).
3. Search for: `Python` (developed by **Microsoft**).
4. Click **Install**.

---

## 🗺 3. Anatomy of the VS Code Workspace

```
  ┌───┬──────────────────┬───────────────────────────────────────────┐
  │ 🗂 │ EXPLORER         │  first-python-program.py                  │
  │   │ ▾ kilele-coding  │  ───────────────────────────────────────  │
  │ 🔍│   ▸ 00-orient... │  1  # My first script                     │
  │   │   ▾ 01-gettin... │  2  print("Welcome to Kilele Code!")      │
  │ 🔀│     hello.py     │  3                                        │
  │   │   ▸ 02-core-c... │                                           │
  │ ⚙ │                  │                                           │
  ├───┴──────────────────┴───────────────────────────────────────────┤
  │ TERMINAL                                                         │
  │ $ python3 first-python-program.py                                │
  │ Welcome to Kilele Code!                                          │
  └──────────────────────────────────────────────────────────────────┘
```

1. **Activity Bar (Far Left):** Switch between File Explorer, Search, Git Version Control, and Extensions.
2. **Explorer Sidebar:** Shows the folders and files in your open project.
3. **Editor Pane:** Where you read, write, and edit your Python code.
4. **Integrated Terminal (Bottom):** The built-in command prompt where you execute your programs!

---

## 🚀 4. How to Open and Run Projects Like a Pro

### Rule #1: Always "Open Folder", Not Single Files!
In VS Code, always select:
```
File ──▶ Open Folder... ──▶ Choose the 'kilele-coding' folder
```
Opening the whole folder ensures that VS Code recognizes your directory structure, finds relative files, and sets the terminal path correctly.

### Opening the Integrated Terminal:
Press the keyboard shortcut:
- **`Ctrl + ` `** (Control + Backtick, the key just below Escape and above Tab).
- Or click the top menu: `Terminal` ──▶ `New Terminal`.

### Running Your Code:
Inside the integrated terminal at the bottom, type:
```bash
python3 01-getting-started/first-python-program.py
```
And press **Enter**!

---

## ⚠️ 5. Common Pitfalls in VS Code

| Pitfall | Symptoms | Fix |
| :--- | :--- | :--- |
| **Unsaved Changes** | Code runs your old instructions instead of your new edits. (Look for a solid white dot `●` on the file tab). | Always press **`Ctrl + S`** (`Cmd + S` on Mac) before running! You can also enable `File ──▶ Auto Save`. |
| **Wrong Terminal Directory** | Terminal displays `No such file or directory` when trying to run a script. | Check what folder your terminal is in by typing `pwd` (Linux/Mac) or `cd` (Windows). Ensure you are in the project folder. |
| **Wrong Python Interpreter** | Yellow warning in bottom-right saying `Select Interpreter`. | Click the warning, or press `Ctrl + Shift + P`, type `Python: Select Interpreter`, and choose your installed Python 3. |

---

## ✏️ 6. First Flight Exercise

Test your setup right now:
1. Open the `kilele-coding` folder in VS Code.
2. Open the integrated terminal (`Ctrl + ` `).
3. Type `python3 --version` in the terminal and hit Enter.
4. Verify that the output shows your installed Python 3 version without errors.

---

## 🏆 7. Extension Challenge: Handy Keyboard Shortcuts

Commit these three power shortcuts to memory:
- **`Ctrl + S` (`Cmd + S` on Mac):** Save file.
- **`Ctrl + ` ` (`Cmd + ` ` on Mac):** Toggle integrated terminal open / closed.
- **`Ctrl + /` (`Cmd + /` on Mac):** Instantly comment or uncomment selected lines of code with `#`.

---

## 📌 Lesson Recap

- **Code editors** provide syntax highlighting, auto-indentation, and integrated tools.
- In VS Code, always use **File ──▶ Open Folder** to work with an organized project.
- You write code in the **Editor Pane** and run it in the **Integrated Terminal**.
- Remember to **Save (`Ctrl + S`)** your files before executing them!
