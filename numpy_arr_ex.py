import numpy as np

###########example for single dimensional numpy array and the difference between normal python array and a numpy is executed below
original_array = [1,2,3]
a = np.array(original_array)
print(a)
print(type(a))
print(original_array)
print(type(original_array))


###########multi dimensional array (the rows and columns should be same, other wise numpy will treat this as a single dimensional array

multidim = np.array([[1,2,3],[4,5,6]])
print(multidim)

zeroarr = np.zeros(8)  #zeros method in numpy to print a single dimensional array of 8 zweros
print zeroarr
arrangearr = np.arange(0,100)
print arrangearr

########restructuring a Numpy array

##how to convert a linear array of 8 elements into a 2*2*2 3D array

zeroarr = zeroarr.reshape(4,2)
print zeroarr
zeroarr = zeroarr.ravel(8)
print  zeroarr

#### Numpy array indexing ---identical to Python's indexing concept

element = arrangearr[6]
print element  ##THis will get the 7th element from arrangearr starting with zero
print(element + 7 )  #actually 7 is an integer and element is a numpy object. we can't do int and obj addition, but python is converting 7 into numpy obj and then adding it

