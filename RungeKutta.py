import numpy as np
import matplotlib.pyplot as plt

# Function f, and step h, at starting position x0 and y0, up until x. Answer is at position (x, y(x)).
def RungeKutta(functions, h, x0, y0, x):


    # Amount of steps needed
    n = int((x - x0) / h)

    results = []

    for f in functions:
        values = []
        for i in range(0, n):

            F1 = h * f(x0, y0)
            F2 = h * f(x0 + 0.5 * h, y0 + 0.5 * F1)
            F3 = h * f(x0 + 0.5 * h, y0 + 0.5 * F2)
            F4 = h * f(x0 + h, y0 + F3)

            # y(x + h) = y(x) + 1/6 (F1 + 2F2 +2F3 +F4)
            y0 += ((1 / 6) * (F1 + 2 * F2 + 2 * F3 + F4))

            values.append([x0, y0])

            # Increment x for next iteration
            x0 += h

        # PLOT results here so you get one plot per function
        values_array = np.array(values)
        plt.plot(values_array[:,0], values_array[:,1])
        plt.show()

        results.append(y0)

    return results


M1 = 5.972 × 10**24 #kg
M2 = 1.989 * 10**30 #kg
distance = 151.87 * 10 ** 9 #m

distance_earth_barycenter = distance * M2 / (M1 + M2)
distance_sun_barycenter = distance * M1 / (M1 + M2)

x0_earth = -distance_earth_barycenter
x0_sun = distance_sun_barycenter

s = 1 + M1/M2

def position_e(x,t):
    return (x / t)

def position_s(y,t):
    return (y / t)

def velocity_e(x,y):
    return (-1*G * M2) * ( x * s ) / ( sqrt ( x**2 * s**2 + y**2 * s**2 ) )**3

def velocity_s(x,y):
    return (-1 * G * M2) * (y * s) / ( sqrt ( x**2 * s**2 + y**2 * s**2 ) )**3