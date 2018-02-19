import collections
import pandas as pd

dataF = pd.read_csv("/Users/dghosh/Desktop/FreqHitterProject/Alphascreen/Data/DataExport_AlphaScreens_Lin28b_noPolyphor.csv", error_bad_lines=False)
dataF2 = pd.read_csv("/Users/dghosh/Desktop/FreqHitterProject/Alphascreen/Data/DataExport_AlphaScreens_PDEde_noPolyphor_bereinigt.csv", error_bad_lines=False)


def getHits(commoncomp):
    mylist = []
    for i in commoncomp:
        totalresVal =0
        #print i[0]
        resultForComp = dataF.loc[dataF['LDC_Nr.'] == i[0]]
        totalresVal = sum(resultForComp["Result_Value"])
        noTested = len(resultForComp["Result_Value"])
        if (totalresVal < 50 *  noTested):
            mylist.append(i[0])
    return mylist

def getCommonComp(df):
    idlist = df["LDC_Nr."].tolist()
    counterbj = collections.Counter(idlist)
    commoncomp = counterbj.most_common(10000)
    return commoncomp

hitList = dataF[dataF["Result_Value"] <= 50.0]
hitList2 = dataF2[dataF2["Result_Value"] <= 50.0]

commonHitID = set.intersection(set(hitList2['LDC_Nr.']),set(hitList2['LDC_Nr.']))

commonHit =  hitList[hitList['LDC_Nr.'].isin(commonHitID)]

commonHit.to_csv("LDC_commonhit.csv", columns=("LDC_Nr.", "Mol_Canonical"))



# for i in counterbj.items():
#     if i[1] < 1:
#         counterbj.pop(i[0])







