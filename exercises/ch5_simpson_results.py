import numpy as np

def integrand_sin(x):
    return x**2 * np.sin(x)

def simpson(f, a, b, nstrips):
    x, dx = np.linspace(a, b, num=2*nstrips+1, endpoint=True, retstep=True)
    return dx / 3 * (f(x[0]) + f(x[-1]) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-1:2])))

nstrips_all = 10 * 2**np.arange(8)
dx = 1 / nstrips_all
errs = np.zeros(len(nstrips_all))
for i in range(len(nstrips_all)):
    errs[i] = abs(simpson(integrand_sin, 0, 1, nstrips_all[i]) - (2 * np.sin(1) + np.cos(1) - 2))
