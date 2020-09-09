import numpy as np

def integrand_1(x):
    '''
    Compute the integrand sqrt(1 - x^2).

    Parameters
    ----------

    x : float
        The input coordinate location

    Returns
    -------

    sqrt(1-x^2) : float
        The integrand
    '''
    return np.sqrt((1 - x**2))
