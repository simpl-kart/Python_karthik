import matplotlib   ###adding these two lines as version compatibility issue is there
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy
#plt.plot([1,2,3,4])
#plt.show()
x = numpy.arange(5)
print x
plt.plot(x,[x1**2 for x1 in x], label='square')
plt.plot(x,[x1**3 for x1 in x], label ='cube')
plt.plot(x, [x1**4 for x1 in x],label = 'power of 4')
plt.title("Learning Matplotlib")
plt.legend()
plt.grid(True)
plt.savefig('plot.png')
plt.show()
