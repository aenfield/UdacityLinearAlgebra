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









if __name__ == '__main__':
    unittest.main()
