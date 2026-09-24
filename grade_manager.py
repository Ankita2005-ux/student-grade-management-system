import json
import os

DATA_FILE = "student_records.json"


class StudentGradeSystem:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        """Loads existing student data from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("[!] Warning: Could not read data file. Starting fresh.")
                return {}
        return {}

    def save_data(self):
        """Saves current student data to the JSON file."""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.students, file, indent=4)
        except IOError as e:
            print(f"[!] Error saving records: {e}")

    @staticmethod
    def calculate_grade(percentage):
        """Returns the letter grade based on percentage."""
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def add_student(self):
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID / Roll No: ").strip()
        if not student_id:
            print("[!] Student ID cannot be empty.")
            return

        if student_id in self.students:
            print(f"[!] Student with ID '{student_id}' already exists.")
            return

        name = input("Enter Student Name: ").strip()
        if not name:
            print("[!] Name cannot be empty.")
            return

        # Input subjects and marks
        marks = {}
        while True:
            try:
                subject_count = int(input("Enter number of subjects: "))
                if subject_count <= 0:
                    print("[!] Must enter at least 1 subject.")
                    continue
                break
            except ValueError:
                print("[!] Please enter a valid integer.")

        for i in range(1, subject_count + 1):
            sub_name = input(f"Enter Subject {i} name: ").strip()
            while True:
                try:
                    score = float(input(f"Enter marks obtained in {sub_name} (out of 100): "))
                    if 0 <= score <= 100:
                        marks[sub_name] = score
                        break
                    else:
                        print("[!] Marks must be between 0 and 100.")
                except ValueError:
                    print("[!] Please enter a valid numerical score.")

        # Calculations
        total_marks = sum(marks.values())
        percentage = round(total_marks / len(marks), 2)
        grade = self.calculate_grade(percentage)

        # Store in dictionary
        self.students[student_id] = {
            "name": name,
            "marks": marks,
            "total": total_marks,
            "percentage": percentage,
            "grade": grade,
        }

        self.save_data()
        print(f"\n[✓] Student '{name}' added successfully with Grade: {grade}")

    def display_all_students(self):
        print("\n" + "=" * 80)
        print(f"{'STUDENT GRADE REPORT':^80}")
        print("=" * 80)

        if not self.students:
            print("No student records found.")
            print("=" * 80)
            return

        header = f"{'ID':<10} | {'Name':<20} | {'Total':<10} | {'Percentage':<12} | {'Grade':<6}"
        print(header)
        print("-" * 80)

        for sid, details in self.students.items():
            print(
                f"{sid:<10} | {details['name']:<20} | {details['total']:<10.2f} | "
                f"{details['percentage']:<10.2f}% | {details['grade']:<6}"
            )
        print("=" * 80)

    def search_student(self):
        print("\n--- Search Student ---")
        student_id = input("Enter Student ID to search: ").strip()

        student = self.students.get(student_id)
        if not student:
            print(f"[!] No record found for ID: {student_id}")
            return

        print("\n" + "-" * 40)
        print(f"ID:         {student_id}")
        print(f"Name:       {student['name']}")
        print("Subject Breakdown:")
        for sub, score in student["marks"].items():
            print(f"  - {sub}: {score}/100")
        print(f"Total:      {student['total']:.2f}")
        print(f"Percentage: {student['percentage']:.2f}%")
        print(f"Grade:      {student['grade']}")
        print("-" * 40)

    def delete_student(self):
        print("\n--- Delete Student Record ---")
        student_id = input("Enter Student ID to delete: ").strip()

        if student_id in self.students:
            removed = self.students.pop(student_id)
            self.save_data()
            print(f"[✓] Record for '{removed['name']}' (ID: {student_id}) has been removed.")
        else:
            print(f"[!] Student ID '{student_id}' not found.")


def main():
    system = StudentGradeSystem()

    while True:
        print("\n=== STUDENT GRADE MANAGEMENT SYSTEM ===")
        print("1. Add New Student & Marks")
        print("2. Display All Student Records")
        print("3. Search Student by ID")
        print("4. Delete Student Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.display_all_students()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            system.delete_student()
        elif choice == "5":
            print("\nExiting program. All records are saved.")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()