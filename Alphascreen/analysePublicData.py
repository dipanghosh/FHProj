import pandas as pd
import numpy as np
from dipan_utilities import utilities
import itertools, collections

fileList = utilities.findCSVFiles("/Users/dghosh/Desktop/FreqHitterProject/Alphascreen/Data/public")

def extractIDList(filePath):
    mydf = pd.read_csv(filePath)
    idlist = mydf["PUBCHEM_SID"]
    return set(idlist)

#idSetList = [extractIDList(file) for file in fileList]
#utilities.plotVenn([idSetList[1], idSetList[2], idSetList[3]])

def extractActiveSID(filePath):
    mydf = pd.read_csv(filePath)
    actives = mydf[mydf['PUBCHEM_ACTIVITY_OUTCOME'] == "Active"]
    activesSID =  actives['PUBCHEM_SID'].astype('int32')
    return set(activesSID)

def extractActiveCID(filePath):
    mydf = pd.read_csv(filePath)
    actives = mydf[mydf['PUBCHEM_ACTIVITY_OUTCOME'] == "Active"]
    actives = actives[np.isfinite(actives['PUBCHEM_CID'])]
    activesCID =  actives['PUBCHEM_CID'].astype(int)
    return set(activesCID)



def counterFilter (counterobj, n):
    for i in counterobj.items():
        if i[1] < n:
            counterobj.pop(i[0])
    return counterobj.keys()

if __name__ == "__main__":
    idSetList = [extractActiveCID(file) for file in fileList]
    allActiveRepeatList = list(itertools.chain.from_iterable(idSetList))
    allActiveCounter = collections.Counter(allActiveRepeatList)

    freqActiveIDList = counterFilter(allActiveCounter, 3)
    #utilities.dumpToPickle("freqActiveIDList", freqActiveIDList)
    #utilities.listToFile("frequentActiveSIDList.txt", freqActiveIDList)
    inactiveIDList = set(allActiveRepeatList) - set(freqActiveIDList)

    utilities.dumpToPickle("publicdataDump", (inactiveIDList, freqActiveIDList))

    #utilities.plotVenn([idSetList[1], idSetList[2], idSetList[3]])