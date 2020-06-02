"""Web Worker script."""

# In web workers, "window" is replaced by "self".
from browser import bind, self
import contextlib


class OutputWriter:
    def __init__(self, window):
        self.window = window

    def write(self, text):
    	self.window.send(['output', text])


@bind(self, "runcode")
def on_run_code(evt):
    """Handle a message sent by the main script.
    evt.data is the message body.
    """
    source = evt.data
    buff = OutputWriter(self)
    with contextlib.redirect_stdout(buff), contextlib.redirect_stderr(buff):
	try:
	    exec(code, {})
	except:
	    import traceback
	    traceback.print_exc()
    self.send(workerResult)
