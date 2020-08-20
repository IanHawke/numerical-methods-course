---
type: slides
---

# Functions

Notes: In the first chapter we looked at quadrature. In the final exercise we changed the integrand. However, we had to copy a lot of code to make this work. Repeated code is not good, as it's too easy to make mistakes. We want to improve our code to make it more general.

---

# General quadrature

We can now solve (or approximate)
\\[
  \int \text{d} x \\, x^2,
\\]
but we want to solve
\\[
  \int \text{d} x \\, f(x).
\\]

How do we generalise our method?

Notes: The problem with our current code is that we keep repeating ourselves. If a mistake creeps in and we copy that code (and mistake) to many places, it can be very hard to find and fix. This is the DRY principle - Do not Repeat Yourself. Instead we want a general algorithm then can be used in all cases.

---

# Functions

We have seen functions like `print`:

- they take input, like `print(1.2)`;
- they can produce output;
- we don't care what they do internally;
- we can get help by `help(print)`.

Notes: Functions are collections, or blocks, of code that take in input arguments or parameters and may return output. We want to produce our own functions, so we don't have to keep copying code.

---

# Defining a function

Define a function a bit like a loop:

```python
def myfunction(a, b):
    """
    Help documentation
    """
    output = a + b**a
    return output
```

Notes: Remember when we defined a loop. The keyword at the start of the line was `for`; the end of the line needed a `:`; and the code to be repeated was indented four spaces. With a function it is similar. The keyword is `def`, to *define* the function. The name of the function comes next. The arguments, or parameters, to the function are inside brackets. The line finishes with a `:`. The code the function runs is indented four spaces. At the end of the function you send back the result of your calculation using `return`.

---

# Adding two numbers

Define and use a short function:

```python
def my_add(a, b):
    """
    Computes a+b.
    """
    return a + b

print(my_add(1, 2.3))
help(my_add)
```

```out
3.3

Help on function my_add in module __main__:

my_add(a, b)
    Computes a+b.
```

Notes: We define a simple function to add two numbers. The parameters `a` and `b` are the inputs to the function, which will be given values when the function is called. The line(s) within the triple quotes are the documentation, which are printed to the screen by the `help` function. The `return` statement sends the result of the calculation back to the caller, where it can be stored (by assigning it to a variable) or printed, as here.

---

# Building a function

1. Start from working code.
2. Put the parameters at the top.
3. Put the `def` after the parameters.
4. Put the parameters in the brackets after the function name.
5. Indent the code.
6. Add a `return` at the end, maybe replacing the `print`.

Notes: We often build code bit-by-bit. In the first chapter we built up a code to do quadrature by adding variables. We know (or at least believe) that that code works. To make it into a function, it's often best to start from there.

---

# Building our quadrature function

Compare

```python
nstrips = 4
width = 1/nstrips
integral = 0
for point in range(nstrips):
    height = (point/nstrips)**2
    integral = integral + width * height
print("The value is", integral)
```

and

```python
def quadrature(nstrips):
  width = 1/nstrips
  integral = 0
  for point in range(nstrips):
      height = (point/nstrips)**2
      integral = integral + width * height
  return integral
```

Notes: This followed exactly the steps on the previous slide. The only parameter (for now) is the number of strips that we split the interval into. We put the `def` statement after the definition of `nstrips`. We add `nstrips` inside the brackets. We indent all the code. We replace the `print` statement with an appropriate `return` statement. We can then call this function, varying the number of strips, and it will return the approximation.

---

# Functions of functions

We wanted an algorithm that worked for any integrand. We can do that by defining the integrand as a function:

```python
def integrand_x_sq(x):
    return x**2
def quadrature(f, nstrips):
  width = 1/nstrips
  integral = 0
  for point in range(nstrips):
      height = f(point/nstrips)
      integral = integral + width * height
  return integral

print(quadrature(integrand_x_sq, 10))
```

```out
0.285
```

Notes: We really wanted a quadrature algorithm that would work for any integrand. That means we want the quadrature function to not depend on the integrand. Instead the integrand function should be passed in as a parameter. In Python, functions can be passed in to other functions in the same way as any other input. Here we define a function for our integrand, and then modify our `quadrature` function in two places. First, we add the integrand to the parameter list as `f`. Second, when evaluating the `height`, we use our integrand function `f` instead of having the particular explicit formula. With this new quadrature function we can approximate a different integrand easily.

---

# Options, options

Our current function only integrates on \\(x \in [0, 1]\\). We can extend our function so it works on \\(x \in [a, b]\\), but make the *default values* be \\(x \in [0, 1]\\), so we don't need to always give them:

```python
def quadrature(f, nstrips, a=0, b=1):
    interval_width = b - a
    width = interval_width/nstrips
    integral = 0
    for point in range(nstrips):
        height = f(a + point*interval_width/nstrips)
        integral = integral + width * height
    return integral

print(quadrature(integrand_x_sq, 10))
print(quadrature(integrand_x_sq, 10, 0, 1))
print(quadrature(integrand_x_sq, 10, 0, 2))
```

```out
0.285
0.285
2.28
```

Notes: There are times where your algorithm will have "obvious" default values, which you want to use most, but not all, of the time. In all the examples so far we've integrated between zero and one. However, in general we'd want to be able to integrate on any domain. To do this we can add *default* values for parameters. In the line defining the function we add the parameter, but we assign it its default value (here, for example, the start of the interval is `a` which defaults to `0`). When the function is called, if we don't specify the value of the parameter then the default is used. If we do specify its value explicitly then the default is over-ridden. Many complex black-box algorithms, when implemented as Python functions, will have many parameters, most of which have sensible defaults. It's always worth checking the help to see how the behaviour of the function can be modified.


---

# Let's practice!

Notes: Mark this section as complete and move on to the exercises. Come back to these slides to refresh your memory if needed.
