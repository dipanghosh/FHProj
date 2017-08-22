from accuAnalysis import loadfiles as ld
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn2
from dipan_utilities import utilities

set1dict = ld.set1dict
set2dict = ld.set2dict
set3dict = ld.set3dict

set1idSet = set(set1dict.keys())
set1inconcidSet = set(ld.set1inconclusivedict.keys())
set2idSet = set(set2dict.keys())
set3idSet = set(set3dict.keys())
set3inconcidSet = set(ld.set3inconclusivedict.keys())

garb = (set2idSet - set3idSet) - (set1inconcidSet | set3inconcidSet)
'''
A few molecules from set3 had no data point at 11.5uM, but the final curve was present. These molecules were lost while 
converting set3 to 11.5uM. Upon substracting set3 from set2, and counting out the inconclusives, these molecules remain at set2. 
For sake of being consistent, these are also being excluded.
'''

def getConclusiveunique(set1, set2):
    return (set1 - set2) - (set1inconcidSet | set3inconcidSet | garb)

uniq1to2 = getConclusiveunique(set1idSet, set2idSet)
uniq1to3 = getConclusiveunique(set1idSet, set3idSet)
uniq2to1 = getConclusiveunique(set2idSet, set1idSet)
uniq3to1 = getConclusiveunique(set3idSet, set1idSet)
uniq2to3 = getConclusiveunique(set2idSet, set3idSet)
uniq3to2 = getConclusiveunique(set3idSet, set2idSet)


def extractList(idlist, mydict):
    mylist = []
    for id in idlist:
        mylist.append(mydict[id])
    return mylist


uniq1to2l = extractList(uniq1to2, set1dict)
uniq1to3l = extractList(uniq1to3, set1dict)
uniq2to1l = extractList(uniq2to1, set2dict)
uniq2to3l = extractList(uniq2to3, set2dict)
uniq3to1l = extractList(uniq3to1, set3dict)
uniq3to2l = extractList(uniq3to2, set3dict)

#print len(set1inconcidSet), len(set3inconcidSet)
# print len(uniq1to2)
# print len(uniq1to3)
# print len(uniq2to1)
# print len(uniq2to3)
# print len(uniq3to1)
# print len(uniq3to2)

utilities.listToFile('/Users/dghosh/Desktop/uniq1to2l.csv', uniq1to2l)
utilities.listToFile('/Users/dghosh/Desktop/uniq1to3l.csv', uniq1to3l)
utilities.listToFile('/Users/dghosh/Desktop/uniq2to1l.csv', uniq2to1l)
utilities.listToFile('/Users/dghosh/Desktop/uniq2to3l.csv', uniq2to3l)
utilities.listToFile('/Users/dghosh/Desktop/uniq3to1l.csv', uniq3to1l)
utilities.listToFile('/Users/dghosh/Desktop/uniq3to2l.csv', uniq3to2l)
