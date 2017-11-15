from bokeh.plotting import figure, output_file, show
from space_rocks.models.spacemodel import Distance
import random


def gather_data(asteroids):
    astronomical_list = []
    lunar_list = []
    kilometers_list = []
    miles_list = []
    for neo in asteroids:
        if neo.astronomical < 0:
            neo.astronomical = -neo.astronomical
        astronomical_list.append(neo.astronomical)
        lunar_list.append(neo.lunar)
        kilometers_list.append(neo.kilometers)
        miles_list.append(neo.miles)
    create_chart_data(astronomical_list)


def create_chart_data(asteroid_list):
    x_numbers = []
    for i in range(len(asteroid_list)):
        x_numbers.append(random.randint(1, 19))
    N = len(asteroid_list)
    x = x_numbers
    y = asteroid_list
    chart_data = [N, x, y]
    create_chart(chart_data)


def create_chart(chart_data):
    output_file('space_rocks/templates/graphs/distance.html', mode="cdn")
    TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
    p = figure(
        tools=TOOLS,
        x_range=(0, 20),
        y_range=(-0.5, 0.5),
        plot_width=700,
        plot_height=1200
        )
    N = chart_data[0]
    x = chart_data[1]
    y = chart_data[2]
    p.circle(x, y, radius=0.5, fill_color='#000000', fill_alpha=0.6, line_color=None)
    show(p)
