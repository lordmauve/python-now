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

    def on_repl_enter(self, event):
        """Handle the user pressing Enter in REPL mode.
        
        We parse the source in order to detect if the statement is complete,
        and only execute it if so.
        """
        try:
            compile(self.codemirror.getValue(), '', 'eval')
        except SyntaxError:
            return window.CodeMirror.Pass
        else:
            self.run()

    def __init__(self, textarea, repl=False):
        """Construct an editor component and insert it into the document."""
        self.id = len(self.components)

        self.run_but = html.BUTTON('Run ▶', **{'class': 'run'})
        textarea.insertAdjacentElement('beforebegin', self.run_but)
        self.run_but.bind('click', self.run)
        self.outbox = html.DIV()
        textarea.insertAdjacentElement('afterend', self.outbox)

        options = {
            "theme": "darcula",
            "lineNumbers": not repl,
            "viewportMargin": window.Infinity,
            "extraKeys": {
                "Ctrl-Enter": self.run,
                "Esc": self.clear,
            }
        }
        if repl:
            options['gutters'] = ['prompt-gutter']
            options['extraKeys']['Enter'] = self.on_repl_enter
        self.codemirror = window.CodeMirror.fromTextArea(textarea, options)
        if repl:
            prompt = html.SPAN('>>>', **{'class': 'prompt'})
            self.codemirror.setGutterMarker(0, 'prompt-gutter', prompt)
        self.repl = repl

        self.output = html.PRE()
        self.outbox <= self.output
        self.components.append(self)

    def clear(self, _event=None):
        """Clear the output window."""
        self.output.text = ''
        self.output.class_name = ''
    
    def on_output(self, command, params):
        """Show output being sent back from the executor web worker."""
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
            self.outbox.class_name = 'outbox'
            
    def run(self, _event=None):
        """Run the code currently in the editor."""
        self.outbox.class_name = 'loader'
        source = self.codemirror.getValue()
        self.output.text = ''
        executor.send({
            'id': self.id,
            'source': source,
            'mode': 'eval' if self.repl else 'exec'
        })


executor = Worker('run_code')


@bind(executor, 'message')
def on_worker_message(msg):
    """Route a message from the executor to the editor that submitted it."""
    id, command, params = msg.data
    editor = Editor.components[id]
    editor.on_output(command, params)


def load_lesson(name, loader=True):
    """Initiate an AJAX request to load lesson source."""
    if loader:
        document['lesson'].html = '<div class="loader"></div>'
    url = f'lessons/{name}.md'
    ajax.get(url, oncomplete=render_lesson)


FENCE_RE = re.compile(r"^```(\w+)\n(.*?)```", re.DOTALL | re.MULTILINE)
REPL_RE = re.compile(r'^(>>>|\.\.\.) ', re.MULTILINE)


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
        if mode == 'repl':
            el.text = REPL_RE.sub('', content.rstrip())
            Editor(el, repl=True)
        else:
            el.text = content.rstrip()
            Editor(el)


def on_hash_change(event=None):
    """Handle the user clicking on an anchor to a different lesson."""
    fragment = window.location.hash.strip('#')
    if fragment:
        load_lesson(fragment)


def on_key(event):
    """Handle reloading the current lesson from the server."""
    if event.ctrlKey and event.keyCode == 82:
        fragment = window.location.hash.strip('#')
        if fragment:
            load_lesson(fragment, loader=False)
            event.preventDefault()


window.bind('keydown', on_key)
window.bind('hashchange', on_hash_change)



if window.location.hash:
    on_hash_change(None)

# Make sure the executor is warm
executor.send({})
