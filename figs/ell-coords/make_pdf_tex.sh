#!/bin/bash

set -e

inkscape -D ./ell-coords.svg  -o ../../latex/fig-ell-coords.pdf --export-latex
