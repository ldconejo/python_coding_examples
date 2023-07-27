import sys
import main
from loguru import logger
logger.remove()
logger.add("log_file_{time:YYYY_MMM_DD}.log")
logger.add(sys.stderr, level='INFO')
logger.info("Hey, the logger is working!!!")
logger.error("It will let you know if things go wrong")
logger.debug("It can also show you debug messages")

if __name__ == '__main__':
    logger.debug('Program started normally')
    print("Welcome to the Current Weather")
    temp_phrase, current_temp = main.get_current_temperature()
    print(temp_phrase)
    print(main.perform_conversion(current_temp, 'Celsius'))