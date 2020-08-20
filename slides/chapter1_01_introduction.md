---
type: slides
---

# Introduction

Notes: This is a course covering the essentials of Python needed for Numerical Methods for differential equations. It assumes you've seen some Python before, but reminds you of the key commands and approaches.

---

# Integration

We are going to need to do numerical integration. For example, computing
\\[
\\begin{aligned}
  I_1 &= \int_0^1 \text{d}x \\, x^2 = \tfrac{1}{3}, \\\\ I_2 &= \int_0^1 \text{d}x \\, \sqrt{1 - x^2} = \tfrac{\pi}{4}.
\\end{aligned}
\\]

<img src="/chapter1/ch1_quad1.png" alt="The integrals we will look at." />

Notes: Our aim is to solve differential equations. The opposite of differentiation is integration. So there's links between numerical methods for DEs and for integration. It's also useful to analyse the algorithms for integration, as that analysis is close to, but often simpler, than the analysis for DEs.

---

# Quadrature

Approximating integrals is called <em>quadrature</em>. One method is

1. Split the domain into strips;
2. Compute the integrand at the left edge of the strip;
3. Find the area of the strip (value of integrand times width of strip);
4. Add up the areas of all strips.

<img src="/chapter1/ch1_quad2.png" alt="One simple quadrature method." />

Notes: This quadrature approach is linked to the Riemann integral often used to introduce integration. We don't have to evaluate the integrand at the left edge - any point within the strip will do. Using the left edge fixes a point. Later you can investigate how much difference this choice does (or doesn't) make.

---

# Spyder

- Python reads text typed into files or terminals and runs the commands.
- Spyder has an editor (left window) for files and built-in terminals (bottom right window).
- The top right window shows the help, plots, or other useful things.

<img src="/chapter1/spyder.png" alt="The Spyder window" />

Notes: Python is free and there are many ways that you can write and run Python code. We generally recommend the Anaconda distribution. Within that you will automatically get `Spyder`, which simplifies editing and running code, which we also recommend. You can also get `VSCode` and other alternatives, and should use whichever you prefer.

---

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

# Quadrature by arithmetic

We could compute the integral of \\(x^2\\) on \\([0, 1]\\) using \\(4\\) strips as

```python
(0**2 + (1/4)**2 + (2/4)**2 + (3/4)**2) * 1/4
```

```out
0.21875
```

Notes: We know the true result should be one third. This approximation uses four strips. The left edges of the strips are at `0`, `1/4`, `2/4`, `3/4`. The width of each strip is `1/4`. Each term inside the bracket is the integrand being evaluated at the left edge. The bracketed expression is the sum of all these integrands. Finally we multiply by the width of the strip, which is the same in all cases, to make this the area in all the strips, which is an approximation to the integrand.

---

# Variables

The code is clearer when <em>variables</em> are used.

```python
nstrips = 4
width = 1/nstrips
integral = ( (0/nstrips)**2 + (1/nstrips)**2 + (2/nstrips)**2 + (3/nstrips)**2 ) * width
print("The value is", integral)
```

```out
The value is 0.21875
```

Notes: A variable is a label on a value. The line `nstrips = 4` puts a label saying `nstrips` on the value `4`. When the code later refers to `nstrips` Python finds the label and replaces it with the value (currently `4`). We use variables in part to explain what we are doing. Note, however, that when we assign a value to a variable then nothing is shown on the screen. In order to find the value we have to explicitly use the `print` command.

---

# Loops

As we increase the number of strips, typing this out becomes impractical. Instead use a *loop*:

```python
nstrips = 4
width = 1/nstrips
integral = 0
for point in range(nstrips):
    print("At point", point)
    height = (point/nstrips)**2
    integral = integral + width * height
print("The value is", integral)
```

```out
At point 0
At point 1
At point 2
At point 3
The value is 0.21875
```

Notes: We are trying to do a repetitive task: compute the width of each strip then add them up. We want the computer to do this, not us. For this we use a loop. In Python the loop is started by the keyword `for`. The line starting the loop must end with `:`. All the commands that are indented four spaces will be run each time through the loop, like the `print` command. To stop the loop, stop indenting by four spaces. Within the line defining the loop we can define variables that change within the loop, to step over our repetitive task. This is often done by giving a list of values we want to use, and assigning them to a variable. Here the variable name is `point`. The function `range` will return integers from `0` up to but not including the final value; so `range(nstrips)` returns `0, 1, 2, 3` as `nstrips=4`. So `point in range(nstrips)` sets `point` first to `0`, then (once the commands in the loop have run for `point=0`) sets `point` to `1`, and so on.

---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
