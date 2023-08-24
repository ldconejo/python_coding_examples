from operator import xor

def your_name():
    name = input('What is your name? ')
    middle_name = input('What is your middle name? (Press enter if none) ')
    last_name = input('What is your lastname? ')
    print(f"Hello {name or middle_name} {last_name}!")

def candidate_student():
    hanzi = False
    knows_hanzi = input("Can you read Chinese characters? (y/n) ")
    if knows_hanzi == "y":
        hanzi = True
    
    knows_mandarin = input("Can you speak Mandarin? (y/n) ")
    mandarin = False
    if knows_mandarin == "y":
        mandarin = True

    if xor(hanzi, mandarin):
        print("We have something to teach you")
    else:
        print("We have nothing to teach you")

if __name__ == "__main__":
    candidate_student()