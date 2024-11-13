# Laboratory 8

## Laboratory Objectives
1. Write Python code using any editor.
2. Execute the program from the command line.
3. Unit test the program.
4. Upload on Canvas for submission

## Getting Started
1. Setting Up Python Environment

     - Verify Python Installation:
     - Open your terminal (Command Prompt for Windows, Terminal for macOS/Linux).
     - Type `python --version` and press Enter.
     - You should see the installed Python version displayed.

2. Configuring Visual Studio Code (VS Code)

     - Install Python Extension:
     - Open VS Code.
     - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
     - Search for `Python` in the Extensions Marketplace.
     - Click “Install” on the Python extension by Microsoft.

3. Running Python in VS Code

     - Create a New Python File:
     - In VS Code, open a folder where you want to save your Python projects.
     - Click on File > New File or press Ctrl+N to create a new file.
     - Save the file with a .py extension (e.g., `hello.py`).

## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Student/Faculty List which contains a list of students and a list of faculty.
1. Create a `people` module to meet the following requirements:
     1. Create a file named `people.py`.
          1. Define a class named `Person`.  
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a first name string as a positional parameter.
                    1. Take a last name string as a positional parameter.
                    1. Set a member variable `firstname` equal to the first name parameter.
                    1. Set a member variable `lastname` equal to the last name parameter.
          1. Define a class named `Faculty` that inherits from `Person`  
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a first name as a positional parameter.
                    1. Take a last name as a positional parameter.
                    1. Take a department as a positional parameter.
                    1. Call the `Person` `__init__` member function passing the first and last name.
                    1. Set a member variable `department` equal to the department parameter.
          1. Define a class named `Student` that inherits from `Person`  
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a first name string as a positional parameter.
                    1. Take a last name string as a positional parameter.
                    1. Call the `Person` `__init__` member function passing the first and last name.
               1. Define a member function named `set_class` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a class year string as a positional parameter.
                    1. Set a member variable `classyear` equal to the class year parameter.
               1. Define a member function named `set_major` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a major string as a positional parameter.
                    1. Set a member variable `major` equal to the major parameter.
               1. Define a member function named `set_advisor` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a `Faculty` object as a positional parameter.
                    1. Set a member variable `advisor` equal to the faculty parameter.
1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Import the `Faculty` and `Student` classes from the `people` module.
     2. Declare a variable to hold a list of faculty.
     3. Declare a variable to hold a list of students.
     6. Implement a menu within a loop with following choices:
          1. Add faculty
          2. Print faculty
          3. Add student
          4. Print student
          9. Exit the program
     7. Prompt the user for the menu choice.
     8. The Add faculty function should prompt the user for the first name, last name, and department, then instantiate a `Faculty` object and append the object to the faculty list.
     8. The Add student function should prompt the user for the first name, last name, class year, major, and the record number of the faculty advisor, then instantiate a `Student` object and append the object to the student list.
1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 -m main
    ```


1. Typical input and output for the program:
     ```
           *** TUFFY TITAN STUDENT/FACULTY MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

     Enter menu choice: 2

     ======================= FACLUTY =======================
     Record  Name                  Department
     ======  ====================  =========================
     0       Susan Barua           Computer Science         
     1       Hosssen Moini         Mechanical Engineering   
     2       Huda Munjy            Civil Engineering        
     3       Mostafa Shiva         Electrical Engineering   

           *** TUFFY TITAN STUDENT/FACULTY MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

     Enter menu choice: 4

     ===================================== STUDENTS ======================================
     Name                  Class      Major                      Advisor
     ====================  ========   =========================  =========================
     Erica Perine          Freshman   Civil Engineering          Huda Munjy          
     Jonathan Rosso        Senior     Computer Science           Susan Barua         
     Samuel Carter         Sophomore  Environmental Engineering  Huda Munjy          
     Stephanie Dalaba      Senior     Electrical Engineering     Mostafa Shiva       
     Chuck Pirards         Junior     Mechanical Engineering     Hosssen Moini       

           *** TUFFY TITAN STUDENT/FACULTY MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

     Enter menu choice: 1

     Enter first name: George
     Enter last name: Kiran
     Enter department: Computer Engineering

           *** TUFFY TITAN STUDENT/FACULTY MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

     Enter menu choice: 2

     ======================= FACLUTY =======================
     Record  Name                  Department
     ======  ====================  =========================
     0       Susan Barua           Computer Science         
     1       Hosssen Moini         Mechanical Engineering   
     2       Huda Munjy            Civil Engineering        
     3       Mostafa Shiva         Electrical Engineering   
     4       George Kiran          Computer Engineering     

           *** TUFFY TITAN STUDENT/FACULTY MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

     Enter menu choice: 3

     Enter first name: Becky
     Enter last name: Hanna
     Enter class year: Senior
     Enter major: Computer Science
     Enter faculty advisor: 4

           *** TUFFY TITAN STUDENT/FACULTY MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

     Enter menu choice: 4

     ===================================== STUDENTS ======================================
     Name                  Class      Major                      Advisor
     ====================  =========  =========================  =========================
     Erica Perine          Freshman   Civil Engineering          Huda Munjy          
     Jonathan Rosso        Senior     Computer Science           Susan Barua         
     Samuel Carter         Sophomore  Environmental Engineering  Huda Munjy          
     Stephanie Dalaba      Senior     Electrical Engineering     Mostafa Shiva       
     Chuck Pirards         Junior     Mechanical Engineering     Hosssen Moini       
     Becky Hanna           Senior     Computer Science           George Kiran        

           *** TUFFY TITAN STUDENT/FACULTY MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

     Enter menu choice: 9
     ```

1. Run the unit testing program to ensure that your program runs as expected.
    
- For Linux and Mac users
    ```
    ./test.sh
    ```
       
- For windows users
    ```
    ./win_test.bat
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` or `./win_test.bat` repeatedly until it passes all the test.

## Submission
Submit a zip file containing all the code files on canvas 

Naming Convention: CWID_LastName.zip

You should have the following files:
```
main.py
people.py
test.txt
test.py
win_test.bat
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|5|main.py file submitted and meets the program requirements |
|10|people.py file submitted and meets the program requirements |
|5|unit test passes Test01_Person|
|5|unit test passes Test02_Faculty|
|5|unit test passes Test03_FacultyInheritsPerson|
|5|unit test passes Test04_FacultyInheritsStudent|
|5|unit test passes Test05_Student|
|5|unit test passes Test06_StudentInheritsPerson|
|5|unit test passes Test07_StudentInheritsFaculty|
