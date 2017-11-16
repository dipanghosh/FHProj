import csv,os
import operator
from collections import Counter

bInDataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/AllData/'

listofAllactives = []
listofallCompounds = []
collectionofDicts = []


def csvToDict(filename):
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
    global activeSIDList
    activeSIDList = []
    for i in mydict.keys():
        if mydict[i] == "Active":
            activeSIDList.append(i)
    return activeSIDList

def testDict(mydict, number):
    for k, v in sorted(mydict.items(), key=operator.itemgetter(1))[:number]:
        print (k, v)

def collectFromAllCsv():
    for myfile in os.listdir(bInDataDir):
        if myfile.endswith(".csv"):
            global listofallCompounds, listofAllactives
            datadict = csvToDict(bInDataDir+myfile)
            listofallCompounds = listofallCompounds + datadict.keys()
            collectionofDicts.append(datadict)
            listofAllactives = listofAllactives + getActives(datadict)


def assignFingerprint(compound):
    fingerprint = []
    global collectionofDicts
    for onedatadict in collectionofDicts:
        try:
            if onedatadict[compound] == "Active":
                fingerprint.append(1)
            else:
                fingerprint.append(0)
        except(KeyError):
            pass
    return fingerprint


def determineFreqHits(compound):
    sum = 0
    compound_signature = assignFingerprint(compound)
    for flag in compound_signature:
        sum = sum + int(flag)
    freq = float(sum) / len(compound_signature)
    if not (len(compound_signature) == 1):
        if not (len(compound_signature) == 2 and (freq == 0.5 or freq == 1)):
            if freq > 0.4:
                return [compound, len(compound_signature), sum, freq, compound_signature]


collectFromAllCsv()
dictofallCompounds = {i:"" for i in set(listofallCompounds)}

if __name__ == "__main__":
    print [determineFreqHits(compound) for compound in dictofallCompounds.keys() if determineFreqHits(compound)]



