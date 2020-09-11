import numpy as np
import matplotlib.pyplot as plt

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
