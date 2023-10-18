# Import modulov
import numpy as np
import matplotlib.pyplot as plt
import shutil

# Ak je dostupný LaTeX, bude použitý na zobrazenie popisu vo výslednom obrázku
if shutil.which('latex') is not None: plt.rc('text', usetex=True)

# Výpočtová oblasť
xmin, xmax, xn = -1.0, 1.0, 101  # Min., max. a počet hodnôt v smere osi "x"
ymin, ymax, yn = xmin, xmax, xn  # Min., max. a počet hodnôt v smere osi "y"

# Zobrazený bude každý "xngrad" a "yngrad" gradient v smere osí "x" a "y"
xngrad, yngrad = 10, 10

# Tvorba gridu
x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))

# Výpočet skalárnej funkcie
f = np.sin(2.0 * x) + np.cos(2.0 * y)

# Výpočet gradientu skalárnej funkcie "f" (derivácií "f" podľa "x" a "y")
fx =  2.0 * np.cos(2.0 * x)
fy = -2.0 * np.sin(2.0 * y)

# Vykreslenie
fig, ax = plt.subplots(figsize=(10.0 / 2.54, 8.0 / 2.54))
im = ax.imshow(f, extent=(xmin, xmax, ymin, ymax), cmap='bwr',
               vmin=-np.abs(f).max(), vmax=np.abs(f).max())
cntr = ax.contour(x, y, f, colors='black', linewidths=0.6)
ax.clabel(cntr, inline=True, fontsize=10)
ax.quiver( x[::xngrad, ::xngrad],  y[::yngrad, ::yngrad],
          fx[::xngrad, ::xngrad], fy[::yngrad, ::yngrad])
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xticks(np.linspace(xmin, xmax, 6))
ax.set_yticks(np.linspace(ymin, ymax, 6))
fig.colorbar(im)
plt.tight_layout()
fig.savefig('./fig-gradient.pdf')
