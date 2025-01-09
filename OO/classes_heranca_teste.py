# %% [markdown]
# # Module: Inheritance Assignments
# ## Lesson: Single and Multiple Inheritance
# ### Assignment 1: Single Inheritance Basic
# 
# Create a base class named `Animal` with attributes `name` and `species`. Create a derived class named `Dog` that inherits from `Animal` and adds an attribute `breed`. Create an object of the `Dog` class and print its attributes.

# %%
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

dog = Dog('Buddy', 'Canine', 'Golden Retriever')
print(dog.name, dog.species, dog.breed)

# %% [markdown]
# ### Assignment 2: Method Overriding in Single Inheritance
# 
# In the `Dog` class, override the `__str__` method to return a string representation of the object. Create an object of the class and print it.

# %%
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def __str__(self):
        return f"Dog(Name: {self.name}, Species: {self.species}, Breed: {self.breed})"

dog = Dog('Buddy', 'Canine', 'Golden Retriever')
print(dog)

# %% [markdown]
# ### Assignment 3: Single Inheritance with Additional Methods
# 
# In the `Dog` class, add a method named `bark` that prints a barking sound. Create an object of the class and call the method.

# %%
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

dog = Dog('Buddy', 'Canine', 'Golden Retriever')
dog.bark()

# %% [markdown]
# ### Assignment 4: Multiple Inheritance Basic
# 
# Create a base class named `Walker` with a method `walk` that prints a walking message. Create another base class named `Runner` with a method `run` that prints a running message. Create a derived class named `Athlete` that inherits from both `Walker` and `Runner`. Create an object of the `Athlete` class and call both methods.

# %%
class Walker:
    def walk(self):
        print("Walking...")

class Runner:
    def run(self):
        print("Running...")

class Athlete(Walker, Runner):
    pass

athlete = Athlete()
athlete.walk()
athlete.run()

# %% [markdown]
# ### Assignment 5: Method Resolution Order (MRO) in Multiple Inheritance
# 
# In the `Athlete` class, override the `walk` method to print a different message. Create an object of the class and call the `walk` method. Use the `super()` function to call the `walk` method of the `Walker` class.

# %%
class Athlete(Walker, Runner):
    def walk(self):
        print("Athlete walking...")
        super().walk()

athlete = Athlete()
athlete.walk()

# %% [markdown]
# ### Assignment 6: Multiple Inheritance with Additional Attributes
# 
# In the `Athlete` class, add an attribute `training_hours` and a method `train` that prints the training hours. Create an object of the class and call the method.

# %%
class Athlete(Walker, Runner):
    def __init__(self, training_hours):
        self.training_hours = training_hours

    def train(self):
        print(f"Training for {self.training_hours} hours.")

athlete = Athlete(5)
athlete.train()

# %% [markdown]
# ### Assignment 7: Diamond Problem in Multiple Inheritance
# 
# Create a class named `A` with a method `show` that prints a message. Create two derived classes `B` and `C` that inherit from `A` and override the `show` method. Create a class `D` that inherits from both `B` and `C`. Create an object of the `D` class and call the `show` method. Observe the method resolution order.

# %%
class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass

d = D()
d.show()  # B's show method

# %% [markdown]
# ### Assignment 8: Using `super()` in Single Inheritance
# 
# Create a base class named `Shape` with an attribute `color`. Create a derived class named `Circle` that inherits from `Shape` and adds an attribute `radius`. Use the `super()` function to initialize the attributes. Create an object of the `Circle` class and print its attributes.

# %%
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

circle = Circle('Red', 5)
print(circle.color, circle.radius)

# %% [markdown]
# ### Assignment 9: Using `super()` in Multiple Inheritance
# 
# Create a class named `Person` with an attribute `name`. Create a class named `Employee` with an attribute `employee_id`. Create a derived class `Manager` that inherits from both `Person` and `Employee`. Use the `super()` function to initialize the attributes. Create an object of the `Manager` class and print its attributes.

# %%
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

class Manager(Person, Employee):
    def __init__(self, name, employee_id):
        super().__init__(name)
        Employee.__init__(self, employee_id)

manager = Manager('John', 'M123')
print(manager.name, manager.employee_id)

# %% [markdown]
# ### Assignment 10: Method Overriding and `super()`
# 
# Create a class named `Vehicle` with a method `start` that prints a starting message. Create a derived class `Car` that overrides the `start` method to print a different message. Use the `super()` function to call the `start` method of the `Vehicle` class. Create an object of the `Car` class and call the `start` method.

# %%
class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        print("Car starting...")
        super().start()

car = Car()
car.start()

# %% [markdown]
# ### Assignment 11: Multiple Inheritance with Different Methods
# 
# Create a class named `Flyer` with a method `fly` that prints a flying message. Create a class named `Swimmer` with a method `swim` that prints a swimming message. Create a derived class `Superhero` that inherits from both `Flyer` and `Swimmer`. Create an object of the `Superhero` class and call both methods.

# %%
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Superhero(Flyer, Swimmer):
    pass

superhero = Superhero()
superhero.fly()
superhero.swim()

# %% [markdown]
# ### Assignment 12: Complex Multiple Inheritance
# 
# Create a class named `Base1` with an attribute `a`. Create a class named `Base2` with an attribute `b`. Create a class named `Derived` that inherits from both `Base1` and `Base2` and adds an attribute `c`. Initialize all attributes using the `super()` function. Create an object of the `Derived` class and print its attributes.

# %%
class Base1:
    def __init__(self, a):
        self.a = a

class Base2:
    def __init__(self, b):
        self.b = b

class Derived(Base1, Base2):
    def __init__(self, a, b, c):
        super().__init__(a)
        Base2.__init__(self, b)
        self.c = c

derived = Derived(1, 2, 3)
print(derived.a, derived.b, derived.c)

# %% [markdown]
# ### Assignment 13: Checking Instance Types with Inheritance
# 
# Create a base class named `Animal` and a derived class named `Cat`. Create objects of both classes and use the `isinstance` function to check the instance types.

# %%
class Animal:
    pass

class Cat(Animal):
    pass

animal = Animal()
cat = Cat()
print(isinstance(animal, Animal))  # True
print(isinstance(cat, Animal))  # True
print(isinstance(cat, Cat))  # True
print(isinstance(animal, Cat))  # False

# %% [markdown]
# ### Assignment 14: Polymorphism with Inheritance
# 
# Create a base class named `Bird` with a method `speak`. Create two derived classes `Parrot` and `Penguin` that override the `speak` method. Create a list of `Bird` objects and call the `speak` method on each object to demonstrate polymorphism.

# %%
class Bird:
    def speak(self):
        pass

class Parrot(Bird):
    def speak(self):
        print("Parrot says: Squawk!")

class Penguin(Bird):
    def speak(self):
        print("Penguin says: Honk!")

birds = [Parrot(), Penguin()]
for bird in birds:
    bird.speak()

# %% [markdown]
# ### Assignment 15: Combining Single and Multiple Inheritance
# 
# Create a base class named `Device` with an attribute `brand`. Create a derived class `Phone` that inherits from `Device` and adds an attribute `model`. Create another base class `Camera` with an attribute `resolution`. Create a derived class `Smartphone` that inherits from both `Phone` and `Camera`. Create an object of the `Smartphone` class and print its attributes.

# %%
class Device:
    def __init__(self, brand):
        self.brand = brand

class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, resolution):
        Phone.__init__(self, brand, model)
        Camera.__init__(self, resolution)

smartphone = Smartphone('Apple', 'iPhone 12', '12 MP')
print(smartphone.brand, smartphone.model, smartphone.resolution)


