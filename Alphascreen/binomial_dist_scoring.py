import pickle
from scipy.stats import binom
#from Application import getActives as gt


p = 919463/3749017      #Probability of finding a hit

#temp = [gt.determineFreq(compound) for compound in gt.dictofallCompounds.keys()]
#pickle.dump(temp, open( "fingerprintDict.p", "wb"))

fingerprintList = pickle.load(open("fingerprintList.p", "rb"))
freqHList = []

def calculateBinomProb(fingerprint):
    compound, n, k, freq, fingerprint = fingerprint  # n = Number of times the compound is tested, k = Number of times a hit is found
    bDist = binom(n, p)
    binomProb = bDist.pmf(k)
    if (freq > binomProb + 0.2) and (n > 2): return (n, k, binomProb, freq)


for fingerprint in fingerprintList:
    binomF = calculateBinomProb(fingerprint)
    if binomF:
        freqHList.append(binomF)

print (len(freqHList))

