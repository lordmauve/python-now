from browser import document, html, alert, markdown
from io import StringIO
import contextlib


class editor():
    def onKeydown(self, event):
        if event.keyCode == 13 and event.ctrlKey:
            event.preventDefault()
            self.run()

    def __init__(self, placeholderText="# Write some Python code here"):
        self.exec = html.INPUT(type='radio', name='mode',
                               value='exec', checked="checked")
        self.eval = html.INPUT(type='radio', name='mode', value='eval')
        # self.single = html.INPUT(type='radio', name='mode', value='single')
        document <= self.exec + html.LABEL('Script')
        document <= self.eval + html.LABEL('Expression')

        self.text = html.TEXTAREA(Class="textarea")
        self.text.value = placeholderText
        self.output = html.PRE()
        document <= self.text
        document <= self.output
        self.text.bind("keydown", self.onKeydown)

    def run(self):
        source = self.text.value
        mode = 'exec' if self.exec.checked else 'eval'
        print(mode)
        code = compile(source, 'input', mode)
        buff = StringIO()
        with contextlib.redirect_stdout(buff), contextlib.redirect_stderr(buff):
            try:
                result = exec(code, {})
            except:
                import traceback
                traceback.print_exc()
            else:
                if result is not None:
                    print(repr(result))
                else:
                    print('None')
        self.output.text = buff.getvalue()


editor("""
from itertools import islice
def fib():
    a, b = 1, 1
    while True: 
        yield a
        a, b = b, a + b   

print(*islice(fib(), 10))
""")
