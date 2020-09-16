import numpy as np
import matplotlib.pyplot as plt
import sys; sys.path.insert(0, 'exercises/')
from ch5_simpson_results import dx, errs

s, log_C = np.polyfit(np.log(dx), np.log(errs), 1)
plt.loglog(dx, errs, 'kx', label="Simpson's rule")
plt.loglog(dx, np.exp(log_C) * dx**s, 'b-', label=fr"$s = {s:.2f}$")
plt.legend()
plt.xlabel(r"$\Delta x$")
plt.ylabel("Errors")
plt.title("Convergence of Simpson's rule")
