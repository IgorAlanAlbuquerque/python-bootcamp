# %% [markdown]
# # Module 2: Control Flow Assignments
# ## Lesson 2.1: Conditional Statements
# ### Assignment 1: Simple if Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive.

# %%
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")

# %% [markdown]
# ### Assignment 2: if-else Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive or negative.

# %%
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# %% [markdown]
# ### Assignment 3: if-elif-else Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero.

# %%
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# %% [markdown]
# ### Assignment 4: Nested if Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.

# %%
number = float(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")

# %% [markdown]
# ## Lesson 2.2: Loops
# ### Assignment 5: for Loop
# 
# Write a program that prints all the numbers from 1 to 10 using a for loop.

# %%
for i in range(1, 11):
    print(i)

# %% [markdown]
# ### Assignment 6: while Loop
# 
# Write a program that prints all the numbers from 1 to 10 using a while loop.

# %%
i = 1
while i <= 10:
    print(i)
    i += 1

# %% [markdown]
# ### Assignment 7: Nested Loops
# 
# Write a program that prints a 5x5 grid of asterisks (*) using nested loops.

# %%
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# %% [markdown]
# ### Assignment 8: break Statement
# 
# Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.

# %%
total = 0
while True:
    number = float(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number
print(f"The sum of all the numbers is {total}.")

# %% [markdown]
# ### Assignment 9: continue Statement
# 
# Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.

# %%
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# %% [markdown]
# ### Assignment 10: pass Statement
# 
# Write a program that defines an empty function using the pass statement.

# %%
def empty_function():
    pass

empty_function()

# %% [markdown]
# ### Assignment 11: Combining Loops and Conditionals
# 
# Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.

# %%
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)

# %% [markdown]
# ### Assignment 12: Factorial Calculation
# 
# Write a program that calculates the factorial of a number input by the user using a while loop.

# %%
number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is {factorial}.")

# %% [markdown]
# ### Assignment 13: Sum of Digits
# 
# Write a program that calculates the sum of the digits of a number input by the user using a while loop.

# %%
number = int(input("Enter a number: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10
print(f"The sum of the digits is {sum_of_digits}.")

# %% [markdown]
# ### Assignment 14: Prime Number Check
# 
# Write a program that checks if a number input by the user is a prime number using a for loop.

# %%
number = int(input("Enter a number: "))
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# %% [markdown]
# ### Assignment 15: Fibonacci Sequence
# 
# Write a program that prints the first n Fibonacci numbers, where n is input by the user.

# %%
n = int(input("Enter the number of Fibonacci numbers to print: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1


