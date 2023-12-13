'''
This project will take multiple name formats and figure out
useful things such as what part of a long name is the name,
middle name and last name
'''

def simplify_name(name):
    ''''
    This function will take any name format and output a name and last name
    '''
    # Split the name into a list, using space as divider
    try:
        name_list = name.split(" ")
    except AttributeError:
        return "Invalid Name"

    # This is for a name with four elements (name, middle name and two last names)
    name_size = len(name_list)
    if name_size == 4:
        name = name_list[0]
        last_name = name_list[2]
    # Case in which you have name, middle name and one last name
    elif name_size == 3:
        name = name_list[0]
        last_name = name_list[2]
    elif name_size == 2:
        name = name_list[0]
        last_name = name_list[1]
    else:
        return "Invalid Name"
    return f"{name} {last_name}"

def deconstruct_name(name):
    '''
    This function will take a name string and return a dictionary with first name
    middle name, first last name and second last name
    '''
    name_list = name.split(" ")
    name_size = len(name_list)

    name_dictionary = {}
    if name_size == 4:
        name_dictionary["name"] = name_list[0]
        name_dictionary["middle_name"] = name_list[1]
        name_dictionary["last_name_1"] = name_list[2]
        name_dictionary["last_name_2"] = name_list[3]

    return name_dictionary