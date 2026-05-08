from data.storage import search_student_by_name

def search_student(name):
    results = search_student_by_name(name)
    
    if not results:
        print(f"\nNo student found with name: {name}")
        return None
    
    print(f"\n===== Search Results for '{name}' =====")
    for idx, student in enumerate(results, 1):
        print(f"\n{idx}. Name: {student['name']}")
        print(f"   Math: {student['math']}")
        print(f"   Science: {student['science']}")
        print(f"   English: {student['english']}")
    
    return results