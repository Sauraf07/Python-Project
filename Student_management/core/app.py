from utils.menu import show_menu
from utils.validator import validate_marks
from model.student import Student
from data.storage import save_student, get_all_students
from services.calculate import calculate_result
from services.search import search_student
from services.report import generate_report

def add_student():
    try:
        print("\n===== Add New Student =====")
        name = input("Enter student name: ").strip()
        
        if not name:
            print("Name cannot be empty!")
            return
        
        while True:
            try:
                math = int(input("Enter Math marks (0-100): "))
                if not validate_marks(math):
                    print("Marks must be between 0 and 100!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        while True:
            try:
                science = int(input("Enter Science marks (0-100): "))
                if not validate_marks(science):
                    print("Marks must be between 0 and 100!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        while True:
            try:
                english = int(input("Enter English marks (0-100): "))
                if not validate_marks(english):
                    print("Marks must be between 0 and 100!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        student = Student(name, math, science, english)
        data = student.to_dict()
        save_student(data)
        
        total, average, grade = calculate_result(math, science, english)
        print(f"\nStudent added successfully!")
        print(f"Total: {total}, Average: {average}, Grade: {grade}")
        
    except Exception as e:
        print(f"Error adding student: {e}")

def view_students():
    try:
        students = get_all_students()
        
        if not students:
            print("\nNo students found in the system.")
            return
        
        print("\n===== ALL STUDENTS =====")
        print(f"{'No.':<5} {'Name':<20} {'Math':<8} {'Science':<10} {'English':<10}")
        print("-" * 60)
        
        for idx, student in enumerate(students, 1):
            print(f"{idx:<5} {student['name']:<20} {student['math']:<8} {student['science']:<10} {student['english']:<10}")
        
    except Exception as e:
        print(f"Error viewing students: {e}")

def run():
    while True:
        show_menu()
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            add_student()
        
        elif choice == "2":
            view_students()
        
        elif choice == "3":
            name = input("Enter student name to search: ").strip()
            if name:
                search_student(name)
            else:
                print("Please enter a valid name!")
        
        elif choice == "4":
            print("\nThank you for using Student Management System!")
            print("Exiting...")
            break
        
        elif choice == "5":
            generate_report()
        
        else:
            print("Invalid choice! Please select a valid option.")