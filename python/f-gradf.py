# Import modulov
import numpy as np
import matplotlib.pyplot as plt

# Výpočtová oblasť
xmin   = -1.0
xmax   =  1.0
xn     = 101  # Počet vzorkovacích bodov funkcie "f" na intervale "[xmin, xmax]"
ymin   = xmin
ymax   = xmax
yn     = xn  # Počet vzorkovacích bodov funkcie "f" na intervale "[ymin, ymax]"
xngrad = 10  # Zobrazený bude každý "xngrad" vzorkovací bod v smere osi "x"
yngrad = xngrad  # Zobrazený bude každý "yngrad" vzorkovací bod v smere osi "y"

# Tvorba gridu
x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))

# Výpočet funkcie
f = np.sin(2.0 * x) + np.cos(2.0 * y)

# Výpočet derivácií "f" podľa "x" a "y"
fx =  2.0 * np.cos(2.0 * x)
fy = -2.0 * np.sin(2.0 * y)

# Vykreslenie
fig, ax = plt.subplots(figsize=(12.0 / 2.54, 8.0 / 2.54))
im = ax.imshow(f, extent=(xmin, xmax, ymin, ymax), cmap="bwr",
               vmin=-np.abs(f).max(), vmax=np.abs(f).max())
ax.quiver( x[::xngrad, ::xngrad],  y[::yngrad, ::yngrad],
          fx[::xngrad, ::xngrad], fy[::yngrad, ::yngrad])
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_xticks(np.linspace(xmin, xmax, 6))
ax.set_yticks(np.linspace(ymin, ymax, 6))
fig.colorbar(im)
plt.show()


fig.savefig("../figs/f-gradf.pdf")
