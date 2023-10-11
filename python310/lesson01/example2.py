# The code below will ask the user for a number,
# which will be captured as a string
first_number = input("Enter the first number: ")
# The user's input is now converted to an integer
first_number = int(first_number)
# For this one, the input from the user is directly converted into integer
second_number = int(input("Enter the second number: "))
result = first_number + second_number
print(f"The result of the operation is {result}")
lenght_of_result = len(str(result))
# In the code below, the expected value is the output of the len() function
print(f"The lenght of the result is {lenght_of_result}")