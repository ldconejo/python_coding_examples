def outer_function():
    known_people = []

    def inner_function():
        name = input("Who are you? ")
        if name in known_people:
            print(f"Hey, {name}, nice to see you again!")
        else:
            print(f"Hello there, {name}, it's great to meet you!")
            known_people.append(name)
    return inner_function

test_function = outer_function()

while True:
    test_function()
