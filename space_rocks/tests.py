"""Testing our Views."""
from pyramid import testing
import random
from pyramid.testing import DummyRequest
import pytest
import os.path
from faker import Faker
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException
from space_rocks.models.meta import Base
from space_rocks.models.spacemodel import (
    Distance,
    Orbit,
    Size,
    AbsoluteMag)


TEST_ID = [3542519, 3542518, 3542517, 3542516, 3542515]

TEST_DATE = ["1900-07-27", "1902-02-11", "1903-09-02", "1904-07-26", "1904-07-26"]

TEST_NEO_ID = [3542519, 3542518, 3542517, 3542516, 3542515]

TEST_NAME = ["2010 PK9", "1998 BT13", "1998 BR26", "1998 DX11", "1998 DV20"]

TEST_URL = [
            "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3542519",
            "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3542518",
            "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3542517",
            "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3542516",
            "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3542515",
            ]

TEST_KILOMETER = [0.0133215567, 0.0133215567, 0.0133215567, 0.0167708462, 0.0375007522]

TEST_METER = [16.7708462163, 37.5007521798, 10.5816885933, 23.6613750114, 231.5021222103]

TEST_MILES = [0.0104209175, 0.0233018799, 0.0065751544, 0.0147024923, 0.1438487052]

TEST_FEET = [55.0224631002, 123.0339677816, 34.7168272045, 77.6291855923, 759.5214226325]

TEST_ASTRONOMICAL = [0.0174689341, 0.0147178778, 0.1736806106, 0.0121961839, 0.1799477889]

TEST_LUNAR = [6.7954158783, 5.7252545357, 67.5617523193, 4.7443156242, 69.9996948242]

TEST_ABSOLUTE_MAG = [26.5, 26.0, 27.0, 20.3, 25.0]

TEST_VELOCITY_KPS = [7.4542360107, 13.7256677343, 13.7256677343, 9.0509437584, 19.7887217851]

TEST_VELOCITY_KPH = [26835.2496386258, 49412.4038435444, 49412.4038435444, 32583.3975300707, 71239.3984263222]

TEST_VELOCITY_MPH = [16674.3805324006, 30702.9461548957, 30702.9461548957, 20246.0560930598, 44265.3917610667]

TEST_ORBIT_PERIOD = [1407.711865632511, 767.1727041453258, 1437.626473218831, 1021.424523097348, 210.3776889314703]

TEST_PERIHELION_TIME = [2457878.800930631387, 2457794.691457975686, 2450854.056593533752, 2450793.681066286840, 2450971.788299469493]

TEST_APHELION_DISTANCE = [3.926911208758061, 2.442028495815412, 4.000026175956884, 3.192506303737014, .9802476908913854]

TEST_ECCENTRICITY = [.5974999452373421, .4889756094791248, .6045912153686241, .608396777796715, .4160165389063018]

TEST_PERIHELION_DISTANCE = [.9894097219129394, .8381172369540927, .9856999549666915, .7772931236285567, .4042667748061776]

FAKE_FACTORY = Faker()

SIZE_LIST = [Size(
   # id=random.choice(TEST_ID),
    date=random.choice(TEST_DATE),
    neo_id=random.choice(TEST_NEO_ID),
    name=random.choice(TEST_NAME),
    url=random.choice(TEST_URL),
    kilometers=random.choice(TEST_KILOMETER),
    meters=random.choice(TEST_METER),
    miles=random.choice(TEST_MILES),
    feet=random.choice(TEST_FEET)
    ) for i in range(20)]


DISTANCE_LIST = [Distance(
    #id=random.choice(TEST_ID),
    date=random.choice(TEST_DATE),
    neo_id=random.choice(TEST_NEO_ID),
    name=random.choice(TEST_NAME),
    url=random.choice(TEST_URL),
    astronomical=random.choice(TEST_ASTRONOMICAL),
    lunar=random.choice(TEST_LUNAR),
    kilometers=random.choice(TEST_KILOMETER),
    miles=random.choice(TEST_MILES)
    )for i in range(20)]


ABSOLUTE_MAG_LIST = [AbsoluteMag(
   # id=random.choice(TEST_ID),
    date=random.choice(TEST_DATE),
    neo_id=random.choice(TEST_NEO_ID),
    name=random.choice(TEST_NAME),
    url=random.choice(TEST_URL),
    velocity_kps=random.choice(TEST_VELOCITY_KPS),
    velocity_kph=random.choice(TEST_VELOCITY_KPH),
    velocity_mph=random.choice(TEST_VELOCITY_MPH)
    )for i in range(20)]



ORBIT_LIST = [Orbit(
   # id=random.choice(TEST_ID),
    date=random.choice(TEST_DATE),
    neo_id=random.choice(TEST_NEO_ID),
    name=random.choice(TEST_NAME),
    url=random.choice(TEST_URL),
    orbit_period=random.choice(TEST_ORBIT_PERIOD),
    perihelion_dist=random.choice(TEST_PERIHELION_DISTANCE),
    aphelion_dist=random.choice(TEST_APHELION_DISTANCE),
    eccentricity=random.choice(TEST_ECCENTRICITY),
    perihelion_time=random.choice(TEST_PERIHELION_TIME)
    )for i in range(20)]


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

'''
def test_size_layout(testapp):
    """Test get response from size view."""
    response = testapp.get('/size', status=200)
    html = response.html
    assert 'Size' in html.find("h1").text
    '''

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


def test_size_view_returns_redirect(dummy_request):
    """Test size view with db call."""
    from space_rocks.views.default import size_view
    dummy_request.dbsession.add_all(SIZE_LIST)
    response = size_view(dummy_request)
    assert isinstance(response, dict)


def test_orbit_view_returns_redirect(dummy_request):
    """Test orbit view with db call."""
    from space_rocks.views.default import orbit_view
    dummy_request.dbsession.add_all(ORBIT_LIST)
    response = orbit_view(dummy_request)
    assert isinstance(response, dict)


def test_abs_mag_view_returns_redirect(dummy_request):
    """Test orbit view with db call."""
    from space_rocks.views.default import absolute_magnitude_view
    dummy_request.dbsession.add_all(ABSOLUTE_MAG_LIST)
    response = absolute_magnitude_view(dummy_request)
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
