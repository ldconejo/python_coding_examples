number = input("Choose one number: ")

number = int(number)

#if (number == 2)or(number == 3)or(number == 5)or(number==7):
if number in (2, 3, 5, 7):
    print("That's one of the correct numbers!")
else:
    print("Sorry, you didn't guess right!")