# %% [markdown]
# # Module 3: Data Structures Assignments
# ## Lesson 3.2: Tuples
# ### Assignment 1: Creating and Accessing Tuples
# 
# Create a tuple with the first 10 positive integers. Print the tuple.

# %%
tpl = tuple(range(1, 11))
print(tpl)

# %% [markdown]
# ### Assignment 2: Accessing Tuple Elements
# 
# Print the first, middle, and last elements of the tuple created in Assignment 1.

# %%
print(f"First element: {tpl[0]}")
print(f"Middle element: {tpl[len(tpl) // 2]}")
print(f"Last element: {tpl[-1]}")

# %% [markdown]
# ### Assignment 3: Tuple Slicing
# 
# Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.

# %%
print(f"First three elements: {tpl[:3]}")
print(f"Last three elements: {tpl[-3:]}")
print(f"Elements from index 2 to 5: {tpl[2:6]}")

# %% [markdown]
# ### Assignment 4: Nested Tuples
# 
# Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.

# %%
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Matrix:")
for row in matrix:
    print(row)
print(f"Element at second row and third column: {matrix[1][2]}")

# %% [markdown]
# ### Assignment 5: Tuple Concatenation
# 
# Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.

# %%
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
concatenated = tpl1 + tpl2
print(concatenated)

# %% [markdown]
# ### Assignment 6: Tuple Methods
# 
# Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.

# %%
tpl = (1, 2, 2, 3, 4, 4, 4, 5)
print(f"Occurrences of 4: {tpl.count(4)}")
print(f"Index of first occurrence of 2: {tpl.index(2)}")

# %% [markdown]
# ### Assignment 7: Unpacking Tuples
# 
# Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.

# %%
tpl = (1, 2, 3, 4, 5)
a, b, c, d, e = tpl
print(a, b, c, d, e)

# %% [markdown]
# ### Assignment 8: Tuple Conversion
# 
# Convert a list of the first 5 positive integers to a tuple. Print the tuple.

# %%
lst = [1, 2, 3, 4, 5]
tpl = tuple(lst)
print(tpl)

# %% [markdown]
# ### Assignment 9: Tuple of Tuples
# 
# Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.

# %%
tpl_of_tpls = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(tpl_of_tpls)

# %% [markdown]
# ### Assignment 10: Tuple and List
# 
# Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.

# %%
tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
lst.append(6)
tpl = tuple(lst)
print(tpl)

# %% [markdown]
# ### Assignment 11: Tuple and String
# 
# Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.

# %%
string = "hello"
tpl = tuple(string)
joined_string = ''.join(tpl)
print(joined_string)

# %% [markdown]
# ### Assignment 12: Tuple and Dictionary
# 
# Create a dictionary with tuple keys and integer values. Print the dictionary.

# %%
tpl_dict = {
    (1, 2): 3,
    (4, 5): 6,
    (7, 8): 9
}
print(tpl_dict)

# %% [markdown]
# ### Assignment 13: Nested Tuple Iteration
# 
# Create a nested tuple and iterate over the elements, printing each element.

# %%
nested_tpl = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
for tpl in nested_tpl:
    for elem in tpl:
        print(elem)

# %% [markdown]
# ### Assignment 14: Tuple and Set
# 
# Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.

# %%
tpl = (1, 2, 2, 3, 4, 4, 4, 5)
unique_set = set(tpl)
print(unique_set)

# %% [markdown]
# ### Assignment 15: Tuple Functions
# 
# Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.

# %%
def min_in_tuple(tpl):
    return min(tpl)

def max_in_tuple(tpl):
    return max(tpl)

def sum_of_tuple(tpl):
    return sum(tpl)

sample_tpl = (1, 2, 3, 4, 5)
print(f"Minimum: {min_in_tuple(sample_tpl)}")
print(f"Maximum: {max_in_tuple(sample_tpl)}")
print(f"Sum: {sum_of_tuple(sample_tpl)}")


