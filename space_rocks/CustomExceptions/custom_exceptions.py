"""This is a class for creating exceptions."""
"""It accounts for missing astronomical data."""


class UnknownAxisException(Exception):
    """This class catches an exception for absolute magnitude graph."""

    def __init__(self):
        """Velocity and absolute magnitude axes do not equal."""
        Exception.__init__(self, "Unknown astronomical data")

if __name__ == '__main__':
    x_axis = [1, 2, 3, 4, 5]
    y_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if len(x_axis) != len(y_axis):
        raise UnknownAxisException