def ask_questions():
    questions = [

        {'id': 'customer', 'text': 'Name of the customer: ', 'validators': [validate_not_blank]},
        #{'description': 'Package description: '},
        #'Are the contents dangerous? [Y/N] ',
        #'Weight (kgs): ',
        #'Volume (cubic meters): ',
        #'Required delivery date (month/date/year): ',
        #'International destination? [Y/N] '
    ]

    response_dictionary = {}

    for question in questions:
        response = input(question["text"])
        for validator in question["validators"]:
            if not validator(response):
                print("nope!")
                break
        response_dictionary[question["id"]] = response

    return response_dictionary

def validate_not_blank(response):
    if response.strip() == "":
        return False
    return True

def validate_answers(response_dictionary):
    pass

if __name__ == "__main__":
    result = ask_questions()
    print(result)