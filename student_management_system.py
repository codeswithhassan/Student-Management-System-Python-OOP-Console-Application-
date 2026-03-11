"""
=============================================================
  Student Management System
  Console-Based Application using Python OOP
=============================================================
"""

import os
import re
from datetime import datetime


# ─────────────────────────────────────────────
#  Helper: terminal colours (cross-platform)
# ─────────────────────────────────────────────
class Color:
    HEADER   = "\033[95m"
    BLUE     = "\033[94m"
    CYAN     = "\033[96m"
    GREEN    = "\033[92m"
    YELLOW   = "\033[93m"
    RED      = "\033[91m"
    BOLD     = "\033[1m"
    UNDERLINE= "\033[4m"
    RESET    = "\033[0m"

    @classmethod
    def bold(cls, text):        return f"{cls.BOLD}{text}{cls.RESET}"
    @classmethod
    def success(cls, text):     return f"{cls.GREEN}{text}{cls.RESET}"
    @classmethod
    def error(cls, text):       return f"{cls.RED}{text}{cls.RESET}"
    @classmethod
    def warning(cls, text):     return f"{cls.YELLOW}{text}{cls.RESET}"
    @classmethod
    def info(cls, text):        return f"{cls.CYAN}{text}{cls.RESET}"
    @classmethod
    def header(cls, text):      return f"{cls.HEADER}{cls.BOLD}{text}{cls.RESET}"


# ─────────────────────────────────────────────
#  Student  (Entity / Model)
# ─────────────────────────────────────────────
class Student:
    """Represents a single student record."""

    SUBJECTS = ["Mathematics", "Science", "English", "History", "Computer Science"]

    def __init__(self, roll_number: str, name: str, age: int,
                 email: str, marks: dict):
        self.roll_number  = roll_number.upper().strip()
        self.name         = name.strip().title()
        self.age          = age
        self.email        = email.strip().lower()
        self.marks        = marks          # {subject: score}
        self.created_at   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ── computed properties ──────────────────
    @property
    def total_marks(self) -> float:
        return sum(self.marks.values())

    @property
    def average_marks(self) -> float:
        if not self.marks:
            return 0.0
        return self.total_marks / len(self.marks)

    @property
    def grade(self) -> str:
        avg = self.average_marks
        if avg >= 90:  return "A+"
        if avg >= 80:  return "A"
        if avg >= 70:  return "B"
        if avg >= 60:  return "C"
        if avg >= 50:  return "D"
        return "F"

    @property
    def status(self) -> str:
        return Color.success("PASS") if self.average_marks >= 50 else Color.error("FAIL")

    # ── display ──────────────────────────────
    def display_card(self):
        w = 54
        bar = "─" * w
        print(f"\n  ╔{bar}╗")
        print(f"  ║{'STUDENT RECORD':^{w}}║")
        print(f"  ╠{bar}╣")
        print(f"  ║  {'Roll Number':<20} {self.roll_number:<{w-23}}║")
        print(f"  ║  {'Name':<20} {self.name:<{w-23}}║")
        print(f"  ║  {'Age':<20} {self.age:<{w-23}}║")
        print(f"  ║  {'Email':<20} {self.email:<{w-23}}║")
        print(f"  ╠{bar}╣")
        print(f"  ║{'MARKS':^{w}}║")
        print(f"  ╠{bar}╣")
        for subject, score in self.marks.items():
            bar_fill  = int(score / 5)          # 0-20 chars
            bar_empty = 20 - bar_fill
            vis = f"[{'█' * bar_fill}{'░' * bar_empty}] {score:>3}/100"
            print(f"  ║  {subject:<20} {vis:<{w-23}}║")
        print(f"  ╠{bar}╣")
        print(f"  ║  {'Total Marks':<20} {self.total_marks:<{w-23}.1f}║")
        print(f"  ║  {'Average':<20} {self.average_marks:<{w-23}.2f}║")
        print(f"  ║  {'Grade':<20} {self.grade:<{w-23}}║")
        print(f"  ║  {'Created At':<20} {self.created_at:<{w-23}}║")
        print(f"  ╚{bar}╝")

    def summary_row(self, index: int) -> str:
        return (f"  {index:<4} {self.roll_number:<10} {self.name:<22}"
                f" {self.age:<5} {self.average_marks:<9.2f} {self.grade:<6}")

    def __repr__(self):
        return f"Student(roll={self.roll_number}, name={self.name})"


# ─────────────────────────────────────────────
#  StudentRepository  (Data Layer / Storage)
# ─────────────────────────────────────────────
class StudentRepository:
    """Stores and manages the collection of Student objects."""

    def __init__(self):
        self._records: dict[str, Student] = {}   # roll_number → Student

    # ── CRUD ─────────────────────────────────
    def add(self, student: Student) -> bool:
        if student.roll_number in self._records:
            return False
        self._records[student.roll_number] = student
        return True

    def get_by_roll(self, roll_number: str) -> Student | None:
        return self._records.get(roll_number.upper().strip())

    def get_all(self) -> list[Student]:
        return list(self._records.values())

    def update(self, roll_number: str, **kwargs) -> bool:
        student = self.get_by_roll(roll_number)
        if not student:
            return False
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        return True

    def delete(self, roll_number: str) -> bool:
        roll = roll_number.upper().strip()
        if roll not in self._records:
            return False
        del self._records[roll]
        return True

    # ── search ───────────────────────────────
    def search_by_name(self, query: str) -> list[Student]:
        q = query.lower()
        return [s for s in self._records.values() if q in s.name.lower()]

    def search_by_grade(self, grade: str) -> list[Student]:
        return [s for s in self._records.values()
                if s.grade.upper() == grade.upper()]

    # ── stats ────────────────────────────────
    def count(self) -> int:
        return len(self._records)

    def top_students(self, n: int = 3) -> list[Student]:
        return sorted(self._records.values(),
                      key=lambda s: s.average_marks, reverse=True)[:n]

    def class_average(self) -> float:
        students = self.get_all()
        if not students:
            return 0.0
        return sum(s.average_marks for s in students) / len(students)

    def exists(self, roll_number: str) -> bool:
        return roll_number.upper().strip() in self._records


# ─────────────────────────────────────────────
#  InputValidator  (Utility)
# ─────────────────────────────────────────────
class InputValidator:
    """Static helpers for validated console input."""

    @staticmethod
    def get_string(prompt: str, min_len: int = 1, max_len: int = 100) -> str:
        while True:
            value = input(prompt).strip()
            if min_len <= len(value) <= max_len:
                return value
            print(Color.error(f"  ✗ Must be {min_len}–{max_len} characters."))

    @staticmethod
    def get_int(prompt: str, low: int, high: int) -> int:
        while True:
            try:
                value = int(input(prompt))
                if low <= value <= high:
                    return value
                print(Color.error(f"  ✗ Enter a number between {low} and {high}."))
            except ValueError:
                print(Color.error("  ✗ Invalid number."))

    @staticmethod
    def get_float(prompt: str, low: float, high: float) -> float:
        while True:
            try:
                value = float(input(prompt))
                if low <= value <= high:
                    return value
                print(Color.error(f"  ✗ Enter a value between {low} and {high}."))
            except ValueError:
                print(Color.error("  ✗ Invalid number."))

    @staticmethod
    def get_email(prompt: str) -> str:
        pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")
        while True:
            value = input(prompt).strip()
            if pattern.match(value):
                return value
            print(Color.error("  ✗ Invalid email format."))

    @staticmethod
    def get_roll_number(prompt: str) -> str:
        while True:
            value = input(prompt).strip().upper()
            if re.match(r"^[A-Z0-9]{3,10}$", value):
                return value
            print(Color.error("  ✗ Roll number must be 3-10 alphanumeric characters."))

    @staticmethod
    def confirm(prompt: str) -> bool:
        while True:
            choice = input(f"{prompt} (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                return True
            if choice in ("n", "no"):
                return False
            print(Color.error("  ✗ Enter 'y' or 'n'."))


# ─────────────────────────────────────────────
#  StudentController  (Business Logic)
# ─────────────────────────────────────────────
class StudentController:
    """Bridges the UI with the repository; handles all operations."""

    def __init__(self, repo: StudentRepository):
        self.repo      = repo
        self.validator = InputValidator()

    # ── Add ──────────────────────────────────
    def add_student(self):
        self._section_header("ADD NEW STUDENT")

        roll = self.validator.get_roll_number("  Roll Number : ")
        if self.repo.exists(roll):
            print(Color.error(f"\n  ✗ Roll number '{roll}' already exists."))
            return

        name  = self.validator.get_string("  Full Name    : ", 2, 60)
        age   = self.validator.get_int(   "  Age          : ", 5, 100)
        email = self.validator.get_email( "  Email        : ")

        print(Color.info("\n  Enter marks for each subject (0–100):"))
        marks = {}
        for subject in Student.SUBJECTS:
            score = self.validator.get_float(f"    {subject:<25}: ", 0, 100)
            marks[subject] = score

        student = Student(roll, name, age, email, marks)
        self.repo.add(student)
        print(Color.success(f"\n  ✓ Student '{name}' added successfully!"))
        student.display_card()

    # ── View All ─────────────────────────────
    def view_all_students(self):
        self._section_header("ALL STUDENT RECORDS")
        students = self.repo.get_all()

        if not students:
            print(Color.warning("  No students found in the system."))
            return

        header = (f"  {'#':<4} {'Roll No':<10} {'Name':<22}"
                  f" {'Age':<5} {'Average':<9} {'Grade':<6}")
        divider = "  " + "─" * 60
        print(Color.bold(header))
        print(divider)

        for i, student in enumerate(
                sorted(students, key=lambda s: s.roll_number), 1):
            print(student.summary_row(i))

        print(divider)
        print(Color.info(f"\n  Total Students : {self.repo.count()}"))
        print(Color.info(f"  Class Average  : {self.repo.class_average():.2f}"))

    # ── Search ───────────────────────────────
    def search_student(self):
        self._section_header("SEARCH STUDENT")
        print("  Search by:")
        print("   1. Roll Number")
        print("   2. Name")
        print("   3. Grade")
        choice = self.validator.get_int("  Select [1-3] : ", 1, 3)

        if choice == 1:
            roll    = self.validator.get_roll_number("  Roll Number : ")
            student = self.repo.get_by_roll(roll)
            if student:
                student.display_card()
            else:
                print(Color.error(f"\n  ✗ No student with roll number '{roll}'."))

        elif choice == 2:
            query   = self.validator.get_string("  Name query  : ", 1, 60)
            results = self.repo.search_by_name(query)
            if results:
                print(Color.success(f"\n  Found {len(results)} result(s):"))
                for s in results:
                    s.display_card()
            else:
                print(Color.error(f"\n  ✗ No students matching '{query}'."))

        else:
            grade   = self.validator.get_string("  Grade (A+/A/B/C/D/F) : ", 1, 2)
            results = self.repo.search_by_grade(grade)
            if results:
                print(Color.success(f"\n  Found {len(results)} student(s) with grade '{grade.upper()}':"))
                for s in results:
                    print(f"    • {s.roll_number} – {s.name} ({s.average_marks:.2f}%)")
            else:
                print(Color.error(f"\n  ✗ No students with grade '{grade.upper()}'."))

    # ── Update ───────────────────────────────
    def update_student(self):
        self._section_header("UPDATE STUDENT RECORD")

        roll    = self.validator.get_roll_number("  Roll Number : ")
        student = self.repo.get_by_roll(roll)
        if not student:
            print(Color.error(f"\n  ✗ Student '{roll}' not found."))
            return

        print(Color.info(f"\n  Editing: {student.name} ({student.roll_number})"))
        print("  What would you like to update?")
        print("   1. Name")
        print("   2. Age")
        print("   3. Email")
        print("   4. Marks (one subject)")
        print("   5. All Marks")
        print("   6. Cancel")

        choice = self.validator.get_int("  Select [1-6] : ", 1, 6)

        if choice == 1:
            new_name     = self.validator.get_string("  New Name  : ", 2, 60)
            student.name = new_name.title()
            print(Color.success("  ✓ Name updated."))

        elif choice == 2:
            student.age = self.validator.get_int("  New Age   : ", 5, 100)
            print(Color.success("  ✓ Age updated."))

        elif choice == 3:
            student.email = self.validator.get_email("  New Email : ")
            print(Color.success("  ✓ Email updated."))

        elif choice == 4:
            print(Color.info("\n  Subjects:"))
            subjects = list(Student.SUBJECTS)
            for i, sub in enumerate(subjects, 1):
                print(f"   {i}. {sub} (current: {student.marks.get(sub, 0):.1f})")
            idx   = self.validator.get_int("  Subject # : ", 1, len(subjects))
            subj  = subjects[idx - 1]
            score = self.validator.get_float(
                        f"  New marks for {subj}: ", 0, 100)
            student.marks[subj] = score
            print(Color.success(f"  ✓ Marks for '{subj}' updated."))

        elif choice == 5:
            print(Color.info("\n  Enter new marks for all subjects:"))
            for subject in Student.SUBJECTS:
                score = self.validator.get_float(
                            f"    {subject:<25}: ", 0, 100)
                student.marks[subject] = score
            print(Color.success("  ✓ All marks updated."))

        else:
            print(Color.warning("  Update cancelled."))
            return

        if choice != 6:
            student.display_card()

    # ── Delete ───────────────────────────────
    def delete_student(self):
        self._section_header("DELETE STUDENT RECORD")

        roll    = self.validator.get_roll_number("  Roll Number : ")
        student = self.repo.get_by_roll(roll)
        if not student:
            print(Color.error(f"\n  ✗ Student '{roll}' not found."))
            return

        print(Color.warning(f"\n  About to delete: {student.name} ({student.roll_number})"))
        if self.validator.confirm("  Are you sure?"):
            self.repo.delete(roll)
            print(Color.success(f"  ✓ Student '{roll}' deleted."))
        else:
            print(Color.info("  Deletion cancelled."))

    # ── Statistics ───────────────────────────
    def show_statistics(self):
        self._section_header("CLASS STATISTICS")
        students = self.repo.get_all()

        if not students:
            print(Color.warning("  No data available."))
            return

        total    = self.repo.count()
        avg      = self.repo.class_average()
        passing  = sum(1 for s in students if s.average_marks >= 50)
        failing  = total - passing

        grade_counts = {}
        for s in students:
            grade_counts[s.grade] = grade_counts.get(s.grade, 0) + 1

        top      = self.repo.top_students(3)
        highest  = max(students, key=lambda s: s.average_marks)
        lowest   = min(students, key=lambda s: s.average_marks)

        print(f"  {'Total Students':<30} {total}")
        print(f"  {'Class Average':<30} {avg:.2f}%")
        print(f"  {'Passing Students':<30} {passing} ({passing/total*100:.1f}%)")
        print(f"  {'Failing Students':<30} {failing} ({failing/total*100:.1f}%)")

        print(Color.bold("\n  Grade Distribution:"))
        for grade in ["A+", "A", "B", "C", "D", "F"]:
            count    = grade_counts.get(grade, 0)
            pct      = count / total * 100
            bar      = "█" * int(pct / 5)
            print(f"    {grade:<4} {bar:<20} {count:>3} students ({pct:.1f}%)")

        print(Color.bold("\n  Top 3 Students:"))
        for i, s in enumerate(top, 1):
            print(f"    {i}. {s.name:<22} {s.average_marks:.2f}% [{s.grade}]")

        print(Color.bold("\n  Highest Scorer:"))
        print(f"    {highest.name} — {highest.average_marks:.2f}% [{highest.grade}]")
        print(Color.bold("  Lowest Scorer:"))
        print(f"    {lowest.name} — {lowest.average_marks:.2f}% [{lowest.grade}]")

    # ── private helper ───────────────────────
    @staticmethod
    def _section_header(title: str):
        width = 58
        print(f"\n  {'═' * width}")
        print(f"  {'  ' + title}")
        print(f"  {'═' * width}")


# ─────────────────────────────────────────────
#  StudentManagementApp  (UI / Entry Point)
# ─────────────────────────────────────────────
class StudentManagementApp:
    """Main console application."""

    VERSION = "1.0.0"

    def __init__(self):
        self.repo       = StudentRepository()
        self.controller = StudentController(self.repo)
        self._seed_demo_data()

    # ── bootstrap with sample data ───────────
    def _seed_demo_data(self):
        samples = [
            ("S001", "Alice Johnson",  20, "alice@example.com",
             {"Mathematics": 92, "Science": 88, "English": 95,
              "History": 87, "Computer Science": 96}),
            ("S002", "Bob Martinez",   22, "bob@example.com",
             {"Mathematics": 74, "Science": 68, "English": 72,
              "History": 65, "Computer Science": 80}),
            ("S003", "Clara Williams", 19, "clara@example.com",
             {"Mathematics": 55, "Science": 60, "English": 58,
              "History": 52, "Computer Science": 62}),
            ("S004", "David Lee",      21, "david@example.com",
             {"Mathematics": 40, "Science": 45, "English": 38,
              "History": 42, "Computer Science": 50}),
            ("S005", "Eva Brown",      20, "eva@example.com",
             {"Mathematics": 85, "Science": 90, "English": 82,
              "History": 88, "Computer Science": 91}),
        ]
        for roll, name, age, email, marks in samples:
            self.repo.add(Student(roll, name, age, email, marks))

    # ── banner ───────────────────────────────
    def _print_banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        banner = rf"""
  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║     ███████╗███╗   ███╗███████╗                      ║
  ║     ██╔════╝████╗ ████║██╔════╝                      ║
  ║     ███████╗██╔████╔██║███████╗                      ║
  ║     ╚════██║██║╚██╔╝██║╚════██║                      ║
  ║     ███████║██║ ╚═╝ ██║███████║                      ║
  ║     ╚══════╝╚═╝     ╚═╝╚══════╝                      ║
  ║                                                      ║
  ║        Student Management System  v{self.VERSION}           ║
  ║        Python OOP Console Application                ║
  ╚══════════════════════════════════════════════════════╝
"""
        print(Color.header(banner))

    # ── main menu ────────────────────────────
    def _print_menu(self):
        print(Color.bold("\n  ┌─────────────────────────────────┐"))
        print(Color.bold(  "  │           MAIN  MENU            │"))
        print(Color.bold(  "  ├─────────────────────────────────┤"))
        print(           f"  │  {Color.info('1.')} Add Student                   │")
        print(           f"  │  {Color.info('2.')} View All Students             │")
        print(           f"  │  {Color.info('3.')} Search Student                │")
        print(           f"  │  {Color.info('4.')} Update Student Record         │")
        print(           f"  │  {Color.info('5.')} Delete Student                │")
        print(           f"  │  {Color.info('6.')} Class Statistics              │")
        print(           f"  │  {Color.info('7.')} Exit                          │")
        print(Color.bold(  "  └─────────────────────────────────┘"))
        print(Color.info(f"\n  Records in system: {self.repo.count()}"))

    # ── run loop ─────────────────────────────
    def run(self):
        self._print_banner()

        menu_map = {
            "1": self.controller.add_student,
            "2": self.controller.view_all_students,
            "3": self.controller.search_student,
            "4": self.controller.update_student,
            "5": self.controller.delete_student,
            "6": self.controller.show_statistics,
        }

        while True:
            self._print_menu()
            choice = input("\n  Enter choice [1-7] : ").strip()

            if choice == "7":
                print(Color.success("\n  Thank you for using the Student Management System!"))
                print(Color.info("  Goodbye!\n"))
                break
            elif choice in menu_map:
                menu_map[choice]()
                input(Color.info("\n  Press Enter to continue..."))
            else:
                print(Color.error("  ✗ Invalid choice. Please enter 1–7."))


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = StudentManagementApp()
    app.run()