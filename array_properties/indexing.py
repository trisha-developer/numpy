#indexing

import numpy as np
a=np.array([1,2,3,5,4,7])
print(a[2])
print(a[-1])
print(a[0])

output:
3
7
1

#slicing
"""
array[start:stop:step]
"""
import numpy as np

arr=np.array([10,20,30,40,50])
print(arr[1:3:1])

output: [20 30 40 50]


