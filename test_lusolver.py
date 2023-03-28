import pytest
import os
import numpy as np
from module_lab2_task1 import *


# test for vector b
def test_read_system_from_file1():
    solver = LUSolver()
    solver.read_system_from_file(r'/Users/celinebui/Desktop/engsci233_lab2/233_lab2/problems/problem0.txt')
    b_test = np.array([[-5], [20], [3]])
    test_var = np.array((solver.vector_b == b_test).all())
    assert (test_var == 1)


# test1 for matrix A
def test_read_system_from_file2():
    # expected a return of true (two matrix are the same)
    solver = LUSolver()
    solver.read_system_from_file(r'/Users/celinebui/Desktop/engsci233_lab2/233_lab2/problems/problem0.txt')
    matrix_a_test = [[2, -1, 3], [-8, 3, -8], [-2, -2, 7]]
    test_var = np.array((solver.matrix_a == matrix_a_test).all())
    assert (test_var == 1)


# test2 for matrix A
def test_read_system_from_file3():
    # expected a return of false (two matrix are not the same)
    solver = LUSolver()
    solver.read_system_from_file(r'/Users/celinebui/Desktop/engsci233_lab2/233_lab2/problems/problem0.txt')
    matrix_a_test = [[0, -1, 3], [-8, 0, -8], [-2, -2, 1]]
    test_var = np.array((solver.matrix_a == matrix_a_test).all())
    assert (test_var == 0)


def test_backward_sub():
    tester = LUSolver()
    tester.matrix_u = np.array([[2, -1, 3], [0, -1, 4], [0, 0, -2]])
    tester.vector_y = np.array([-5, 0, -2])
    tester.backward_sub()
    x_testvalue = np.array([[-2], [4], [1]])
    testValue = (tester.vector_x == x_testvalue).all()
    assert (testValue == 1)


def test_forward_sub():
    solver = LUSolver()
    solver.matrix_l = np.array([[1, 0, 0], [-4, 1, 0], [-1, 3, 1]])
    solver.vector_b = np.array([-5, 20, 3])
    solver.forward_sub()
    correct_y = np.array([[-5], [0], [-2]])
    testValue = (solver.vector_y == correct_y).all()
    assert (testValue == 1)


def test_write_sol_to_file():
    solver = LUSolver()
    file_path = r'/Users/celinebui/Desktop/engsci233_lab2/233_lab2/method5_test.txt'
    solver.vector_x = np.array([[-2], [4], [1]])
    # write solution to file in column
    solver.write_solution_to_file(file_path)

    # open the newly created file in read mode to check for written data
    with open(file_path, 'r') as fp:
        line = fp.readline().strip()
        vector_x_test = np.zeros((3, 1), dtype='int32')

        count = 0
        while line != '':
            vector_x_test[count, 0] = np.array(line)
            count += 1
            line = fp.readline().strip()

    test_var = (vector_x_test == solver.vector_x).all()
    assert (test_var == 1)

