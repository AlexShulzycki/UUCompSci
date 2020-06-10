import numpy as np


class LargeBody:
    mass = 0
    position = []
    velocityVector = []

    def __init__(self, _mass, _position, _velocityVector):
        self.mass = _mass
        self.position = _position
        self.velocityVector = _velocityVector

# Constants
G = 6.674083131313131313 * 10 ** (-11)

mEarth = 5.972 * 10 ** 24  # kg
mSun = 1.989 * 10 ** 30  # kg
distance = 151.87 * 10 ** 9  # m

# center of mass when both masses are on the x-axis
barycenter = (mSun * distance) / (mEarth + mSun)
print(barycenter)

x0_sun = barycenter - distance
x0_earth = barycenter

v0_earth = 29.78  # km/s

s = 1 + mEarth / mSun

# Declaring the Earth and Sun objects

Earth = LargeBody(mEarth, [0, distance], [v0_earth, 0]) # Position (0, distance) going v0 in the x direction
Sun = LargeBody(mSun, [0,0], [0,0]) # The sun sitting in the middle, not doing anything

def simulate(body1, body2, steps):
    for i in range(0, steps):
        # Calculate distance r squared
        r2 = [body1.position[0] - body2.position[0], body1.position[1] - body2.position[1]]



# velocities of earth with respect to the barycenter = Vx and Vy
# velocities of sun are -p * Vx and -p * Vy, with p being a constant we will calculate
# same goes for accelerations in x and y direction, thus we only need the velocities of earth in x and y direction
# aka earths change in position per time period
#
# at x0, Vx = 0 and Vy = max
# at a quarter of the orbit, Vx = max and Vy = 0

def velocityEarth_x(x, t):
    return (x / t)


def velocityEarth_y(y, t):
    return (y / t)


def accelerationEarth_x(x, y):
    return (-1 * G * mSun) * (x * s) / (np.sqrt(x ** 2 * s ** 2 + y ** 2 * s ** 2)) ** 3


def accelerationEarth_y(x, y):
    return (-1 * G * mSun) * (y * s) / (np.sqrt(x ** 2 * s ** 2 + y ** 2 * s ** 2)) ** 3


print("The mass of the Earth is %fkg, while the mass of the sun is %fkg" % (mEarth, mSun))


