import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
plt.plot(x, np.sin(x))
plt.xlabel(r"$x$")
plt.ylabel(r"$\sin(x)$")
plt.title("Titled plot")
plt.xlim(1, 8)
