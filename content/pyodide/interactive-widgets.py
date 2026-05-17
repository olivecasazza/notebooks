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
    # `ipywidgets` Interactive Demo

    Simple demonstration of rendering Interactive widgets in a `jupyterlite` notebook.

    `ipywidgets` can be installed in this deployment (it provides the @jupyter-widgets/jupyterlab-manager federated extension), but you will need to make your own deployment to have access to other interactive widgets libraries.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "Dependencies are preinstalled in the published marimo environment."
    )
    return


@app.cell
def _():
    from ipywidgets import IntSlider

    return (IntSlider,)


@app.cell
def _(IntSlider):
    slider = IntSlider()
    return (slider,)


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(slider):
    slider.value
    return


@app.cell
def _(slider):
    slider.value = 5
    return


@app.cell
def _():
    from ipywidgets import IntText, link

    return IntText, link


@app.cell
def _(IntText):
    text = IntText()
    return (text,)


@app.cell
def _(text):
    text
    return


@app.cell
def _(link, slider, text):
    link((slider, 'value'), (text, 'value'));
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `bqplot` Interactive Demo

    Plotting in JupyterLite

    `bqplot` can be installed in this deployment (it provides the bqplot federated extension), but you will need to make your own deployment to have access to other interactive widgets libraries.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "bqplot is preinstalled in the published marimo environment."
    )
    return


@app.cell
def _():
    from bqplot import Axis, Bars, Figure, LinearScale, Lines
    import numpy as np
    import pandas as pd

    np.random.seed(0)

    n = 100
    x = list(range(n))
    y = np.cumsum(np.random.randn(n)) + 100.0

    sc_x = LinearScale()
    sc_y = LinearScale()

    lines = Lines(
        x=x,
        y=y,
        scales={'x': sc_x, 'y': sc_y}
    )
    ax_x = Axis(scale=sc_x, label='Index')
    ax_y = Axis(scale=sc_y, orientation='vertical', label='lines')

    Figure(marks=[lines], axes=[ax_x, ax_y], title='Lines')
    return Axis, Bars, Figure, LinearScale, Lines, lines, np, pd


@app.cell
def _(lines):
    lines.colors = ['green']
    return


@app.cell
def _(lines):
    lines.fill = 'bottom'
    return


@app.cell
def _(lines):
    lines.marker = 'circle'
    return


@app.cell
def _(Axis, Bars, Figure, LinearScale, np):
    _n = 100

    _x = list(range(_n))
    _y = np.cumsum(np.random.randn(_n))

    _sc_x = LinearScale()
    _sc_y = LinearScale()

    bars = Bars(
        x=_x, y=_y,
        scales={'x': _sc_x, 'y': _sc_y}
    )
    _ax_x = Axis(scale=_sc_x, label='Index')
    _ax_y = Axis(scale=_sc_y, orientation='vertical', label='bars')

    Figure(marks=[bars], axes=[_ax_x, _ax_y], title='Bars', animation_duration=1000)
    return _n, bars


@app.cell
def _(bars, n, np):
    bars.y = np.cumsum(np.random.randn(n))
    return


if __name__ == "__main__":
    app.run()

