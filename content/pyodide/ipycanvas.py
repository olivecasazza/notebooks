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
    # ipycanvas: John Conway's Game Of Life
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Some of the following code is adapted from https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
    """)
    return


@app.cell
def _():
    # '%pip install -q ipycanvas' command supported automatically in marimo
    return


@app.cell
def _():
    import asyncio

    import numpy as np

    from ipycanvas import RoughCanvas, hold_canvas

    return RoughCanvas, asyncio, hold_canvas, np


@app.cell
def _(np):
    def life_step(x):
        """Game of life step"""
        nbrs_count = sum(np.roll(np.roll(x, i, 0), j, 1)
                         for i in (-1, 0, 1) for j in (-1, 0, 1)
                         if (i != 0 or j != 0))
        return (nbrs_count == 3) | (x & (nbrs_count == 2))

    return (life_step,)


@app.cell
def _(hold_canvas, n_pixels, np):
    def draw(x, canvas, color='black'):
        with hold_canvas(canvas):
            canvas.clear()
            canvas.fill_style = '#FFF0C9'
            canvas.rough_fill_style = 'solid'
            canvas.fill_rect(-10, -10, canvas.width + 10, canvas.height + 10)
            canvas.rough_fill_style = 'cross-hatch'

            canvas.fill_style = color
            canvas.stroke_style = color

            living_cells = np.where(x)
        
            rects_x = living_cells[1] * n_pixels
            rects_y = living_cells[0] * n_pixels

            canvas.fill_rects(rects_x, rects_y, n_pixels)
            canvas.stroke_rects(rects_x, rects_y, n_pixels)

    return (draw,)


@app.cell
def _(np):
    glider_gun =\
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    x = np.zeros((50, 70), dtype=bool)
    x[1:10,1:37] = glider_gun
    return (x,)


@app.cell
def _(RoughCanvas, x):
    n_pixels = 15

    canvas = RoughCanvas(width=x.shape[1]*n_pixels, height=x.shape[0]*n_pixels)
    canvas.fill_style = '#FFF0C9'
    canvas.rough_fill_style = 'solid'
    canvas.fill_rect(0, 0, canvas.width, canvas.height)

    canvas
    return canvas, n_pixels


@app.cell
def _(canvas, draw, x):
    draw(x, canvas, '#5770B3')
    return


@app.cell
async def _(asyncio, canvas, draw, life_step, x):
    for _ in range(300):
        x_1 = life_step(x)
        draw(x_1, canvas, '#5770B3')
        await asyncio.sleep(0.1)
    return


if __name__ == "__main__":
    app.run()

