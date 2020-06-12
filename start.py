from browser import document, html, bind, window
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

    def __init__(self, placeholder="# Write some Python code here"):
        """Construct an editor component and insert it into the document."""
        self.id = len(self.components)
        self.codemirror = window.CodeMirror(document.body, {
            "value": placeholder,
            "theme": "darcula",
            "lineNumbers": True,
            "viewportMargin": window.Infinity,
            "extraKeys": {
                "Ctrl-Enter": self.run,
            }
        })

        self.outbox = html.DIV()
        document <= self.outbox
        self.output = html.PRE()
        self.outbox <= self.output
        self.components.append(self)
    
    def on_output(self, command, params):
        if command == 'output':
            node = document.createTextNode(params)
            self.output <= node
            self.output.class_name = 'output'
        elif command == 'err':
            err = html.SPAN(params)
            err.class_name = 'err'
            self.output <= err
        elif command == 'result':
            pass  # discard for now
        elif command == 'ready':
            self.outbox.class_name = ''
            
    def run(self, _event=None):
        self.outbox.class_name = 'loader'
        source = self.codemirror.getValue()
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
