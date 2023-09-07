from math import sqrt
from time import time

def math_loop(cycles=50000000, number=103, current_cycle=0):
    while current_cycle < cycles:
        number = sqrt(number)
        current_cycle += 1
    return number

if __name__ == '__main__':
    start_time = time()
    math_loop()
    math_loop()
    math_loop()
    elapsed_time = time() - start_time
    print(f"Elapsed time: {elapsed_time}")