from ovito.data import *

def modify(frame, input, output):
	dam  = output['Damage'].marray
	print(dam.mean())