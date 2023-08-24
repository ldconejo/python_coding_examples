#for x in range(10):
#    print(x)

#test_list = [x for x in range(10)]

#for value in test_list:
#    print(value)

#def add_one(x):
#    return x + 1

#test_list = list(map(add_one, range(10))) # Take each value in range(10) and run it through the add_one function, returning everything as a list
#print(test_list)

#test_list = [add_one(x) for x in range(10)]
#print(test_list)

#test_list = [x+1 for x in range(10)]
#print(test_list)

def filter_odds(x):
    return x % 2

#test_list = []
#for x in range(10):
#    if filter_odds(x):
#        test_list.append(x)

#test_list = [x for x in range(10) if filter_odds(x)]

test_list = [x for x in range(10) if x % 2]

#test_list = list(filter(filter_odds, range(10)))

print(test_list)