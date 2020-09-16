def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"
    assert "import matplotlib.pyplot as plt" in __solution__, "Have you imported pyplot in its short form?"

    assert np.allclose((s, log_C), (3.99955988203847, -5.844916461863553)), "Have you computed the best fit line correctly?"

    try:
        ax = plt.gca()
        lines = ax.get_lines()
        leg = ax.get_legend()
    except:
        raise AssertionError("Have you produced a plot to the screen that contains a legend?")

    assert ax.get_xlabel() == r"$\Delta x$", "Have you set the x label correctly?"
    assert ax.get_ylabel() == "Errors", "Have you set the y label correctly?"
    assert (leg.get_texts()[0].get_text() == r"Simpson's rule") and (leg.get_texts()[1].get_text() == r"$s = 4.00$"), "Have you set the legend labels correctly?"
    assert ax.get_title() == "Convergence of Simpson's rule", "Have you set the plot title correctly?"
    for l in lines:
        assert np.allclose(l.get_data()[0], dx), "Have you used the correct array on the x axis?"
        assert np.allclose(l.get_data()[1], errs) or np.allclose(l.get_data()[1], np.exp(log_C) * dx**s), "Have you used the correct array on the y axis?"

    __msg__.good("Well done!")
