# Test
def RungeKuttaTest(value):
    print("Placeholder for now to demonstrate that tests work")
    return value


# Function f, and step h, at position x and y. Note that the answer is at position f(x+h)
def RungeKutta(f, h, x, y):
    F1 = h * f(x, y)
    F2 = h * f(x + 0.5 * h, y + 0.5 * F1)
    F3 = h * f(x + 0.5 * h, y + 0.5 * F2)
    F4 = h * f(x + h, y + F3)

    # y(x + h) = y(x) + 1/6 (F1 + 2F2 +2F3 +F4)
    return y + ((1 / 6) * (F1 + 2 * F2 + 2 * F3 + F4))
