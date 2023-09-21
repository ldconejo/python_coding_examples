import traceback

class Context():

    # Triggered when an instance of the context manager is created
    def __init__(self, handle_error):
        print("Context manager has been initialized")
        if handle_error:
            print("Context manager will handle errors")
        self.handle_error = handle_error

    # Triggered when the "with" statement is called for the instance of the context manager
    def __enter__(self):
        print("Entering context manager")
        self.name = "Happy, lazy context manager"
        return self
    
    # Triggered when we 'exit' the context of the context manager
    def __exit__(self, exception_type, exception_value, exception_traceback):
        print('Exiting context manager')
        print(f"Exception type: {exception_type}")
        print(f"Exception value: {exception_value}")
        print(f"Exception traceback: {exception_traceback}")
        return self.handle_error
    
if __name__ == "__main__":
    this_cm = Context(handle_error=True)

    with this_cm as test:
        print(f"Handle error is set to: {test.handle_error}")
        print(f"The name of this context manager is {test.name}")
        print("We are inside of the context manager")
        print("We are still inside of the context manager")
        #raise RuntimeError("This is the error message")
        #1/0
    print("We are outside of the context manager")