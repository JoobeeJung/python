#32scatter.py

import numpy as np
import matplotlib.pyplot as graph

# 3D를 위한 import
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = graph.figure(figsize=(8, 8))
fig.suptitle("$f(x, y) = x^2 + y^2$", color="#0000FF", fontsize=20)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
ax2 = fig.add_subplot(111, projection='3d')
surface = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.RdPu)
fig.colorbar(surface)
ax2.set_title("surface")

graph.show()
