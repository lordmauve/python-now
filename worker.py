"""Web Worker script."""

# In web workers, "window" is replaced by "self".
from browser import bind, self
import contextlib
import traceback


class OutputWriter:
    def __init__(self, id, window):
        self.id = id
        self.window = window

    def write(self, text):
        """Write output to the screen."""
        self.window.send([self.id, 'output', text])


@bind(self, "message")
def on_message(event):
    """Handle a message sent by the main script.

    evt.data is the message body.
    """
    msg = event.data
    try:
        id = msg['id']
    except KeyError:
        return
    source = msg['source']
    mode = msg['mode']
    buff = OutputWriter(id, self)

    with contextlib.redirect_stdout(buff), contextlib.redirect_stderr(buff):
        self.send([id, 'ready', 0])
        try:
            code = compile(source, filename='python-now', mode=mode)
            ns = {
                '__name__': '__main__',
                '__filename__': '<python-now>'
            }
            result = exec(code, ns)
        except BaseException:
            self.send([id, 'err', traceback.format_exc()])
        else:
            if result is not None:
                print(repr(result))
