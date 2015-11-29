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









if __name__ == '__main__':
    unittest.main()
