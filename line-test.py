import unittest

from line import Line
from vector import Vector

class ParallelLinesTest(unittest.TestCase):

    def test_parallel_lines_are_parallel(self):
        l1 = Line(Vector([2,3]), 6)
        l2 = Line(Vector([2,3]), 12)

        self.assertTrue(l1.parallelTo(l2))
        self.assertTrue(l2.parallelTo(l1))

    def test_non_parallel_lines_are_not_parallel(self):
        l1 = Line(Vector([2,3]), 6)
        l2 = Line(Vector([3,2]), 6)

        self.assertFalse(l1.parallelTo(l2))
        self.assertFalse(l2.parallelTo(l1))


# 'coincident' lines are the same line
class CoincidentLinesTest(unittest.TestCase):

    def test_coincident_lines_are_coincident(self):
        l1 = Line(Vector([1,1]), 1)
        l2 = Line(Vector([-3,-3]), -3)

        self.assertTrue(l1.coincidentTo(l2))
        self.assertTrue(l2.coincidentTo(l1))

    def test_non_coincident_lines_are_not_coincident(self):
        l1 = Line(Vector([1,1]), 1)
        l2 = Line(Vector([1,1]), 2)

        self.assertFalse(l1.coincidentTo(l2))
        self.assertFalse(l2.coincidentTo(l1))

    def test_coincident_vertical_lines_are_coincident(self):
        l1 = Line(Vector([1,0]), 1)
        l2 = Line(Vector([5,0]), 5)

        self.assertTrue(l1.coincidentTo(l2))

    def test_coincident_horizontal_lines_are_coincident(self):
        l1 = Line(Vector([0,1]), 1)
        l2 = Line(Vector([0,5]), 5)

        self.assertTrue(l1.coincidentTo(l2))

    def test_can_get_a_point_on_a_diagonal_line(self):
        self.assertEqual(Line(Vector([1,1]), 1).pointOnLine(), (1,0))

    def test_can_get_a_point_on_a_horizontal_line(self):
        self.assertEqual(Line(Vector([0,1]), 2).pointOnLine(), (0,2))

    def test_can_get_a_point_on_a_vertical_line(self):
        self.assertEqual(Line(Vector([1,0]), 3).pointOnLine(), (3,0))



if __name__ == '__main__':
    unittest.main()
