# Capstone B — Student Results Management System

> **Kilele Code Studio · Capstone Project 2**  
> *Structured Data Analytics, Ranking, and Academic Reporting*

---

## 🎯 Project Overview & Objectives

The **Student Results Management System** is a data-driven terminal application that records student marks across multiple academic disciplines, calculates weighted averages, assigns official grades, ranks cohort performance, and exports formatted report cards to disk.

### Core Objectives:
1. Model complex multi-student, multi-subject data using nested dictionaries and lists.
2. Implement statistical aggregations: class mean, median, standard grading scales, and class rankings.
3. Provide an interactive CRUD terminal menu (Create, Read, Update, Delete marks).
4. Persist data to disk using JSON and generate exportable `.csv` spreadsheets and `.txt` report cards.
5. Provide comprehensive error handling against missing subjects and non-numeric marks.

---

## 🧩 Required Python Concepts

- **Collections:** Nested dictionaries (`{student_id: {"name": ..., "marks": {...}}}`).
- **Loops & Comprehensions:** Iterating student records and computing subject aggregates.
- **Functions:** Modular decomposition (`calculate_average()`, `rank_students()`, `export_csv()`).
- **File I/O:** Reading and writing `.json`, `.csv`, and `.txt` files with `with open(...)`.
- **String Formatting:** Aligned tabular reports using f-strings (`{value:<15}`).

---

## 🚀 How to Run the Program

```bash
cd 05-capstone-projects/student-results-system
python3 main.py
```
*(Run with `--demo` for an automated test run)*

---

## 🧪 Testing Scenarios

- **Adding a Duplicate ID:** The system should reject adding an existing ID or prompt to update.
- **Negative or Excess Marks:** Marks must be strictly between 0 and 100.
- **Cohort Ranking Ties:** When two students have identical averages, they should share a rank cleanly.
- **File Export:** Verify that exported CSV files can be opened in spreadsheet applications (like LibreOffice Calc or Microsoft Excel).
