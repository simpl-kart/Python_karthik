import numpy as np
arr = np.arange(20)
print arr
np.savetxt('test.txt',arr)
new_arr = np.loadtxt('test.txt')
print new_arr