def memoize_factorial(f):
    memory = {}

    def inner(num):
        if num not in memory:
            print(f"Factorial {num} NOT in memory")
            memory[num] = f(num)
        else:
            print(f"Factorial {num} was already in memory")
        return memory[num]
    
    return inner

@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)

@memoize_factorial  
def square_number(num):
    return num*num