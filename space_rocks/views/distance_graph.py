from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models import HoverTool
from space_rocks.models.spacemodel import Distance
import random


def gather_data(asteroids):
    kilo_list = []
    neo_name = []
    neo_id = []
    for neo in asteroids:
        kilo_list.append(neo.kilometers)
        neo_name.append(neo.name)
        neo_id.append(neo.neo_id)
    create_chart_data(kilo_list, neo_name, neo_id)


def create_chart_data(asteroid_list, name_list, id_list):
    x_numbers = []
    for i in range(len(asteroid_list)):
        x_numbers.append(random.uniform(0.1, 19.9))
    N = len(asteroid_list)
    x = x_numbers
    y = asteroid_list
    name = name_list
    neo_id = id_list
    chart_data = [N, x, y, name, neo_id]
    create_chart(chart_data)


def create_chart(chart_data):
    N = chart_data[0]
    x = chart_data[1]
    y = chart_data[2]
    name = chart_data[3],
    neo_id = chart_data[4]

    output_file('space_rocks/static/distance.html')
    TOOLS = "hover"

    p = figure(
        tools=TOOLS,
        x_range=(0, 20),
        y_range=(-10, 200),
        plot_width=1000,
        plot_height=2500,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        )
    # source = ColumnDataSource(data=dict(
    #         'x'=chart_data[1],
    #         'y'=chart_data[2],
    #         'N'=chart_data[0],
    #         'name'=chart_data[3],
    #         'neo_id'=chart_data[4]))

    p.circle(
        x=10,
        y=150,
        radius=1,
        fill_color='#FF0000',
        fill_alpha=0.6,
        line_color=None)

    p.circle(
        x,
        y,
        radius=0.1,
        fill_color='#FFFFFF',
        fill_alpha=0.6,
        line_color=None)
    show(p)
