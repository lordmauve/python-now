from browser import document, html, alert, markdown, bind
from io import StringIO
import contextlib


class Editor:
    def on_key_down(self, event):
        if event.keyCode == 13 and event.ctrlKey:
            event.preventDefault()
            self.run()

    def __init__(self, placeholderText="# Write some Python code here"):
        self.text = html.TEXTAREA(Class="textarea")
        self.text.value = placeholderText
        self.output = html.PRE()
        document <= self.text
        document <= self.output
        self.text.bind("keydown", self.on_key_down)

    def on_worker_message(msg):
	cmd, params = msg
	if cmd == 'output':
	    node = document.createTextNode(text)
	    self.output.appendChild(node)

    def run(self):
        source = self.text.value
        code = compile(source, 'input', 'exec')
        buff = OutputWriter(self.output)
        #buff = StringIO()
        with contextlib.redirect_stdout(buff), contextlib.redirect_stderr(buff):
            try:
                exec(code, {})
            except:
                import traceback
                traceback.print_exc()


Editor("""
from itertools import islice
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

print(*islice(fib(), 10))
""")
