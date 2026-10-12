from const import earth, moon, ts, G0
import math


# ------ MATH STUFF

def magnitude(vector):
    return (math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2))

def dot_pro(vec1, vec2):
    return (vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2])

def vec_pro(vec1, vec2):
    return [
        ((vec1[1]*vec2[2])-(vec2[1]*vec1[2])), #i
        ((vec1[2]*vec2[0])-(vec1[0]*vec2[2])), #j
        ((vec1[0]*vec2[1])-(vec2[0]*vec1[1])), #k
    ]

# ------ MOON STUFF

def get_moon(year, month, day, hour=0):
    t = ts.utc(year, month, day, hour)
    barycentric = earth.at(t)
    astrometric = barycentric.observe(moon) # similar to documentation example

    r_moon = astrometric.position.km
    v_moon = astrometric.velocity.km_per_s

    return r_moon, v_moon

# ------ ORBIT STUFF

def get_vis_vel(mu, r, a): # Vis-Viva Equation : velocity at distance r for an orbit with semi-major axis a
    return math.sqrt(mu*(2/r - 1/a))

def get_cir_vel(mu, r): # Above but r = a
    return math.sqrt(mu/r)

def get_deltav(v1, v2, i):
    #inc_rad = math.radians(i)
    #return math.sqrt(v1**2 + v2**2 - 2*v1*v2*math.cos(inc_rad)) # law of cosines, vector subtraction for magnitude
    return abs(v2-v1)

#------- Tsiolkovsky Rocket Equation for fuel required

def get_fuel(mass, isp, delv):
    mass_ratio = math.exp(delv / (isp*G0))
    return mass*(mass_ratio - 1)
