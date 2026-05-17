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
    # `folium` Interactive Map Demo

    Simple demonstration of rendering a map in a `jupyterlite` notebook.

    Note that the `folium` package has several dependencies which themselves may have dependencies.

    The following code fragement, run in a fresh Python enviroment into which `folium` has already been installed, identifies the packages that are loaded in when `folium` is loaded:

    ```python
    #https://stackoverflow.com/a/40381601/454773
    import sys
    before = [str(m) for m in sys.modules]
    import folium
    after = [str(m) for m in sys.modules]
    set([m.split('.')[0] for m in after if not m in before and not m.startswith('_')])
    ```

    The loaded packages are:

    ```
    {'branca',
     'certifi',
     'chardet',
     'cmath',
     'csv',
     'dateutil',
     'encodings',
     'folium',
     'gzip',
     'http',
     'idna',
     'importlib',
     'jinja2',
     'markupsafe',
     'mmap',
     'numpy',
     'pandas',
     'pkg_resources',
     'pytz',
     'requests',
     'secrets',
     'stringprep',
     'urllib3',
     'zipfile'}
     ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The following packages seem to need installing in order load `folium`, along with folium itself:

    ```
    chardet, certifi, idna, branca, urllib3, Jinja2, requests, Markupsafe
    ```

    Universal wheels, with filenames of the form `PACKAGE-VERSION-py2.py3-none-any.whl` appearing in the *Download files* area of a PyPi package page ([example](https://pypi.org/project/requests/#files)] are required in order to install the package.

    One required package, [`Markupsafe`](https://pypi.org/project/Markupsafe/#files)) *did not* have a universal wheel available, so a wheel was manually built elsewhere (by hacking the [`setup.py` file](https://github.com/pallets/markupsafe/blob/main/setup.py) to force it to build the wheel in a platform and speedup free way) and pushed to a downloadable location in an [*ad hoc* wheelhouse](https://opencomputinglab.github.io/vce-wheelhouse/).
    """)
    return


@app.cell
def _():
    # Install folium requirements
    # '%pip install -q folium' command supported automatically in marimo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Demo of `folium` Map

    Load in the `folium` package:
    """)
    return


@app.cell
def _():
    import folium

    return (folium,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And render a demo map:
    """)
    return


@app.cell
def _(folium):
    m = folium.Map(location=[50.693848, -1.304734], zoom_start=11)
    m
    return


if __name__ == "__main__":
    app.run()

