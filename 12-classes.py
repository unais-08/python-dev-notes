# ==============================================================================
#                 Object-Oriented Programming (OOP) in Python
# ==============================================================================
# This document provides a comprehensive overview of OOP concepts in Python
# through practical, commented code examples.
#
# OOP is a programming paradigm based on the concept of "objects," which can
# contain data (attributes) and code (methods).

# ------------------------------------------------------------------------------
# 1. Classes and Objects
# ------------------------------------------------------------------------------
# A class is a blueprint for creating objects. An object is an instance of a class.


class Dog:
    """
    A simple class representing a dog.
    This is a docstring, used to describe the purpose of the class.
    """

    # Class attribute: a variable shared by all instances of the class.
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        """
        The constructor method, called when a new object is created.
        The 'self' parameter refers to the instance of the object itself.
        It is used to access attributes and methods of the object.
        """
        # Instance attributes: variables unique to each instance.
        self.name = name
        self.age = age
        print(f"{self.name} the dog has been born!")

    def bark(self):
        """A simple method to make the dog bark."""
        print(f"{self.name} says: Woof! Woof!")

    def get_info(self):
        """A method to return information about the dog."""
        return f"{self.name} is a {self.age}-year-old {self.species}."


# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

# Accessing instance attributes and calling methods
print(dog1.get_info())
dog2.bark()

# Accessing the class attribute
print(f"Dog1's species: {dog1.species}")
print(f"Dog2's species: {dog2.species}")
print(f"The class species: {Dog.species}")

# ------------------------------------------------------------------------------
# 2. The Four Pillars of OOP
# ------------------------------------------------------------------------------

# a) Encapsulation
# Encapsulation is the bundling of data (attributes) and methods that
# operate on that data into a single unit (the class). It also restricts
# direct access to some of the object's components.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        # Convention for "private" attribute: single leading underscore.
        # This is a strong suggestion to not access it directly.
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance is ${self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self._balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Using a property to control access to the balance.
    # The @property decorator turns a method into a read-only attribute.
    @property
    def balance(self):
        """Getter method for balance."""
        print("Accessing balance...")
        return self._balance


# Double leading underscore for name mangling
class ProtectedDog:
    def __init__(self, name):
        # Python "mangles" this name to _ProtectedDog__name,
        # making it harder to access directly from outside the class.
        self.__name = name

    def get_name(self):
        return self.__name


my_account = BankAccount("John Doe", 1000)
my_account.deposit(500)
my_account.withdraw(200)

# The user can still access _balance, but it's discouraged.
print(f"Current balance (direct access): {my_account._balance}")

# Using the property getter is the preferred way.
print(f"Current balance (via property): {my_account.balance}")

# Trying to set a private attribute directly won't work as intended with mangling
dog_protected = ProtectedDog("Max")
print(f"Dog's name: {dog_protected.get_name()}")
try:
    print(dog_protected.__name)
except AttributeError as e:
    print(f"Error trying to access __name directly: {e}")
    print("This is because Python name-mangles the attribute.")

# b) Inheritance
# Inheritance allows a class (child/derived class) to inherit attributes and
# methods from another class (parent/base class).


class Animal:
    """Base class for all animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """This method will be overridden by child classes."""
        raise NotImplementedError("Subclass must implement abstract method.")


class Cat(Animal):
    """Derived class for cats."""

    def __init__(self, name, breed):
        # Call the parent class's constructor using super()
        super().__init__(name)
        self.breed = breed

    def speak(self):
        """Override the speak method for a cat."""
        print(f"{self.name} the {self.breed} says: Meow!")


class Dog(Animal):
    """Derived class for dogs (revisiting the Dog class)."""

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        """Override the speak method for a dog."""
        print(f"{self.name} the dog says: Woof!")


my_cat = Cat("Whiskers", "Siamese")
my_dog = Dog("Fido", 7)

my_cat.speak()
my_dog.speak()

# c) Polymorphism
# Polymorphism means "many forms." In OOP, it allows objects of different
# classes to be treated as objects of a common base class.


def animal_sound(animal):
    """
    A function that can accept any object that has a 'speak' method.
    This demonstrates polymorphism.
    """
    animal.speak()


print("\nDemonstrating polymorphism:")
animal_sound(my_cat)
animal_sound(my_dog)

# d) Abstraction
# Abstraction is the concept of hiding complex implementation details and
# showing only the essential features of an object. This is often achieved
# using abstract base classes and methods.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    An abstract base class for a vehicle.
    Cannot be instantiated directly.
    """

    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def accelerate(self):
        """An abstract method that must be implemented by subclasses."""
        pass

    def get_brand(self):
        """A concrete method that can be used by subclasses."""
        return self.brand


class Car(Vehicle):
    """A concrete class implementing the Vehicle abstract class."""

    def accelerate(self):
        print(f"The {self.brand} car is accelerating.")


# This would raise a TypeError because Vehicle is an abstract class
# try:
#     my_vehicle = Vehicle("Generic")
# except TypeError as e:
#     print(f"\nError: {e}")

my_car = Car("Toyota")
my_car.accelerate()
print(f"The brand is: {my_car.get_brand()}")

# ------------------------------------------------------------------------------
# 3. Other Key Concepts
# ------------------------------------------------------------------------------

# a) Class vs. Instance Variables (Revisited)
# Class variables are shared, instance variables are unique.


class CarCounter:
    # Class variable
    number_of_cars = 0

    def __init__(self, model):
        self.model = model  # Instance variable
        CarCounter.number_of_cars += 1


car_a = CarCounter("Sedan")
car_b = CarCounter("SUV")

print(f"\nNumber of cars created: {CarCounter.number_of_cars}")

# b) Static Methods and Class Methods
#
# - Instance methods: Take `self` as the first argument, can access instance state.
# - Class methods: Take `cls` (the class itself) as the first argument, can modify class state.
#   Uses the `@classmethod` decorator.
# - Static methods: Don't take `self` or `cls`. They are simple functions grouped
#   within a class, but have no access to the class or instance state.
#   Uses the `@staticmethod` decorator.


class MathUtils:
    @staticmethod
    def add(x, y):
        """A static method to add two numbers."""
        return x + y

    @classmethod
    def get_class_name(cls):
        """A class method to return the name of the class."""
        return cls.__name__


print(f"\nStatic method result: {MathUtils.add(10, 20)}")
print(f"Class method result: {MathUtils.get_class_name()}")

# c) Magic Methods (Dunder Methods)
#
# These are special methods with double underscores (e.g., __init__) that
# allow us to use built-in functions and operators with our custom objects.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Called by str() and print(). Provides a user-friendly string."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Called by repr(). Provides an unambiguous, developer-friendly string."""
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """Called by the == operator. Defines equality."""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"\nString representation (str()): {p1}")
print(f"Object representation (repr()): {repr(p1)}")
print(f"Are p1 and p2 equal? {p1 == p2}")
print(f"Are p1 and p3 equal? {p1 == p3}")
