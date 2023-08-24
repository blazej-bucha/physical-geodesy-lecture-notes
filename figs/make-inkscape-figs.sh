#!/bin/bash

# DESCRIPTION:  Generates "pdf" and "pdf_tex" from all inkscape files stored
# within the directories of this folder.


set -e


SH_FILE="make_pdf_tex.sh"


for DIR in `ls -d */`
do
    echo "Processing the \"$DIR\" directory..."

    cd $DIR

    if test -f "$SH_FILE"; then
        ./$SH_FILE
    fi

    cd ..
done


echo "Done!"
