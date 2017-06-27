'''
Created on 27 Jun 2017
@author: dghosh
'''

import vennDiagAnalysis as vd
def calculatesideSwitchM1(fromSet, toSet1, toSet2, *args):
    activeToInactive = set.intersection(activeSet[fromSet], inactiveSet[toSet1])|set.intersection(activeSet[fromSet], inactiveSet[toSet2])
    InactiveToActive = set.intersection(inactiveSet[fromSet], activeSet[toSet1])|set.intersection(inactiveSet[fromSet], activeSet[toSet2])
    sideswitch = activeToInactive|InactiveToActive
    return sideswitch
def compareSets(candidate, target):
    return (set.intersection(activeSet[candidate], inactiveSet[target])|set.intersection(inactiveSet[candidate], activeSet[target]))

fullset, activeSet, inactiveSet = ([] for i in range(3))
fullset.append(set(vd.listAll411))
fullset.append(set(vd.listAll1006))
fullset.append(set(vd.listAll588342))
activeSet.append(set(vd.list411))
activeSet.append(set(vd.list1006))
activeSet.append(set(vd.list588342))
for i,_ in enumerate(fullset):
    inactiveSet.append(fullset[i]-activeSet[i])
for j in range(3):
    for i in range(3):
        #print str(len(compareSets(j, i))) + "\t || \t",
        print str((len(compareSets(j, i))*100/float(len(fullset[j]))))+ "\t || \t",
    print ("\n")


