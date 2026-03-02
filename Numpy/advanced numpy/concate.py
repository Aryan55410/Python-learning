"""
np.concatenate((a1, a2, ...), axis=0)

axis=0 : row-wise
axis=1 : column-wise
"""

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
new_arr = np.concatenate((arr1, arr2), axis=0)
print(new_arr)