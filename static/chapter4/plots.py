import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
plt.plot(x, np.sqrt(1 - x**2))
plt.savefig("./ch4_plot1.png", bbox_inches='tight')
