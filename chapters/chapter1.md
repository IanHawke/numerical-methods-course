---
title: 'Chapter 1: Getting started'
description:
  'This chapter will teach you about many cool things and introduce you to the
  most important concepts of the course.'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Introduction" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>

<exercise id="2" title="Arithmetic">

What would you type in the terminal to compute \\(2.3^{4.5}\\)?

<choice id="ch1_q2">

<opt text="<code>pow(2.3, 4.5)</code>">

This would work in the C programming language, but not in Python.

</opt>
<opt text="<code>2.3^4.5</code>">

This would work in Matlab, but would give something very odd in Python.

</opt>
<opt text="<code>2.3**4.5</code>" correct="true">

This is correct: well done.

</opt>

</choice>

</exercise>

<exercise id="3" title="Variables">

How would you assign the value \\(42\\) to the variable <code>answer</code>?

<choice id="ch1_q3">

<opt text="<code>answer <- 42</code>">

This would work in the R programming language, but not in Python.

</opt>
<opt text="<code>answer = 42</code>" correct="true">

This is correct: well done.

</opt>
<opt text="<code>answer == 42</code>">

This compares the value of <code>answer</code> to <code>42</code>, but does not assign.

</opt>

</choice>

</exercise>

<exercise id="4" title="Reassigning variables">

What would be the value of the variable <code>x</code> after running the following code?

<pre><code>
x = 4
x = "Hello"
x = 5.5
x = 2 * x
</code></pre>

<choice id="ch1_q4">

<opt text="<code>4</code>">

Each line will change the value assigned to <code>x</code>.

</opt>
<opt text="<code>11.0</code>" correct="true">

This is correct: well done.

</opt>
<opt text="The code will fail with an error.">

Python allows you to re-assign a variable to different types. This code would fail in (e.g.) C, but is valid Python.

</opt>

</choice>

</exercise>

<exercise id="5" title="Loops">

Which of the following would start a loop in Python?

<choice id="ch1_q5">

<opt text="<code>for (i=0; i<10; i++) {</code>">

This would work in the C programming language, but not in Python.

</opt>
<opt text="<code>for i in range(10)</code>">

This is almost correct, but is missing the <code>:</code> at the end of the line.

</opt>
<opt text="<code>do i=0,9</code>">

This would work in the Fortran programming language, but not in Python.

</opt>
<opt text="None of the above." correct="true">

Correct. The <code>:</code> at the end of the line is essential, and the correct keywords are needed.

</opt>

</choice>

</exercise>

<exercise id="6" title="Values in loops">

After this code, what is the value of <code>x</code>?

<pre><code>
x = 0
for y in range(3):
    x = y**2 - 1
</code></pre>

<choice id="ch1_q6">

<opt text="<code>3</code>" correct="true">

This is correct: well done.

</opt>
<opt text="<code>8</code>">

This is almost correct, but you have got the end condition for the loop wrong. The <code>range</code> function will stop before <code>3</code>, so the final value of <code>y</code> is <code>2</code>.

</opt>
<opt text="<code>0</code>">

The value of <code>x</code> is changed within the loop and will be visible outside the loop.

</opt>

</choice>

</exercise>

<exercise id="7" title="Changing the quadrature point">

The code below was our code to approximate the quadrature of \\(x^2\\) using four strips, evaluating the integrand at the left of each strip.

Modify the code so that

- the integrand is evaluated in the middle of each strip;
- ten strips are used.

Make sure not to change any of the variable names.

<codeblock id="01_07">

The width of each strip is already computed, so the middle of the strip is at `point/nstrips + 0.5*width`.

</codeblock>

</exercise>


<exercise id="8" title="Changing the function">

We also want to compute
\\[
  \int_0^1 \text{d}x \\, \sqrt{1 - x^2}.
\\]

Modify the skeleton code so that

- the integrand is evaluated at the *left edge* of the strip;
- the integrand is changed to compute the square root above;
- \(100\) strips are used.

Make sure the value of the integrand is stored in the variable `height`, and the final approximation to the integral is stored in the variable `integral`.

<codeblock id="01_08">

The square root can be computed by using an exponent of `1/2`, meaning the integrand in this case can be coded as `(1 - x**2)**(1/2)`.

</codeblock>

</exercise>
