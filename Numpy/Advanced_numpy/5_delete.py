"""
np.delete(array,index,axis = none)
flatten array
"""

import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,100])
new_arr = np.delete(arr,3)
print(new_arr)
