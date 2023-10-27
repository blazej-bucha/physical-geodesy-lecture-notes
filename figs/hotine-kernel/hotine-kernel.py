import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

# Computation of the Hotine function
psi    = np.linspace(5.0 * np.pi / 180.0, np.pi, 100)
hotine = 1.0 / np.sin(psi / 2.0) - np.log(1.0 + 1.0 / np.sin(psi / 2.0))

# Plotting
fig, ax = plt.subplots(figsize=(14.0 / 2.54, 8.0 / 2.54))
ax.plot(psi * 180.0 / np.pi, hotine)
ax.set_xlabel("$\psi$ $(^\circ)$")
ax.set_ylabel("$H(\psi)$")
ax.set_xticks(np.arange(0, 200, 20))
ax.grid(visible=True)
plt.subplots_adjust(top=0.98, bottom=0.15)
plt.show()

fig.savefig("../../latex/fig-hotine-kernel.pdf")
