import numpy as np
import matplotlib.pyplot as plt

# from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Generate some random data
np.random.seed(42)
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

# This will be used for coloring the points
color_values = np.random.rand(num_points)

# Create a 3D scatterplot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Scatterplot with color mapping
scatter = ax.scatter(x, y, z, c=color_values, cmap=cm.viridis)

# Add a colorbar
cbar = plt.colorbar(scatter)
cbar.set_label("FitIndex Plagioclase")

# Label the axes
ax.set_xlabel("Pressure (kbar)")
ax.set_ylabel("Temperature (C)")
ax.set_zlabel("H$_2$O (wt. %)")


# Adjust subplot dimensions to make space for the colorbar
plt.subplots_adjust(left=0.05, right=2)

# Show the plot
plt.show()
