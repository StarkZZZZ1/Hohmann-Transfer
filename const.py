from skyfield.api import load
# https://rhodesmill.org/skyfield/positions.html#quick-reference

ts = load.timescale()
planets = load('de421.bsp')
earth, moon = planets['earth'], planets['moon']

# CONSTANTS
MU_EARTH = 3.986004418e5
MU_MOON = 4902.8    # in km^3 / s^2
G0 = 0.00981                # for rocket equation, in km / s^2
R_EARTH = 6371.0            # in km
R_MOON = 1737.1             # in km

EARTH_NORTH_POLE = [0.0, 0.0, 1.0] # ALL LAUNCHES ASSUMED FROM EQUATOR


