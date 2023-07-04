# Import modulov
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

# Výpočtová oblasť
xmin, xmax = -1.0, 1.0
xn         = 101     # Počet vzorkovacích bodov na intervale "[xmin, xmax]"
ymin, ymax = xmin, xmax
ymax       = xmax
yn         = xn      # Počet vzorkovacích bodov na intervale "[ymin, ymax]"
xngrad     = 10      # Zobrazený bude každý "xngrad" gradient v smere osi "x"
yngrad     = xngrad  # Zobrazený bude každý "yngrad" gradient v smere osi "y"

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
