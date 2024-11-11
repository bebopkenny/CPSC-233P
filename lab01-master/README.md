# Laboratory 1

## Laboratory Objectives
1. Write Python code using any editor.
2. Execute the program from the command line.
3. Unit test the program.
4. Upload on Canvas for submission

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
1. Write a Python program that performs as a Tuffy Titan Hello Program which simply contains two functions that return *Hello ...* strings and are then outputted to the screen.

1. Create a `hello` module to meet the following requirements:
     1. Create a file named `hello.py`.
     1. Add a comment at the top of your code.
          ```
          # Name: Stephen May
          # Date: 8/1/2021
          # File Purpose: Multiple hello functions
          ```
     1. Define a function named `helloworld` which takes no parameters and returns the string `Hello World!`.
          ```
          def helloworld():
              return "Hello World!"
          ```
     1. Define a function named `helloname` which takes one string parameter and returns the string `Hello xxx!` where xxx is the value of the string parameter.
          ```
          def helloname(name):
              return "Hello " + name + "!"
          ```
1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Add a comment at the top of your code.
          ```
          # Name: Stephen May
          # Date: 8/1/2021
          # File Purpose: Lab01 main program driver program
          ```
     1. Import the `hello` module.
          ```
          from hello import *
          ```
     1. Output a program header to the standard output.
          ```
          print("*** TUFFY TITAN HELLO PROGRAM ***")
          ```
     1. Call the `helloworld` function and output the return value to the standard output.
          ```
          print(helloworld())
          ```
     1. Call the `helloname` function passing a string parameter and output the return value to the standard output.
          ```
          print(helloname("Steve"))
          ```

1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 -m main
    ```


1. Typical output for the program:
     ```
    *** TUFFY TITAN HELLO PROGRAM ***
    Hello World!
    Hello Steve!
     ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission

Submit a zip file containing all the code files on canvas 

Naming Convention: <CWID>_<LastName>.zip

You should have the following files:
```
main.py
hello.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|15|main.py file submitted contains the main driver program and meets the program requirements|
|15|hello.py file submitted contains the hello module and meets the program requirements|
|10|unit test passes Test01_HelloWorld|
|10|unit test passes Test02_HelloName|
