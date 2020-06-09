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



