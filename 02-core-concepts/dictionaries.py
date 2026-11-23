"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: dictionaries.py
Description: Key-Value data mapping, lookups, updates, and dictionary methods
=============================================================================

Learning Objectives:
1. Understand dictionaries as Key-Value data structures.
2. Access values using square bracket notation and safe .get() method.
3. Add, update, and delete key-value pairs.
4. Iterate over keys, values, and .items().
5. Avoid KeyError crashes.
"""

print("==================================================")
print("          LESSON 13: DICTIONARIES                 ")
print("==================================================")

# ==========================================
# 1. WHAT IS A DICTIONARY?
# ==========================================
# A dictionary maps unique KEYS to VALUES.
# Defined using curly braces {key: value}.
# Think of an English dictionary: you search a "word" (key) to find its "definition" (value).

student = {
    "id": "KCS-101",
    "name": "Zawadi",
    "grade": 9,
    "courses": ["Python", "Robotics", "Algebra"],
    "is_active": True
}

print("\n--- 1. Dictionary Structure ---")
print("Student Dictionary:", student)
print("Student Name:      ", student["name"])
print("Enrolled Grade:    ", student["grade"])


# ==========================================
# 2. SAFE RETRIEVAL WITH .get()
# ==========================================
# If you look up a key that doesn't exist with [], Python raises a KeyError crash!
# .get() safely returns None (or a fallback default value) if the key is missing:

print("\n--- 2. Safe Retrieval with .get() ---")
# print(student["email"])  --> KeyError: 'email'
email = student.get("email", "No email on record")
print("Email status:", email)


# ==========================================
# 3. ADDING AND UPDATING ENTRIES
# ==========================================
print("\n--- 3. Updating and Adding Entries ---")
# Updating an existing value:
student["grade"] = 10
print("Promoted Grade:  ", student["grade"])

# Adding a brand new key:
student["house"] = "Kilimanjaro"
print("After adding house:", student)

# Deleting an entry (.pop()):
removed_val = student.pop("is_active")
print(f"Removed 'is_active' (was {removed_val}):", student)


# ==========================================
# 4. ITERATING OVER A DICTIONARY
# ==========================================
print("\n--- 4. Iterating with .items() ---")
# A horse racing profile (directly connecting to our Capstone!):
race_horse = {
    "name": "Thunder",
    "jockey": "J. Mwangi",
    "speed_rating": 88,
    "wins": 14,
    "current_odds": "2.5x"
}

for attribute, val in race_horse.items():
    print(f"  {attribute.replace('_', ' ').title():<15}: {val}")


# ==========================================
# 5. NESTED DICTIONARIES (STUDENT ROSTER)
# ==========================================
print("\n--- 5. Nested Dictionaries ---")
classroom = {
    "ST-01": {"name": "Amina", "score": 92},
    "ST-02": {"name": "Tendo", "score": 87},
    "ST-03": {"name": "Zuri",  "score": 95}
}

for student_id, info in classroom.items():
    print(f"ID: {student_id} | Name: {info['name']:<8} | Score: {info['score']}%")
