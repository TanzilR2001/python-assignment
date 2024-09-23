students = []

def add_student(student_id, name, grade):
    
    for student in students:
        if student['ID'] == student_id:
            print(f"Student with ID {student_id} already exists.")
            return
    
    new_student = {
        'ID': student_id,
        'Name': name,
        'Grade': grade
    }
    
    students.append(new_student)
    print(f"Student {name} added successfully.")

add_student(1, 'Akshay', 'O')
add_student(2, 'Biju', 'A')
add_student(1, 'Akib', 'A+')

print(students)