# %% [markdown]
# # Module: OOP Assignments
# ## Lesson: Polymorphism, Abstraction, and Encapsulation
# ### Assignment 1: Polymorphism with Methods
# 
# Create a base class named `Shape` with a method `area`. Create two derived classes `Circle` and `Square` that override the `area` method. Create a list of `Shape` objects and call the `area` method on each object to demonstrate polymorphism.

# %%
import math

class Shape:
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

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area())

# %% [markdown]
# ### Assignment 2: Polymorphism with Function Arguments
# 
# Create a function named `describe_shape` that takes a `Shape` object as an argument and calls its `area` method. Create objects of `Circle` and `Square` classes and pass them to the `describe_shape` function.

# %%
def describe_shape(shape):
    print(f"The area of the shape is: {shape.area()}")

circle = Circle(5)
square = Square(4)
describe_shape(circle)
describe_shape(square)

# %% [markdown]
# ### Assignment 3: Abstract Base Class with Abstract Methods
# 
# Create an abstract base class named `Vehicle` with an abstract method `start_engine`. Create derived classes `Car` and `Bike` that implement the `start_engine` method. Create objects of the derived classes and call the `start_engine` method.

# %%
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

car = Car()
bike = Bike()
car.start_engine()
bike.start_engine()

# %% [markdown]
# ### Assignment 4: Abstract Base Class with Concrete Methods
# 
# In the `Vehicle` class, add a concrete method `fuel_type` that returns a generic fuel type. Override this method in `Car` and `Bike` classes to return specific fuel types. Create objects of the derived classes and call the `fuel_type` method.

# %%
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def fuel_type(self):
        return "Generic Fuel"

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def fuel_type(self):
        return "Petrol"

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def fuel_type(self):
        return "Diesel"

car = Car()
bike = Bike()
print(car.fuel_type())
print(bike.fuel_type())

# %% [markdown]
# ### Assignment 5: Encapsulation with Private Attributes
# 
# Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Ensure that the balance cannot be accessed directly.

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
# ### Assignment 6: Encapsulation with Property Decorators
# 
# In the `BankAccount` class, use property decorators to get and set the `balance` attribute. Ensure that the balance cannot be set to a negative value.

# %%
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount

account = BankAccount('12345678', 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)  # 1300
account.balance = -500  # Balance cannot be negative!

# %% [markdown]
# ### Assignment 7: Combining Encapsulation and Inheritance
# 
# Create a base class named `Person` with private attributes `name` and `age`. Add methods to get and set these attributes. Create a derived class named `Student` that adds an attribute `student_id`. Create an object of the `Student` class and test the encapsulation.

# %%
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student = Student('John', 20, 'S123')
print(student.get_name(), student.get_age(), student.student_id)
student.set_name('Alice')
student.set_age(22)
print(student.get_name(), student.get_age(), student.student_id)

# %% [markdown]
# ### Assignment 8: Polymorphism with Inheritance
# 
# Create a base class named `Animal` with a method `speak`. Create two derived classes `Dog` and `Cat` that override the `speak` method. Create a list of `Animal` objects and call the `speak` method on each object to demonstrate polymorphism.

# %%
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

# %% [markdown]
# ### Assignment 9: Abstract Methods in Base Class
# 
# Create an abstract base class named `Employee` with an abstract method `calculate_salary`. Create two derived classes `FullTimeEmployee` and `PartTimeEmployee` that implement the `calculate_salary` method. Create objects of the derived classes and call the `calculate_salary` method.

# %%
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

full_time = FullTimeEmployee(5000)
part_time = PartTimeEmployee(20, 80)
print(full_time.calculate_salary())  # 5000
print(part_time.calculate_salary())  # 1600

# %% [markdown]
# ### Assignment 10: Encapsulation in Data Classes
# 
# Create a data class named `Product` with private attributes `product_id`, `name`, and `price`. Add methods to get and set these attributes. Ensure that the price cannot be set to a negative value.

# %%
class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative!")
        else:
            self.__price = price

product = Product('P001', 'Laptop', 1000)
print(product.get_product_id(), product.get_name(), product.get_price())
product.set_price(-500)  # Price cannot be negative!
product.set_price(1500)
print(product.get_product_id(), product.get_name(), product.get_price())

# %% [markdown]
# ### Assignment 11: Polymorphism with Operator Overloading
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
print(v3)  # Vector(6, 8)

# %% [markdown]
# ### Assignment 12: Abstract Properties
# 
# Create an abstract base class named `Appliance` with an abstract property `power`. Create two derived classes `WashingMachine` and `Refrigerator` that implement the `power` property. Create objects of the derived classes and access the `power` property.

# %%
class Appliance(ABC):
    @property
    @abstractmethod
    def power(self):
        pass

class WashingMachine(Appliance):
    @property
    def power(self):
        return "500W"

class Refrigerator(Appliance):
    @property
    def power(self):
        return "300W"

wm = WashingMachine()
fridge = Refrigerator()
print(wm.power)  # 500W
print(fridge.power)  # 300W

# %% [markdown]
# ### Assignment 13: Encapsulation in Class Hierarchies
# 
# Create a base class named `Account` with private attributes `account_number` and `balance`. Add methods to get and set these attributes. Create a derived class named `SavingsAccount` that adds an attribute `interest_rate`. Create an object of the `SavingsAccount` class and test the encapsulation.

# %%
class Account:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

savings = SavingsAccount('12345678', 1000, 0.05)
print(savings.get_account_number(), savings.get_balance(), savings.interest_rate)
savings.set_balance(1500)
print(savings.get_account_number(), savings.get_balance(), savings.interest_rate)

# %% [markdown]
# ### Assignment 14: Polymorphism with Multiple Inheritance
# 
# Create a class named `Flyer` with a method `fly`. Create a class named `Swimmer` with a method `swim`. Create a class named `Superhero` that inherits from both `Flyer` and `Swimmer` and overrides both methods. Create an object of the `Superhero` class and call both methods.

# %%
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Superhero(Flyer, Swimmer):
    def fly(self):
        print("Superhero flying...")

    def swim(self):
        print("Superhero swimming...")

superhero = Superhero()
superhero.fly()
superhero.swim()

# %% [markdown]
# ### Assignment 15: Abstract Methods and Multiple Inheritance
# 
# Create an abstract base class named `Worker` with an abstract method `work`. Create two derived classes `Engineer` and `Doctor` that implement the `work` method. Create another derived class `Scientist` that inherits from both `Engineer` and `Doctor`. Create an object of the `Scientist` class and call the `work` method.

# %%
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Engineer(Worker):
    def work(self):
        print("Engineer working...")

class Doctor(Worker):
    def work(self):
        print("Doctor working...")

class Scientist(Engineer, Doctor):
    def work(self):
        Engineer.work(self)
        Doctor.work(self)

scientist = Scientist()
scientist.work()


