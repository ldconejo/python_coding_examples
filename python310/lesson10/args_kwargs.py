def test_function(favorite_food="hot dog", meal_time="dinner"):
    return f"My favorite food is {favorite_food}, I normally eat it at {meal_time}"

def test_function2(*args):
    for argument in args:
        #print(argument)
        if argument == "pizza":
            print("Hey, I like pizza too!")

def test_function3(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

    if "food" in kwargs:
        print("Food is included in the keyword arguments passed!")

    if "popcorn" in kwargs.values():
        print("Popcorn was a value in one of the keyword arguments passed!")

def test_function4(name, *args, **kwargs):
    print(args)
    print(kwargs)
    print(f"Name: {name}")
    print("Arguments:")
    for value in args:
        print(f"\t{value}")

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}\t\t{value}")

def test_function5(**kwargs):
    if "name" not in kwargs.items():
        print("Name is missing")



if __name__ == "__main__":
    #result = test_function()
    #print(result)
    #result = test_function("pizza", "lunch")
    #print(result)
    #test_function2("pizza", "hot dog", "pop corn", "sandwich")
    #test_function2("kebab", "garbanzo beans")
    #test_function3(meal_time="lunch", food="popcorn", month="December")
    #test_function4("pizza", "hot dog", "pop corn", "sandwich", meal_time="lunch", food="popcorn", month="December")

    test_dict = {
        "age": 51,
        "eye color": "Brown"
    }

    test_function5(**test_dict)

    mylist = ["asdf", "fdsa", "asldkfjklad"]
    print("Hello! {}, {}, {}".format(*mylist))