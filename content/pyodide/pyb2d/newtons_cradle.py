import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
async def _():
    import sys
    if "pyodide" in sys.modules:
        import micropip
        await micropip.install('pyb2d-jupyterlite-backend>=0.4.0')
    return


@app.cell
def _():
    from b2d.testbed import TestbedBase
    import b2d


    class NewtonsCradle(TestbedBase):

        name = "newton's cradle"

        def __init__(self, settings=None):
            super(NewtonsCradle, self).__init__(settings=settings)

            # radius of the circles
            r = 1.0
            # length of the rope
            l = 10.0
            # how many balls
            n = 10

            offset = (l + r, 2 * r)
            dynamic_circles = []
            static_bodies = []
            for i in range(n):
                if i + 1 == n:
                    position = (offset[0] + i * 2 * r + l, offset[1] + l)
                else:
                    position = (offset[0] + i * 2 * r, offset[1])

                circle = self.world.create_dynamic_body(
                    position=position,
                    fixtures=b2d.fixture_def(
                        shape=b2d.circle_shape(radius=r * 0.90),
                        density=1.0,
                        restitution=1.0,
                        friction=0.0,
                    ),
                    linear_damping=0.01,
                    angular_damping=1.0,
                    fixed_rotation=True,
                )
                dynamic_circles.append(circle)

                static_body = self.world.create_static_body(
                    position=(offset[0] + i * 2 * r, offset[1] + l)
                )

                self.world.create_distance_joint(
                    static_body,
                    circle,
                    local_anchor_a=(0, 0),
                    local_anchor_b=(0, 0),
                    max_length=l,
                    stiffness=0,
                )

                static_bodies.append(static_body)

    return NewtonsCradle, b2d


@app.cell
def _(NewtonsCradle, b2d):
    from pyb2d_jupyterlite_backend.async_jupyter_gui import JupyterAsyncGui
    s = JupyterAsyncGui.Settings()
    s.resolution = [1000,300]
    b2d.testbed.run(NewtonsCradle, backend=JupyterAsyncGui, gui_settings=s);
    return


if __name__ == "__main__":
    app.run()

