test_dictionary = {}

test_dictionary["favorite food"] = "pizza"
test_dictionary["cost of food"] = 12.99

filled_dictionary = {
    'age': 44,
    'name': 'Luis',
    'lastname': 'Conejo'
}

character_dictionary = {
    "我": "I",
    "她": "She",
    "他": "He",
    "\n": "Return",
    24: "Twenty four",
    # A list cannot be a dictionary key
    #[0,2]: "This will not work"
    (0,2): "This will work fine",
    "some list": [1, 2, 3, "hello"]
}

users_dictionary = {
    "ldconejo": {
        "name": "Luis",
        "lastname": "Conejo"
    },
    "gfawkes": {
        "name": "Guy",
        "lastname": "Fawkes",
        "nickname": "V"
    }
}

'''
print(test_dictionary)

print(test_dictionary['cost of food'])

test_dictionary["cost of food"] = 15.99
print(test_dictionary["cost of food"])

print(filled_dictionary)
print(character_dictionary)

print(users_dictionary['gfawkes']['name'])
print(character_dictionary["some list"][2])

print(character_dictionary["some list"]["name"])
'''

using_dict = dict([('key1',3), ('key2',5)])
using_parameters = dict(key1=3, key2=5)

'''
print(using_dict)
print(using_parameters)
'''

#for element in users_dictionary.items():
#    print(element)
#    print(element[0])
#    print(element[1])

#for element in users_dictionary.keys():
#    print(f"The user ID is: {element}")

#for element in users_dictionary.values():
#    print(f"The value for this one is {element}")

# The default iterative behavior will be to return keys
#for element in users_dictionary:
#    print(f"The user ID is: {element}")

#for key,value in users_dictionary.items():
#    print(f"Key: {key} \t Value: {value}")

#for _ in users_dictionary.items():
#    print("Hey, I'm not using keys or values!")

# Non-existent key
#try:
#    print(users_dictionary['dvader'])
#except KeyError:
#    print("That key does not exist")

#result = users_dictionary.get('dvader')
#print(f"The result is {result}")

#result = users_dictionary.get('dvader', 'non-existent key')
#print(f"The result is {result}")

def normal_function():
    print("Congratulations! This one does exist!")
    return True

def another_function():
    print("Looks like this was also a valid key!")

def default_function():
    print("You got here because you called a key that does not exist")


dict_with_functions = {
    "normal_function": normal_function,
    "another_function": another_function
}

#dict_with_functions["normal_function"]()
#dict_with_functions.get("another_function")()
#dict_with_functions.get("this one is not there", default_function)()

#print(filled_dictionary)
#result = filled_dictionary.popitem()
#print(result)
#print(filled_dictionary)
#filled_dictionary.pop("age")
#print(filled_dictionary)
# This one will raise a KeyError exception
#filled_dictionary.pop("profession")
#filled_dictionary.popitem()
#print(filled_dictionary)

new_dictionary = {
    "Sunday": 1,
    "Monday": 2,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saturday": 7
}

pop_list = []
for day in new_dictionary:
    if "S" in day:
        pop_list.append(day)

for day in pop_list:
    new_dictionary.pop(day)
#print(new_dictionary)

print(users_dictionary)
for user in users_dictionary.values():
    # Check if user contains a key called "lastname"
    if "lastname" in user:
        # if so, delete the key
        user.pop("lastname")
    else:
        print(user)
print(users_dictionary)
