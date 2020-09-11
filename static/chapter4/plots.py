import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

x = np.linspace(0, 1)
plt.plot(x, np.sqrt(1 - x**2))
plt.savefig("./ch4_plot1.png", bbox_inches='tight')

plt.clf()

plt.plot(x, np.sqrt(1 - x**2), label=r"$\sqrt{1-x^2}$")
plt.title("The integrand")
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.legend()
plt.savefig("./ch4_plot1_labeled.png", bbox_inches='tight')

plt.clf()

plt.plot(x, np.sqrt(1 - x**2))
plt.xlim(0, 1)
plt.ylim(-0.1, 1.1)
plt.savefig("./ch4_plot1_scales.png", bbox_inches='tight')

plt.clf()

plt.plot(x, np.sqrt(1 - x**2), label=r"$\sqrt{1-x^2}$",
         linestyle='-', color='black')
plt.plot(x, x**2, label=r"$x^2$",
         linestyle='--', color='green', marker='x')
plt.legend()
plt.savefig("./ch4_plot1_multiple.png", bbox_inches='tight')

plt.clf()

x = np.linspace(1e-4, 1)
plt.loglog(x, x**2, label=r"$x^2$",
         linestyle='-', color='black')
plt.loglog(x, x**4, label=r"$x^4$",
         linestyle='--', color='green')
plt.legend()
plt.savefig("./ch4_plot1_loglog.png", bbox_inches='tight')

plt.clf()

x = np.linspace(0, 1)
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(x, np.sin(10*x))
axes[1].plot(x, np.cos(15*x))
plt.savefig("./ch4_plot2_subplots.png", bbox_inches="tight")

plt.clf()

fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(x, np.sin(10*x))
axes[0].set_xlim(0, 1)
axes[0].set_title("Sine and cosine")
axes[1].plot(x, np.cos(15*x))
axes[1].set_xlabel(r"$x$")
axes[1].set_ylabel(r"$\cos(15x)$")
plt.savefig("./ch4_plot2_subplots_labels.png", bbox_inches="tight")

plt.clf()

fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(x, np.sin(10*x))
axes[0].set_xlabel(r"$x$")
axes[1].plot(x, np.cos(15*x))
axes[1].set_xlabel(r"$x$")
fig.tight_layout()
plt.savefig("./ch4_plot2_subplots_tight.png", bbox_inches="tight")

plt.clf()

x = np.linspace(0, 1)
y = np.linspace(0, 1)
X, Y = np.meshgrid(x, y)
F = np.exp(-X) * np.sin(10 * Y)
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].pcolormesh(X, Y, F)
axes[1].contour(X, Y, F)
plt.savefig("./ch4_plot2_contours.png", bbox_inches="tight")

plt.clf()

x = np.linspace(0, 1)
y = np.linspace(0, 1)
X, Y = np.meshgrid(x, y)
F = np.exp(-X) * np.sin(10 * Y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, F)
plt.savefig("./ch4_plot2_surface.png", bbox_inches="tight")

plt.clf()

x = np.linspace(0, 1)
y = np.linspace(0, 1)
X, Y = np.meshgrid(x, y)
F = np.exp(-X) * np.sin(10 * Y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, F, cmap=cm.viridis)
fig.colorbar(surf)
plt.savefig("./ch4_plot2_colourmaps.png", bbox_inches="tight")

plt.clf()
