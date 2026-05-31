"""
np.insert(array,index,value,asix=none)

"""

import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr)
new_arr = np.insert(arr,3,35)
print(new_arr)