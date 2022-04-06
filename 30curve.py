#30curve.py

import numpy as np
import matplotlib.pyplot as graph

#x = np.arange(5)
x = np.linspace(-5, 5, 100)
y = x**2 -1
graph.xlabel("x axis")
graph.ylabel("y won")
graph.title("Plot Math Function")
graph.grid(True)
graph.plot(x, y, "b-", x, y, "ro")
graph.show()