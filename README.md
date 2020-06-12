# Python Now

An interative Python tutorial in the browser, as a static site.

[Jump straight in!](https://lordmauve.github.io/python-now/).

Example screenshot:

![Example Screenshot](https://raw.githubusercontent.com/lordmauve/python-now/master/docs/running-python.png)


## Current status

This project is fully functional, but lacks content.

It can

* Render tutorial pages loaded as Markdown
* Edit and run code, and display output
* Navigate between pages

If you'd like to contribute, you can write content
([it's just Markdown](https://github.com/lordmauve/python-now/tree/master/lessons)),
or check out the [issues](https://github.com/lordmauve/python-now/issues).



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
