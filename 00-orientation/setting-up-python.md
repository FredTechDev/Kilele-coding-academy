# Setting Up Python 3

> **Module 00: Orientation** · Lesson 3  
> *Kilele Code Studio · 2026*

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
1. Check whether Python 3 is already installed on your system.
2. Install Python 3.8+ on Windows, macOS, or Linux.
3. Configure your system PATH environment variable properly.
4. Launch the interactive Python REPL and exit it cleanly.

---

## 🔍 1. Verification First: Do You Already Have Python?

Before downloading anything, test whether your computer already has Python 3 installed. Open your system terminal (Command Prompt, PowerShell, or Linux/macOS Terminal) and run:

```bash
python3 --version
```
*(If that doesn't work, try `python --version`)*

### Interpreting the Result:
- **Success:** You see something like `Python 3.10.12` or `Python 3.11.4`. You're ready to go!
- **Legacy Warning:** If you see `Python 2.7.x`, that is an obsolete legacy version. We specifically require **Python 3**.
- **Error:** If you see `"command not found"` or `"not recognized as an internal or external command"`, proceed with the installation steps below.

---

## 💻 2. Operating System Installation Guides

### A. Windows Installation
1. Go to the official website: [python.org/downloads](https://www.python.org/downloads/).
2. Click the yellow button: **Download Python 3.x.x**.
3. Run the downloaded installer `.exe`.
4. ⚠️ **CRITICAL STEP (Do Not Miss!):** At the bottom of the very first setup window, check the box that says:
   ```
   [✔] Add python.exe to PATH
   ```
   *(If you skip this box, your computer terminal will not know where to find Python!)*
5. Click **Install Now**.
6. When finished, close Command Prompt and open a fresh one to test: `python --version`.

---

### B. Linux (Ubuntu / Debian / Mint)
Most modern Linux distributions come with Python 3 pre-installed. If you need to install or update:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

Verify with:
```bash
python3 --version
```

---

### C. macOS Installation
1. Visit [python.org/downloads/macos](https://www.python.org/downloads/macos/) and download the latest universal package installer.
2. Open the `.pkg` file and follow the standard installation wizard.
3. Alternatively, if you use Homebrew:
   ```bash
   brew install python
   ```
4. Verify in the Terminal with:
   ```bash
   python3 --version
   ```

---

## 🧪 3. The Interactive Shell (REPL)

Python includes a real-time playground called the **REPL** (*Read-Eval-Print Loop*). This lets you type Python code one line at a time and see immediate results.

### Launching the REPL:
In your terminal, type:
```bash
python3
```
You will see three arrows appear:
```python
Python 3.10.12 (main, Nov 20 2023)
[GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Now try typing simple commands:
```python
>>> 25 + 75
100
>>> print("Hello from inside the REPL!")
Hello from inside the REPL!
```

### How to Exit the REPL:
To return to your normal computer terminal, type:
```python
>>> exit()
```
*(Or press `Ctrl + D` on Linux/macOS, or `Ctrl + Z` then `Enter` on Windows).*

---

## ⚠️ 4. Common Setup Roadblocks

| Problem | Cause | How to Fix |
| :--- | :--- | :--- |
| `"Python is not recognized as an internal or external command"` | On Windows, the installer was run without checking **"Add Python to PATH"**. | Re-run the installer, choose **Modify**, and make sure the **Add to PATH** box is checked. |
| `python` launches Python 2.7 instead of 3 | Older macOS or Linux computers sometimes have legacy Python 2 mapped to the command `python`. | Always use the command **`python3`** in your terminal instead of `python`. |
| Running `exit` (without parentheses) says `Use exit() or Ctrl-D to exit` | `exit` is a function in Python, so it requires parentheses `()`. | Type **`exit()`** and press enter. |

---

## ✏️ 5. Verification Checklist

Complete this checklist to confirm your environment is ready:
- [ ] Opened terminal / command prompt.
- [ ] Ran `python3 --version` and confirmed a version >= `3.8`.
- [ ] Launched the REPL by typing `python3`.
- [ ] Performed a simple calculation (e.g. `12 * 12`).
- [ ] Successfully exited back to the terminal using `exit()`.

---

## 🏆 6. Extension Challenge

In the REPL (`python3`), test how Python handles text multiplication by typing:
```python
>>> "Kilele! " * 5
```
What did Python output? Can you guess why Python allowed you to multiply a text string by a number?

---

## 📌 Lesson Recap

- You need **Python 3.8 or newer** for this curriculum.
- On Windows, always check **"Add Python to PATH"** during installation.
- On Linux and macOS, invoke Python using **`python3`**.
- The interactive shell (**REPL**) lets you test single lines of Python instantly; exit with **`exit()`**.
