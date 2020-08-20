---
type: slides
---

# Introduction

Notes: This is a course covering the essentials of Python needed for Numerical Methods for differential equations. It assumes you've seen some Python before, but reminds you of the key commands and approaches.

---

---

# Spyder

- Python reads text typed into files or terminals and runs the commands.
- Spyder has an editor (left window) for files and built-in terminals (bottom right window).
- The top right window shows the help, plots, or other useful things.

<img src="/chapter1/spyder.jpg" alt="The Spyder window" />

Notes: Python is free and there are many ways that you can write and run Python code. We generally recommend the Anaconda distribution. Within that you will automatically get `Spyder`, which simplifies editing and running code, which we also recommend. You can also get `VSCode` and other alternatives, and should use whichever you prefer.

# Arithmetic

Try arithmetic commands in the terminal:

```python
(1 + 2.3 * 4.5) / 6.7**8.9
```

```out
5.045800988343705e-07
```

- The terminal gives output immediately to the screen.
- More complex mathematics doesn't work immediately in base Python.

Notes: We will be using Python version 3. For arithmetic there are few surprises, but care is needed for division. When dividing integers, like `1/4`, Python version 3 will treat them as real numbers and return `0.25`. In earlier versions of Python the division of two integers would be an integer, and `1/4` would return `0`.

---

# Let's practice!

---
