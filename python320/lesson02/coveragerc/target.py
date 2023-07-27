import temperature_sensor

def get_current_temperature():
    current_temp = temperature_sensor.read_temperature()
    return f"Current temperature is {current_temp}"

if __name__ == '__main__':
    print(get_current_temperature())