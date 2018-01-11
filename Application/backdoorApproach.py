from dipan_utilities import utilities
#import getActives as gt

dirPath = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/AllData/BigData-curated/inhibition/'

# setList = [utilities.csvToSet(myfile) for myfile in utilities.findCSVFiles(dirPath)]
#
# commons = set.intersection(*setList)
#
#utilities.listToFile(dirPath+"listofAllActives", set(gt.listofAllactives))

predictedPos = utilities.csvToSet('/Users/dghosh/Desktop/predicted_inhibitors')
predictedPosSmiles = utilities.csvToSet('/Users/dghosh/Desktop/model-pred-actives-smiles')
pPos1006 = utilities.csvToSet('/Users/dghosh/Desktop/1006-model-pred-actives')
activesPred = utilities.csvToSet(dirPath+'onlyActives_pred')
allActivesSet = utilities.csvToSet(dirPath+'listofAllActives')
#allActivesSet = set(gt.listofAllactives)
allset = utilities.csvToSet(dirPath+'commonList')
suspectedFH = utilities.csvToSet(dirPath+'freqHitterSIDList_new')
predictedFH = utilities.csvToSet('/Users/dghosh/Desktop/65661-pred-inh')
predictedNotFH = utilities.csvToSet('/Users/dghosh/Desktop/65661-pred-Notinh')

#FHDict = gt.extractFingerprints()

inactiveSet = allset - allActivesSet
predictedNeg = allset - predictedPos

activeAndCommon = set.intersection(allActivesSet, allset)
#hitList = [i for i in allActivesSet if sum(FHDict[i]) > 1]

#print len(hitList)

commonAndActive = set.intersection(predictedPosSmiles, suspectedFH, allset)

print len(inactiveSet)
print len(set.intersection(suspectedFH, allset))
print len(set.intersection(allActivesSet, allset))
print len(commonAndActive)



#utilities.listToFile('/Users/dghosh/Desktop/all_inactives', inactiveSet)

#print ((len(predictedPos)/float(len(allActivesSet))) + (len(predictedNeg)/float(len(inactiveSet))))/2
#commons = set.intersection(predictedSet, allActivesSet)
# count = 0
# print len(predictedNeg)
# for compound in predictedPos:
#     try:
#         fp = FHDict[compound]
#         if sum(fp):
#             print sum(fp)
#             count +=1
#     except(KeyError):
#         pass
# print count
#utilities.plotVenn([inactiveSet,allActivesSet, allset])
#utilities.plotVenn([predictedPos,suspectedFH])