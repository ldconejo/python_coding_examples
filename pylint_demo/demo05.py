'''
Different examples of warning-triggering PEP8 issues
'''

def demo(filename):
    '''
    Demo of bare-except warning
    '''
    try:
        with open(filename, 'r') as demo_file:
            for line in demo_file:
                print(int(line))
    except:
        print("ERROR: File not found")
    #except ValueError as details:
    #    print(f"ERROR: Exception found while reading file: {details}")
    #except FileNotFoundError as details:
    #    print(f"ERROR: {details}")

if __name__ == '__main__':
    #demo('wrong_file.txt')
    demo('demo05.txt')
