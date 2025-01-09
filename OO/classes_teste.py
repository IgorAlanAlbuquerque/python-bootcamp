# %% [markdown]
# # Module: Classes and Objects Assignments
# ## Lesson: Creating and Working with Classes and Objects
# ### Assignment 1: Basic Class and Object Creation
# 
# Create a class named `Car` with attributes `make`, `model`, and `year`. Create an object of the class and print its attributes.

# %%
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car('Toyota', 'Camry', 2020)
print(car.make, car.model, car.year)

# %% [markdown]
# ### Assignment 2: Methods in Class
# 
# Add a method named `start_engine` to the `Car` class that prints a message when the engine starts. Create an object of the class and call the method.

# %%
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine has started.")

car = Car('Toyota', 'Camry', 2020)
car.start_engine()

# %% [markdown]
# ### Assignment 3: Class with Constructor
# 
# Create a class named `Student` with attributes `name` and `age`. Use a constructor to initialize these attributes. Create an object of the class and print its attributes.

# %%
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student('John', 20)
print(student.name, student.age)

# %% [markdown]
# ### Assignment 4: Class with Private Attributes
# 
# Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Create an object of the class and perform some operations.

# %%
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

account = BankAccount('12345678', 1000)
account.deposit(500)
account.withdraw(200)
print(account.check_balance())  # 1300
account.withdraw(2000)  # Insufficient balance!

# %% [markdown]
# ### Assignment 5: Class Inheritance
# 
# Create a base class named `Person` with attributes `name` and `age`. Create a derived class named `Employee` that inherits from `Person` and adds an attribute `employee_id`. Create an object of the derived class and print its attributes.

# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

employee = Employee('Alice', 30, 'E123')
print(employee.name, employee.age, employee.employee_id)

# %% [markdown]
# ### Assignment 6: Method Overriding
# 
# In the `Employee` class, override the `__str__` method to return a string representation of the object. Create an object of the class and print it.

# %%
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id})"

employee = Employee('Alice', 30, 'E123')
print(employee)

# %% [markdown]
# ### Assignment 7: Class Composition
# 
# Create a class named `Address` with attributes `street`, `city`, and `zipcode`. Create a class named `Person` that has an `Address` object as an attribute. Create an object of the `Person` class and print its address.

# %%
class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

address = Address('123 Main St', 'New York', '10001')
person = Person('John', 25, address)
print(person.address.street, person.address.city, person.address.zipcode)

# %% [markdown]
# ### Assignment 8: Class with Class Variables
# 
# Create a class named `Counter` with a class variable `count`. Each time an object is created, increment the count. Add a method to get the current count. Create multiple objects and print the count.

# %%
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.get_count())
print(c1.count)

# %% [markdown]
# ### Assignment 9: Static Methods
# 
# Create a class named `MathOperations` with a static method to calculate the square root of a number. Call the static method without creating an object.

# %%
import math

class MathOperations:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

print(MathOperations.sqrt(16))

# %% [markdown]
# ### Assignment 10: Class with Properties
# 
# Create a class named `Rectangle` with private attributes `length` and `width`. Use properties to get and set these attributes. Create an object of the class and test the properties.

# %%
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

rect = Rectangle(10, 5)
print(rect.length, rect.width)  # 10 5
rect.length = 15
rect.width = 7
print(rect.length, rect.width)  # 15 7

# %% [markdown]
# ### Assignment 11: Abstract Base Class
# 
# Create an abstract base class named `Shape` with an abstract method `area`. Create derived classes `Circle` and `Square` that implement the `area` method. Create objects of the derived classes and call the `area` method.

# %%
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

circle = Circle(5)
square = Square(4)
print(circle.area())  # 78.53981633974483
print(square.area())  # 16

# %% [markdown]
# ### Assignment 12: Operator Overloading
# 
# Create a class named `Vector` with attributes `x` and `y`. Overload the `+` operator to add two `Vector` objects. Create objects of the class and test the operator overloading.

# %%
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)

# %% [markdown]
# ### Assignment 13: Class with Custom Exception
# 
# Create a custom exception named `InsufficientBalanceError`. In the `BankAccount` class, raise this exception when a withdrawal amount is greater than the balance. Handle the exception and print an appropriate message.

# %%
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance!")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

account = BankAccount('12345678', 1000)
account.deposit(500)
try:
    account.withdraw(2000)
except InsufficientBalanceError as e:
    print(f"Error: {e}")

# %% [markdown]
# ### Assignment 14: Class with Context Manager
# 
# Create a class named `FileManager` that implements the context manager protocol to open and close a file. Use this class to read the contents of a file.

# %%
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# %% [markdown]
# ### Assignment 15: Chaining Methods
# 
# Create a class named `Calculator` with methods to add, subtract, multiply, and divide. Each method should return the object itself to allow method chaining. Create an object and chain multiple method calls.

# %%
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self

    def subtract(self, amount):
        self.value -= amount
        return self

    def multiply(self, amount):
        self.value *= amount
        return self

    def divide(self, amount):
        if amount != 0:
            self.value /= amount
        else:
            print("Cannot divide by zero!")
        return self

calc = Calculator()
calc.add(10).subtract(3).multiply(2).divide(2)
print(calc.value)


