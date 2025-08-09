# Conditional Logic and While Loops

In programming, we often need to make decisions and execute different code based on certain conditions, or repeat a block of code as long as a condition is true. This lesson explores `if`, `elif`, `else` statements for conditional logic and `while` loops for condition-based repetition.

## `if` Statements

An `if` statement allows Python to execute a block of code only if a certain condition is true.

```python
age = 20
if age >= 18:
    print("You are an adult.")
```

If the condition (`age >= 18`) is false, the indented block is skipped.

### `else`

You can use an `else` statement to provide a block of code that executes if the `if` condition is false.

```python
temperature = 15
if temperature > 25:
    print("It's a hot day!")
else:
    print("It's not a hot day.")
```

### `elif` (Else If)

For multiple conditions, you can use `elif` (short for "else if"). Python will check each `if` and `elif` condition in order, and execute the block for the first one that is true. If none are true, the `else` block (if present) is executed.

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")
```

```python
# Code for 'if' statement exercises

# Example for test_check_number_positive:
# number = 5
# if number > 0:
#     print("Positive")

# Example for test_check_number_even_odd:
# number = 4
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Example for test_check_age_group:
# age = 12
# if age < 13:
#     print("Child")
# elif age < 18:
#     print("Teenager")
# else:
#     print("Adult")
```
```exercises
def test_check_number_positive():
    """Given `number = 5`. Write an if statement to print 'Positive' if the number is greater than 0."""
    number = 5
    # Your code here
    # if number > 0:
    #     print("Positive")
    assert output.strip() == "Positive"

def test_check_number_even_odd():
    """Given `number = 4`. Write an if-else statement to print 'Even' if the number is even, and 'Odd' otherwise.
    Hint: Use the modulo operator `%`."""
    number = 4
    # Your code here
    # if number % 2 == 0:
    #     print("Even")
    # else:
    #     print("Odd")
    assert output.strip() == "Even"

def test_check_age_group():
    """Given `age = 12`.
    Write if-elif-else statements to print:
    - 'Child' if age < 13
    - 'Teenager' if age >= 13 and age < 18
    - 'Adult' if age >= 18
    """
    age = 12
    # Your code here
    # if age < 13:
    #     print("Child")
    # elif age < 18:
    #     print("Teenager")
    # else:
    #     print("Adult")
    assert output.strip() == "Child"
```

## `while` Loops

A `while` loop repeatedly executes a block of code as long as a given condition remains true. It's useful when you don't know beforehand how many times you need to loop.

```python
count = 0
while count < 5:
    print("Count is:", count)
    count = count + 1 # It's important to change the condition variable inside the loop

print("Loop finished.")
```

**Caution:** If the condition in a `while` loop never becomes false, the loop will run forever (an infinite loop). You'll usually need to interrupt your program (often Ctrl+C in a terminal) if this happens.

### Example: Simple Guessing Game

```python
secret_number = 7
guess = 0 # Initialize guess to something that is not the secret number

# Keep asking until the user guesses the secret number
# (This example would be interactive in a real Python environment)
# For this tutorial, we'll simulate a few guesses.

print("Guessing game simulation:")
guesses_made = [3, 5, 7]
current_guess_index = 0

while guess != secret_number and current_guess_index < len(guesses_made):
    guess = guesses_made[current_guess_index]
    print("User guesses:", guess)
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")
    current_guess_index += 1
```

### `break` and `continue` in Loops

Python provides two statements to control loop execution further:

*   `break`: Immediately exits the current loop (works for `for` and `while` loops).
*   `continue`: Skips the rest of the code inside the current iteration of the loop and proceeds to the next iteration.

```python
# Example with break
print("Example of break:")
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)
```

```python
# Example with continue
print("\nExample of continue:")
for i in range(5):
    if i == 2:
        continue  # Skip printing when i is 2
    print(i)
```

```python
# Code for 'while' loop, break/continue exercises

# Example for test_while_countdown:
# n = 3
# while n > 0:
#     print(n)
#     n -= 1
# print("Go!")

# Example for test_find_first_multiple_of_5:
# numbers = [2, 3, 7, 5, 8, 10]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 5 == 0:
#         print(numbers[i])
#         break
#     i += 1

# Example for test_skip_even_numbers:
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
```
```exercises
def test_while_countdown():
    """Use a while loop to print numbers from 3 down to 1. Then print 'Go!'.
    Output:
    3
    2
    1
    Go!
    """
    # Your code here
    # n = 3
    # while n > 0:
    #     print(n)
    #     n -= 1
    # print("Go!")
    assert output.strip() == "3\n2\n1\nGo!"

def test_find_first_multiple_of_5():
    """Given a list of numbers, find the first number that is a multiple of 5.
    Use a while loop and the `break` statement.
    Print the number once found.
    `numbers = [2, 3, 7, 5, 8, 10]`
    Output should be:
    5
    """
    numbers = [2, 3, 7, 5, 8, 10]
    # Your code here
    # i = 0
    # found_number = None
    # while i < len(numbers):
    #     if numbers[i] % 5 == 0:
    #         found_number = numbers[i]
    #         print(found_number)
    #         break
    #     i += 1
    assert output.strip() == "5"

def test_skip_even_numbers():
    """Print all odd numbers from 0 to 9 (inclusive). Use a for loop and `continue`.
    Output:
    1
    3
    5
    7
    9
    """
    # Your code here
    # for i in range(10):
    #     if i % 2 == 0:
    #         continue
    #     print(i)
    assert output.strip() == "1\n3\n5\n7\n9"
```

Understanding `if`, `elif`, `else`, and `while` loops allows you to control the flow of your Python programs, making them more dynamic and responsive to different situations.

Next up, in <a href="#05-functions">Lesson 5</a>, we'll learn how to organize our code into reusable blocks called functions.
