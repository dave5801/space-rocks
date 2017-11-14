"""Class for Scatter Plot -to be integrated with API calls"""


from bokeh.models import ColumnDataSource, OpenURL, TapTool
from bokeh.plotting import figure, output_file

output_file("abs_magnitude.html")

p = figure(title="Brightness and Velocity", tools="tap", x_axis_label='Absolute Magnitude', y_axis_label='Velocity')


source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    color=["navy", "orange", "olive", "firebrick", "gold"]
    ))

p.circle('x', 'y', color='color', size=20, source=source)

url = "../templates/details_neo1.html"
#url = "http://www.colors.commutercreative.com/@color/"
taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)

