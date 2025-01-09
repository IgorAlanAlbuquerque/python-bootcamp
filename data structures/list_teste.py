# %% [markdown]
# # Module 3: Data Structures Assignments
# ## Lesson 3.1: Lists
# ### Assignment 1: Creating and Accessing Lists
# 
# Create a list of the first 20 positive integers. Print the list.

# %%
lst = list(range(1, 21))
print(lst)

# %% [markdown]
# ### Assignment 2: Accessing List Elements
# 
# Print the first, middle, and last elements of the list created in Assignment 1.

# %%
print(f"First element: {lst[0]}")
print(f"Middle element: {lst[len(lst) // 2]}")
print(f"Last element: {lst[-1]}")

# %% [markdown]
# ### Assignment 3: List Slicing
# 
# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.

# %%
print(f"First five elements: {lst[:5]}")
print(f"Last five elements: {lst[-5:]}")
print(f"Elements from index 5 to 15: {lst[5:16]}")

# %% [markdown]
# ### Assignment 4: List Comprehensions
# 
# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.

# %%
squares = [x**2 for x in range(1, 11)]
print(squares)

# %% [markdown]
# ### Assignment 5: Filtering Lists
# 
# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.

# %%
evens = [x for x in lst if x % 2 == 0]
print(evens)

# %% [markdown]
# ### Assignment 6: List Methods
# 
# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.

# %%
import random

random_numbers = [random.randint(1, 20) for _ in range(15)]
print(f"Original list: {random_numbers}")

sorted_numbers = sorted(random_numbers)
print(f"Sorted in ascending order: {sorted_numbers}")

sorted_numbers_desc = sorted(random_numbers, reverse=True)
print(f"Sorted in descending order: {sorted_numbers_desc}")

unique_numbers = list(set(random_numbers))
print(f"List with duplicates removed: {unique_numbers}")

# %% [markdown]
# ### Assignment 7: Nested Lists
# 
# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.

# %%
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)
print(f"Element at second row and third column: {matrix[1][2]}")

# %% [markdown]
# ### Assignment 8: List of Dictionaries
# 
# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.

# %%
students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 72},
    {'name': 'Charlie', 'score': 95},
    {'name': 'David', 'score': 65},
    {'name': 'Eve', 'score': 78}
]
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
print("Sorted students by score in descending order:")
for student in sorted_students:
    print(student)

# %% [markdown]
# ### Assignment 9: Matrix Transposition
# 
# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.

# %%
def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed:
    print(row)

# %% [markdown]
# ### Assignment 10: Flattening a Nested List
# 
# Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.

# %%
def flatten_list(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return flat_list

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = flatten_list(nested_list)
print("Original nested list:")
print(nested_list)
print("Flattened list:")
print(flattened)

# %% [markdown]
# ### Assignment 11: List Manipulation
# 
# Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.

# %%
lst = list(range(1, 11))
print(f"Original list: {lst}")
del lst[6]
del lst[4]
del lst[2]
lst.insert(5, 99)
print(f"Modified list: {lst}")

# %% [markdown]
# ### Assignment 12: List Zipping
# 
# Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.

# %%
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = list(zip(list1, list2))
print(zipped)

# %% [markdown]
# ### Assignment 13: List Reversal
# 
# Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.

# %%
def reverse_list(lst):
    return lst[::-1]

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_list}")

# %% [markdown]
# ### Assignment 14: List Rotation
# 
# Write a function that rotates a list by n positions. Print the original and rotated lists.

# %%
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

original_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(original_list, 2)
print(f"Original list: {original_list}")
print(f"Rotated list: {rotated_list}")

# %% [markdown]
# ### Assignment 15: List Intersection
# 
# Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.

# %%
def list_intersection(lst1, lst2):
    return [x for x in lst1 if x in lst2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list_intersection(list1, list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection}")


