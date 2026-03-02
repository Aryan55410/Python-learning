"""
vertically 
horizontally

vstack() row wise
hstack() column wise

"""
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
new_arr_v = np.vstack((arr1, arr2))
new_arr_h = np.hstack((arr1, arr2))
print(new_arr_v)
print(new_arr_h)