def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"
    assert "np.sqrt" in __solution__, "Have you used the square root function from numpy?"
    assert abs(integrand_1(0) - 1) < 1e-10, "The function, called on 0, does not return 1?"
    assert abs(integrand_1(0.5) - 0.8660254037844386) < 1e-10, "The function, called on a random real number (less than 1!), does not return the correct value?"

    __msg__.good("Well done!")
