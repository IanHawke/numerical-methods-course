---
type: slides
---

# numpy

Notes: In numerical methods we often deal with vectors and matrices. For example, in the quadrature we approximate the integrand at a list of points, which can be represented as a vector. This can be done with loops, as we have seen earlier. However, the numpy library is a powerful tool for working with vectors and matrices and will save us a lot of time.

---

# Vectors and quadrature

We approximate
\\[
  \int \text{d} x \\, f(x) \\simeq \\sum_{i=0}^N w_i f(x_i).
\\]
That is, we evaluate the integrand \\(f\\) on a grid of (\\(N+1\\)) points \\(\{x_i\}\\) and combine them using a set of weights \\(\{w_i\}\\).

In previous examples the grid were equally spaced and the weights were the same.

Notes: In previous chapters we approximated the quadrature by splitting the domain into strips, picking one point in each strip, evaluating the integrand at that point, and computing the area of the strip by multiplying the integrand by the width of the strip. In this chapter we replace the strips with the points directly, leading to the grid of points. We also replace the width with the weights. This gives a form that we can generalise for more accuracy later. The key point is that we have <em>vectors</em> of weights and grid points, from which we can form a vector (the summand) which we will sum to get the approximation to the integral.

---

# lists and vectors

Python gives you lists:
```python
x = [0, 0.5, 1]
print(x[0])
print(x + x)
```
```out
0
[0, 0.5, 1, 0, 0.5, 1]
```

`numpy` gives you arrays, which work like vectors:
```python
import numpy as np
x = np.array([0, 0.5, 1])
print(x[0])
print(x + x)
```
```out
0.0
[0.0, 1.0, 2.0]
```

Notes: Python lists are collections of things. The square brackets define the list. Each item in the list is separated by a comma. To access an item again use square brackets, using the index (starting from zero) into the list. Lists behave a bit like sets - if you add two sets you get the items in the list added. With <code>numpy</code>, you create the vector (or array) using the <code>numpy.array</code> function, which turns the list into something that acts like a vector. Accessing items works the same way as for lists. However, mathematical operations are applied to each element of the list. This is very powerful for numerical methods.<br>There is one weakness of <code>numpy</code> arrays. These arrays must contain the same type of things. Python lists, however, can contain different things in the same list. For numerical methods we will mostly use floating point numbers, so this is not a problem.

---

# Grids

We can use `numpy` to construct a grid (with \\(x \in [0, 1]\\) and \\(5\\) points):
```python
x = np.linspace(0, 1, num=5)
print(x)
```
```output
[0.  , 0.25, 0.5 , 0.75, 1.  ]
```
Note the point at the end, and the grid spacing is \\(1/4 = 1/(5-1)\\).

We can use more arguments to get the grid we want for quadrature:
```python
x, dx = np.linspace(0, 1, num=4, endpoint=False, retstep=True)
print(x)
print(dx)
```
```output
[0.  , 0.25, 0.5 , 0.75]
0.25
```

Notes: Constructing evenly spaced grids is something we do all the time in numerical methods. For this reason <code>numpy</code> has a function that that quickly constructs a linearly spaced vector of points. This function, <code>linspace</code>, has two required arguments, which are the start and end of the domain. The number of points in the grid is given by the argument <code>num</code>. <br> For our quadrature method we wanted the grid points on the left of the strip, so we do not want a point sitting on the end of the domain. For this reason we use the additional argument <code>endpoint</code> to switch it off. The number of points in the grid will now match the number of strips. Finally, for simplicity, we can use the <code>retstep</code> (short for <em>return stepsize</em>) argument to find the grid spacing. You can see this is equal to <code>x[1] - x[0]</code>.

---

# Functions of arrays

To compute our integrand \\(x^2\\) on the grid, use
```python
x, dx = np.linspace(0, 1, num=4, endpoint=False, retstep=True)
integrand = x**2
print(integrand)
```
```output
[0.     0.0625 0.25   0.5625]
```
To compute our integrand \\(\\sqrt{1-x^2}\\) on the grid, use
```python
integrand = np.sqrt(1 - x**2)
print(integrand)
```
```output
[1.         0.96824584 0.8660254  0.66143783]
```
So for a general integrand, use `f(x)`.

Notes: One powerful feature of <code>numpy</code> is that functions are applied directly to each element of arrays. That means we can compute the value of a function, such as the integrand, at every gridpoint, with a single line of code. We no longer need to use a loop. This reduces code length (which nearly always reduces errors) and increases speed (as <code>numpy</code> can do clever tricks at a low level). We see this working for both our integrands here, and it will apply to a general integrand.

---

# Sums and quadrature

Our original quadrature code used a loop to find the grid point and compute the sum:
```python
nstrips = 4
width = 1/nstrips
integral = 0
for point in range(nstrips):
    height = (point/nstrips)**2
    integral = integral + width * height
```
With `numpy` we can use in-built functions instead:
```python
x, dx = np.linspace(0, 1, num=nstrips, endpoint=False, retstep=True)
integral = dx * np.sum(x**2)
```
Easier to read and write, so less chance of errors.

Notes: In our original quadrature code we used a loop. We did this to loop over each strip, computing the location of each gridpoint (as <code>point/nstrips</code>), computing the value of the integrand at that gridpoint (as <code>height</code>), and then adding the area of the strip (<code>width * height</code>) to the current value for the integral. <br> In <code>numpy</code> we can shorten this considerably. The grid and grid spacing can be constructed using <code>linspace</code> as above. The grid spacing <code>dx</code> corresponds to the <code>width</code> of the strip. The integrand can be found at every gridpoint at once by applying the function to the grid. Here that is <code>x**2</code>, but in general would be <code>f(x)</code>. The sum is computed by the <code>numpy</code> function <code>sum</code>, and finally we multiply by the width. With much less code to read and write this is much easier to understand, and has less chance of errors, as well as being faster.

---

# Trapezoidal rule

The course will show a better quadrature rule is
\\[
  I = \int_0^1 \text{d}x \\, f(x) \simeq \frac{\Delta x}{2} \left[ f(x_0) + f(x_N) + 2 \sum_{i=1}^{N-1} f(x_i) \right].
\\]

* To access first point use `x[0]`.
* To access *last* point use `x[-1]`.
* To access *all* points from `start` up to, but not including, `end`, use `x[start:end]`.

So code the trapezoidal rule as
```python
x, dx = np.linspace(0, 1, num=nstrips+1, endpoint=True, retstep=True)
integral = dx / 2 * (f(x[0]) + f(x[-1]) + 2 * np.sum(f(x[1:-1])))
```

Notes: Sometimes we want to work on <em>part</em> of an array, not all of it. One example would be the trapezoidal rule. This is much more accurate that the Riemann integral approximation we have used so far. In this case there is a point on both the left and right boundary of every strip. For every strip except the last, the right point of one strip is exactly the left point of the next. So there is now one more point in the grid than the number of strips. Considering the grid in terms of points, in this case the first and last points of the grid (which now must lie on the boundaries of the interval) are treated differently to all other points. The integrand at the boundary gets half the weight of the integrand at all other points.<br>To code this we need to access individual points (the first and last, corresponding to the boundaries), and all the points in the interior. We have seen how to access the first. We use square brackets, and the zero index gives the first point. For the last point, Python allows us to count from the end using negative integers, where <code>-1</code> is the last point, <code>-2</code> next to last, and so on. To access all the interior points we use a <em>slice</em>. Within the square brackets we give the start and end indexes, with a <code>:</code> between them. This returns an array with all the value from the start up to, but not including, the end. So we start from the second point (index <code>1</code>) and go up to, but not including, the last (index <code>-1</code>). The sum is used as before.<br>Note that as we need a point on the right boundary the code defining the grid has changed the <code>endpoint</code> argument.<br>We can also use slicing to select every <code>n</code>th point. For example, <code>x[1:-1:2]</code> selects points <code>2, 4, 6, ...</code> up to, but not including, the last point.

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
