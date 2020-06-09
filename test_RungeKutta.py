from unittest import TestCase
import RungeKutta

# You can hit the green arrows to run individual tests,
# or press the arrow next to the class declaration to run all of them
class Test(TestCase):

    def test_runge_kutta(self):
        assert RungeKutta.RungeKutta(5) == 5
        # Test passes because it returns true

    def test(self):
        # Create any function and it will run as a test - All assert
        # statements must evaluate to true for the test pass.
        assert 1 == 1
        assert not False
