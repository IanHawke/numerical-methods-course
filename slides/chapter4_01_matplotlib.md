---
type: slides
---

# matplotlib

Notes: Using plots to check results and communicate correctness is a key part of numerical methods. When solving differential equations we often care about the solutions and also about errors. Often we need different types of plots to communicate correctness in different cases. The Python standard plotting library is <code>matplotlib</code>.

---

# Plotting a line

We wanted to approximate
\\[
  \int_0^1 \text{d} x \\, \sqrt{1 - x^2}.
\\]
What does the integrand look like?

To plot a simple line, use `matplotlib` with `numpy`:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
plt.plot(x, np.sqrt(1 - x**2))
```
<img src="/chapter4/ch4_plot1.png" alt="The integrand plotted against the independent variable." />


Notes: Plotting can give us important qualitative information quickly. For example, is the integrand finite and continuous over the domain? To check this, we want to plot the integrand against the independent variable.<br>With Python, the standard plotting library is <code>matplotlib</code>. This has a default interface <code>pyplot</code>, which is designed to work with <code>numpy</code>. So first we <code>import</code> the <code>numpy</code> and <code>matplotlib.pyplot</code> packages. We then approximate the independent variable using a grid of points across the domain, using <code>linspace</code> with the default number of points. Finally, a line plot is produced with the <code>plot</code> command, which plots the integrand against the independent variable.<br>You should note that sometimes it is necessary to explicitly tell Python to show the plot using the <code>plt.show()</code> command.

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
