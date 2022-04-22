#!/bin/bash

set -e

inkscape -D ./reduced-ell-coords.svg  -o ../../latex/fig-reduced-ell-coords.pdf --export-latex
