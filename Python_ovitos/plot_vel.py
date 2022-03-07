from ovito.data import *
import numpy as np
import matplotlib.pyplot as plt

V_tip = np.zeros((43,1))

fig = plt.figure()
fig.show()

ax = fig.add_subplot(1,1,1)

def modify(frame, input, output):
	global V_tip
	if frame == 0:
		V_tip = np.zeros((43,1))
	mask1 = (output('VelocityZ').array[295829:295850,:])
	mask2 = (output('VelocityZ').array[318402:318415,:])
	V_tip[frame] = np.average(output('VelocityZ').array[mask1 & mask2])
	
	ax.clear()
	ax.scatter(V_tip[:frame])
	fig.canvas.draw()
	
	
	