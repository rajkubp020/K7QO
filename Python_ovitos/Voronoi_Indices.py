# Import OVITO modules.
from ovito.data import *
from ovito.modifiers import *

# Import NumPy module.
import numpy
def modify(frame, input, output):
# Load a simulation snapshot of a Cu-Zr metallic glass.
#node = import_file("../data/CuZr_metallic_glass.dump.gz")

# Set atomic radii (required for polydisperse Voronoi tessellation).
#atypes = node.source.particle_properties.particle_type.type_list
#atypes[0].radius = 1.35        # Cu atomic radius (atom type 1 in input file)
#atypes[1].radius = 1.55        # Zr atomic radius (atom type 2 in input file)

# Set up the Voronoi analysis modifier.
#voro = VoronoiAnalysisModifier(
 #   compute_indices = True,
 #   use_radii = True,
  #  edge_count = 6, # Length after which Voronoi index vectors are truncated
   # edge_threshold = 0.1
#)
#node.modifiers.append(voro)
                      
# Let OVITO compute the results.
#node.compute()

# Make sure we did not lose information due to truncated Voronoi index vectors.
#if voro.max_face_order > voro.edge_count:
 #   print("Warning: Maximum face order in Voronoi tessellation is {0}, "
  #        "but computed Voronoi indices are truncated after {1} entries. "
   #       "You should consider increasing the 'edge_count' parameter to {0}."
    #      .format(voro.max_face_order, voro.edge_count))
    # Note that it would be possible to automatically increase the 'edge_count'
    # parameter to 'max_face_order' here and recompute the Voronoi tessellation:
    #   voro.edge_count = voro.max_face_order
    #   node.compute()

# Access computed Voronoi indices as NumPy array.
# This is an (N)x(edge_count) array.
    voro_indices = output['Voronoi Index'].array

# This helper function takes a two-dimensional array and computes a frequency 
# histogram of the data rows using some NumPy magic. 
# It returns two arrays (of equal length): 
#    1. The list of unique data rows from the input array
#    2. The number of occurences of each unique row
# Both arrays are sorted in descending order such that the most frequent rows 
# are listed first.
    def row_histogram(a):
        ca = numpy.ascontiguousarray(a).view([('', a.dtype)] * a.shape[1])
        unique, indices, inverse = numpy.unique(ca, return_index=True, return_inverse=True)
        counts = numpy.bincount(inverse)
        sort_indices = numpy.argsort(counts)[::-1]
        return (a[indices[sort_indices]], counts[sort_indices])

# Compute frequency histogram.
    unique_indices, counts = row_histogram(voro_indices)

# Print the ten most frequent histogram entries.
    for i in range(10):
        print("%s\t%i\t(%.1f %%)" % (tuple(unique_indices[i]), 
                                     counts[i], 
                                     100.0*float(counts[i])/len(voro_indices)))
