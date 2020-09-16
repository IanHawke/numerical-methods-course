def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"

    i_exact = lambda x: x**3 - 2*x**2 + 3*x + 1
    x = np.linspace(-1, 1)
    assert np.allclose(integrand_exact(x), i_exact(x)), "Have you set up the integrand_exact function correctly?"

    value_exact = lambda a, b: -a**4/4 + 2*a**3/3 - 3*a**2/2 - a + b**4/4 - 2*b**3/3 + 3*b**2/2 + b
    pairs = [(0, 1), (-1, 2), (1.5, 3.6)]
    for (a, b) in pairs:
        assert np.allclose(simpson(integrand_exact, a, b, 10) - value_exact(a, b), 0), f"The quadrature value does not match for a={a}, b={b}"

    __msg__.good("Well done!")
