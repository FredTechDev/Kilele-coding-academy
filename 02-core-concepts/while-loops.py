"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: while-loops.py
Description: Indefinite iteration, game loops, and preventing infinite loops
=============================================================================

Learning Objectives:
1. Understand indefinite iteration and when to use while vs for loops.
2. Control while loops using loop counters and sentinel conditions.
3. Understand how infinite loops happen and how to prevent them.
4. Master the while True + break pattern used in game loops.
"""

print("==================================================")
print("            LESSON 08: WHILE LOOPS                ")
print("==================================================")

# ==========================================
# 1. BASIC while LOOP
# ==========================================
# A while loop repeats its indented body as long as its condition is True.
print("\n--- 1. Loop with a Counter ---")
countdown = 5

while countdown > 0:
    print(f"T-minus: {countdown}...")
    countdown -= 1  # VERY IMPORTANT: update counter to prevent an infinite loop!

print("Ignition and liftoff! 🚀")


# ==========================================
# 2. SIMULATING A GAME ENERGY DEPLETION
# ==========================================
# While loops shine when you don't know in advance how many turns will occur:
print("\n--- 2. Energy Depletion Simulation ---")
player_energy = 100
drain_per_turn = 25
turn = 1

while player_energy > 0:
    print(f"Turn {turn}: Energy = {player_energy}%")
    player_energy -= drain_per_turn
    turn += 1

print(f"Player collapsed: Energy reached {player_energy}% (Game Over).")


# ==========================================
# 3. THE while True + break PATTERN
# ==========================================
# Used extensively in interactive programs and games. The loop runs indefinitely
# until an explicit exit condition triggers 'break':
print("\n--- 3. Terminal Menu Loop Pattern ---")
# Simulating a user choosing menu options:
simulated_actions = ["1", "2", "3", "quit"]
step = 0

while True:
    choice = simulated_actions[step]
    step += 1
    print(f"Menu Selection: '{choice}'")

    if choice == "1":
        print("  --> Displaying High Scores...")
    elif choice == "2":
        print("  --> Opening Audio Settings...")
    elif choice == "3":
        print("  --> Starting New Game Level...")
    elif choice == "quit":
        print("  --> Goodbye! Exiting game loop...")
        break  # Clean exit from the while True loop


# ==========================================
# 4. HOW INFINITE LOOPS HAPPEN
# ==========================================
# If a while loop's condition NEVER becomes False, it runs forever, freezing the program!
# Example of an accidental infinite loop:
#   count = 1
#   while count <= 5:
#       print(count)
#       # OOPS! Forgot: count += 1. 'count' stays 1 forever!
#
# Rule of Thumb: Always verify that your loop body modifies the condition variable!
