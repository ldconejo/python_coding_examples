import temperature_sensor

def get_current_temperature():
    current_temp = temperature_sensor.read_temperature()
    if 70 < current_temp < 80:
        return f'Nice temperature, {current_temp}F!'
    if current_temp < 0:
        raise SystemError
    return f'Tough weather, {current_temp}F'

def perform_conversion(value, units):
    if units == 'Celsius':
        original_units = 'Fahrenheit'
        result = temperature_sensor.convert_to(value, 'Celsius')
    elif units == 'Fahrenheit':
        original_units = 'Celsius'
        result = temperature_sensor.convert_to(value, 'Fahrenheit')
        #result = temperature_sensor.convert_to(value)
    return f"A reading of {value} degrees {original_units} is equivalent to {int(result)} degrees {units}"
