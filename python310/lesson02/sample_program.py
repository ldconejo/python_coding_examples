def ask_user_info_version_1():
    name = ""
    while name == "":
        name = input("What is your name? ")
    age = input("What is your age? ")
    return name, age

def ask_user_info_version_2():
    name = ""
    while not name:
        name = input("What is your name? ")
    age = input("What is your age? ")
    return name, age

def ask_user_info_version_3():
    while True:
        name = input("What is your name? ")
        if name != "":
            break
    age = input("What is your age? ")
    return name, age

def ask_user_info():
    while True:
        name = input("What is your name? ")
        if name:
            break
    age = input("What is your age? ")
    return name, age

def multi_language_greeting():
    while True:
        language = input("What language would you like to use? ")
        if language:
            break
    return language

def greet_in_language_version_1(language):
    language = language.lower()
    if language == "spanish":
        print("Hola, cómo estás?")
    elif language == "french":
        print("Salut, ça va?")
    elif language == "german":
        print("Hallo! Wie geht's?")
    elif language == "italian":
        print("Ciao, come stai?")
    elif language == "chinese":
        print("你好么?")
    else:
        print("Hey, what's up?")

def greet_in_language(language):
    match language.lower():
        case "english":
            print("Hey, what's up?")
        case "spanish":
            print("Hola, cómo estás?")
        case "french":
            print("Salut, ça va?")
        case "german":
            print("Hallo! Wie geht's?")
        case "italian":
            print("Ciao, come stai?")
        case "chinese":
            print("你好么?")
        case _:
            print("Sorry, I don't recognize that language")

def greeting_name_age(name, age):
    print(f"Your name is {name} and you are {age} years old")

def simple_greeting():
    print("Hi, how are you?")

def greeting_with_name(name):
    print(f"Hi, how are you {name}?")

def main():
    name, age = ask_user_info()
    greeting_name_age(name, age)
    language = multi_language_greeting()
    greet_in_language(language)
#print(f"The __name__ variable has a value of: {__name__}")

#__name__ = "Now I broke the __name__ variable"

# Is this Python program running directly?
if __name__ == "__main__":
    main()
else:
    print("Welcome to sample program.py. You are reading this because you imported the file.")
