# Phone-Only Quick Start (Android)

> **Kilele Code Studio · 2026**  
> *A single, short path for learners who have only an Android phone.*

This is the shortest route through the curriculum when you have **no laptop and no shared computer**. Use one app: **Pydroid 3**. It is free, works offline, and runs all the standard Python 3 code in this pack. If you later want to learn terminal commands, the Termux section at the end is optional.

---

## 1. Install (once)

1. Open the **Google Play Store**.
2. Search for **Pydroid 3 - Python IDE** and install it.
3. Open the app. You will see a code editor with a Run button at the bottom.

No account is needed, and it works without internet after installing.

---

## 2. Write and run your first program

1. In the editor, type:
   ```python
   print("Hello, Kilele!")
   ```
2. Tap the **Run** button (the play icon at the bottom).
3. You should see `Hello, Kilele!` printed on the screen.

That's the same result as running `python3 first-script.py` on a laptop.

---

## 3. Handle input() exercises

Many exercises (for example the number guessing game) ask the user a question.

1. Run the program.
2. A text box appears near the output area.
3. Type your answer there and confirm/submit.

If the app uses a terminal view instead, tap inside that area and type your answer, then press Enter.

---

## 4. Save and organise your work

1. Tap **Save As** and create one folder, for example `Download/Kilele`.
2. Save each exercise with a clear name: `variables.py`, `loops.py`, `calculator.py`.
3. **Keep every file a program needs in that same folder.** This matters for Module 10, where you import your own helper module — imports only work when the files sit together.
4. To reopen a file, tap the **folder icon** in the app and browse to `Download/Kilele`.

---

## 5. File handling exercises (Module 12)

Pydroid 3 can read and write real files, but use **simple filenames**, not long paths:

```python
with open("students.txt", "w") as file:
    file.write("Amina, 87\n")

with open("students.txt", "r") as file:
    print(file.read())
```

Using `"students.txt"` (a plain name) works in the app's working folder and matches the code in the guides. Long Android paths such as `/storage/emulated/0/Download/...` are more fragile, so avoid them while learning.

---

## 6. Submitting work

- Attach the saved `.py` file from your phone using email, WhatsApp, or cloud storage.
- If your teacher uses Replit, you can instead paste the same code into a Repl on any browser. The code does not change.

---

## 7. Optional: learn the terminal with Termux

Do this only when the basics feel comfortable, or if a lesson asks you to use commands like `cd`, `ls`, or `git clone`.

1. Install **Termux** from **F-Droid** (`https://f-droid.org`). ⚠️ The old Google Play version is outdated — do not use it.
2. Open Termux and type:
   ```bash
   pkg update && pkg upgrade
   pkg install python nano git
   python --version
   ```
3. Create and run a script:
   ```bash
   nano hello.py
   ```
   Type `print("Hello, Kilele!")`, press **Ctrl+O**, **Enter**, **Ctrl+X**, then run:
   ```bash
   python hello.py
   ```
4. To reach files in your Downloads folder, run `termux-setup-storage` once, then use `~/storage/downloads/` as the path.

Termux is a real Linux environment, so **every** command in the setup guides works there, including cloning this repository and running multi-file projects.

---

## 8. Tips for long practice sessions

- A Bluetooth keyboard makes typing much faster; a phone stand avoids holding the device.
- Charge your phone before a long session; coding with the screen on uses battery quickly.
- Test `input()` with a 3-line program before starting a long exercise.
- Back up your `Kilele` folder to cloud storage at the end of each session.
- If storage is tight, skip the apps and use **Replit** in your phone's browser instead — the code is identical.

---

## ➡️ Ready?

Open [`../01-getting-started/`](../01-getting-started/README.md) and start with `first-python-program.py`. Nothing in the code needs to change for a phone setup.

For all other options (browser IDEs, notebooks, Codespaces), see [`no-laptop-setups.md`](./no-laptop-setups.md).
