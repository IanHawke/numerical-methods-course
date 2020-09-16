def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    integrand_1 = lambda x : x**2
    integrand_2 = lambda x : 1 + x**0.5
    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"
    assert "np.sum" in __solution__, "Have you used the sum function from numpy?"
    assert abs(simpson(integrand_1, 0, 1, 10) - 1/3) < 1e-10, "The quadrature, applied to x^2 on [0, 1], does not return the expected value?"
    assert abs(simpson(integrand_1, 1, 2, 10) - 7/3) < 1e-10, "The quadrature, applied to x^2 on [1, 2], does not return the expected value?"
    assert abs(simpson(integrand_2, 1.5, 2.1, 123) - 1.4040478730749175) < 1e-10, "The quadrature, applied to 1+sqrt(x) on [1.5, 2.1], does not return the expected value?"

    __msg__.good("Well done!")
