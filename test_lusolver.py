import pytest
from module_lab2_task1 import *
from problems import *


def test_read_system_from_file():
    problem = LUSolver.read_system_from_file()