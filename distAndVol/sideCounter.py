'''
Created on 3 Mar 2017
@author: dghosh
'''
# import __main__
# __main__.pymol_argv = [ 'pymol', '-qc']
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
            if np.dot(coord1 - centerpos, normalvector) > 0: # Positive means outside
                dotList.append(True)
            else:
                dotList.append(False)            
        dot2Dlist.append(dotList)
    return dot2Dlist
def determineDist(inputFile, pseudoAtomCoord):
    dist2Dlist = []
    for i in range(1, cmd.count_states(inputFile.split(".")[0])):
        ligcoords = cmd.get_coords(inputFile.split(".")[0], i)
        distList = []
        for coord1 in ligcoords:
            distVector = coord1-pseudoAtomCoord
            distList.append(np.sqrt(np.vdot(distVector,distVector)))
        dist2Dlist.append(distList)
    return dist2Dlist
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
centerpos = np.array((12.5, 36.7,8.3))
pointa = np.array([15.18700027,36.02099991,3.9849999 ])
pointb = np.array([17.23699951,37.56800079,8.26000023])
pointc = np.array([9.17000008,34.95100021,9.55500031])
normalvector = np.cross(pointa-pointb, pointa-pointc)
pymol.finish_launching()
cmd.load("withPhem.pse")
superListAtomwise =  []
superDistList = []
lenList = []
avgList = []
#inputFile = "1010824.ouput.pdbqt"
#cmd.load(pc.vinaOutputDir+inputFile)
pseudoAtomCoord = cmd.get_coords("phem")
for inputFile in os.listdir(pc.vinaOutputDir):
    if inputFile.endswith(".pdbqt"):
        cmd.load(pc.vinaOutputDir+inputFile)
        #superListAtomwise.append(determineSide(inputFile, centerpos, normalvector)) #Get atom wise indication as to which side of the pocket it is, write them off to a list
        tempdistArray = np.array(determineDist(inputFile, pseudoAtomCoord)).mean(axis = 0)
        superDistList.append(tempdistArray)
        if isinstance(tempdistArray, np.ndarray):
            lenList.append(len(tempdistArray))
            avgList.append(np.mean(tempdistArray))
        cmd.delete(inputFile.split(".")[0]+"*")
# explicitCountList, percList = getCountAndPerc(superListAtomwise) #Read from that earlier list and calculate fractions of molecules INSIDE, averaged over their poses.
cmd.quit()
plt.hist(lenList, bins = 100)
plt.show()
plt.hist(avgList, bins = 100)
plt.show()

                    
                
