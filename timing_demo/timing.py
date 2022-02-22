from time import process_time



def my_timer(func):

    def timer_wrap(*args, **kwargs):
        start_time = process_time()
        return_value = func(*args, **kwargs)
        elapsed_time = process_time() - start_time
        # do something with the elapsed_time
        return elapsed_time
    return timer_wrap



@my_timer
def some_function():
    result = 1
    for i in range(1,1000000):
        result *= (i + 1)/i
    return result

# Same function as above, but not decorated
def some_other_function():
    result = 1
    for i in range(1,1000000):
        result *= (i + 1)/i
    return result


def function_with_its_own_timer():
    start_time = process_time()
    return_value = some_other_function()
    elapsed_time = process_time() - start_time
    # do something with the elapsed_time
    return elapsed_time

if __name__ == "__main__":
    total_decorated = 0
    total_non_decorated = 0
    for iteration in range(10):
        total_decorated += some_function()
        total_non_decorated += function_with_its_own_timer()
    print(f"Decorated total time: {total_decorated}")
    print(f"Non-decorated total time: {total_non_decorated}")