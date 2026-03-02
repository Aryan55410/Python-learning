"""
np.split()
equal

np.hsplit()
np.vsplit()
"""
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
new_arr = np.split(arr, 2)
print(new_arr)