import os, csv, sys
from matplotlib_venn import venn3, venn2, venn2_unweighted
from dipan_utilities import utilities
from matplotlib import pyplot as plt
dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/AllData/BigData/'
plt.rcParams['svg.fonttype'] = 'none'
plt.figure(figsize=(25 ,25))



vennlist = []
constSet = utilities.csvToSet(utilities.findCSVFiles(dataDir)[5])
filecount = len(utilities.findCSVFiles(dataDir))

for i, myfile in enumerate(utilities.findCSVFiles(dataDir)):
    if myfile.endswith(".csv"):
        if i == filecount: i-=1
        else: i +=1
        plt.subplot(filecount / 4, 5, i)
        comparisonSet = utilities.csvToSet(myfile)
        figure = venn2((constSet, comparisonSet), set_labels=("", ""))
plt.savefig("venn-diag.svg")


#plt.show()






