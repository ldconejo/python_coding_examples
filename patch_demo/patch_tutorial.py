def get_user_input():
    name = input('Enter your name: ')
    last_name = input('Enter your last name: ')
    age = int(input('Enter your age: '))
    robot = input('Are you a robot? (y/n)')

    if robot.lower() == 'n':
        return f"You are {name} {last_name}, and you're {age} years old."
    if robot.lower() == 'y':
        return f"Welcome, my artificial friend!"
    return f"You are not a human or a robot. What are you?"

def get_user_name():

if __name__ == '__main__':
    print(get_user_input())
