# Example from: https://www.geeksforgeeks.org/memoization-using-decorators-in-python/
# Reproduced here for academic purposes
#  Factorial program with memoization using 
# decorators. 
  
# A decorator function for function 'f' passed 
# as parameter 
def memoize_factorial(f): 
    memory = {} 
  
    # This inner function has access to memory 
    # and 'f' 
    def inner(num): 
        if num not in memory: 
            print(f"{num} NOT in memory")         
            memory[num] = f(num)
        else: 
            print(f"{num} was already in memory")
        return memory[num] 
  
    return inner 
      
@memoize_factorial
def facto(num): 
    if num == 1: 
        return 1
    else: 
        return num * facto(num-1) 