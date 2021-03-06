"""Testing our Views."""
from pyramid import testing
from pyramid.testing import DummyRequest
import pytest
import os.path
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException
from space_rocks.models.meta import Base
from space_rocks.models.spacemodel import (
    Distance,
    Orbit,
    Size,
    AbsoluteMag)



@pytest.fixture
def dummy_request():
    """Set up a dummy request for testing."""
    return DummyRequest()


@pytest.fixture(scope="session")
def configuration(request):
    """Set up a Configurator instance.

    This Configurator instance sets up a pointer to the location of the
        database.
    It also includes the models from your app's model package.
    Finally it tears everything down, including the in-memory SQLite database.

    This configuration will persist for the entire duration of your PyTest run.
    """
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres:///test_database'
    })
    config.include("space_rocks.models")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database.

    This uses the dbsession_factory on the configurator instance to create a
    new database session. It binds that session to the available engine
    and returns a new session for every call of the dummy_request object.
    """
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session.
    This is a function-level fixture, so every new request will have a
    new database session.
    """
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture()
def testapp():
    """Test fixture for creating an app"""
    from space_rocks import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    """Test get response from layout view."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'SpaceRocks' in html.find("title").text


def test_index_layout(testapp):
    """Test get response from index view."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'SPACE' in html.find("h1").text


def test_about_layout(testapp):
    """Test get response from about view."""
    response = testapp.get('/about', status=200)
    html = response.html
    assert 'Chaitanya' in html.find("h1").text


def test_size_layout(testapp):
    """Test get response from size view."""
    response = testapp.get('/size', status=200)
    html = response.html
    assert 'Size' in html.find("h1").text

def test_home_view_returns_dict(dummy_request):
    """Test home view creation."""
    from space_rocks.views.default import home_view
    response = home_view(dummy_request)
    assert isinstance(response, dict)


def test_about_view_returns_dict(dummy_request):
    """Test about view creation."""
    from space_rocks.views.default import about_view
    response = about_view(dummy_request)
    assert isinstance(response, dict)


def test_size_view_returns_dict(dummy_request):
    """Test size view creation."""
    from space_rocks.views.default import size_view
    response = size_view(dummy_request)
    assert isinstance(response, dict)


'''

def test_distance_view_returns_dict(dummy_request):
    """Test size view creation."""
    from space_rocks.views.default import distance_view
    response = distance_view(dummy_request)
    assert isinstance(response, dict)
'''


def test_orbit_view_returns_dict(dummy_request):
    """Test orbit view creation."""
    from space_rocks.views.default import orbit_view
    response = orbit_view(dummy_request)
    assert isinstance(response, dict)


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
        graph_abs_magnitude(test_mag, [], test_neo_names)


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
    assert os.path.isfile("static/graphs/abs_magnitude.html")
