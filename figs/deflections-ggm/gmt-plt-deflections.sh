#!/bin/bash
set -e






# INPUTS
# ====================================================================

# -----------------------------------------------------------------------------
#
# NOTE: Due to their size, the input data files to plot the deflections of the
# vertical are not a part of the repository.  They can be, however, easily
# computed, say, as an exercise.
#
# -----------------------------------------------------------------------------


# Prefix of the output file names include the path.  Create will be a "pdf"
# files.
outfile_prefix="../../latex/fig-"


# Cartographic projection (projection_lon0/map_width_in_cm)
proj="W180/11c"


# Region to be plotted (min_lon/max_lon/min_lat/max_lat in degrees)
region="0.0/360.0/-90.0/90.0"


# Geographic grid
geogrd="60dg60d/30dg30dWSen"


# Color scale
colorscale="viridis"


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






# GMT plotting
# ====================================================================
for file in `ls deflections-*.txt`
do
    # Prepare the input and output file names (no suffices)
    infile=$(basename $file ".txt")
    outfile=$outfile_prefix$infile


    echo "Plotting $infile.txt..."


    if [[ "$file" == "deflections-theta.txt" ]]; then
        # Use a different colorscale for total deflections of the vertical
        colorscale_lims="0/20/1"
        colorbar_minmax="0/20"
        colorbar_step="5"
    else
        colorscale_lims="-20/20/1"
        colorbar_minmax="-20/20"
        colorbar_step="5"
    fi


    # Color pallet table file (deleted at the end of the script)
    cptfile="data.cpt"


    # Create a GMT GRD file to be plotted
    grdfile="plt-tmp.grd"
    gmt xyz2grd $infile.txt -G$grdfile -R$region -rg -I0.25/0.25 -fg -:


    # Create a shading effect
    gmt grdgradient $grdfile -Gshading.int -A45 -Ne0.6


    # Create a color pallet
    gmt grd2cpt $grdfile -C$colorscale -S$colorscale_lims -Z > $cptfile


    # Plot the grid
    gmt grdimage $grdfile \
                 -C$cptfile \
                 -R$region \
                 -J$proj \
                 -B$geogrd \
                 -Ishading.int \
                 -K \
                 -X0.6c \
                 -Y1.2c \
                 -E200 \
                 -Q \
                 -P > $outfile.ps

    # Add the colorbar
    gmt psscale -C$cptfile \
                -D$colorbar_loc$colorbar_pos \
                -G$colorbar_minmax \
                -B$colorbar_step/:$colorbar_label: \
                -Y-0.0c \
                -O >> $outfile.ps


    # Convert the output "ps" file to the "pdf" format.
    gmt psconvert $outfile.ps -P -Tf


    rm $outfile.ps
done

# ====================================================================






# Clean-up the mess
# ====================================================================

rm $grdfile
rm $cptfile
rm shading.int
rm gmt.history
rm gmt.conf

# ====================================================================
