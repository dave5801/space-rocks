from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource, BoxZoomTool, HoverTool
from space_rocks.models.spacemodel import Distance
from bokeh.models.widgets import Panel, Tabs
import random


def gather_data(asteroids):
    lunar_list = []
    for neo in asteroids:
        lunar_list.append(neo.lunar)
    create_chart_data(lunar_list)


def create_chart_data(asteroid_list):
    x_numbers = []
    y_numbers = []
    N = len(asteroid_list)
    num = N//2
    for neo in asteroid_list[:num]:
        a = random.uniform(0.1, neo)
        x_numbers.append(neo - a)
        y_numbers.append(a)
    for neo in asteroid_list[num:]:
        a = random.uniform(0.1, neo)
        b = neo - a
        x_numbers.append(-b)
        y_numbers.append(a)
    x = x_numbers
    y = y_numbers
    chart_data = [N, x, y]
    create_chart(chart_data)


def create_chart(chart_data):
    N = chart_data[0]
    x = chart_data[1]
    y = chart_data[2]

    output_file('space_rocks/static/distance.html')

    p1 = figure(
        tools=" ",
        x_range=(-14.5, 14.5),
        y_range=(-0.5, 14.4),
        plot_width=1200,
        plot_height=800,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p1.xaxis.axis_label = "Lunar Distance"
    p1.xgrid.grid_line_color = "#240090"
    p1.yaxis.axis_label = "Lunar Distance"
    p1.ygrid.grid_line_color = "#240090"

    p1.circle(
        x=0,
        y=0,
        radius=0.01,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p1.circle(
        x,
        y,
        radius=0.08,
        fill_color='#FFFFFF',
        fill_alpha=0.6,
        line_color=None)
    tab1 = Panel(child=p1, title="circle")

    p2 = figure(
        tools=" ",
        x_range=(-5.5, 5.5),
        y_range=(-0.5, 5.4),
        plot_width=1200,
        plot_height=800,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p2.xaxis.axis_label = "Lunar Distance"
    p2.xgrid.grid_line_color = "#240090"
    p2.yaxis.axis_label = "Lunar Distance"
    p2.ygrid.grid_line_color = "#240090"

    p2.circle(
        x=0,
        y=0,
        radius=0.01,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p2.circle(
        x,
        y,
        radius=0.06,
        fill_color='#FFFFFF',
        fill_alpha=0.7,
        line_color=None)
    tab2 = Panel(child=p2, title="other")

    p3 = figure(
        tools=" ",
        x_range=(-2.5, 2.5),
        y_range=(-0.5, 2.4),
        plot_width=1200,
        plot_height=800,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p3.xaxis.axis_label = "Lunar Distance"
    p3.xgrid.grid_line_color = "#240090"
    p3.yaxis.axis_label = "Lunar Distance"
    p3.ygrid.grid_line_color = "#240090"

    p3.circle(
        x=0,
        y=0,
        radius=0.01,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p3.circle(
        x,
        y,
        radius=0.03,
        fill_color='#FFFFFF',
        fill_alpha=0.6,
        line_color=None)
    tab3 = Panel(child=p3, title="circle")

    tabs = Tabs(tabs=[tab1, tab2, tab3])

    save(tabs)