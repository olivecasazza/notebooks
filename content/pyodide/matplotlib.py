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
    ## Matplotlib
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    return np, plt


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 1000)
    plt.plot(_x, np.sin(_x))
    return


@app.cell
def _(plt):
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Matplotlib: support for widgets backend
    """)
    return


@app.cell
def _():
    # '%pip install -q ipympl' command supported automatically in marimo
    return


@app.cell
def _():
    # '%matplotlib widget' command supported automatically in marimo
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 1000)
    plt.plot(_x, np.sin(_x))
    return


if __name__ == "__main__":
    app.run()

