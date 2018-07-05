import pandas as pd
import numpy as np
from dipan_utilities import utilities
import analysePublicData as an
import pickle

dataDir = "E:\FreqHitterProject\Alphascreen\Data\public"
fileList = utilities.findCSVFiles(dataDir)
with open("getactivesOut", 'rb') as f:
    listofAllactives, freqhitterList = pickle.load(f)

dFList = [pd.read_csv(csvfile) for csvfile in fileList]


masterList = pd.concat(dFList)

#print masterList.columns.values

def getCIDfromSID(SIDList):
    freqhitterDF =  masterList[masterList['PUBCHEM_SID'].isin(SIDList)]
    CIDList = freqhitterDF['PUBCHEM_CID'].fillna(0).astype(int).tolist()
    return set(CIDList)

freqhitterCIDList = getCIDfromSID(freqhitterList)
listofAllactivesCID = getCIDfromSID(listofAllactives)

listofinactivesCID = listofAllactivesCID - freqhitterCIDList


listofinactivesCID = list(listofinactivesCID)[1:]

freqhitterSmilesDF = utilities.getSmilesFromPubchem(freqhitterCIDList,
                                                   renameDict={'': 'externalid', 'IsomericSMILES': 'molecule'},
                                                   addCol={'Alphascreen-FHs': 'yes'})

inactiveSmilesDF = utilities.getSmilesFromPubchem(listofinactivesCID,
                                                   renameDict={'': 'externalid', 'IsomericSMILES': 'molecule'},
                                                   addCol={'Alphascreen-FHs': 'no'})
mergedDF = pd.concat([freqhitterSmilesDF, inactiveSmilesDF])
mergedDF.to_excel("stringentFHAlphascreen.xls")






