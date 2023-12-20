import logging
import pysnooper

logging.basicConfig(level=logging.DEBUG)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('example2.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def add(x, y):
    logger.info(f"Adding {x} and {y}")
    return x + y

@pysnooper.snoop()
def divide(x, y):
    logger.info(f"Dividing {x} by {y}")
    try:
        return x / y
    except ZeroDivisionError:
        logger.error("Division by zero")
        raise

if __name__ == "__main__":
    result1 = add(3, 5) 
    result2 = divide(10, 0)