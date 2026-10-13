// ---------- constants (from const.py) ----------
export const MU_EARTH = 398600.4418; // km^3 / s^2
export const MU_MOON = 4902.8;       // km^3 / s^2
export const G0 = 0.00981;           // km / s^2, for the rocket equation
export const R_EARTH = 6371.0;       // km
export const R_MOON = 1737.1;        // km

// ---------- vector maths ----------
export function magnitude(v) {
  return Math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2);
}

export function dot(a, b) {
  return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

export function cross(a, b) {
  return [
    a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0],
  ];
}

// ---------- orbit maths ----------
// Vis-viva: speed at distance r on an orbit with semi-major axis a
export function visViva(mu, r, a) {
  return Math.sqrt(mu * (2 / r - 1 / a));
}

// Circular orbit speed (vis-viva with r = a)
export function circularVelocity(mu, r) {
  return Math.sqrt(mu / r);
}

export function getDeltaV(v1, v2) {
  return Math.abs(v2 - v1);
}

// Tsiolkovsky rocket equation: propellant needed
export function getFuel(mass, isp, deltaV) {
  const massRatio = Math.exp(deltaV / (isp * G0));
  return mass * (massRatio - 1);
}
