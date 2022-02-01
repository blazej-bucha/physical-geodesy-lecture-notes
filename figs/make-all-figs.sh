#!/bin/bash

# DESCRIPTION:  Generates "pdf" and "pdf_tex" files for all inkscape figures in 
# a single run.


set -e


# List of directories with inkscape figures
DIRS="./analytical-continuation/
      ./coordinate-systems/
      ./gg-n-point-masses/
      ./gravitating-body/
      ./newton-law/"


for DIR in $DIRS
do
    echo "Processing the \"$DIR\" directory..."
    cd $DIR

    ./make_pdf_tex.sh

    cd ..
done


echo "Done!"
