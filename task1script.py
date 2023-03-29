import os
import shutil

import numpy as np
from module_lab2_task1 import *
from glob import glob

try:
    os.makedirs('solutions')
except OSError:
    print ('Create directory failed')

currentDirectory = os.getcwd()

counter = 0
match = glob(os.path.join(currentDirectory,'problems',f'problem{counter}*'))

while match != []:
    match = match[0]
    counterString = str(counter)
    solver = LUSolver()
    solver.read_system_from_file(match)
    solver.lu_solver()
    solver.forward_sub()
    solver.backward_sub()
    solver.write_solution_to_file(os.path.join(currentDirectory,'solutions','solutions'+counterString+'.txt'))
    counter = counter + 1
    match = glob(os.path.join(currentDirectory,'problems',f'problem{counter}*'))








