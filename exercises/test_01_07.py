def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert nstrips == 10, "Have you set the value of nstrips correctly?"
    assert abs(integral - 0.3325) < 1e-10, "Have you evaluated the integrand at the right points?"

    __msg__.good("Well done!")
