# Python Practice Without a Laptop - Quick Handout

Kilele Code Studio 2026. This handout is plain text on purpose so it prints clearly in black and white.

Every exercise in the Kilele Python Learning Pack can be completed for free without a laptop. Pick ONE of the two routes below and use it for the whole course.

---

## Route A: Use a browser (Replit)

Works on any device with internet: school lab computer, library computer, tablet, or phone. Nothing to install.

1. Go to https://replit.com and create a free account.
2. Click Create Repl, choose Python, name it (for example kilele-01), click Create Repl.
3. Type the exercise code into the file called main.py.
4. Click the green Run button. If the program asks a question, type your answer in the Console box.
5. Your work saves automatically. To submit, share the Repl link or download main.py.

Replit supports multiple files and text files, so all modules of the course work, including file handling (Module 12) and custom modules (Module 10).

---

## Route B: Use an Android phone (Pydroid 3)

Works offline after installation. Best choice if you have a phone but no reliable internet.

1. Install the free app Pydroid 3 from the Google Play Store.
2. Open the app and type the exercise code in the editor. To reopen saved work, tap the folder icon and open your .py file.
3. Tap the Run button at the bottom. Type answers into the console when the program asks a question.
4. Save your work with Save As in one folder, for example Download/Kilele. Keep all .py files for a project in that same folder.
5. To submit, attach the .py file from your phone by email, messaging app, or cloud storage.

For file handling exercises (Module 12), use short filenames such as students.txt, not long paths.

---

## Optional upgrade: Termux (Android, real terminal)

Only if you want to practise the terminal commands used in the guides.

1. Install Termux from F-Droid at https://f-droid.org (not the old Play Store version).
2. Open Termux and type:

   pkg update && pkg upgrade
   pkg install python nano git

3. Check the install with: python --version
4. Create a file with: nano hello.py
   Type print("Hello, Kilele!"), then press Ctrl+O, Enter, Ctrl+X.
5. Run it with: python hello.py

Termux runs standard Python on Linux, so every exercise and command in the guides works exactly as written.

---

## Quick checklist: what works where

| Exercise type | Replit | Pydroid 3 | Termux |
| --- | --- | --- | --- |
| Basic print, variables, input, loops, functions (Modules 01-09) | Yes | Yes | Yes |
| Custom modules with several files (Module 10) | Yes | Yes | Yes |
| Error handling and classes (Modules 11, 13) | Yes | Yes | Yes |
| File handling with real files (Module 12) | Yes | Yes | Yes |
| Mini-projects and capstones | Yes | Yes | Yes |
| Terminal commands and git clone | Limited | No | Yes |

Quick websites such as Programiz, Trinket, or OnlineGDB are fine for a single short answer from Modules 02-09, but they cannot do file handling or multiple files. Do not use them for projects.

---

## Practical tips

- Use a Bluetooth keyboard and a phone stand if you type a lot.
- Test that input() works with a tiny program before starting a long exercise.
- Keep all files for one program in the same folder so imports work.
- Keep one cloud backup of your work so a lost phone does not mean lost code.
- Pair up if devices are shared: one student types, the other reads the exercise and checks the output.

---

Full instructions, including browser notebook and codespace options, are in no-laptop-setups.md in the same folder.
