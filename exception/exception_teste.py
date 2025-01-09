# %% [markdown]
# # Module: Exception Handling Assignments
# ## Lesson: Exception Handling with try, except, and finally
# ### Assignment 1: Handling Division by Zero
# 
# Write a function that takes two integers as input and returns their division. Use try, except, and finally blocks to handle division by zero and print an appropriate message.

# %%
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        result = None
    finally:
        print("Execution complete.")
    return result

print(divide(10, 2))
print(divide(10, 0))

# %% [markdown]
# ### Assignment 2: File Reading with Exception Handling
# 
# Write a function that reads the contents of a file named `data.txt`. Use try, except, and finally blocks to handle file not found errors and ensure the file is properly closed.

# %%
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        try:
            file.close()
        except NameError:
            pass

print(read_file('data.txt'))

# %% [markdown]
# ### Assignment 3: Handling Multiple Exceptions
# 
# Write a function that takes a list of integers and returns their sum. Use try, except, and finally blocks to handle TypeError if a non-integer value is encountered and print an appropriate message.

# %%
def sum_list(lst):
    total = 0
    try:
        for item in lst:
            total += item
    except TypeError as e:
        print(f"Error: {e}")
        total = None
    finally:
        print("Execution complete.")
    return total

print(sum_list([1, 2, 3, 'a']))
print(sum_list([1, 2, 3, 4]))

# %% [markdown]
# ### Assignment 4: Exception Handling in User Input
# 
# Write a function that prompts the user to enter an integer. Use try, except, and finally blocks to handle ValueError if the user enters a non-integer value and print an appropriate message.

# %%
def get_integer():
    try:
        value = int(input("Enter an integer: "))
    except ValueError as e:
        print(f"Error: {e}")
        value = None
    finally:
        print("Execution complete.")
    return value

print(get_integer())

# %% [markdown]
# ### Assignment 5: Exception Handling in Dictionary Access
# 
# Write a function that takes a dictionary and a key as input and returns the value associated with the key. Use try, except, and finally blocks to handle KeyError if the key is not found in the dictionary and print an appropriate message.

# %%
def get_dict_value(d, key):
    try:
        value = d[key]
    except KeyError as e:
        print(f"Error: {e}")
        value = None
    finally:
        print("Execution complete.")
    return value

d = {'a': 1, 'b': 2, 'c': 3}
print(get_dict_value(d, 'b'))  # 2
print(get_dict_value(d, 'x'))  # None

# %% [markdown]
# ### Assignment 6: Nested Exception Handling
# 
# Write a function that performs nested exception handling. It should first attempt to convert a string to an integer, and then attempt to divide by that integer. Use nested try, except, and finally blocks to handle ValueError and ZeroDivisionError and print appropriate messages.

# %%
def nested_exception_handling(s):
    try:
        try:
            num = int(s)
        except ValueError as e:
            print(f"Conversion error: {e}")
            num = None
        finally:
            print("Conversion attempt complete.")
        if num is not None:
            try:
                result = 10 / num
            except ZeroDivisionError as e:
                print(f"Division error: {e}")
                result = None
            finally:
                print("Division attempt complete.")
            return result
    finally:
        print("Overall execution complete.")

print(nested_exception_handling('0'))  # None
print(nested_exception_handling('a'))  # None
print(nested_exception_handling('2'))  # 5.0

# %% [markdown]
# ### Assignment 7: Exception Handling in List Operations
# 
# Write a function that takes a list and an index as input and returns the element at the given index. Use try, except, and finally blocks to handle IndexError if the index is out of range and print an appropriate message.

# %%
def get_list_element(lst, index):
    try:
        element = lst[index]
    except IndexError as e:
        print(f"Error: {e}")
        element = None
    finally:
        print("Execution complete.")
    return element

lst = [1, 2, 3, 4, 5]
print(get_list_element(lst, 2))  # 3
print(get_list_element(lst, 10))  # None

# %% [markdown]
# ### Assignment 8: Exception Handling in Network Operations
# 
# Write a function that attempts to open a URL and read its contents. Use try, except, and finally blocks to handle network-related errors and print an appropriate message.

# %%
import requests

def read_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None
    finally:
        print("Execution complete.")

print(read_url('https://jsonplaceholder.typicode.com/posts/1'))
print(read_url('https://nonexistent.url'))

# %% [markdown]
# ### Assignment 9: Exception Handling in JSON Parsing
# 
# Write a function that attempts to parse a JSON string. Use try, except, and finally blocks to handle JSONDecodeError if the string is not a valid JSON and print an appropriate message.

# %%
import json

def parse_json(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
        return None
    finally:
        print("Execution complete.")

# Test
# print(parse_json('{"name": "John", "age": 30}'))  # {'name': 'John', 'age': 30}
# print(parse_json('Invalid JSON'))  # None

# %% [markdown]
# ### Assignment 10: Custom Exception Handling
# 
# Define a custom exception named `NegativeNumberError`. Write a function that raises this exception if a negative number is encountered in a list. Use try, except, and finally blocks to handle the custom exception and print an appropriate message.

# %%
class NegativeNumberError(Exception):
    pass

def check_for_negatives(lst):
    try:
        for num in lst:
            if num < 0:
                raise NegativeNumberError(f"Negative number found: {num}")
    except NegativeNumberError as e:
        print(f"Error: {e}")
    finally:
        print("Execution complete.")

# Test
# check_for_negatives([1, -2, 3, 4])  # Error: Negative number found: -2
# check_for_negatives([1, 2, 3, 4])  # Execution complete.

# %% [markdown]
# ### Assignment 11: Exception Handling in Function Calls
# 
# Write a function that calls another function which may raise an exception. Use try, except, and finally blocks to handle the exception and print an appropriate message.

# %%
def risky_function():
    raise ValueError("An error occurred in risky_function.")

def safe_function():
    try:
        risky_function()
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Execution complete.")

# Test
# safe_function()  # Error: An error occurred in risky_function.

# %% [markdown]
# ### Assignment 12: Exception Handling in Class Methods
# 
# Define a class with a method that performs a division operation. Use try, except, and finally blocks within the method to handle division by zero and print an appropriate message.

# %%
class Calculator:
    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            result = None
        finally:
            print("Execution complete.")
        return result

# Test
# calc = Calculator()
# print(calc.divide(10, 2))  # 5.0
# print(calc.divide(10, 0))  # None

# %% [markdown]
# ### Assignment 13: Exception Handling in Data Conversion
# 
# Write a function that takes a list of strings and converts them to integers. Use try, except, and finally blocks to handle ValueError if a string cannot be converted and print an appropriate message.

# %%
def convert_to_integers(lst):
    integers = []
    try:
        for item in lst:
            integers.append(int(item))
    except ValueError as e:
        print(f"Error: {e}")
        integers = None
    finally:
        print("Execution complete.")
    return integers

# Test
# print(convert_to_integers(['1', '2', 'three', '4']))  # None
# print(convert_to_integers(['1', '2', '3', '4']))  # [1, 2, 3, 4]

# %% [markdown]
# ### Assignment 14: Exception Handling in List Comprehensions
# 
# Write a function that uses a list comprehension to convert a list of strings to integers. Use try, except, and finally blocks within the list comprehension to handle ValueError and print an appropriate message.

# %%
def convert_with_comprehension(lst):
    try:
        integers = [int(item) for item in lst]
    except ValueError as e:
        print(f"Error: {e}")
        integers = None
    finally:
        print("Execution complete.")
    return integers

print(convert_with_comprehension(['1', '2', 'three', '4']))  # None
print(convert_with_comprehension(['1', '2', '3', '4']))  # [1, 2, 3, 4]

# %% [markdown]
# ### Assignment 15: Exception Handling in File Writing
# 
# Write a function that attempts to write a list of strings to a file. Use try, except, and finally blocks to handle IOError and ensure the file is properly closed.

# %%
def write_strings_to_file(strings, filename):
    try:
        file = open(filename, 'w')
        for string in strings:
            file.write(string + '\n')
    except IOError as e:
        print(f"Error: {e}")
    finally:
        try:
            file.close()
        except NameError:
            pass

write_strings_to_file(['Hello', 'World'], 'output.txt')


