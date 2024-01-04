#Access moudles
from math import pi
import sys
import random as rdm
from enum import Enum
import test_module
import rps

print(pi)

# for item in dir(rdm):

#     print(item)

test_module.start()

print(__name__)
print(test_module.__name__)

rps.rock_paper_scissors()
