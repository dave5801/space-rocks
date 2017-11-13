"""."""
from pyramid.view import view_config


@view_config(route_name='home', renderer='space_rocks:templates/layout.jinja2')
def home_view(request):
    """Home view."""
    pass


@view_config(route_name='about')
def about_view(request):
    """Home view."""
    pass


@view_config(route_name='size')
def size_view(request):
    """Home view."""
    pass


@view_config(route_name='distance')
def distance_view(request):
    """Home view."""
    pass


@view_config(route_name='absmag')
def absolute_magnitude_view(request):
    """Home view."""
    pass


@view_config(route_name='orbits')
def orbit_view(request):
    """Home view."""
    pass
