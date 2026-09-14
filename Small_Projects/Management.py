# Student Management System

students =[]
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    
    students.append({
        "name" : name,
        "age" : age
    })
    print("Student added successfully!")
    
def view_students():
    if len(students) ==0:
        print("No student found.")
    else:
        print("\nStudents List:")
        for Student in students:
            print("Name:" , Student["name"])
            print("Age:" , Student["age"])

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")