"""."""
from pyramid.views import view_config


@view_config(route_name='home', renderer='.jinja2')
def home_view(request):
    """Home view."""
    pass


@view_config(route_name='about', renderer='.jinja2')
def about_view(request):
    """Home view."""
    pass


@view_config(route_name='size', renderer='.jinja2')
def size_view(request):
    """Home view."""
    pass


@view_config(route_name='distance', renderer='.jinja2')
def distance_view(request):
    """Home view."""
    pass


@view_config(route_name='absmag', renderer='.jinja2')
def absolute_magnitude_view(request):
    """Home view."""
    pass


@view_config(route_name='orbits', renderer='.jinja2')
def orbit_view(request):
    """Home view."""
    pass
