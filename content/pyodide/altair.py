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
    # Altair in `JupyterLite`

    **Altair** is a declarative statistical visualization library for Python.

    Most of the examples below are from: https://altair-viz.github.io/gallery
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Import the dependencies:
    """)
    return


@app.cell
def _():
    # '%pip install -q altair' command supported automatically in marimo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Simple Bar Chart
    """)
    return


@app.cell
def _():
    import altair as alt
    import pandas as pd
    _source = pd.DataFrame({'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]})
    alt.Chart(_source).mark_bar().encode(x='a', y='b')
    return alt, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Simple Heatmap
    """)
    return


@app.cell
def _(alt, pd):
    import numpy as np
    x, y = np.meshgrid(range(-5, 5), range(-5, 5))
    z = x ** 2 + y ** 2
    _source = pd.DataFrame({'x': x.ravel(), 'y': y.ravel(), 'z': z.ravel()})
    alt.Chart(_source).mark_rect().encode(x='x:O', y='y:O', color='z:Q')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Install the Vega Dataset
    """)
    return


@app.cell
def _():
    # '%pip install -q vega_datasets' command supported automatically in marimo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interactive Average
    """)
    return


@app.cell
def _(alt):
    from vega_datasets import data
    _source = data.seattle_weather()
    brush = alt.selection(type='interval', encodings=['x'])
    bars = alt.Chart().mark_bar().encode(x='month(date):O', y='mean(precipitation):Q', opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7))).add_selection(brush)
    line = alt.Chart().mark_rule(color='firebrick').encode(y='mean(precipitation):Q', size=alt.SizeValue(3)).transform_filter(brush)
    alt.layer(bars, line, data=_source)
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Locations of US Airports
    """)
    return


@app.cell
def _(alt, data):
    airports = data.airports.url
    states = alt.topo_feature(data.us_10m.url, feature='states')
    background = alt.Chart(states).mark_geoshape(fill='lightgray', stroke='white').properties(width=500, height=300).project('albersUsa')
    points = alt.Chart(airports).transform_aggregate(latitude='mean(latitude)', longitude='mean(longitude)', count='count()', groupby=['state']).mark_circle().encode(longitude='longitude:Q', latitude='latitude:Q', size=alt.Size('count:Q', title='Number of Airports'), color=alt.value('steelblue'), tooltip=['state:N', 'count:Q']).properties(title='Number of airports in US')
    # US states background
    # airport positions on background
    background + points
    return


if __name__ == "__main__":
    app.run()

