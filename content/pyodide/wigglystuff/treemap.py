import marimo

__generated_with = "0.23.6"
app = marimo.App(
    width="full",
    app_title="Treemap",
    css_file="content/pyodide/wigglystuff/theme.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Treemap

    A zoomable hierarchical treemap. Click a rectangle to zoom in; click
    the breadcrumb to zoom back out.

    Leaves can carry a single number or a dict of `{column: number}`. When
    values are dicts, pass `value_col` to pick which column drives rectangle
    sizing, and use `format=` to humanize the label.
    """)
    return


@app.cell
async def _():
    import piplite
    await piplite.install(['wigglystuff', 'polars'])

    from wigglystuff import Treemap

    tasks = {
        "analytics/cluster/Agglomerative": {"hours": 39.5, "count": 12},
        "analytics/cluster/Community": {"hours": 22.0, "count": 7},
        "analytics/cluster/Hierarchical": {"hours": 48.25, "count": 18},
        "analytics/graph/Betweenness": {"hours": 18.0, "count": 4},
        "analytics/graph/MaxFlow": {"hours": 56.5, "count": 15},
        "analytics/graph/Shortest": {"hours": 32.75, "count": 9},
        "animate/Easing": {"hours": 84.0, "count": 24},
        "animate/Transition": {"hours": 41.5, "count": 11},
        "animate/Transitioner": {"hours": 102.25, "count": 31},
        "animate/Tween": {"hours": 29.0, "count": 8},
        "data/converters/JSONConverter": {"hours": 22.5, "count": 6},
    }

    widget = Treemap.from_paths(
        tasks,
        value_col="hours",
        format=lambda v: f"{v:.1f}h",
        root_name="projects",
        width="100%",
    )
    widget
    return (Treemap,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Simulated deep hierarchy

    A synthetic tree generated with `random`, branching up to eight levels
    deep with variable fan-out.
    """)
    return


@app.cell
def _(Treemap):
    import random

    rng = random.Random(42)
    paths = {}

    def walk(depth_left: int, parts: list[str]) -> None:
        if depth_left == 0 or (depth_left < 6 and rng.random() < 0.25):
            paths["/".join(parts)] = rng.randint(50, 2500)
            return
        for i in range(rng.randint(2, 4)):
            walk(depth_left - 1, parts + [chr(ord("a") + i)])

    walk(8, [])

    deep_widget = Treemap.from_paths(paths, root_name="fs", width="100%")
    deep_widget
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## From a dataframe

    `from_dataframe` duck-types pandas and polars.
    """)
    return


@app.cell
def _(Treemap):
    import polars as pl

    df = pl.DataFrame({
        "dept": ["eng", "eng", "eng", "eng", "design", "design"],
        "team": ["infra", "infra", "product", "product", "brand", "brand"],
        "person": ["alice", "bob", "carol", "dan", "erin", "fran"],
        "hours": [40, 35, 42, 28, 30, 25],
        "tickets": [12, 8, 15, 6, 9, 7],
    })

    df_widget = Treemap.from_dataframe(
        df,
        path_cols=["dept", "team", "person"],
        value_cols=["hours", "tickets"],
        root_name="org",
        format=lambda v: f"{v:.0f}h",
        width=800,
    )
    df_widget
    return


if __name__ == "__main__":
    app.run()

