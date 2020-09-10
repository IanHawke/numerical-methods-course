---
type: slides
---

# matplotlib

Notes: Using plots to check results and communicate correctness is a key part of numerical methods. When solving differential equations we often care about the solutions and also about errors. Often we need different types of plots to communicate correctness in different cases. The Python standard plotting library is <code>matplotlib</code>.

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

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
