from contextlib import contextmanager

@contextmanager
def context(handle_error):
    print("Context manager has been initialized")
    if handle_error:
        print("Context manager will automatically handle exceptions")

    try:
        print("Entering context manager")
        yield object()
    except Exception as e:
        print(e)
        if not handle_error:
            raise e
    finally:
        print("Exiting context manager")

if __name__ == "__main__":
    my_cm = context(True)
    with my_cm:
        print('We are inside the context manager')
        3/0