import random

def hex_decorator(func):
    def wrapper(*args, **kwargs):
            decimal_value = func(*args, **kwargs)
            if decimal_value < 10:
                return str(decimal_value)
            hex_values = ['A', 'B', 'C', 'D', 'E', 'F']
            return hex_values[decimal_value - 10]
    return wrapper

#@hex_decorator
def return_number():
    return random.randint(0, 15)

if __name__ == "__main__":
    print(f"The value returned is {return_number()}")