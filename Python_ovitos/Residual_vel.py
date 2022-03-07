from ovito.data import *

def modify(frame, input, output):
	damage = output['Damage'].array
	vz = output['VelocityZ'].array
	id = output['Particle Type'].array
	mask1 = (id ==2)	
	mask2 = (damage<0.5)
	mask = mask1 & mask2
	print(vz[mask].mean())