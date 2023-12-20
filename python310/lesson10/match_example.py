from sys import version as python_version
language_for_greeting = input("What language would you like me to use to greet you? ")

language = language_for_greeting.lower()

if python_version < 3.10:

    if language == "spanish":
        print("Hola, cómo estás?")
    elif language == "french":
        print("Salut! Comment ça va?")
    elif language == "chinese":
        print("你好! 怎么样?")
    else:
        print("Hi, how are you?")
else:
    match language_for_greeting.lower():
        case "spanish":
            print("Hola, cómo estás?")
        case "french":
            print("Salut! Ça va?")
        case "chinese":
            print("你好! 怎么样?")
        case _:
            print("Hi, how are you?")

# Another way of doing it
languages = {
    "spanish": "Hola, cómo estás?",
    "french": "Salut! Comment ça va?",
    "chinese": "你好! 怎么样?"
}

try:
    print(languages[language_for_greeting.lower()])
except KeyError:
    print("Hi, how are you?")


