from sqlalchemy import (
    Bool,
    Column,
    Float,
    Integer,
    Unicode
)

from .meta import Base


class Size(Base):
    """Size data for N.E.Os."""

    __tablename__ = 'sizedata'
    id = Column(Unicode)
    name = Column(Unicode)
    kilometers = Column(Float)
    meters = Column(Float)
    miles = Column(Float)
    feet = Column(Float)


class Distance(Base):
    """Distance data for N.E.Os."""

    __tablename__ = 'distancedata'
    id = Column(Unicode)
    name = Column(Unicode)
    astronomical = Column(Float)
    lunar = Column(Float)
    kilometers = Column(Float)
    miles = Column(Float)


class AbsoluteMag(Base):
    """Absolute Magnitude data for N.E.Os."""

    __tablename__ = 'absmagdata'
    id = Column(Unicode)
    absolutemag = Column(Float)
    velocity_kps = Column(Float)
    velocity_kph = Column(Float)
    velocity_mph = Column(Float)


class Orbit(Base):
    """Orbit data for N.E.Os."""

    __tablename__ = 'orbitdata'
    id = Column(Unicode)
    orbit_body = Column(Unicode)
    orbit_period = Column(Float)
    perihelion_dist = Column(Float)
    aphelion_dist = Column(Float)
    eccentricity = Column(Float)
    perihelion_time = Column(Float)
