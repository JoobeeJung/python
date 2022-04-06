#32SVM.py : Support Vector Machine 추세선

import numpy as np
import matplotlib.pyplot as graph

x = np.linspace(-10, 10, 101)
#m = 3
#c = -10
m, c = 3, -10
# y = ax + b = 3x - 10
y = m * x + c

e = np.random.normal(0, 10.0, x.size)
y1 = y + e

A = np.vstack([x, np.ones(len(x))]).T
a1, a2, a3, a4 = np.linalg.lstsq(A, y1)
m1, c1 = a1
y2 = m1 * x + c1

graph.plot(x, y, "b--", label="y=3x-10")


graph.grid(True)


graph.show()