"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: random-module.py
Description: Random number generation, choice selection, and simulation basics
=============================================================================

Learning Objectives:
1. Import and utilize standard library modules (import random, import time).
2. Generate integers within a range using random.randint().
3. Select elements randomly from a collection using random.choice().
4. Shuffle items in-place using random.shuffle().
5. Build simulations (dice rolls, coin flips, horse race strides).
"""

import random
import time

print("==================================================")
print("         LESSON 14: RANDOM MODULE                 ")
print("==================================================")

# ==========================================
# 1. GENERATING RANDOM INTEGERS
# ==========================================
# random.randint(a, b) returns a random integer N such that a <= N <= b (inclusive!)
print("\n--- 1. Simulating Dice Rolls ---")
for roll_num in range(1, 4):
    dice_roll = random.randint(1, 6)
    print(f"Roll #{roll_num}: Rolled a {dice_roll} 🎲")


# ==========================================
# 2. RANDOM SELECTION WITH random.choice()
# ==========================================
# random.choice() picks one element at random from any non-empty list or tuple:
print("\n--- 2. Random Selection ---")
weather_conditions = ["Sunny ☀️", "Rainy 🌧️", "Windy 💨", "Cloudy ⛅"]
todays_weather = random.choice(weather_conditions)
print("Today's simulated track weather:", todays_weather)

# Simulating a Coin Flip:
coin_result = random.choice(["Heads", "Tails"])
print("Coin flip outcome:              ", coin_result)


# ==========================================
# 3. SHUFFLING COLLECTIONS IN-PLACE
# ==========================================
# random.shuffle() rearranges the items of a mutable list:
print("\n--- 3. Shuffling a Deck ---")
quiz_topics = ["Loops", "Variables", "Functions", "OOP", "File I/O"]
print("Before shuffle:", quiz_topics)
random.shuffle(quiz_topics)
print("After shuffle: ", quiz_topics)


# ==========================================
# 4. CAPSTONE LINK: HORSE RACING STRIDE SIMULATION
# ==========================================
# In our Horse Racing Capstone, horses take random step increments each turn:
print("\n--- 4. Simulated Mini-Race Turn ---")
horses = ["Thunder", "Lightning", "Shadow"]
positions = {"Thunder": 0, "Lightning": 0, "Shadow": 0}

print("Starting race stride simulation:")
for step in range(1, 4):
    for h in horses:
        # Each horse moves forward randomly between 1 and 3 steps
        stride = random.randint(1, 3)
        positions[h] += stride
    print(f"Turn {step}: {positions}")
