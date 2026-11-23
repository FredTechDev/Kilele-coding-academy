# Level 1 — Beginner Exercises

> **Kilele Python Learning Pack · Practical Practice**  
> *Target: Grades 7–10 / Introductory Programmers*  
> *Concepts: Variables, Data Types, Input/Output, Operators, Basic Conditionals*

---

## 🎯 Purpose of These Exercises
Level 1 exercises focus on building syntax fluency with isolated concepts. Each problem gives you clear specifications, sample inputs, and expected outputs.

Attempt every exercise independently before checking [`solutions/beginner_solutions.py`](./solutions/beginner_solutions.py).

---

### Exercise 1: Student ID Badge Generator
**Problem:** Write a program that stores your name, school/academy name, student ID number, and favorite coding language in variables. Print a neat text badge.  
**Requirements:**
- Store values in properly named `snake_case` variables.
- Display a decorative border with asterisks or equal signs.
**Sample Output:**
```text
========================================
       KILELE CODE STUDIO STUDENT BADGE  
========================================
Name:     Amani Mwangi
ID:       KCS-2026-042
Academy:  Kilele Code Studio
Focus:    Python Programming
========================================
```

---

### Exercise 2: Age in Months and Days
**Problem:** Write a program that asks the user for their age in whole years. Calculate and display approximately how many months, days, and hours they have been alive.  
**Formulas:**
- Months = Years × 12
- Days = Years × 365 (ignore leap years for simplicity)
- Hours = Days × 24  
**Sample Output:**
```text
Enter your age in years: 14
At 14 years old, you have lived approximately:
- 168 months
- 5,110 days
- 122,640 hours!
```

---

### Exercise 3: Temperature Converter (Celsius to Fahrenheit)
**Problem:** Create a program that converts a temperature from degrees Celsius to Fahrenheit.  
**Formula:** `Fahrenheit = (Celsius * 9/5) + 32`  
**Sample Output:**
```text
Enter temperature in Celsius: 25.0
25.0°C is equal to 77.0°F.
```

---

### Exercise 4: Restaurant Bill Splitter
**Problem:** Write a program to help friends split a restaurant bill equally.  
**Requirements:**
- Input: Total bill amount (float), tip percentage (e.g., 10 for 10%), and number of people (int).
- Output: Total tip amount, total bill with tip, and amount each person must pay.  
**Sample Output:**
```text
Total food bill: $80.00
Tip percentage:  15%
Number of people: 4

Tip amount:      $12.00
Total with tip:  $92.00
Each person pays: $23.00
```

---

### Exercise 5: Even or Odd Checker
**Problem:** Write a program that takes an integer from the user and determines whether it is an Even number or an Odd number using the modulus operator (`%`).  
**Sample Output:**
```text
Enter an integer: 17
17 is an ODD number!
```

---

### Exercise 6: Password Length Validator
**Problem:** Prompt the user to enter a proposed password. Use `len()` to check its length:
- If length is less than 8 characters, print: `"Weak: Password must be at least 8 characters long."`
- If length is 8 characters or more, print: `"Strong: Password length accepted."`  
**Sample Output:**
```text
Enter your new password: coder
Weak: Password must be at least 8 characters long.
```

---

### Exercise 7: Cinema Ticket Pricing
**Problem:** Write a ticket pricing calculator based on customer age:
- Age 0–5: Free ($0.00)
- Age 6–12: Child ticket ($5.00)
- Age 13–17: Teenager ticket ($8.00)
- Age 18+: Adult ticket ($12.00)  
**Sample Output:**
```text
Enter customer age: 14
Customer is a Teenager. Ticket price: $8.00
```

---

### Exercise 8: Rectangle Geometry Tool
**Problem:** Ask the user for the length and width of a rectangle (allowing decimal numbers). Calculate and display both the **Perimeter** and the **Area**.  
**Formulas:**
- `Perimeter = 2 * (length + width)`
- `Area = length * width`  
**Sample Output:**
```text
Enter length: 8.5
Enter width: 4.0
Perimeter: 25.0 units
Area:      34.0 square units
```

---

### Exercise 9: Discount Eligibility Inspector
**Problem:** A bookshop offers a discount if a student has a loyalty card **OR** if their purchase total is over $50.00.  
Write a program that asks for the purchase total and a `yes/no` answer for the loyalty card. Use logical operators (`or`) to display whether they qualify for the discount.  
**Sample Output:**
```text
Purchase total: $35.00
Do you have a loyalty card (yes/no)? yes
Discount Applied: You qualify for the 10% member discount!
```

---

### Exercise 10: Classroom Supply Inventory
**Problem:** Create a script simulating an inventory count of pencils in a school supply locker.  
**Requirements:**
- Start with 120 pencils.
- Simulate handing out 35 pencils to Grade 7 (`-= 35`).
- Simulate receiving a donation box of 50 new pencils (`+= 50`).
- Print the initial count, after distribution, and the final tally.
