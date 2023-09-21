import inflect

p = inflect.engine()

def convert_to_text(number):
    return p.number_to_words(number)

def return_as_text(func):
    def text_result(*args, **kwargs):
        try:
            for value in args:
                float(value)
            for key, value in kwargs:
                float(value)
            numeric_result = func(*args, **kwargs)
            return convert_to_text(numeric_result)
        except:
            return "ERROR: Value provided is not numeric"
    return text_result

@return_as_text
def multiply(first_value, second_value):
    return first_value * second_value

@return_as_text
def add(first_value, second_value):
    return first_value + second_value

@return_as_text
def square(single_value):
    return single_value * single_value

if __name__ == '__main__':
    operation = multiply(21,2)
    print(operation)
    operation = add(first_value=21,second_value=2)
    print(operation)
    #multiply_text = return_as_text(multiply)
    #print(multiply_text(43,54))
    #print(return_as_text(multiply)(43,54))
    operation = square("hello")
    print(operation)
