# Import modulov
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.special import lpmv

# Sférický harmonický stupeň "n" a sférický harmonický rád "k"
n, k = 3, 1

# "False" pre zobrazenie na jednotkovej sfére, "True" pre zobrazenie pomocou
# odhľahlostí od jednotkovej sféry
zobrazenie_3d = True

# Tvorba gridu na jednotkovej sfére
lat      = np.linspace(-np.pi / 2.0, np.pi / 2.0, 181)
lon      = np.linspace(0.0, 2.0 * np.pi, 361)
lon, lat = np.meshgrid(lon, lat)

# Výpočet nenormovanej Legendreovej funkcie stupňa "n" a rádu "|k|"
pnk = lpmv(np.abs(k), n, np.sin(lat))

# Výpočet sférickej harmonickej funkcie
if k >= 0:
    ynk = pnk * np.cos(k * lon)
else:
    ynk = pnk * np.sin(np.abs(k) * lon)

# Odstránenie Condonovho-Shortleyho fázového faktora
ynk *= (-1)**np.abs(k)

# Sprievodič
if zobrazenie_3d:
    # Zobrazenie odľahlosťami od jednotkovej sféry.
    #
    # Hodnota "1.0" reprezentuje polomer jednotkovej sféry.  Hodnota "0.5" je
    # amplitúdový faktor, ktorý pre účely zobrazenia pozmení amplitúdu
    # oscilácií sférických harmonických funkcií tak, aby bol zreteľný
    # zobrazovaný tvar.  Člen "ynk / np.abs(ynk).max()" zabezpečuje, že
    # hodnoty "ynk" sa budú nachádzať v jednotnom intervale "[-1.0, 1.0]" pre
    # ľubovoľné "n" a "k", čo je opäť výhodné pre vizualizačné účely.
    r = 1.0 + 0.5 * ynk / np.abs(ynk).max()
else:
    r = 1.0  # Zobrazenie na jednotkovej sfére

# Transformácia sférických súradníc na pravouhlé súradnice
x = r * np.cos(lat) * np.cos(lon)
y = r * np.cos(lat) * np.sin(lon)
z = r * np.sin(lat)

# Vykreslenie
fig, ax = plt.subplots(figsize=(4.0 / 2.54, 4.0 / 2.54),
                       subplot_kw={'projection': '3d'})
ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))
norm = mpl.colors.Normalize()
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.cm.bwr,
                facecolors=plt.cm.bwr(norm(ynk)))
ax.set_axis_off()
ax.set_rasterized(True)
plt.tight_layout(pad=-2.0)

# Názov výstupného súboru
fileout = f'./fig-spherical-harmonic-n{n}-k{k}'
if zobrazenie_3d:
    fileout += '-3d'
fileout += '.pdf'
fig.savefig(fileout, dpi=300)
