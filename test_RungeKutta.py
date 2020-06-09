from unittest import TestCase
import numpy
import RungeKutta

# You can hit the green arrows to run individual tests,
# or press the arrow next to the class declaration to run all of them
class Test(TestCase):

    def testRungeKuttaBasic(self):
        def f(x, y):
            return (5 * x**2 - y)/(numpy.e**(x+y))

        def g(x, y):
            return ((x + y) / 2)
        functions = [f]
        assert str(RungeKutta.RungeKutta(functions, 0.1, 1, 0, 5)[0])[0:6] == "2.1526"
        assert str(RungeKutta.RungeKutta(functions, 0.1, 0, 1, 0.1)[0])[0:6] == "0.9655"
        assert str(RungeKutta.RungeKutta(functions, 0.1, 0, 1, 0.2)[0])[0:6] == "0.9377"

