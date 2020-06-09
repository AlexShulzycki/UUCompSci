# Test
def RungeKuttaTest(value):
    print("Placeholder for now to demonstrate that tests work")
    return value

# Function f, and step h, at starting position x0 and y0, up until x. Answer is at position (x, y(x)).
def RungeKutta(f, h, x0, y0, x):

    # Amount of steps needed
    n = int((x - x0) / h)

    for i in range(1, n+1):

        F1 = h * f(x0, y0)
        F2 = h * f(x0 + 0.5 * h, y0 + 0.5 * F1)
        F3 = h * f(x0 + 0.5 * h, y0 + 0.5 * F2)
        F4 = h * f(x0 + h, y0 + F3)

        x0 += h
        # y(x + h) = y(x) + 1/6 (F1 + 2F2 +2F3 +F4)
        y0 += ((1 / 6) * (F1 + 2 * F2 + 2 * F3 + F4))

    return y0
