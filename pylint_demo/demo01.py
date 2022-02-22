'''
Different examples of warning-triggering PEP8 issues
'''

def demo(number_of_passengers):
    '''
    Demo of chained-comparison warning
    '''
    #if (number_of_passengers > 0)and(number_of_passengers < 551):
    if 0 < number_of_passengers < 551:
        return "Boeing 777-300"
    return "Take a train"
