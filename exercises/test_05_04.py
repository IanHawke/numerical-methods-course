def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"

    i_exact = lambda x: x**2 * np.sin(x)
    x = np.linspace(-1, 1)
    assert np.allclose(integrand_sin(x), i_exact(x)), "Have you set up the integrand_sin function correctly?"

    assert np.allclose(nstrips_all, 10 * 2**np.arange(10)), "Have you set up the nstrips_all variable correctly?"

    vals = [(0, 1, 10, 0.22324398545899074),
            (0, 1, 50, 0.22324427502018113),
            (-1, 2, 10, 2.246212475089211),
            (1.5, 3.6, 20, 3.6675254267609945)]
    for (a, b, ns, sol) in vals:
        assert np.allclose(simpson(i_exact, a, b, ns) - sol, 0), f"The value from the simpson function does not match for a={a}, b={b}, nstrips={ns}"

    errs_expected = np.array([2.90024942e-07, 1.81177624e-08, 1.13222279e-09, 7.07618131e-11, 4.42260117e-12, 2.76473289e-13, 1.73194792e-14, 1.08246745e-15, 5.55111512e-17, 2.77555756e-17])
    assert(np.allclose(errs, errs_expected)), "The errors in the errs variable do not match expectations. Is your loop correct? Have you compared to the correct exact value?"

    __msg__.good("Well done!")
