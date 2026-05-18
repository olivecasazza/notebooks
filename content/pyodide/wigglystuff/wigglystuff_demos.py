import marimo

__generated_with = "0.23.6"
app = marimo.App(
    width="full",
    app_title="Wigglystuff Demos",
    css_file="content/pyodide/wigglystuff/theme.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wigglystuff demos

    A small gallery of interactive browser-native widgets from
    [Wigglystuff](https://github.com/koaning/wigglystuff). These demos run in
    Marimo WASM via Pyodide: no server, no notebook chrome, just the widgets.
    """)
    return


@app.cell
async def _():
    import micropip

    await micropip.install([
        "wigglystuff",
        "polars",
        "scikit-learn",
        "matplotlib",
        "numpy",
    ])

    import matplotlib.pyplot as plt
    import numpy as np
    import polars as pl
    from sklearn.datasets import load_iris
    from wigglystuff import ChartPuck, ParallelCoordinates, Treemap

    return ChartPuck, ParallelCoordinates, Treemap, load_iris, np, pl, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Parallel coordinates

    Interactive multidimensional data visualization. Brush on axes to filter,
    drag axis labels to reorder, and right-click an axis to color by it.
    """)
    return


@app.cell
def _(ParallelCoordinates, load_iris, pl):
    iris = load_iris()
    iris_df = pl.DataFrame(
        {name: iris.data[:, i] for i, name in enumerate(iris.feature_names)}
    ).with_columns(pl.Series("target", iris.target))

    parallel_widget = ParallelCoordinates(
        iris_df,
        height=320,
        width=700,
        color_by="target",
        color_map={0: "teal", 1: "orange", 2: "crimson"},
    )
    parallel_widget
    return (parallel_widget,)


@app.cell
def _(parallel_widget):
    print(
        f"Filtered: {len(parallel_widget.filtered_indices)} / {len(parallel_widget.data)} rows"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Treemap

    Zoomable hierarchical treemaps. Click a rectangle to zoom in; use the
    breadcrumb to zoom back out. Leaves can carry a single number or a dict of
    `{column: number}`; `value_col` chooses which column drives rectangle size.
    """)
    return


@app.cell
def _(Treemap):
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

    task_treemap = Treemap.from_paths(
        tasks,
        value_col="hours",
        format=lambda v: f"{v:.1f}h",
        root_name="projects",
        width="100%",
    )
    task_treemap
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Treemap from a dataframe

    `from_dataframe` duck-types pandas and polars, using path columns to build
    the hierarchy and value columns for sizing/labels.
    """)
    return


@app.cell
def _(Treemap, pl):
    org_df = pl.DataFrame({
        "dept": ["eng", "eng", "eng", "eng", "design", "design"],
        "team": ["infra", "infra", "product", "product", "brand", "brand"],
        "person": ["alice", "bob", "carol", "dan", "erin", "fran"],
        "hours": [40, 35, 42, 28, 30, 25],
        "tickets": [12, 8, 15, 6, 9, 7],
    })

    org_treemap = Treemap.from_dataframe(
        org_df,
        path_cols=["dept", "team", "person"],
        value_cols=["hours", "tickets"],
        root_name="org",
        format=lambda v: f"{v:.0f}h",
        width=700,
    )
    org_treemap
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Polynomial argument on the complex plane

    Each pixel is colored by $\arg p(z)$, where $p$ is the monic polynomial
    whose roots are the white pucks. Drag the pucks to move roots and watch the
    phase portrait update.

    The widget combines Matplotlib with `ChartPuck`, Wigglystuff's draggable
    point overlay for charts.
    """)
    return


@app.cell
def _(ChartPuck, np, plt):
    def create_grid(dx=1.5, dy=1.5, n_grid=250):
        x, y = np.meshgrid(
            np.linspace(-dx, dx, n_grid),
            np.linspace(-dy, dy, n_grid),
        )
        return x + 1j * y

    rng = np.random.default_rng(42)
    n_roots = 8
    radius = np.sqrt(rng.uniform(0.0, 1.0, n_roots))
    theta = rng.uniform(0.0, 2 * np.pi, n_roots)
    root_xs = (radius * np.cos(theta)).tolist()
    root_ys = (radius * np.sin(theta)).tolist()

    roots = np.array(root_xs) + 1j * np.array(root_ys)
    dx, dy = 1.5, 1.5
    z = create_grid(dx, dy)
    angle = np.angle(z[..., None] - roots).sum(axis=-1)
    angle = (angle + np.pi) % (2 * np.pi) - np.pi

    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
    ax.imshow(angle, origin="lower", extent=[-dx, dx, -dy, dy], cmap="twilight")
    ax.set_xlabel(r"$\Re z$")
    ax.set_ylabel(r"$\Im z$")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.close(fig)

    polynomial_widget = ChartPuck(
        fig,
        x=root_xs,
        y=root_ys,
        drag_x_bounds=(-dx, dx),
        drag_y_bounds=(-dy, dy),
        throttle="dragend",
        puck_color="white",
        puck_radius=4,
    )
    polynomial_widget
    return


if __name__ == "__main__":
    app.run()
