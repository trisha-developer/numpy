# Create a 1D NumPy array of numbers from 0 to 9
import numpy as np
a=np.arange(10)
print(a)

output:
[0 1 2 3 4 5 6 7 8 9]

# Convert 1D array to 2D
import numpy as np
a = np.arange(6)
print("a = ",a)
print("Dimension = ",a.ndim)
a2=a.reshape(3,2)
print("Dimension of the array after reshaping = ",a2.size)

output:
a =  [0 1 2 3 4 5]
Dimension =  1
Dimension of the array after reshaping =  6

"""
Exercise 3: Print Array Attributes
Instructions: Print the following attributes of the array:

The shape of the array.
The number of array dimensions.
The size of each element in bytes.
"""
import numpy as np
my_array=np.array([[1,2],[3,4],[5,6],[7,8]], dtype=np.uint16)
print("Shape of the array = ",my_array.shape)
print("Dimension of the array = ",my_array.ndim)
print("Size of each element of the array = ",my_array.itemsize)

output: 
Shape of the array =  (4, 2)
Dimension of the array =  2
Size of each element of the array =  2


