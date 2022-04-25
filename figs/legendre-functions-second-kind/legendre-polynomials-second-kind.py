# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy.special
rc('text', usetex=True)

# Maximum harmonic degree of Legendre polynomials of the second kind
nmax = 5

# Latitudes and their sines
lat = np.linspace(-np.pi / 2.0, np.pi / 2.0, 101)
t   = np.sin(lat)

# Computation of Legendre functions of the second kind
qn = np.zeros((nmax + 1, len(t)))
for i in range(len(t)):
    qn[:, i] = scipy.special.lqmn(0, nmax, t[i])[0][0, :]

# Plotting.  The south and the north poles are not plotted due to the
# singulariries of Legendre functions of the second kind.
fig, ax = plt.subplots(figsize=(13.0 / 2.54, 9.0 / 2.54))
ax.plot(t[1:-1], qn[:, 1:-1].transpose())
ax.grid(visible=True)
ax.set_xlabel("$t$")
labels = [""] * (nmax + 1)
for n in range(nmax + 1):
    labels[n] = "$Q_%d$" % n
ax.legend(labels, loc="center", bbox_to_anchor=(0.5, -0.35), ncol=nmax + 1)
ax.set_ylim(-1.5, 1.5)
fig.subplots_adjust(bottom=0.3, top=0.98)
plt.show()

fig.savefig("../../latex/fig-legendre-polynomials-qn.pdf")
