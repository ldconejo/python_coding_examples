import random
import asyncio
import queue
import time
from types import coroutine

@coroutine
def process_file(filename):
    print(f"Fetching {filename}")
    yield
    print(f"{filename} has been processed")

async def async_pool(limit, filename_queue):
    for i in range(limit):
        filename = filename_queue.get()
        await process_file(filename)

if __name__ == "__main__":
    file_queue = queue.Queue()
    runner = async_pool(3, file_queue)
    file_queue.put('first_file.txt')
    runner.send(None)
    file_queue.put('second_file.txt')
    runner.send(None)
    file_queue.put('third_file.txt')
    runner.send(None)
    file_queue.put('fourth_file.txt')
    runner.send(None)