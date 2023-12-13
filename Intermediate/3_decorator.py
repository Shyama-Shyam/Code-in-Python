'''
Decorators are a very powerful and useful tool in Python since it allows programmers 
to modify the behaviour of a function or class. Decorators allow us to wrap another 
function in order to extend the behaviour of the wrapped function, without permanently modifying it.
'''

import time

def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        # Do something after the original function is called
        end = time.time()
        elapsed = end - start
        print(f"{func.__name__} took {elapsed} seconds to run.")
        return result
    return wrapper

@record_time
def add(x, y):
    print(f"Original function called with arguments: {x}, {y}")
    time.sleep(1)
    return x + y

result = add(3, 4)
print(f"Result: {result}")


#parameters to decorators
def decorator_func(x, y):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            # Do something before the original function is called
            result = func(*args, **kwargs)
            # Do something after the original function is called
            return result
        return wrapper
    return inner_decorator

@decorator_func(10, 20)
def example_function(a, b):
    print(f"Original function called with arguments: {a}, {b}")
    return a + b

result = example_function(3, 4)
print(f"Result: {result}")
