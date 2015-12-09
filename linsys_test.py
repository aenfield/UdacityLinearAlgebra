import unittest

from linsys import LinearSystem
from plane import Plane
from vector import Vector

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
        # comparisons of normal vectors. (They could probably use some de-duplication.)
        # (It would also be better if we used assertEqual for each comparisons
        # instead of the assertTrue w/ the comparisons provided, at least because
        # that'd show us the actual values when we have a failure.)
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
        self.assertTrue((s[0].normal_vector == p0.normal_vector and
                         s[1].normal_vector == p1.normal_vector and
                         s[2].normal_vector == Plane(Vector([-1,-1,1]), -3).normal_vector and
                         s[3].normal_vector == p3.normal_vector))

        s.multiply_coefficient_and_row(10,1)
        self.assertTrue((s[0] == p0 and
                         s[1] == Plane(Vector([10,10,10]), 10) and
                         s[2] == Plane(Vector([-1,-1,1]), -3) and
                         s[3] == p3))
        self.assertTrue((s[0].normal_vector == p0.normal_vector and
                         s[1].normal_vector == Plane(Vector([10,10,10]), 10).normal_vector and
                         s[1].constant_term == Plane(Vector([10,10,10]), 10).constant_term and
                         s[2].normal_vector == Plane(Vector([-1,-1,1]), -3).normal_vector and
                         s[2].constant_term == Plane(Vector([-1,-1,1]), -3).constant_term and
                         s[3].normal_vector == p3.normal_vector))

    def test_add_multiple_times_to_row(self):
        p0 = Plane(Vector([0,1,0]), 2)
        p1 = Plane(Vector([10,10,10]), 10)
        p2 = Plane(Vector([-1,-1,1]), -3)
        p3 = Plane(Vector([1,0,-2]), 2)

        s = LinearSystem([p0,p1,p2,p3])

        s.add_multiple_times_row_to_row(0,0,1)
        self.assertEqual(s[0], p0)
        self.assertEqual(s[1], Plane(Vector(['10','10','10']), '10'))
        self.assertEqual(s[2], Plane(Vector(['-1','-1','1']), '-3'))
        self.assertEqual(s[3], p3)

        # TODO should update above to compare normal vectors and constant terms
        # explicitly, below to replace old code w/ indiv assertions, and optionally
        # overall here and all above to reduce duplication when comparing
        # normal vectors and constant terms explicitly 

        s.add_multiple_times_row_to_row(1,0,1)
        if not (s[0] == p1 and
                s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
                s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
                s[3] == p3):
            print('test case 8 failed')

        s.add_multiple_times_row_to_row(-1,1,0)
        if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
                s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
                s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
                s[3] == p3):
            print('test case 9 failed')




if __name__ == '__main__':
    unittest.main()
