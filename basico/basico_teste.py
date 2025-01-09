# %% [markdown]
# # Lesson 1.2: Python Basics
# ## Topics Covered:
# - Syntax and Semantics
# - Variables and Data Types
# - Basic Operators (Arithmetic, Comparison, Logical)
# 

# %% [markdown]
# ## 1. Syntax and Semantics
# 
# **Question 1:** Write a Python program to print "Hello, World!".

# %%
print("Hello, World!")

# %% [markdown]
# **Question 2:** Write a Python program that takes a user input and prints it.

# %%
user_input = input()
print(user_input)

# %% [markdown]
# **Question 3:** Write a Python program to check if a number is positive, negative, or zero.

# %%
number = float(input())
if number > 0:
    print("positive.")
elif number < 0:
    print("negative.")
else:
    print("zero.")

# %% [markdown]
# **Question 4:** Write a Python program to find the largest of three numbers.

# %%
num1 = float(input())
num2 = float(input())
num3 = float(input())

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")

# %% [markdown]
# **Question 5:** Write a Python program to calculate the factorial of a number.

# %%
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input())
print(factorial(num))

# %% [markdown]
# ## 2. Variables and Data Types
# 
# **Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.

# %%
integer_var = 10
float_var = 10.5
string_var = "Hello"
boolean_var = True

print(f"Integer value: {integer_var}, type: {type(integer_var)}")
print(f"Float value: {float_var}, type: {type(float_var)}")
print(f"String value: {string_var}, type: {type(string_var)}")
print(f"Boolean value: {boolean_var}, type: {type(boolean_var)}")

# %% [markdown]
# **Question 7:** Write a Python program to swap the values of two variables.

# %%
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")

a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# %% [markdown]
# **Question 8:** Write a Python program to convert Celsius to Fahrenheit.

# %%
celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# %% [markdown]
# **Question 9:** Write a Python program to concatenate two strings.

# %%
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)

# %% [markdown]
# **Question 10:** Write a Python program to check if a variable is of a specific data type.

# %%
var = 10.5
if isinstance(var, float):
    print(f"{var} is a float")
else:
    print(f"{var} is not a float")

# %% [markdown]
# ## 3. Basic Operators (Arithmetic, Comparison, Logical)
# 
# **Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.

# %%
a = 5
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")

# %% [markdown]
# **Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.

# %%
a = 5
b = 3

print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")

# %% [markdown]
# **Question 13:** Write a Python program to demonstrate logical operators: and, or, not.

# %%
a = True
b = False

print(f"True and False: {a and b}")
print(f"True or False: {a or b}")
print(f"not True: {not a}")

# %% [markdown]
# **Question 14:** Write a Python program to calculate the square of a number.

# %%
num = float(input("Enter a number: "))
square = num ** 2
print(f"The square of {num} is {square}")

# %% [markdown]
# **Question 15:** Write a Python program to check if a number is even or odd.

# %%
num = int(input())
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# %% [markdown]
# **Question 16:** Write a Python program to find the sum of the first n natural numbers.

# %%
n = int(input())
sum_n = (n * (n + 1)) // 2
print(f"The sum of the first {n} natural numbers is {sum_n}")

# %% [markdown]
# **Question 17:** Write a Python program to check if a year is a leap year.

# %%
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# %% [markdown]
# **Question 18:** Write a Python program to reverse a string.

# %%
string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"The reversed string is: {reversed_string}")

# %% [markdown]
# **Question 19:** Write a Python program to check if a string is a palindrome.

# %%
string = input()
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

# %% [markdown]
# **Question 20:** Write a Python program to sort a list of numbers in ascending order.

# %%
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print(f"Sorted list: {numbers}")


