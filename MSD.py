#######

import MDAnalysis as mda
from MDAnalysis.tests.datafiles import LAMMPSDUMP
import MDAnalysis.analysis.msd as msd
u = mda.Universe("../results/lgnn/sio2_33/sio2_trigonal.dump", format="LAMMPSDUMP")
MSD = msd.EinsteinMSD(u, select='all', msd_type='xyz', fft=True)
MSD.results.timeseries

#Ravinder

# import sys
# !{sys.executable} -m pip install tidynamics #git+https://github.com/ravinderbhattoo/kurma.git
import MDAnalysis as mda
from MDAnalysis.tests.datafiles import LAMMPSDUMP
import MDAnalysis.analysis.msd as msd
from MDAnalysis.core.groups import AtomGroup as ag

u = mda.Universe("./BS00.fracture.lammpstrj", format="LAMMPSDUMP")
u.select_atoms('type 2')
MSD1 = msd.EinsteinMSD(u.select_atoms('type 1'),  msd_type='xyz', fft=True)
MSD2 = msd.EinsteinMSD(u.select_atoms('type 2'),  msd_type='xyz', fft=True)
MSD3 = msd.EinsteinMSD(u.select_atoms('type 3'),  msd_type='xyz', fft=True)
MSD4 = msd.EinsteinMSD(u.select_atoms('type 4'),  msd_type='xyz', fft=True)
MSD = msd.EinsteinMSD(u,  msd_type='xyz', fft=False)
# MSDall = msd.EinsteinMSD(u,  msd_type='xyz', fft=True)
MSD1.run()
MSD2.run()
MSD3.run()
MSD4.run()
MSD.run()
MSD.results.timeseries
# MSD.ag
# help(msd.EinsteinMSD)
# help(ag)
# ag.groupby(u,'type')
u.select_atoms('type 2')
plt.plot(MSD1.results.timeseries)
plt.plot(MSD2.results.timeseries)
plt.plot(MSD3.results.timeseries)
plt.plot(MSD4.results.timeseries)
plt.plot(MSD.results.timeseries,'k--')
