# Vykreslenie Legendreových polynómov

# Import modulov
import numpy as np
import matplotlib.pyplot as plt

# Maximálny stupeň 
nmax = 5

# Vzorkovanie sférických šírok
lat = np.linspace(-np.pi / 2.0, np.pi / 2.0, 101)
x   = np.sin(lat)

# Výpočet Legendreových polynómov pomocou rekurentných vzťahov
pn = np.zeros((nmax + 1, x.shape[0]), dtype=np.float64)
pn[0, :] = 1.0
if nmax > 0:
    pn[1, :] = x
    for n in range(2, nmax + 1):
        pn[n, :] = (2.0 * n - 1.0) / n * x * pn[n - 1, :] - \
                  (n - 1.0) / n * pn[n - 2, :]

# Vykreslenie
fig, ax = plt.subplots(figsize=(13.0 / 2.54, 9.0 / 2.54))
ax.plot(x, pn.transpose())
ax.grid(visible=True)
ax.set_xlabel("$x$")
labels = [""] * (nmax + 1)
for n in range(nmax + 1):
    labels[n] = "$P_%d$" % n
ax.legend(labels, loc="center", bbox_to_anchor=(0.5, -0.35), ncol=nmax + 1)
fig.subplots_adjust(bottom=0.3, top=0.98)
plt.show()

fig.savefig("../figs/legendre-polynomials.pdf")
