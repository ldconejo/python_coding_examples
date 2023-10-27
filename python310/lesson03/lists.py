ages = [42,6,23,7]
age = []
names = ["Paul", "Elisa", "Luis"]
names[1] = "Rosa"
combined = ["Paul", 1, 2.6, ["a", "b"]]

def test_function(name="Luis"):
    print(f"Hey, I'm here, {name}")

def find_all_occurrences(target_character, test_string):
    current_index = 0
    results = []
    for character in test_string:
        if character == target_character:
            #print(f"Found {target_character} at index {current_index}")
            results.append(current_index)
        #current_index = current_index + 1
        current_index += 1
    return results

def for_loop_example_1():
    for cat in "this is a string":
        print(cat)

def for_loop_example_2():
    test_list = [0, 2, 5, 1, "a", "hello"]
    for element in test_list:
        print(element)
        if element == "a":
            print("We found the a!!!")
            break

def for_loop_example_3():
    new_list = [0, 2, 3, 5, 1, 3, 52, 2, 75, 122]
    for element in new_list:
        print(element)
        if element > 50:
            continue
        print("This will not happen for numbers greater than 50")

if __name__ == "__main__":
    #test_function()
    #test_list = [0, 1, "hello", test_function]
    #test_list[3]("Paul")
    #sample_string = 'This is just some string I came up with'
    #index_of_occurrences = find_all_occurrences("u", sample_string)
    #print(f"Target character found at the following indexes: {index_of_occurrences}")
    for_loop_example_3()