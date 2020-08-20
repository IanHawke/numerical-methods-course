def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert nstrips == 100, "Have you set the value of nstrips correctly?"
    assert abs(height - 0.14106735979665894) < 1e-10, "Have you set the value of height, containing the integrand, correctly?"
    assert abs(integral - 0.7901042579447618) < 1e-10, "Have you changed the code consistently?"

    __msg__.good("Well done!")
