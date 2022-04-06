#30curve.py

import numpy as np
import matplotlib.pyplot as graph

#x = np.arange(5)
x = np.linspace(0, 2 * np.pi , 100)
y = np.sin(x)

graph.xlabel("x axis")
graph.ylabel("y won")
graph.title("y = sin(x)")
graph.grid(True)
line = graph.plot(x, y)
xmin, xmax, ymin, ymax = np.amin(x), np.amax(x), -1, 1
graph.axis( [xmin, xmax, ymin, ymax] )
graph.plot([xmin, xmax], [0,0], color='blue', linewidth=4.0)
graph.setp(line, color='red', linewidth=2.0)


#graph.plot(x, y, "b-")
graph.show()