import pickle, re
import pandas as pd
import headless
from mineTextData import assaydata
import dipan_utilities.utilities as util

dataDir = '/Users/dghosh/Desktop/'
listofassay = pickle.load(open(dataDir + "datainfo.pkl", "r"))

def stringCleanup(infostr):
    try:
        return str.strip(infostr).split(':')[1]
    except(IndexError):
        return infostr


def getNoTested(activityStr):
    noTested = 0
    noActive = 0
    splituple = activityStr.split(',')
    for i in splituple:
        if i.__contains__('Tested'):
            noTested = i.split(" ")[1]
        if i.__contains__('Active'):
            noActive = i.split(" ")[1]
    return (noTested, noActive)


listoflists = []
for index, assay in enumerate(listofassay):
    source = stringCleanup(assay.source)
    target = stringCleanup(assay.target)
    activity = stringCleanup(assay.activity)
    assayid = stringCleanup(assay.aid)
    date = stringCleanup(str(assay.date))
    noTested, noActive = getNoTested(activity)
    #print '|'.join(map(str, [index + 1, source,    target,    noTested, noActive,    assayid,    date]))
    listoflists.append([index + 1, source,    target,    noTested, noActive,    assayid,    date])
assayData = pd.DataFrame(listoflists, columns=("Index", "Source", "Target", "Number tested", "Number Active", "Assay ID", "Date"))
assayData = assayData.infer_objects()
assayData[['Number tested', "Number Active"]] = assayData[['Number tested',  'Number Active']].apply(pd.to_numeric)
assayData.sort_values(by=['Number Active'], inplace=True, ascending= False)

for i in assayData['Assay ID'][0:10]:
    print i
    assayData['Protocol'] = headless.getDepositDate(str.strip(i))[1]
    assayData['Date'] = headless.getDepositDate(str.strip(i))[0]

util.viewTable(assayData)