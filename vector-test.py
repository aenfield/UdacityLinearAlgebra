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








if __name__ == '__main__':
    unittest.main()
