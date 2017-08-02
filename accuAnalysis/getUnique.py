from accuAnalysis import loadfiles as ld
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn2
from dipan_utilities import utilities
set1dict = ld.set1dict
set2dict = ld.set2dict
set3dict = ld.set3dict

set1idSet = set(set1dict.keys())
set2idSet = set(set2dict.keys())
set3idSet = set(set3dict.keys())
uniq1to2 = set1idSet - set2idSet
uniq1to3 = set1idSet - set3idSet
uniq2to1 = set2idSet - set1idSet
uniq3to1 = set3idSet - set1idSet
uniq2to3 = set2idSet - set3idSet
uniq3to2 = set3idSet - set2idSet

def extractList(idlist, mydict):
    mylist = []
    for id in idlist:
        mylist.append(mydict[id])
    return mylist

uniq1to2l = extractList(uniq1to2, set1dict)
uniq1to3l = extractList(uniq1to3, set1dict)
uniq2to1l = extractList(uniq2to1, set2dict)
uniq3to1l = extractList(uniq3to1, set3dict)


# print len(uniq1to2)
# print len(uniq3to1)
# print len(uniq2to1)
# print len(uniq1to3)

# utilities.listToFile('/Users/dghosh/Desktop/uniq1to2.csv', uniq1to2l)
# utilities.listToFile('/Users/dghosh/Desktop/uniq1to3.csv', uniq1to3l)
# utilities.listToFile('/Users/dghosh/Desktop/uniq2to1.csv', uniq2to1l)
# utilities.listToFile('/Users/dghosh/Desktop/uniq3to1.csv', uniq3to1l)