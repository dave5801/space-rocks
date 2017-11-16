"""Function to make a chart for the size of the asteroids.

The size is compared to the number of elephants.
"""
import os
from bokeh.plotting import(
    figure,
    output_file,
)
from bokeh.embed import components
from random import randint
HERE = os.path.abspath(__file__)
BAR = os.path.join(os.path.dirname(os.path.dirname(HERE)), "static/bar_shit.html")


def size_chart(asteroid_list):
    """."""
    x_axis = [float('{0:.4f}'.format(item.feet)) for item in asteroid_list]
    y_axis = [randint(1, 300) for item in range(len(x_axis))]
    dot_size = [float('{0:.2f}'.format(item / 13)) for item in x_axis]
    output_file(BAR)
    p = figure(
        title='Asteroid Size Compared to Elephants',
        tools=['pan', 'wheel_zoom'],
        plot_width=1000,
        plot_height=1000,
        background_fill_color='black',
        border_fill_color='black',
        y_range=(0, 300)
    )

    p.scatter(
        x=y_axis,
        y=x_axis,
        size=dot_size,
        color='green'
    )

    p.yaxis.axis_label = "Number of Elephants"
    p.yaxis.major_label_orientation = "vertical"
    p.xaxis.visible = False
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    script, div = components(p)

    return script, div
