#Reshape array
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print("a =\n",a)
a=a.reshape((2,3))
print("After Reshape =\n",a)

output:
a =
 [[1 2]
 [3 4]
 [5 6]]
After Reshape =
 [[1 2 3]
 [4 5 6]]


#from 3D to 1D dimension             
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print("a =\n",a)

flat=a.reshape(-1)
print("Flat = ",flat)

output:
a =
 [[1 2]
 [3 4]
 [5 6]]

Flate = [1 2 3 4 5 6]

#flatten() function

import numpy as np
b=np.array([[8,9,7],[1,2,3]])
b=b.flatten()
print(b)

output: [8 9 7 1 2 3]

#transpose array (inverse of the matrix)

import numpy as np
c=np.array([['t','r','i'],['s','h','a']])
print("C =\n",c)
c=c.T
print("C Transpose =\n",c)

output:
C =
 [['t' 'r' 'i']
 ['s' 'h' 'a']]
C Transpose =
 [['t' 's']
 ['r' 'h']
 ['i' 'a']]
