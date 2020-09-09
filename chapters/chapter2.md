---
title: 'Chapter 2: Functions and packages'
description:
  'Extending the quadrature example to make our method more general.'
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Functions" type="slides">

<slides source="chapter2_01_functions">
</slides>

</exercise>

<exercise id="2" title="Testing">

Recap: which of the following would assign the value of <code>3</code> to the variable <code>integrand</code>?

<choice id="ch2_q2">

<opt text="<code>integrand <- 3</code>">

This would work in <code>R</code> but not in Python.

</opt>
<opt text="<code>integrand == 3</code>">

In Python two equals signs compares the value on the left to that on the right. If <code>integrand</code> already has a value this would do that comparison and return <code>True</code> or <code>False</code>. If <code>integrand</code> does not yet have a value this would give an error.

</opt>
<opt text="<code>integrand = 3</code>" correct="true">

That's correct: in Python a single equals sign assigns the value on the right to the variable name on the left.

</opt>
<opt text="None of the above">

No: one of the above will work in Python.

</opt>

</choice>

</exercise>

<exercise id="3" title="Functions">

Which of the following would be the first line to define a function with name <code>my_add</code>?

<choice id="ch2_q3">

<opt text="<code>int my_add(a, b) {</code>">

This would work in <code>C</code> but not in Python.

</opt>
<opt text="<code>my_add def(a, b):</code>">

This has flipped around the keyword and function name.

</opt>
<opt text="<code>def my_add(a, b):</code>" correct="true">

That's correct: the keyword is <code>def</code> and there must be a <code>:</code> at the end of the line. Remember to indent the body of the code by four spaces.

</opt>
<opt text="None of the above">

No: one of the above will work in Python.

</opt>

</choice>

</exercise>

<exercise id="4" title="Returning">

Which of the following would be the last line of the function <code>my_add</code>, sending back the value of <code>a+b</code>?

<choice id="ch2_q4">

<opt text="<code>print(a + b)</code>">

This prints the value to the screen, but does not send the value back to the caller.

</opt>
<opt text="<code>return a + b</code>" correct="true">

This is correct. No code in the function after the <code>return</code> statement will run.

</opt>
<opt text="<code>a + b</code>">

This does not work in Python. Some programming languages will return the value of the last line in the function, but Python requires you to be explicit as to what you send back.

</opt>
<opt text="None of the above">

No: one of the above will work in Python.

</opt>

</choice>

</exercise>

<exercise id="5" title="Defining the integrand">

Our quadrature example involved approximating
\\[
  \int_0^1 \text{d}x \\, \sqrt{1 - x^2}.
\\]
Write a function to evaluate the integrand, given \\(x\\).

Modify the skeleton code so that

- the function is defined;
- the function returns the \\(\sqrt{1 - x^2}\\).

Make sure the function defined is called `integrand_1` and that it takes a single input, `x`.

<codeblock id="02_05">

The square root can be computed by using an exponent of `1/2`, meaning the integrand in this case can be coded as `(1 - x**2)**(1/2)`.

</codeblock>

</exercise>

<exercise id="6" title="Options">

The arguments to functions can be given default values. When calling the function we can refer to arguments by name. Consider our <code>quadrature</code> function

<pre><code>
def quadrature(f, nstrips, a=0, b=1):
    ...
    return integral
</code></pre>

Which of the following would <em>not</em> be a valid way of calling the function?

<choice id="ch2_q6">

<opt text="<code>quadrature(integrand_1, 100, a=0.5)</code>">

This is a valid way of calling the function. The value for <code>b</code> will be its default, <code>1</code>

</opt>
<opt text="<code>quadrature(integrand_1, b=2, nstrips=100)</code>">

This is valid way of calling the function. The first argument is not explicitly called <code>f</code>, but that's fine. The other arguments are called out of order, but are explicitly referred to, so Python can work out what argument should have what value. <code>a</code> is not given a value so takes its default.

</opt>
<opt text="<code>quadrature(f=integrand_1, 100, b=2)</code>" correct="true">

Correct: this is not valid in Python. Even though the arguments seem to be in the obvious order, as soon as one argument is explicitly referred to by name (as <code>f</code> is here), all following arguments must be as well.

</opt>
<opt text="None of the above">

No: one of the above is not valid in Python.

</opt>

</choice>

</exercise>

<exercise id="7" title="Using numpy">

Our quadrature example involved approximating
\\[
  \int_0^1 \text{d}x \\, \sqrt{1 - x^2}.
\\]
We wrote a function to evaluate the integrand, given \\(x\\). However, `numpy` has built-in functions to compute the square root, which (as we'll see later) are more powerful than working on a single variable.

Modify the skeleton code so that

- `numpy` is imported with the short name `np`;
- the function is defined;
- the function uses a `numpy` function to compute the square root;
- the function returns the \\(\sqrt{1 - x^2}\\).

Make sure the function defined is called `integrand_1` and that it takes a single input, `x`.

<codeblock id="02_07">

To find functions in `numpy` use some form of the help. If you have a good idea what the function is called, type the first few characters and press the `Tab` key: Python will show you options. So, type `np.s` and then `Tab` to see all functions starting `s`. Alternatively, use the help tab in Spyder, or use Google or similar.

</codeblock>

</exercise>
