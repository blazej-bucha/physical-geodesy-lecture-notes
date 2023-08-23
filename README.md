# Description

The source code of lecture notes on Physical Geodesy (in Slovak).

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


# Contributing

Did you find a typo or an error?  Do you find some topics missing or excessive?
Any contributions are welcome!


# Contact

Feel free to contact the author, Blazej Bucha, at
[blazej.bucha@stuba.sk](mailto:blazej.bucha@stuba.sk).
