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
        lines = ax.get_lines()
        leg = ax.get_legend()
    except:
        raise AssertionError("Have you produced a plot to the screen that contains a legend?")

    assert ax.get_xlabel() == r"$x$", "Have you set the x label correctly?"
    assert ax.get_ylabel() == r"$f(x)$", "Have you set the y label correctly?"
    assert (leg.get_texts()[0].get_text() == r"$\sin(x)$") and (leg.get_texts()[1].get_text() == r"$\cos(2x)$"), "Have you set the legend labels correctly?"
    assert (lines[0].get_linestyle() == '-') and (lines[1].get_linestyle() == '--'), "Have you set the line styles correctly?"
    assert (lines[0].get_color() in ['black', 'k']) and (lines[1].get_color() in ['blue', 'b']), "Have you set the line colours correctly?"


    __msg__.good("Well done!")
