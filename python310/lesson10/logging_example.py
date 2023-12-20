import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

def add(x, y):
    logging.info(f"Adding {x} and {y}")
    return x + y

def divide(x, y):
    logging.info(f"Dividing {x} by {y}")
    try:
        return x / y
    except ZeroDivisionError:
        logging.error("Division by zero")
        raise

if __name__ == "__main__":
    result1 = add(3, 5)
    result2 = divide(10, 0)