"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: file-handling.py
Description: Reading, writing, appending files, and saving data with JSON
=============================================================================

Learning Objectives:
1. Understand file persistence: volatile RAM vs non-volatile disk storage.
2. Master file modes: "w" (write), "a" (append), "r" (read).
3. Use the safe 'with open(...) as f:' context manager.
4. Read files line-by-line using loops and .strip().
5. Save and reload structured data using the built-in json module.
"""

import os
import json

print("==================================================")
print("           LESSON 16: FILE HANDLING               ")
print("==================================================")

demo_file = "high_scores_demo.txt"
json_demo_file = "game_save_demo.json"

# ==========================================
# 1. WRITING TO A FILE ("w" mode)
# ==========================================
# "w" creates a new file, or completely OVERWRITES an existing file!
print("\n--- 1. Writing to a Text File ('w') ---")
with open(demo_file, "w") as file:
    file.write("Player: Amani | Score: 950\n")
    file.write("Player: Baraka | Score: 880\n")
print(f"Created '{demo_file}' and wrote 2 initial records.")


# ==========================================
# 2. APPENDING TO A FILE ("a" mode)
# ==========================================
# "a" adds new content to the END of the file without erasing existing data:
print("\n--- 2. Appending to a File ('a') ---")
with open(demo_file, "a") as file:
    file.write("Player: Zawadi | Score: 1020\n")
print(f"Appended a new high score to '{demo_file}'.")


# ==========================================
# 3. READING FROM A FILE ("r" mode)
# ==========================================
print("\n--- 3. Reading File Line-by-Line ---")
if os.path.exists(demo_file):
    with open(demo_file, "r") as file:
        line_num = 1
        for line in file:
            print(f"  Line {line_num}: {line.strip()}")
            line_num += 1


# ==========================================
# 4. STRUCTURED DATA PERSISTENCE WITH JSON
# ==========================================
# JSON (JavaScript Object Notation) is the universal format for saving dictionaries and lists:
print("\n--- 4. Saving and Loading with JSON ---")
player_save_state = {
    "username": "CodeNinja2026",
    "level": 5,
    "credits": 250,
    "inventory": ["Speed Boots", "Lucky Horseshoe", "Shield"]
}

# Saving to disk:
with open(json_demo_file, "w") as jf:
    json.dump(player_save_state, jf, indent=4)
print(f"Saved game state to '{json_demo_file}'.")

# Loading from disk:
with open(json_demo_file, "r") as jf:
    loaded_data = json.load(jf)

print("Loaded Player Data:", loaded_data["username"])
print(f"Credits: {loaded_data['credits']} | Items: {len(loaded_data['inventory'])}")


# ==========================================
# 5. CLEANUP DEMO FILES
# ==========================================
# In a demo script, we clean up the temporary files so our workspace stays pristine:
for f in [demo_file, json_demo_file]:
    if os.path.exists(f):
        os.remove(f)
print("\nCleaned up temporary demonstration files successfully.")
