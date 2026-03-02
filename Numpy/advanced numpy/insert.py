"""
numpy.insert(array, index, values, axis=None)
array-original array
index - 
value-
axis-
axis = 0 , row-wise
1 column wise
"""

import numpy as np
arr = np.array([10, 20, 30, 40, 50])

new_arr = np.insert(arr, 2, 25)
print(new_arr)  # 