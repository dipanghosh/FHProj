import os
from matplotlib_venn import venn3, venn2
from dipan_utilities import utilities
from matplotlib import pyplot as plt
dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/bigAssayOthers/'
bInDataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/BroadInstt/bigData/'


setlist = [utilities.csvToSet(dataDir+myfile) for myfile in os.listdir(dataDir)]
setlist2 = [utilities.csvToSet(bInDataDir+myfile) for myfile in os.listdir(bInDataDir)]
otherdata = set.union(*setlist)
bInData = set.union(*setlist2)
venn2((otherdata, bInData), set_labels=('Other Data', 'Broad Instt Data'))
plt.show()

