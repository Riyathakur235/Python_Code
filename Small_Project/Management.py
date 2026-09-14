# Student Management System

students =[]
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    
    students.append({
        "name" : name,
        "age" : age
    })
    print("Student ")