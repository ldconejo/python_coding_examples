import random

def read_temperature():
    return random.randint(-10, 110)

def convert_to(value, units):
    if units == 'Celsius':
        value_in_celsius = (value - 32) * 5 / 9
        return value_in_celsius
    value_in_fahrenheit = value * 9 / 5 + 32
    return value_in_fahrenheit