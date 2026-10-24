#finding the shape of the array
#variable.shape
import numpy as np

a=np.array([[1,2,3],[3,2,1]])
print(a.shape)

output:
(2,3)

#finding the size of the array (total elements of the array)
#variable.size
import numpy as np
b=np.array([[7,8,9],[6,5,4]])
print(b.size)

output: 
6

#finding the dimensions of the array
#using ndim function

import numpy as np
c=np.array([[2,3,4],[1,3,4],[9,7,8]])
print(c.ndim)

output: 2

#finding the datatype of the array
#using dtype function

import numpy as np
d=np.array([[2.3,4.1,9.0]])
print(d.dtype)

output: float64

#converting datatype of the array
#using astype() method

import numpy as np
e=np.array([[1.2,3.2,3.1],[4.1,4.0,5.2]])
str_arr=e.astype(str)
print(str_arr)
print(str_arr.dtype)

output:
[['1.2' '3.2' '3.1']
 ['4.1' '4.0' '5.2']]
<U32

