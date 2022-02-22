'''
Different examples of warning-triggering PEP8 issues
'''

def needed_fuel(distance, gallons_per_mile=5.85):
    '''
    Demo of inconsistent-return-statements warning
    '''
    if distance > 0:
        return distance * gallons_per_mile
    #return 0

if __name__ == '__main__':
    TOTAL_DISTANCE = input("Please enter the distance: ")
    TOTAL_FUEL = int(needed_fuel(int(TOTAL_DISTANCE)))
    print(f"You need to total of {TOTAL_FUEL} gallons to travel {TOTAL_DISTANCE} miles by plane.")
        