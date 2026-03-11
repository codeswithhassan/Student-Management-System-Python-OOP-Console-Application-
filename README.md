<div align="center">

# 🎓 Student Management System

### A Console-Based Application Built with Python & OOP

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OOP](https://img.shields.io/badge/Paradigm-OOP-FF6B6B?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22C55E?style=for-the-badge)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-6366F1?style=for-the-badge)]()

<br/>

> A fully-featured, terminal-based student record management system using clean Object-Oriented Programming principles — no external libraries, no database required.

<br/>

[![Demo Banner](https://drive.google.com/file/d/1fGnyPbkBOPxv2gVtF3RKSQw0fCHjfY-B/view?usp=sharing)]()

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Project Structure](#-project-structure)
- [Class Architecture](#-class-architecture)
- [OOP Concepts Used](#-oop-concepts-used)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [Data Model](#-data-model)
- [Grading System](#-grading-system)
- [Technologies](#-technologies)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

The **Student Management System** is a console-based CRUD application developed entirely in Python using Object-Oriented Programming (OOP). It allows users to manage student academic records — including personal details and subject-wise marks — through an intuitive menu-driven interface.

Designed as a portfolio project, this system demonstrates the practical application of OOP principles such as encapsulation, abstraction, and separation of concerns through a layered architecture (Model → Repository → Controller → View).

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Add Student** | Register new students with roll number validation and full marks entry |
| 📋 **View All Students** | Tabular display of all students sorted by roll number |
| 🔍 **Search** | Find students by roll number, partial name match, or grade filter |
| ✏️ **Update Records** | Selectively update name, age, email, or individual / all subject marks |
| 🗑️ **Delete Student** | Remove records with a confirmation prompt to prevent accidents |
| 📊 **Class Statistics** | Overview of averages, pass/fail ratios, grade distribution, and top performers |
| 🎨 **Coloured Terminal UI** | ANSI-coloured output with visual progress bars and formatted tables |
| 🔒 **Input Validation** | Every input is validated with re-prompt loops — no crashes from bad data |
| 📦 **Demo Data Seeded** | 5 sample students pre-loaded on startup for immediate exploration |

---

## 🎬 Demo

```
  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║     ███████╗███╗   ███╗███████╗                      ║
  ║     ██╔════╝████╗ ████║██╔════╝                      ║
  ║     ███████╗██╔████╔██║███████╗                      ║
  ║     ╚════██║██║╚██╔╝██║╚════██║                      ║
  ║     ███████║██║ ╚═╝ ██║███████║                      ║
  ║     ╚══════╝╚═╝     ╚═╝╚══════╝                      ║
  ║                                                      ║
  ║        Student Management System  v1.0.0             ║
  ║        Python OOP Console Application                ║
  ╚══════════════════════════════════════════════════════╝

  ┌─────────────────────────────────┐
  │           MAIN  MENU            │
  ├─────────────────────────────────┤
  │  1. Add Student                 │
  │  2. View All Students           │
  │  3. Search Student              │
  │  4. Update Student Record       │
  │  5. Delete Student              │
  │  6. Class Statistics            │
  │  7. Exit                        │
  └─────────────────────────────────┘

  Records in system: 5
```

### Student Card Preview
```
  ╔──────────────────────────────────────────────────────╗
  ║                   STUDENT RECORD                     ║
  ╠──────────────────────────────────────────────────────╣
  ║  Roll Number        S001                             ║
  ║  Name               Alice Johnson                   ║
  ║  Age                20                              ║
  ║  Email              alice@example.com               ║
  ╠──────────────────────────────────────────────────────╣
  ║                      MARKS                          ║
  ╠──────────────────────────────────────────────────────╣
  ║  Mathematics        [██████████████████░░]  92/100  ║
  ║  Science            [█████████████████░░░]  88/100  ║
  ║  English            [███████████████████░]  95/100  ║
  ║  History            [█████████████████░░░]  87/100  ║
  ║  Computer Science   [███████████████████░]  96/100  ║
  ╠──────────────────────────────────────────────────────╣
  ║  Total Marks        458.0                           ║
  ║  Average            91.60                           ║
  ║  Grade              A+                              ║
  ╚──────────────────────────────────────────────────────╝
```

---

## 📁 Project Structure

```
student-management-system/
│
├── student_management_system.py   # Main application (single file)
├── README.md                      # Project documentation
└── LICENSE                        # MIT License
```

> The entire system is intentionally contained in a single `.py` file for simplicity and portability — no setup, no dependencies.

---

## 🏗️ Class Architecture

The project is structured into **6 classes** following a clean layered design pattern:

```
┌─────────────────────────────────────────────────────────┐
│                  StudentManagementApp                   │  ← UI / Entry Point
│          (Main loop, banner, menu, seed data)           │
└─────────────────────────┬───────────────────────────────┘
                          │ uses
┌─────────────────────────▼───────────────────────────────┐
│                  StudentController                      │  ← Business Logic
│    (Add, View, Search, Update, Delete, Statistics)      │
└──────────┬──────────────────────────┬───────────────────┘
           │ uses                     │ uses
┌──────────▼───────────┐  ┌──────────▼───────────────────┐
│  StudentRepository   │  │       InputValidator          │  ← Data / Utility
│  (CRUD, Search,      │  │  (Validated typed input       │
│   Stats, Storage)    │  │   with re-prompt loops)       │
└──────────┬───────────┘  └───────────────────────────────┘
           │ stores
┌──────────▼───────────┐
│       Student        │  ← Entity / Model
│  (Fields, computed   │
│   properties, grade, │
│   display methods)   │
└──────────────────────┘

           ┌──────────────────┐
           │      Color       │  ← Utility / Helper
           │  (ANSI terminal  │
           │   colour codes)  │
           └──────────────────┘
```

### Class Descriptions

#### `Student` — Entity Model
The core data class representing a single student record.

```python
class Student:
    # Fields
    roll_number: str        # Unique identifier (e.g. "S001")
    name:        str        # Student's full name
    age:         int        # Age (5–100)
    email:       str        # Email address
    marks:       dict       # {subject: score} dictionary
    created_at:  str        # Timestamp of record creation

    # Computed Properties
    @property total_marks    -> float   # Sum of all subject marks
    @property average_marks  -> float   # Mean across subjects
    @property grade          -> str     # Letter grade (A+ to F)
    @property status         -> str     # "PASS" or "FAIL"

    # Display Methods
    def display_card()       # Full formatted student card with progress bars
    def summary_row()        # Single-line summary for table view
```

#### `StudentRepository` — Data Layer
Manages the in-memory collection of `Student` objects using a dictionary keyed by roll number.

```python
class StudentRepository:
    _records: dict[str, Student]   # Internal storage

    # CRUD
    def add(student)               -> bool
    def get_by_roll(roll_number)   -> Student | None
    def get_all()                  -> list[Student]
    def update(roll_number, **kw)  -> bool
    def delete(roll_number)        -> bool

    # Search
    def search_by_name(query)      -> list[Student]
    def search_by_grade(grade)     -> list[Student]

    # Statistics
    def count()                    -> int
    def top_students(n)            -> list[Student]
    def class_average()            -> float
    def exists(roll_number)        -> bool
```

#### `InputValidator` — Utility
A collection of static methods providing safe, validated console input. All methods re-prompt the user until valid data is entered.

```python
class InputValidator:
    @staticmethod get_string(prompt, min_len, max_len)   -> str
    @staticmethod get_int(prompt, low, high)             -> int
    @staticmethod get_float(prompt, low, high)           -> float
    @staticmethod get_email(prompt)                      -> str
    @staticmethod get_roll_number(prompt)                -> str
    @staticmethod confirm(prompt)                        -> bool
```

#### `StudentController` — Business Logic
Orchestrates user-facing operations by combining the repository and validator. Each public method corresponds to a menu option.

```python
class StudentController:
    def add_student()        # Guided form to register a new student
    def view_all_students()  # Sorted table of all records + summary stats
    def search_student()     # Multi-mode search (roll / name / grade)
    def update_student()     # Selective field/marks editor
    def delete_student()     # Confirmed removal
    def show_statistics()    # Class-wide performance dashboard
```

#### `StudentManagementApp` — UI / Entry Point
Owns the main run loop, renders the banner and menu, and seeds demo data on startup.

```python
class StudentManagementApp:
    def run()                # Main event loop
    def _print_banner()      # ASCII art header
    def _print_menu()        # Numbered menu display
    def _seed_demo_data()    # Pre-loads 5 sample students
```

#### `Color` — Terminal Helper
Provides ANSI escape-code helpers for coloured console output.

```python
class Color:
    @classmethod bold(text)     # Bold white
    @classmethod success(text)  # Green
    @classmethod error(text)    # Red
    @classmethod warning(text)  # Yellow
    @classmethod info(text)     # Cyan
    @classmethod header(text)   # Magenta + Bold
```

---

## 🧠 OOP Concepts Used

| Concept | Where Applied |
|---|---|
| **Classes & Objects** | Every module of the app (Student, Repository, Controller, etc.) is a class |
| **Encapsulation** | `StudentRepository._records` is private; accessed only through methods |
| **Abstraction** | `StudentController` hides all data logic from the UI layer |
| **Properties** | `@property` decorators for `grade`, `average_marks`, `total_marks`, `status` in `Student` |
| **Static Methods** | `InputValidator` uses `@staticmethod` for utility functions without needing instance state |
| **Separation of Concerns** | Each class has one clear responsibility (Model / Repo / Controller / UI) |
| **Composition** | `StudentManagementApp` composes `StudentRepository` and `StudentController` |
| **Data Hiding** | Internal storage `_records` uses Python naming convention for private attributes |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10 or higher** (uses `str | None` union type hints)
- No external packages required — uses Python standard library only

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/codeswithhassan/Student-Management-System-Python-OOP-Console-Application-
cd student-management-system
```

**2. Verify Python version**
```bash
python3 --version
# Expected: Python 3.10.x or higher
```

**3. Run the application**
```bash
python3 student_management_system.py
```

That's it — no `pip install`, no virtual environment, no config files needed.

---

## 📖 Usage Guide

### Main Menu Navigation
Enter the number corresponding to the desired operation and press **Enter**.

---

### 1️⃣ Add Student
```
Roll Number : S006
Full Name   : John Doe
Age         : 21
Email       : john@example.com

Enter marks for each subject (0–100):
  Mathematics              : 85
  Science                  : 78
  English                  : 90
  History                  : 72
  Computer Science         : 88
```
- Roll numbers are **automatically uppercased** (e.g. `s006` → `S006`)
- Duplicate roll numbers are **rejected** with an error message
- Invalid email formats are re-prompted until correct

---

### 2️⃣ View All Students
Displays a compact table of all students sorted alphabetically by roll number, along with the total record count and class average.

```
  #    Roll No    Name                   Age   Average   Grade
  ────────────────────────────────────────────────────────────
  1    S001       Alice Johnson          20    91.60     A+
  2    S002       Bob Martinez           22    71.80     B
  3    S003       Clara Williams         19    57.40     D
  ...

  Total Students : 5
  Class Average  : 74.16
```

---

### 3️⃣ Search Student
Three search modes are available:

| Mode | Input | Example |
|---|---|---|
| **Roll Number** | Exact match | `S001` |
| **Name** | Partial, case-insensitive | `alice` matches "Alice Johnson" |
| **Grade** | Letter grade | `A+`, `B`, `F` |

---

### 4️⃣ Update Student Record
After entering a roll number, choose what to edit:

```
  1. Name
  2. Age
  3. Email
  4. Marks (one subject)
  5. All Marks
  6. Cancel
```
The updated student card is displayed after every successful edit.

---

### 5️⃣ Delete Student
```
  About to delete: Alice Johnson (S001)
  Are you sure? (y/n): y
  ✓ Student 'S001' deleted.
```
Deletion requires explicit `y` confirmation — entering `n` or anything else cancels the operation.

---

### 6️⃣ Class Statistics
```
  Total Students                 5
  Class Average                  74.16%
  Passing Students               4 (80.0%)
  Failing Students               1 (20.0%)

  Grade Distribution:
    A+   ████                 1 students (20.0%)
    A    ████                 1 students (20.0%)
    B    ████                 1 students (20.0%)
    D    ████                 1 students (20.0%)
    F    ████                 1 students (20.0%)

  Top 3 Students:
    1. Alice Johnson          91.60% [A+]
    2. Eva Brown              87.20% [A]
    3. Bob Martinez           71.80% [B]
```

---

## 🗂️ Data Model

Each student record stores the following fields:

| Field | Type | Validation | Example |
|---|---|---|---|
| `roll_number` | `str` | 3–10 alphanumeric chars | `S001` |
| `name` | `str` | 2–60 chars, title-cased | `Alice Johnson` |
| `age` | `int` | 5–100 | `20` |
| `email` | `str` | Valid email regex | `alice@example.com` |
| `marks` | `dict` | Keys: 5 subjects, values: 0–100 | `{"Mathematics": 92, ...}` |
| `created_at` | `str` | Auto-generated timestamp | `2025-03-11 14:30:00` |

**Subjects tracked:**
- Mathematics
- Science
- English
- History
- Computer Science

---

## 📊 Grading System

| Average Marks | Grade | Status |
|:---:|:---:|:---:|
| 90 – 100 | A+ | ✅ PASS |
| 80 – 89  | A  | ✅ PASS |
| 70 – 79  | B  | ✅ PASS |
| 60 – 69  | C  | ✅ PASS |
| 50 – 59  | D  | ✅ PASS |
| 0 – 49   | F  | ❌ FAIL |

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core programming language |
| **OOP (Classes & Objects)** | Application architecture |
| **`@property` decorators** | Computed attributes (grade, average, total) |
| **`@staticmethod`** | Stateless utility methods in `InputValidator` |
| **`re` module** | Email and roll number regex validation |
| **`os` module** | Cross-platform terminal clear (`cls` / `clear`) |
| **`datetime` module** | Record creation timestamps |
| **ANSI Escape Codes** | Terminal colour output |
| **Python `dict`** | O(1) roll-number-keyed student storage |

---

## 🔮 Possible Future Enhancements

- [ ] File persistence using `json` or `csv` for data saving across sessions
- [ ] `sqlite3` database integration for scalable storage
- [ ] Export reports to `.csv` or `.pdf`
- [ ] Additional subjects configurable at runtime
- [ ] Password-protected admin mode
- [ ] Pagination for large student lists
- [ ] Unit tests using `unittest` or `pytest`

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a **Pull Request**

Please keep code style consistent with the existing OOP structure.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License  |  Copyright (c) 2025  |  Free to use, modify, and distribute
```

---

<div align="center">

Made with ❤️ using Python

⭐ **If you found this project helpful, please give it a star!** ⭐

</div>
