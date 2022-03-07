from ovito.io import *
from ovito.modifiers import *
from ovito.data import *
import os
import sys
import log_reader
import numpy as np

Folder = "/Users/tanupittie/Documents/Mg_tde"
node = None
for FILE in os.listdir(Folder):
    if ('defect' in FILE) or ('equi.dat' in FILE) or ('log' in FILE) or (FILE[0]=='.') or ('.py' in FILE) or ('.png' in FILE):
        pass
    else :
        print ('Filename = ', FILE)
        if node == None:
            node = import_file(Folder + '/' + FILE, multiple_frames = True , columns =
              ["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z", "None", "None""None"])
            ws = WignerSeitzAnalysisModifier(
                eliminate_cell_deformation = True)
            ws.reference.load(Folder + "/Mg.equi.dat")
            node.modifiers.append(ws)
        else:
            node.source.load(Folder + '/' + FILE, multiple_frames = True , columns =
              ["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z", "None", "None""None"])
        Tables = log_reader.reader(Folder + '/' + FILE + '.log')
        dfs = []
        for i in range (len(Tables['label'])):
            if 'impact' in Tables['label'][i]:
                dfs += [Tables['df'][i]]
        vacancy=[]
        interstitial=[]
        Frame=[]
        for frame in range(node.source.num_frames):
            #print (dfs[frame]['PotEng'][-1])
            if (dfs[frame]['PotEng'][-1]+1323)>6.8:
                node.compute(frame)
                occupancy = node.output['Occupancy'].array
                mask1 = (occupancy==0)
                mask2 = (occupancy>1)
                vacancy += [np.sum(mask1)]
                interstitial += [np.sum(mask2)]
                Frame+= [frame]
        np.savetxt(Folder + '/' + FILE + 'defect.txt',np.vstack([Frame,vacancy,interstitial]).T,header='frame vacancy interstitial',fmt='%d')
