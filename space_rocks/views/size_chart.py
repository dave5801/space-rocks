"""Function to make a chart for the size of the asteroids.

The size is compared to the number of elephants.
"""
import os
from bokeh.plotting import figure, save, output_file
from bokeh.palettes import YlGnBu3
from bokeh.models import HoverTool, ColumnarDataSource
from random import randint

HERE = os.path.abspath(__file__)
PLOT = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'static/size.html')


def size_chart(asteroid_list):
    """Create scatter plot for asteroid sizes."""
    y_axis_2016 = []
    y_axis_2017 = []
    y_axis_2018 = []
    size_2016 = []
    size_2017 = []
    size_2018 = []
    name_2016 = []
    name_2017 = []
    name_2018 = []
    for item in asteroid_list:
        if '2016' in item.date:
            y_axis_2016.append(float('{0:.4f}'.format(item.feet)))
            size_2016.append(float('{0:.2f}'.format(item.feet / 13)))
            name_2016.append(item.name)
        if '2017' in item.date:
            y_axis_2017.append(float('{0:.4f}'.format(item.feet)))
            size_2017.append(float('{0:.2f}'.format(item.feet / 13)))
            name_2017.append(item.name)
        if '2018' in item.date:
            y_axis_2018.append(float('{0:.4f}'.format(item.feet)))
            size_2018.append(float('{0:.2f}'.format(item.feet / 13)))
            name_2018.append(item.name)
    x_axis = [randint(1, 356) for _ in range(len(asteroid_list))]

    hover = HoverTool(tooltips="""
        <div>
            <div>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: lighter;">Name of NEO: </span>
                <span style="font-size: 17px; font-weight: bold;">$name</span>
            </div>
        </div>
        """)

    p = figure(
        title='Asteroid Size Compared to Elephants',
        tools=['pan', 'wheel_zoom', hover],
        plot_width=1130,
        plot_height=800,
        background_fill_color='black',
        background_fill_alpha=0.9,
        border_fill_color='black',
        border_fill_alpha=0.9,
        y_range=(0, 300)
    )

    for item, size, name, color in zip([y_axis_2018, y_axis_2017, y_axis_2016],
                                       [size_2018, size_2017, size_2016], ['2018', '2017', '2016'], YlGnBu3):
        p.scatter(
            x=x_axis,
            y=item,
            size=size,
            color=color,
            name='Ugh',
            legend=name
        )

    p.yaxis.axis_label = "Number of Elephants"
    p.yaxis.major_label_text_font_style = "bold"
    p.yaxis.major_label_orientation = "vertical"
    p.ygrid.grid_line_color = None

    p.xaxis.visible = False
    p.xgrid.grid_line_color = None

    p.legend.location = "top_left"
    p.legend.click_policy = "hide"
    p.legend.background_fill_color = "black"
    p.legend.background_fill_alpha = 0.9

    p.toolbar_location = None
    p.toolbar.logo = None

    output_file(PLOT)
    save(p)
