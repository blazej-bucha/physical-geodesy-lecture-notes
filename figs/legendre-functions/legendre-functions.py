# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

# Latitudes and their sines
lat = np.linspace(-np.pi / 2.0, np.pi / 2.0, 101)
t   = np.sin(lat)

# Legendre functions
p00 = np.ones(t.shape)
p10 = t
p11 = np.sqrt(1.0 - t**2)
p20 = 0.5 * (3.0 * t**2 - 1.0)
p21 = 3.0 * t * np.sqrt(1.0 - t**2)
p22 = 3.0 * (1.0 - t**2)

# Plotting
fig, ax = plt.subplots(figsize=(14.0 / 2.54, 9.0 / 2.54))
ax.plot(t, p00, label="$P_{0,0}$", color='#1f77b4')
ax.plot(t, p10, label="$P_{1,0}$", color='#ff7f0e')
ax.plot(t, p11, label="$P_{1,1}$", color='#ff7f0e', linestyle="dashed")
ax.plot(t, p20, label="$P_{2,0}$", color='#2ca02c')
ax.plot(t, p21, label="$P_{2,1}$", color='#2ca02c', linestyle="dashed")
ax.plot(t, p22, label="$P_{2,2}$", color='#2ca02c', linestyle="dotted")
ax.grid(visible=True)
ax.set_xlabel("$t$")
ax.legend(loc="center", bbox_to_anchor=(0.5, -0.35), ncol=6)
fig.subplots_adjust(bottom=0.3, top=0.98)
plt.show()

fig.savefig("../../latex/fig-legendre-functions.pdf")
