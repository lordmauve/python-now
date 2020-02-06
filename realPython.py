from browser import document, html, alert
from io import StringIO
import contextlib

# bind event 'click' on button to function echo


class editor():
    def onKeydown(self, event):
        if event.keyCode == 13 and event.ctrlKey:
            event.preventDefault()
            self.run()

    def __init__(self, placeholderText="# Write some Python code here"):

        self.text = html.TEXTAREA(Class="textarea")
        self.text.value = placeholderText
        self.output = html.PRE()
        document <= self.text
        document <= self.output
        self.text.bind("keydown", self.onKeydown)

    def run(self):
        source = self.text.value
        code = compile(source, 'input', 'exec')
        buff = StringIO()
        with contextlib.redirect_stdout(buff):
            exec(code)
        self.output.text = buff.getvalue()


editor()
editor("""
from itertools import islice
def fib():
    a, b = 1, 1
    while True: 
        yield a
        a, b = b, a + b   

print(*islice(fib(), 10))
""")
