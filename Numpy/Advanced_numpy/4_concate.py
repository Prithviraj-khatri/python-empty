"""
np.concanate((array1,array2),axis = 0)

axis 0 > vertical stacking 
axis 1 > horizontal stacking
"""

import numpy as np
arr_1 = ([1,2,3])
arr_2 = ([4,5,6])

new_arr = np.concat((arr_1,arr_2))
print(new_arr)