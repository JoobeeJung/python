#28plot.py

import matplotlib.pyplot as graph
import numpy as np

x = np.arange(5)
y = np.arange(5)

graph.plot(x, y, "b-", x, y, "ro")
#graph.plot( )
#graph.plot()

# marker : 모양
"""
    o : circle, 8 : octagon, p : pentagon, D : diamond
    v ^ < >,        s : square, * : star , x,  d : thin_Diamon
"""
# 색 :
#   b : blue   r : red
#   m : magenta     g : green, c : cyan, y : yello

graph.xlabel("x")
graph.ylabel("y")
graph.title("Plot Line Marker")
graph.grid(True)
graph.savefig("d:/plot_marker.png")
graph.show()