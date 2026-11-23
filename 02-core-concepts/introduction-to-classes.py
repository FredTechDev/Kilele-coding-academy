"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: introduction-to-classes.py
Description: Introduction to Object-Oriented Programming (Classes & Objects)
=============================================================================

Learning Objectives:
1. Understand the core philosophy of Object-Oriented Programming (OOP).
2. Grasp the Blueprint Analogy: Class (blueprint) vs Object (actual instance).
3. Define classes using the class keyword and PascalCase naming.
4. Master the __init__() initializer and the self parameter.
5. Define instance attributes and behavior methods.
"""

import random

print("==================================================")
print("     LESSON 17: INTRODUCTION TO CLASSES (OOP)     ")
print("==================================================")

# ==========================================
# 1. THE OOP BLUEPRINT ANALOGY
# ==========================================
# In procedural programming, we pass raw data into loose functions.
# In Object-Oriented Programming (OOP), we bundle together:
#   1. ATTRIBUTES (Data / State: what the object KNOWS)
#   2. METHODS (Behavior / Functions: what the object DOES)
#
# Analogy:
#   Class  = Architectural blueprint for a racing horse
#   Object = An actual living horse constructed using that blueprint!


# ==========================================
# 2. DEFINING A CLASS AND THE __init__ METHOD
# ==========================================
class RaceHorse:
    """Represents a competitive horse on the race track."""

    def __init__(self, name, jockey, jersey_color):
        """
        The constructor / initializer. Runs automatically when a new horse is created!
        'self' refers to the specific individual horse instance being born.
        """
        # Attributes (State):
        self.name = name
        self.jockey = jockey
        self.jersey_color = jersey_color
        self.track_position = 0
        self.is_finished = False

    # Methods (Behavior):
    def gallop(self):
        """Advances the horse forward by a random sprint distance."""
        advance = random.randint(2, 5)
        self.track_position += advance
        return advance

    def get_progress_display(self, finish_line=30):
        """Generates an ASCII visualization of the horse's position on track."""
        track = "-" * self.track_position + "🏇" + " " * max(0, finish_line - self.track_position) + "|🏁"
        return f"{self.name:<10} [{self.jersey_color:<6}]: {track} (Pos: {self.track_position})"


# ==========================================
# 3. CREATING OBJECTS (INSTANTIATION)
# ==========================================
print("\n--- 3. Instantiating Objects from a Class ---")

# Creating three distinct objects from the RaceHorse class blueprint:
horse1 = RaceHorse(name="Thunder", jockey="Mwangi", jersey_color="Blue")
horse2 = RaceHorse(name="Lightning", jockey="Amina", jersey_color="Gold")
horse3 = RaceHorse(name="Shadow", jockey="Kofi", jersey_color="Black")

print(f"Created horse: {horse1.name} ridden by {horse1.jockey}")
print(f"Created horse: {horse2.name} ridden by {horse2.jockey}")
print(f"Created horse: {horse3.name} ridden by {horse3.jockey}")


# ==========================================
# 4. INVOKING METHODS (BEHAVIOR IN ACTION)
# ==========================================
print("\n--- 4. Running Simulation with Object Methods ---")

# Turn 1:
print("--- Turn 1 Sprint ---")
for h in [horse1, horse2, horse3]:
    step = h.gallop()
    print(f"  {h.name} galloped forward {step} meters!")

# Display current track positions:
print("\nTrack Status:")
for h in [horse1, horse2, horse3]:
    print(h.get_progress_display(finish_line=20))


# ==========================================
# 5. SUMMARY OF KEY OOP TERMS
# ==========================================
# - Class: A blueprint defining attributes and methods (e.g. RaceHorse).
# - Object / Instance: A concrete entity built from a class (e.g. horse1).
# - Attribute: A variable that belongs to an object (e.g. self.name).
# - Method: A function that belongs to an object and can access 'self' (e.g. gallop()).
