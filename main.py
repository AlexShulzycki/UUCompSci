import matplotlib.pyplot as plt
import numpy as np

import RungeKutta

# Constants

mEarth = 5.972 * 10 ** 24  # kg
mSun = 1.989 * 10 ** 30  # kg
mMoon = 7.347 * 10 ** 22 # kg

system = input("What system would you like to compute? '1' for earth-sun, '2' for earth-moon.")

if system == "1":
    # Constants earth-sun system
    name1 = 'Earth'
    name2 = 'sun'
    M1 = mEarth / (mEarth + mSun) # Reduced mass
    M2 = mSun / (mEarth + mSun) # Reduced mass

    G = 4. * np.pi ** 2  # Gravitational Constant G, for use with Astronomical Units.
    #r_m1 = mEarth / (mEarth + mSun)
    #r_m2 = mSun / (mEarth + mSun)
    distance = 1.01518824626  # AU
    r_ratio = 1. + M1 / M2  # Useful value which will be used in the gravity equations
    v0 = 6.2777771  # Initial velocity of Earth, in AU/yr
    barycenter = M2 * distance # Center of mass when both masses are on the x-axis
    x0_2 = barycenter - distance  # Initial x position of the sun
    x0_1 = barycenter  # Initial x position of Earth

    dt = 0.01
    t_end = 2



elif system == "2":
    # Constants earth-moon system
    name1 = 'Moon'
    name2 = 'Earth'
    M1 = 7.347 * 10 ** 22 # kg
    M2 = 5.972 * 10 ** 24  # kg

    G = 6.67408 * 10**(-12)
    #r_m1 = M1 # extra reduction not needed, definition to make it work in the functions later in the code
    #r_m2 = M2 # extra reduction not needed, definition to make it work in the functions later in the code
    distance = 384400 #km
    r_ratio = 1. + M1 / M2
    v0 = 3683.  # Initial velocity of Moon, in km/hr
    barycenter = M1 * distance / (M2 + M1)  # Center of mass when both masses are on the x-axis
    x0_2 = -1 * barycenter  # Initial x position of Earth
    x0_1 = distance - barycenter  # Initial x position of the moon

    dt = 0.1
    t_end = 100


print("The mass of the %s is %fkg, while the mass of the %s is %fkg. The %s initially traveling at %fAU per "
      "year." % (name1, M1, name2, mSun, name1, v0))


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
                     - G * M2 * y[0] * r_ratio / r ** 3,  # X component of velocity dx/dt
                     y[3],  # Initial y of the body
                     - G * M2 * y[2] * r_ratio / r ** 3])  # Y component of velocity dx/dt
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



# Initial conditions - Note that in this configuration both bodies exist on the line y = 0, and the larger body has no
#                      initial velocity.
x = x0_1       # Initial x position of smaller body
vx = 0         # Initial x velocity of smaller body, which is 0
y = 0          # Initial y position of smaller body, which is 0
vy = v0        # Initial y velocity of smaller body

# Initial values packaged into array for use with function fct.
y = np.array([x, vx, y, vy])

# Runge-Kutta algorithm used with the initial conditions, which plots the results.
values = RungeKutta.RungeKutta(fct, dt, 0, y, t_end)

# Plotting the results
plt.plot(values[:, 0], values[:, 1])  # Plot of the x component of Earth's velocity
plt.show()
plt.plot(values[:, 0], values[:, 3])  # Plot of the y component of Earth's velocity
plt.show()
plt.plot(values[:, 1], values[:, 3])  # Plot of Earth's position
plt.show()

print("The orbital period of the %s - %s system is %f years." % (name1, name2, findPeriod(values, 0.01)))

