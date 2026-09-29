import math
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from geometry import pythagorean_areas, inscribed_angle_ratio  # noqa: E402


class GeometryTests(unittest.TestCase):
    def test_pythagorean_3_4_5(self):
        result = pythagorean_areas(3, 4)
        self.assertEqual(result["a_sq"], 9)
        self.assertEqual(result["b_sq"], 16)
        self.assertAlmostEqual(result["c"], 5.0)
        self.assertAlmostEqual(result["c_sq"], 25.0)

    def test_pythagorean_rejects_nonpositive(self):
        with self.assertRaises(ValueError):
            pythagorean_areas(0, 5)

    def test_inscribed_angle_half_of_central(self):
        self.assertEqual(inscribed_angle_ratio(80), 40)
        self.assertEqual(inscribed_angle_ratio(180), 90)

    def test_inscribed_angle_bounds(self):
        with self.assertRaises(ValueError):
            inscribed_angle_ratio(400)


if __name__ == "__main__":
    unittest.main()
