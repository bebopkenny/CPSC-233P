# main.py
# Name: Kenny Garcia
# Date: 11/05/2024
# Purpose: Use the person class from people.py module to display the program

from people import Faculty, Student

faculty_list = []
student_list = []

def add_faculty():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    department = input("Enter department: ")
    faculty = Faculty(first_name, last_name, department)
    faculty_list.append(faculty)

def print_faculty():
    print("\n======================= FACULTY =======================")
    print("Record  Name                  Department")
    print("======  ====================  =========================")
    for i, faculty in enumerate(faculty_list):
        print(f"{i:<6}  {faculty.firstname} {faculty.lastname:<20}  {faculty.department}")

def add_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    class_year = input("Enter class year: ")
    major = input("Enter major: ")
    
    print("\nSelect faculty advisor by record number:")
    print_faculty()
    
    advisor_index = int(input("Enter faculty advisor: "))
    if 0 <= advisor_index < len(faculty_list):
        advisor = faculty_list[advisor_index]
    else:
        print("Invalid advisor selection. Advisor not assigned.")
        advisor = None
    
    student = Student(first_name, last_name)
    student.set_class(class_year)
    student.set_major(major)
    student.set_advisor(advisor)
    
    student_list.append(student)

def print_student():
    print("\n===================================== STUDENTS ======================================")
    print("Name                  Class      Major                      Advisor")
    print("====================  =========  =========================  =========================")
    for student in student_list:
        advisor_name = f"{student.advisor.firstname} {student.advisor.lastname}" if student.advisor else "None"
        print(f"{student.firstname} {student.lastname:<18}  {student.classyear:<8}  {student.major:<25}  {advisor_name}")

def main_menu():
    while True:
        print("\n      *** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
        print("1. Add faculty")
        print("2. Print faculty")
        print("3. Add student")
        print("4. Print student")
        print("9. Exit the program")
        
        choice = input("\nEnter menu choice: ")
        
        if choice == '1':
            add_faculty()
        elif choice == '2':
            print_faculty()
        elif choice == '3':
            add_student()
        elif choice == '4':
            print_student()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()