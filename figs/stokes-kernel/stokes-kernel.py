import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

# Computation of the Stokes function
psi    = np.linspace(5.0 * np.pi / 180.0, np.pi, 100)
stokes = 1.0 / np.sin(psi / 2.0) - 6.0 * np.sin(psi / 2.0) + 1.0 - \
         5.0 * np.cos(psi) - 3.0 * np.cos(psi) * np.log(np.sin(psi / 2.0) + \
                                                        np.sin(psi / 2.0)**2)

# Plotting
fig, ax = plt.subplots(figsize=(14.0 / 2.54, 8.0 / 2.54))
ax.plot(psi * 180.0 / np.pi, stokes)
ax.set_xlabel("$\psi$ $(^\circ)$")
ax.set_ylabel("$S(\psi)$")
ax.grid(visible=True)
plt.subplots_adjust(top=0.98, bottom=0.15)
plt.show()

fig.savefig("../../latex/fig-stokes-kernel.pdf")
