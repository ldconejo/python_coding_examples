import temperature_sensor

def get_user_info():
    name = input('What is your name?')
    return name

def get_current_temperature():
    current_temp = temperature_sensor.read_temperature()
    if 70 < current_temp < 80:
        return f'Nice temperature, {current_temp}F!'
    if current_temp < 0:
        raise SystemError
    return f'Tough weather, {current_temp}F'
