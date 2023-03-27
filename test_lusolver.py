import pytest
import os
import numpy as np
from module_lab2_task1 import *


# test for vector b
def test_read_system_from_file1():
    solver = LUSolver()
    solver.read_system_from_file(r'/Users/celinebui/Desktop/engsci233_lab2/233_lab2/problems/problem0.txt')
    b_test = [[-5], [20], [3]]
    assert (np.array(solver.vector_b).all() == np.array(b_test).all())


# test for matrix A
def test_read_system_from_file2():
    solver = LUSolver()
    solver.read_system_from_file(r'/Users/celinebui/Desktop/engsci233_lab2/233_lab2/problems/problem0.txt')
    matrix_a_test = [[2, -1, 3], [-8, 3, -8], [-2, -2, 7]]
    assert (np.array(solver.matrix_a).all() == np.array(matrix_a_test).all())


def test_write_sol_to_file():
    solver = LUSolver()
    file_path = r'/Users/celinebui/Desktop/engsci233_lab2/233_lab2/solutions'
    solver.vector_x = [[-2], [4], [1]]
    solver.write_solution_to_file(file_path)

    with open(file_path, 'r') as fp:
        line = fp.readline().strip()
        vector_x_test = np.zeros((3, 1), dtype='int32')
        count = 0
        while line != '':
            vector_x_test[count] = np.array(line)
            count += 1

    assert (np.array(vector_x_test).all() == np.array(solver.vector_x).all())
