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
