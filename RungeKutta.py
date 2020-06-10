import numpy as np
import matplotlib.pyplot as plt

# Function f, and step h, at starting position x0 and y0, up until x. Answer is at position (x, y(x)).
def RungeKutta(f, h, t0, y0, x):

    # Amount of steps needed
    n = int((x - t0) / h)

    m = len(y0)
    F1 = np.zeros(m)
    F2 = np.zeros(m)
    F3 = np.zeros(m)
    F4 = np.zeros(m)

    results = []

    #for f in functions:
    values = np.zeros((n, 5))
    for i in range(0, n):

        for j in range(0,m):
            F1[j] = h * f(t0, y0)[j]
        for j in range(0,m):
            F2[j] = h * f(t0 + 0.5 * h, y0 + 0.5 * F1)[j]
        for j in range(0, m):
            F3[j] = h * f(t0 + 0.5 * h, y0 + 0.5 * F2)[j]
        for j in range(0, m):
            F4[j] = h * f(t0 + h, y0 + F3)[j]

        for k in range(0,m):
            # y(x + h) = y(x) + 1/6 (F1 + 2F2 +2F3 +F4)
            y0[k] += ((1 / 6) * (F1[k] + 2 * F2[k] + 2 * F3[k] + F4[k]))

        values[i] = t0, y0[0], y0[1], y0[2], y0[3]

        # Increment x for next iteration
        t0 += h

    # PLOT results here so you get one plot per function

    plt.plot(values[:,0], values[:,1])
    plt.show()
    plt.plot(values[:,0], values[:,3])
    plt.show()
    plt.plot(values[:,1], values[:,3])
    plt.show()

    #results.append(y0)

    return y0




