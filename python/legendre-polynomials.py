# Import modulov
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

# Maximálny stupeň Legendreových polynómov
nmax = 5

# Vzorkovanie sférických šírok a ich sínusov
lat = np.linspace(-np.pi / 2.0, np.pi / 2.0, 101)
t   = np.sin(lat)

# Výpočet Legendreových polynómov pomocou rekurentných vzťahov
pn       = np.zeros((nmax + 1, t.shape[0]), dtype=np.float64)
pn[0, :] = 1.0
if nmax > 0:
    pn[1, :] = t
    for n in range(2, nmax + 1):
        pn[n, :] = ((2.0 * n - 1.0) / n) * t * pn[n - 1, :] - \
                   ((n - 1.0) / n) * pn[n - 2, :]

# Vykreslenie
fig, ax = plt.subplots(figsize=(13.0 / 2.54, 9.0 / 2.54))
ax.plot(t, pn.transpose())
ax.grid(visible=True)
ax.set_xlabel('$t$')
labels = [''] * (nmax + 1)
for n in range(nmax + 1):
    labels[n] = f'$P_{n}$'
ax.legend(labels, loc='center', bbox_to_anchor=(0.5, -0.35), ncol=nmax + 1)
fig.subplots_adjust(bottom=0.3, top=0.98)
plt.show()
fig.savefig('./fig-legendre-polynomials.pdf')
