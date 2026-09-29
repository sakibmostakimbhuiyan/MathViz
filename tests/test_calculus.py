import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from calculus import numerical_derivative, numerical_integral  # noqa: E402


class CalculusTests(unittest.TestCase):
    def test_derivative_of_x_squared(self):
        f = lambda x: x ** 2
        # d/dx x^2 = 2x, at x=3 -> 6
        self.assertAlmostEqual(numerical_derivative(f, 3), 6, places=4)

    def test_derivative_of_constant_is_zero(self):
        f = lambda x: 5
        self.assertAlmostEqual(numerical_derivative(f, 10), 0, places=6)

    def test_integral_of_x_squared_0_to_2(self):
        f = lambda x: x ** 2
        # integral of x^2 from 0 to 2 = 8/3
        self.assertAlmostEqual(numerical_integral(f, 0, 2, n=10000), 8 / 3, places=3)

    def test_integral_rejects_zero_steps(self):
        with self.assertRaises(ValueError):
            numerical_integral(lambda x: x, 0, 1, n=0)


if __name__ == "__main__":
    unittest.main()
