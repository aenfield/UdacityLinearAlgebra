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




if __name__ == '__main__':
    unittest.main()
