"""
=============================================================================
Kilele Python Learning Pack — Capstone Project B
Project: Student Results Management System
File: main.py
Description: Terminal academic results database, ranking, analytics & CSV export
=============================================================================
"""

import sys
import json
import os
import csv

DATA_FILE = "student_results_db.json"
DEFAULT_SUBJECTS = ["Mathematics", "Physics", "English", "Python Programming", "Robotics"]

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return demo_val

class ResultsManager:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.records = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.records = json.load(f)
            except Exception:
                self.records = {}

    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.records, f, indent=4)
        except IOError as err:
            print(f"⚠️ Error saving records: {err}")

    def add_or_update_student(self, student_id, name, marks_dict):
        self.records[student_id] = {
            "name": name,
            "marks": marks_dict
        }
        self.save_data()
        print(f"✔ Results recorded for {name} ({student_id}).")

    def calculate_student_average(self, student_id):
        marks = self.records[student_id]["marks"].values()
        if not marks:
            return 0.0
        return sum(marks) / len(marks)

    @staticmethod
    def get_letter_grade(average):
        if average >= 80: return "A (Distinction)"
        elif average >= 70: return "B (Merit)"
        elif average >= 60: return "C (Credit)"
        elif average >= 50: return "D (Pass)"
        else: return "E (Referral)"

    def get_ranked_students(self):
        ranked = []
        for s_id, data in self.records.items():
            avg = self.calculate_student_average(s_id)
            ranked.append((s_id, data["name"], avg, self.get_letter_grade(avg)))
        # Sort by average descending
        ranked.sort(key=lambda x: x[2], reverse=True)
        return ranked

    def display_master_gradebook(self):
        ranked = self.get_ranked_students()
        print("\n" + "=" * 70)
        print(f"{'KILELE CODE STUDIO · COHORT MASTER GRADEBOOK':^70}")
        print("=" * 70)
        print(f"{'Rank':<6} {'ID':<10} {'Name':<22} {'Average':<12} {'Letter Grade'}")
        print("-" * 70)
        if not ranked:
            print("No student records found.")
        else:
            for rank, (s_id, name, avg, grade) in enumerate(ranked, start=1):
                badge = "🏆" if rank == 1 else f"#{rank}"
                print(f"{badge:<6} {s_id:<10} {name:<22} {avg:>6.1f}%     {grade}")
        print("=" * 70 + "\n")

    def display_subject_analytics(self):
        if not self.records:
            print("No records available to compute analytics.")
            return

        subject_scores = {subj: [] for subj in DEFAULT_SUBJECTS}
        for data in self.records.values():
            for subj, mark in data["marks"].items():
                if subj in subject_scores:
                    subject_scores[subj].append(mark)

        print("\n" + "=" * 60)
        print(f"{'SUBJECT-BY-SUBJECT PERFORMANCE ANALYTICS':^60}")
        print("=" * 60)
        print(f"{'Subject':<22} {'Mean Avg':<12} {'Highest':<10} {'Lowest'}")
        print("-" * 60)
        for subj, marks in subject_scores.items():
            if marks:
                mean_val = sum(marks) / len(marks)
                high_val = max(marks)
                low_val = min(marks)
                print(f"{subj:<22} {mean_val:>6.1f}%     {high_val:>5.1f}%    {low_val:>5.1f}%")
        print("=" * 60 + "\n")

    def export_to_csv(self, output_path="cohort_results_export.csv"):
        ranked = self.get_ranked_students()
        try:
            with open(output_path, "w", newline="") as f:
                writer = csv.writer(f)
                header = ["Rank", "StudentID", "Name"] + DEFAULT_SUBJECTS + ["OverallAverage", "Grade"]
                writer.writerow(header)
                for rank, (s_id, name, avg, grade) in enumerate(ranked, start=1):
                    row = [rank, s_id, name]
                    student_marks = self.records[s_id]["marks"]
                    for subj in DEFAULT_SUBJECTS:
                        row.append(student_marks.get(subj, "N/A"))
                    row.extend([f"{avg:.2f}", grade])
                    writer.writerow(row)
            print(f"✔ Successfully exported cohort gradebook to: '{output_path}'")
        except IOError as err:
            print(f"⚠️ Error exporting CSV: {err}")

def run_results_system():
    print("=" * 65)
    print("      KILELE CODE STUDIO · STUDENT RESULTS MANAGEMENT SYSTEM     ")
    print("=" * 65)

    test_file = "temp_results_test.json" if "--demo" in sys.argv else DATA_FILE
    manager = ResultsManager(test_file)

    if "--demo" in sys.argv:
        print("[Auto-demo]: Populating sample student examination results...")
        manager.add_or_update_student(
            "KCS-101", "Zawadi Baraka",
            {"Mathematics": 92.0, "Physics": 85.0, "English": 78.0, "Python Programming": 98.0, "Robotics": 90.0}
        )
        manager.add_or_update_student(
            "KCS-102", "Amina Patel",
            {"Mathematics": 88.0, "Physics": 91.0, "English": 89.0, "Python Programming": 94.0, "Robotics": 86.0}
        )
        manager.add_or_update_student(
            "KCS-103", "Kofi Mensah",
            {"Mathematics": 74.0, "Physics": 68.0, "English": 82.0, "Python Programming": 85.0, "Robotics": 79.0}
        )
        manager.add_or_update_student(
            "KCS-104", "Faraji Kimani",
            {"Mathematics": 58.0, "Physics": 62.0, "English": 65.0, "Python Programming": 70.0, "Robotics": 64.0}
        )

        manager.display_master_gradebook()
        manager.display_subject_analytics()
        manager.export_to_csv("temp_export.csv")

        # Clean demo files
        for f in [test_file, "temp_export.csv"]:
            if os.path.exists(f): os.remove(f)
        print("[Auto-demo completed test runs. Cleaned temporary files.]\n")
        return

    while True:
        print("\nMain Menu:")
        print("  [1] Display Cohort Master Gradebook")
        print("  [2] View Subject Performance Analytics")
        print("  [3] Record / Update Student Marks")
        print("  [4] Export Results to CSV")
        print("  [5] Exit")

        choice = get_input("\nEnter choice (1-5): ", "5")
        if choice == "1":
            manager.display_master_gradebook()
        elif choice == "2":
            manager.display_subject_analytics()
        elif choice == "3":
            s_id = get_input("Student ID (e.g. KCS-201): ", "KCS-201").upper()
            name = get_input("Student Full Name: ", "Learner Name").title()
            marks = {}
            for subj in DEFAULT_SUBJECTS:
                raw = get_input(f"Mark for {subj} (0-100): ", "75")
                try:
                    marks[subj] = float(raw)
                except ValueError:
                    marks[subj] = 50.0
            manager.add_or_update_student(s_id, name, marks)
        elif choice == "4":
            filename = get_input("Export filename [results.csv]: ", "results.csv")
            manager.export_to_csv(filename if filename else "results.csv")
        elif choice in ["5", "exit", "quit"]:
            print("System shutting down. Goodbye! 👋")
            break

if __name__ == "__main__":
    run_results_system()
