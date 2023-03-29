import numpy as np
from glob import glob

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

        METHODS:
        -------
        read_system_from_file
            Read a system of linear equations from a file along with vector b.
        lu_factors
            Perform row subtraction / Gaussian elimination for matrixes L and U.
        forward_sub
            Calculates vector y using Ly = b
        backward_sub
            Calculates solution vector v using Ux = y
        write_solution_to_file
            Write solution vector x into a solution file in the solutions folder

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
        """
            Write object's vector_x attribute to a file, with each value of vector x on a new line.

                Arguments:
                    f_path: str
                        path to file where vector_x will be stored

                Notes:
                    Method has no output.
                """
        with open(f_path, 'r') as fp:
            # get number of unknowns
            line = np.array(fp.readline().strip())
            n = np.array(line)

            # initialise zeroes arrays
            size = int(n)
            self.matrix_a = np.zeros((size, size))
            self.vector_b = np.zeros((size, 1))

            # get the next line of matrix
            line = fp.readline().strip()

            # loop through the next n lines to get matrix A
            j = 0
            while line != '':
                if j < size:
                    a_values = line.split(',')
                    self.matrix_a[int(j)] = np.array(a_values)
                    j += 1

                else:
                    b_vector = line.strip()
                    self.vector_b[j - size] = np.array(b_vector)
                    j += 1

                line = fp.readline().strip()

    # Method 2
    def lu_solver(self):
        """
        Uses row substitution to update the arrays' matrix_u and matrix_l for Gaussian Elimination.

        Notes:
        --------
            This method has no inputs or outputs. The purpose of this function is to simply update matrix_l and
            matrix_u from the attribute matrix A of the object.

        """

        # Receive the number of rows and columns in the matrix_a using .shape
        rows = self.matrix_a.shape[0]
        cols = self.matrix_a.shape[1]
        # There is no need to find the number of columns as it is the same as the number of rows. However will make the
        # function easier to follow

        # Setting up the matrix_u and matrix_l for LU factorisation
        self.matrix_u = self.matrix_a.copy()
        self.matrix_l = np.eye(rows, cols)
        # matrix_u is a copy of matrix_a
        # matrix_l is set up as an array with ones running diagonally. Made with .eye

        for i in range(rows):
            # Setting pivot point for the first column to use during the row subtraction operations. With two for loops,
            # the row subtraction operations can happen within the first row until the end before moving on to the next
            # column for the next row subtraction
            pivot_point = self.matrix_u[i, i]
            for j in range(i + 1, cols):
                # Finding the value of the elements under the pivot points to be put in the matrix_l
                self.matrix_l[j, i] = self.matrix_u[j, i] / pivot_point
                self.matrix_u[j] = self.matrix_u[j] - self.matrix_l[j, i] * self.matrix_u[i]

    # Method 4
    def backward_sub(self):
        """
        Calculates the solutions to the x vector using backwards substitution (Ux = y)
        --------

        Notes:
            Does not have any inputs or outputs, it just updates the vector_x attribute.

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

            self.vector_x[size - i] = (self.vector_y[size - i]-sum) / self.matrix_u[size - i, size - j]

    # Method 3
    def forward_sub(self):
        """
        Calculates y vector from Ly=b using forwards substitution

        Notes:
            Method has no inputs our outputs. Only updates the vector_y attributes of object
        """

        # getting the size of the matrix l
        size = len(self.matrix_l)

        # vector_y is an array of zeros of size+1 rows and 1 column
        self.vector_y = np.zeros((size, 1))

        # nested for loop that calculates the values of each y and puts them into the vector_y
        # array replacing the zeros
        for i in range(0, size):
            sum = 0

            # for loop multiplies all calculated y values with its corresponding L value, so that we
            # can use it to calculate the next y value
            # range function automatically goes from 0 to i-1
            for j in range(0, i):
                # sum is a variable that stores the sum of the products of the matrix_l and
                # the corresponding values of the vector_y
                sum = sum + self.matrix_l[i, j] * self.vector_y[j]

            # calculates the value for each row of vector_y
            self.vector_y[i] = (self.vector_b[i] - sum) / self.matrix_l[i, i]

    def write_solution_to_file(self, f_path):
        """
        Write object's vector_x attribute to a file, with each value of vector x on a new line.

        Arguments:
            f_path: str
                path to file for writing vector_x

        Notes:
            Method has no output.
        """
        with open(f_path, 'w') as fp:
            n = len(self.vector_x)

            count = 0
            # loop through vector x
            while count < n:
                write_val = str(self.vector_x[count])
                fp.write(f"{write_val.strip('[]')}\n")
                count += 1

            # blank line at end of file
            if count == n:
                fp.write(f"")
