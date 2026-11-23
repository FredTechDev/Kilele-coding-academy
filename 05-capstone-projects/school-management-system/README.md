# Capstone C — School Management System

> **Kilele Code Studio · Capstone Project 3**  
> *Object-Oriented Architecture, Multi-Entity Modeling & Persistent School Operations*

---

## 🎯 Project Overview & Objectives

The **School Management System** is an Object-Oriented Programming (OOP) capstone that models the real-world operational structure of an educational academy:
- **Students**: Tracks learner IDs, grade cohorts, enrolled courses, and attendance points.
- **Teachers / Instructors**: Models faculty IDs, names, and teaching specializations.
- **Courses**: Manages subject codes, maximum enrollment capacities, assigned instructors, and enrolled rosters.
- **School Administration**: Orchestrates registrations, enrollment links, and persists the complete school state to JSON.

---

## 🧩 Required Python Concepts

- **Object-Oriented Programming (OOP):** Class blueprints, constructors (`__init__`), instance attributes, and method encapsulation.
- **Entity Relationships:** Linking `Student` objects to `Course` objects and assigning a `Teacher` as course head.
- **Data Persistence:** Serializing and deserializing multiple connected objects using JSON.
- **Defensive Logic:** Enforcing classroom enrollment caps and preventing duplicate registrations.

---

## 🚀 How to Run the Program

```bash
cd 05-capstone-projects/school-management-system
python3 main.py
```
*(Run with `--demo` for an automated test run)*

---

## 🧪 Testing Scenarios

- **Enrollment Capacity Cap:** Attempting to enroll a student in a course that has reached its maximum student limit.
- **Duplicate Registration:** Attempting to register two students with the same ID.
- **State Reloading:** Modifying records, saving, terminating the application, and confirming that reload recovers the exact state.
