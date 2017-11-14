import os
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.models')
    config.scan()
    return config.make_wsgi_app()
