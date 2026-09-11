from datetime import datetime
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def display_info(self):
        pass
class Student(Person):
    def __init__(self, student_id, name, age, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self._marks = marks
    def display_info(self):
        total = sum(self._marks)
        percentage = total / len(self._marks)
        print("\n----- Student Details -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self._marks)
        print("Total:", total)
        print("Percentage:", round(percentage, 2))
class GraduateStudent(Student):
    def display_info(self):
        total = sum(self._marks)
        percentage = total / len(self._marks)
        print("\n----- Graduate Student -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self._marks)
        print("Total:", total)
        print("Percentage:", round(percentage, 2))
        print("Level: Graduate")
students = []
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = []
        for i in range(3):
            mark = float(input(f"Enter marks for subject {i + 1}: "))
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(mark)
        for student in students:
            if student.student_id == student_id:
                print("Student ID already exists.")
                return
        student = Student(student_id, name, age, marks)
        students.append(student)
        print("Student added successfully!")
    except ValueError:
        print("Please enter valid numbers.")
def view_students():
    if len(students) == 0:
        print("No student records found.")
        return
    for student in students:
        student.display_info()
def search_student():
    try:
        student_id = int(input("Enter Student ID to search: "))
        for student in students:
            if student.student_id == student_id:
                student.display_info()
                return
        print("Student not found.")
    except ValueError:
        print("Invalid Student ID.")
def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: "))
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid Student ID.")
def show_date_time():
    current_time = datetime.now()
    print("Current Date and Time:", current_time)
def main():
    while True:
        print("\n==============================")
        print(" ADVANCED STUDENT MANAGEMENT ")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Show Date and Time")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_date_time()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")
main()