---
title: 'Chapter 4: plotting'
description:
  'When we check are results we would like to clearly communicate when, and how, they are correct. This is often best done with a plot.'
prev: /chapter3
next: /chapter1
type: chapter
id: 4
---

<exercise id="1" title="matplotlib" type="slides">

<slides source="chapter4_01_matplotlib">
</slides>

</exercise>

<exercise id="2" title="Plotting a line">

Plot \\(\sin(x)\\) against \\(x \\in [0, 10]\\).

Modify the skeleton code so that

- `numpy` is imported with the short name `np`;
- `matplotlib.pyplot` is imported with the short name `plt`;
- the grid `x` is evenly spaced with `50` points;
- the plot appears on the screen.

<codeblock id="04_02">

Check against the slides.

</codeblock>

</exercise>

<exercise id="3" title="Labels and ranges">

Plot \\(\sin(x)\\) against \\(x \\in [0, 10]\\). Add axis labels, a title, and fix the limits in \\(x\\) to \\([1, 8]\\).

Modify the skeleton code so that

- `numpy` is imported with the short name `np`;
- `matplotlib.pyplot` is imported with the short name `plt`;
- the grid `x` is evenly spaced with `50` points;
- the axis labels are `x` and `$\sin(x)$` as appropriate;
- the title is `Titled plot`;
- the `x` limits are as required;
- the plot appears on the screen.

<codeblock id="04_03">

Check against the slides.

</codeblock>

</exercise>

</exercise>

<exercise id="4" title="Multiple plots">

Plot \\(\sin(x)\\) and \\(\cos(2x)\\) against \\(x \\in [0, 10]\\). Add axis labels and a legend. The \\(\sin\\) curve should be solid and black. The \\(\cos\\) curve should be dashed and blue.

Modify the skeleton code so that

- `numpy` is imported with the short name `np`;
- `matplotlib.pyplot` is imported with the short name `plt`;
- the grid `x` is evenly spaced with `50` points;
- the axis labels are `x` and `$f(x)$` as appropriate;
- the line styles are as required;
- the legend appears in the default position and matches the function, `$\sin(x)$` or `$\cos(2x)$`, as appropriate;
- the plot appears on the screen.

<codeblock id="04_04">

Check against the slides.

</codeblock>

</exercise>

<exercise id="5" title="Subplots" type="slides">

<slides source="chapter4_02_matplotlib_subplots">
</slides>

</exercise>

<exercise id="6" title="Subplots">

Plot \\(x^3\\) against \\(x \\in [10^{-4}, 10]\\). Two subplots should be created. The left subplot should use linear scales. The right subplot should use logarithmic scales. The \\(x\\) axis should be labelled `x` for both subplots. Otherwise, defaults should be used.

Modify the skeleton code so that

- `numpy` is imported with the short name `np`;
- `matplotlib.pyplot` is imported with the short name `plt`;
- the grid `x` is evenly spaced with `50` points;
- the axis labels are `x` as appropriate;
- two subplots with appropriate scales appear in one row;
- the plot appears on the screen.

<codeblock id="04_06">

Check against the slides.

</codeblock>

</exercise>
