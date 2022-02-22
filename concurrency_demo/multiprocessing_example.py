#!/usr/bin/env python3

from time import sleep, time
from multiprocessing import Process
from math_operation import math_loop

def perform_calculation(calculation_name, cycles=50000000, number=103):
    result = math_loop(cycles, number)
    print(f"The result from {calculation_name} was {result}")

def main(): 
    calculation_list = ['calculation 01', 'calculation 02', 'calculation 03']
    processes = []

    for calculation in calculation_list:
        process = Process(target=perform_calculation, args=(calculation,))
        process.start()
        processes.append(process)
   
    for process in processes:
        process.join()

if __name__ == '__main__':
    start_time = time()
    main()
    elapsed_time = time() - start_time
    print(f"Elapsed time: {elapsed_time}")
