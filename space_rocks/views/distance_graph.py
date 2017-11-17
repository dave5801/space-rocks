from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource, BoxZoomTool, HoverTool
from space_rocks.models.spacemodel import Distance
from bokeh.models.widgets import Panel, Tabs
import random
import os

HERE = os.path.abspath(__file__)
graph_path = os.path.join(
    os.path.dirname(os.path.dirname(HERE)),
    "static/graphs/distance.html")


def gather_data(asteroids):
    """Take all asteroids an create dictionary for chart."""
    neo_dict = {
        'lunar_list': [],
        'neo_id_list': [],
        'name_list': [],
        'x_numbers': [],
        'y_numbers': [],
    }

    for neo in asteroids:
        neo_dict['lunar_list'].append(neo.lunar)
        neo_dict['neo_id_list'].append(neo.neo_id)
        neo_dict['name_list'].append(neo.name)

    num = len(neo_dict['lunar_list'])//2

    for neo in neo_dict['lunar_list'][:num]:
        a = random.uniform(0.1, neo)
        neo_dict['x_numbers'].append(neo - a)
        neo_dict['y_numbers'].append(a)

    for neo in neo_dict['lunar_list'][num:]:
        a = random.uniform(0.1, neo)
        b = neo - a
<<<<<<< HEAD
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

    here = os.path.abspath(__file__)
    graph_file_path = os.path.join(os.path.dirname(os.path.dirname(here)),"static/distance.html")

    output_file(graph_file_path)

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
    p1.xgrid.grid_line_color = "#240090"
    p1.yaxis.axis_label = "Lunar Distance"
    p1.ygrid.grid_line_color = "#240090"

    p1.circle(
        x=0,
        y=0,
        legend='yes',
        radius=0.145,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p1.circle(
        x,
        y,
        radius=0.08,
        legend='no',
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
    p2.xgrid.grid_line_color = "#240090"
    p2.yaxis.axis_label = "Lunar Distance"
    p2.ygrid.grid_line_color = "#240090"

    p2.circle(
        x=0,
        y=0,
        radius=0.09,
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
    p3.xgrid.grid_line_color = "#240090"
    p3.yaxis.axis_label = "Lunar Distance"
    p3.ygrid.grid_line_color = "#240090"

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
    p4.xgrid.grid_line_color = "#240090"
    p4.yaxis.axis_label = "Lunar Distance"
    p4.ygrid.grid_line_color = "#240090"

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
    p5.xgrid.grid_line_color = "#240090"
    p5.yaxis.axis_label = "Lunar Distance"
    p5.ygrid.grid_line_color = "#240090"

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
=======
        neo_dict['x_numbers'].append(-b)
        neo_dict['y_numbers'].append(a)

    create_chart(neo_dict)


def create_dictionaries():
    """Create dictionaries to be used to make each chart."""
    d1 = {
            'p': 'p1',
            'tab': 'tab1',
            'x_min': -14.5,
            'x_max': 14.5,
            'y_min': -0.5,
            'y_max': 14.5,
            'earth_rad': 0.145,
            'moon_rad': 0.145,
            'neo_rad': 0.08,
        }
    d2 = {
            'p': 'p2',
            'tab': 'tab2',
            'x_min': -5.5,
            'x_max': 5.5,
            'y_min': -0.5,
            'y_max': 5.5,
            'earth_rad': 0.11,
            'moon_rad': 0.11,
            'neo_rad': 0.06,
        }
    d3 = {
            'p': 'p3',
            'tab': 'tab3',
            'x_min': -2.5,
            'x_max': 2.5,
            'y_min': -0.2,
            'y_max': 2.5,
            'earth_rad': 0.05,
            'moon_rad': 0.05,
            'neo_rad': 0.03,
        }
    d4 = {
            'p': 'p4',
            'tab': 'tab4',
            'x_min': -1.5,
            'x_max': 1.5,
            'y_min': -0.1,
            'y_max': 1.5,
            'earth_rad': 0.03,
            'moon_rad': 0.03,
            'neo_rad': 0.03,
        }
    d5 = {
            'p': 'p5',
            'tab': 'tab5',
            'x_min': -0.5,
            'x_max': 0.5,
            'y_min': -0.1,
            'y_max': 0.5,
            'earth_rad': 0.01,
            'moon_rad': 0.01,
            'neo_rad': 0.01,
        }
    return [d1, d2, d3, d4, d5]


def create_chart(neo_dict):
    """Create the chart."""
    dictionaries = create_dictionaries()
    distance = neo_dict['lunar_list']
    neo_id = neo_dict['neo_id_list']
    names = neo_dict['name_list']
    display = []

    for d in dictionaries:
        d['p'] = figure(
            tools=" ",
            x_range=(d['x_min'], d['x_max']),
            y_range=(d['y_min'], d['y_max']),
            plot_width=1100,
            plot_height=740,
            background_fill_color="black",
            border_fill_color="black",
            outline_line_color="black",
            toolbar_location=None,
            )

        d['p'].xgrid.grid_line_color = None
        d['p'].yaxis.axis_label = "Lunar Distance"
        d['p'].ygrid.grid_line_color = None
        d['p'].xaxis.visible = False

        d['p'].circle(
            x=0,
            y=0,
            legend='Earth',
            radius=d['earth_rad'],
            fill_color='green',
            fill_alpha=0.6,
            line_color=None)
        d['p'].circle(
            x=0,
            y=1,
            legend='Moon',
            radius=d['moon_rad'],
            fill_color='blue',
            fill_alpha=0.6,
            line_color=None)
        d['p'].circle(
            neo_dict['x_numbers'],
            neo_dict['y_numbers'],
            radius=d['neo_rad'],
            legend='Asteroids',
            fill_color='#FFFFFF',
            fill_alpha=0.6,
            line_color=None)
        d['tab'] = Panel(
            child=d['p'],
            title="NEOs <= {}LD".format(d['x_max']))
        display.append(d['tab'])

    output_file(graph_path)

    tabs = Tabs(tabs=display)
>>>>>>> master

    save(tabs)
