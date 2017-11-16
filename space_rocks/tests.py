"""Testing our Views."""
from pyramid.testing import DummyRequest
import pytest
import os.path
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException


@pytest.fixture
def dummy_request():
    """Set up a dummy request for testing."""
    return DummyRequest()


def test_home_view_returns_empty_dict(dummy_request):
    """Test home view creation."""
    from space_rocks.views.default import home_view
    dummy_request.method = "POST"
    response = home_view(dummy_request)
    assert response == {}


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
        graph_abs_magnitude(test_mag, test_vel, [])


def test_abs_magnitude_graph_exists_valid_arguments():
    """Test if absolute magnitude scatter plot is generated with arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    test_mag = [1, 2, 3, 4, 5]
    test_vel = [2, 5, 8, 2, 7]
    test_neo_names = ["ceres", "phobos", "deimos", "asteroid x", "it was earth all along!!"]

    graph_abs_magnitude(test_mag, test_vel, test_neo_names)
    assert os.path.isfile("static/abs_magnitude.html")
