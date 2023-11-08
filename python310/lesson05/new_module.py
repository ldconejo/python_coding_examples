def say_hi():
    return "Hey, how's it going?"

def say_hi_name(username):
    return f"Hey {username}, how's it going?"

print("This is new_module.py")
print(f"This is being executed as {__name__}")

if __name__ == "__main__":
    print("new_module.py is being executed directly.")
    result = say_hi()
    print(result)
    print(say_hi_name("Paul"))
else:
    # This is what will run if the code is called using import
    print("new_module.py was imported")
