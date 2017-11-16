"""Class for Scatter Plot -to be integrated with API calls."""

import os
from bokeh.plotting import figure, output_file, save, ColumnDataSource
from bokeh.models import HoverTool
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException
from bokeh.embed import components


def graph_abs_magnitude(abs_mag=None, velocity=None, neo_names=None):
    """Create Bokeh Scatter Plot."""
    if len(abs_mag) != len(velocity):
        raise UnknownAxisException

    if abs_mag is None and velocity is None:
        abs_mag = []
        velocity = []

    here = os.path.abspath(__file__)
    graph_file_path = os.path.join(os.path.dirname(os.path.dirname(here)), "static/abs_magnitude.html")

    output_file(graph_file_path)

    p = figure(
        title="Brightness and Velocity", tools="tap",
        x_axis_label='Absolute Magnitude', y_axis_label='Velocity km/s'
    )

    source = ColumnDataSource(data=dict(
        x=abs_mag,
        y=velocity,
        names=neo_names,
        fonts=[
            '<i>italics</i>',
            '<pre>pre</pre>',
            '<b>bold</b>',
            '<small>small</small>',
            '<del>del</del>'
        ]
    ))

    hover = HoverTool( tooltips="""
        <div>
            <div>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: lighter;">Name of NEO: </span>
                <span style="font-size: 17px; font-weight: bold;">@names</span>
                <span style="font-size: 15px; color: #966;">[$index]</span>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: lighter;">Absolute Magnitude: </span>
                <span style="font-size: 17px; font-weight: bold;">@x</span>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: lighter;">Relative Velocity: </span>
                <span style="font-size: 17px; font-weight: bold;">@y</span>
            </div>
        </div>
        """
    )

    p = figure(plot_width=400, plot_height=400, tools=[hover],
               title="Brightness and Velocity", 
               x_axis_label='Absolute Magnitude', y_axis_label='Velocity km/s')

    p.circle('x', 'y', size=20, source=source)
    url = "static/details_neo1.html"
    taptool = p.select(type=TapTool)
    taptool.callback = OpenURL(url=url)

    save(p)
    # script, div = components(p)
    # with open(graph_file_path, 'w') as output:
    #     output.write(div)
    #     output.write(script)


if __name__ == '__main__':
    mag = [1, 2, 3, 4, 5]
    vel = [2, 5, 8, 2, 7]
    neo_names = ["ceres", "phobos", "deimos", "asteroid x", "it was earth all along!!"]

    graph_abs_magnitude(mag, vel, neo_names)
