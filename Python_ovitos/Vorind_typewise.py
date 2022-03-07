# Import OVITO modules.
from ovito.data import *
from ovito.modifiers import *

# Import NumPy module.
import numpy
def modify(frame, input, output):

    mask1 = output['Particle Type'].array==1
    mask2 = output['Particle Type'].array==2
    voro_indices1 = output['Voronoi Index'].array[mask1]
    voro_indices2 = output['Voronoi Index'].array[mask2]

    def row_histogram(a):
        ca = numpy.ascontiguousarray(a).view([('', a.dtype)] * a.shape[1])
        unique, indices, inverse = numpy.unique(ca, return_index=True, return_inverse=True)
        counts = numpy.bincount(inverse)
        sort_indices = numpy.argsort(counts)[::-1]
        return (a[indices[sort_indices]], counts[sort_indices])

# Compute frequency histogram.
    unique_indices1, counts1 = row_histogram(voro_indices1)
    unique_indices2, counts2 = row_histogram(voro_indices2)

# Print the ten most frequent histogram entries.
    for i in range(10):
        print("%s\t%i\t(%.1f %%)" % (tuple(unique_indices1[i]),
                                     counts1[i],
                                     100.0*float(counts1[i])/len(voro_indices1)))
    print("\n\n")
    for i in range(10):
        print("%s\t%i\t(%.1f %%)" % (tuple(unique_indices2[i]),
                                     counts2[i],
                                     100.0*float(counts2[i])/len(voro_indices2)))
