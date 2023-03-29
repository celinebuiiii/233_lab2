# Python program to demonstrate
# glob using different wildcards
from module_lab2_task1 import *
from glob import glob
import os

currentDirectory = os.getcwd()
solver = LUSolver()

os.makedirs('Solutions')
counter = 0

for match in glob(os.path.join(currentDirectory, 'problems', '*problem*')):
    # if os.path.isdir(match):
    #    print(f'Directory {match} contains files:')
    #    dir_contents = glob(match+os.sep+'*')

    #    for content in dir_contents:
    #        if not os.path.isdir(content)

    counterString = str(counter)
    print(match)
    solver.read_system_from_file(match)
    solver.lu_solver()
    solver.forward_sub()
    solver.backward_sub()
    solver.write_solution_to_file(currentDirectory + 'Solutions' + 'solutions'+counterString+'.txt')

#

