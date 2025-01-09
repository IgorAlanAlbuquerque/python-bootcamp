# Module 4: Advanced Functions Assignments
## Lesson 4.1: Defining Functions
### Assignment 1: Fibonacci Sequence with Memoization

#Define a recursive function to calculate the nth Fibonacci number using memoization. Test the function with different inputs.

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print("questao 1")
print(fibonacci(10))
print(fibonacci(15))

### Assignment 2: Function with Nested Default Arguments

#Define a function that takes two arguments, a and b, where b is a dictionary with a default value of an empty dictionary. The function should add a new key-value pair to the dictionary and return it. Test the function with different inputs.

def add_to_dict(a, b=None):
    if b is None:
        b = {}
    b[a] = a**2
    return b

print("questao 2")
print(add_to_dict(2))
print(add_to_dict(3, {1: 1}))

### Assignment 3: Function with Variable Keyword Arguments

#Define a function that takes a variable number of keyword arguments and returns a dictionary containing only those key-value pairs where the value is an integer. Test the function with different inputs.

def filter_integers(**kwargs):
    return {k: v for k, v in kwargs.items() if isinstance(v, int)}

print("questao 3")
print(filter_integers(a=1, b='two', c=3, d=4.5))
print(filter_integers(x=10, y='yes', z=20))

### Assignment 4: Function with Callback

#Define a function that takes another function as a callback and a list of integers. The function should apply the callback to each integer in the list and return a new list with the results. Test with different callback functions.

def apply_callback(callback, lst):
    return [callback(x) for x in lst]

print("questao 4")
print(apply_callback(lambda x: x**2, [1, 2, 3, 4]))
print(apply_callback(lambda x: x+1, [1, 2, 3, 4]))

### Assignment 5: Function that Returns a Function

#Define a function that returns another function. The returned function should take an integer and return its square. Test the returned function with different inputs.

def outer_function():
    def inner_function(x):
        return x ** 2
    return inner_function

square = outer_function()
print("questao 5")
print(square(2))
print(square(5))

### Assignment 6: Function with Decorators

#Define a function that calculates the time taken to execute another function. Apply this decorator to a function that performs a complex calculation. Test the decorated function with different inputs.

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def complex_calculation(n):
    return sum(x**2 for x in range(n))

print("questao 6")
print(complex_calculation(10000))

### Assignment 7: Higher-Order Function for Filtering and Mapping

#Define a higher-order function that takes two functions, a filter function and a map function, along with a list of integers. The higher-order function should first filter the integers using the filter function and then apply the map function to the filtered integers. Test with different filter and map functions.

def filter_and_map(filter_func, map_func, lst):
    return [map_func(x) for x in lst if filter_func(x)]

print("questao 7")
print(filter_and_map(lambda x: x % 2 == 0, lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(filter_and_map(lambda x: x > 2, lambda x: x + 1, [1, 2, 3, 4, 5]))

### Assignment 8: Function Composition

#Define a function that composes two functions, f and g, such that the result is f(g(x)). Test with different functions f and g.

def compose(f, g):
    return lambda x: f(g(x))

f = lambda x: x + 1
g = lambda x: x * 2
h = compose(f, g)
print("questao 8")
print(h(3))
print(h(5))

### Assignment 9: Partial Function Application

#Use the functools.partial function to create a new function that multiplies its input by 2. Test the new function with different inputs.

from functools import partial

multiply_by_2 = partial(lambda x, y: x * y, 2)

print("questao 9")
print(multiply_by_2(3))
print(multiply_by_2(5))

### Assignment 10: Function with Error Handling

#Define a function that takes a list of integers and returns their average. The function should handle any errors that occur (e.g., empty list) and return None in such cases. Test with different inputs.

def average(lst):
    try:
        return sum(lst) / len(lst)
    except ZeroDivisionError:
        return None

print("questao 10")
print(average([1, 2, 3, 4, 5]))
print(average([]))

### Assignment 11: Function with Generators

#Define a function that generates an infinite sequence of Fibonacci numbers. Test by printing the first 10 numbers in the sequence.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
print("questao 11")
for _ in range(10):
    print(next(fib_gen))
    
### Assignment 12: Currying

#Define a curried function that takes three arguments, one at a time, and returns their product. Test the function by providing arguments one at a time.

def curry_product(x):
    def inner1(y):
        def inner2(z):
            return x * y * z
        return inner2
    return inner1
print("questao 12")
print(curry_product(2)(3)(4))
print(curry_product(1)(5)(6))

### Assignment 13: Function with Context Manager

#Define a function that uses a context manager to write a list of integers to a file. The function should handle any errors that occur during file operations. Test with different lists.

def write_to_file(lst, filename):
    try:
        with open(filename, 'w') as f:
            for num in lst:
                f.write(f"{num}\n")
    except IOError as e:
        print(f"An error occurred: {e}")

print("questao 13")
write_to_file([1, 2, 3, 4, 5], 'output.txt')

### Assignment 14: Function with Multiple Return Types

#Define a function that takes a list of mixed data types (integers, strings, and floats) and returns three lists: one containing all the integers, one containing all the strings, and one containing all the floats. Test with different inputs.

def separate_types(lst):
    ints, strs, floats = [], [], []
    for item in lst:
        if isinstance(item, int):
            ints.append(item)
        elif isinstance(item, str):
            strs.append(item)
        elif isinstance(item, float):
            floats.append(item)
    return ints, strs, floats

print("questao 14")
print(separate_types([1, 'a', 2.5, 3, 'b', 4.0, 'c']))

### Assignment 15: Function with State

#Define a function that maintains state between calls using a mutable default argument. The function should keep track of how many times it has been called. Test by calling the function multiple times.

def call_counter(counter={'count': 0}):
    counter['count'] += 1
    return counter['count']

print("questao 15")
print(call_counter()) 
print(call_counter())
print(call_counter())