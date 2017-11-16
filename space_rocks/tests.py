"""Testing our Views."""
from pyramid.testing import DummyRequest
import pytest
import os.path
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException


@pytest.fixture
def dummy_request():
    """Set up a dummy request for testing."""
    return DummyRequest()



def test_abs_magnitude_graph_no_arguments_returns_exception():
    """Test if absolute magnitude graph's raises exception, no args."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude
    with pytest.raises(UnknownAxisException):
        graph_abs_magnitude()


def test_abs_magnitude_graph_empty_arguments_returns_exception():
    """Test if absolute magnitude graph's raises exception, empty args."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude
    with pytest.raises(UnknownAxisException):
        graph_abs_magnitude([], [], [])


def test_abs_magnitude_graph_missing_magnitude_returns_exception():
    """Test if absolute magnitude graph's raises exception, missing mag arg."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    test_vel = [2, 5, 8, 2, 7]
    test_neo_names = ["ceres", "phobos", "deimos", "asteroid x", "it was earth all along!!"]

    with pytest.raises(UnknownAxisException):
        graph_abs_magnitude(test_vel, [], test_neo_names)


def test_abs_magnitude_graph_missing_velocity_returns_exception():
    """Test if absolute magnitude graph's raises exception, missing velocity arg."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    test_mag = [1, 2, 3, 4, 5]
    test_neo_names = ["ceres", "phobos", "deimos", "asteroid x", "it was earth all along!!"]

    with pytest.raises(UnknownAxisException):
        graph_abs_magnitude(test_mag, [],test_neo_names)


def test_abs_magnitude_graph_missing_neo_names_returns_exception():
    """Test if absolute magnitude graph's raises exception, missing neo names arg."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude
    test_mag = [1, 2, 3, 4, 5]
    test_vel = [2, 5, 8, 2, 7]
    with pytest.raises(UnknownAxisException):
        graph_abs_magnitude(test_mag, test_vel,[])

'''
def test_abs_magnitude_graph_exists_no_arguments():
    """Test if absolute magnitude scatter plot is generated with no arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude
    graph_abs_magnitude()
    assert os.path.isfile("static/abs_magnitude.html") 


def test_abs_magnitude_graph_exists_no_arguments():
    """Test if absolute magnitude scatter plot is generated with empty arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude
    graph_abs_magnitude([],[])
    assert os.path.isfile("static/abs_magnitude.html")


def test_abs_magnitude_graph_exists_simple_arguments():
    """Test if absolute magnitude scatter plot is generated with same length arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    test_abs_mag = [1, 2, 3, 4, 5]
    test_velocity = [2, 5, 8, 2, 7]

    graph_abs_magnitude(test_abs_mag, test_velocity)
    assert os.path.isfile("static/abs_magnitude.html")


def test_abs_magnitude_graph_exists_real_arguments_arguments():
    """Test if absolute magnitude scatter plot is generated with real-world arguments arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    test_absolute_magnitude_h = [26.5, 26.0, 27.0, 20.3, 25.0, 27.2, 21.0, 23.2, 24.4, 20.8]

    test_relative_velocity = [7.4542360107, 13.7256677343, 13.2380539495, 9.0509437584, 19.7887217851, 7.2800549558, 12.0981897733, 9.355840583, 11.0721262621, 17.4263077305]

    graph_abs_magnitude(test_absolute_magnitude_h, test_relative_velocity)
    assert os.path.isfile("static/abs_magnitude.html")


def test_abs_magnitude_graph_exists_arguments_x_axis_different_len():
    """Test if absolute magnitude scatter plot is generated with real-world arguments arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    test_absolute_magnitude_h = [26.5, 26.0, 27.0, 20.3, 25.0]

    test_relative_velocity = [7.4542360107, 13.7256677343, 13.2380539495, 9.0509437584, 19.7887217851, 7.2800549558, 12.0981897733, 9.355840583, 11.0721262621, 17.4263077305]

    with pytest.raises(UnknownAxisException):
        graph_abs_magnitude(test_absolute_magnitude_h, test_relative_velocity)
        '''
