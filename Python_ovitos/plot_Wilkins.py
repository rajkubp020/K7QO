from ovito.data import *
import matplotlib.pyplot as plt
fig, (ax,ax2)  = plt.subplots(1,2)
plt.show()
ms = ['bo','rs','g*','k^','m>','y<']
names = ['b4c','al','jec','tip','core','tail']

def modify(frame, input, output):
	for i in output:
		#print(i)
		pass
	
	dam  = output['Damage'].marray
	vz  = output['VelocityZ'].marray
	for i in range(1,7):
		mask1  = output['Particle Type'].marray==i
		ax.plot(frame,dam[mask1].mean(),ms[i-1])
		ax2.plot(frame,vz[mask1].mean(),ms[i-1])
	ax.legend(names,loc=2,bbox_to_anchor=[0,1])
	fig.canvas.draw()
	