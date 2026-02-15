import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleFunc(unittest.TestCase):

    def test_equilateral(self):
        res = get_triangle_type(5.0, 5.0, 5.0) 
        self.assertEqual(res, "equilateral")
    
    def test_isosceles(self):
        res = get_triangle_type(4.0, 4.0, 6.0) 
        self.assertEqual(res, "isosceles")
    
    def test_nonequilateral(self):
        res = get_triangle_type(3.0, 4.0, 5.0) 
        self.assertEqual(res, "nonequilateral")
    
    def test_isosceles_another_sides(self):
        res = get_triangle_type(5.0, 3.0, 3.0) 
        self.assertEqual(res, "isosceles")
    
    def test_isosceles_minimal_value(self):
        res = get_triangle_type(0.1, 0.1, 0.15) 
        self.assertEqual(res, "isosceles")

    def test_equilateral_maximum_value(self):
        res = get_triangle_type(1_000_000.0, 1_000_000.0, 1_000_000.0) 
        self.assertEqual(res, "equilateral")
    
    def test_one_side_zero(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0.0, 4.0, 5.0) 
    
    def test_one_side_negative(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3.0, -4.0, 5.0) 
    
    def test_degenerate_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2.0, 3.0, 5.0) 
    
    def test_violation_triangle_inequalities(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1.0, 2.0, 10.0) 
    
    def test_simple_degenerate_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0.0, 0.0, 0.0) 
    
    def test_two_side_negative(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-4.0, -4.0, 5.0) 
    
    def test_one_side_not_a_number(self):
        with self.assertRaises((IncorrectTriangleSides, TypeError)):
            get_triangle_type("4.0", 4.0, 5.0) 
    
    def test_huge_nequality(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1.0, 1.0, 1000.0) 

if __name__ == "__main__":
    unittest.main()