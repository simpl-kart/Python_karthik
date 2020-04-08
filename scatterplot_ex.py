import matplotlib   ###adding these two lines as version compatibility issue is there
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy
x=numpy.random.randn(100)
y=numpy.random.randn(100)
plt.scatter(x,y)
plt.show()