"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: sets.py
Description: Unique collections, mathematical set operations, and deduplication
=============================================================================

Learning Objectives:
1. Understand sets as unordered collections of unique elements.
2. Deduplicate lists instantly using set().
3. Add and remove set elements (.add(), .remove(), .discard()).
4. Perform set operations: Union (|), Intersection (&), Difference (-).
5. Understand the empty set quirk: set() vs {}.
"""

print("==================================================")
print("              LESSON 13B: SETS                    ")
print("==================================================")

# ==========================================
# 1. WHAT IS A SET?
# ==========================================
# A set is an UNORDERED collection of UNIQUE elements.
# Sets are created with curly braces {item1, item2} or the set() constructor.
# Duplicates are automatically and silently removed!

club_members = {"Amani", "Zawadi", "Kofi", "Amani", "Zuri", "Zawadi"}
print("\n--- 1. Set Uniqueness ---")
print("Raw input had duplicates ('Amani' x2, 'Zawadi' x2).")
print("Set contents:", club_members)
print("Unique member count:", len(club_members))


# ==========================================
# 2. INSTANT DEDUPLICATION OF LISTS
# ==========================================
# A common real-world use case: removing duplicate entries from user lists.
print("\n--- 2. Deduplicating a List ---")
survey_cities = ["Nairobi", "Mombasa", "Kisumu", "Nairobi", "Nakuru", "Mombasa"]
unique_cities = list(set(survey_cities))
print("Original list with duplicates:", survey_cities)
print("Clean deduplicated list:      ", sorted(unique_cities))


# ==========================================
# 3. ADDING AND REMOVING ELEMENTS
# ==========================================
print("\n--- 3. Adding and Removing ---")
tech_skills = {"Python", "Scratch", "HTML"}
print("Initial skills:", tech_skills)

# Adding an element (.add()):
tech_skills.add("Robotics")
print("After .add('Robotics'):", tech_skills)

# Removing safely (.discard() won't crash if item is absent):
tech_skills.discard("Scratch")
print("After .discard('Scratch'):", tech_skills)


# ==========================================
# 4. MATHEMATICAL SET OPERATIONS
# ==========================================
# Sets are built for Venn-Diagram operations:
print("\n--- 4. Venn Diagram Operations ---")
coding_club = {"Amani", "Baraka", "Zawadi", "Faraji"}
robotics_club = {"Zawadi", "Faraji", "Zuri", "Kofi"}

print("Coding Club:  ", coding_club)
print("Robotics Club:", robotics_club)

# A. UNION (|): Students in EITHER club (or both)
all_tech_students = coding_club | robotics_club
print("\nUnion (|) - All tech students:          ", all_tech_students)

# B. INTERSECTION (&): Students in BOTH clubs simultaneously
dual_enrolled = coding_club & robotics_club
print("Intersection (&) - In BOTH clubs:       ", dual_enrolled)

# C. DIFFERENCE (-): In Coding Club but NOT in Robotics Club
coding_only = coding_club - robotics_club
print("Difference (-) - In Coding ONLY:        ", coding_only)


# ==========================================
# 5. LIGHTNING-FAST MEMBERSHIP TESTING
# ==========================================
# Checking 'item in my_set' is instantaneous (O(1) time), even with 1,000,000 items!
print("\n--- 5. Membership Testing ---")
banned_usernames = {"admin", "root", "superuser", "guest"}
test_user = "baraka_coder"

if test_user in banned_usernames:
    print(f"Username '{test_user}' is prohibited!")
else:
    print(f"Username '{test_user}' is available and accepted! ✔")


# ==========================================
# 6. THE EMPTY SET QUIRK
# ==========================================
# CRITICAL TRAP:
#   empty_curly = {}       --> This creates an EMPTY DICTIONARY!
#   empty_set = set()      --> This creates an EMPTY SET!
print("\n--- 6. Empty Set vs Empty Dictionary ---")
print("type({}):    ", type({}))
print("type(set()): ", type(set()))
