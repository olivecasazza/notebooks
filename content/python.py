import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Python kernel backed by Pyodide

    ![](https://raw.githubusercontent.com/pyodide/pyodide/master/docs/_static/img/pyodide-logo.png)
    """)
    return


@app.cell
def _():
    import pyodide_kernel
    pyodide_kernel.__version__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Simple code execution
    """)
    return


@app.cell
def _():
    a = 3
    return (a,)


@app.cell
def _(a):
    a
    return


@app.cell
def _():
    b = 89

    def sq(x):
        return x * x

    sq(b)
    return


@app.cell
def _():
    print
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Redirected streams
    """)
    return


@app.cell
def _():
    import sys

    print("Error !!", file=sys.stderr)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Error handling
    """)
    return


@app.cell
def _():
    "Hello"

    def dummy_function():
        import missing_module

    return (dummy_function,)


@app.cell
def _(dummy_function):
    dummy_function()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Code completion
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### press `tab` to see what is available in `sys` module
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("Autocomplete examples from the original notebook are omitted in marimo export.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Code inspection
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### using the question mark
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("Inline object inspection via `?` is omitted in marimo export.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### by pressing `shift+tab`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("Shift-tab signature help is omitted in marimo export.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Input support
    """)
    return


@app.cell
async def _():
    name = await input('Enter your name: ')
    return (name,)


@app.cell
def _(name):
    'Hello, ' + name
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Rich representation
    """)
    return


@app.cell
def _():
    from IPython.display import display, Markdown, HTML, JSON, Latex

    return HTML, JSON, Latex, Markdown, display


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## HTML
    """)
    return


@app.cell
def _(HTML, display):
    print('Before display')

    s = '<h1>HTML Title</h1>'
    display(HTML(s))

    print('After display')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Markdown
    """)
    return


@app.cell
def _(Markdown):
    Markdown('''
    # Title

    **in bold**

    ~~Strikthrough~~
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pandas DataFrame
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    from string import ascii_uppercase as letters
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, len(letters))), columns=list(letters))
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Show the same DataFrame
    """)
    return


@app.cell
def _(df):
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## IPython.display module
    """)
    return


@app.cell
def _():
    from IPython.display import clear_output, update_display
    from asyncio import sleep

    return clear_output, sleep, update_display


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Update display
    """)
    return


@app.cell
def _(display):
    class Square:
        color = 'PeachPuff'
        def _repr_html_(self):
            return '''
            <div style="background: %s; width: 200px; height: 100px; border-radius: 10px;">
            </div>''' % self.color
    square = Square()

    display(square, display_id='some-square')
    return (square,)


@app.cell
def _(square, update_display):
    square.color = 'OliveDrab'
    update_display(square, display_id='some-square')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Clear output
    """)
    return


@app.cell
async def _(clear_output, sleep):
    print("hello")
    await sleep(3)
    clear_output()             # will flicker when replacing "hello" with "goodbye"
    print("goodbye")
    return


@app.cell
async def _(clear_output, sleep):
    print("hello")
    await sleep(3)
    clear_output(wait=True)   # prevents flickering
    print("goodbye")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Display classes
    """)
    return


@app.cell
def _(HTML):
    HTML('\n        <div style="background: aliceblue; width: 200px; height: 100px; border-radius: 10px;">\n        </div>')
    return


@app.cell
def _():
    from IPython.display import Math
    Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx')
    return


@app.cell
def _(Latex):
    Latex('\\begin{eqnarray}\n\\nabla \\times \\vec{\\mathbf{B}} -\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{E}}}{\\partial t} & = \\frac{4\\pi}{c}\\vec{\\mathbf{j}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{E}} & = 4 \\pi \\rho \\\\\n\\nabla \\times \\vec{\\mathbf{E}}\\, +\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{B}}}{\\partial t} & = \\vec{\\mathbf{0}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{B}} & = 0 \n\\end{eqnarray}')
    return


@app.cell
async def _(sleep):
    from IPython.display import ProgressBar

    for i in ProgressBar(10):
        await sleep(0.1)
    return


@app.cell
def _(JSON):
    JSON(['foo', {'bar': ('baz', None, 1.0, 2)}], metadata={}, expanded=True, root='test')
    return


@app.cell
def _():
    from IPython.display import GeoJSON
    GeoJSON(
      data={
          "type": "Feature",
          "geometry": {
              "type": "Point",
              "coordinates": [11.8, -45.04]
          }
      }, url_template="http://s3-eu-west-1.amazonaws.com/whereonmars.cartodb.net/{basemap_id}/{z}/{x}/{y}.png",
      layer_options={
          "basemap_id": "celestia_mars-shaded-16k_global",
          "attribution" : "Celestia/praesepe",
          "tms": True,
          "minZoom" : 0,
          "maxZoom" : 5
      }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Network requests and JSON
    """)
    return


@app.cell
def _():
    import json
    from js import fetch

    return fetch, json


@app.cell
async def _(JSON, fetch, json):
    res = await fetch('https://httpbin.org/get')
    text = await res.text()
    obj = json.loads(text) 
    JSON(obj)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sympy
    """)
    return


@app.cell
def _():
    from sympy import Integral, sqrt, symbols, init_printing

    init_printing()

    x = symbols('x')

    Integral(sqrt(1 / x), x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Magics
    """)
    return


@app.cell
def _():
    import os
    os.listdir()
    return (os,)


@app.cell
def _(os):
    os.chdir('/home')
    return




@app.cell
def _(os):
    current_path = os.getcwd()
    print(current_path)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("The original `%writefile` magic example is omitted in marimo export.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("The original `%history` magic example is omitted in marimo export.")
    return


@app.cell
def _():
    import time

    return (time,)


@app.cell
def _(time):
    # magic command not supported in marimo; please file an issue to add support
    # %%timeit 

    time.sleep(0.1)
    return


if __name__ == "__main__":
    app.run()

