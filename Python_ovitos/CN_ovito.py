from ovito.data import *
import numpy as np
# to calculate the average coordination number and distribution for CSH particle system
def modify(frame, input, output):
	type = output['Particle Type'].array
	#print('type:',type)
	bonds = output['Bonds'].array
	#print('bonds:',bonds)
	atoms = len(type)
	print('Atoms:',atoms)
	CN = np.zeros((len(type),1))

	for i in bonds:
		CN[i[0]] += 1

	Cu_CN = CN[type==2] # get the distribution of bonds (or distribution of coordination number for each csh particle type 1 cutoff 60 uniform)

	avgcn = np.average(Cu_CN) # avg coordination number
	# distribution of bonds/ coordination number for each frame from 1 to 12
	cn1 = sum(Cu_CN==1)
	cn2 = sum(Cu_CN==2)
	cn3 = sum(Cu_CN==3)
	cn4 = sum(Cu_CN==4)
	cn5 = sum(Cu_CN==5)
	cn6 = sum(Cu_CN==6)
	cn7 = sum(Cu_CN==7)
	cn8 = sum(Cu_CN==8)
	cn9 = sum(Cu_CN==9)
	cn10 = sum(Cu_CN==10)
	cn11 = sum(Cu_CN==11)
	cn12 = sum(Cu_CN==12)
	cn13 = sum(Cu_CN==13)
	cn14 = sum(Cu_CN==14)
	cn15 = sum(Cu_CN==15)
	cn16 = sum(Cu_CN==16)
	cn17 = sum(Cu_CN==17)
	cn18 = sum(Cu_CN==18)
	cn19 = sum(Cu_CN==19)
# savind data in one list
	cn = np.zeros((1,22))
	cn[0,0] = frame
	cn[0,1] = atoms
	cn[0,2] = cn1
	cn[0,3] = cn2
	cn[0,4] = cn3
	cn[0,5] = cn4
	cn[0,6] = cn5
	cn[0,7] = cn6
	cn[0,8] = cn7
	cn[0,9] = cn8
	cn[0,10] = cn9
	cn[0,11] = cn10
	cn[0,12] = cn11
	cn[0,13] = cn12
	cn[0,14] = cn13
	cn[0,15] = cn14
	cn[0,16] = cn15
	cn[0,17] = cn16
	cn[0,18] = cn17
	cn[0,19] = cn18
	cn[0,20] = cn19
	cn[0,21] = avgcn
	print('cn_data:',cn)

	print('frame=%d'%int(cn[0,0]))
	np.savetxt("/Users/tanupittie/Documents/CuZrAl/cn_%d.csv"%(int(cn[0,0])), cn, fmt='%10.10f',delimiter=",")
	
	
