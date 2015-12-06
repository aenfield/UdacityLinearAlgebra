import math
from decimal import Decimal, DivisionUndefined

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        return Vector([Decimal(scalar)*x for x in self.coordinates])

    # we overload __rmul__ to support scalar * vector operations (for ex, 3*v)
    def __rmul__(self, scalar):
        return self * scalar  # implement by calling __mul__ here

    # implement indexing by passing through using the coordinates member
    def __getitem__(self, index):
        return self.coordinates[index]

    def magnitude(self):
        # magnitude is the sqrt of each component squared (this is the normal formula
        # for distance, but since the second component is the origin, we subtract
        # zero)
        return (sum([x**2 for x in self.coordinates])).sqrt()

    def normalized(self):
        # the normalization of a vector is another vector w/ the same direction and
        # magnitude of one - to get this we multiply the vector in question by
        # one over the magnitude of the vector - i.e., we scale it larger/smaller
        # so that its length is one (remember that scaling doesn't change the
        # direction)
        try:
            return (Decimal('1.0')/self.magnitude()) * self
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        # the dot product is the sum of the corresponding components multiplied together
        return sum([(x*y) for (x,y) in zip(self.coordinates, v.coordinates)])

    def angleBetween(self, v, degrees=False):
        if (not(self.isZero()) and not(v.isZero())):
            radians_between = math.acos((self.dot(v)) / (self.magnitude() * v.magnitude()))
        else:
            raise Exception('Cannot calculate the angle between using a zero vector')

        return radians_between if not degrees else math.degrees(radians_between)

    def parallelTo(self, v):
        # the class-defined definition of parallel is where two vectors are scalar
        # multiples of each other - I implement by seeing if the angle between
        # the two vector is either 0 or 180 degrees
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

    def projectedOnTo(self, b):
        magnitude_of_projection = self.dot(b.normalized())
        return magnitude_of_projection * b.normalized()
        # his impl catches attempts to to normalize the zero vector and raises an exception

    def componentOrthogonalTo(self, b):
        # since v = v parallel + v orthogonal, then
        # v orthogonal = v - v parallel, which we use here:
        return self - self.projectedOnTo(b) # self.projectedOnTo(b) is v parallel
        # his impl catches the exception his impl raises in projectedOnTo

    def cross(self, v):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates

        return Vector([
            (y1*z2 - y2*z1),
            (-(x1*z2 - x2*z1)),
            (x1*y2 - x2*y1)
        ])

    def cross_parallelogram_area(self, v):
        return (self.cross(v).magnitude())

    def cross_triangle_area(self, v):
        return Decimal('0.5') * self.cross_parallelogram_area(v)

    # TODO generally: I updated this to use Decimal only when required by
    # Line. The entire class could use some cleanup in what's returned I think
    # and the use of isclose and tolerance manually (which were needed when we
    # used floats, but aren't needed now?)



if __name__ == '__main__':
    # here we're using the implemented functions to output the results of the
    # questions asked by the course

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
    print()

    print(Vector([3.039,1.879]).projectedOnTo(Vector([0.825,2.036])))
    print(Vector([-9.88,-3.264,-8.159]).componentOrthogonalTo(Vector([-2.155,-9.353,-9.473])))
    v = Vector([3.009,-6.172,3.692,-2.51])
    b = Vector([6.404,-9.144,2.759,8.718])
    print(v.projectedOnTo(b))
    print(v.componentOrthogonalTo(b))
    print()

    print(Vector([8.462,7.893,-8.187]).cross(Vector([6.984,-5.975,4.778])))
    print(Vector([-8.987,-9.838,5.031]).cross_parallelogram_area(Vector([-4.268,-1.861,-8.866])))
    print(Vector([1.5,9.547,3.691]).cross_triangle_area(Vector([-6.007,0.124,5.772])))
