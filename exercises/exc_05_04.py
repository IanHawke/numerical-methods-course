import numpy as np

def integrand_sin(x):
    return ___

def simpson(f, a, b, nstrips):
    x, dx = ___
    return ___

nstrips_all = ___
dx = ___
errs = np.zeros(___)
for i in range(len(nstrips_all)):
    errs[i] = abs(simpson(___) - (___))
