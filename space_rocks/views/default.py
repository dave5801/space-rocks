"""."""
from pyramid.views import view_config


@view_config(route_name='home', renderer='index.jinja2')
def home_view(request):
    """Home view for website."""
    pass


@view_config(route_name='about', renderer='about_us.jinja2')
def about_view(request):
    """Renders about us page."""
    pass


@view_config(route_name='size', renderer='size_view.jinja2')
def size_view(request):
    """Renders view page for the size view."""
    pass


@view_config(route_name='distance', renderer='distance_view.jinja2')
def distance_view(request):
    """Renders the distance view."""
    pass


@view_config(route_name='absmag', renderer='absmag_view.jinja2')
def absolute_magnitude_view(request):
    """Renders the view for absolute mignitude."""
    pass


@view_config(route_name='orbits', renderer='orbits_view.jinja2')
def orbit_view(request):
    """Renders the view for the orbits."""
    pass
