# Introduction to Classes and Objects

Python is an object-oriented programming (OOP) language. This means it provides features that support organizing software design around data, or "objects", rather than functions and logic. **Classes** are the blueprints for creating these objects.

## What are Classes and Objects?

*   **Class**: A blueprint or template for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have.
*   **Object (Instance)**: A specific instance of a class. It has its own values for the attributes defined by the class.

Think of a class like a cookie cutter (`Dog` class) and objects as the cookies you make with it (specific dogs like `my_dog`, `another_dog`). Each cookie has the same shape (attributes and methods) but might have different decorations (attribute values).

## Defining a Class and Creating Objects

You define a class using the `class` keyword, followed by the class name (conventionally `CamelCase`) and a colon. Inside the class, you'll typically define methods (functions that belong to the class).

The first method we usually define is `__init__`. This special method is called a **constructor**, and it runs automatically when you create a new **object** (or **instance**) of the class. Its job is to set up the initial state of the object. The `self` parameter refers to the instance being created.

Let's create a simple `Dog` class:

```python
class Dog:
    def __init__(self, name_param, age_param):
        # These are instance attributes
        self.name = name_param
        self.age = age_param
        print(f"A new dog named {self.name}, {self.age} years old, has been created!")

    def bark(self):
        print(f"{self.name} says: Woof woof!")

# Creating objects (instances) of our Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing attributes of an object
print(f"{dog1.name} is a good dog.")
print(f"{dog2.name} is {dog2.age} years old.")

# Calling methods on an object
dog1.bark()
dog2.bark()
```
In this example, `name_param` and `age_param` are parameters passed to the constructor. `self.name` and `self.age` are **instance attributes**, which store data specific to each `Dog` object. `bark` is an **instance method** that performs an action related to a `Dog` object.

## More on `__init__` and Instance Attributes

As we saw, the `__init__` method is crucial for setting up an object's initial state. The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

When you assign a value to an attribute using `self.attribute_name = value` inside `__init__` (or any other instance method), you are creating an **instance attribute**. Each object of the class will have its own copy of these attributes with its own values.

Let's look at another example with a `Book` class:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Every time a Book object is made, this message will print.
        print(f"Book '{self.title}' by {self.author} added to library.")

book_a = Book("The Hobbit", "J.R.R. Tolkien")
book_b = Book("1984", "George Orwell")

print(f"We have '{book_a.title}' and '{book_b.title}'.")
```

## Instance Methods

Methods are functions defined inside a class that operate on instances of that class. Like `__init__`, their first parameter is always `self`, which gives them access to the instance's attributes and other methods.

Here's a `BankAccount` class with methods to deposit and withdraw funds:
```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        print(f"Account for {self.account_holder} created with balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount invalid or insufficient funds.")

my_account = BankAccount("John Doe", 100)
my_account.deposit(50)
my_account.withdraw(30)
my_account.withdraw(150) # Try to withdraw too much
```

```python
# Define your Car class and other classes here for the exercises.

class Car:
    def __init__(self, make, model, year=2020):
        self.make = make
        self.model = model
        self.year = year # Added year for another attribute example
        # print(f"Car created: {self.year} {self.make} {self.model}") # Optional print

    # Add methods for exercises below
    # def display_info(self):
    #     print(f"Car: {self.year} {self.make} {self.model}")

# Example usage for your testing (the exercises will run their own):
# car1 = Car("Toyota", "Camry", 2021)
# car1.display_info()

# car2 = Car("Honda", "Civic") # Uses default year
# car2.display_info()

```
```exercises
def test_create_car_class_attributes():
    """Inside the `Car` class provided in the editor:
    1. The `__init__` method should take `make`, `model`, and `year`.
    2. Store these as instance attributes: `self.make`, `self.model`, `self.year`.
    For testing in the editor, you might create a `Car("Ford", "Mustang", 1967)`
    and print its attributes; the test expects output: 1967, Ford, Mustang, each on a new line."""
    # To pass, your Car class __init__ must assign these attributes.
    # The print statements in your editable code block should output:
    # 1967
    # Ford
    # Mustang
    # (if you uncomment and run print(my_car.year) etc. for a car made with these values)
    assert 'Car' in source_code # Check if Car class is defined
    # The test will create its own instance and check attributes and output
    # For local check:
    # my_car = Car("Ford", "Mustang", 1967)
    # print(my_car.year)
    # print(my_car.make)
    # print(my_car.model)
    assert output.strip() == "1967\nFord\nMustang"


def test_car_method_display_info():
    """Add a method `display_info` to the `Car` class.
    This method should take no arguments (other than `self`).
    It should print a string in the format: "Car: [year] [make] [model]".
    For example, for a 2022 Audi A4, it should print "Car: 2022 Audi A4".
    Call this method on an instance (e.g., make='Tesla', model='Model 3', year=2023)."""
    # To pass, your Car class must have this method.
    # The test will call it on an instance it creates.
    # For local check:
    # my_tsla = Car('Tesla', 'Model 3', 2023)
    # my_tsla.display_info()
    assert "display_info" in source_code
    assert output.strip() == "Car: 2023 Tesla Model 3"

def test_person_class_greet():
    """
    Define a new class `Person`.
    1. Its `__init__` method should take `name` and `age`, storing them as attributes.
    2. It should have a method `greet()` that prints "Hello, my name is [name] and I am [age] years old."
    Create a Person object with name "Alice" and age 30, then call its `greet` method.
    """
    # Define the Person class in the editor above.
    # class Person:
    #    def __init__(self, name, age):
    #        self.name = name
    #        self.age = age
    #    def greet(self):
    #        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    # p = Person("Alice", 30)
    # p.greet()
    assert "Person" in source_code
    assert output.strip() == "Hello, my name is Alice and I am 30 years old."
```

Classes are a powerful tool for creating well-structured and reusable code. They are a core concept in many programming languages, and understanding them is key to mastering Python for larger projects.

This concludes our initial set of new lessons! You've learned about printing, loops, conditionals, functions, and now the basics of classes (`__init__`, attributes, and methods). Keep practicing to solidify these concepts.
