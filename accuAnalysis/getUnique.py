from accuAnalysis import loadfiles as ld

uniq1to2 = set(ld.set1RID) - set(ld.set2RID)
uniq1to3 = set(ld.set1RID) - set(ld.set3RID)
uniq2to1 = set(ld.set2RID) - set(ld.set1RID)
uniq3to1 = set(ld.set3RID) - set(ld.set1RID)

def listToFile(filename, listname):
    with open(filename, 'w') as f:
        for line in listname:
            f.write(line+'\n')

print len(uniq1to2)
print len(uniq3to1)
print len(uniq2to1)
print len(uniq1to3          )
# listToFile('/Users/dghosh/Desktop/uniq1to2', uniq1to2)
# listToFile('/Users/dghosh/Desktop/uniq1to3', uniq1to3)
# listToFile('/Users/dghosh/Desktop/uniq2to1', uniq2to1)
# listToFile('/Users/dghosh/Desktop/uniq3to1', uniq3to1)