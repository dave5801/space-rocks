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
            'earth_dif': '1350%',
            'moon_dif': '3122%',
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
            'earth_dif': '1000%',
            'moon_dif': '2344%',
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
            'earth_dif': '400%',
            'moon_dif': '1011%',
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
            'earth_dif': '200%',
            'moon_dif': '566%',
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
            'earth_dif': 'to scale',
            'moon_dif': 'not shown',
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
            plot_width=1400,
            plot_height=740,
            background_fill_color="black",
            background_fill_alpha=0.4,
            border_fill_color="black",
            border_fill_alpha=0.4,
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
            legend='Earth (size increase: {})'.format(d['earth_dif']),
            radius=d['earth_rad'],
            fill_color='green',
            fill_alpha=0.6,
            line_color=None)
        d['p'].circle(
            x=0,
            y=1,
            legend='Moon (size increase: {})'.format(d['moon_dif']),
            radius=d['moon_rad'],
            fill_color='blue',
            fill_alpha=0.6,
            line_color=None)
        d['p'].circle(
            neo_dict['x_numbers'],
            neo_dict['y_numbers'],
            radius=d['neo_rad'],
            fill_color='#FFFFFF',
            fill_alpha=0.6,
            line_color=None)
        d['tab'] = Panel(
            child=d['p'],
            title="NEOs <= {}LD".format(d['x_max']))
        display.append(d['tab'])

    output_file(graph_path)

    tabs = Tabs(tabs=display)

    save(tabs)
