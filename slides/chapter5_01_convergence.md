---
type: slides
---

# Convergence

Notes: We have seen and coded three methods for approximating integrals. But how do we know if any of them are correct? This chapter will briefly introduce two tools for checking, and the exercises will check you can code them.

---

# Errors in quadrature

We saw three methods to approximate
\\[
  I = \int_a^b \text{d} x \\, f(x).
\\]
Methods needed grid, width \\(\\Delta x\\). Errors scale:
\\[
\\begin{aligned}
  {\cal E}\_{\text{Riemann}} &\propto \max | f^{(1)} | \\, \left( \Delta x \right)^1, \\\\
  {\\cal E}\_{\text{Trapezoidal}} &\propto \max | f^{(2)} | \\, \left( \Delta x \right)^2, \\\\
  {\\cal E}\_{\text{Simpson}} &\propto \max | f^{(4)} | \\, \left( \Delta x \right)^4.
\\end{aligned}
\\]
How to check?

Notes: The lectures go into the analysis of the errors of each scheme. Essentially, you investigate one strip at a time. Take the Taylor series expansion of the method in one strip, and compare to an appropriate Taylor series expansion of the exact solution. The error in one strip is the difference. The error over the full domain comes from adding up all the strips, which (in the worst case) increases the total error by a factor \\((\Delta x)^{-1}\\). The analysis also shows that the error is proportional to a largest derivative of the integrand. The number of derivatives required is, in our cases, the same as the power of the grid spacing in the total error.<br>We can see a few features that we would want to check our code obeys. For example, if our integrand has derivatives than vanish beyond an appropriate order, the error should be zero (eg, the trapezoidal rule should be exact for linear polynomials). Second, when the error is non-zero, it should scale with the grid spacing in a predictable way.<br>The analysis also raises questions. For example, what happens when derivatives of the integrand don't exist and we try to use, say, Simpson's rule?

---

# Exact simple cases

If the error
\\[
  {\cal E} \propto f^{(n)}
\\]
then if all derivatives vanish the error will vanish.

For trapezoidal rule \\(n=2\\). Define `trapezoidal(f, a, b, nstrips)`. Try:
```python
def integrand_linear(x):
    return x + 1
print(trapezoidal(integrand_linear, 0, 1, 10) - 3/2)
```
```output
0.0
```

Notes: The quadrature methods work by approximating the integrand by a polynomial. It follows that when the integrand <em>is</em> a polynomial that the method represents exactly, the answer from the method is exact. For the Riemann integral method, the integrand must be constant. For the trapezoidal rule it must be linear.<br>We can use this as a cross-check of our method. Assume we have defined a function <code>trapezoidal</code> that uses the trapezoidal rule shown in Chapter 3, and takes the integrand, the boundaries of the domain, and the number of strips in the standard form. We then check against some linear polynomial, and ensure we get the exact answer. It is useful to check on a couple of functions with different domains (in case of lucky cancellations), but this is a first check that the local error behaves as expected.

---

# Convergence plots

<img src="/chapter5/ch5_plot1.png" alt="Showing convergence with grid resolution." width="40%" align="right"/>

If the error goes as
\\[
  {\cal E} \simeq C ( \Delta x )^s
\\]
then
\\[
  \log {\cal E} \simeq \log C + s \log ( \Delta x ).
\\]
The slope of the best-fit straight line of \\(\log {\cal E}\\) against \\(\log ( \Delta x )\\) gives the <em>convergence rate</em> \\(s\\).

In code, given `dx` and `errs`, best-fit line is
```python
s, log_C = np.polyfit(np.log(dx), np.log(errs), 1)
```
Then plot:
```python
plt.loglog(dx, errs, 'kx', label="Random data")
plt.loglog(dx, np.exp(log_C) * dx**s, 'b-', label=fr"$s = {s:2f}$")
```

Notes: For more general integrands than simple polynomials we expect the method to have a numerical error, and the analysis in the notes shows how that scales with the grid resolution. We can then use some general integrand whose exact integral we can compute, and check that the numerical error of the code scales as we expect.<br>The error in general is a power series in the grid spacing. However, it is only the leading term (smallest power of \\(\Delta x\\)) that we care about. To measure this it is best to take logarithms of the error and grid spacing. The best-fit <em>straight line</em> of \\(\log {\cal E}\\) against \\(\log ( \Delta x )\\) has slope which is the measured convergence rate \\(s\\). This is the smallest power of \\(\Delta x\\) in the power series, and can be compared to the value from the analysis.<br><code>numpy</code> has a function that computes best fit polynomials, which is <code>polyfit</code>. We only want a straight line, so the degree is <code>1</code>, and it returns the slope and the intersection. The slope is the key number, but it is important to check that the fit makes sense (there may be outliers!). We can do this using a <code>loglog</code> plot, which we can annotate with the convergence rate.

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
