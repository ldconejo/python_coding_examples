def printing_decorator(func):
    def wrapper(*args, **kwargs):
        list_output = func(*args, **kwargs)
        return f"My favorite dessert is {list_output[0]} {list_output[1]} {list_output[2]}"
    return wrapper

@printing_decorator
def turn_into_list(color, fruit, dish):
    return [color, fruit, dish]

if __name__ == '__main__':
    print(turn_into_list("blue", "berry", "muffin"))