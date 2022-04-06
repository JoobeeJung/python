#32scatter.py

import numpy as np
import matplotlib.pyplot as graph

N = 200
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2
graph.scatter(x, y, s=area, c=colors, alpha=0.5)
graph.grid(True)
graph.show()
