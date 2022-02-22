import argparse

DEBUG = None
SKY = None

def parse_cmd_arguments():
    """ this function parses the command line arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--color',
                        help='Color of the sky',
                        required=True)
    parser.add_argument('-d',
                        '--debug',
                        action='store_true',
                        help='Debug mode, forces the sky to gray',
                        required=False)

    return parser.parse_args()

def debug_decorator(func):
    """
    Function to temporarily turn on debug mode
    """
    def wrapper(*args, **kwargs):
        if DEBUG:
            global SKY
            original_color = SKY
            SKY = "gray"
            func(*args, **kwargs)
            SKY = original_color
        else:
            func(*args, **kwargs)

    return wrapper

def sky_color():
    print(f"The color of the sky is {SKY}")

@debug_decorator
def sky_color_debug():
    print(f"The color of the sky is {SKY}")

if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    DEBUG = ARGS.debug if ARGS.debug else None
    SKY = ARGS.color
    sky_color_debug()
    sky_color()



