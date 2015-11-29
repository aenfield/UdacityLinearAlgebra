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
