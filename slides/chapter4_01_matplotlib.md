---
type: slides
---

# matplotlib

Notes: Using plots to check results and communicate correctness is a key part of numerical methods. When solving differential equations we often care about the solutions and also about errors. Often we need different types of plots to communicate correctness in different cases. The Python standard plotting library is <code>matplotlib</code>.

---

# Quantitative information

We wanted to approximate
\\[
  \int_0^1 \text{d} x \\, \sqrt{1 - x^2}.
\\]

* What does the integrand look like?
* Is it finite?
* Is it continuous?
* How does the approximation error change with computational effort?

Notes: Plotting can give us important qualitative information quickly. For example, is the integrand finite and continuous over the domain? To check this, we want to plot the integrand against the independent variable.

---

# Plotting a line

<img src="/chapter4/ch4_plot1.png" alt="The integrand plotted against the independent variable." width="40%" align="right"/>

To plot a simple line, use `matplotlib` with `numpy`:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
plt.plot(x, np.sqrt(1 - x**2))
```

Notes: With Python, the standard plotting library is <code>matplotlib</code>. This has a default interface <code>pyplot</code>, which is designed to work with <code>numpy</code>. So first we <code>import</code> the <code>numpy</code> and <code>matplotlib.pyplot</code> packages. We then approximate the independent variable using a grid of points across the domain, using <code>linspace</code> with the default number of points. Finally, a line plot is produced with the <code>plot</code> command, which plots the integrand against the independent variable.<br>You should note that sometimes it is necessary to explicitly tell Python to show the plot using the <code>plt.show()</code> command.

---

# Making plots useful

<img src="/chapter4/ch4_plot1_labeled.png" alt="The integrand plotted against the independent variable with labels." width="40%" align="right"/>

Add axis labels, a title, and a legend:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
plt.plot(x, np.sqrt(1 - x**2), label=r"$\sqrt{1-x^2}$")
plt.title("The integrand")
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.legend()
```


Notes: For a plot to be useful it has to communicate clearly what its information is. For that use should use axis labels, titles, and legends at least. With a single line plot we can do that directly with function calls in <code>pyplot</code>. Each will take a string argument with what to display.<br>When displaying mathematics, the string can use <em>LaTeX</em> syntax. To do this, surround the contents with dollars, <code>$</code>. This allows us to display superscripts and special commands. However, as the special commands often need backslashes (as in <code>\sqrt</code>), we need to tell Python not to interpret these as special <em>string</em> commands. For that we tell Python this is a <em>raw</em> string, by putting the <code>r</code> before the quotes.

---

# Making plots useful

<img src="/chapter4/ch4_plot1_scales.png" alt="The integrand plotted against the independent variable with range set by hand." width="40%" align="right"/>

Add axis labels, a title, and a legend:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
plt.plot(x, np.sqrt(1 - x**2))
plt.xlim(0, 1)
plt.ylim(-0.1, 1.1)
```


Notes: The previous plots looked a little odd as the plot domain extended outside the domain of the quadrature. That meant the line stopped, as if supported in mid-air. We can set the domain explicitly by setting the <em>limits</em>, for example using the <code>xlim</code> command. These take numerical arguments for the start and end of the range.

---

# More than one line

<img src="/chapter4/ch4_plot1_multiple.png" alt="Two integrands plotted against the independent variable with different linestyles." width="40%" align="right"/>

To add two lines to the plot, add more plot commands.

To tell which is which use linestyles and markers:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
plt.plot(x, np.sqrt(1 - x**2), label=r"$\sqrt{1-x^2}$",
         linestyle='-', color='black')
plt.plot(x, x**2, label=r"$x^2$",
         linestyle='--', color='green', markerstyle='x')
plt.legend()
```


Notes: We often want to use plots to compare qualitative features of two functions or datasets. To add a second line to the same plot, use the <code>plot</code> command a second time. You can add as many lines as you want.<br>The problem with adding more lines is it becomes harder to see what is what. To distinguish the lines it is best to change their looks, by changing style (for example to dashed lines), their colour (using American spelling), or by adding markers. In addition you could change the thickness of lines or markers. All of these need a legend for clarity.<br>It is a convention in numerical methods that analytical solutions are plotted with lines and numerical solutions with markers.

---

# Different scales

<img src="/chapter4/ch4_plot1_loglog.png" alt="Two integrands plotted against the independent variable with different linestyles." width="40%" align="right"/>

We will often need logarithmic plots:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1e-4, 1)
plt.loglog(x, x**2, label=r"$x^2$",
         linestyle='-', color='black')
plt.loglog(x, x**4, label=r"$x^4$",
         linestyle='--', color='green')
plt.legend()
```

Notes: In numerical methods we often want to check the qualitative behavior of the method, or its error, and it often behaves like a polynomial (this is linked to Taylor expansions). Polynomials are often clearest on <em>logarithmic</em> plots, where \\(\log(f)\\) appears as a straight line when plotted against \\(\log(x)\\).<br>To construct a logarithmic plot, use the <code>loglog</code> command. In all other respects it behaves like the <code>plot</code> command. It will, of course, give errors if either the function or the independent variable are not positive.<br>If you want to display exponential or logarithmic behaviour of the function you would want to have one axis linear and one logarithmic. For this you would use, for example, <code>semilogx</code>.

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
