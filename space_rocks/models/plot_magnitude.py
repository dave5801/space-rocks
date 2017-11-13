"""Class for Scatter Plot -to be integrated with API calls"""


from bokeh.plotting import figure, output_file, show

# placeholder for API Data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file in template directory
output_file("../templates/graphs/abs_magnitude.html")

# create a new plot with a title and axis labels
p = figure(title="Brightness and Velocity", x_axis_label='Absolute Magnitude', y_axis_label='Velocity')


#render points
p.circle(x, y, legend="Near Earth Objects.", line_width=2)

# show the results
show(p)