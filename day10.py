import csv

students = []

def add_student():

    try:
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        students.append({
            "name": name,
            "marks": marks
        })

        print("Student added successfully")

    except ValueError as e:
        print("Error:", e)


def display_students():

    if not students:
        print("No student records found")
        return

    for student in students:
        print(student["name"], student["marks"])


def save_students():

    with open("students.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["name", "marks"]
        )

        writer.writeheader()
        writer.writerows(students)

    print("Records saved successfully")


def load_students():

    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            students.clear()

            for row in reader:
                students.append({
                    "name": row["name"],
                    "marks": float(row["marks"])
                })

        print("Records loaded successfully")

    except FileNotFoundError:
        print("CSV file not found")


while True:

    print("\n--- Student Marks Manager ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save Students")
    print("4. Load Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        save_students()

    elif choice == "4":
        load_students()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")