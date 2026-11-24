# 00 — Alternative Setups: Learning Python Without a Laptop

> **Kilele Code Studio · 2026**  
> *No laptop? No problem. Every exercise in this learning pack can still be completed.*

---

## 🎯 Purpose

The main setup guides assume a computer with Python and VS Code installed. This guide is for learners who **do not own a laptop** and have no way to get one. All the options below are **free** and run the **same Python 3 code** used throughout the curriculum.

Choose **one** path and stick with it:

| Situation | Best option |
| :--- | :--- |
| You can use any computer with internet (school lab, library, friend's device) | **Replit** (browser) |
| You have an Android phone and a data connection | **Replit** or **Pydroid 3** |
| You have an Android phone but unreliable internet | **Pydroid 3** or **Termux** |
| Your teacher wants to give out lessons as notebooks | **Google Colab** |
| You want the closest experience to VS Code in a browser | **GitHub Codespaces** |

---

## 🌐 Option 1: Replit (Recommended — works on any device)

**What it is:** A free Python editor + runner that lives in your web browser. No installation at all. Works on phones, tablets, old laptops, and shared lab computers.

**How to start:**
1. Open <https://replit.com> and create a free account (email or Google).
2. Click **Create Repl** → choose **Python** → give it a name (e.g. `kilele-exercise-01`) → **Create Repl**.
3. Delete the starter code, paste or type the exercise code from this pack into `main.py`.
4. Click the green **Run** button. Type answers into the **Console** box when the program asks for `input()`.
5. Your work is saved automatically in your account — you can continue on any device.

**Why it works well for this curriculum:**
- Supports **multiple files**, so you can create helper modules (Module 10).
- Supports **real files** on disk, so file handling exercises (Module 12) work correctly.
- The console handles `input()` the same way a local terminal does.
- You can share a read-only link to your Repl with your teacher instead of emailing a file.

**Limitations:** Needs internet. The free account is fine for all exercises here. Long-running programs may pause if you leave the tab idle — just press Run again.

---

## 📱 Option 2: Pydroid 3 (Best free Android app for beginners)

**What it is:** A free Python 3 IDE app for Android with a code editor and a **big Run button**. No typing commands needed.

**How to start:**
1. Install **Pydroid 3** from the Google Play Store.
2. Open the app and type your code into the editor (or tap the folder icon to open a `.py` file from `Downloads`).
3. Tap the **play/Run** button at the bottom. Output appears on the same screen; type input into the console field when prompted.
4. To save work, use **Save As** and keep all your `.py` files in one folder (e.g. `Download/Kilele`).

**Why it works well for this curriculum:**
- Runs standard-library Python, so Modules 01–11 work normally.
- Can keep several files in one folder, so custom module imports (Module 10) work if all files are in that folder.
- Can read and write files in its own working directory, so Module 12 exercises work if you use plain filenames like `students.txt`.
- Works **offline** once installed — ideal if data is expensive or unreliable.

**Limitations:** Android only; no true terminal. For file handling, use simple filenames rather than deep paths. The free version is enough for everything in this pack; the paid version only adds extras you do not need.

---

## 🐧 Option 3: Termux (Most powerful — a real Linux terminal on Android)

**What it is:** A terminal emulator app for Android that gives you a real Linux environment where you can install Python with one command. Best choice if you want to learn the terminal commands used in this pack (`cd`, `ls`, `python file.py`, `git clone`).

**How to start:**
1. Install **Termux** from **F-Droid** (<https://f-droid.org>). ⚠️ Do **not** use the old Google Play version — it is no longer updated.
2. Open Termux and run:
   ```bash
   pkg update && pkg upgrade
   pkg install python nano git
   ```
3. Check it worked:
   ```bash
   python --version
   ```
4. Write a program:
   ```bash
   nano hello.py
   ```
   Type `print("Hello, Kilele!")`, then press **Ctrl+O**, **Enter**, **Ctrl+X**.
5. Run it:
   ```bash
   python hello.py
   ```
6. To open files you downloaded in your phone's `Downloads` folder, run `termux-setup-storage` once, then use `~/storage/downloads/` as the path.

**Why it works well for this curriculum:**
- It is genuine Python 3 on Linux — **every** exercise, including file handling, modules, and `git clone` of this repository, works exactly as written in the guides.
- `pip install` works if you ever need extra packages.
- Pairs well with a Bluetooth keyboard if you have one.

**Limitations:** You must be comfortable typing commands. If plain commands feel intimidating, start with **Pydroid 3** or **Replit** and come back to Termux later. On some Android versions, background battery optimisation can stop long-running scripts — disable it for Termux in Android settings.

---

## 📓 Option 4: Google Colab (Best for teacher-assigned notebooks)

**What it is:** Free Python notebooks in the browser, linked to a Google account. Good when a teacher wants to hand out lessons and collect work.

**How to start:**
1. Go to <https://colab.research.google.com> and sign in.
2. **File → New notebook**.
3. In a cell, type `print("Hello, Kilele!")` and press **Shift+Enter** to run it.
4. For `input()` exercises, type the answer in the box that appears under the cell.

**Caveats for this curriculum:** Colab runs in a cloud folder, not your own files. For **Module 12 (File Handling)** you must first upload files (`from google.colab import files`) or create them inside the notebook before reading them. Multi-file modules (Module 10) also need files uploaded into the notebook's folder. For those modules, prefer **Replit**, **Codespaces**, **Pydroid 3**, or **Termux**.

---

## 💻 Option 5: GitHub Codespaces (Browser VS Code — closest to the original setup)

**What it is:** A full VS Code editor that runs in your browser with a Python terminal, free for a limited number of hours each month.

**How to start:**
1. Create a free GitHub account at <https://github.com>.
2. Open this repository (or fork it) and click **Code → Codespaces → Create codespace on main**.
3. Wait for the browser editor to load.
4. Open a `.py` file, then run it in the terminal panel at the bottom with `python filename.py`.

**Why it works well:** It is the same editor and terminal experience as `using-vscode.md`, and the repository is already cloned for you. Requires a reasonably stable internet connection.

---

## ⚡ Quick Practice Sites (for very short drills only)

<https://www.programiz.com/python-programming/online-compiler>, <https://trinket.io/python>, and <https://www.onlinegdb.com/online_python_compiler> let you paste code and run it instantly with no account. They are handy for checking a single answer from **Modules 02–09**, but most do **not** support multiple files or saved files, so they cannot be used for the file-handling and module exercises.

---

## ✅ Can every exercise be done this way?

| Curriculum part | Replit | Pydroid 3 | Termux | Colab | Quick sites |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Modules 01–09 (single-file code) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Module 10 (custom modules / multiple files) | ✅ | ✅ | ✅ | ⚠️ with upload | ❌ |
| Module 11 (error handling) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Module 12 (file handling) | ✅ | ✅ with plain filenames | ✅ | ⚠️ with upload | ❌ |
| Module 13 (classes) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mini-projects & capstones | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Terminal commands / `git clone` | ⚠️ limited | ❌ | ✅ | ✅ with terminal | ❌ |

✅ works normally · ⚠️ works with extra steps or limits · ❌ not suitable

**Bottom line:** **Replit** is the simplest option that does everything. **Pydroid 3** is the best free phone app. **Termux** is the best choice if you want to learn real terminal commands and work offline.

> 📄 **Short versions:** For a phone-only walkthrough, use [`phone-only-quickstart.md`](./phone-only-quickstart.md). To print for a class, use [`no-laptop-handout.md`](./no-laptop-handout.md).

---

## 📤 Submitting Work Without a Laptop

- **Replit / Codespaces:** share a link to your Repl or Codespace, or download the `.py` file and send it.
- **Pydroid 3 / Termux:** attach the `.py` file directly from your phone (email, WhatsApp, or cloud storage).
- **Colab:** use **File → Download → Download .py** or just share the notebook link.
- Always keep a backup of your work in one cloud place so a lost phone does not mean lost code.

---

## 💡 Practical Tips

- use a **Bluetooth keyboard** and a phone stand if you will type a lot.
- Test a short program first to confirm that `input()` works in your chosen tool before starting a long exercise.
- In file handling exercises, use **short, simple filenames** (`students.txt`) rather than long absolute paths — this behaves the same across phone and browser setups.
- If your phone has limited storage, use the browser options instead of installing apps.
- Pair up: one student with a device can drive while a partner reads the exercise and checks the output — this is still active learning.

---

## ➡️ Next Step

Once your chosen tool runs `print("Hello, Kilele!")` correctly, continue with [`../01-getting-started/`](../01-getting-started/README.md). The code in every later module is written in standard Python 3 and needs no changes for these setups.
