from bokeh.plotting import figure, output_file, show
from space_rocks.models.spacemodel import Distance


def get_data(asteroids):
    astronomical_list = []
    lunar_list = []
    kilometers_list = []
    miles_list = []
    for neo in asteroids:
        astronomical_list.append(neo.astornomical)
        lunar_list.append(neo.lunar)
        kilometers_list.append(neo.kilometers)
        miles_list.append(neo.miles)
    else:
        raise HTTPNotFound
    return lunar_list


def create_chart(asteroid_list):
    output_file('space_rocks/templates/graphs/distance.html', mode="cdn")
    N = len(list)
    x = 10
    y = lunar_list
    radii = size
    colors = colors
    TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
    p = figure(tools=TOOLS, x_range=(0, 20), y_range=(1, 200))
    p.circle(x, y, radius=1, fill_color='#000000', fill_alpha=0.6, line_color=None)
    show(p)
