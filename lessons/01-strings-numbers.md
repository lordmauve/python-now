# Strings

In programming, a **string** is a piece of text. Python calls strings by the
abbreviation `str` and lets you type them out by enclosing them in single-quote
chararacters `'` or double-quote characters `"`.

Try changing this example so that it reads "hello world!".

```repl
>>> 'hello!'
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

You can also add three strings. Can you make this say `'joined up'` by adding
an extra string? You need one of the strings to include a space inside the
quotes, or else it will say `'joinedup'`.


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

* Can you subtract the numbers instead?
* Can you multiply the numbers? The multiply operator in Python, like most
  programming languages is `*` (not `×`).
