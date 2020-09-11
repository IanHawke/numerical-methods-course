def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"
    assert "import matplotlib.pyplot as plt" in __solution__, "Have you imported matplotlib in its short form?"
    assert "np.sin" in __solution__, "Have you used the sin function from numpy?"
    assert "plt.plot" in __solution__, "Have you used the plot function from matplotlib?"
    assert np.allclose(x, np.linspace(0, 10)), "Have you set up the grid correctly?"

    try:
        ax = plt.gca()
    except:
        raise AssertionError("Have you produced a plot to the screen?")

    assert np.allclose(ax.get_xlim(), [1, 8]), "Have you set the limits in x correctly?"
    assert ax.get_title() == "Titled plot", "Have you set the title correctly?"
    assert ax.get_xlabel() == r"$x$", "Have you set the x label correctly?"
    assert ax.get_ylabel() == r"$\sin(x)$", "Have you set the y label correctly?"


    __msg__.good("Well done!")
