"""."""
from pyramid.view import view_config
from space_rocks.models.spacemodel import (
    Distance,
    Size,
    AbsoluteMag,
    Orbit)


@view_config(route_name='home', renderer='../templates/index.jinja2')
def home_view(request):
    """Home view for website."""
    return {}


@view_config(route_name='about', renderer='../templates/about_us.jinja2')
def about_view(request):
    """Renders about us page."""
    return {}


@view_config(route_name='size', renderer='../templates/size_view.jinja2')
def size_view(request):
    """Renders view page for the size view."""
    return {}


@view_config(route_name='distance', renderer='../templates/distance_view.jinja2')
def distance_view(request):
    """Renders the distance view."""
    from space_rocks.views.distance_graph import gather_data
    asteroids = request.dbsession.query(Distance).all()
    asteroid_list = []
    for neo in asteroids:
        asteroid_list.append(neo)
    graph = gather_data(asteroid_list)
    return {
        "asteroids": asteroids
    }


@view_config(route_name='absmag', renderer='../templates/absmag_view.jinja2')
def absolute_magnitude_view(request):
    """Renders the view for absolute mignitude."""
    return {}


@view_config(route_name='orbits', renderer='../templates/orbits_view.jinja2')
def orbit_view(request):
    """Renders the view for the orbits."""
    return {}


@view_config(route_name='detail', renderer='../templates/detail_view.jinja2')
def detail_view(request):
    """Renders the detail view for Near Earth Object."""
    neo_id = int(request.matchdict['id'])
    return {}
