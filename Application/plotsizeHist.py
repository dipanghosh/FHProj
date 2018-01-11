import os, csv, sys
from matplotlib_venn import venn3, venn2
from dipan_utilities import utilities
from matplotlib import pyplot as plt
dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/AllData/'
plt.rcParams['svg.fonttype'] = 'none'
plt.figure(figsize=(10 ,10))


lengthList = []
for i, myfile in enumerate(utilities.findCSVFiles(dataDir)):
    if myfile.endswith(".csv"):
        compoundsTested = len(utilities.csvToDict(myfile))
        lengthList.append(compoundsTested)
sortedList = sorted(lengthList, reverse=True)
mye = [i+1 for i in range(len(lengthList))]
plt.bar(mye, sortedList)
plt.show()