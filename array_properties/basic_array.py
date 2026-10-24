#1D array

import numpy
a=numpy.array([1,2])
print(a)


#2D array

import numpy as np
b=np.array([[1,2,3],[4,5,6]])
print(b)

#with default values
#np.zeros(shape) (3), etc...

import numpy as np
c=np.zeros(3)
print(c)

output: [0. 0. 0.]

#ones (shape)
import numpy as np
d=np.ones((2,3))
print(d)

output: [[1. 1. 1.]
 [1. 1. 1.]]


#full function(shape, value)

import numpy as np
e=np.full((3,3),7)  #7 is default value
print(e)

output: 
[[7 7 7]
 [7 7 7]
 [7 7 7]]


#creating sequences of numbers in numpy
#arange(start,stop,step)

import numpy as np
f=np.arange(0,10,2)
print(f)

output: [0 2 4 6 8]

#creating identity matrix
#eye(size)

import numpy as np
g=np.eye(3)
print(g)

output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

