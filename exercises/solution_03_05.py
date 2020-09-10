import numpy as np

def quadrature(f, a, b, N):
    '''
    Compute the quadrature of f on [a, b].

    Parameters
    ----------

    f : function
        The integrand
    a : float
        The start of the domain
    b : float
        The end of the domain
    N : int
        The number of strips, which is the number of gridpoints

    Returns
    -------

    I : float
        The integral approximation
    '''
    x, dx = np.linspace(a, b, num=N, endpoint=False, retstep=True)
    return dx * np.sum(f(x))
