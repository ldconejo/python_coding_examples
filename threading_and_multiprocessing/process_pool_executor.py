from time import time
from concurrent.futures import ProcessPoolExecutor
from math_operation import math_loop

def perform_calculation(calculation_name, cycles=50000000, number=103):
    print(f"Launching calculation {calculation_name}")
    result = math_loop(cycles, number)
    print(f"The result from {calculation_name} was {result}")

if __name__ == '__main__':
    start_time = time()
    executor = ProcessPoolExecutor(max_workers=20)
    for i in range(20):
        name = 'calculation ' + str(i)
        executor.submit(perform_calculation, name)
    executor.shutdown(wait=True)
    elapsed_time = time() - start_time
    print(f"Elapsed time: {elapsed_time}")