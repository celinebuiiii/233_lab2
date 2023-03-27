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

    def backward_sub(self):
        """
        Calculates the solutions to the x vector using backwards substitution (Ux = y)

        --------

        Notes:
        Does not have any inputs or outputs, it just updates the vector x attribute.

    `   """

        # self.vector_x = np.linalg.solve(self.matrix_u, self.vector_y)

        size = len(self.matrix_u) - 1
        # Assigning the x vector to all zeros in order to do calculations with it
        self.vector_x = np.zeros((size + 1, 1))

        # For loop to index every row
        for i in range(0, size + 1):
            j = 0
            sum = 0
            # While loop multiplies every previously calculated x value with its corresponding u matrix value in
            # order to calculate the next x value. The loop breaks when the next u matrix value is a 0 or its reached
            # the end of the row.
            while (self.matrix_u[size - i, size - 1 - j] != 0) and (j != size):
                sum = sum + self.vector_x[size - j] * self.matrix_u[size - i, size - j]
                j = j + 1
            # Finally, the x value is calculated by summing the previous while loop sum and the y value for that
            # row. Then everything is divided by the u matrix value for the corresponding x variable.
            self.vector_x[size - i] = (sum + self.vector_y[size - i]) / self.matrix_u[size - i, size - j]
