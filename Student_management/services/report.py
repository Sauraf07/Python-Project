from data.storage import get_all_students
from services.calculate import calculate_result

def generate_report():
    students = get_all_students()
    
    if not students:
        print("\nNo students in the system.")
        return
    
    print("\n===== STUDENT REPORT =====")
    print(f"{'Name':<20} {'Math':<8} {'Science':<10} {'English':<10} {'Total':<8} {'Average':<10} {'Grade':<8}")
    print("-" * 85)
    
    for student in students:
        total, average, grade = calculate_result(
            int(student['math']),
            int(student['science']),
            int(student['english'])
        )
        print(f"{student['name']:<20} {student['math']:<8} {student['science']:<10} {student['english']:<10} {total:<8} {average:<10} {grade:<8}")
    
    print("\nReport generated successfully!")