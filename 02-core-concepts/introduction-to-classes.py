"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: introduction-to-classes.py
Description: Introduction to Object-Oriented Programming (OOP), Dunder Methods,
             and Inheritance
=============================================================================

Learning Objectives:
1. Understand the core philosophy of Object-Oriented Programming (OOP).
2. Grasp the Blueprint Analogy: Class (blueprint) vs Object (actual instance).
3. Define classes using the class keyword and PascalCase naming.
4. Master the __init__() initializer and the self parameter.
5. Implement the __str__() dunder method for clean object printing.
6. Understand Inheritance: Subclassing and super().__init__().
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
# 2. DEFINING A CLASS AND __init__
# ==========================================
class RaceHorse:
    """Base class representing a competitive horse on the race track."""

    def __init__(self, name, jockey, jersey_color):
        """
        The constructor / initializer. Runs automatically when a new horse is created!
        'self' refers to the specific individual horse instance being initialized.
        """
        # Attributes (State):
        self.name = name
        self.jockey = jockey
        self.jersey_color = jersey_color
        self.track_position = 0

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

    # DUNDER METHOD: __str__() controls how this object appears when printed:
    def __str__(self):
        return f"RaceHorse('{self.name}', Jockey: {self.jockey}, Color: {self.jersey_color})"


# ==========================================
# 3. INHERITANCE: SUBCLASSING & super()
# ==========================================
# A subclass inherits all attributes and methods of its parent class,
# but can add specialized behaviors or override existing ones:

class ChampionHorse(RaceHorse):
    """A specialized Thoroughbred horse that possesses a nitro boost ability."""

    def __init__(self, name, jockey, jersey_color, championship_trophies):
        # Call the parent class __init__ using super():
        super().__init__(name, jockey, jersey_color)
        self.championship_trophies = championship_trophies

    def turbo_sprint(self):
        """A specialized method only available to Champion horses!"""
        boost = random.randint(5, 8)
        self.track_position += boost
        print(f"  ⚡ TURBO SPRINT: {self.name} unleashes a {boost}m burst!")
        return boost

    def __str__(self):
        return f"ChampionHorse('{self.name}', Trophies: {self.championship_trophies})"


# ==========================================
# 4. INSTANTIATING OBJECTS AND TESTING
# ==========================================
print("\n--- 4. Instantiating Objects and __str__ ---")

horse1 = RaceHorse(name="Thunder", jockey="Mwangi", jersey_color="Blue")
horse2 = RaceHorse(name="Lightning", jockey="Amina", jersey_color="Gold")
champ = ChampionHorse(name="Shadow", jockey="Kofi", jersey_color="Black", championship_trophies=3)

# Notice how clean print() looks thanks to __str__():
print("Horse 1:", horse1)
print("Horse 2:", horse2)
print("Champion:", champ)


# ==========================================
# 5. RUNNING SIMULATION WITH INHERITED METHODS
# ==========================================
print("\n--- 5. Sprint Simulation ---")
horse1.gallop()
horse2.gallop()
champ.turbo_sprint()  # Champion uses its unique subclass method!

print("\nCurrent Track Status:")
for h in [horse1, horse2, champ]:
    print(h.get_progress_display(finish_line=20))
