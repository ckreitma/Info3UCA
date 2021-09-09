
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

x = [0.0, 0.56, ]
y = [0.0, 0.98]
z = [0.0, 0.55]
ax.plot3D(x, y, z, 'red')
ax.plot3D(x, y, [0, 0], 'blue')
ax.plot3D(x, [0, 0], z, 'blue')
ax.plot3D([0, 0], y, z, 'blue')
ax.view_init(azim=-90)
plt.show()
