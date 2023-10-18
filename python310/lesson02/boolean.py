can_drive = ""

if can_drive:
    print("Okay, take the car!")
else:
    print("You have to wait a few years!")

print(bool(-12))
print(bool(0))

print(bool(""))
print(bool("  "))
print(bool(None))

# AND truth table (boolean multiplication)
# Input-1   Input-2     Result
# False     False       False
# False     True        False
# True      False       False
# True      True        True

result = True and False
print(f"The result is {result}")

# OR truth table (boolean addition)
# Input-1   Input-2     Result
# False     False       False
# False     True        True
# True      False       True
# True      True        True

result = True or False
print(f"The result is {result}")
