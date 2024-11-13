# Laboratory 5

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
1. Write a Python package with sub-packages, modules, and functions using keyword arguments.  Use the following directory outline and module names (your first starting point should be a directory called `mathematics` within your `lab05-username` directory):
     ```
	mathematics/
		__init__.py
		whoami.py
		numbers/
			__init__.py
			whoami.py
			series.py
			simple.py
		geometry/
			__init__.py
			whoami.py
			rectangle.py
			circle.py
			cube.py
     ```

1. Create a `mathematics` package.
     1. Initialize the `__all__` variable to the `whoami` module.
     1. Create a `whoami` module.
          1. Create a function named `getname` which returns the `__name__` variable.
     1. Create a `numbers` sub-package.
          1. Initialize the `__all__` variable to the `whoami` and `series` modules.
          1. Create a `whoami` module.
               1. Create a function named `getname` which returns the `__name__` variable.
          1. Create a `series` module.
               1. Create a function named `sum` which receives a keyword parameter `list` and returns the sum of all the values in the list.
               1. Create a function named `average` which receives a keyword parameter `list` and returns the average of all the values in the list.
          1. Create a `simple` module.
               1. Create a function named `addition` which receives the keyword parameters `left` and `right` and returns left plus right.
               1. Create a function named `subtraction` which receives the keyword parameters `left` and `right` and returns left minus right.
               1. Create a function named `multiplication` which receives the keyword parameters `left` and `right` and returns left multiplied by right.
               1. Create a function named `division` which receives the keyword parameters `left` and `right` and returns left divided by right.
     1. Create a `geometry` sub-package.
          1. Initialize the `__all__` variable to the `whoami`, `circle`, and `cube` modules.
          1. Create a `whoami` module.
               1. Create a function named `getname` which returns the `__name__` variable.
          1. Create a `rectangle` module.
               1. Create a function named `perimeter` which receives a keyword parameters `length` and `width` and returns (2l + 2h).
               1. Create a function named `area` which receives a keyword parameters `length` and `width` and returns (l * h).
          1. Create a `circle` module.
               1. Create a function named `circumference` which receives the keyword parameter `radius` and returns (2 * pi * r).
               1. Create a function named `area` which receives the keyword parameter `radius` and returns (pi * r * r).
          1. Create a `cube` module.
               1. Create a function named `surface_area` which receives the keyword parameter `side` and returns (s * s * 6).
               1. Create a function named `volume` which receives the keyword parameter `side` and returns (s * s * s).
5. Create your own main.py file to test all the modules and functions and run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements. I will not grade this file - it is for your use to test the package.

    ```
    python3 -m main
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

## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|1|mathematics/__init__.py file submitted and meets the program requirements |
|1|mathematics/whoami.py file submitted and meets the program requirements |
|1|mathematics/numbers/__init__.py file submitted and meets the program requirements |
|2|mathematics/numbers/whoami.py file submitted and meets the program requirements |
|2|mathematics/numbers/series.py file submitted and meets the program requirements |
|2|mathematics/numbers/simple.py file submitted and meets the program requirements |
|1|mathematics/geometry/__init__.py file submitted and meets the program requirements |
|2|mathematics/geometry/whoami.py file submitted and meets the program requirements |
|2|mathematics/geometry/rectangle.py file submitted and meets the program requirements |
|2|mathematics/geometry/circle.py file submitted and meets the program requirements |
|2|mathematics/geometry/cube.py file submitted and meets the program requirements |
|2|unit test passes Test01_mathematics_whoami_getname|
|2|unit test passes Test02_mathematics_numbers_whoami_getname|
|2|unit test passes Test03_mathematics_numbers_series_sum|
|2|unit test passes Test04_mathematics_numbers_series_average|
|2|unit test passes Test05_mathematics_numbers_simple_addition|
|2|unit test passes Test06_mathematics_numbers_simple_subtraction|
|2|unit test passes Test07_mathematics_numbers_simple_multiplication|
|2|unit test passes Test08_mathematics_numbers_simple_division|
|2|unit test passes Test09_mathematics_geometry_whoami_getname|
|2|unit test passes Test10_mathematics_geometry_rectangle_perimeter|
|2|unit test passes Test11_mathematics_geometry_rectangle_area|
|2|unit test passes Test12_mathematics_geometry_cube_surfacearea|
|2|unit test passes Test13_mathematics_geometry_cube_volume|
|2|unit test passes Test14_mathematics_init|
|2|unit test passes Test15_mathematics_numbers_init|
|2|unit test passes Test16_mathematics_geometry_init|
