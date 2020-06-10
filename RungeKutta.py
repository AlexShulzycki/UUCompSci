import numpy as np
import matplotlib.pyplot as plt


def RungeKutta(f, h, x0, y0, x):
    """
    Takes in a function and integrates it using the Runge-Kutta algorithm. Can take in multiple y's for simultaneous
    integration over the same x.

    :param f: Function to be used that takes y as an input
    :param h: The size of the step to make in the Runge-Kutta algorithm
    :param x0: The starting value of x
    :param y0: The starting values of y - can be an array, function f will take it as an input
    :param x: The limit x that will be integrated to
    :return: The values of y0 after running the integration algorithm.
    """
    # Amount of steps needed
    n = int((x - x0) / h)

    # Declare variables for use by the Runge-Kutta algorithm
    m = len(y0)
    F1 = np.zeros(m)
    F2 = np.zeros(m)
    F3 = np.zeros(m)
    F4 = np.zeros(m)

    # for f in functions:
    values = np.zeros((n, 5))
    for i in range(0, n):

        for j in range(0, m):
            F1[j] = h * f(x0, y0)[j]
        for j in range(0, m):
            F2[j] = h * f(x0 + 0.5 * h, y0 + 0.5 * F1)[j]
        for j in range(0, m):
            F3[j] = h * f(x0 + 0.5 * h, y0 + 0.5 * F2)[j]
        for j in range(0, m):
            F4[j] = h * f(x0 + h, y0 + F3)[j]

        for k in range(0, m):
            # y(x + h) = y(x) + 1/6 (F1 + 2F2 +2F3 +F4)
            y0[k] += ((1 / 6) * (F1[k] + 2 * F2[k] + 2 * F3[k] + F4[k]))

        values[i] = x0, y0[0], y0[1], y0[2], y0[3]

        # Increment x for next iteration
        x0 += h

    # Plotting the results
    plt.plot(values[:, 0], values[:, 1])  # Plot of the x component of Earth's velocity
    plt.show()
    plt.plot(values[:, 0], values[:, 3])  # Plot of the y component of Earth's velocity
    plt.show()
    plt.plot(values[:, 1], values[:, 3])  # Plot of Earth's position
    plt.show()

    return y0
