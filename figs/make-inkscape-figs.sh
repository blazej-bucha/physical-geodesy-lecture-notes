#!/bin/bash

# DESCRIPTION:  Generates "pdf" and "pdf_tex" files for all inkscape figures in 
# a single run.


set -e


# List of directories with inkscape figures
DIRS="./analytical-continuation/
      ./coordinate-systems/
      ./distance-l/
      ./equipotenital-surfaces/
      ./gg-n-point-masses/
      ./gravitating-body/
      ./gravity-vector/
      ./newton-law/
      ./orbital-motion-ideal/
      ./orbital-motion-real/
      ./spherical-harmonics-convergence/
      ./unit-vectors/"


for DIR in $DIRS
do
    echo "Processing the \"$DIR\" directory..."
    cd $DIR

    ./make_pdf_tex.sh

    cd ..
done


echo "Done!"
