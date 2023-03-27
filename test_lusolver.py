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
