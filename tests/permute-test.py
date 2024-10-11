import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from permutation import *

elements = [1,2,3,4]
print(permute(elements))
print('')
print(permute(elements,3))

print('')

elements = ['+','-','*','/']
print(permute_with_repetition(elements))
print('')
print(permute_with_repetition(elements,3))
