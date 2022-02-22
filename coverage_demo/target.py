'''
Just a simple piece of code to show coverage analysis
'''


def welcome_person(name, role):
    '''
    Welcomes a student or an instructor
    '''test
    if role == 'student':
        return f"Welcome {name}, hope you enjoy the class"
    if role == 'instructor':
        return f"Welcome {name}, break a leg!"
    return f"Error, the role entered by {name} does not exist"
    