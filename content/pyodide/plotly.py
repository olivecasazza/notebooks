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
    # Plotly in JupyterLite

    `plotly.py` is an interactive, open-source, and browser-based graphing library for Python: https://plotly.com/python/
    """)
    return


@app.cell
def _():
    # '%pip install -q nbformat plotly' command supported automatically in marimo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Basic Figure
    """)
    return


@app.cell
def _():
    import plotly.graph_objects as go
    _fig = go.Figure()
    _fig.add_trace(go.Scatter(y=[2, 1, 4, 3]))
    _fig.add_trace(go.Bar(y=[1, 4, 3, 2]))
    _fig.update_layout(title='Hello Figure')
    _fig.show()
    return (go,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Basic Table with a Pandas DataFrame
    """)
    return


@app.cell
async def _(go):
    import pandas as pd
    from js import fetch
    URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
    res = await fetch(URL)
    text = await res.text()
    filename = 'data.csv'
    with open(filename, 'w') as f:
        f.write(text)
    df = pd.read_csv(filename)
    _fig = go.Figure(data=[go.Table(header=dict(values=list(df.columns), fill_color='paleturquoise', align='left'), cells=dict(values=[df.Rank, df.State, df.Postal, df.Population], fill_color='lavender', align='left'))])
    _fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quiver Plot with Points
    """)
    return


@app.cell
def _(go):
    import plotly.figure_factory as ff
    import numpy as np
    x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.25))
    z = x * np.exp(-x ** 2 - y ** 2)
    v, u = np.gradient(z, 0.2, 0.2)
    _fig = ff.create_quiver(x, y, u, v, scale=0.25, arrow_scale=0.4, name='quiver', line_width=1)
    _fig.add_trace(go.Scatter(x=[-0.7, 0.75], y=[0, 0], mode='markers', marker_size=12, name='points'))
    _fig.show()
    return


if __name__ == "__main__":
    app.run()

