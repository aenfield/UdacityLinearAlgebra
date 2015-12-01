import unittest

from vector import Vector

class AdditionTest(unittest.TestCase):

    def testPositiveAddition(self):
        v1 = Vector([1,2])
        v2 = Vector([3,4])

        self.assertEqual(Vector([4,6]), v1+v2)

    def testNegativeAddition(self):
        v1 = Vector([1,2])
        v2 = Vector([-5,-5])

        self.assertEqual(Vector([-4,-3]), v1+v2)


class SubtractionTest(unittest.TestCase):

    def testSubtraction(self):
        v1 = Vector([1,4])
        v2 = Vector([3,2])

        self.assertEqual(Vector([-2,2]), v1-v2)


class ScalarMultiplyTest(unittest.TestCase):

    def testPositiveScalarMultiplication(self):
        v1 = Vector([1,2])

        self.assertEqual(Vector([3,6]), v1*3)

    def testNegativeScalarMultiplication(self):
        v1 = Vector([2,4])

        self.assertEqual(Vector([-4,-8]), v1*-2)

    # here we test 3*v instead of v*3 (as above)
    def testScalarMultiplicationWithScalarFirst(self):
        v1 = Vector([1,2])

        self.assertEqual(Vector([3,6]), 3*v1)


class MagnitudeTest(unittest.TestCase):

    def testMagnitudeOfAVector(self):
        v1 = Vector([4,4])

        self.assertAlmostEqual(v1.magnitude(), 5.65685424949238)


class NormalizationTest(unittest.TestCase):

    def testNormalizationOfAVector(self):
        v1 = Vector([4,4])

        v1n = v1.normalized()

        self.assertAlmostEqual(v1n.coordinates[0], 0.7071067811865475)
        self.assertAlmostEqual(v1n.coordinates[1], 0.7071067811865475)
        self.assertAlmostEqual(v1n.magnitude(), 1)

    def testNormalizedHandlesZeroVectorWithException(self):
        v1 = Vector([0,0])

        with self.assertRaises(Exception) as context:
            v1.normalized()

        self.assertTrue('Cannot normalize the zero vector' in str(context.exception))

class DotProductTest(unittest.TestCase):

    def test_dot_product(self):
        v1 = Vector([1,2,-1])
        v2 = Vector([3,1,0])

        self.assertEqual(v1.dot(v2), 5)
        self.assertEqual(v2.dot(v1), 5)

    def test_dot_product_with_zero_vector(self):
        v1 = Vector([1,2,-1])
        v2 = Vector([0,0,0])

        self.assertEqual(v1.dot(v2), 0)
        self.assertEqual(v2.dot(v1), 0)


class AngleBetweenTest(unittest.TestCase):

    def test_angle_between(self):
        v1 = Vector([1,2,-1])
        v2 = Vector([3,1,0])

        self.assertAlmostEqual(v1.angleBetween(v2), 0.87, places=2)
        self.assertAlmostEqual(v1.angleBetween(v2, degrees=True), 50, places=0)

    def test_angle_between_with_zero_vector(self):
        v1 = Vector([1,2,-1])
        v2 = Vector([0,0,0])

        with self.assertRaises(Exception) as context:
            v1.angleBetween(v2)

        self.assertTrue('Cannot calculate the angle between using a zero vector' in str(context.exception))


class ParallelAndOrthogonalBooleans(unittest.TestCase):

    def test_parallel_boolean(self):
        # v1, v2, v3, and of course v0 are all parallel;
        # v4 is not parallel to v1, v2, or v3 but is parallel to v0
        v1 = Vector([1,1])
        v2 = Vector([-1,-1])
        v3 = Vector([2,2])
        v4 = Vector([1,0])
        v0 = Vector([0,0])

        self.assertTrue(v1.parallelTo(v2))
        self.assertTrue(v2.parallelTo(v1))
        self.assertTrue(v1.parallelTo(v3))
        self.assertTrue(v3.parallelTo(v1))
        self.assertTrue(v1.parallelTo(v0))

        self.assertTrue(v0.parallelTo(v1))
        self.assertTrue(v2.parallelTo(v0))
        self.assertTrue(v0.parallelTo(v2))
        self.assertTrue(v3.parallelTo(v0))
        self.assertTrue(v0.parallelTo(v3))

        self.assertFalse(v1.parallelTo(v4))
        self.assertFalse(v2.parallelTo(v4))
        self.assertFalse(v3.parallelTo(v4))
        self.assertTrue(v0.parallelTo(v4))

    def test_orthogonal_boolean(self):
        # v1 and v2 are not orthogonal, v2 is orthogonal to v1 and v2,
        # v0 is orthogonal to v1, v2, and v3
        v1 = Vector([1,1])
        v2 = Vector([-1,-1])
        v3 = Vector([-1,1])
        v0 = Vector([0,0])

        self.assertFalse(v1.orthogonalTo(v2))
        self.assertFalse(v2.orthogonalTo(v1))
        self.assertTrue(v1.orthogonalTo(v3))
        self.assertTrue(v3.orthogonalTo(v1))
        self.assertTrue(v2.orthogonalTo(v3))
        self.assertTrue(v3.orthogonalTo(v2))

        self.assertTrue(v0.orthogonalTo(v1))
        self.assertTrue(v0.orthogonalTo(v2))
        self.assertTrue(v0.orthogonalTo(v3))
        self.assertTrue(v1.orthogonalTo(v0))
        self.assertTrue(v2.orthogonalTo(v0))
        self.assertTrue(v3.orthogonalTo(v0))

        # check that we handle FP rounding too - this is orthogonal, but
        # if we don't handle rounding we'll say it's not
        v4 = Vector([-2.328,-7.284,-1.214])
        v5 = Vector([-1.821,1.072,-2.94])
        self.assertTrue(v4.orthogonalTo(v5))
        self.assertTrue(v5.orthogonalTo(v4))

    def test_iszero_boolean(self):
        self.assertTrue(Vector([0,0]).isZero())
        self.assertFalse(Vector([1,1]).isZero())

class ProjectingVectors(unittest.TestCase):

    def test_projection_onto_basis_vector(self):
        v = Vector([1,1])
        b = Vector([5,0])

        self.assertEqual(v.projectedOnTo(b), Vector([1,0]))

    def test_component_orthogonal_to_basis(self):
        v = Vector([1,1])
        b = Vector([5,0])

        self.assertEqual(v.componentOrthogonalTo(b), Vector([0,1]))        



if __name__ == '__main__':
    unittest.main()
