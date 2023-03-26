import numpy as np
# additional imports here


class LUSolver(object):
    def __init__(self):
        self.matrix_a = None
        self.matrix_l = None
        self.matrix_u = None
        self.vector_b = None
        self.vector_x = None
        self.vector_y = None

    def read_system_from_file(self, f_path):
        with open(f_path, 'r') as fp:
            # get number of unknowns
            n = fp.readline()
            line = fp.readline().strip()

            # loop thru the next n lines to get matrix A
            count = 1
            while count <= n:
                a_values = line.split(',')
                self.matrix_a.append(float(a_values))
                count += 1
                line = fp.readline().strip()

            # after looping for matrix A finishes
            # loop thru the rest till end line
            while line != '':
                b_values = line.strip()
                self.vector_b.append(float(b_values))
                line = fp.readline().strip()