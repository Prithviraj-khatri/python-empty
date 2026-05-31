# change data type 

import numpy as np

arr = np.array([1.2,2.3,3.4])
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)
