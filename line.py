from decimal import Decimal, getcontext, DivisionByZero

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'
    NO_INTERSECTIONS_NOT_COINCIDENT = 'No intersection - lines are parallel and not coincident'
    INFINITE_INTERSECTIONS_COINCIDENT = 'Infinite intersections - lines are coincident'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def __eq__(self, l):
        return self.coincidentTo(l)

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def parallelTo(self, line):
        return self.normal_vector.parallelTo(line.normal_vector)

    def coincidentTo(self, line):
        # TODO include logic to handle when normal vector is zero - 1:40 in 'coding functions for lines - solution'

        # first, coincident lines - equal lines - have to be parallel
        if not self.parallelTo(line):
            return False

        # then, a vector connecting one point on one line to a point on the
        # other line must be orthogonal to the lines' normal vectors
        p_on_self = self.pointOnLine()
        p_on_line = line.pointOnLine()

        v_joining_lines = Vector(p_on_self) - Vector(p_on_line)

        return (v_joining_lines.orthogonalTo(self.normal_vector.normalized()))
        # TODO what if the x-coord of the normal vector is zero? have to do it
        # the other direction w/ y? is this generalizable? seems like the logic
        # getting a point on each line should be in its own function, which could
        # be tested in isolation and could abstract the vertical/horizontal thing

    # return a point on the line - this is currently used for coincidentTo, which
    # doesn't need any particular point, so we do the easy thing and set one
    # dimension to zero and return the result (we still have to complicated things
    # by handling vertical and horizontal lines)
    # Later: I could have just used line.basepoint - :-(
    def pointOnLine(self):
        # horizontal lines have a normal vector with 0 for the x component
        if self.normal_vector[0] != 0:
            # not a horizontal line, and we'll return the point on the x-axis
            return ( (self.constant_term / self.normal_vector[0]), 0)
        else:
            # it's a horizontal line, so we'll return the point on the y-axis
            return (0, (self.constant_term / self.normal_vector[1]) )

    def intersectionWith(self, line):
        if self.coincidentTo(line):
            # same line, return self
            return self
        elif self.parallelTo(line):
            # parallel but not same line, so no intersections, return None
            return None
        else:
            # since it's not the same line or a parallel line, we have to have
            # one intersection, with these coordinates:
            a, b = self.normal_vector
            c, d = line.normal_vector
            k1, k2 = self.constant_term, line.constant_term
            denominator = (a*d) - (b*c)
            return ( ( ((d*k1) - (b*k2)) / denominator),
                     ( (-(c*k1) + (a*k2)) / denominator) )


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps



if __name__ == '__main__':
    # here we're using the implemented functions to output the results of the
    # questions asked by the course

    l1 = Line(Vector([4.046,2.836]), 1.21)
    l2 = Line(Vector([10.115,7.09]), 3.025)
    print(l1.intersectionWith(l2))

    l1 = Line(Vector([7.204,3.182]), 8.68)
    l2 = Line(Vector([8.172,4.114]), 9.883)
    print(l1.intersectionWith(l2))

    l1 = Line(Vector([1.182,5.562]), 6.744)
    l2 = Line(Vector([1.773, 8.343]), 9.525)
    print(l1.intersectionWith(l2))
