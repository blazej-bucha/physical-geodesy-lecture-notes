#!/bin/bash

set -e

inkscape -D ./deflections.svg  -o ../../latex/fig-deflections.pdf --export-latex
