import numpy as np

arr = np.arange(20)
print(arr)
slice_arr = slice(1,10,2) #slice from 1 in 10 in array of 20 with 2 in diff which gives the output belowads
print arr[slice_arr]

#slicing items beginning with a specified index
print(arr[2:])
#slicing items until a specified index
print(arr[:15])

multiarr =np.array([[1,2,3],[4,5,6],[6,7,8]])
print(multiarr)
print(multiarr[0:2,0:3,])

###Numpy array attributes

print(multiarr.shape) #returns the shape of the array 3*3
print(multiarr.ndim) #dimension of the array - this is a 2D array
print(multiarr.itemsize) #length of each element in the array in bytes. ans will be 8 bytes

# Numpy array creation routines

x = np.empty([3,3],dtype=int)  #this will return random values.
print(x)