import log
Tables = log.reader('log.lammps')
count = -1
tf = []
for i in range (15,195,15):
    for j in range (0,360,15):
        tf += ['{},{}'.format(i,j)]

for i in range (len(Tables['label'])):
    if 'impact' in Tables['label'][i]:
        count += 1
        if (Tables['df'][i]['PotEng'].values[-1] + 1322) >= 5 :
            print (tf[count], Tables['df'][i]['PotEng'].values[-1])
