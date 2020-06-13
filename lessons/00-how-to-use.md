# Welcome to Python Now

Welcome to **Python Now**, and welcome to the
[Python programming language](https://www.python.org/).

This is an interactive tutorial for Python - any code examples you see can be
run right here in your browser.


## Getting Started

When you see prompts like `>>>`, this indicates code fragments that you can
edit. You can run it either by pressing the `Enter` key, or by clicking the
"Run" button. Python prints the result of evaluating the code.

```repl
>>> "hello world!"
```

Later we'll put together these fragments into a more complete **program**. In
these examples, you have to use a `print()` function (which prints text to the
screen) to see the output.

Here's an example of what this looks like; a program that prints the first
10 numbers from the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number).
To run this example, either click the "Run" button, or hold `Ctrl` and press
`Enter`.

```python
a = b = 1
for _ in range(10):
    print(a)
    a, b = b, a + b
```

Finally, sometimes there are exercises associated with an editor.

```python
def f(x):
    return x
```

```exercises

def test_double():
    """Make `f(x)` return the **square** of *x*."""
    assert f(10) == 100
    assert f(-1) == 1

def test_square_root():
    """Make `f(x)` return the **square root** of *x*."""
    assert f(25) == 5
    assert f(36) == 6
    assert abs(f(2) - 2 ** 0.5) < 1e-9
```
