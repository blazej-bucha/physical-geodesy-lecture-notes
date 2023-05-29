#!/bin/bash

set -e

inkscape -D ./homogeneous-ball-out.svg  -o ../../latex/fig-homogeneous-ball-out.pdf --export-latex
inkscape -D ./homogeneous-ball-in.svg  -o ../../latex/fig-homogeneous-ball-in.pdf --export-latex
