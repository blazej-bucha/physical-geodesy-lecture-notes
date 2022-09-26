#!/bin/bash
set -e






# INPUTS
# ====================================================================

# Input GMT GRD file to be plotted.  To limit the size of the repository, this
# file is not distributed but can be obtained from the "grav-sr-2arcsec" model
# available at "https://zenodo.org/record/7074772".
grdfile="./h.grd"


# Output file without the file extension.  Create will be "ps" and "pdf" files.
outfile="../../latex/fig-h-grav-sr-2arcsec"


# Cartographic projection (projection_lon0/map_width_in_cm)
proj="M19.95/8c"


# Region to be plotted (min_lon/max_lon/min_lat/max_lat in degrees)
region="19.5/20.4/48.8/49.3"


# Geographic grid
geogrd="20mg20m/10mg10mWSen"


# Color scale
colorscale="globe"


# min/max/step values to create a color pallet
colorscale_lims="650/2500/10"


# min/max values of the colorbar
colorbar_minmax="650/2500"


# Step of colorbar values to be shown
colorbar_step="500"


# Colorbar label
colorbar_label=""


# Colorbar location
colorbar_loc="4c/-0.5c/8c/0.2"


# Colorbar position ("h" for horizontal, "v" for vertical)
colorbar_pos="h"


# Some further GMT stuff
gmt gmtset PAPER_MEDIA Custom_10.0cx9c
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

# Color pallet table file (deleted at the end of the script)
cptfile="data.cpt"


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
             -X1.3c \
             -Y1.5c \
             -E150 \
             -Q \
             -P > $outfile.ps


# Plot the SR borders
gmt psxy sr-border.txt -R$region -J$proj -W0.7,black -O -K -A >> $outfile.ps


# Add the colorbar
gmt psscale -C$cptfile \
            -D$colorbar_loc$colorbar_pos \
            -G$colorbar_minmax \
            -B$colorbar_step/:$colorbar_label: \
            -Y-0.3c \
            -O >> $outfile.ps


# Convert the output "ps" file to the "pdf" format.
gmt psconvert $outfile.ps -P -Tf

# ====================================================================






# Clean-up the mess
# ====================================================================

rm $cptfile
rm shading.int
rm gmt.history
rm gmt.conf
rm $outfile.ps

# ====================================================================
