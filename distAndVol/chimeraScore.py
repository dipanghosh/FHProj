'''
Created on 18 May 2017

@author: dghosh
'''


import os
import re
import matplotlib.pyplot as plt
from dockingPipeline import pathCollections as pc
import pickle
def extractVinaEn(vinaEnList, count, inputFile, pc):
    enList = []
    if inputFile.endswith(".pdbqt"):
        with open(pc.vinaOutputDir + inputFile) as f:
            lines = f.readlines()
        for line in lines:
            if "REMARK VINA RESULT:" in line:
                regex = r'.+:\s+([+-].+?)(\s+.*$)'
                match = re.search(regex, line)
                if match:
                    try:
                        vinaEner = float(match.group(1))
                        enList.append(vinaEner) #print vinaEner
                    #print line
                    except:
                        print line #pass
        
        try:
            vinaEnList.append(sum(enList) / len(enList))
            print count #print enList
        except:
            print inputFile + " is probably not a vinaOutput file, skipping" #pass

vinaEnList = []
for count,inputFile in enumerate(os.listdir(pc.customDir)):
    extractVinaEn(vinaEnList, count, inputFile, pc)
with open(pc.basepath+pc.subpath+'vinaScore_custom.pkl', 'wb') as fp:
    pickle.dump(vinaEnList, fp)
plt.hist(vinaEnList, bins = 100)
plt.show()