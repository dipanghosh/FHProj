'''
Created on 3 Mar 2017

@author: dghosh






'''
import __main__
__main__.pymol_argv = [ 'pymol', '-qc']
import os
import numpy as np
import pymol
from pymol import cmd
import matplotlib.pyplot as plt
from dockingPipeline import pathCollections as pc
from pprint import pprint


def determineSide(inputFile, centerpos, normalvector):
    dot2Dlist = []
    for i in range(1, cmd.count_states(inputFile.split(".")[0])):
        ligcoords = cmd.get_coords(inputFile.split(".")[0], i)
        dotList = []
        for coord1 in ligcoords:
            if np.dot(coord1 - centerpos, normalvector) > 0: # Positive means outside - Verify!
                dotList.append(True)
            else:
                dotList.append(False)            
        dot2Dlist.append(dotList)
    return dot2Dlist

def getCountAndPerc(superListAtomwise):
    avgAtomInside = []
    avgPercInside = []
    for atomwiseSideList in superListAtomwise:
        insideAtomCount = []
        insideperc = []
        for confsideList in atomwiseSideList:
            insideAtomCount.append(confsideList.count(False))
            insideperc.append(confsideList.count(False) / float(len(confsideList))) #print np.mean(insideAtomCount)
        
        if insideAtomCount:
            avgAtomInside.append(np.mean(insideAtomCount))
        if insideperc:
            avgPercInside.append(np.mean(insideperc))
    return avgAtomInside, avgPercInside
os.chdir(pc.basepath)
#inputFile = "17509699.ouput.pdbqt"
centerpos = np.array((12.5, 36.7,8.3))
pointa = np.array([15.18700027,36.02099991,3.9849999 ])
pointb = np.array([17.23699951,37.56800079,8.26000023])
pointc = np.array([9.17000008,34.95100021,9.55500031])
normalvector = np.cross(pointa-pointb, pointa-pointc)
pymol.finish_launching()
cmd.load("dist_det.pse")
superListAtomwise = []
for inputFile in os.listdir(pc.vinaOutputDir):
    if inputFile.endswith(".pdbqt"):
        cmd.load(pc.vinaOutputDir+inputFile)
        superListAtomwise.append(determineSide(inputFile, centerpos, normalvector)) #Get atom wise indication as to which side of the pocket it is.
        cmd.delete(inputFile.split(".")[0]+"*")
        #print np.mean(insideperc)*100,
#print avgAtomInside
#pprint(superListAtomwise[0])
explicitCountList, percList = getCountAndPerc(superListAtomwise)
plt.hist(percList, bins = 100)
plt.show()


                    
                
