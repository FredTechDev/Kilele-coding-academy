# Capstone A — Horse Racing Simulation

> **Primary Python Capstone Project**  
> *Kilele Code Studio · 2026*

An interactive terminal-based horse racing game and simulation. The player manages a fictional classroom token balance, places wagers on competing horses, and watches an animated race sequence unfold in real time.

---

## 🎯 Project Overview & Objectives

This capstone demonstrates how foundational Python topics come together to produce a complete, polished interactive application:
1. **State Management:** Tracking player balance, horse positions, odds, and round outcomes.
2. **Animation & Timing:** Creating terminal graphics using loops, string repetition, screen refreshing, and `time.sleep()`.
3. **Simulation Logic:** Calculating step increments with `random.randint()`.
4. **Input Defense:** Guarding against invalid choices, non-numeric stakes, and bets exceeding current balance.
5. **Replay Flow:** Enabling continuous rounds until the player chooses to exit or runs out of credits.

---

## 🧩 Required Python Concepts

- **Variables & Constants:** `STARTING_BALANCE`, `FINISH_LINE`, etc.
- **Data Structures:** Dictionaries mapping horse numbers to names, positions, and track progress.
- **Loops:** `while` game loops and `for` animation rendering cycles.
- **Conditional Logic:** Evaluating winners, payouts, and player eligibility.
- **Standard Modules:** `random`, `time`, `os`.
- **Functions:** Modular procedures with single responsibilities (`clear_screen()`, `get_valid_bet()`, `run_race()`, etc.).

---

## 🚀 How to Run the Program

Navigate to this folder and execute `main.py`:

```bash
cd 05-capstone-projects/horse-racing-game
python3 main.py
```

---

## 🎮 Expected Behaviour & Game Rules

1. **Age Verification:** Confirms eligibility before commencing.
2. **Bankroll:** The player starts with 100 classroom credits.
3. **Horse Selection:** Choose between Thunder, Lightning, and Shadow.
4. **Wager Placement:** Enter a stake between 1 credit and your current balance.
5. **The Race:** The terminal clears and displays the track dynamically as horses advance toward the finish line.
6. **Result & Settlement:** If your chosen horse wins, you receive a 2x payout; otherwise, the stake is deducted.
7. **Replay / Game Over:** Continue racing until credits reach zero or you choose to quit.

---

## 🧪 Testing Scenarios

Verify the program's resilience by testing these scenarios:
- **Zero or Negative Stake:** Enter `0` or `-20` when prompted for a bet. The game should politely decline and prompt again.
- **Overdraft Attempt:** If your balance is 100, try entering `150`. The program should block the bet.
- **Non-Numeric Characters:** Type `"abc"` or symbols instead of numbers. The program must not crash with a `ValueError`.
- **Photo Finish:** Check how the simulation resolves ties when two horses cross the finish line on the same cycle.

---

## 🌟 Extension Challenges

Ready to take the game further? Try implementing:
1. **Custom Horse Odds:** Give each horse varying speeds and payout multipliers (e.g. a faster horse with a 1.5x payout vs. an underdog with a 4x payout).
2. **Obstacles & Weather:** Add random weather events (e.g. "Muddy track slows all horses by 1 step").
3. **Multiplayer Mode:** Allow two players in the classroom to take turns betting on horses in the same race.
