from loguru import logger
import temperature_sensor

def get_current_temperature():
    logger.debug('Running a temperature measurement')
    current_temp = temperature_sensor.read_temperature()
    if 70 < current_temp < 80:
        return f'Nice temperature, {current_temp}F!', current_temp
    if current_temp < 0:
        raise SystemError
    return f'Tough weather, {current_temp}F', current_temp

def perform_conversion(value, units):
    logger.debug('Performing a temperature conversion')
    if units == 'Celsius':
        original_units = 'Fahrenheit'
        result = temperature_sensor.convert_to(value, units)
    elif units == 'Fahrenheit':
        original_units = 'Celsius'
        result = temperature_sensor.convert_to(value, units)
    return f"A reading of {value} degrees {original_units} is equivalent to {int(result)} degrees {units}"