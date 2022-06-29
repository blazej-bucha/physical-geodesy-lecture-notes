#!/bin/bash

set -e

inkscape -D ./heights.svg  -o ../../latex/fig-heights.pdf --export-latex
