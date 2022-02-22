def adding_params(func):
    def wrapper(*args, **kwargs):
        print(f"Log level: {args[-1]}")
        # Removing the extra parameter, so that 
        # the decorated function does not complain
        args = args[:-1]
        result = func(*args, **kwargs)
        return result
    return wrapper

@adding_params
def first_original_function(num1, num2):
    result = num1 + num2
    print(f"The result is {result}")

def second_adding_params(func):
    def wrapper(*args, **kwargs):
        logging_level = kwargs["log_level"]
        print(f"Log level: {logging_level}")
        # Sending only the unnamed arguments to
        # the decorated function, you could also
        # delete the extra key and send a sanitized
        # kwargs
        result = func(*args)
        return result
    return wrapper

@second_adding_params
def second_original_function(num1, num2):
    result = num1 + num2
    print(f"The result is {result}")

if __name__ == '__main__':
    first_original_function(3,4,5)
    second_original_function(3,4,log_level=5)
