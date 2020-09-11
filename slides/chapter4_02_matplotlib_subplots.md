---
type: slides
---

# More complex plots

Notes: Most of the plots we need will be line plots, but a single figure is not always enough. Sometimes we will want to group multiple datasets into one figure, but not on the same axes. An example would be when features are at similar locations, but have very different scales or values. At other times we will want to plot contours our surfaces.

---

# Subplots

<img src="/chapter4/ch4_plot2_subplots.png" alt="Two subplots in one figure." width="40%" align="right"/>

To use subplots, we need to control each axes separately:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(x, np.sin(10*x))
axes[1].plot(x, np.cos(15*x))
```

Notes: Subplots are the most useful tool for controlling plots in more detail. However, they need a fundamentally different way of thinking about plotting.<br>The <code>subplots</code> command will construct the figure <code>fig</code> and an array of <code>axes</code> that we can use to do the plotting. Each axis in the array can be accessed as we would a <code>numpy</code> array of numbers, with a square bracket and an integer index starting from zero.<br>To produce a plot <em>on a particular axis</em> <code>ax</code> we need to apply the <plot> method of that axis <code>ax</code>. That is, we call <code>ax.plot</code>.

---

# More methods

<img src="/chapter4/ch4_plot2_subplots_labels.png" alt="Two subplots in one figure with labels and titles." width="40%" align="right"/>

To use subplots, we need to control each axes separately:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(x, np.sin(10*x))
axes[0].set_xlim(0, 1)
axes[0].set_title("Sine and cosine")
axes[1].plot(x, np.cos(15*x))
axes[1].set_xlabel(r"$x$")
axes[1].set_ylabel(r"$\cos(15x)$")
```

Notes: Controlling details of each axis needs more methods on that axis. Most of these methods have similar, but not identical, names to the functions applied to a single plot. So, to set the <code>x</code> label the method name is <code>set_xlabel</code>, compared to the function name <code>xlabel</code>. To set the <code>x</code> limits the method name is <code>set_xlims</code>, compared to the function name <code>xlims</code>. A couple of functions (like <code>legend</code>) do not change, so check the help if you have problems.

---

# Spacing and layout

<img src="/chapter4/ch4_plot2_subplots_tight.png" alt="Two subplots in one figure with labels that might overlap." width="40%" align="right"/>

Fix potential overlapping parts of the plot at the `figure` level:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(x, np.sin(10*x))
axes[0].set_xlabel(r"$x$")
axes[1].plot(x, np.cos(15*x))
axes[1].set_xlabel(r"$x$")
fig.tight_layout()
```

Notes: A problem with many axes is that they may overlap. This is particularly true for titles, labels, or axis ticks. In most cases <code>matplotlib</code> can fix this automatically with the function <code>tight_layout</code>. However, this has to be applied <em>to the whole figure</em> <code>fig</code>, as it requires considering every axis within the figure and how they fit together.

---

# Higher dimensions

Suppose we have a two parameter function,
\\[
  f(x, y) = e^{-x} \sin(10 y).
\\]
We want to plot this as a function of \\(x\\) *and* \\(y\\). First we need to construct the grid and data. Use <code>meshgrid</code>:
```python
import numpy as np
x = np.linspace(0, 1)
y = np.linspace(0, 1)
X, Y = np.meshgrid(x, y)
F = np.exp(-X) * np.sin(10 * Y)
```

Notes: Higher dimensional data first needs constructing. It's simplest (where possible) to use a regular grid on which to sample the data. That makes it easier for plotting algorithms to join neighbouring points and produce nice plots.<br>Here we use the <code>numpy</code>function <code>meshgrid</code>. Given to one-dimensional arrays containing the location of the coordinates along each axis, it produces two-dimensional arrays (essentially matrices) giving the coordinates of the grid points. We can use this (with standard <code>numpy</code> operations) to construct two-dimensional datasets. For example, here we are sampling the two parameter function onto a <code>50</code> by <code>50</code> grid that we can then plot.

---

# Flat plots

<img src="/chapter4/ch4_plot2_contours.png" alt="Higher dimensional data presented on flat plots using pcolormesh and contour." width="40%" align="right"/>

Flat plots using colour or contours give useful information:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
y = np.linspace(0, 1)
X, Y = np.meshgrid(x, y)
F = np.exp(-X) * np.sin(10 * Y)
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].pcolormesh(X, Y, F)
axes[1].contour(X, Y, F)
```

Notes: Once we have two dimensional data then there are a few functions in standard <code>matplotlib</code> that will produce useful plots.<br>One uses colour to present the data, like in a heatmap. The <code>pcolormesh</code> function takes the two coordinate arrays and the data array, and the size of the value is represented by the colour.<br>The second approach draws lines at constant values. The <code>contour</code> function uses exactly the same arguments.<br>Both types of plots should be used with care. Human perception of colour can be misleading, so colour-based plots needed careful checks. Likewise, the algorithm to draw contour lines can break down on nasty functions.

---

# Surface plots

<img src="/chapter4/ch4_plot2_surface.png" alt="Higher dimensional data presented on a surface plot." width="40%" align="right"/>

Surface plots show structure:
```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(0, 1)
y = np.linspace(0, 1)
X, Y = np.meshgrid(x, y)
F = np.exp(-X) * np.sin(10 * Y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, F)
```

Notes: Flat projections of higher dimensional data are useful, but surface plots can show the large scale structure more easily. These require more control over the axis on which we plot, which means loading more packages.<br>The first change is the requirement to <code>import</code> the <code>Axes3D</code> object from <code>mpl_toolkits</code>. This defines a three-dimensional axis projection on which we can produce the plot. When we construct the axis for the figure (again using <code>subplots</code> as before, although here we only construct one axis) we can pass through the keyword for the projection, to tell the code that constructs the axis that we want it to be three-dimensional.<br>Once we have this three-dimensional axis we can use the <code>plot_surface</code> function in exactly the same way as, for example, the <code>contour</code> function.

---

# Colourmaps

<img src="/chapter4/ch4_plot2_colourmaps.png" alt="Higher dimensional data with a colourmap." width="40%" align="right"/>

Being explicit about the colourmap is often useful:
```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
x = np.linspace(0, 1)
y = np.linspace(0, 1)
X, Y = np.meshgrid(x, y)
F = np.exp(-X) * np.sin(10 * Y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, F, cmap=cm.viridis)
fig.colorbar(surf)
```

Notes: Even contour and surface plots can, and often do, make use of colour. It is useful to control the colourmap, and to explicitly show it so a human can see how the values of the data map to the colours in the plot.<br>To control the map we need to load the available colourmaps through the subpackage <code>cm</code>. Once we have access to that, we can use any colourmap within that package as an argument to the plotting function, as seen here with the final argument to <code>plot_surface</code>.<br>We then need to store the output of the plotting function, as we have done here in the variable <code>surf</code>. We can then use the (figure level!) function <code>colorbar</code> to show how the colours link the data values for this particular surface (or set of contours, or whatever is displayed in the plot).

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
