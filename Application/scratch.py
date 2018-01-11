import pickle
import os
from mineTextData import assaydata
dataDir1 = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/'

listofassay = pickle.load(open(dataDir1 + "datainfo.pkl", "r"))

htmlfiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(dataDir1)
             for name in files
             if name.endswith(("csv"))]
print htmlfiles


# print len(listofassay)
#
# broadinsttData = []
# otherData = []
# rnaiData = []
#
# for index, assay in enumerate(listofassay):
#     if (assay.source.__contains__('Broad')):
#         broadinsttData.append(listofassay[index])
#     elif (assay.source.__contains__('RNAi')):
#         rnaiData.append(listofassay[index])
#     else: otherData.append(listofassay[index])



