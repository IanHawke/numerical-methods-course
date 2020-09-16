def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import numpy as np" in __solution__, "Have you imported numpy in its short form?"
    assert "import matplotlib.pyplot as plt" in __solution__, "Have you imported pyplot in its short form?"

    assert np.allclose((s, log_C), (3.863568238574405, -6.413802170416763)), "Have you computed the best fit line correctly?"

    __msg__.good("Well done!")
