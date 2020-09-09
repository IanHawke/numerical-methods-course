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

Notes: Python lists are collections of things. The square brackets define the list. Each item in the list is separated by a comma. To access an item again use square brackets, using the index (starting from zero) into the list. Lists behave a bit like sets - if you add two sets you get the items in the list added. With <code>numpy</code>, you create the vector (or array) using the <code>numpy.array</code> function, which turns the list into something that acts like a vector. Accessing items works the same way as for lists. However, mathematical operations are applied to each element of the list. This is very powerful for numerical methods.

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
