# 🎓 Student Grade Management System

A simple Python-based Student Grade Management System that allows users to add student records, store subject marks, calculate percentages and grades, search student records, and delete records.

Student data is stored permanently in a JSON file.

## ✨ Features

- Add new student records
- Enter marks for multiple subjects
- Automatically calculate total marks
- Automatically calculate percentage
- Automatically assign letter grades
- Display all student records
- Search students using Student ID / Roll No
- Delete student records
- Store data using a JSON file
- Validate user inputs
- Handle invalid or corrupted data files

## 🛠️ Technologies Used

- Python
- JSON
- File Handling
- Object-Oriented Programming (OOP)

## 📂 Project Structure

```text
student-grade-management-system/
```
## 📊 Grading System

The program calculates grades according to the following percentage:

| Percentage | Grade |
|------------|-------|
| 90% - 100% | A+ |
| 80% - 89% | A |
| 70% - 79% | B |
| 60% - 69% | C |
| 50% - 59% | D |
| Below 50% | F |

## 💻 How It Works

When the program starts, it provides a menu with five options:

1. Add New Student & Marks
2. Display All Student Records
3. Search Student by ID
4. Delete Student Record
5. Exit

### Add Student

The user enters:

- Student ID / Roll Number
- Student name
- Number of subjects
- Subject names
- Marks obtained in each subject

The system automatically calculates:

- Total marks
- Percentage
- Grade

The student record is then saved to `student_records.json`.

### Display Students

Displays all stored student records in a formatted table containing:

- Student ID
- Student Name
- Total Marks
- Percentage
- Grade

### Search Student

A student can be searched using their Student ID.

The program displays:

- Name
- Subject-wise marks
- Total marks
- Percentage
- Grade

### Delete Student

A student record can be deleted using the Student ID.

## 🗃️ Data Storage

Student records are stored in a JSON file:

```text
student_records.json
```
🚀 How to Run
1. Clone the repository
git clone https://github.com/your-username/student-grade-management-system.git
2. Open the project folder
cd student-grade-management-system
3. Run the program
python grade_manager.py

🖥️ Example
=== STUDENT GRADE MANAGEMENT SYSTEM ===
1. Add New Student & Marks
2. Display All Student Records
3. Search Student by ID
4. Delete Student Record
5. Exit

Enter your choice (1-5): 1

--- Add New Student ---

Enter Student ID / Roll No: 101
Enter Student Name: Ankita
Enter number of subjects: 3

Enter Subject 1 name: Python
Enter marks obtained in Python (out of 100): 85

Enter Subject 2 name: DBMS
Enter marks obtained in DBMS (out of 100): 90

Enter Subject 3 name: Java
Enter marks obtained in Java (out of 100): 80

[✓] Student 'Ankita' added successfully with Grade: A
🎯 Learning Objectives
This project helped me practice:
.Python classes and objects
.Object-Oriented Programming
.Functions and methods
.Dictionaries and lists
.Loops and conditional statements
.JSON data handling
.File handling
.Exception handling
.User input validation
.Basic data management

🔮 Future Improvements
Possible improvements for future versions:
•Add a graphical user interface (GUI)
•Add an option to update student records
•Add class/section information
•Add attendance management
•Generate printable student report cards
•Add sorting and filtering options
•Add database support using SQLite or MySQL

👩‍💻 Author
Ankita
├── grade_manager.py
├── student_records.json
└── README.md```
