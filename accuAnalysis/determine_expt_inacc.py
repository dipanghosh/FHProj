'''
Created on 27 Jun 2017
@author: dghosh
'''

from accuAnalysis import loadfiles as vd


def calculatesideSwitchM1(fromSet, toSet1, toSet2, *args):
    activeToInactive = set.intersection(activeSet[fromSet], inactiveSet[toSet1]) | set.intersection(activeSet[fromSet],
                                                                                                    inactiveSet[toSet2])
    InactiveToActive = set.intersection(inactiveSet[fromSet], activeSet[toSet1]) | set.intersection(
        inactiveSet[fromSet], activeSet[toSet2])
    sideswitch = activeToInactive | InactiveToActive
    return sideswitch


def compareSets(candidate, target):
    activeToInactive = set.intersection(activeSet[candidate], inactiveSet[target])
    inactiveToActive = set.intersection(inactiveSet[candidate], activeSet[target])
    return (len(activeToInactive), len(inactiveToActive))


def intersectionByIndex(i1, i2, givefullset=True):
    if givefullset:
        return len(set.intersection(fullset[i1], fullset[i2]))
    else:
        return len(set.intersection(activeSet[i1], activeSet[i2]))


fullset, activeSet, inactiveSet = ([] for i in range(3))
fullset.append(set(vd.listAll411))
fullset.append(set(vd.listAll1006))
fullset.append(set(vd.listAll588342))
activeSet.append(set(vd.list411))
activeSet.append(set(vd.list1006))
activeSet.append(set(vd.list588342))
for i, _ in enumerate(fullset):
    inactiveSet.append(fullset[i] - activeSet[i])


def calculateBalAccforSets(i, j):
    switched = compareSets(i, j)
    activeinCommon = float(intersectionByIndex(i, j, givefullset=False))
    totalinCommon = float(intersectionByIndex(i, j, givefullset=True))
    inactiveinCommon = totalinCommon - activeinCommon
    TP = activeinCommon - switched[0]
    TN = inactiveinCommon - switched[1]
    balAcc = 0.5 * ((TP / (TP + switched[0])) + (TN/ (TN + switched[1])))
    print balAcc


if __name__ == '__main__':
    print 100 - (100 * calculateBalAccforSets(0, 1))
