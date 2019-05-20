import csv,os
import operator
from dipan_utilities import utilities
from collections import Counter

bInDataDir = '/Users/dghosh/Desktop/FreqHitterProject/Alphascreen/Data/public/'

listofAllactives = []
listofallCompounds = []
collectionofDicts = []


def csvToDict(filename):
    print filename
    reader = csv.reader(open(filename, 'r'))
    dict = {}
    try:
        for row in reader:
            k, v= row[1], row[3]
            dict[k] = v
    except:
        pass
    return dict

def getActives(mydict):
    activeSIDList = []
    for i in mydict.keys():
        if mydict[i] == "Active":
            activeSIDList.append(i)
    return activeSIDList

def testDict(mydict, number):
    for k, v in sorted(mydict.items(), key=operator.itemgetter(1))[:number]:
        print (k, v)

def collectFromAllCsv():
    for myfile in utilities.findCSVFiles(bInDataDir):
        if myfile.endswith(".csv"):
            global listofallCompounds, listofAllactives, collectionofDicts
            datadict = csvToDict(myfile)
            listofallCompounds = listofallCompounds + datadict.keys()
            collectionofDicts.append(datadict)
            listofAllactives = listofAllactives + getActives(datadict)


def assignFingerprint(compound, collectionofDicts):
    fingerprint = []
    for onedatadict in collectionofDicts:
        try:
            if (onedatadict[compound] == "Active" or onedatadict[compound] == 1 ):
                fingerprint.append(1)
            else:
                fingerprint.append(0)
        except(KeyError):
            pass
    return fingerprint


def determineFreq(compound):
    global collectionofDicts
    sum = 0
    compound_signature = assignFingerprint(compound, collectionofDicts)
    for flag in compound_signature:
        sum = sum + int(flag)
    freq = float(sum) / len(compound_signature)
    return [compound, len(compound_signature), sum, freq, compound_signature]


def determineFreqHits(compound):
    compound,timesTested,timesPositive, freq, compound_signature = determineFreq(compound)
    if (len(compound_signature)> 4 and freq >0.5):
        print compound, compound_signature
        return compound



collectFromAllCsv()
#print testDict(collectionofDicts[0], 10)
dictofallCompounds = {i:"" for i in set(listofallCompounds)}

#freq = [determineFreq(compound)[3] for compound in dictofallCompounds.keys() if determineFreq(compound)[1] > 2]

def extractFingerprints():
    FHDict = {}
    for compound in dictofallCompounds.keys():
        #if determineFreqHits(compound):
        FHDict[determineFreq(compound)[0]] = determineFreq(compound)[4]
    return FHDict


if __name__ == "__main__":
    print len(dictofallCompounds)
    freqhitterList =  [determineFreqHits(compound) for compound in dictofallCompounds.keys() if determineFreqHits(compound)]
    #utilities.listToFile(bInDataDir + "freqHitterSIDList_new", freqhitterList)
    print len(listofallCompounds)
    print len(freqhitterList)
    print len(listofAllactives)

    utilities.dumpToPickle("getactivesOut", (listofAllactives, freqhitterList))



