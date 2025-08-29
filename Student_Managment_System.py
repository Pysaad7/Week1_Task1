# Function to Calculate Grade Average
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "Fail"

# Function To Add Student
def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Student Roll No: ")
    marks = [int(input(f"Enter Marks for Subject {i+1}: ")) for i in range(3)]
    avg = sum(marks) / 3
    grade = calculate_grade(avg)
    record = {"Name": name, "Roll": roll, "Marks": marks, "Average": avg, "Grade": grade}
    with open("students.txt", "a") as f:
        f.write(str(record) + "\n")
    print("Student added successfully.")

#Function to view Student 
def view_students():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No records found.")

#Function to search Student
def search_student():
    roll = input("Enter Roll No to search: ")
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                record = eval(line.strip())
                if record["Roll"] == roll:
                    print(record)
                    found = True
                    break
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No records found.")

       #Main Menu  
while True:
    print(" === Student Managment System === " )
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exit the Program! ")
        break
    else:
        print("Invalid choice.")
 