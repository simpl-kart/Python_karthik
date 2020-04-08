import matplotlib   ###adding these two lines as version compatibility issue is there
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.pie([40,20,10],labels=['python','Java','C'])
plt.show()