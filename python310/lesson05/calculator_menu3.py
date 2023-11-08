'''
This is a demonstration of a simple calculator menu
'''
import sys
from calculator_implementation import *
from calculator_implementation import add as add_model
from calculator_implementation import subtract as subtract_model

menu_options = """
    A. Addition.
    B. Subtraction.
    Q. Quit program.

    Please select one of the options above.
"""

def addition():
    number1 = input(f"Please enter your first number: ")
    number2 = input(f"Please enter your second number: ")
    result = add_model(number1, number2)
    print(f"Your result is {result}")

def subtraction():
    number1 = input(f"Please enter your first number: ")
    number2 = input(f"Please enter your second number: ")
    result = subtract_model(number1, number2)
    print(f"Your result is {result}")

def quit_program():
    print("Goodbye!")
    sys.exit()

menu_functions = {
    "a": addition,
    "b": subtraction,
    "q": quit_program
}

if __name__ == "__main__":
    while True:
        menu_selection = input(menu_options).strip().lower()
        if menu_selection in menu_functions.keys():
            menu_functions[menu_selection]()
        else:
            print(f"You selected {menu_selection}. Please select a valid option")
