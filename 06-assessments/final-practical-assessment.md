# Final Practical Capstone Assessment & Viva Voce

> **Kilele Python Learning Pack · Comprehensive Evaluation**  
> *Coverage: Modules 01 to 14 (Full Curriculum Integration)*  
> *Target: Grades 7–10 / Junior Software Engineers*  
> *Duration: 90 minutes (Practical Project + 10-minute Viva Defense) | Total Marks: 100*

---

## 🎯 Purpose of This Final Assessment
The Final Practical Assessment evaluates your transition from following instructions to **independently designing, coding, testing, debugging, and explaining a complete software application**.

---

## 🏗 The Project Brief (60 Marks)

Choose **ONE** of the following two project options to build from scratch:

### Option A: The Kilele Space Rover Resource Manager (OOP & File I/O)
Build a terminal mission controller for an autonomous planetary exploration rover:
1. **Rover Class**: Define a `Rover` class with attributes: `battery_level` (0–100%), `sample_inventory` (list), `distance_traveled`, and `status`.
2. **Rover Methods**:
   - `travel(km)`: Deducts battery (`1%` per km), increments distance, with random obstacle encounter checks.
   - `collect_sample(rock_type)`: Adds to inventory if battery > 10%.
   - `recharge()`: Restores battery to 100% using solar arrays.
3. **Data Persistence**: Save and reload the mission log (`mission_save.json`) across program restarts.
4. **Defensive Design**: Wrap battery depletion and file operations in `try...except` blocks so the rover controller never crashes.

### Option B: The Classroom Bank & Virtual Token Exchange
Build a full bank account and transaction ledger:
1. **Account Class**: Models student accounts with attributes: `account_id`, `owner_name`, `balance`, and `transaction_history` (list of timestamps & descriptions).
2. **Operations**:
   - Deposit and withdraw credits with strict overdraft protection (`balance >= withdrawal`).
   - Transfer credits between two accounts with atomic balance updates.
3. **Audit Trail**: Save an exportable text statement `statement_<id>.txt` summarizing all transactions.
4. **Input Validation**: Handle non-numeric deposits, negative inputs, and missing accounts gracefully.

---

## 📊 Marking Rubric (100 Marks Total)

| Evaluation Dimension | Description & Criteria | Marks |
| :--- | :--- | :---: |
| **1. Functional Correctness** | Application fulfills all core functional requirements without crashing. Edge cases (zero inputs, invalid types) handled defensively. | 25 |
| **2. Modular & OOP Architecture** | Proper use of classes (`class`, `__init__`, `self`), encapsulation of state, and single-responsibility functions. | 20 |
| **3. Code Style & Readability** | Adheres to PEP 8: clean `snake_case` naming, 4-space indentation, no dead code, and helpful inline comments. | 15 |
| **4. File I/O & Persistence** | Robust reading and writing of data (JSON or formatted text) using `with open(...)` context managers. | 15 |
| **5. Testing & Debugging Proof** | Student demonstrates testing with valid, invalid, and boundary inputs, explaining how potential bugs were identified and fixed. | 10 |
| **6. Viva Voce Defense** | 10-minute student oral presentation answering conceptual questions about their design choices and architecture. | 15 |
| **TOTAL** | **Comprehensive Certificate of Mastery** | **100** |

---

## 🎙 Viva Voce (Oral Defense) Question Bank

During the 10-minute defense, the instructor will ask the learner three questions selected from this bank:

1. *"Walk me through the flow of execution in your script from the moment you hit Enter in the terminal to when the main menu renders."*
2. *"Show me the most defensive line of code in your project. Why did you place a `try...except` or condition there, and what would happen if that check were deleted?"*
3. *"Why did you choose a dictionary (or class/list) to model this specific entity instead of simple individual variables?"*
4. *"If you had to add a multiplayer or networking feature next week, which function or class in your codebase would need to change first, and why?"*
5. *"Explain what the `self` keyword actually refers to inside your class methods."*
