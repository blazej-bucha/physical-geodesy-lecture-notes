#!/bin/bash

set -e

inkscape -D ./geoid.svg  -o ../../latex/fig-geoid.pdf --export-latex
