import matplotlib.pyplot as plt
import numpy as np

import RungeKutta

# Constants
G = 4. * np.pi ** 2  # Gravitational Constant G, for use with Astronomical Units.
mEarth = 5.972 * 10 ** 24  # kg
mSun = 1.989 * 10 ** 30  # kg

# Reduced masses
r_mEarth = mEarth / (mEarth + mSun)
r_mSun = mSun / (mEarth + mSun)
distance = 1.01518824626  # AU
r_ratio = 1. + r_mEarth / r_mSun  # Useful value which will be used in the gravity equations

# Center of mass when both masses are on the x-axis
barycenter = (mSun * distance) / (mEarth + mSun)
print("Barycenter: ", barycenter)

# Initial conditions - Note that in this configuration both bodies exist on the line y = 0, and the Sun has no
#                      initial velocity.
x0_sun = barycenter - distance  # Initial x position of the sun
x0_earth = barycenter  # Initial x position of Earth
v0_earth = 6.2777771  # Initial velocity of Earth, in AU/yr

print("The mass of the Earth is %fkg, while the mass of the sun is %fkg. The Earth initially traveling at %fAU per "
      "year." % (mEarth, mSun, v0_earth))


def fct(x, y):
    """
    Function for the Runge-Kutta algorithm, which calculates a simultaneous equation for the two body problem.
    :param x: The x value for the function.
    :param y: The y value for the function.
    :return: An array y[] which contains the corresponding values for each equation,
             which includes position and velocity.
    """
    r = np.sqrt((y[0] * r_ratio) ** 2 + (y[2] * r_ratio) ** 2.)

    return np.array([y[1],  # Initial x of the body
                     - G * r_mSun * y[0] * r_ratio / r ** 3,  # X component of velocity dx/dt
                     y[3],  # Initial y of the body
                     - G * r_mSun * y[2] * r_ratio / r ** 3])  # Y component of velocity dx/dt


def findPeriod(values, step):
    """
    Find the x and y values at time 0, and then look for the next identical entry and compare time
    :param values: The values returned from the Runge-Kutta algorithm
    :param step: The step used in the Runge-Kutta algorithm, in AU
    """
    t0 = values[0]
    next = 0
    for i in range(0, len(values)):
        # We take the substring in order to get the closes values and avoid float precision errors
        if str(values[i, 1])[0:3] == str(t0[1])[0:3] and str(values[i, 3])[0:3] == str(t0[3])[0:3]:
            next = i
    return (next * step)


x = x0_earth  # Initial x position of Earth
vx = 0  # Initial x velocity of Earth, which is 0
y = 0  # Initial y position of Earth, which is 0
vy = v0_earth  # Initial y velocity of Earth

# Initial values packaged into array for use with function fct.
y = np.array([x, vx, y, vy])

# Runge-Kutta algorithm used with the initial conditions, which plots the results.
values = RungeKutta.RungeKutta(fct, 0.01, 0, y, 2)

# Plotting the results
plt.plot(values[:, 0], values[:, 1])  # Plot of the x component of Earth's velocity
plt.show()
plt.plot(values[:, 0], values[:, 3])  # Plot of the y component of Earth's velocity
plt.show()
plt.plot(values[:, 1], values[:, 3])  # Plot of Earth's position
plt.show()

print("The orbital period of the Sun - Earth system is %f years." % (findPeriod(values, 0.01)))
