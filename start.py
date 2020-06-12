"""UI system for Python Now.

This is a Brython front-end which loads and displays lessons.
"""
import re
from browser import document, html, bind, window, ajax, markdown
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

    def __init__(self, textarea):
        """Construct an editor component and insert it into the document."""
        self.id = len(self.components)

        self.run_but = html.BUTTON('Run ▶', **{'class': 'run'})
        textarea.insertAdjacentElement('beforebegin', self.run_but)
        self.run_but.bind('click', self.run)
        self.outbox = html.DIV()
        textarea.insertAdjacentElement('afterend', self.outbox)

        self.codemirror = window.CodeMirror.fromTextArea(textarea, {
            "theme": "darcula",
            "lineNumbers": True,
            "viewportMargin": window.Infinity,
            "extraKeys": {
                "Ctrl-Enter": self.run,
            }
        })
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
        """Run the code currently in the editor."""
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
    """Route a message from the executor to the editor that submitted it."""
    id, command, params = msg.data
    editor = Editor.components[id]
    editor.on_output(command, params)


def load_lesson(name):
    """Initiate an AJAX request to load lesson source."""
    url = f'lessons/{name}.md'
    ajax.get(url, oncomplete=render_lesson)


FENCE_RE = re.compile(r"^```(\w+)\n(.*?)```", re.DOTALL | re.MULTILINE)


def render_lesson(req):
    """Display the given markdown document as a lesson."""
    url = req.responseURL
    if req.status == 200:
        source = req.text
    else:
        source = f"""# Error
        
There was an error loading the lesson {url}.

    HTTP Error {req.status}
"""

    interactions = []

    def match_code(mo):
        obj_id = f'{url}-{len(interactions)}'
        mode, content = mo.groups()
        interactions.append((obj_id, mode, content))
        return f'<textarea id="{obj_id}"></textarea>'

    source = FENCE_RE.sub(
        match_code,
        source,
    )
    mk, scripts = markdown.mark(source)

    container = document['lesson']
    container.class_name = ''
    container.html = mk

    for id, mode, content in interactions:
        el = document[id]
        el.text = content.rstrip()
        Editor(el)

load_lesson("01-strings")


# Make sure the executor is warm
executor.send({})
