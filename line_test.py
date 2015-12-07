import unittest

import line
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

    def test_equal_overload_uses_coincident_lines(self):
        l1 = Line(Vector([1,1]), 1)
        l2 = Line(Vector([-3,-3]), -3)

        self.assertTrue(l1 == l2)


class IntersectionTest(unittest.TestCase):

    def test_single_intersection(self):
        l1 = Line(Vector([1,1]), 3)
        l2 = Line(Vector([1,-1]), 1)

        self.assertEqual(l1.intersectionWith(l2), (2,1) )

    def test_no_intersections(self):
        # these lines are parallel, so no intersections
        l1 = Line(Vector([2,3]), 6)
        l2 = Line(Vector([2,3]), 12)

        self.assertEqual(l1.intersectionWith(l2), None)

    def test_infinite_intersections(self):
        # these lines are equal/coincident, so infinite intersections
        l1 = Line(Vector([1,1]), 1)
        l2 = Line(Vector([-3,-3]), -3)

        self.assertEqual(l1.intersectionWith(l2), l1)



if __name__ == '__main__':
    unittest.main()
