"""Web Worker script."""

# In web workers, "window" is replaced by "self".
from browser import bind, self
import contextlib


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
    id = msg['id']
    code = msg['exec']
    buff = OutputWriter(id, self)

    with contextlib.redirect_stdout(buff), contextlib.redirect_stderr(buff):
        self.send([id, 'ready', 0])
        try:
            result = exec(code, {})
        except BaseException:
            import traceback
            traceback.print_exc()
            self.send([id, 'err', traceback.format_exc()])
        else:
            self.send([id, 'result', result])
