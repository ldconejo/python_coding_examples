'''
Sample code to demonstrate unit testing
'''

def perform_addition(first_number, second_number):
    '''
    Adds two numbers entered as strings
    '''
    return float(first_number) + float(second_number)

def perform_subtraction(first_number, second_number):
    '''
    Subtracts two numbers entered as strings
    '''
    return float(first_number) - float(second_number)

def main_menu():
    '''
    Implements a basic main menu
    '''
    print("Welcome to this simple adder / subtracter")
    user_name = input("What is your name? ")
    print(f"Welcome {user_name}")
    operation = ""
    # Checks the operation entered by the user is valid
    # and keeps on asking if not
    while operation not in ("addition", "subtraction"):
        operation = input("Would you like to do addition or subtraction? ")
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    if operation == "addition":
        result = perform_addition(first_number, second_number)
        return f"The result of adding {first_number} plus {second_number} is {result}"
    # No 'else' needed here, since the presiding line is a 'return'
    result = perform_subtraction(first_number, second_number)
    return f"The result of subtracting {first_number} minus {second_number} is {result}"

if __name__ == "__main__":
    print(main_menu())
