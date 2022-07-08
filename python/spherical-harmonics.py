# Import modulov
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.special import lpmv

# Sférický harmonický stupeň "n" a rád "k"
n = 3
k = 1

# "False" pre zobrazenie na jednotkovej sfére, "True" pre zobrazenie pomocou
# odhľahlostí od jednotkovej sféry
zobrazenie_3d = True

# Tvorba gridu na jednotkovej sfére
lat      = np.linspace(-np.pi / 2.0, np.pi / 2.0, 181)
lon      = np.linspace(0.0, 2.0 * np.pi, 361)
lon, lat = np.meshgrid(lon, lat)

# Výpočet sférickej harmonickej funkcie
if k >= 0:
    ynm = lpmv(k, n, np.sin(lat)) * np.cos(k * lon)
else:
    ynm = lpmv(np.abs(k), n, np.sin(lat)) * np.sin(np.abs(k) * lon)

# Odstránenie Condon--Shortley fázového faktora
ynm *= (-1)**np.abs(k)

# Sprievodič
if zobrazenie_3d:
    r = 1.0 + 0.5 * ynm / np.abs(ynm).max()
else:
    r = 1.0

# Transformácia sférických súradnic na pravouhlé suradnice
x = r * np.cos(lat) * np.cos(lon)
y = r * np.cos(lat) * np.sin(lon)
z = r * np.sin(lat)

# Vykreslenie
fig, ax = plt.subplots(figsize=(4.0 / 2.54, 4.0 / 2.54),
                       subplot_kw={"projection": "3d"})
ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))
norm = mpl.colors.Normalize()
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.cm.bwr,
                facecolors=plt.cm.bwr(norm(ynm)))
ax.set_axis_off()
ax.set_rasterized(True)
plt.tight_layout(pad=-2.0)
plt.show()

# Nazov výstupného súboru
fileout = "./fig-spherical-harmonic-n%d-k%d" % (n, k)
if zobrazenie_3d:
    fileout += "-3d.pdf"
else:
    fileout += ".pdf"
fig.savefig(fileout, dpi=300)
