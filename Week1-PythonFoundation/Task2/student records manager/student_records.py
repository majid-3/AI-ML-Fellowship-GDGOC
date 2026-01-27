# This program manages student records using a list of dictionaries

students = []   # List to store student records


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\nStudent Records:")
    for student in students:
        print(
            "Name:", student["name"], "| Roll No:", student["roll_no"], "| Marks:", student["marks"])


def update_student():
    roll_no = input("Enter roll number to update: ")
    found = False

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ")
            student["marks"] = float(input("Enter new marks: "))
            print("Student record updated successfully!")
            found = True
            break

    if not found:
        print("Student not found.")


def menu():
    while True:
        print("Student Record System Menu")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")



menu()
