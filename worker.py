"""Web Worker script."""

# In web workers, "window" is replaced by "self".
from browser import bind, self
import contextlib
import traceback


class OutputWriter:
    def __init__(self, id, window):
        self.id = id
        self.window = window
        self.buf = []

    def write(self, text):
        """Write output to the screen."""
        self.buf.append(text)
        self.window.send([self.id, 'output', text])

    def getvalue(self):
        """Get everything that was printed."""
        return ''.join(self.buf)


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
            namespace = {
                '__name__': '__main__',
                '__filename__': '<python-now>'
            }
            result = exec(code, namespace)
        except BaseException:
            self.send([id, 'err', traceback.format_exc()])
        else:
            if result is not None:
                print(repr(result))

        # If we have exercises, run them as tests
        if msg['exercises']:
            if mode == 'exec':
                test_ns = namespace.copy()
            else:
                test_ns = {}

            test_ns.update(
                source=source,
                result=result,
                output=buff.getvalue(),
            )
                
            exec(msg['exercises'], test_ns)

            tests = []
            for name, test in test_ns.items():
                if name.startswith('test_') and callable(test):
                    tests.append(test)
                
            for test_id, test in enumerate(tests):
                try:
                    test()
                except BaseException:
                    err = traceback.format_exc() + repr(test_ns)
                else:
                    err = None
                self.send([id, 'ex_result', (test_id, err)])
