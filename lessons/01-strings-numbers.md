# Strings

In programming, a **string** is a piece of text. Python calls strings by the
abbreviation `str` and lets you type them out by enclosing them in single-quote
chararacters `'` or double-quote characters `"`.

Try changing this example so that it reads "hello world!".

```repl
>>> 'hello!'
```

```exercises
def test_helloworld():
    """Input the string 'hello world!'"""
    assert result == 'hello world!'
```

And make this one into Hello... and then your own name.

```repl
>>> "Hello"
```

Note how when Python is displaying a string back to you as a programmer, it
keeps the quotes around it. This is a hint to you that you are dealing with a
string.

But the quotes are not *part of* the string. We can use the `print()` function
to see what the string actually contains:

```repl
>>> print("hello python")
```

A **function** is a list of operations. `print` is the name of the function and
the parentheses `(` and `)` denote that we're asking Python to run those
operations. Between the `()` are any **arguments** that we're asking the
function to work on.

Often we will write the functions ourselves, but Python knows about `print()`
already.

`print()` is a funny function; it can accept more than one argument (the commas
`,` separate the arguments)

```repl
>>> print("joined", "up", "string")
```


## Adding strings

Now we've typed strings into Python and we've got them back out, which isn't
very useful. What's more important is that we can ask Python to perform
**operations** on them to **manipulate** them.

We can **concatenate** two strings by using a `+` sign.

```repl
>>> "joi" + "ned"
```

```exercise
def test_joined_up():
    """
    You can also add three strings. Can you make this say `'joined up'` by
    adding an extra string? You need one of the strings to include a space
    inside the quotes, or else it will say `'joinedup'`.
    """
    assert source.count('+') == 2
    assert result == 'joined up'
```


## Calling methods

We saw the `print()` function which displays the contents of a string.
A close cousin of a function is a **method**. Methods are just the same as
functions, but we write `thing.operation_to_do()` instead of
`operation_to_do(thing)`.

Let's call the `.upper()` **method** on a string. 

```repl
>>> "why are you SHOUTING?".upper()
```

`.upper()` is just *an operation that strings can do*. Here are some more (try
these!):

* `.lower()`
* `.title()`
* `.capitalize()`

Some methods require an argument, or more than one. 

```repl
>>> "I cannot write Python".replace("cannot", "can")
```


## Adding numbers

Just like adding strings, you can add numbers. Only this doesn't *concatenate*
the numbers, it just adds them.

```repl
>>> 5 + 2
```

```exercises
def test_subtract():
    """Can you subtract the numbers instead?"""
    assert '-' in source and result == 3

def test_multiply():
    """Can you multiply the numbers? The multiply operator in Python, like most
    programming languages is `*` (not `×` - you probably don't have an `×` key
    on your keyboard!).
    """
    assert '*' in source and result == 10
```


## Division and remainder

Python's division operator is: `/`. `÷` won't work.

However `/` gives the result as a decimal number. Python also has an integer
division operator `//`, which pairs up with the remainder operator `%`.

```repl
>>> 10 / 3
```

```exercises
def test_floordiv():
    """Calculate the answer `3` by using the `//` operator."""
    assert result == 3

def test_mod():
    """Calculate the answer `1` as the remainder for 10 ÷ 3."""
    assert result == 1

def test_divmod():
    """Try instead the `divmod(x, y)` function gives you both `x // y` and
    `x % y` at the same time.""" 
    assert result == (3, 1) and 'divmod' in source
```

## Parentheses

Python follows normal mathematical order when working out how to do a
calculation. The order is

1. Parentheses aka brackets - `(` and `)`
2. Exponents aka powers aka orders - the `**` operator
3. Multiplication and division (left to right) - `*`, `/`, `//` and `%`
4. Addition and subtraction (left to right) - `+` and `-`

If you're unsure you can just add extra parentheses to make sure the calculation
is done in the order you expect.

```repl
>>> 5 * 3 - 2 - 1
```

```exercises
def check_nums():
    import re
    assert [int(n) for n in re.findall(r'\d+', source)] == [5, 3, 2, 1]

def test_four():
    """Insert parentheses so that the answer is 4."""
    check_nums()
    assert result == 4

def test_14():
    """Insert parentheses so that the answer is 14."""
    check_nums()
    assert result == 14
```
