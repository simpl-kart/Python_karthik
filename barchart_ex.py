import matplotlib   ###adding these two lines as version compatibility issue is there
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.bar([1,2,3],[10,20,30])
plt.show()