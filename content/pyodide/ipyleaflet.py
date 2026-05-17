import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    # '%pip install -q bqplot ipyleaflet' command supported automatically in marimo
    return


@app.cell
def _():
    import os
    from urllib.request import urlopen
    import json
    from datetime import datetime

    import numpy as np
    import pandas as pd

    from js import fetch

    from ipywidgets import Dropdown

    from bqplot import Lines, Figure, LinearScale, DateScale, Axis

    from ipyleaflet import Map, GeoJSON, WidgetControl

    return (
        Axis,
        DateScale,
        Dropdown,
        Figure,
        GeoJSON,
        LinearScale,
        Lines,
        Map,
        WidgetControl,
        datetime,
        fetch,
        json,
        np,
        pd,
    )


@app.cell
async def _(fetch, pd):
    _URL = 'https://raw.githubusercontent.com/jupyter-widgets/ipyleaflet/master/examples/nations.json'
    _res = await fetch(_URL)
    _text = await _res.text()
    data = pd.read_json(_text)
    return (data,)


@app.cell
def _(np):
    def clean_data(data):
        for column in ['income', 'lifeExpectancy', 'population']:
            data = data.drop(data[data[column].apply(len) <= 4].index)
        return data

    def extrap_interp(data):
        data = np.array(data)
        x_range = np.arange(1800, 2009, 1.)
        y_range = np.interp(x_range, data[:, 0], data[:, 1])
        return y_range

    def extrap_data(data):
        for column in ['income', 'lifeExpectancy', 'population']:
            data[column] = data[column].apply(extrap_interp)
        return data

    return clean_data, extrap_data


@app.cell
def _(clean_data, data, extrap_data):
    data_1 = clean_data(data)
    data_1 = extrap_data(data_1)
    return (data_1,)


@app.cell
def _(data_1):
    data_1
    return


@app.cell
def _(DateScale, datetime):
    date_start = datetime(1800, 12, 31)
    date_end = datetime(2009, 12, 31)

    date_scale = DateScale(min=date_start, max=date_end)
    return date_end, date_scale, date_start


@app.cell
def _(date_end, date_start, pd):
    date_data = pd.date_range(start=date_start, end=date_end, freq='A', normalize=True)
    return (date_data,)


@app.cell
def _(data_1):
    country_name = 'Angola'
    data_name = 'income'
    x_data = data_1[data_1.name == country_name][data_name].values[0]
    return country_name, data_name, x_data


@app.cell
def _(
    Axis,
    Figure,
    LinearScale,
    Lines,
    country_name,
    data_name,
    date_data,
    date_scale,
    x_data,
):
    x_scale = LinearScale()

    lines = Lines(x=date_data, y=x_data, scales={'x': date_scale, 'y': x_scale})

    ax_x = Axis(label='Year', scale=date_scale, num_ticks=10, tick_format='%Y')
    ax_y = Axis(label=data_name.capitalize(), scale=x_scale, orientation='vertical', side='left')

    figure = Figure(axes=[ax_x, ax_y], title=country_name, marks=[lines], animation_duration=500,
                    layout={'max_height': '250px', 'max_width': '400px'})
    return ax_y, figure, lines


@app.cell
def _(ax_y, data_1, figure, lines):
    def update_figure(country_name, data_name):
        try:
            lines.y = data_1[data_1.name == country_name][data_name].values[0]
            ax_y.label = data_name.capitalize()
            figure.title = country_name
        except IndexError:
            pass

    return (update_figure,)


@app.cell
async def _(fetch, json):
    _URL = 'https://raw.githubusercontent.com/jupyter-widgets/ipyleaflet/master/examples/countries.geo.json'
    _res = await fetch(_URL)
    _text = await _res.text()
    countries = json.loads(_text)
    return (countries,)


@app.cell
def _(GeoJSON, Map, countries):
    m = Map(zoom=3)

    geo = GeoJSON(data=countries, style={'fillColor': 'white', 'weight': 0.5}, hover_style={'fillColor': '#1f77b4'}, name='Countries')
    m.add_layer(geo)
    return geo, m


@app.cell
def _(WidgetControl, country_name, data_name, figure, geo, m, update_figure):
    widget_control1 = WidgetControl(widget=figure, position='bottomright')
    m.add_control(widget_control1)

    def on_hover(event, feature, **kwargs):
        global country_name
        country_name_1 = feature['properties']['name']
        update_figure(country_name_1, data_name)
    geo.on_hover(on_hover)
    return


@app.cell
def _(Dropdown, WidgetControl, country_name_1, data_name, m, update_figure):
    dropdown = Dropdown(options=['income', 'population', 'lifeExpectancy'], value=data_name, description='Plotting:')

    def on_click(change):
        global data_name
        data_name_1 = change['new']
        update_figure(country_name_1, data_name_1)
    dropdown.observe(on_click, 'value')
    widget_control2 = WidgetControl(widget=dropdown, position='bottomleft')
    m.add_control(widget_control2)
    return


@app.cell
def _(m):
    m
    return


if __name__ == "__main__":
    app.run()

