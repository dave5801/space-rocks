"""Function to create a bokeh scatter plot.

    It takes in the absolute magnitude, relative velocity and N.E.O's name and returns
    a scatter plot charting them.
"""

import os
from bokeh.plotting import figure, output_file, save, ColumnDataSource
from bokeh.models import HoverTool
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException


def graph_abs_magnitude(abs_mag=None, velocity=None, neo_names=None):
    """Create bokeh scatter plot."""

    """Redundancy checks."""
    if len(abs_mag) != len(velocity):
        raise UnknownAxisException

    if abs_mag is None and velocity is None:
        abs_mag = []
        velocity = []

    """Create absolute file path for embedded html graph."""
    here = os.path.abspath(__file__)
    graph_file_path = os.path.join(os.path.dirname(os.path.dirname(here)), "static/abs_magnitude.html")

    output_file(graph_file_path)

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

    hover = HoverTool(tooltips="""
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
        """)

    p = figure(plot_width=800, plot_height=800, tools=[hover],
               title="Brightness and Velocity",
               x_axis_label='Absolute Magnitude', y_axis_label='Velocity km/s')

    p.circle('x', 'y', size=10, source=source)

    save(p)

