import unittest

from linsys import LinearSystem
from plane import Plane
from vector import Vector

# Checks that the normal vector and the constant term are equal. Works with both
# planes and lines since both have the same two components. We want this because
# __eq__ in both cases returns True when the things being compared refer to the
# same plane/line, even when component values are different, and here we want
# to compare component values too. Rather then require multiple lines for each
# comparison, we'll do it once here.
# This should ideally be in the Line and Plane classes, but they don't have a
# common parent or share utlity code (due to how the instructor implemented
# them and I don't want to complicate things now by adding something like that.)
def assertComponentsHaveSameValues(t, o1, o2):
    t.assertEqual(o1.normal_vector, o2.normal_vector)
    t.assertEqual(o1.constant_term, o2.constant_term)

class BasicOperationsTest(unittest.TestCase):
    # here im going to use the test cases provided with/by the course

    def test_can_swap_rows(self):
        p0 = Plane(Vector([1,1,1]), 1)
        p1 = Plane(Vector([0,1,0]), 2)
        p2 = Plane(Vector([1,1,-1]), 3)
        p3 = Plane(Vector([1,0,-2]), 2)

        s = LinearSystem([p0,p1,p2,p3])

        s.swap_rows(0,1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and
                        s[2] == p2 and s[3] == p3)

        s.swap_rows(1,3)
        self.assertTrue(s[0] == p1 and s[1] == p3 and
                        s[2] == p2 and s[3] == p0)

        s.swap_rows(3,1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and
                        s[2] == p2 and s[3] == p3)

    def test_can_multiply_coef_and_row(self):
        # like w/ the first and third tests, this one comes directly from the
        # course. note however that as this is defined it passes with a no-op
        # implementation for multiply_coefficient_and_row, because the Plane
        # __eq__ impl considers two planes that have diff coef and constant
        # terms but that reduce to the same plane/have the same points as equal.
        # to really test this then, we'd need probably to use some different -
        # perhaps poke further into the planes and validate coefficients and
        # constant term directly - and that's what I've added below w/ the
        # comparisons of normal vectors.
        # (It would also be better if we used assertEqual for each comparisons
        # instead of the assertTrue w/ the comparisons provided, at least because
        # that'd show us the actual values when we have a failure. I've done this
        # where I've added tests.)
        p0 = Plane(Vector([0,1,0]), 2)
        p1 = Plane(Vector([1,1,1]), 1)
        p2 = Plane(Vector([1,1,-1]), 3)
        p3 = Plane(Vector([1,0,-2]), 2)

        s = LinearSystem([p0,p1,p2,p3])

        s.multiply_coefficient_and_row(1,0)
        self.assertTrue(s[0] == p0 and s[1] == p1 and
                        s[2] == p2 and s[3] == p3)

        s.multiply_coefficient_and_row(-1,2)
        self.assertTrue((s[0] == p0 and
                         s[1] == p1 and
                         s[2] == Plane(Vector([-1,-1,1]), -3) and
                         s[3] == p3))
        assertComponentsHaveSameValues(self, s[0], p0)
        assertComponentsHaveSameValues(self, s[1], p1)
        assertComponentsHaveSameValues(self, s[2], Plane(Vector([-1,-1,1]), -3))
        assertComponentsHaveSameValues(self, s[3], p3)

        s.multiply_coefficient_and_row(10,1)
        self.assertTrue((s[0] == p0 and
                         s[1] == Plane(Vector([10,10,10]), 10) and
                         s[2] == Plane(Vector([-1,-1,1]), -3) and
                         s[3] == p3))
        assertComponentsHaveSameValues(self, s[0], p0)
        assertComponentsHaveSameValues(self, s[1], Plane(Vector([10,10,10]), 10))
        assertComponentsHaveSameValues(self, s[2], Plane(Vector([-1,-1,1]), -3))
        assertComponentsHaveSameValues(self, s[3], p3)

    def test_add_multiple_times_to_row(self):
        p0 = Plane(Vector([0,1,0]), 2)
        p1 = Plane(Vector([10,10,10]), 10)
        p2 = Plane(Vector([-1,-1,1]), -3)
        p3 = Plane(Vector([1,0,-2]), 2)

        s = LinearSystem([p0,p1,p2,p3])

        s.add_multiple_times_row_to_row(0,0,1)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], p1)
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)

        s.add_multiple_times_row_to_row(1,0,1)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], Plane(Vector(['10','11','10']), '12'))
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)
        assertComponentsHaveSameValues(self, s[0], p0)
        assertComponentsHaveSameValues(self, s[1], Plane(Vector(['10','11','10']), '12'))
        assertComponentsHaveSameValues(self, s[2], p2)
        assertComponentsHaveSameValues(self, s[3], p3)

        s.add_multiple_times_row_to_row(-1,1,0)
        self.assertEqual(s[0], Plane(Vector(['-10','-10','-10']), '-10'))
        self.assertEqual(s[1], Plane(Vector(['10','11','10']), '12'))
        self.assertEqual(s[2], p2)
        self.assertEqual(s[3], p3)
        assertComponentsHaveSameValues(self, s[0], Plane(Vector(['-10','-10','-10']), '-10'))
        assertComponentsHaveSameValues(self, s[1], Plane(Vector(['10','11','10']), '12'))
        assertComponentsHaveSameValues(self, s[2], p2)
        assertComponentsHaveSameValues(self, s[3], p3)

# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2):
#     print 'test case 1 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2 and
#         t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#         t[3] == Plane()):
#     print 'test case 3 failed'
#
# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
#     print 'test case 4 failed'



if __name__ == '__main__':
    unittest.main()
