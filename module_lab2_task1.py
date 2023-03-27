import numpy as np
# additional imports here


class LUSolver(object):
    """
        Object representing a system of linear questions.

        Attributes:
        -----------
        matrix_a : NumPy array
            unique identifier for the starting matrix A.
        matrix_l : NumPy array
            unique identifier for the matrix L.
        matrix_u : NumPy array
            unique identifier for the matrix U.
        vector_b : NumPy array
            unique identifier for the starting vector b.
        vector_x : NumPy array
            unique identifier for the vector x.
        vector_y : NumPy array
            unique identifier for the vector y.
    """
    def __init__(self):
        self.matrix_a = None
        self.matrix_l = None
        self.matrix_u = None
        self.vector_b = None
        self.vector_x = None
        self.vector_y = None

    def __repr__(self):
        return f'LU factorisation for {self.matrix_a} with {self.vector_b}:' \
               f'L matrix: {self.matrix_l}' \
               f'U matrix: {self.matrix_u}' \
               f'Ly = b gives a y-vector of: {self.vector_y}' \
               f'Ux = y gives a solution x-vector of: {self.vector_x}'

    # method 1
    def read_system_from_file(self, f_path):
        with open(f_path, 'r') as fp:
            # get number of unknowns
            n = int(fp.readline().strip())

            # initialise zeroes arrays
            self.matrix_a = np.zeros((n, n), dtype='int32')
            self.vector_b = np.zeros((n, 1), dtype='int32')
            line = fp.readline().strip()

            # loop through the next n lines to get matrix A
            count = 0
            while line != '':
                if count < n:
                    a_values = line.split(',')
                    self.matrix_a[count] = np.array(a_values)
                    count += 1

                else:
                    b_vector = line.strip()
                    self.vector_b[count-n] = np.array(b_vector)
                    count += 1

                line = fp.readline().strip()

    def write_solution_to_file(self, f_path):
        with open(f_path, 'w') as fp:
            n = self.vector_x.shape[0]

            count = 0
            while count < n:
                fp.write(f"{self.vector_x[count]}\n")

            if count == n:
                fp.write(f"")