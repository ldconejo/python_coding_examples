from pysnooper import snoop

def print_weather_report(filename):
    try:
        with open(filename, 'r') as demo_file:
            for line in demo_file:
                fields = line.split(',')
                city = fields[0]
                temperature = int(fields[1])
                print(f"The temperature in {city} is {temperature}C")
        while True:
            pass
    except KeyboardInterrupt:
        raise ValueError
    except FileNotFoundError:
        print("ERROR: File not found")
    except Exception as exception_description:
        print(f"THIS IS THE END OF THE WORLD!!!!: An unexpected issue occurred: {exception_description}")

if __name__ == "__main__":
    print_weather_report('weather.txt')