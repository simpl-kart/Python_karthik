import matplotlib   ###adding these two lines as version compatibility issue is there
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy
y=numpy.random.randn(100,100)
plt.hist(y)
plt.savefig('histogram example')
plt.show()
