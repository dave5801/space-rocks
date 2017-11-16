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
        y_range=(-0.5, 14.5),
        plot_width=1200,
        plot_height=780,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p1.xaxis.axis_label = "Lunar Distance"
    p1.xgrid.grid_line_color = None
    p1.yaxis.axis_label = "Lunar Distance"
    p1.ygrid.grid_line_color = None
    p1.legend.background_fill_color = "black"
    p1.legend.label_text_color = "white"
    p1.circle(
        x=0,
        y=0,
        legend='Earth',
        radius=0.145,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p1.circle(
        x=0,
        y=1,
        legend='Moop',
        radius=0.145,
        fill_color='blue',
        fill_alpha=0.6,
        line_color=None)
    p1.circle(
        x,
        y,
        radius=0.08,
        legend='Not Earth',
        fill_color='#FFFFFF',
        fill_alpha=0.6,
        line_color=None)
    tab1 = Panel(child=p1, title="NEOs <= 14.5 Lunar Distance")

    p2 = figure(
        tools=" ",
        x_range=(-5.5, 5.5),
        y_range=(-0.5, 5.5),
        plot_width=1200,
        plot_height=780,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p2.xaxis.axis_label = "Lunar Distance"
    p2.xgrid.grid_line_color = None
    p2.yaxis.axis_label = "Lunar Distance"
    p2.ygrid.grid_line_color = None

    p2.circle(
        x=0,
        y=0,
        radius=0.11,
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
    tab2 = Panel(child=p2, title="NEOs <= 5.5 Lunar Distance")

    p3 = figure(
        tools=" ",
        x_range=(-2.5, 2.5),
        y_range=(-0.2, 2.5),
        plot_width=1200,
        plot_height=800,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p3.xaxis.axis_label = "Lunar Distance"
    p3.xgrid.grid_line_color = None
    p3.yaxis.axis_label = "Lunar Distance"
    p3.ygrid.grid_line_color = None

    p3.circle(
        x=0,
        y=0,
        radius=0.05,
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
    tab3 = Panel(child=p3, title="NEOs <= 2.5 Lunar Distance")

    p4 = figure(
        tools=" ",
        x_range=(-1.5, 1.5),
        y_range=(-0.1, 1.5),
        plot_width=1200,
        plot_height=780,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p4.xaxis.axis_label = "Lunar Distance"
    p4.xgrid.grid_line_color = None
    p4.yaxis.axis_label = "Lunar Distance"
    p4.ygrid.grid_line_color = None

    p4.circle(
        x=0,
        y=0,
        radius=0.03,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p4.circle(
        x,
        y,
        radius=0.03,
        fill_color='#FFFFFF',
        fill_alpha=0.6,
        line_color=None)
    tab4 = Panel(child=p4, title="NEOs <= 1.5 Lunar Distance")

    p5 = figure(
        tools=" ",
        x_range=(-0.5, 0.5),
        y_range=(-0.1, 0.5),
        plot_width=1200,
        plot_height=780,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        toolbar_location=None,
        )

    p5.xaxis.axis_label = "Lunar Distance"
    p5.xgrid.grid_line_color = None
    p5.yaxis.axis_label = "Lunar Distance"
    p5.ygrid.grid_line_color = None

    p5.circle(
        x=0,
        y=0,
        radius=0.01,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p5.circle(
        x,
        y,
        radius=0.01,
        fill_color='#FFFFFF',
        fill_alpha=0.6,
        line_color=None)
    tab5 = Panel(child=p5, title="NEOs <= 0.5 Lunar Distance")

    tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5])

    save(tabs)
