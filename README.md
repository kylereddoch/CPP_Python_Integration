# CPP_Python_Integration
Integrating CPP and Python for a simple math-based program.

**Design a menu with appropriate user interactions and checks for valid entry.** Use C++ to successfully complete this criterion. Your simple program will need a menu that can validate user input and is easy to use. It needs to include options for the display of a multiplication table, doubling a value, and exiting the program. If either of the first two options are selected, then users need to be prompted to input a numeric value. The menu should be displayed using a loop, where the user can choose to exit the program only by selecting option 3. Any user input other than 1, 2, or 3 should result in an error message that returns the user to the menu. An example menu might look like the following:

```code
1: Display a Multiplication Table
2: Double a Value
3: Exit

Enter your selection as a number 1, 2, or 3.
```

**Create code that prints a multiplication table for a given numeric value.** Both C++ and Python will be necessary to successfully complete this criteria. Be sure to focus on their interactions as you work. Consider the following steps to help organize your code design. Note that you should have already written C++ code that prompts a user to input a number while working on the menu portion of this assignment.

- Write C++ code that reads and passes a number, as an integer, to Python. C++ should also call a function in Python to display the multiplication table for the passed parameter. Note that you will be creating that function in the next step. For this step, be sure to check the starter code you were given and use the applicable components.
- Write Python code to create a multiplication table for the given integer. Name this function MultiplicationTable for consistency. The printed table should include values for the multipliers one through ten. An example result is shown below.

```code
6 X 1 = 6
6 X 2 = 12
6 X 3 = 18
6 X 4 = 24
6 X 5 = 30
6 X 6 = 36
6 X 7 = 42
6 X 8 = 48
6 X 9 = 54
6 X 10 = 60
```
