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

# Computing errors

Before we can plot we need to compute the errors.

First construct an array of number of strips:
```python
nstrips_all = 10 * 2**np.arange(10)
```
Then the domain, grid spacings, and an empty array for the errors:
```python
a = 0
b = 1
dx = (b - a) / nstrips_all
errs = np.zeros(len(nstrips_all))
```
Finally, loop to compute the error:
```python
for i in range(len(nstrips_all)):
    errs[i] = abs(quadrature(f, a, b, nstrips_all[i]) - exact)
```
We can now use `dx` and `errs` to do the plotting.

Notes: Setting up the arrays to produce the convergence plots can be simplified using some <code>numpy</code> functions. What we need to know in advance is the domain on which the integral is computed (specified by <code>a</code> and <code>b</code>, the endpoints of the domain) and the exact value of the integral <code>exact</code>. We then want to compute our approximation multiple times, using different values of the grid spacing <code>dx</code> (corresponding to different numbers of strips <code>nstrips</code>), and store the results. This is naturally done with a loop.<br>First we have to construct an array containing the number of strips we are going to use. As we are going to expect power law behaviour, it is natural to use a power law to construct the number of strips. Here we use \\(10 \times 2^{0, 1, \dots, 9} = 10, 20, \dots, 5120\\). This is fairly arbitrary, but using powers of two is the smallest step guaranteed to give integers. The <code>np.arange</code> function works exactly like <code>range</code>, but produces a <code>numpy</code> <code>array</code>, which means we can immediately use it in the exponent.<br> We then set up the grid spacings. As <code>nstrips_all</code> is an <code>array</code>, the line defining <code>dx</code> makes it an array as well.<br>We define an <code>array</code> just containing zeros to hold the errors, <code>errs</code> This has the same size as <code>nstrips_all</code>. This means the array to hold the errors is ready for when we do the loop.<br>Finally we loop over all the values of <code>nstrips</code>. For each value we compute the result from the quadrature and compute the magnitude of the difference between the value and the exact solution. This is stored in <code>errs</code>. We can now use <code>dx</code> and <code>errs</code> to produce the convergence plot as in the previous slide.

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
