from csv import DictReader

with open("sample.csv") as file:
    list_of_dictionary_rows = DictReader(file)
    for dictionary in list_of_dictionary_rows:
        print(dictionary)
        print(dictionary['name'])