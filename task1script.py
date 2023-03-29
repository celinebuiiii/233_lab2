import os
import shutil

import numpy as np
from module_lab2_task1 import *
from glob import glob

import os

try:
    os.makedirs('solutions')
except OSError:
    print ('Create directory failed')

currentDirectory = os.getcwd()

counter = 0

for match in glob('problems*'):
    if os.path.isdir(match):
        for file in glob ('problem*'):
            solver = LUSolver()
            solver.read_system_from_file(file)
            solver.lu_factors()
            solver.forward_sub()
            solver.backward_sub()
            solver.write_solution_to_file(currentDirectory+os.sep+'solutions')
    break








