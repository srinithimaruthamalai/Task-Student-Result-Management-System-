# Student Result Management System

students = []


def add_student():
    print("\n===== ADD STUDENT =====")

    name = input("Enter Student Name : ")
    roll_no = input("Enter Roll Number  : ")
    department = input("Enter Department   : ")

    python = int(input("Enter Python Mark  : "))
    english = int(input("Enter English Mark : "))
    maths = int(input("Enter Maths Mark   : "))

    total = python + english + maths
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if python >= 35 and english >= 35 and maths >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    student = {
        "name": name,
        "roll_no": roll_no,
        "department": department,
        "python": python,
        "english": english,
        "maths": maths,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


def display_students():
    print("\n===== ALL STUDENTS =====")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("--------------------------------")
        print("Name       :", student["name"])
        print("Roll No    :", student["roll_no"])
        print("Department :", student["department"])
        print("Total      :", student["total"])
        print("Average    :", round(student["average"], 2))
        print("Grade      :", student["grade"])
        print("Result     :", student["result"])
        print("--------------------------------")


def search_student():
    print("\n===== SEARCH STUDENT =====")

    roll_no = input("Enter Roll Number : ")

    found = False

    for student in students:
        if student["roll_no"] == roll_no:

            print("\n--------------------------------")
            print("        STUDENT MARK SHEET")
            print("--------------------------------")
            print("Name       :", student["name"])
            print("Roll No    :", student["roll_no"])
            print("Department :", student["department"])
            print()
            print("Python     :", student["python"])
            print("English    :", student["english"])
            print("Maths      :", student["maths"])
            print()
            print("Total      :", student["total"])
            print("Average    :", round(student["average"], 2))
            print("Grade      :", student["grade"])
            print("Result     :", student["result"])
            print("--------------------------------")

            found = True
            break

    if not found:
        print("Student not found.")


def display_topper():
    print("\n===== TOPPER =====")

    if len(students) == 0:
        print("No student records found.")
        return

    topper = students[0]

    for student in students:
        if student["total"] > topper["total"]:
            topper = student

    print("--------------------------------")
    print("Name       :", topper["name"])
    print("Roll No    :", topper["roll_no"])
    print("Department :", topper["department"])
    print("Total      :", topper["total"])
    print("Average    :", round(topper["average"], 2))
    print("Grade      :", topper["grade"])
    print("--------------------------------")


def display_passed():
    print("\n===== PASSED STUDENTS =====")

    found = False

    for student in students:
        if student["result"] == "PASS":
            print(
                student["roll_no"],
                "-",
                student["name"],
                "-",
                student["grade"]
            )
            found = True

    if not found:
        print("No passed students.")


def display_failed():
    print("\n===== FAILED STUDENTS =====")

    found = False

    for student in students:
        if student["result"] == "FAIL":
            print(
                student["roll_no"],
                "-",
                student["name"],
                "-",
                student["grade"]
            )
            found = True

    if not found:
        print("No failed students.")


# Main Program

while True:

    print("\n====================================")
    print("       STUDENT RESULT SYSTEM")
    print("====================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Display Topper")
    print("5. Display Passed Students")
    print("6. Display Failed Students")
    print("7. Exit")
    print("====================================")

    choice = input("Enter your choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_topper()

    elif choice == "5":
        display_passed()

    elif choice == "6":
        display_failed()

    elif choice == "7":
        print("\nThank you for using Student Result System!")
        break

    else:
        print("\nInvalid choice! Please try again.")
