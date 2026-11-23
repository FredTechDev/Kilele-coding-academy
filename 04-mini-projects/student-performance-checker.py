"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 6
Project: Student Academic Performance Checker
File: student-performance-checker.py
Concepts Applied: Functions with return values, validation, grading logic
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

def calculate_stats(scores):
    """Returns total and mean average of a list of marks."""
    total = sum(scores)
    average = total / len(scores)
    return total, average

def determine_grade_and_remark(average):
    """Maps average percentage to grade, GPA, and teacher remark."""
    if average >= 85:
        return "A", 4.0, "Distinction — Exemplary academic mastery!"
    elif average >= 75:
        return "B", 3.5, "Merit — Strong understanding and application."
    elif average >= 65:
        return "C", 3.0, "Credit — Consistent, satisfactory achievement."
    elif average >= 50:
        return "D", 2.0, "Pass — Meets minimum requirements; needs review."
    else:
        return "E", 1.0, "Referral — Requires targeted educational support."

def run_performance_checker():
    print("=" * 65)
    print("      KILELE ACADEMY · STUDENT PERFORMANCE EVALUATION TOOL       ")
    print("=" * 65)

    student_name = get_input("Student Name:       ", "Zuri Wanjiku").title()
    student_id = get_input("Student ID Number:  ", "KCS-901").upper()

    subjects = ["Mathematics", "Science", "English Literature", "Python Programming"]
    demo_scores = [88.0, 92.0, 79.0, 95.0]
    scores = []

    print("\nEnter marks for each subject (0 to 100):")
    for idx, subject in enumerate(subjects):
        prompt = f"  - {subject:<20}: "
        demo_val = str(demo_scores[idx])
        raw_val = get_input(prompt, demo_val)
        try:
            val = float(raw_val)
            if 0 <= val <= 100:
                scores.append(val)
            else:
                print("    ⚠️ Mark must be between 0 and 100! Defaulting to 50.")
                scores.append(50.0)
        except ValueError:
            print("    ⚠️ Non-numeric mark entered! Defaulting to 50.")
            scores.append(50.0)

    total_marks, average = calculate_stats(scores)
    grade, gpa, remark = determine_grade_and_remark(average)

    # Print Official Terminal Report Card
    print("\n" + "=" * 65)
    print(f"{'OFFICIAL TERMINAL REPORT CARD':^65}")
    print("=" * 65)
    print(f"Student: {student_name:<25} ID: {student_id}")
    print("-" * 65)
    print(f"{'Subject':<25} {'Mark':>10} {'Status':>25}")
    print("-" * 65)
    for subj, mark in zip(subjects, scores):
        status = "Distinction" if mark >= 80 else ("Pass" if mark >= 50 else "Fail")
        print(f"{subj:<25} {mark:>9.1f}% {status:>25}")
    print("-" * 65)
    print(f"Total Marks:       {total_marks:.1f} / {len(subjects) * 100}")
    print(f"Overall Average:   {average:.1f}%")
    print(f"Assigned Grade:    {grade} (GPA: {gpa:.1f})")
    print(f"Faculty Remark:    {remark}")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_performance_checker()
