"""Class for Scatter Plot -to be integrated with API calls."""

from bokeh.models import ColumnDataSource, OpenURL, TapTool
from bokeh.plotting import figure, output_file, show
import os
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException

def graph_abs_magnitude(abs_mag=None, velocity=None):
    """Create Bokeh Scatter Plot."""

    if len(abs_mag) != len(velocity):
        raise UnknownAxisException

    if abs_mag == None and velocity == None:
        abs_mag = []
        velocity = []

    here = os.path.abspath(__file__)
    graph_file_path = os.path.join(os.path.dirname(os.path.dirname(here)), "static/abs_magnitude.html")
    #import pdb;
    #pdb.set_trace()

    #output_file("static/abs_magnitude.html")
    output_file(graph_file_path)


    p = figure(
        title="Brightness and Velocity", tools="tap",
        x_axis_label='Absolute Magnitude', y_axis_label='Velocity km/s'
    )

    source = ColumnDataSource(data=dict(
        x=abs_mag,
        y=velocity,
        color=["navy" for i in range(len(abs_mag))]))

    p.circle('x', 'y', color='color', size=20, source=source)

    url = "static/details_neo1.html"
    #url = "http://www.colors.commutercreative.com/@color/" <---- save this for now, it is an example for later
    taptool = p.select(type=TapTool)
    taptool.callback = OpenURL(url=url)

    show(p)


if __name__ == '__main__':

    abs = [1, 2, 3, 4, 5]
    vel = [2, 5, 8, 2, 7]

    graph_abs_magnitude(abs, vel)

'''
test if abs_magnitude.html exists if data good
test if abs_magnitude.html exists if data NONE
abs, and vel NOT same length
abs, and vel SAME length
'''