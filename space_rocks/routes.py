"""Routes for our SPACE ROCKS site"""


def includeme(config):
    """The routes for our totally sweet SPACE ROCKS site."""
    config.add_static_view('static', 'space_rocks:static')
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('size', '/size')
    config.add_route('distance', '/distance')
    config.add_route('absmag', '/absolutemagnitude')
    config.add_route('orbits', '/orbits')
<<<<<<< HEAD
    config.add_route('neo_detail', '/neo_detail')
=======
    config.add_route('detail', '/{id:\d+}')
>>>>>>> 96cd3a96a47fec9bce5d1d88d433f626ffd35d6a
