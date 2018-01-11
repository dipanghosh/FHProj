# from matplotlib import pyplot as plt
import numpy as np
# import pickle
import getActives as gt
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from dipan_utilities import pyDec

freqList = []
collectionofRearrangedDicts = []
localCollectionofDicts = gt.collectionofDicts

def bootstrap_resample(X, n=None):
    """ Bootstrap resample an array_like
    Parameters
    ----------
    X : array_like
      data to resample
    n : int, optional
      length of resampled array, equal to len(X) if n==None
    Results
    -------
    returns X_resamples
    """
    X = np.array(X)

    if n == None:
        n = len(X)

    resample_i = np.floor(np.random.rand(n) * len(X)).astype(int)
    X_resample = np.array(X[resample_i])
    return X_resample


def convertAssayDict(mydict):
    for i in mydict.keys():
        if mydict[i] == "Active":
            mydict[i] = 1
        else:

            mydict[i] = 0
    return mydict


def resampleAssayDict(mydict):
    mydict = convertAssayDict(mydict)
    arrayToRearrange = np.array(mydict.values())
    rearranged = bootstrap_resample(arrayToRearrange)
    for i, key in enumerate(mydict.keys()):
        mydict[key] = rearranged[i]
    return mydict


def determineFreq(compound):
    sum = 0
    compound_signature = gt.assignFingerprint(compound, collectionofRearrangedDicts)
    for flag in compound_signature:
        sum = sum + int(flag)
    freq = float(sum) / len(compound_signature)
    return [compound, len(compound_signature), sum, freq, compound_signature]


@pyDec.timeit
def getFreqList():
    global collectionofRearrangedDicts
    collectionofRearrangedDicts = [resampleAssayDict(singleAssayDict) for singleAssayDict in localCollectionofDicts]
    return [determineFreq(compound)[3] for compound in gt.dictofallCompounds.keys() if determineFreq(compound)[1] > 2]
    # if determineFreq(compound)[1] > 2

for i in range(100):
    print "Round " + str(i) + " of 100"
    freqList.append(getFreqList())
avgFreqList = np.mean(freqList, axis=0)


def normalize(input_array):
    result_array = (input_array - np.min(input_array)) / np.ptp(input_array)
    return result_array


navgFreqList = normalize(avgFreqList)

# for i in freqList:
#     print i[:20]
#
# print navgFreqList[:20]






# totalNum = 1000#len(gt.listofallCompounds)
# activeNum = 50#len(gt.listofAllactives)
#
#
# zeros = [0]*(totalNum - activeNum)
# ones = [1]*(activeNum)
#
# sampleList = zeros+ones
#
# listofResampledList = [bootstrap_resample(sampleList) for i in range(100)]
#
# bootstrapList = []
#
# for i in range(len(sampleList)):
#     print sum([resampledList[i] for resampledList in listofResampledList])
# #utilities.dumpToPickle("bootstrapped.p",bootstrapList)
