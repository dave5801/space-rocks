import os
from bokeh.plotting import(
    figure,
    output_file,
    show
)
HERE = os.path.abspath(__file__)
BAR = os.path.join(os.path.dirname(os.path.dirname(HERE)), "static/bar_shit.html")


def test_chart(asteroid_list):
    """."""
    x_axis = [float('{0:.4f}'.format(item.feet)) for item in asteroid_list]
    y_axis = [float('{0:.4f}'.format(item.feet)) for item in asteroid_list]
    dot_size = [float('{0:.2f}'.format(item / 13)) for item in x_axis]
    output_file(BAR)
    p = figure(
        tools=['xwheel_pan', 'ywheel_pan', 'zoom_in', 'zoom_out'],
        plot_width=1800,
        plot_height=1800,
        background_fill_color='black'
    )

    p.scatter(
        x=x_axis,
        y=y_axis,
        size=dot_size,
        color='grey'
    )
    show(p)
