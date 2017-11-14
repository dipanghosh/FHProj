import os, csv, sys
from matplotlib_venn import venn3, venn2
from matplotlib import gridspec
from matplotlib import pyplot as plt
dataDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Application/Data/Pubchem/bigAssayOthers/'

def csvToSet(filename):
    reader = csv.reader(open(filename, 'r'))
    mylist = [row[1] for row in reader]
    return set(mylist)

fig = plt.figure()
vennlist = []
constSet = csvToSet(dataDir + os.listdir(dataDir)[1])
for i, myfile in enumerate(os.listdir(dataDir)):
    comparisonSet = csvToSet(dataDir+myfile)
    venn2((constSet, comparisonSet), set_labels=(os.listdir(dataDir)[1], myfile))
    plt.subplot(3, 4,i+1)
plt.show()




