import unittest

import plane
from plane import Plane
from vector import Vector

class ParallelPlanesTest(unittest.TestCase):

    def test_parallel_planes_are_parallel(self):
        l1 = Plane(Vector([2,3,4]), 6)
        l2 = Plane(Vector([2,3,4]), 12)

        self.assertTrue(l1.parallelTo(l2))
        self.assertTrue(l2.parallelTo(l1))

    def test_non_parallel_planes_are_not_parallel(self):
        l1 = Plane(Vector([2,3,4]), 6)
        l2 = Plane(Vector([3,2,1]), 6)

        self.assertFalse(l1.parallelTo(l2))
        self.assertFalse(l2.parallelTo(l1))

# 'coincident' planes are the same plane
class CoincidentPlanesTest(unittest.TestCase):

    def test_coincident_planes_are_coincident(self):
        l1 = Plane(Vector([1,1,1]), 1)
        l2 = Plane(Vector([-3,-3,-3]), -3)

        self.assertTrue(l1.coincidentTo(l2))
        self.assertTrue(l2.coincidentTo(l1))

    def test_non_coincident_planes_are_not_coincident(self):
        l1 = Plane(Vector([1,1,1]), 1)
        l2 = Plane(Vector([1,1,1]), 2)

        self.assertFalse(l1.coincidentTo(l2))
        self.assertFalse(l2.coincidentTo(l1))

    def test_equal_overload_uses_coincident_planes(self):
        l1 = Plane(Vector([1,1,1]), 1)
        l2 = Plane(Vector([-3,-3,-3]), -3)

        self.assertTrue(l1 == l2)




if __name__ == '__main__':
    unittest.main()
