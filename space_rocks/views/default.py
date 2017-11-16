"""."""
from pyramid.view import view_config
from space_rocks.models.spacemodel import (
    Distance,
    Orbit,
    Size,
    AbsoluteMag,
)


@view_config(route_name='home', renderer='../templates/index.jinja2')
def home_view(request):
    """Home view for website."""
    return {}


@view_config(route_name='about', renderer='../templates/about_us.jinja2')
def about_view(request):
    """Render the about us page."""
    return {}


@view_config(route_name='size', renderer='space_rocks:templates/size_view.jinja2')
def size_view(request):
    """Render the view page for the size view."""
    from space_rocks.views.size_chart import size_chart
    asteroids = request.dbsession.query(Size).order_by(Size.feet.desc()).all()
    script, div = size_chart(asteroids)
    return {
        "asteroids": asteroids,
        "script": script,
        "div": div
    }


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
    """Render the view for absolute mignitude."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    plot_data = request.dbsession.query(AbsoluteMag).all()

    mag_axis = []
    vel_axis = []

    for i in range(len(plot_data)):
        mag_axis.append(plot_data[i].absolutemag)
        vel_axis.append(plot_data[i].velocity_kps)

    graph_abs_magnitude(mag_axis, vel_axis)

    return {}


@view_config(route_name='orbits', renderer='../templates/orbits_view.jinja2')
def orbit_view(request):
    """Renders the view for the orbits."""
    Orbits = request.dbsession.query(Orbit).all()
    return {
        "Orbits": Orbits
    }


@view_config(route_name='detail', renderer='../templates/detail_view.jinja2')
def detail_view(request):
    """Render the detail view for Near Earth Object."""
    neo_id = int(request.matchdict['id'])
    return {}
