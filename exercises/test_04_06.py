def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"
    assert "import matplotlib.pyplot as plt" in __solution__, "Have you imported matplotlib in its short form?"
    assert "x**3" in __solution__, "Have you plotted the correct function?"
    assert "plot" in __solution__, "Have you used the plot function from matplotlib?"
    assert np.allclose(x, np.linspace(1e-4, 10)), "Have you set up the grid correctly?"

    try:
        f = plt.gcf()
        geom = f.axes[0].get_subplotspec().get_topmost_subplotspec().get_gridspec().get_geometry()
    except:
        raise AssertionError("Have you produced a plot to the screen?")

    assert numpy.allclose(geom, (1, 2)) , "Have you set the number of rows (1) and columns (2) correctly?"
    assert (f.axes[0].get_xscale() == r"linear") and (f.axes[0].get_yscale() == r"linear"), "Have you plotted on linear scales for the left plot?"
    assert (f.axes[1].get_xscale() == r"log") and (f.axes[1].get_yscale() == r"log"), "Have you plotted on logarithmic scales for the right plot?"
    assert (f.axes[0].get_xlabel() == r"$x$") and (f.axes[1].get_xlabel() == r"$x$"), "Have you set the x labels correctly?"


    __msg__.good("Well done!")
