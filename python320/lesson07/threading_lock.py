import threading

x_lock = threading.Lock()

def thread_worker(thread_name):
    with x_lock:
        with open('test2.txt', 'a') as file:
            file.write(f"Thread {thread_name} is now writing to this file!\n")

if __name__ == '__main__':
    thread_names = ['first', 'second', 'third', 'fourth']
    for thread_name in thread_names:
        thread = threading.Thread(target=thread_worker, args=(thread_name,))
        thread.start()