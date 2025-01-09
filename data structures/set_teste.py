# %% [markdown]
# # Module 3: Data Structures Assignments
# ## Lesson 3.3: Sets
# ### Assignment 1: Creating and Accessing Sets
# 
# Create a set with the first 10 positive integers. Print the set.

# %%
s = set(range(1, 11))
print(s)

# %% [markdown]
# ### Assignment 2: Adding and Removing Elements
# 
# Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.

# %%
s.add(11)
s.remove(1)
print(s)

# %% [markdown]
# ### Assignment 3: Set Operations
# 
# Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.

# %%
set1 = set(range(1, 6))
set2 = set(range(2, 11, 2))
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")

# %% [markdown]
# ### Assignment 4: Set Comprehensions
# 
# Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.

# %%
squares = {x**2 for x in range(1, 11)}
print(squares)

# %% [markdown]
# ### Assignment 5: Filtering Sets
# 
# Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.

# %%
evens = {x for x in s if x % 2 == 0}
print(evens)

# %% [markdown]
# ### Assignment 6: Set Methods
# 
# Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.

# %%
s = {1, 2, 2, 3, 4, 4, 5}
unique_s = set(s)
print(unique_s)

# %% [markdown]
# ### Assignment 7: Subsets and Supersets
# 
# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.

# %%
set1 = set(range(1, 6))
set2 = set(range(1, 4))
print(f"Is set2 a subset of set1? {set2.issubset(set1)}")
print(f"Is set1 a superset of set2? {set1.issuperset(set2)}")

# %% [markdown]
# ### Assignment 8: Frozenset
# 
# Create a frozenset with the first 5 positive integers. Print the frozenset.

# %%
fs = frozenset(range(1, 6))
print(fs)

# %% [markdown]
# ### Assignment 9: Set and List Conversion
# 
# Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.

# %%
s = set(range(1, 6))
lst = list(s)
lst.append(6)
s = set(lst)
print(s)

# %% [markdown]
# ### Assignment 10: Set and Dictionary
# 
# Create a dictionary with set keys and integer values. Print the dictionary.

# %%
d = {
    frozenset({1, 2}): 3,
    frozenset({3, 4}): 7,
    frozenset({5, 6}): 11
}
print(d)

# %% [markdown]
# ### Assignment 11: Iterating Over Sets
# 
# Create a set and iterate over the elements, printing each element.

# %%
s = set(range(1, 6))
for elem in s:
    print(elem)

# %% [markdown]
# ### Assignment 12: Removing Elements from Sets
# 
# Create a set and remove elements from it until it is empty. Print the set after each removal.

# %%
s = set(range(1, 6))
while s:
    s.pop()
    print(s)

# %% [markdown]
# ### Assignment 13: Set Symmetric Difference Update
# 
# Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.

# %%
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)

# %% [markdown]
# ### Assignment 14: Set Membership Testing
# 
# Create a set and test if certain elements are present in the set. Print the results.

# %%
s = set(range(1, 6))
print(3 in s)
print(6 in s)

# %% [markdown]
# ### Assignment 15: Set of Tuples
# 
# Create a set containing tuples, where each tuple contains two elements. Print the set.

# %%
s = { (1, 2), (3, 4), (5, 6) }
print(s)


