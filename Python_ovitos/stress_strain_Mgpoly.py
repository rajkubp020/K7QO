from ovito.data import *
import numpy as np
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
data = '/Users/tanupittie/Documents/Polycrystal/tensile/export.txt'
x= np.loadtxt(data)
plt.show()
ar = np.zeros(320)
def modify(frame, input, output):
	global ar

	box = output['Simulation cell'].matrix
	ar[frame] = (box[0,0]/box[1,1])	
	f = int(frame/320*len(x))
	ax.clear()
	ax.plot(x[:,0],x[:,1])
	ax.plot(x[:f,0],x[:f,1],'-r',lw=2)
	ax.plot(np.arange(320)*200000/320,np.array(ar)/max(ar),'*m')
	fig.canvas.draw()
	print(frame)