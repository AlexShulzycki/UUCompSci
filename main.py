import numpy as np

import RungeKutta


class LargeBody:
    mass = 0
    position = []
    velocityVector = []
    acceleration = [0,0]

    def __init__(self, _mass, _position, _velocityVector):
        self.mass = _mass
        self.position = _position
        self.velocityVector = _velocityVector

# Constants
G = 6.674083131313131313 * 10 ** (-11)


mEarth = 5.972 * 10 ** 24  # kg
mSun = 1.989 * 10 ** 30  # kg
#reduced masses
r_mEarth = mEarth / (mEarth + mSun)
r_mSun = mSun / (mEarth + mSun)
distance = 1.01518824626  # AU


# center of mass when both masses are on the x-axis
barycenter = (mSun * distance) / (mEarth + mSun)
print("Barycenter: ", barycenter)

x0_sun = barycenter - distance
x0_earth = barycenter

v0_earth = 6.2777771  # AU/yr

s = 1 + mEarth / mSun

# Declaring the Earth and Sun objects

Earth = LargeBody(mEarth, [x0_earth, 0], [0, v0_earth]) # Position (distance, x) going v0 in the y direction
Sun = LargeBody(mSun, [x0_sun, 0], [0,0]) # The sun sitting in the middle, not doing anything


def accelerationFunctionX(x, y):
    gmass = -G * Earth.mass
    massratio = 1 + Earth.mass / Sun.mass
    bottom = (x ** 2 * massratio ** 2 + y ** 2 * massratio ** 2) ** 1.5
    resultx = gmass * x * massratio
    return resultx / bottom

def accelerationFunctionY(x, y):
    gmass = -G * Earth.mass
    massratio = 1 + Earth.mass / Sun.mass
    bottom = (x ** 2 * massratio ** 2 + y ** 2 * massratio ** 2) ** 1.5
    resultx = gmass * y * massratio
    return resultx / bottom







def fct(x, y):
    G = 4. * np.pi ** 2

    r = np.sqrt((y[0] * (1. + r_mEarth / r_mSun)) ** 2 + (y[2] * (1. + r_mEarth / r_mSun)) ** 2.)

    return np.array([y[1], - G * r_mSun * y[0] * (1 + r_mEarth / r_mSun) / r ** 3,
            y[3], - G * r_mSun * y[2] * (1 + r_mEarth / r_mSun) / r ** 3])  # dy/dx = v, dv/dx = F

x = x0_earth
vx = 0
y = 0
vy = v0_earth

y = np.array([x, vx, y, vy])

def integrate():
    RungeKutta.RungeKutta(fct, 0.01, 0, y, 2)

integrate()


# velocities of earth with respect to the barycenter = Vx and Vy
# velocities of sun are -p * Vx and -p * Vy, with p being a constant we will calculate
# same goes for accelerations in x and y direction, thus we only need the velocities of earth in x and y direction
# aka earths change in position per time period
#
# at x0, Vx = 0 and Vy = max, & acceleration in x direction = - gravitational force from sun on earth
# at a quarter of the orbit, Vx = max and Vy = 0

print("The mass of the Earth is %fkg, while the mass of the sun is %fkg" % (mEarth, mSun))


