'''
Different examples of warning-triggering PEP8 issues
'''

def demo(number_of_passengers):
    '''
    Demo of unreachable warning
    '''
    if number_of_passengers > 0:
        return "We definitely have a plane for you!"
    return "If you have zero or negative passengers, why do you need a plane?"
    new_response = "How do we get here?"
    return new_response
