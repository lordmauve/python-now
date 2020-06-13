# Variables and lists

We've seen a bit about how strings and numbers work by themselves, but to write
a program we have to deal with many strings and many numbers.

In this chapter we're going to look at two ways to keep track of strings,
numbers, and many more things.


## Variables

A variable is a name that we attach to an object. We write `a = ` something
in order to store the something in a variable called `a`.

```python
a = 1
```

```exercises
def test_b():
    """Can you assign the number 2 to a variable called `b`?"""
    assert b == 2

def test_c():
    """Can you assign the string "hi" to a variable called `greeting`?"""
    assert greeting == "hi"
```

Once a variable has been assigned, every time we type the variable name, it is
replaced by the value we stored.

```python
a = 7
b = 3

print(a * b + a + b)
```

A variable can be given a new value at any time:

```python
a = 7
a = "hi"
a = -1

print(a)
```

## Lists

Now we can name things, we can deal with more than one object at a time.

We use square brackets `[` and `]` to enclose several things to make them into
a **list**. A list contains other objects: strings, numbers - even other lists.

```python
hi = "hi"
items = [7, hi, -1]
print(items)
```

```exercises
def test_repeat_hi():
    """Change this program so that it prints a list that contains "hi"
    3 times."""
    assert output.strip() == "['hi', 'hi', 'hi']"


def test_repeat_hello():
    """Change the value of `hi` so that the program prints "hello" three
    times."""
    assert output.strip() == "['hello', 'hello', 'hello']"
```

Python provides a function `len(...)` which returns the length of the list, ie.
how many items are in it.

```repl
>>> len([1, 9, 9, 7])
```

To retrieve an item from a list, we write `variable[position]`, where `variable`
is a list and position is a number. The first item in a list is numbered `0`.

```repl
>>> my_list = [1, 9, 9, 7]
>>> my_list[0]
```

```exercises
def test_get_last():
    """Get the last item from the list."""
    assert result == 7

def test_add():
    """Add together the first and last items from the list."""
    assert result == 8
```
