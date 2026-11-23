"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 3
Project: Age & Program Eligibility Checker
File: age-eligibility-checker.py
Concepts Applied: User input, type casting, nested & compound conditionals
=============================================================================
"""

import sys

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return demo_val

def check_eligibility():
    print("=" * 60)
    print("        KILELE STUDENT PROGRAM & CIVIC ELIGIBILITY CHECKER   ")
    print("=" * 60)

    applicant_name = get_input("Enter student name: ", "Faraji Kimani").title()
    raw_age = get_input("Enter student age:  ", "14")

    if not raw_age.isdigit():
        print("⚠️ Invalid age entered! Please enter a whole positive number.")
        return

    age = int(raw_age)
    has_parent_consent = get_input("Has parental consent slip? (yes/no): ", "yes").lower().startswith("y")

    print("\n" + "-" * 50)
    print(f"ELIGIBILITY REPORT FOR: {applicant_name} ({age} years old)")
    print("-" * 50)

    # 1. Kilele Code Studio Curriculum Track Placement
    print("1. Kilele Coding Pathway Placement:")
    if age < 7:
        print("   ❌ Too young for current cohorts. Recommended: Unplugged Logic Games.")
    elif 7 <= age <= 9:
        print("   ✔ Track: Junior Creative Coders (Block-based Scratch & Micro:bit)")
    elif 10 <= age <= 15:
        print("   ✔ Track: Python Foundation & App Builder (Current Course: Grades 7-10)")
    else:
        print("   ✔ Track: Senior Software Engineering & Full-Stack Development")

    # 2. Classroom Horse Racing Simulation Access (Needs age >= 8)
    print("\n2. Classroom Simulation & Capstone Lab Access:")
    if age >= 8:
        print("   ✔ Eligible for Horse Racing Simulation Capstone!")
    else:
        print("   ❌ Requires minimum age of 8.")

    # 3. Youth Robotics & Drone Field Trips (Needs age >= 12 AND consent)
    print("\n3. Advanced Robotics Field Trip:")
    if age >= 12 and has_parent_consent:
        print("   ✔ APPROVED: Student meets age threshold (12+) and holds signed consent!")
    elif age >= 12 and not has_parent_consent:
        print("   ⚠️ PENDING: Student meets age requirement but needs a signed consent form.")
    else:
        print("   ❌ NOT ELIGIBLE: Requires minimum age of 12.")

    # 4. Civic Milestones
    print("\n4. General Civic Age Benchmarks:")
    can_work = age >= 16
    can_vote = age >= 18
    print(f"   - Youth Apprenticeship (16+): {'Eligible' if can_work else 'Underage'}")
    print(f"   - Voter Registration  (18+): {'Eligible' if can_vote else 'Underage'}")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    check_eligibility()
