import os
import re
import itertools as it
import headless
import pprint


dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/'
filename = dataDir+'mined'

class assaydata:
    source = 'source unknown'
    target = 'target unknown'
    activity = ''
    aid = 'Pubchem AssayID'
    date = ''

def createEntry(mylist):
    assayEntry = assaydata()
    for element in mylist:
        if element.__contains__('Source:'):
            assayEntry.source = element
        elif element.__contains__('AID:'):
            assayEntry.aid = element
        elif element.__contains__('BioActivity'):
            assayEntry.activity = element
        elif element.__contains__('Target'):
            assayEntry.target = element
        else: pass
    assayEntry.date = headless.getDepositDate(str.strip(assayEntry.aid.split(':')[1]))
    return assayEntry

listofassay = []
with open(filename,'r') as f:
    for key,group in it.groupby(f,lambda line: line.startswith('#')):
        if not key:
            group = list(group)
            assayentry = createEntry(group)
            listofassay.append(assayentry)

for i in listofassay:
    print i.date

broadinsttData = []
otherData = []
rnaiData = []

for index, assay in enumerate(listofassay):
    if (assay.source.__contains__('Broad')):
        broadinsttData.append(listofassay[index])
    elif (assay.source.__contains__('RNAi')):
        rnaiData.append(listofassay[index])
    else: otherData.append(listofassay[index])

compoundcountDict = {}

for assay in broadinsttData:
    coumpoundcountText = assay.activity.split(',')[-1]
    compoundcountDict[int(coumpoundcountText.split()[0])] = int(str.strip(assay.aid.split(':')[1]))

# for w in sorted(compoundcountDict, key=compoundcountDict.get, reverse=True):
#   print(w, compoundcountDict[w])

#print(compoundcountDict)



for i in compoundcountDict.keys():
    if (i<300000):
        pass
        #print(compoundcountDict[i])





