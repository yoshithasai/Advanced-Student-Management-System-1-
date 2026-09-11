# Advanced Student Management System

A simple command-line application for managing student records, built with Python using object-oriented programming principles (abstraction, inheritance, and encapsulation).

## Features

- **Add Student** – Register a new student with ID, name, age, and marks for 3 subjects.
- **View Students** – Display details of all registered students, including total and percentage.
- **Search Student** – Look up a student by their ID.
- **Delete Student** – Remove a student record by ID.
- **Show Date and Time** – Display the current system date and time.
- **Graduate Student Support** – A `GraduateStudent` subclass extends `Student` with a customized info display (currently defined but not yet wired into the menu).

## Requirements

- Python 3.x (no external libraries needed — uses only the built-in `datetime` and `abc` modules)

## How to Run

1. Save the script as `student_management.py`.
2. Run it from the terminal:
   ```bash
   python student_management.py
   ```
3. Follow the on-screen menu to add, view, search, or delete students.

## Menu Options

```
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Show Date and Time
6. Exit
```

## Code Structure

| Component | Description |
|---|---|
| `Person` (ABC) | Abstract base class defining common attributes (`name`, `age`) and an abstract `display_info()` method. |
| `Student` | Concrete class inheriting from `Person`; adds `student_id` and `marks`, and implements `display_info()` with total/percentage calculation. |
| `GraduateStudent` | Subclass of `Student` that overrides `display_info()` to add a "Level: Graduate" tag. |
| `students` | In-memory list storing all `Student` objects (data is **not persisted** between runs). |
| `add_student()` | Prompts for student details, validates marks (0–100) and unique ID, then adds to the list. |
| `view_students()` | Iterates through and prints all student records. |
| `search_student()` | Finds and displays a student by ID. |
| `delete_student()` | Removes a student by ID. |
| `show_date_time()` | Prints the current date and time. |
| `main()` | Runs the interactive menu loop. |

## Validation Rules

- Student ID and age must be valid integers.
- Marks must be numeric and fall between **0 and 100**.
- Student IDs must be unique — duplicate IDs are rejected when adding.

## Known Limitations / Notes

- **No data persistence**: all records are lost when the program exits (stored only in memory).
- **`GraduateStudent` is not yet used**: the `add_student()` function only ever creates instances of `Student`, so the graduate-specific display is currently unreachable from the menu.
- **Marks count is fixed at 3 subjects** per student.

## Possible Improvements

- Add file or database persistence (e.g., JSON, CSV, or SQLite).
- Add a menu option to register `GraduateStudent` records.
- Add an "Update Student" feature to edit existing records.
- Add input sanitization for names (e.g., reject empty strings).
