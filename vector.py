import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def __add__(self, v):
        # when applied to tuples, + concatenates, so we need to
        # zip the two tuples together and add the results
        return Vector([x+y for (x,y) in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([x-y for (x,y) in zip(self.coordinates, v.coordinates)])
        # would it be better to define a unary negative and then implement this as
        # self + (-(v))? reduces duplication...

    # support vector * scalar (for ex, v*3)
    def __mul__(self, scalar):
        return Vector([scalar*x for x in self.coordinates])

    # we overload __rmul__ to support scalar * vector operations (for ex, 3*v)
    def __rmul__(self, scalar):
        return self * scalar  # implement by calling __mul__ here

    def magnitude(self):
        # magnitude is the sqrt of each component squared (this is the normal formula
        # for distance, but since the second component is the origin, we subtract
        # zero)
        return math.sqrt(sum([x**2 for x in self.coordinates]))

    def normalized(self):
        # the normalization of a vector is another vector w/ the same direction and
        # magnitude of one - to get this we multiply the vector in question by
        # one over the magnitude of the vector - i.e., we scale it larger/smaller
        # so that its length is one (remember that scaling doesn't change the
        # direction)
        try:
            return (1/self.magnitude()) * self
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        # the dot product is the sum of the corresponding components multiplied together
        return sum([(x*y) for (x,y) in zip(self.coordinates, v.coordinates)])

    def angleBetween(self, v, degrees=False):
        try:
            radians_between = math.acos((self.dot(v)) / (self.magnitude() * v.magnitude()))
        except ZeroDivisionError:
            raise Exception('Cannot calculate the angle between using a zero vector')

        return radians_between if not degrees else math.degrees(radians_between)

    def parallelTo(self, v):
        # the class-defined definition of parallel is where two vectors are scalar
        # multiples of each other - I wasn't sure how to implement this simply,
        # and the instructor didn't implement it this way either...
        return (self.isZero() or v.isZero() or
                math.isclose(self.angleBetween(v), 0, abs_tol=1e-05) or
                math.isclose(self.angleBetween(v), math.pi, rel_tol=1e-05))

    def orthogonalTo(self, v, tolerance=1e-10):
        # can't just do self.dot(v) == 0 due to FP rounding issues
        return abs(self.dot(v)) < tolerance
        # TODO update to use math.isclose?

    def isZero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
        # TODO update to use math.isclose?

if __name__ == '__main__':
    print(Vector([8.218,-9.341]) + Vector([-1.129,2.111]))
    print(Vector([7.119,8.215]) - Vector([-8.223,0.878]))
    print(7.41 * Vector([1.671,-1.012,-0.318]))
    print()

    print(Vector([-0.221,7.437]).magnitude())
    print(Vector([8.813,-1.331,-6.247]).magnitude())
    print(Vector([5.581,-2.136]).normalized())
    print(Vector([1.996,3.108,-4.554]).normalized())
    print()

    print(Vector([7.887,4.138]).dot(Vector([-8.802,6.776])))
    print(Vector([-5.955,-4.904,-1.874]).dot(Vector([-4.496,-8.755,7.103])))
    print(Vector([3.183,-7.627]).angleBetween(Vector([-2.668,5.319])))
    print(Vector([7.35,0.221,5.188]).angleBetween(Vector([2.751,8.259,3.985]), degrees=True))
    print()

    v1 = Vector([-7.579,-7.88])
    w1 = Vector([22.737,23.64])
    print(v1.parallelTo(w1), v1.orthogonalTo(w1))
    v2 = Vector([-2.029,9.97,4.172])
    w2 = Vector([-9.231,-6.639,-7.245])
    print(v2.parallelTo(w2), v2.orthogonalTo(w2))
    v3 = Vector([-2.328,-7.284,-1.214])
    w3 = Vector([-1.821,1.072,-2.94])
    print(v3.parallelTo(w3), v3.orthogonalTo(w3))
    v4 = Vector([2.118,4.827])
    w4 = Vector([0,0])
    print(v4.parallelTo(w4), v4.orthogonalTo(w4))
