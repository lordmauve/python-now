from browser import document, html, bind
from browser.worker import Worker


class Editor:
    """A Python code editor component which executes code with Brython."""

    #: A list of the Editor instances
    components = []

    def on_key_down(self, event):
        """Handle a key press in the editor component."""
        if event.keyCode == 13 and event.ctrlKey:
            event.preventDefault()
            self.run()

    def __init__(self, placeholderText="# Write some Python code here"):
        """Construct an editor component and insert it into the document."""
        self.id = len(self.components)
        self.text = html.TEXTAREA(Class="textarea")
        self.text.value = placeholderText
        self.output = html.PRE()
        document <= self.text
        document <= self.output
        self.text.bind("keydown", self.on_key_down)
        self.components.append(self)

    def on_output(self, command, params):
        if command == 'output':
            node = document.createTextNode(params)
            self.output <= node
        elif command == 'err':
            self.output.text = params
        elif command == 'result':
            pass  # discard for now

    def run(self):
        source = self.text.value
        self.output.text = ''
        executor.send({
            'id': self.id,
            'exec': source
        })


executor = Worker('run_code')


@bind(executor, 'message')
def on_worker_message(msg):
    id, command, params = msg.data
    editor = Editor.components[id]
    editor.on_output(command, params)


Editor("""
from itertools import islice
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

print(*islice(fib(), 10))
""")
