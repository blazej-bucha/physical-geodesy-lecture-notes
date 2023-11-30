# Description

The source code of the lecture notes on Physical Geodesy (in Slovak).

Starting with Newton's law of gravitation, discussed are fundamental quantities
and concepts of Physical Geodesy such as the gravitational potential, the
gravitational vector and the equipotential surfaces.  The next two chapters are
centered around spherical and spheroidal harmonic expansions of the Earth's
external gravitational field, focusing on Legendre polynomials, Legendre
functions, spherical harmonics and their normalization.  Next, introduced are
the normal and the disturbing gravity field, after which the basic concepts of
the geoid determination are discussed.


# Compilation

```bash
git clone https://github.com/blazej-bucha/physical-geodesy-lecture-notes
cd physical-geodesy-lecture-notes/latex
pdflatex lecture-notes.tex
biber lecture-notes.bcf
pdflatex lecture-notes.tex
```


# Notes

* The textbook is written in LaTeX using UTF-8 encoding.

* The figures are drawn in Inkscape.

* The maps are produced using GMT.

* The numerical examples are written in Python (require NumPy, Matplotlib and
  SciPy) and MATLAB.


# Final Published Version

The final published version is available at
[https://www.svf.stuba.sk/buxus/docs/dokumenty/skripta/2023/Fyzikalna_geodezia.pdf](https://www.svf.stuba.sk/buxus/docs/dokumenty/skripta/2023/Fyzikalna_geodezia.pdf).

To reduce eye strain, you may want to use dark mode when reading the lecture
notes.  On Android, [Book Reader](https://gitlab.com/axet/android-book-reader)
works nicely.  On a desktop PC, color rendering can be inverted in, for
instance, [MuPDF](https://mupdf.com/), a lightweight keyboard-oriented PDF
viewer.  Undoubtedly, there are many other applications supporting dark mode.
Use whichever works best for you, but use one.


# Citing

The lecture notes can be cited as

> Bucha B, 2023. Fyzikálna geodézia [Physical Geodesy]. 1st edn. Spektrum STU,
> Bratislava, p 184. ISBN 978-80-227-5368-5.


# Licensing

The source of the lecture notes is published under the BSD-3-Clause license.
The final published version is licensed under CC BY 4.0.  Either way, you are
free to use, share, adapt, distribute and reproduce both the source code and
the final published version within the license terms.


# Contributing

Did you find a typo or an error?  Do you find some topics missing or excessive?
Any feedback is appreciated!


# Contact

Feel free to contact the author, Blazej Bucha, at
[blazej.bucha@stuba.sk](mailto:blazej.bucha@stuba.sk).
