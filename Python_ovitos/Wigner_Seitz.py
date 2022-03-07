from ovito.io import *
from ovito.data import *
from ovito.modifiers import *

def modify(frame, input, output):
    node = import_file("/Users/tanupittie/Desktop/tde12.xyz", columns = 
      ["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z", "None", "None""None"])

  # Perform Wigner-Seitz analysis:
    ws = WignerSeitzAnalysisModifier(
        eliminate_cell_deformation = True)
    ws.reference.load("/Users/tanupittie/Desktop/Mg.equi.dat")
    node.modifiers.append(ws)
    node.compute()
    Vacancies = node.output.attributes['WignerSeitz.vacancy_count']
    Interstitials = node.output.attributes['WignerSeitz.interstitial_count']
    export_file(node, "/Users/tanupittie/Desktop/Defect.txt", "txt", 
        columns = ['Frame', 'Vacancies', 'Interstitials'],
        multiple_frames = True)
	


