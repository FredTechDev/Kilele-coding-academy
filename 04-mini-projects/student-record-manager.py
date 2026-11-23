"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 7
Project: Student Record Directory & Data Manager
File: student-record-manager.py
Concepts Applied: Dictionaries, lists, JSON file persistence, CRUD operations
=============================================================================
"""

import sys
import json
import os

RECORDS_FILE = "student_records.json"

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return demo_val

class StudentDatabase:
    def __init__(self, storage_path=RECORDS_FILE):
        self.storage_path = storage_path
        self.students = {}
        self.load_from_disk()

    def add_student(self, student_id, name, grade, track):
        self.students[student_id] = {
            "name": name,
            "grade": grade,
            "track": track
        }
        self.save_to_disk()
        print(f"✔ Successfully enrolled {name} (ID: {student_id}).")

    def display_all(self):
        print("\n" + "=" * 65)
        print(f"{'CURRENT ENROLLED COHORT ROSTER':^65}")
        print("=" * 65)
        print(f"{'ID':<10} {'Name':<22} {'Grade':<10} {'Curriculum Track'}")
        print("-" * 65)
        if not self.students:
            print("No students currently registered in database.")
        else:
            for s_id, data in self.students.items():
                print(f"{s_id:<10} {data['name']:<22} {data['grade']:<10} {data['track']}")
        print("=" * 65 + "\n")

    def search_student(self, query):
        print(f"\nSearch results for query: '{query}'")
        found = False
        for s_id, data in self.students.items():
            if query.lower() in s_id.lower() or query.lower() in data['name'].lower():
                print(f"  FOUND: ID: {s_id} | Name: {data['name']} | Grade: {data['grade']} | Track: {data['track']}")
                found = True
        if not found:
            print("  No matching student record found.")

    def save_to_disk(self):
        try:
            with open(self.storage_path, "w") as f:
                json.dump(self.students, f, indent=4)
        except IOError as err:
            print(f"⚠️ Error saving records: {err}")

    def load_from_disk(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r") as f:
                    self.students = json.load(f)
            except Exception:
                self.students = {}

def run_record_manager():
    print("=" * 60)
    print("      KILELE CODE STUDIO · STUDENT RECORD MANAGER        ")
    print("=" * 60)

    db = StudentDatabase("temp_demo_students.json" if "--demo" in sys.argv else RECORDS_FILE)

    if "--demo" in sys.argv:
        print("[Auto-demo]: Populating initial sample cohort records...")
        db.add_student("KCS-001", "Zawadi Baraka", "Grade 9", "Python Core")
        db.add_student("KCS-002", "Faraji Mwangi", "Grade 8", "Game Dev")
        db.add_student("KCS-003", "Amina Patel",  "Grade 10", "AI & Data")
        db.display_all()
        db.search_student("Zawadi")
        db.search_student("KCS-003")

        # Cleanup demo file
        if os.path.exists("temp_demo_students.json"):
            os.remove("temp_demo_students.json")
        print("[Auto-demo complete. Cleaned up demo files.]\n")
        return

    while True:
        print("\nMain Menu:")
        print("  [1] View All Students")
        print("  [2] Add New Student")
        print("  [3] Search Student")
        print("  [4] Exit")

        choice = get_input("Choose option (1-4): ", "4")

        if choice == "1":
            db.display_all()
        elif choice == "2":
            s_id = get_input("Enter Student ID (e.g. KCS-105): ", "KCS-105").upper()
            name = get_input("Enter Full Name: ", "New Student").title()
            grade = get_input("Enter Grade: ", "Grade 9")
            track = get_input("Enter Track: ", "Python Programming")
            db.add_student(s_id, name, grade, track)
        elif choice == "3":
            query = get_input("Enter name or ID to search: ", "")
            if query:
                db.search_student(query)
        elif choice in ["4", "exit", "quit"]:
            print("Records safely persisted. Goodbye! 👋")
            break

if __name__ == "__main__":
    run_record_manager()
