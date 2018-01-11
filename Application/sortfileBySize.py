import os, csv, sys
from matplotlib_venn import venn3, venn2
from dipan_utilities import utilities
from matplotlib import pyplot as plt
dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/AllData/'


os.mkdir(dataDir+"smallData")
for i, myfile in enumerate(os.listdir(dataDir)):
    if myfile.endswith(".csv"):
        compoundsTested = len(utilities.csvToDict(dataDir + myfile))
        if compoundsTested<50000:
            os.rename(dataDir + myfile, dataDir + "smallData/" + myfile)

