import marimo

__generated_with = "0.23.6"
app = marimo.App(
    width="full",
    app_title="Parallel Coordinates",
    css_file="content/pyodide/wigglystuff/theme.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ParallelCoordinates

    Interactive parallel coordinates plot powered by HiPlot and Wigglystuff.
    Brush on axes to filter, drag axis labels to reorder, and right-click an axis to color by it.
    """)
    return


@app.cell
async def _():
    import micropip
    await micropip.install(['wigglystuff', 'polars', 'scikit-learn'])

    from sklearn.datasets import load_iris
    from wigglystuff import ParallelCoordinates
    import polars as pl

    iris = load_iris()
    df = pl.DataFrame(
        {name: iris.data[:, i] for i, name in enumerate(iris.feature_names)}
    ).with_columns(pl.Series("target", iris.target))

    widget = ParallelCoordinates(
        df,
        height=300,
        width=700,
        color_by="target",
        color_map={0: "teal", 1: "orange", 2: "crimson"},
    )
    widget
    return (widget,)


@app.cell
def _(widget):
    print(f"Filtered: {len(widget.filtered_indices)} / {len(widget.data)} rows")
    return


if __name__ == "__main__":
    app.run()

