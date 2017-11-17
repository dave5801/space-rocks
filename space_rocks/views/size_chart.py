"""Function to make a chart for the size of the asteroids.

The size is compared to the number of elephants.
"""
import os
from bokeh.plotting import figure, save, output_file
from bokeh.palettes import YlOrRd3
from random import randint

HERE = os.path.abspath(__file__)
PLOT = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'static/graphs/size.html')


def size_chart(asteroid_list):
    """Create scatter plot for asteroid sizes."""
    y_axis_2016 = []
    y_axis_2017 = []
    y_axis_2018 = []
    size_2016 = []
    size_2017 = []
    size_2018 = []
    for item in asteroid_list:
        if '2016' in item.date:
            y_axis_2016.append(float('{0:.4f}'.format(item.feet)))
            size_2016.append(float('{0:.2f}'.format(item.feet / 13)))
        if '2017' in item.date:
            y_axis_2017.append(float('{0:.4f}'.format(item.feet)))
            size_2017.append(float('{0:.2f}'.format(item.feet / 13)))
        if '2018' in item.date:
            y_axis_2018.append(float('{0:.4f}'.format(item.feet)))
            size_2018.append(float('{0:.2f}'.format(item.feet / 13)))
    x_axis = [randint(1, 356) for _ in range(len(asteroid_list))]

    p = figure(
        title='Asteroid Size Compared to Elephants',
        plot_width=900,
        plot_height=800,
        background_fill_color='black',
        background_fill_alpha=0.7,
        border_fill_color='black',
        border_fill_alpha=0.7,
        y_range=(0, 300),
        responsive=True
    )

    for item, size, name, color in zip([y_axis_2018, y_axis_2017, y_axis_2016], [size_2018, size_2017, size_2016],
                                       ['2018', '2017', '2016'], YlOrRd3):
        p.scatter(
            x=x_axis,
            y=item,
            size=size,
            color=color,
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
    p.legend.background_fill_alpha = 0.7

    p.toolbar_location = None
    p.toolbar.logo = None

    output_file(PLOT)
    save(p)
