from dipan_utilities import utilities
import getUnique as gt
import exportOverlaps as ex

overlaps13 = ex.exportOverlaps(0, 2)
overlaps23 = ex.exportOverlaps(1, 2)
overlaps12 = ex.exportOverlaps(0, 1)
desktopDir = '/Users/dghosh/Desktop/'

#Accounting for all the molecules showing class changing
switchersForset1 = utilities.extractList(overlaps13[0], gt.set3dict)
switchersForset2 = utilities.extractList(overlaps23[0], gt.set3dict)
switchersForset2and1 = utilities.extractList(overlaps12[0], gt.set2dict)
switchersForset2and1From1 = utilities.extractList(overlaps12[0], gt.set1dict)

print len(switchersForset2and1From1)

set3list = utilities.extractList(gt.set3idSet, gt.set3dict)
uniqFromSet1 = utilities.extractList(gt.uniq1to3, gt.set1dict)
uniqFromSet2 = utilities.extractList(gt.uniq2to3, gt.set2dict)

combined = set.union(set(set3list), set(uniqFromSet1), set(uniqFromSet2))


combinedExcludeSwitching =(set(switchersForset1)|set(switchersForset2)|set(switchersForset2and1)|set(switchersForset2and1From1))
print len(combinedExcludeSwitching)
utilities.listToFile(desktopDir+'toExclude.txt', combinedExcludeSwitching)
