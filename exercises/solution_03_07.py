import numpy as np

def simpson(f, a, b, N):
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
    x, dx = np.linspace(a, b, num=N, endpoint=True, retstep=True)
    return dx / 3 * (f(x[0]) + f(x[-1]) + 4 * np.sum(f(x[1:-1:2]))+ 2 * np.sum(f(x[2:-1:2])))
