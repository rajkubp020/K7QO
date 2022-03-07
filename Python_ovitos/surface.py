import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

(n, m) = (250, 250)

# Meshing a unit sphere according to n, m
theta = np.linspace(0, 2 * np.pi, num=25)#, endpoint=False)
phi = np.linspace(np.pi/12, np.pi , num=12)#, endpoint=False)
theta, phi = np.meshgrid(theta, phi)
theta, phi = theta.ravel(), phi.ravel()
print(phi.shape)
print(theta.shape)
print(theta)


#theta = np.append(theta, [0.]) # Adding the north pole...
#phi = np.append(phi, [np.pi*0.5])
#mesh_x, mesh_y = ((np.pi*0.5 - phi)*np.cos(theta), (np.pi*0.5 - phi)*np.sin(theta))
mesh_x, mesh_y = ((np.pi - phi)*np.cos(theta), (np.pi - phi)*np.sin(theta))
triangles = mtri.Triangulation(mesh_x, mesh_y).triangles
x, y, z = np.cos(phi)*np.cos(theta), np.cos(phi)*np.sin(theta), np.sin(phi)

# Defining a custom color scalar field
vals = np.sin(6*phi) * np.sin(3*theta)
colors = np.mean(vals[triangles], axis=1)

# Plotting
fig = plt.figure()
ax = fig.gca(projection='3d')
cmap = plt.get_cmap('Blues')
triang = mtri.Triangulation(x, y, triangles)
collec = ax.plot_trisurf(triang, z, cmap=cmap, shade=False, linewidth=0.)
collec.set_array(colors)
collec.autoscale()
plt.show()
