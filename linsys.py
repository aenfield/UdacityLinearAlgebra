from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1_index, row2_index):
        self.planes[row1_index], self.planes[row2_index] = self.planes[row2_index], self.planes[row1_index]


    def multiply_coefficient_and_row(self, coefficient, row_index):
        self.planes[row_index] = self.planes[row_index].scaledBy(coefficient)

    # TODO looks like this, when given 0 for the coefficient should be adding
    # zero rows - i.e., not changing the row_to_be_added_to at all - rather
    # than what it's doing now
    def add_multiple_times_row_to_row(self, coefficient, row_to_add_index, row_to_be_added_to_index):
        plane_multiplied = self.planes[row_to_add_index].scaledBy(coefficient)
        self.planes[row_to_be_added_to_index] = self.planes[row_to_add_index].add(plane_multiplied)


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps



if __name__ == '__main__':
    # initial code provided with module
    p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
    p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
    p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

    s = LinearSystem([p0,p1,p2,p3])

    print(s.indices_of_first_nonzero_terms_in_each_row())
    print('{},{},{},{}'.format(s[0],s[1],s[2],s[3]))
    print(len(s))
    print(s)
    print()

    s[0] = p1
    print(s)
    print()

    print(MyDecimal('1e-9').is_near_zero())
    print(MyDecimal('1e-11').is_near_zero())
