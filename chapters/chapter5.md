---
title: 'Chapter 5: Convergence'
description:
  'This keystone exercise looks at how we would demonstrate the correctness of the quadrature methods we have implmeneted so far.'
prev: /chapter4
next: /chapter1
type: chapter
id: 5
---

<exercise id="1" title="Convergence" type="slides">

<slides source="chapter5_01_convergence">
</slides>

</exercise>

<exercise id="2" title="Testing Simpson's rule">

Which of the following polynomials is best to check the local error of a code implementing Simpson's rule?

Remember that
\\[
{\\cal E}\_{\text{Simpson}} \propto \max | f^{(4)} | \\, \left( \Delta x \right)^4.
\\]

<choice id="ch5_q2">

<opt text="\\(x^2 + x + 1\\)">

This is not general enough, given the local error of Simpson's rule.

</opt>
<opt text="\\(x^4 + 2 x^3 - 3 x^2 + 4 x - 1\\)">

This polynomial has too high an order for Simpson's rule to represent exactly, so would not make an ideal test.

</opt>
<opt text="\\(x^3 - 2 x^2 + 3 x + 1\\)" correct="true">

This polynomial is not too symmetric, and is the highest order polynomial that can be represented exactly by Simpson's method.

</opt>

</choice>

</exercise>

<exercise id="3" title="Coding Simpson's Rule">

Code the best integrand from the previous exercise, and use it to check that the provided function is correct. If not, fix it.

Modify the skeleton code so that

- the integrand is defined in the function `integrand_exact`;
- the provided `simpson` function gives the exact solution for this integrand.

Note that the exact solution for the quadrature will be
\\[
\tfrac{1}{4}(b^4 - a^4) - \tfrac{2}{3}(b^3 - a^3) + \tfrac{3}{2}(b^2 - a^2) + (b - a).
\\]

<codeblock id="05_03">

You can check the code and algorithm for Simpson's rule in chapter 3, or in the course notes.

</codeblock>

</exercise>

<exercise id="4" title="Errors from Simpson's Rule">

Using the integrand
\\[
  f(x) = x^2 \\sin(x),
\\]
compute the errors from Simpson's rule when approximating the quadrature
\\[
  \\int_0^1 \text{d} x \\, f(x) = 2 \\sin(1) + \\cos(1) - 2.
\\]
Use \\(10 \times 2^{0, \dots, 9}\\) strips.

Modify the skeleton code so that

- the integrand is defined in the function `integrand_sin`;
- the `simpson` function approximates the quadrature;
- the number of strips is encoded in `nstrips_all`;
- the error values are encoded in `errs`.

<codeblock id="05_04">

You can check the code and algorithm for Simpson's rule in chapter 3, or in the course notes, or in the solution to the previous exercise. You can check the slides for how to compute the errors.

</codeblock>

</exercise>

<exercise id="5" title="Convergence plot for Simpson's Rule">

Plot the errors from Simpson's rule when approximating the quadrature in the last exercise. The grid spacings and errors are imported for you. You should measure the convergence rate and annotate the plot appropriately.

Modify the skeleton code so that

- the coefficients for the best fit line are computed by `polyfit` and stored in `s`, `log_C` as appropriate;
- the numerical errors are plotted, with label `"Simpson's rule"`;
- the best fit line is plotted, with a label `"$s = {...}$"`, filling in the convergence rate to two decimal places (automatically!);
- the plot has a legend;
- the plot is annotated with labels `"$\Delta x$"` and `"Errors"` as appropriate;
- the plot has the title `"Convergence of Simpson's rule"`.

<codeblock id="05_05">

You can check how to produce the plot on the slides.

</codeblock>

</exercise>
