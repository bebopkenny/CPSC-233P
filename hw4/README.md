# Laboratory 4

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and VS Code.
1. Write a Python program using:
     1. lists
     2. loops
     3. conditional statements
     4. input/output
     5. modules
     6. functions using positional and keyword arguments
     7. dictionaries
1. Run and test a Python program.

## Getting Started

1. Setting Up Python Environment

     - Verify Python Installation:
     - Open your terminal (Command Prompt for Windows, Terminal for macOS/Linux).
     - Type python --version and press Enter.
     - You should see the installed Python version displayed.

2. Configuring Visual Studio Code (VS Code)

     - Install Python Extension:
     - Open VS Code.
     - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
     - Search for “Python” in the Extensions Marketplace.
     - Click “Install” on the Python extension by Microsoft.

3. Running Python in VS Code

     - Create a New Python File:
     - In VS Code, open a folder where you want to save your Python projects.
     - Click on File > New File or press Ctrl+N to create a new file.
     - Save the file with a .py extension (e.g., hello.py).
     
## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

1. Create a `contacts` module to meet the following requirements:
     1. Create a file named `contacts.py`.
     1. Add a comment at the top of the file which indicates your name, date and the purpose of the file.
     1. Note: All contact dictionaries within this module should assume a dictionary of the form: `{id: ['first', 'last'], id: ['first', 'last'], id: ['first', 'last']...}` where the id will be the phone number in this exercise.
     1. Note: All functions should implement a docstring with a simple sentence that describes the function.
     1. Define a function named `add_contact` to meet the following requirements:
          1. Take a contact dictionary as a positional parameter.
          1. Take a `id` as a keyword parameter.
          1. Take a `first_name` as a keyword parameter.
          1. Take a `last_name` as a keyword parameter.
          2. If the id exists in the dictionary, return the string `error`.
          3. Append the id:[first_name, last_name] key:value pair to the contact dictionary.
          4. Return the key:value pair that was added.
     1. Define a function named `modify_contact` to meet the following requirements:
          1. Take a contact dictionary as a positional parameter.
          1. Take a `id` as a keyword parameter.
          1. Take a `first_name` as a keyword parameter.
          1. Take a `last_name` as a keyword parameter.
          1. If the id does not exists in the dictionary, return the string `error`.
          1. Append the id:[first_name, last_name] key:value pair to the contact dictionary.
          1. Return the key:value pair that was added.
     1. Define a function named `delete_contact` to meet the following requirements:
          1. Take a contact dictionary as a positional parameter.
          1. Take a `id` as a keyword parameter.
          2. If the id does not exists in the dictionary, return the string `error`.
          3. Remove the key:value pair with the key equal to id.
          3. Return the key:value pair with the key equal to id.
     1. Define a function named `sort_contacts` to meet the following requirements:
          1. Take a contact dictionary as a positional parameter.
          2. Sort the dictionary in ascending order by last name, and then by first name, ignoring case.
          3. Return the sorted dictionary. 
     1. Define a function named `find_contact` to meet the following requirements:
          1. Take a contact dictionary as a positional parameter.
          1. Take a `find` as a keyword parameter.
          2. Create an empty dictionary.
          3. If find is a numeric value and contained as a key in the dictionary, add the key:value pair to the created dictionary.
          4. Loop through all the key:value pairs and if the find substring is contained in either the first name or last name, add the key:value pair to the created dictionary.
          5. Sort the created dictionary in ascending order by last name, and then by first name, ignoring case.
          6. Return the created dictionary. 
1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Add a comment at the top of the file which indicates your name, date and the purpose of the file.
     1. Import the `contacts` module.
     2. Define a variable to use for the contact dictionary. 
     3. Implement a menu within a loop with following choices:
          1. Add contact
          1. Modify contact
          1. Delete contact
          1. Print contact list (sorted)
          1. Find contact
          1. Exit the program
     4. Prompt the user for the menu choice.
     5. Prompt the user for the information needed for the appropriate `contacts` function and call the function.
     6. Print out appropriate errors with function return values of `error`.
1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 -m main
    ```


1. Typical input and output for the program:
     ```
           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 1

     Enter phone number: 7145551212
     Enter first name: Steve 
     Enter last name: Jobs
     Added: Steve Jobs.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 4

     ==================== CONTACT LIST ====================
     Last Name             First Name            Phone
     ====================  ====================  ==========
     Jobs                  Steve                 7145551212  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 1

     Enter phone number: 7145551212
     Enter first name: Bill 
     Enter last name: Gates
     Phone number already exists.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 2

     Enter phone number: 7145551212
     Enter first name: Bill
     Enter last name: Gates
     Modified: Bill Gates.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 4

     ==================== CONTACT LIST ====================
     Last Name             First Name            Phone
     ====================  ====================  ==========
     Gates                 Bill                  7145551212  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 2

     Enter phone number: 5551212
     Enter first name: Richard 
     Enter last name: Stallman
     Phone number does not exist.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 3

     Enter phone number: 5551212
     Invalid phone number.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 3

     Enter phone number: 7145551212
     Deleted: Bill Gates.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 4

     ==================== CONTACT LIST ====================
     Last Name             First Name            Phone
     ====================  ====================  ==========

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 1

     Enter phone number: 7145551111
     Enter first name: Alpha
     Enter last name: Jobs
     Added: Alpha Jobs.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 1

     Enter phone number: 7145552222
     Enter first name: Steve
     Enter last name: Jobs
     Added: Steve Jobs.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 1

     Enter phone number: 5625553333
     Enter first name: Bill
     Enter last name: Gates
     Added: Bill Gates.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 4

     ==================== CONTACT LIST ====================
     Last Name             First Name            Phone
     ====================  ====================  ==========
     Gates                 Bill                  5625553333  
     Jobs                  Alpha                 7145551111  
     Jobs                  Steve                 7145552222  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 5

     Enter search string: jobs
     ================== FOUND CONTACT(S) ==================
     Last Name             First Name            Phone
     ====================  ====================  ==========
     Jobs                  Alpha                 7145551111  
     Jobs                  Steve                 7145552222  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 5

     Enter search string: 5625553333
     ================== FOUND CONTACT(S) ==================
     Last Name             First Name            Phone
     ====================  ====================  ==========
     Gates                 Bill                  5625553333  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Add contact
     2. Modify contact
     3. Delete contact
     4. Print contact list
     5. Find contact
     6. Exit the program

     Enter menu choice: 6
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

Your zipped folder should contain below files:
```
CWID_LASTNAME.zip -
                  | > test.py
                  | > test.sh
                  | > main.py
                  | > contacts.py
                  | > test.txt
                  | > win_test.bat
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|10|main.py file submitted contains the main driver program and meets the program requirements|
|10|contacts.py file submitted contains the contacts module and meets the program requirements|
|3|unit test passes Test01_AddContact|
|3|unit test passes Test02_AddContact|
|3|unit test passes Test03_ModifyContact|
|3|unit test passes Test04_ModifyContact|
|3|unit test passes Test05_DeleteContact|
|3|unit test passes Test06_DeleteContact|
|4|unit test passes Test07_SortContacts|
|4|unit test passes Test08_FindContact|
|4|unit test passes Test09_FindContact|



