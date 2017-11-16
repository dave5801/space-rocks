from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource, BoxZoomTool, HoverTool
from space_rocks.models.spacemodel import Distance
from bokeh.models.widgets import Panel, Tabs
import random


def gather_data(asteroids):
    """Take all asteroids a break down into lists for chart."""
    lunar_list = []
    neo_id_list = []
    name_list = []
    for neo in asteroids:
        lunar_list.append(neo.lunar)
        neo_id_list.append(neo.neo_id)
        name_list.append(neo.name)
    create_chart_data(lunar_list)
    return [lunar_list, neo_id_list, name_list]


def create_chart_data(asteroid_list):
    """Create x and y axes based of lunar distance."""
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
    create_chart(N, x_numbers, y_numbers)
    return [N, x_numbers, y_numbers]


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
            'x_min': -5.5,
            'x_max': 5.5,
            'y_min': -0.5,
            'y_max': 5.5,
            'earth_rad': 0.11,
            'moon_rad': 0.11,
            'neo_rad': 0.06,
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


def create_chart(number, x_axes, y_axes):
    dictionaries = create_dictionaries()
    data = gather_data()
    distance = data[0]
    neo_id = data[1]
    names = data[2]

    for d in dictionaries:
        d['p'] = figure(
            tools=" ",
            x_range=(d['x_min'], d['x_max']),
            y_range=(d['y_min'], d['y_max']),
            plot_width=1200,
            plot_height=780,
            background_fill_color="black",
            border_fill_color="black",
            outline_line_color="black",
            toolbar_location=None,
            )

        # d['p'].xaxis.axis_label = "Lunar Distance"
        # d['p'].xgrid.grid_line_color = None
        # d['p'].yaxis.axis_label = "Lunar Distance"
        # d['p'].ygrid.grid_line_color = None
        # d['p'].legend.background_fill_color = "black"
        # d['p'].legend.label_text_color = "white"
        d['p'].circle(
            x=0,
            y=0,
            legend='Earth',
            radius=d['earth_rad'],
            fill_color='red',
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
            x_axes,
            y_axes,
            radius=d['neo_rad'],
            legend='Asteroids',
            fill_color='#FFFFFF',
            fill_alpha=0.6,
            line_color=None)
        d['tab'] = Panel(
            child=d['p'],
            title="NEOs <= {} Lunar Distance".format(d['x_max']))
        display.append(d['tab'])

    output_file('space_rocks/static/distance.html')
    display = []
    tabs = Tabs(tabs=display)

    save(tabs)


# def create_chart(number, x_axes, y_axes):
#     dictionaries = create_dictionaries()
#     data = gather_data()
#     distance = data[0]
#     neo_id = data[1]
#     names = data[2]

#     for d in dictionaries:
#         d['p'] = figure(
#             tools=" ",
#             x_range=(-14.5, 14.5),
#             y_range=(-0.5, 14.5),
#             plot_width=1200,
#             plot_height=780,
#             background_fill_color="black",
#             border_fill_color="black",
#             outline_line_color="black",
#             toolbar_location=None,
#             )

#         d['p'].xaxis.axis_label = "Lunar Distance"
#         d['p'].xgrid.grid_line_color = None
#         d['p'].yaxis.axis_label = "Lunar Distance"
#         d['p'].ygrid.grid_line_color = None
#         d['p'].legend.background_fill_color = "black"
#         d['p'].legend.label_text_color = "white"
#         d['p'].circle(
#             x=0,
#             y=0,
#             legend='Earth',
#             radius=0.145,
#             fill_color='red',
#             fill_alpha=0.6,
#             line_color=None)
#         d['p'].circle(
#             x=0,
#             y=1,
#             legend='Moop',
#             radius=0.145,
#             fill_color='blue',
#             fill_alpha=0.6,
#             line_color=None)
#         d['p'].circle(
#             x,
#             y,
#             radius=0.08,
#             legend='Not Earth',
#             fill_color='#FFFFFF',
#             fill_alpha=0.6,
#             line_color=None)
#         d['tab'] = Panel(child=d['p'], title="NEOs <= 14.5 Lunar Distance")
#         display.append(d['tab'])

#     output_file('space_rocks/static/distance.html')
#     display = []
#     tabs = Tabs(tabs=display)

#     save(tabs)
