"""
=============================================================================
Kilele Python Learning Pack — Capstone Project C
Project: School Management System
File: main.py
Description: Object-Oriented educational management system modeling Students,
             Teachers, Courses, and School Administration with JSON persistence
=============================================================================
"""

import sys
import json
import os

DB_FILE = "school_state.json"

def get_input(prompt, demo_val):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_val}")
        return demo_val
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return demo_val


class Student:
    """Represents a student enrolled at Kilele Academy."""
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.enrolled_course_codes = []

    def enroll(self, course_code):
        if course_code not in self.enrolled_course_codes:
            self.enrolled_course_codes.append(course_code)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
            "enrolled_course_codes": self.enrolled_course_codes
        }

    @classmethod
    def from_dict(cls, data):
        s = cls(data["student_id"], data["name"], data["grade"])
        s.enrolled_course_codes = data.get("enrolled_course_codes", [])
        return s


class Teacher:
    """Represents an instructor teaching at Kilele Academy."""
    def __init__(self, teacher_id, name, subject_specialty):
        self.teacher_id = teacher_id
        self.name = name
        self.subject_specialty = subject_specialty

    def to_dict(self):
        return {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "subject_specialty": self.subject_specialty
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["teacher_id"], data["name"], data["subject_specialty"])


class Course:
    """Represents a curriculum course offering."""
    def __init__(self, code, title, capacity=25):
        self.code = code
        self.title = title
        self.capacity = capacity
        self.assigned_teacher_id = None
        self.enrolled_student_ids = []

    def assign_teacher(self, teacher_id):
        self.assigned_teacher_id = teacher_id

    def add_student(self, student_id):
        if len(self.enrolled_student_ids) >= self.capacity:
            return False, "Course has reached maximum student capacity!"
        if student_id in self.enrolled_student_ids:
            return False, "Student is already registered in this course."
        self.enrolled_student_ids.append(student_id)
        return True, "Enrolled successfully."

    def to_dict(self):
        return {
            "code": self.code,
            "title": self.title,
            "capacity": self.capacity,
            "assigned_teacher_id": self.assigned_teacher_id,
            "enrolled_student_ids": self.enrolled_student_ids
        }

    @classmethod
    def from_dict(cls, data):
        c = cls(data["code"], data["title"], data.get("capacity", 25))
        c.assigned_teacher_id = data.get("assigned_teacher_id")
        c.enrolled_student_ids = data.get("enrolled_student_ids", [])
        return c


class School:
    """Administrative orchestrator that oversees students, teachers, and courses."""
    def __init__(self, name="Kilele Code Studio", storage_file=DB_FILE):
        self.name = name
        self.storage_file = storage_file
        self.students = {}
        self.teachers = {}
        self.courses = {}
        self.load_state()

    def register_student(self, student_id, name, grade):
        if student_id in self.students:
            print(f"⚠️ Error: Student ID {student_id} already exists!")
            return False
        self.students[student_id] = Student(student_id, name, grade)
        self.save_state()
        print(f"✔ Registered student: {name} ({student_id})")
        return True

    def register_teacher(self, teacher_id, name, specialty):
        if teacher_id in self.teachers:
            print(f"⚠️ Error: Teacher ID {teacher_id} already exists!")
            return False
        self.teachers[teacher_id] = Teacher(teacher_id, name, specialty)
        self.save_state()
        print(f"✔ Registered instructor: {name} ({specialty})")
        return True

    def create_course(self, code, title, capacity=25):
        if code in self.courses:
            print(f"⚠️ Error: Course code {code} already exists!")
            return False
        self.courses[code] = Course(code, title, capacity)
        self.save_state()
        print(f"✔ Created course: {title} [{code}]")
        return True

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students:
            print(f"⚠️ Error: Student {student_id} not found.")
            return False
        if course_code not in self.courses:
            print(f"⚠️ Error: Course {course_code} not found.")
            return False

        course = self.courses[course_code]
        student = self.students[student_id]

        success, msg = course.add_student(student_id)
        if success:
            student.enroll(course_code)
            self.save_state()
            print(f"✔ Enrolled {student.name} in {course.title} [{course_code}].")
            return True
        else:
            print(f"⚠️ Could not enroll: {msg}")
            return False

    def display_directory(self):
        print("\n" + "=" * 70)
        print(f"{self.name.upper()} · ACADEMY DIRECTORY")
        print("=" * 70)
        print(f"Active Students:    {len(self.students)}")
        print(f"Active Faculty:     {len(self.teachers)}")
        print(f"Offered Courses:    {len(self.courses)}")
        print("-" * 70)
        print("COURSES OFFERED:")
        for c_code, c in self.courses.items():
            t_name = self.teachers[c.assigned_teacher_id].name if c.assigned_teacher_id in self.teachers else "Unassigned"
            print(f"  [{c_code:<8}] {c.title:<28} | Faculty: {t_name:<16} | Enrolled: {len(c.enrolled_student_ids)}/{c.capacity}")
        print("=" * 70 + "\n")

    def save_state(self):
        payload = {
            "name": self.name,
            "students": {s_id: s.to_dict() for s_id, s in self.students.items()},
            "teachers": {t_id: t.to_dict() for t_id, t in self.teachers.items()},
            "courses": {c_code: c.to_dict() for c_code, c in self.courses.items()}
        }
        try:
            with open(self.storage_file, "w") as f:
                json.dump(payload, f, indent=4)
        except IOError as err:
            print(f"⚠️ Error saving state: {err}")

    def load_state(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    self.name = data.get("name", self.name)
                    self.students = {s_id: Student.from_dict(d) for s_id, d in data.get("students", {}).items()}
                    self.teachers = {t_id: Teacher.from_dict(d) for t_id, d in data.get("teachers", {}).items()}
                    self.courses = {c_code: Course.from_dict(d) for c_code, d in data.get("courses", {}).items()}
            except Exception:
                pass


def run_school_system():
    print("=" * 65)
    print("      KILELE CODE STUDIO · SCHOOL MANAGEMENT SYSTEM (OOP)        ")
    print("=" * 65)

    test_file = "temp_school_state.json" if "--demo" in sys.argv else DB_FILE
    school = School("Kilele Code Studio Academy", test_file)

    if "--demo" in sys.argv:
        print("[Auto-demo]: Populating demo school community and courses...")
        # 1. Teachers
        school.register_teacher("T-01", "Dr. Nelson Mwangi", "Computer Science")
        school.register_teacher("T-02", "Eng. Fatuma Ali", "Robotics & Hardware")

        # 2. Courses
        school.create_course("CS-101", "Introduction to Python 3", capacity=30)
        school.create_course("ROB-201", "Micro:bit & Sensors", capacity=20)
        school.courses["CS-101"].assign_teacher("T-01")
        school.courses["ROB-201"].assign_teacher("T-02")

        # 3. Students
        school.register_student("S-101", "Zawadi Baraka", "Grade 9")
        school.register_student("S-102", "Amina Patel",   "Grade 10")
        school.register_student("S-103", "Kofi Mensah",   "Grade 8")

        # 4. Enrolling Students
        school.enroll_student("S-101", "CS-101")
        school.enroll_student("S-101", "ROB-201")
        school.enroll_student("S-102", "CS-101")
        school.enroll_student("S-103", "ROB-201")

        # 5. Display Directory
        school.display_directory()

        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)
        print("[Auto-demo completed test runs. Cleaned temporary files.]\n")
        return

    while True:
        print("\nSchool Operations Menu:")
        print("  [1] Display Academy Directory & Courses")
        print("  [2] Register New Student")
        print("  [3] Register New Instructor")
        print("  [4] Create New Course")
        print("  [5] Enroll Student in Course")
        print("  [6] Exit")

        choice = get_input("\nEnter option (1-6): ", "6")
        if choice == "1":
            school.display_directory()
        elif choice == "2":
            s_id = get_input("Student ID: ", "S-201").upper()
            name = get_input("Student Name: ", "Student Name").title()
            grade = get_input("Grade: ", "Grade 9")
            school.register_student(s_id, name, grade)
        elif choice == "3":
            t_id = get_input("Teacher ID: ", "T-10").upper()
            name = get_input("Teacher Name: ", "Teacher Name").title()
            dept = get_input("Specialty: ", "Python Programming")
            school.register_teacher(t_id, name, dept)
        elif choice == "4":
            c_code = get_input("Course Code (e.g. PY-101): ", "PY-101").upper()
            title = get_input("Course Title: ", "Python Fundamentals").title()
            school.create_course(c_code, title)
        elif choice == "5":
            s_id = get_input("Student ID: ", "").upper()
            c_code = get_input("Course Code: ", "").upper()
            school.enroll_student(s_id, c_code)
        elif choice in ["6", "exit", "quit"]:
            print("School data saved. Goodbye! 👋")
            break

if __name__ == "__main__":
    run_school_system()
