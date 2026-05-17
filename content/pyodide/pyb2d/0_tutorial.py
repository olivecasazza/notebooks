import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
async def _():
    import sys
    if "pyodide" in sys.modules:
        import piplite
        await piplite.install('pyb2d-jupyterlite-backend>=0.4.2')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    pyb2d is imported as b2d
    """)
    return


@app.cell
def _():
    import b2d
    # import pyb2d_jupyterlite_backend
    from pyb2d_jupyterlite_backend.async_jupyter_gui import JupyterAsyncGui
    import numpy as np
    import matplotlib.pylab as plt

    return JupyterAsyncGui, b2d, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tutorial 0: A free falling body
    The first step with Box2D is the creation of the world. The world is parametrized by a gravity vector.
    """)
    return


@app.cell
def _(b2d):
    # the world
    gravity = (0, -10)
    world = b2d.World(gravity)
    return (world,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a circle-shaped body
    """)
    return


@app.cell
def _(b2d, world):
    # the body def
    body_def = b2d.BodyDef()
    body_def.type = b2d.BodyType.dynamic
    body_def.position = (0, 0)

    # the body
    body = world.create_body(body_def)

    # shape
    circle_shape = b2d.CircleShape()
    circle_shape.radius = 1.0

    # the fixture
    fixture_def = b2d.FixtureDef()
    fixture_def.shape = circle_shape
    fixture_def.density = 1.0

    # create and add the fixture to the body
    fixture = body.create_fixture(fixture_def)
    return (body,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can now have a look at the world: We render the world st. each meter in the Box2D world will be 100 pixels in the image:
    """)
    return


@app.cell
def _(b2d, world):
    # from b2d.plot import render_world
    b2d.plot.plot_world(world, ppm=100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lets run the world for a total of 5 seconds.
    Usually one wants to run the world at a certain frame rate.
    With the frame rate and the total time we can compute the delta for each iteration and how many steps we need
    """)
    return


@app.cell
def _():
    t = 5
    fps = 40
    dt = 1.0 / fps
    n_steps = int(t / dt + 0.5)
    print(f"t={t} fps={fps} dt={dt} n_steps={n_steps}")
    return dt, n_steps


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    in each step we query the bodies position and velocity and store then for later plotting
    """)
    return


@app.cell
def _(body, dt, n_steps, np, world):
    positions = np.zeros([n_steps, 2])
    velocites = np.zeros([n_steps, 2])
    timepoints = np.zeros([n_steps])
    t_elapsed = 0.0
    for _i in range(n_steps):
        positions[_i, :] = body.world_center
        velocites[_i, :] = body.linear_velocity
        timepoints[_i] = t_elapsed
        world.step(time_step=dt, velocity_iterations=1, position_iterations=1)
        t_elapsed = t_elapsed + dt
    return positions, timepoints


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    plot the y-position against the time. We can see that the body is falling down in an accelerating way:
    """)
    return


@app.cell
def _(plt, positions, timepoints):
    plt.plot(timepoints, positions[:, 1])
    plt.ylabel('y-poistion [meter]')
    plt.xlabel('t [sec]')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    as expected the x position is not changing since the gravity vector is non-zero only in the x direction
    """)
    return


@app.cell
def _(plt, positions, timepoints):
    plt.plot(timepoints, positions[:, 0])
    plt.ylabel('x-poistion [meter]')
    plt.xlabel('t [sec]')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tutorial 1: A  falling body in a box, more pythonic
    Create a world, but in a more pythonic way, and animate the world
    """)
    return


@app.cell
def _(b2d):
    # the world
    world_1 = b2d.world(gravity=(0, -10))
    body_1 = world_1.create_dynamic_body(position=(5, 5), fixtures=b2d.fixture_def(shape=b2d.circle_shape(radius=1), density=1, restitution=0.75))
    # create the dynamic body
    box_shape = b2d.ChainShape()
    box_shape.create_loop([(0, 0), (0, 10), (10, 10), (10, 0)])
    box = world_1.create_static_body(position=(0, 0), fixtures=b2d.fixture_def(shape=box_shape, friction=0))
    # create a box
    b2d.plot.animate_world(world_1, ppm=20, t=10)
    return (world_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    note that when we animate that world again, the body has already been fallen
    """)
    return


@app.cell
def _(b2d, world_1):
    b2d.plot.animate_world(world_1, ppm=20, t=2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tutorial 2: Interactive worlds
    While animating the world already is already nice, interacting with the world is even better.
    pyb2d has a framwork to interact with the world for multiple backends.
    This framework is called `TestbedBase` since you can "test" your world in an interactive way
    """)
    return


@app.cell
def _(JupyterAsyncGui, b2d):
    from b2d.testbed import TestbedBase

    class InteractiveExample(TestbedBase):
        def __init__(self, settings=None):
            super(InteractiveExample, self).__init__(settings=settings)
            # create two balls
            body = self.world.create_dynamic_body(position=(5, 5),
                fixtures=b2d.fixture_def(shape=b2d.circle_shape(radius=1), density=1, restitution=0.5),
            )
            body = self.world.create_dynamic_body(position=(8, 5),
                fixtures=b2d.fixture_def(shape=b2d.circle_shape(radius=1), density=1, restitution=0.8),
            )
            # create a box
            box_shape = b2d.ChainShape()
            box_shape.create_loop([(0, 0), (0, 10),(10,10),(10, 0)])
            box = self.world.create_static_body(
                position=(0, 0), fixtures=b2d.fixture_def(shape=box_shape, friction=0)
            )
        
    s = JupyterAsyncGui.Settings()
    s.resolution = [300,300]
    b2d.testbed.run(InteractiveExample, backend=JupyterAsyncGui, gui_settings=s);
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tutorial 3: Joints
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tutorial 3.1: Prismatic Joint
    """)
    return


@app.cell
def _(b2d):
    world_2 = b2d.world(gravity=(0, -10))
    anchor_body = world_2.create_static_body(position=(0, 0))
    _b = world_2.create_dynamic_body(position=(10, 10), fixtures=b2d.fixture_def(shape=b2d.polygon_shape(box=[2, 0.5]), density=1), linear_damping=0.0, angular_damping=0.0)
    world_2.create_prismatic_joint(anchor_body, _b, local_axis_a=(1, 1))
    b2d.plot.animate_world(world_2, ppm=20, t=3, bounding_box=((0, 0), (10, 10)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tutorial 3.2: Pully Joint
    """)
    return


@app.cell
def _(b2d):
    world_3 = b2d.world(gravity=(0, -10))
    _a = world_3.create_dynamic_body(position=(-5, 0), fixtures=b2d.fixture_def(shape=b2d.polygon_shape(box=[2, 0.8]), density=1), linear_damping=0.0, angular_damping=0.0)
    _b = world_3.create_dynamic_body(position=(5, 0), fixtures=b2d.fixture_def(shape=b2d.polygon_shape(box=[2, 0.5]), density=1), linear_damping=0.0, angular_damping=0.0)
    world_3.create_pully_joint(_a, _b, length_a=10, length_b=10, ground_anchor_a=(-5, 10), ground_anchor_b=(5, 10), local_anchor_a=(0, 0), local_anchor_b=(0, 0))
    b2d.plot.animate_world(world_3, ppm=20, t=5, bounding_box=((-10, -12), (10, 12)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tutorial 3.3: Revolute Joint
    """)
    return


@app.cell
def _(b2d):
    world_4 = b2d.world(gravity=(0, -10))
    _bodies = []
    _b = world_4.create_static_body(position=(0, 15))
    _bodies.append(_b)
    for _i in range(5):
        _b = world_4.create_dynamic_body(position=(_i * 4 + 2, 15), fixtures=b2d.fixture_def(shape=b2d.polygon_shape(box=[2, 0.5]), density=1), linear_damping=0.0, angular_damping=0.0)
        _bodies.append(_b)
    world_4.create_revolute_joint(_bodies[0], _bodies[1], local_anchor_a=(0, 0), local_anchor_b=(-2, 0.0))
    for _i in range(1, len(_bodies) - 1):
        _a = _bodies[_i]
        _b = _bodies[_i + 1]
        world_4.create_revolute_joint(_a, _b, local_anchor_a=(2, 0.0), local_anchor_b=(-2, 0.0))
    b2d.plot.animate_world(world_4, ppm=20, t=5, bounding_box=((-20, -10), (20, 20)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tutorial 3.4: Weld Joint
    """)
    return


@app.cell
def _(b2d):
    world_5 = b2d.world(gravity=(0, -10))
    _bodies = []
    _b = world_5.create_static_body(position=(0, 4), fixtures=b2d.fixture_def(shape=b2d.polygon_shape(box=[0.3, 0.5])))
    _bodies.append(_b)
    for _i in range(4):
        _b = world_5.create_dynamic_body(position=(_i + 1.0, 4), fixtures=b2d.fixture_def(shape=b2d.polygon_shape(box=[0.3, 0.5]), density=0.1), linear_damping=2.5, angular_damping=2.5)
        _bodies.append(_b)
    for _i in range(len(_bodies) - 1):
        _a = _bodies[_i]
        _b = _bodies[_i + 1]
        world_5.create_weld_joint(_a, _b, local_anchor_a=(0.5, 0.5), local_anchor_b=(-0.5, 0.5), damping=0.1, reference_angle=0, stiffness=20)
        world_5.create_weld_joint(_a, _b, local_anchor_a=(0.5, -0.5), local_anchor_b=(-0.5, -0.5), damping=0.1, reference_angle=0, stiffness=20)
    b2d.plot.animate_world(world_5, ppm=20, t=5, bounding_box=((0, -5), (5, 5)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tutorial 3.5: Wheel Joint
    """)
    return


@app.cell
def _(b2d, np):
    world_6 = b2d.world(gravity=(0, -10))
    edge = world_6.create_static_body(position=(0, 0), fixtures=b2d.fixture_def(shape=b2d.edge_shape([(-20, 0), (5, 0)])))
    x = np.linspace(5, 50, 10)
    y = np.random.rand(10) * 4 - 2
    y[0] = 0
    # random slope
    xy = np.stack([x, y]).T
    xy = np.flip(xy, axis=0)
    edge = world_6.create_static_body(position=(0, 0), fixtures=b2d.fixture_def(shape=b2d.chain_shape(xy, prev_vertex=(10, 0))))
    left_wheel = world_6.create_dynamic_body(position=(-3, 2), fixtures=b2d.fixture_def(shape=b2d.circle_shape(radius=2), density=1))
    right_wheel = world_6.create_dynamic_body(position=(3, 2), fixtures=b2d.fixture_def(shape=b2d.circle_shape(radius=2), density=1))
    chasis = world_6.create_dynamic_body(position=(0, 2), fixtures=b2d.fixture_def(shape=b2d.polygon_shape(box=[3, 0.5]), density=1))
    wheel_joint_def = dict(stiffness=10, enable_motor=True, motor_speed=-100, max_motor_torque=100, collide_connected=False, enable_limit=True, lower_translation=-0.4, upper_translation=0.4, local_axis_a=(0, 1))
    world_6.create_wheel_joint(chasis, left_wheel, local_anchor_a=(-3, 0), **wheel_joint_def)
    world_6.create_wheel_joint(chasis, right_wheel, local_anchor_a=(3, 0), **wheel_joint_def)
    # create car
    b2d.plot.animate_world(world_6, ppm=20, t=15, bounding_box=((-10, -5), (20, 5)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tutorial 3.6: Distance Joint
    """)
    return


@app.cell
def _(b2d):
    world_7 = b2d.world(gravity=(0, -10))
    for _i in range(10):
        anchor = world_7.create_static_body(position=(_i, 0))
        body_2 = world_7.create_dynamic_body(position=(_i, -10), fixtures=b2d.fixture_def(shape=b2d.circle_shape(radius=0.4), density=0.5))
        world_7.create_distance_joint(anchor, body_2, length=10, stiffness=0.5 * (_i + 1))
    b2d.plot.animate_world(world_7, ppm=20, t=10, bounding_box=((-2, -20), (10, 0)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tutorial 4: Particles
    """)
    return


@app.cell
def _(b2d):
    world_8 = b2d.world(gravity=(0, -10))
    pdef = b2d.particle_system_def(radius=0.1)
    psystem = world_8.create_particle_system(pdef)
    emitter_pos = (0, 0)
    emitter_def = b2d.RandomizedLinearEmitterDef()
    emitter_def.emite_rate = 400
    emitter_def.lifetime = 5.1
    emitter_def.size = (2, 1)
    emitter_def.velocity = (6, 20)
    emitter = b2d.RandomizedLinearEmitter(psystem, emitter_def)
    b2d.plot.animate_world(world_8, ppm=20, t=10, bounding_box=((-10, -20), (20, 5)), pre_step=emitter.step)
    return


if __name__ == "__main__":
    app.run()

