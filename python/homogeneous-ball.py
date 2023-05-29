# Import modulov
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

G    = 6.67430 * 10**-11  # Newtonova gravitačná konštanta (jednotky
                          # "m**3 * kg**-1 * s**-2")
M    = 5.9722 * 10**24    # Hmotnosť Zeme ("kg")
dr   = 10.0**5            # Krok vo sférickom sprievodiči ("m")
R    = 6378137.0          # Polomer Zeme ("m")
rmax = 2.5 * 10**7        # Maximálny sférický sprievodič ("m")

GM = G * M  # Geocentrická gravitačná konštanta ("m**3 * s**-2")

# Diskretizácia výpočtovej oblasti vo vnútri gule ("ri") a mimo gule ("ro")
ri = np.arange(0.0, np.floor(R / dr) * dr + dr, dr, dtype=np.float64)
ro = np.arange(np.ceil(R / dr) * dr, rmax + dr, dtype=np.float64)

# Gravitačný potenciál a gravitačné zrýchlenie vo vnutri gule
Vgi = (GM / 2.0) * (3.0 / R - ri**2 / R**3)
ggi = (GM / R**3) * ri

# Gravitačný potenciál a gravitačné zrýchlenie na povrchu gule
VgR = GM / R
ggR = GM / R**2

# Gravitačný potenciál a gravitačné zrýchlenie mimo gule
Vgo = GM / ro
ggo = GM / ro**2

# Spojenie výsledkov do polí pre jednoduché vykreslenie
r  = np.hstack((ri, R,  ro))     # Sférický sprievodič
Vg = np.hstack((Vgi, VgR, Vgo))  # Gravitačný potenciál
gg = np.hstack((ggi, ggR, ggo))  # Gravitačné zrýchlenie

# Vykreslenie
blue   = 'tab:blue'    # Farba pre zobrazenie gravitačného potenciálu
orange = 'tab:orange'  # Farba pre zobrazenie gravitačného zrýchlenia

fig, ax1 = plt.subplots(figsize=(13.0 / 2.54, 9.0 / 2.54))
ax1.plot(r, Vg, color=blue)
ax1.set_ylabel('$V_{\mathrm{g}} \ (\mathrm{m}^2 \ \mathrm{s}^{-2})$',
               color=blue)
ax1.tick_params(axis='y', colors=blue)

ax2 = ax1.twinx()  # Pridanie druhej vertikálnej osi
ax2.plot(r, gg, color=orange)
ax2.set_ylabel('$\| \mathbf{g}_{\mathrm{g}} \| \ ' +
               '(\mathrm{m} \ \mathrm{s}^{-2})$',
               color=orange)
ax2.spines['right'].set_color(orange)
ax2.spines['left'].set_color(blue)
ax2.tick_params(axis='y', colors=orange)

ylim = ax2.get_ylim()
ax2.set_ylim(ylim)
ax2.set_xlim([0, rmax])

# Vyznačenie oblasti vo vnútri homogennej gule
ax2.axhspan(ylim[0], ylim[1], xmin=0, xmax=R / rmax, facecolor='0', alpha=0.15)

ax1.set_xlabel('$r \ (\mathrm{m})$')
fig.savefig('./fig-homogeneous-ball-vg-gg.pdf')

