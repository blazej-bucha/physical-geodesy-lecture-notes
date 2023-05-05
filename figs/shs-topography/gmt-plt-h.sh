#!/bin/bash
set -e






# INPUTS
# ====================================================================

# Prefix of the input files to be plotted.  To limit the size of the
# repository, these files are not distributed but can be obtained by executing
# the "../../matlab/shs_h.m" script
infile="topography-nmax"


# Maximum harmonic degrees (suffices in "infile")
nmax="30 90 360"


# Output file without the file extension.  Create will be "ps" and "pdf" files.
outfile="../../latex/fig-h-shs"


# Cartographic projection (projection_lon0/map_width_in_cm)
proj="W180/11c"


# Region to be plotted (min_lon/max_lon/min_lat/max_lat in degrees)
region="0.0/360.0/-90.0/90.0"


# Geographic grid
geogrd="60dg60d/30dg30dWSen"


# Color scale
colorscale="viridis"


# min/max/step values to create a color pallet
colorscale_lims="-8000/5000/70"


# min/max values of the colorbar
colorbar_minmax="-8000/5000"


# Step of colorbar values to be shown
colorbar_step="2000"


# Colorbar label
colorbar_label=""


# Colorbar location
colorbar_loc="5.5c/-0.5c/11c/0.2"


# Colorbar position ("h" for horizontal, "v" for vertical)
colorbar_pos="h"


# Some further GMT stuff
gmt gmtset PAPER_MEDIA Custom_12cx7c
gmt gmtset MAP_ORIGIN_X 0c
gmt gmtset MAP_ORIGIN_Y 0c
gmt gmtset ANNOT_FONT_SIZE_PRIMARY 8p
gmt gmtset FONT_LABEL 8p
gmt gmtset FRAME_WIDTH 0.1c
gmt gmtset TICK_PEN 0.25p
gmt gmtset FRAME_PEN 0.5p
gmt gmtset TICK_LENGTH 0.075c

# ====================================================================






for N in $nmax
do
    # GMT plotting
    # ====================================================================
    echo "Plotting $infile$N.txt..."


    # Color pallet table file (deleted at the end of the script)
    cptfile="data.cpt"


    # Create a GMT GRD file to be plotted
    grdfile="plt-tmp.grd"
    gmt xyz2grd $infile$N.txt -G$grdfile -R$region -rg -I0.25/0.25 -fg -:


    # Create a shading effect
    gmt grdgradient $grdfile -Gshading.int -A45 -Ne0.6


    # Create a color pallet
    gmt grd2cpt $grdfile -C$colorscale -S$colorscale_lims -Z > $cptfile


    if [ $N = "360" ]
    then
        # Plot the grid
        outfile_tmp=$outfile-nmax$N.ps
        gmt grdimage $grdfile \
                     -C$cptfile \
                     -R$region \
                     -J$proj \
                     -B$geogrd \
                     -Ishading.int \
                     -K \
                     -X0.7c \
                     -Y1.2c \
                     -E200 \
                     -Q \
                     -P > $outfile_tmp


        # Add the colorbar
        gmt psscale -C$cptfile \
                    -D$colorbar_loc$colorbar_pos \
                    -G$colorbar_minmax \
                    -B$colorbar_step/:$colorbar_label: \
                    -Y-0.0c \
                    -O >> $outfile_tmp
    else
        # Plot the grid
        outfile_tmp=$outfile-nmax$N.ps
        gmt grdimage $grdfile \
                     -C$cptfile \
                     -R$region \
                     -J$proj \
                     -B$geogrd \
                     -Ishading.int \
                     -X0.7c \
                     -Y1.2c \
                     -E200 \
                     -Q \
                     -P > $outfile_tmp
    fi


    # Convert the output "ps" file to the "pdf" format.
    gmt psconvert $outfile_tmp -P -Tf


    rm $outfile_tmp

    # ====================================================================
done






# Clean-up the mess
# ====================================================================

rm $grdfile
rm $cptfile
rm shading.int
rm gmt.history
rm gmt.conf

# ====================================================================
