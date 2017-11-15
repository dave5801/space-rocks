from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource, BoxZoomTool, HoverTool
from space_rocks.models.spacemodel import Distance
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
        # b = neo - a
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
    TOOLS = "hover,box_select,box_zoom,pan"

    p = figure(
        tools=TOOLS,
        x_range=(-14.5, 14.5),
        y_range=(-0.5, 14.4),
        plot_width=1200,
        plot_height=800,
        background_fill_color="black",
        border_fill_color="black",
        outline_line_color="black",
        )

    p.xaxis.axis_label = "Lunar Distance"
    p.xgrid.grid_line_color = "#240090"
    p.yaxis.axis_label = "Lunar Distance"
    p.ygrid.grid_line_color = "#240090"

    zoom_overlay = p.select_one(BoxZoomTool).overlay

    zoom_overlay.line_color = "#3500d3"
    zoom_overlay.line_width = 8
    zoom_overlay.line_dash = "solid"
    zoom_overlay.fill_color = None

    source = ColumnDataSource(data=dict(
        x=chart_data[1],
        y=chart_data[2],
    ))
    hover = p.select_one(HoverTool)
    hover.tooltips = [
        ("index", "butthole"),
        ("(x,y)", "($x, $y)"),
        ("x", "@x"),
        ("fill color", "$color[hex, swatch]:fill_color")
    ]

    p.circle(
        x=0,
        y=0,
        radius=0.01,
        fill_color='red',
        fill_alpha=0.6,
        line_color=None)
    p.circle(
        x,
        y,
        radius=0.05,
        fill_color='#FFFFFF',
        fill_alpha=0.6,
        line_color=None)
    save(p)
