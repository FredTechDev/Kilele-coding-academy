"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: tuples.py
Description: Immutable sequences, coordinate pairs, and tuple unpacking
=============================================================================

Learning Objectives:
1. Understand tuples as ordered, immutable collections.
2. Differentiate between lists (mutable) and tuples (immutable).
3. Master tuple unpacking into separate variables.
4. Return multiple values from functions using tuples.
5. Learn the single-item tuple syntax (item,).
"""

print("==================================================")
print("             LESSON 12: TUPLES                    ")
print("==================================================")

# ==========================================
# 1. WHAT IS A TUPLE?
# ==========================================
# Tuples are created with parentheses ().
# Like lists, they are ordered and zero-indexed.
# UNLIKE lists, they CANNOT be changed after creation (immutable).

screen_dimensions = (1920, 1080)
gps_coordinates = (-1.286389, 36.817223)  # Latitude and Longitude of Nairobi

print("\n--- 1. Declaring and Accessing Tuples ---")
print("Screen Dimensions:", screen_dimensions)
print("Width [0]:        ", screen_dimensions[0])
print("Height [1]:       ", screen_dimensions[1])


# ==========================================
# 2. WHY USE TUPLES INSTEAD OF LISTS?
# ==========================================
# 1. Data Integrity / Safety: Protects data that should never accidentally be changed
#    (like days of the week, geographic coordinates, or RGB color values).
# 2. Performance: Tuples take less memory and are faster to process than lists.

primary_colors = ("Red", "Green", "Blue")
print("\n--- 2. Immutable Guarantee ---")
# primary_colors[0] = "Yellow"  --> TypeError: 'tuple' object does not support item assignment
print("Tuples protect constant sequences from accidental reassignment.")


# ==========================================
# 3. TUPLE UNPACKING
# ==========================================
# You can extract values directly into individual variables:
print("\n--- 3. Tuple Unpacking ---")
player_profile = ("Zuri", 15, "Grade 9", "Gold Medalist")

# Unpack into 4 clean variables:
name, age, grade, award = player_profile

print(f"Name:  {name}")
print(f"Age:   {age}")
print(f"Grade: {grade}")
print(f"Award: {award}")


# ==========================================
# 4. RETURNING MULTIPLE VALUES FROM A FUNCTION
# ==========================================
# When a function returns multiple items separated by commas, it actually returns a tuple!
print("\n--- 4. Multi-Value Return ---")

def get_circle_stats(radius):
    """Calculates circumference and area of a circle."""
    pi = 3.14159
    circumference = 2 * pi * radius
    area = pi * (radius ** 2)
    return circumference, area  # Returns a tuple: (circumference, area)

circ, circle_area = get_circle_stats(10)
print(f"Radius: 10 ──▶ Circumference: {circ:.2f}, Area: {circle_area:.2f}")


# ==========================================
# 5. THE SINGLE-ITEM TUPLE QUIRK
# ==========================================
# In Python, parentheses around a single value are treated as math grouping:
not_a_tuple = ("Single")       # type: str!
is_a_tuple = ("Single",)       # type: tuple! (Notice the trailing comma)

print("\n--- 5. Single-item Tuples ---")
print("type(('Single')): ", type(not_a_tuple))
print("type(('Single',)):", type(is_a_tuple))
