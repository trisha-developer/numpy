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


#fancy indexing
"""jis indexing pe jo value hongi vo print ho jayegi"""

import numpy as np

b=np.array([12,14,15,16,71])
print(b[[0,4,2]])

output: [12 71 15]


"""Boolean masking
filtering"""

import numpy as np

c=np.array([1,2,3,4,5,6,9])
print(c[c > 5])

output: [6 9]


