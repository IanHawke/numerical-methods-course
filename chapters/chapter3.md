---
title: 'Chapter 3: numpy'
description:
  'For numerical work we save a lot of time and effort using the powerful numpy package. We will rewrite and extend our quadrature examples using that.'
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="numpy" type="slides">

<slides source="chapter3_01_numpy">
</slides>

</exercise>

<exercise id="2" title="Defining a vector">

Which of the following defines a valid <code>numpy</code> array? The code run before this line would be

<pre><code>
import numpy as np
l1 = [1, 2, 3]
l2 = [1, 2, "3"]
</code></pre>

<choice id="ch3_q2">

<opt text="<code>x = array(l1)</code>">

This will not work as <code>array</code> is a <code>numpy</code> function, so must be referred to as <code>np.array</code>.

</opt>
<opt text="<code>x = np.array(l1)</code>" correct="true">

Yes, this would be the syntax to define an array from a list.

</opt>
<opt text="<code>x = np.array(l2)</code>">

This will not work as <code>numpy</code> arrays must contain the same type of variable. In the list <code>l2</code> there are numbers (integers, such as <code>1</code>) but also a string (<code>"3"</code>), so this will fail.

</opt>

</choice>

</exercise>

<exercise id="3" title="Modifying a grid">

We can use standard code to define a grid with <code>100</code> points on \\([0, 1]\\) without an endpoint as

<pre><code>
import numpy as np
x, dx = np.linspace(0, 1, num=100, endpoint=False, retstep=True)
</code></pre>

What one line of code would give the location, <code>loc</code>, half way between the tenth and eleventh gridpoint?

<choice id="ch3_q3">

<opt text="<code>loc = (x[10] + x[11]) / 2</code>">

This will not work as the tenth gridpoint is <code>x[9]</code> (remember, Python starts indexing from zero). It is also not safe on general domains, as the approach would not work if the domain did not start at zero.

</opt>
<opt text="<code>loc = x[9] + dx / 2</code>" correct="true">

Yes, this works as Python starts indexing from zero.

</opt>
<opt text="<code>loc = x[10] + dx / 2</code>">

This will not work as the tenth gridpoint is <code>x[9]</code> (remember, Python starts indexing from zero).

</opt>

</choice>

</exercise>

<exercise id="4" title="More numpy functions">

Define the same grid as the previous question.

<pre><code>
import numpy as np
x, dx = np.linspace(0, 1, num=100, endpoint=False, retstep=True)
</code></pre>

What one line of code would compute \\(\sin(\log(x^2 + 1))\\) at every gridpoint?

<choice id="ch3_q4">

<opt text="<code>sin(log(x**2 + 1))</code">

This will not work as <code>sin</code> and <code>log</code> are not basic Python functions. You have to get them from <code>numpy</code>.

</opt>
<opt text="<code>np.sin(log(x**2 + 1))</code>">

This will not work as <em>every</em> function needs to explicitly say where it comes from, so we need to specify that <code>log</code> is also a <code>numpy</code> function.

</opt>
<opt text="<code>np.sin(np.log(x**2 + 1))</code>" correct="true">

This works, computing a moderately complex function quickly and easily.

</opt>

</choice>

</exercise>

<exercise id="5" title="Quadrature function in numpy">

Write a function to approximate
\\[
  I = \\int_a^b \\text{d}x \\, f(x).
\\]
It should use the simple approximation
\\[
  I \simeq \Delta x \sum\_{i=0}^{\text{nstrips}-1} f(x\_{i})
\\]
where \\(\text{nstrips}\\) is the number of strips and \\(\\Delta x\\) their width.

Modify the skeleton code so that

- `numpy` is imported with the short name `np`;
- the function `quadrature` is defined;
- the function uses a `numpy` function to compute the sum;
- the function returns the quadrature.

Make sure the function defined is called `quadrature` and that it takes as arguments the integrand `f`, the start `a` and end `b` of the domain, and the number of strips `nstrips`.

<codeblock id="03_05">

Compare your function to the code examples on the slide. Remember, we are using the Riemann integral, not the trapezoidal rule, so we do not want a gridpoint at the end of the domain.

</codeblock>

</exercise>

<exercise id="6" title="More slicing">

Define the same grid as in earlier questions.

<pre><code>
import numpy as np
x, dx = np.linspace(0, 1, num=100, endpoint=False, retstep=True)
</code></pre>

What one line of code would return an array containing every third point, starting from the second?

<choice id="ch3_q6">

<opt text="<code>x[1:3]</code">

This does not work as it has send the end point to <code>3</code>, not the step between points. You need to add another <code>:</code>. The slicing notation is <code>x[start:end:step]</code>, where obvious default values are used if a value is not given.

</opt>
<opt text="<code>x[1::3]</code>" correct="true">

This works as the end point does not need to be given.

</opt>
<opt text="<code>x[2::3]</code>">

This has the wrong start point. Remember, Python indexing starts from zero, so the second point has index <code>1</code>.

</opt>

</choice>

</exercise>

<exercise id="7" title="Simpson's Rule">

Write a function to implement Simpson's Rule which approximates the quadrature as
\\[
  I \simeq \frac{\Delta x}{3} \left[ f(x\_0) + f(x\_{2 \text{nstrips}}) + 4 \sum\_{i \\text{ odd}} f(x\_{i}) + 2 \sum\_{i \\text{ even}} f(x\_{i}) \right].
\\]
Here \\(\text{nstrips}\\) is the number of strips, and \\(\\Delta x\\) the grid spacing. In terms of gridpoints, there must be three gridpoints in each strip, one at each end and one in the middle. This means the total number of gridpoints is \\(2 \text{nstrips} + 1\\), which includes one at the end. The first and last points do not appear in the sums.

Modify the skeleton code so that

- `numpy` is imported with the short name `np`;
- the function `simpson` is defined;
- the function uses a `numpy` function to compute the sum;
- the function returns the quadrature.

Make sure the function defined is called `simpson` and that it takes as arguments the integrand `f`, the start `a` and end `b` of the domain, and the number of strips `nstrips`.

<codeblock id="03_07">

Compare your function to the trapezoidal rule code examples on the slide.

</codeblock>

</exercise>
