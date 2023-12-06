'''
This module is designed  to demonstrate
some common errors when writing Python code
'''
# pylint: disable=W1514
AUTHOR = "jdoe"

def good_function_name():
    '''
    This is a function that demonstrates some issues
    when coding functions
    '''
    # Open the file and display the content of each line
    try:
        with open("test.txt", "r") as test_file:
            all_lines = test_file.readlines()
            for line in all_lines:
                print(line)
    except FileNotFoundError:
        print("ERROR: File not found")
    except ValueError:
        print("Value error")
    # pylint: disable=broad-exception-caught
    # This is a bare exception
    except Exception as exception_details: 
        # This should eventually be a log entry
        # warning that we ran into something unexpected
        # TODO: Need to turn this into a log entry, instead of a print
        print(f"Ran into something unexpected: {exception_details}")

def extra_else(direction):
    ''''
    This one portrays the issues with return
    '''
    if direction == "North":
        return "Going North"
    if direction == "South":
        return "Going South"
    return "You can only go North or South!"
    # print("There is no way for us to get here!")

def inconsistent_returns(user_input):
    ''''
    This one shows the pitfalls with inconsistent returns
    '''
    if user_input == 1:
        return 1
    if user_input == 2:
        return 0
    # print("You didn't enter 1 or 2")
    return "You didn't enter 1 or 2"
