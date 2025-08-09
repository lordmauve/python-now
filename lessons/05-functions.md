# Functions

As programs grow larger and more complex, it becomes important to organize code into manageable, reusable pieces. **Functions** are a fundamental way to do this in Python. A function is a named block of code that performs a specific task. You can **call** a function whenever you need to perform that task.

## Defining a Function

You define a function using the `def` keyword, followed by the function's name, parentheses `()`, and a colon `:`. The code block within the function is indented.

```python
def greet():
    print("Hello from a function!")
```

## Calling a Function

Once a function is defined, you can call it by using its name followed by parentheses.

```python
def greet():
    print("Hello from a function!")

# Call the function
greet()
greet() # You can call it multiple times
```

## Arguments

Functions can accept inputs, called **arguments** (or parameters). You define arguments by placing them inside the parentheses in the function definition.

```python
def greet_user(name): # 'name' is an argument
    print("Hello,", name + "!")

greet_user("Alice")
greet_user("Bob")
```

You can define functions with multiple arguments:

```python
def add_numbers(x, y):
    sum_result = x + y
    print(x, "+", y, "=", sum_result)

add_numbers(5, 3)
add_numbers(100, -20)
```

### Combining Functions

Functions can also call other functions. This is a powerful way to build up complex operations from simpler, reusable parts.

```python
def calculate_double(number):
    return number * 2

def calculate_square(number):
    return number * number

def print_doubled_and_squared(value):
    doubled = calculate_double(value)
    squared = calculate_square(value)
    print(f"Original: {value}, Doubled: {doubled}, Squared: {squared}")

print_doubled_and_squared(4)
print_doubled_and_squared(5)
```

## Return Values

Functions can also produce a result, called a **return value**. You use the `return` statement to send a value back from the function.

```python
def multiply(x, y):
    return x * y # The function sends this value back

result = multiply(6, 7)
print("6 * 7 is", result)

product = multiply(result, 0.5)
print("Half of that is", product)
```

If a function doesn't have a `return` statement, or has a `return` statement without a value, it implicitly returns `None` (a special Python value representing the absence of a value).

```python
def print_greeting(name):
    print("Hello,", name)

output = print_greeting("Test")
print("The function returned:", output)
```

## Docstrings

It's good practice to include a documentation string (docstring) as the first statement in a function's definition. A docstring is a string literal enclosed in triple quotes (`"""Docstring goes here"""`) that explains what the function does.

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

area = calculate_area(10, 5)
print("Area:", area)

# You can access the docstring using help() or the __doc__ attribute
help(calculate_area)
print(calculate_area.__doc__)
```

```python
# Define your functions here for the exercises.

# Example for test_simple_function:
# def say_hello():
#     print("Hello!")
# say_hello()

# Example for test_function_with_argument:
# def greet(name):
#     print(f"Hello, {name}!")
# greet("Dev")

# Example for test_function_with_return:
# def square(number):
#     return number * number
# result = square(5)
# print(result)

# Example for a new exercise (calling another function):
# def get_greeting(name):
#    return "Hello, " + name + "!"

# def print_loud_greeting(name):
#    message = get_greeting(name)
#    print(message.upper())
# print_loud_greeting("Explorer")

```
```exercises
def test_simple_function():
    """Define a function called `say_hello` that prints 'Hello!' when called."""
    # Your code here. Try editing the `say_hello()` example in the editor above.
    assert output.strip() == "Hello!"

def test_function_with_argument():
    """Define a function `greet(name)` that takes one argument `name` and prints 'Hello, [name]!'
    For example, if name is "World", it should print "Hello, World!"."""
    # Your code here. Try editing the `greet(name)` example.
    assert output.strip() == "Hello, Dev!" # Assuming the example call is greet("Dev")

def test_function_with_return():
    """Define a function `square(number)` that returns the square of the number.
    Then, call it with the number 7 and print the result."""
    # Your code here. Try editing the `square(number)` example.
    assert output.strip() == "49" # Expecting square(7) to be printed

def test_function_calling_another():
    """
    1. Define a function `get_personal_greeting(name)` that returns a string "Hi there, [name]".
    2. Define a function `print_personal_greeting(name)` that calls `get_personal_greeting`
       and then prints the returned greeting.
    Call `print_personal_greeting` with your name (or "Pythonista").
    """
    # Your code here. You can adapt the `get_greeting` and `print_loud_greeting` examples.
    # Make sure the final output is just the greeting string, e.g., "Hi there, Pythonista"
    assert "Hi there, " in output.strip() and len(output.strip().splitlines()) == 1
```

Functions are a cornerstone of writing clean, modular, and reusable Python code. By breaking down your program into functions, you make it easier to understand, test, and maintain.

In <a href="#06-classes">Lesson 6</a>, we'll take another step in organizing our code by learning about classes and object-oriented programming.
