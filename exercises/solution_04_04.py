import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
plt.plot(x, np.sin(x), label=r"$\sin(x)$",
         linestyle='-', color='black')
plt.plot(x, np.cos(2 * x), label=r"$\cos(2x)$",
         linestyle='--', color='blue')
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.legend()
