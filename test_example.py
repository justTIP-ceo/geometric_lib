import unittest
import math
from triangle import area as triangle_area
from triangle import perimeter as triangle_perimeter
from circle import area as circle_area
from circle import perimeter as circle_perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_positive_numbers(self):
        res = triangle_area(2, 3)
        self.assertEqual(res, 3)

    def test_area_negative_numbers(self):
        res = triangle_area(-1, -1)
        self.assertEqual(res, 0.5)

    def test_area_zero(self):
        res = triangle_area(0, 0)
        self.assertEqual(res, 1)
    
    def test_perimeter_positive_numbers(self):
        res = triangle_perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    def test_perimeter_negative_numbers(self):
        res = triangle_perimeter(-2, -3, -6)
        self.assertEqual(res, -11)
    
    def test_perimeter_zero(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)

class CircleTestCase(unittest.TestCase):

    def test_area_positive_numbers(self):
        res = circle_area(2)
        self.assertAlmostEqual(res, math.pi * (2 ** 2))

    def test_area_negative_numbers(self):
        res = circle_area(-1)
        self.assertEqual(res, math.pi)
    
    def test_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_positive_numbers(self):
        res = circle_perimeter(2)
        self.assertEqual(res, 4*math.pi)

    def test_perimeter_negative_numbers(self):
        res = circle_perimeter(-2)
        self.assertEqual(res, 4*math.pi)
    
    def test_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
