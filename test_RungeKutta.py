from unittest import TestCase
import numpy
import RungeKutta

# You can hit the green arrows to run individual tests,
# or press the arrow next to the class declaration to run all of them
class Test(TestCase):

    def test_runge_kuttaTest(self):
        assert RungeKutta.RungeKuttaTest(5) == 5
        # Test passes because it returns true

    def test(self):
        # Create any function and it will run as a test - All assert
        # statements must evaluate to true for the test pass.
        assert 1 == 1
        assert not False

    def testRungeKuttaBasic(self):
        def f(x, y):
            return (5 * x**2 - y)/(numpy.e**(x+y))

        def g(x, y):
            return ((x + y) / 2)
        assert str(RungeKutta.RungeKutta(f, 0.1, 0, 1, 0.1))[0:6] == "0.9655"
        assert str(RungeKutta.RungeKutta(f, 0.1, 0, 1, 0.2))[0:6] == "0.9377"
