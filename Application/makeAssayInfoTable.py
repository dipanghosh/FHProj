import pickle
from mineTextData import assaydata

dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/'
listofassay = pickle.load(open(dataDir + "datainfo.pkl", "r"))

def stringCleanup(infostr):
    try:
        return str.strip(infostr).split(':')[1]
    except(IndexError):
        return infostr



for index, assay in enumerate(listofassay):
    source = stringCleanup(assay.source)
    target = stringCleanup(assay.target)
    activity = stringCleanup(assay.activity)
    assayid = stringCleanup(assay.aid)
    date = stringCleanup(str(assay.date))
    print '|'.join(map(str, [index + 1, source,    target,    activity,    assayid,    date]))

