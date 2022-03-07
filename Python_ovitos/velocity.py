from ovito.data import *

def modify(frame, input, output):
	vx = output['VelocityX'].array
	vy = output['VelocityY'].array
	vz = output['VelocityZ'].array
	v2 = (vx**2+vy**2+vz**2)
	vr = (vx**2+vy**2)
	
	# Create a user-defined particle property.
	my_prop1 = ParticleProperty.create_user('Velocity**2', 'float', len(vx))
	my_prop1.marray[:] = v2

	my_prop2 = ParticleProperty.create_user('Velocity_r', 'float', len(vx))
	my_prop2.marray[:] = vr
	
	output.add(my_prop1)
	output.add(my_prop2)
