import const
import datetime
import phy_functions as p
import math

def calculate_window(year, month, day, hour, alt, target_alt):

    r_moon, v_moon = p.get_moon(year, month, day, hour)
    magr = (p.magnitude(r_moon))

    r1 = const.R_EARTH + alt
    r2 = magr - const.R_MOON + target_alt
    a_tran = (r2/2+r1/2)

    # Moon orbit's normal
    m_norm = p.vec_pro(r_moon, v_moon)
    # Inclination angle
    inc = math.acos((p.dot_pro(m_norm, const.EARTH_NORTH_POLE))/p.magnitude(m_norm))

    # Moon mean motion
    moon_mm = math.sqrt(const.MU_EARTH/magr**3)
    # Time of Flight
    TOF = math.pi*math.sqrt((a_tran**3)/const.MU_EARTH)

    # ideal phase angle for launch window good
    ideal_phase = math.pi - (moon_mm * TOF)
    # current phase angle
    now_phase = math.acos(p.dot_pro([r1,0,0], r_moon)/(r1*magr))

    return {                                    #-----------------------for down function also
        "TOF":  TOF/86400,
        "Ideal_Phase": math.degrees(ideal_phase),
        "Current_Phase": math.degrees(now_phase),
        "Inc": math.degrees(inc),
        "atran": a_tran,
        "r2": r2,
        "target_alt": target_alt
    }

#=================================================================================================

def calc_fuel(alt, results, isp, mass):
    r1 = const.R_EARTH + alt
    a = results['atran']
    i = results['Inc']
    r2 = results['r2']
    target = results['target_alt']

    v1 = p.get_cir_vel(const.MU_EARTH, r1)
    v2 = p.get_vis_vel(const.MU_EARTH, r1, a)

    dv1 = abs(v2-v1) #p.get_deltav(v1, v2, i) ---------------------------TRANSFER DV

    v_apo = p.get_vis_vel(const.MU_EARTH, r2, a)
    v_moon = p.get_cir_vel(const.MU_EARTH, r2)
    v_infinity = abs(v_moon-v_apo)

    r_orbit = const.R_MOON + target

    v_arr = math.sqrt(v_infinity**2 +(2*(const.MU_MOON/r_orbit)))
    v_capture = math.sqrt(const.MU_MOON/r_orbit)

    dv2 = abs(v_arr - v_capture) #--------------------------------------- CAPTURE DV

    deltav = dv1 + dv2

    fuel = p.get_fuel(mass, isp, deltav)

    return fuel, deltav

#=========================================================================================

def next_date(year, month, day, alt, target_alt):
    now = datetime.datetime(year, month, day)

    for i in range(24*31): #one month of orbit
        y,m,d,h = now.year, now.month, now.day, now.hour

        output = calculate_window(y, m, d, h, alt, target_alt)
        delta =  abs(output['Ideal_Phase'] - output['Current_Phase']) % 360
        if delta > 180:
            delta = 360 - delta

        if delta < 1:
            return now, output#---------------------------

        now += datetime.timedelta(hours=1)

    return None, None
