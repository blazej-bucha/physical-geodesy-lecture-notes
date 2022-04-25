# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy.special
rc('text', usetex=True)

# Maximum harmonic degree of Legendre functions of the second kind
nmax = 2

# Latitudes and their sines
lat = np.linspace(-np.pi / 2.0, np.pi / 2.0, 201)
t   = np.sin(lat)


# Computation of Legendre functions of the second kind
qn = np.zeros((nmax + 1, nmax + 1, len(t)))
for i in range(len(t)):
    qn[:, :, i] = scipy.special.lqmn(nmax, nmax, t[i])[0]

# Plotting.  The south and the north poles are not plotted due to the
# singulariries of Legendre functions of the second kind.  Note that we remove
# the Condon--Shortley phase factor that is included in the definition in
# SciPy.
fig, ax = plt.subplots(figsize=(14.0 / 2.54, 9.0 / 2.54))
ax.plot(t[1:-1], qn[0, 0, 1:-1], label="$Q_{0,0}$", color='#1f77b4')
ax.plot(t[1:-1], qn[0, 1, 1:-1], label="$Q_{1,0}$", color='#ff7f0e')
ax.plot(t[1:-1], (-1) * qn[1, 1, 1:-1], label="$Q_{1,1}$", color='#ff7f0e',
        linestyle="dashed")
ax.plot(t[1:-1], qn[0, 2, 1:-1], label="$Q_{2,0}$", color='#2ca02c')
ax.plot(t[1:-1], (-1) * qn[1, 2, 1:-1], label="$Q_{2,1}$", color='#2ca02c',
        linestyle="dashed")
ax.plot(t[1:-1], qn[2, 2, 1:-1], label="$Q_{2,2}$", color='#2ca02c', linestyle="dotted")
ax.grid(visible=True)
ax.set_xlabel("$t$")
ax.set_ylim(-3.0, 3.0)
ax.legend(loc="center", bbox_to_anchor=(0.5, -0.35), ncol=6)
fig.subplots_adjust(bottom=0.3, top=0.98)
plt.show()

fig.savefig("../../latex/fig-legendre-functions-qnm.pdf")
