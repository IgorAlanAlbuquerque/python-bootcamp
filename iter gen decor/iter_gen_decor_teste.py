# %% [markdown]
# # Module: Iterators, Generators, and Decorators Assignments
# ## Lesson: Iterators, Generators, and Decorators
# ### Assignment 1: Custom Iterator
# 
# Create a custom iterator class named `Countdown` that takes a number and counts down to zero. Implement the `__iter__` and `__next__` methods. Test the iterator by using it in a for loop.

# %%
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current

for number in Countdown(5):
    print(number)

# %% [markdown]
# ### Assignment 2: Custom Iterable Class
# 
# Create a class named `MyRange` that mimics the behavior of the built-in `range` function. Implement the `__iter__` and `__next__` methods. Test the class by using it in a for loop.

# %%
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for number in MyRange(1, 5):
    print(number)

# %% [markdown]
# ### Assignment 3: Generator Function
# 
# Write a generator function named `fibonacci` that yields the Fibonacci sequence. Test the generator by iterating over it and printing the first 10 Fibonacci numbers.

# %%
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# %% [markdown]
# ### Assignment 4: Generator Expression
# 
# Create a generator expression that generates the squares of numbers from 1 to 10. Iterate over the generator and print each value.

# %%
squares = (x * x for x in range(1, 11))

for square in squares:
    print(square)

# %% [markdown]
# ### Assignment 5: Chaining Generators
# 
# Write two generator functions: `even_numbers` that yields even numbers up to a limit, and `squares` that yields the square of each number from another generator. Chain these generators to produce the squares of even numbers up to 20.

# %%
def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

def squares(numbers):
    for number in numbers:
        yield number * number

even_gen = even_numbers(20)
square_gen = squares(even_gen)
for square in square_gen:
    print(square)

# %% [markdown]
# ### Assignment 6: Simple Decorator
# 
# Write a decorator named `time_it` that measures the execution time of a function. Apply this decorator to a function that calculates the factorial of a number.

# %%
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@time_it
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))

# %% [markdown]
# ### Assignment 7: Decorator with Arguments
# 
# Write a decorator named `repeat` that takes an argument `n` and repeats the execution of the decorated function `n` times. Apply this decorator to a function that prints a message.

# %%
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def print_message(message):
    print(message)

print_message("Hello, World!")

# %% [markdown]
# ### Assignment 8: Nested Decorators
# 
# Write two decorators: `uppercase` that converts the result of a function to uppercase, and `exclaim` that adds an exclamation mark to the result of a function. Apply both decorators to a function that returns a greeting message.

# %%
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@uppercase
@exclaim
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# %% [markdown]
# ### Assignment 9: Class Decorator
# 
# Create a class decorator named `singleton` that ensures a class has only one instance. Apply this decorator to a class named `DatabaseConnection` and test it.

# %%
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Database connection created")

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True

# %% [markdown]
# ### Assignment 10: Iterator Protocol with Decorators
# 
# Create a custom iterator class named `ReverseString` that iterates over a string in reverse. Write a decorator named `uppercase` that converts the string to uppercase before reversing it. Apply the decorator to the `ReverseString` class.

# %%
def uppercase(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.data = self.data.upper()
    return Wrapped

@uppercase
class ReverseString:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for char in ReverseString("hello"):
    print(char)

# %% [markdown]
# ### Assignment 11: Stateful Generators
# 
# Write a stateful generator function named `counter` that takes a start value and increments it by 1 each time it is called. Test the generator by iterating over it and printing the first 10 values.

# %%
def counter(start):
    current = start
    while True:
        yield current
        current += 1

count = counter(0)
for _ in range(10):
    print(next(count))

# %% [markdown]
# ### Assignment 12: Generator with Exception Handling
# 
# Write a generator function named `safe_divide` that takes a list of numbers and yields the division of each number by a given divisor. Implement exception handling within the generator to handle division by zero.

# %%
def safe_divide(numbers, divisor):
    for number in numbers:
        try:
            yield number / divisor
        except ZeroDivisionError:
            yield "Error: Division by zero"

numbers = [10, 20, 30, 40]
for result in safe_divide(numbers, 0):
    print(result)

# %% [markdown]
# ### Assignment 13: Context Manager Decorator
# 
# Write a decorator named `open_file` that manages the opening and closing of a file. Apply this decorator to a function that writes some text to a file.

# %%
def open_file(file_name, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_name, mode) as file:
                return func(file, *args, **kwargs)
        return wrapper
    return decorator

@open_file('sample.txt', 'w')
def write_to_file(file, text):
    file.write(text)

write_to_file('Hello, World!')

# %% [markdown]
# ### Assignment 14: Infinite Iterator
# 
# Create an infinite iterator class named `InfiniteCounter` that starts from a given number and increments by 1 indefinitely. Test the iterator by printing the first 10 values generated by it.

# %%
class InfiniteCounter:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current

counter = InfiniteCounter(0)
for _ in range(10):
    print(next(counter))

# %% [markdown]
# ### Assignment 15: Generator Pipeline
# 
# Write three generator functions: `integers` that yields integers from 1 to 10, `doubles` that yields each integer doubled, and `negatives` that yields the negative of each doubled value. Chain these generators to create a pipeline that produces the negative doubled values of integers from 1 to 10.

# %%
def integers():
    for i in range(1, 11):
        yield i

def doubles(numbers):
    for number in numbers:
        yield number * 2

def negatives(numbers):
    for number in numbers:
        yield -number

int_gen = integers()
double_gen = doubles(int_gen)
negative_gen = negatives(double_gen)
for value in negative_gen:
    print(value)


