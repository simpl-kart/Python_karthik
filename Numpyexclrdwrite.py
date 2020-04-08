import numpy as np
arr = np.array([[1,2],[3,4]])
print arr
np.savetxt('test.csv',arr, delimiter=',')   #it is best to use the delimiter with comma

#getting the data back from the csv file

new_arr = np.genfromtxt('test.csv',delimiter=',')
print new_arr
