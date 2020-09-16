import numpy as np
import matplotlib.pyplot as plt

dx = 1/2**np.arange(16)
errs = 0.3 * dx**2 + 5*np.random.rand(len(dx)) * dx**4
s, log_C = np.polyfit(np.log(dx), np.log(errs), 1)
plt.loglog(dx, errs, 'kx', label="Random data")
plt.loglog(dx, np.exp(log_C) * dx**s, 'b-', label=fr"$s = {s:.2f}$")
plt.xlabel(r"$x$")
plt.ylabel("Errors")
plt.legend()
plt.savefig("./ch5_plot1.png", bbox_inches='tight')

plt.clf()
