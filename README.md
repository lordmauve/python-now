# Python Now

An interative Python tutorial in the browser, as a static site.

[Jump straight in!](https://lordmauve.github.io/python-now/).

Example screenshot:

![Example Screenshot](https://raw.githubusercontent.com/lordmauve/python-now/master/docs/running-python.png)


## Current state:

This project is currently very incomplete. It can

* Edit code using CodeMirror
* Execute that code in a web worker using Brython
* Display output from that program


## Running

To see the tutorial, serve index.html using a web server:

```
$ python3 -m http.server
```

To run the code in an editor, press `Ctrl-Enter`.


## Adding content

* Content is under `lessons/` in Markdown format.
* The navigation panel is in `index.html` in HTML format.

While developing a lesson, you can press `Ctrl-R` to reload the current lesson
more quickly than reloading the page.
