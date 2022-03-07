from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
import numpy as np

def modify(frame, input, output):
    node = import_file("/Users/tanupittie/Desktop/tde12.xyz", columns = 
      ["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z", "None", "None""None"])

  # Perform Wigner-Seitz analysis:
    ws = WignerSeitzAnalysisModifier(
        eliminate_cell_deformation = True)
    ws.reference.load("/Users/tanupittie/Desktop/Mg.equi.dat")
    node.modifiers.append(ws)
    node.compute()
    occupancy = node.output['Occupancy'].array
    mask1 = (occupancy==0)
    mask2 = (occupancy>1)
    vacancies = np.count_nonzero((occupancy[mask1]))
    interstitials = np.count_nonzero((occupancy[mask2]))
    export_file(node, "/Users/tanupittie/Desktop/Defect.txt", "txt", 
        columns = ['Frame', 'vacancies', 'interstitials'],
        multiple_frames = True)
	


