import os
import sys

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
)
<<<<<<< HEAD
# from spce_rocks.models.spacemodel import Size
# from spce_rocks.models.spacemodel import Distance
# from spce_rocks.models.spacemodel import AbsoluteMag
# from spce_rocks.models.spacemodel import Orbit
=======
from space_rocks.models.spacemodel import Size, AbsoluteMag, Distance, Orbit
from space_rocks.data.space_data import SUPER_DICT
>>>>>>> master


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    if os.environ.get('DATABASE_URL', ''):
        settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]
    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        size_models = []
        distance_models = []
        absolute_magnitude_models = []
        orbit_models = []
        for item in SUPER_DICT:
            new_size = Size(
                id=int(item["id"]),
                name=item["name"],
                kilometers=item["diakm"],
                meters=item["diam"],
                miles=item["diamiles"],
                feet=item["diafeet"],
            )
            size_models.append(new_size)
            new_distance = Distance(
                id=int(item["id"]),
                name=item["name"],
                astronomical=item["miss_astronomical"],
                lunar=item["miss_lunar"],
                kilometers=item["miss_km"],
                miles=item["miss_miles"],
            )
            distance_models.append(new_distance)
            new_absmag = AbsoluteMag(
                id=int(item["id"]),
                name=item["name"],
                absolutemag=item["absmag"],
                velocity_kps=item["velocity_kps"],
                velocity_kph=item["velocity_kph"],
                velocity_mph=item["velocity_mph"],
            )
            absolute_magnitude_models.append(new_absmag)
            new_orbit = Orbit(
                id=int(item["id"]),
                name=item["name"],
                orbit_period=item["orbit_period"],
                perihelion_dist=item["perihelion_dist"],
                aphelion_dist=item["aphelion_dist"],
                eccentricity=item["orbit_eccentricity"],
                perihelion_time=item["perihelion_time"],
            )
            orbit_models.append(new_orbit)
        dbsession.add_all(
            size_models,
            distance_models,
            absolute_magnitude_models,
            orbit_models)
