'''
Different examples of warning-triggering PEP8 issues
'''

def demo(number_of_passengers):
    '''
    Demo of no-else-return warning
    '''
    if 0 < number_of_passengers < 551:
        return "Boeing 777-300"
    elif number_of_passengers < 700:
    #if number_of_passengers < 700:
        return "Boeing 747-8"
    else:
        return "Take a train"
        