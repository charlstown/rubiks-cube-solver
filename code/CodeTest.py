import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create axis

axes = [3,3,3]
# Create Data
data = np.ones(axes, dtype=bool)

# Control colour
colors = np.empty(axes + [3], dtype=int)

colors[0] = [1, 0, 0] # red
colors[1] = [0, 1, 0] # green
colors[2] = [0, 0, 1] # blue


# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Voxels is used to customizations of
# the sizes, positions and colors.
ax.voxels(data, facecolors=colors, edgecolors='black')

# it can be used to change the axes view
ax.view_init(50, 0)

plt.show()