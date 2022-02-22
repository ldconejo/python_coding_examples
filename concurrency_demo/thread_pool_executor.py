import time
import random
from concurrent.futures import ThreadPoolExecutor

def just_wait(thread_number):
    print(f"Thread {thread_number} started")
    time.sleep(random.randint(1,5))
    print(f"Thread {thread_number} finished")


executor = ThreadPoolExecutor(max_workers=2)
for i in range(5):
    executor.submit(just_wait, i)