def get_number():
    ssn_number = input("What is your SSN (don't give me a real one!): ")
    if len(ssn_number) > 8:
        return "Invalid SSN"
    return ssn_number

def get_personal_data():
    name = input("What is your name? ")
    last_name = input("What is your last name? ")
    return name, last_name

def validate_number(ssn_number):
    if len(ssn_number) != 8:
        return False
    return True

if __name__ == "__main__":
    ssn_number = get_number()
    print(validate_number(ssn_number))