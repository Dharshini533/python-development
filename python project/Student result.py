students = []

def add_student():
    print("\n Add New Student ")
    name = input("Enter student name: ")
    reg_no = input("Enter register number: ")

    marks = []
    num_subjects = int(input("Enter number of subjects: "))

    for i in range(num_subjects):
        m = float(input(f"Enter mark for subject {i + 1}: "))
        marks.append(m)

    total = sum(marks)
    avg = total / num_subjects

    if avg >= 90:
        grade = "O"
    elif avg >= 80:
        grade = "A+"
    elif avg >= 70:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "RA"

    student = {
        "name": name,
        "reg_no": reg_no,
        "marks": marks,
        "total": total,
        "avg": avg,
        "grade": grade
    }
    students.append(student)
    print("Student details added successfully!\n")


def view_students():
    print("\n Student Report ")
    if not students:
        print("No student records found.\n")
        return

    for s in students:
        print(f"Name       : {s['name']}")
        print(f"Reg No     : {s['reg_no']}")
        print(f"Marks      : {s['marks']}")
        print(f"Total      : {s['total']}")
        print(f"Average    : {s['avg']:.2f}")
        print(f"Grade      : {s['grade']}")
        print("-" * 30)
    print()


def search_student():
    print("\n Search Student ")
    reg = input("Enter register number to search: ")
    for s in students:
        if s["reg_no"] == reg:
            print(f"Name       : {s['name']}")
            print(f"Reg No     : {s['reg_no']}")
            print(f"Marks      : {s['marks']}")
            print(f"Total      : {s['total']}")
            print(f"Average    : {s['avg']:.2f}")
            print(f"Grade      : {s['grade']}\n")
            return
    print("Student not found.\n")


def save_to_file():
    print("\n Save to File ")
    if not students:
        print("No records to save.\n")
        return
    with open("student_report.txt", "w") as f:
        for s in students:
            f.write(f"Name: {s['name']}, Reg: {s['reg_no']}, "
                    f"Marks: {s['marks']}, Total: {s['total']}, "
                    f"Average: {s['avg']:.2f}, Grade: {s['grade']}\n")
    print("All records saved to student_report.txt\n")


def main():
    while True:
        print("Student Result Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Reg No")
        print("4. Save Report to File")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            print("Exiting Student Result Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()