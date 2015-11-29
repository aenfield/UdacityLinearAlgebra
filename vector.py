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
        # would it be better to define a unary negative and then implement this as self + (-(v))? reduces duplication...

    # support vector * scalar (for ex, v*3)
    def __mul__(self, v):
        return Vector([v*x for x in self.coordinates])

    # we overload __rmul__ to support scalar * vector operations (for ex, 3*v)
    def __rmul__(self, v):
        return self * v  # implement by calling __mul__ here






if __name__ == '__main__':
    print(Vector([8.218,-9.341]) + Vector([-1.129,2.111]))
    print(Vector([7.119,8.215]) - Vector([-8.223,0.878]))
    print(7.41 * Vector([1.671,-1.012,-0.318]))
