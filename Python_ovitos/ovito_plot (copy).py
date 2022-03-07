from ovito.data import *
import numpy as np
import matplotlib.pyplot as plt

F = np.zeros((1001,1))
D = np.zeros((1001,1))

fig = plt.figure()
fig.show()

ax = fig.add_subplot(1,1,1)

def modify(frame, input, output):
	global F,D
	if frame == 0:
		F = np.zeros((1001,1))
		D = np.zeros((1001,1))
	mask  = (output['Position'].marray[:,0]>0)
	F[frame] = sum(output['ForceX'].marray[mask])
	mask  = (output['ForceX'].marray>0)
	D[frame] = (max(output['DisplacementX'].marray[mask]))
	ax.clear()
	ax.scatter(D[:frame],F[:frame])
	fig.canvas.draw()
	
	
	