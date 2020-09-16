import numpy as np

def integrand_exact(x):
    return ___

def simpson(f, a, b, nstrips):
    x, dx = np.linspace(a, b, num=2*nstrips+1, endpoint=True, retstep=True)
    return dx / 3 * (f(x[0]) + f(x[-1]) + 4 * np.sum(f(x[2:-1:2])) + 2 * np.sum(f(x[1:-1:2])))

check1 = simpson(integrand_exact, 0, 1, 10) - 25/12
print(check1)
