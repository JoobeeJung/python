#35scatter.py

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

ax4 = fig.add_subplot(111, projection='3d')
surface = ax4.scatter(X, Y, Z)
#fig.colorbar(surface)
ax4.set_title("contour")

graph.show()
