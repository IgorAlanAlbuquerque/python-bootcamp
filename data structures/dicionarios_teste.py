# %% [markdown]
# # Module 3: Data Structures Assignments
# ## Lesson 3.4: Dictionaries
# ### Assignment 1: Creating and Accessing Dictionaries
# 
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.

# %%
d = {i: i**2 for i in range(1, 11)}
print(d)

# %% [markdown]
# ### Assignment 2: Accessing Dictionary Elements
# 
# Print the value of the key 5 and the keys of the dictionary created in Assignment 1.

# %%
print(f"Value of key 5: {d[5]}")
print(f"Keys: {list(d.keys())}")

# %% [markdown]
# ### Assignment 3: Dictionary Methods
# 
# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.

# %%
d[11] = 121
d.pop(1)
print(d)

# %% [markdown]
# ### Assignment 4: Iterating Over Dictionaries
# 
# Iterate over the dictionary created in Assignment 1 and print each key-value pair.

# %%
for key, value in d.items():
    print(f"{key}: {value}")

# %% [markdown]
# ### Assignment 5: Dictionary Comprehensions
# 
# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.

# %%
cubes = {i: i**3 for i in range(1, 11)}
print(cubes)

# %% [markdown]
# ### Assignment 6: Merging Dictionaries
# 
# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

# %%
d1 = {i: i**2 for i in range(1, 6)}
d2 = {i: i**2 for i in range(6, 11)}
d1.update(d2)
print(d1)

# %% [markdown]
# ### Assignment 7: Nested Dictionaries
# 
# Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.

# %%
student = {
    'name': 'John Doe',
    'age': 16,
    'grades': {
        'math': 90,
        'science': 85,
        'english': 88
    }
}
print(student)

# %% [markdown]
# ### Assignment 8: Dictionary of Lists
# 
# Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.

# %%
multiples = {i: [i * j for j in range(1, 6)] for i in range(1, 6)}
print(multiples)

# %% [markdown]
# ### Assignment 9: Dictionary of Tuples
# 
# Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.

# %%
tuple_dict = {i: (i, i**2) for i in range(1, 6)}
print(tuple_dict)

# %% [markdown]
# ### Assignment 10: Dictionary and List Conversion
# 
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.

# %%
d = {i: i**2 for i in range(1, 6)}
list_of_tuples = list(d.items())
print(list_of_tuples)

# %% [markdown]
# ### Assignment 11: Dictionary Filtering
# 
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

# %%
d = {i: i**2 for i in range(1, 11)}
even_dict = {k: v for k, v in d.items() if k % 2 == 0}
print(even_dict)

# %% [markdown]
# ### Assignment 12: Dictionary Key and Value Transformation
# 
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.

# %%
d = {i: i**2 for i in range(1, 6)}
swapped_dict = {v: k for k, v in d.items()}
print(swapped_dict)

# %% [markdown]
# ### Assignment 13: Default Dictionary
# 
# Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.

# %%
from collections import defaultdict

default_dict = defaultdict(list)
default_dict['a'].append(1)
default_dict['a'].append(2)
default_dict['b'].append(3)
print(default_dict)

# %% [markdown]
# ### Assignment 14: Counting with Dictionaries
# 
# Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.

# %%
def count_chars(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

string = "hello world"
print(count_chars(string))

# %% [markdown]
# ### Assignment 15: Dictionary and JSON
# 
# Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.

# %%
import json

book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year': 1960,
    'genre': 'Fiction'
}
book_json = json.dumps(book)
print(book_json)


