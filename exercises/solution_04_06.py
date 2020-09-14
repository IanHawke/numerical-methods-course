import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1e-4, 10)
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, x**3)
axes[0].set_xlabel(r"$x$")
axes[1].loglog(x, x**3)
axes[1].set_xlabel(r"$x$")
