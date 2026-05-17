import marimo

__generated_with = "0.23.6"
app = marimo.App(
    width="full",
    app_title="Polynomials on Complex Plane",
    css_file="content/pyodide/wigglystuff/theme.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Polynomial argument on the complex plane

    Each pixel is colored by $\arg p(z)$, where $p$ is the monic polynomial whose
    roots are the white pucks.

    Interactive widget powered by ChartPuck from Wigglystuff and Matplotlib.
    """)
    return


@app.cell
async def _():
    import piplite
    await piplite.install(['wigglystuff', 'matplotlib', 'numpy'])

    import numpy as np
    import matplotlib.pyplot as plt
    from wigglystuff import ChartPuck

    def create_grid(dx=1., dy=1., n_grid=250):
        x, y = np.meshgrid(np.linspace(-dx, dx, n_grid), np.linspace(-dy, dy, n_grid))
        return x + 1.j * y

    rng = np.random.default_rng(42)
    n_roots = 8
    r = np.sqrt(rng.uniform(0., 1., n_roots))
    th = rng.uniform(0., 2 * np.pi, n_roots)
    xs = (r * np.cos(th)).tolist()
    ys = (r * np.sin(th)).tolist()

    roots = np.array(xs) + 1.j * np.array(ys)
    dx, dy = 1.5, 1.5
    z = create_grid(dx, dy)
    ang = np.angle(z[..., None] - roots).sum(axis=-1)
    ang = (ang + np.pi) % (2 * np.pi) - np.pi

    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
    ax.imshow(ang, origin="lower", extent=[-dx, dx, -dy, dy], cmap="twilight")
    ax.set_xlabel(r"$\Re z$")
    ax.set_ylabel(r"$\Im z$")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.close(fig) # Prevent duplicate display

    puck = ChartPuck(
        fig,
        x=list(xs),
        y=list(ys),
        drag_x_bounds=(-dx, dx),
        drag_y_bounds=(-dy, dy),
        throttle="dragend",
        puck_color="white",
        puck_radius=4,
    )
    puck
    return


if __name__ == "__main__":
    app.run()

