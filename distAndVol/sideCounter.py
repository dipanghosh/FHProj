'''
Created on 3 Mar 2017
@author: dghosh



'''


import __main__
from dockingPipeline.pathCollections import subpath
#from distAndVol.determineCutoff import percList
__main__.pymol_argv = [ 'pymol', '-qc']
import os
import numpy as np
import pymol
from pymol import cmd
import matplotlib.pyplot as plt
import threading
from dockingPipeline import pathCollections as pc
from learning import pyDec
#from pprint import pprint
import pickle
@pyDec.timeit
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
@pyDec.timeit
def determineDist(inputFile, pseudoAtomCoord):
    dist2Dlist = []
    for i in range(1, cmd.count_states(inputFile.split(".")[0])):
        ligcoords = cmd.get_coords(inputFile.split(".")[0], i)
        distList = []
        for coord1 in ligcoords:
            distVector = coord1-pseudoAtomCoord
            distList.append(np.sqrt(np.vdot(distVector,distVector)))
        dist2Dlist.append(distList)
        #print dist2Dlist
    return dist2Dlist
@pyDec.timeit
def getCountAndPerc(superListAtomwise):
    counter = 0
    avgAtomInside = {}
    avgPercInside = {}
    for moleculeID, atomwiseSideList in superListAtomwise.items():
        insideAtomCount = []
        insideperc = []
        for confsideList in atomwiseSideList:
            insideAtomCount.append(confsideList.count(False))
            insideperc.append(confsideList.count(False) / float(len(confsideList))) #print np.mean(insideAtomCount)
        
        if insideAtomCount:
            avgAtomInside[moleculeID]=(np.mean(insideAtomCount))
        if insideperc:
            avgPercInside[moleculeID]=(np.mean(insideperc))
        counter = counter+1
        print "Processing complete for"+moleculeID,
        print (str((float(counter)/len(superListAtomwise))*100)+"% done")        
    return avgAtomInside, avgPercInside
def getPheDist(np, cmd, superDistList, lenList, avgList, inputFile, tempdistArray):
    superDistList.append(tempdistArray)
    if isinstance(tempdistArray, np.ndarray):
        lenList.append(len(tempdistArray))
        avgList.append(np.mean(tempdistArray))
    cmd.delete(inputFile.split(".")[0] + "*")
def processMolecules(os, pc, centerpos, np, normalvector, cmd, superListAtomwise, superDistList, lenList, avgList, pseudoAtomCoord, inputFile):
    if inputFile.endswith(".pdbqt"):
        try:
            cmd.load(pc.vinaOutputDir + inputFile)
            superListAtomwise[inputFile.split(".")[0]] = determineSide(inputFile, centerpos, normalvector) #Get atom wise indication as to which side of the pocket it is, write them off to a list
            tempdistArray = np.array(determineDist(inputFile, pseudoAtomCoord)).mean(axis=0)
            getPheDist(np, cmd, superDistList, lenList, avgList, inputFile, tempdistArray) #print("Done with "+pc.vinaOutputDir+inputFile)
             #print (float(processcount/totalcount)*100)
        except:
            print "Unable to open to molecule, throwing into error and moving on"
            os.rename(pc.vinaOutputDir + inputFile, pc.processErrorDir + inputFile)
os.chdir(pc.basepath)
pc.createFolder(pc.processErrorDir)
centerpos = np.array((12.5, 36.7,8.3))
pointa = np.array([15.18700027,36.02099991,3.9849999 ])
pointb = np.array([17.23699951,37.56800079,8.26000023])
pointc = np.array([9.17000008,34.95100021,9.55500031])
normalvector = np.cross(pointa-pointb, pointa-pointc)
pymol.finish_launching()
cmd.load("/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/withPhem.pse")
superListAtomwise =  {}
superDistList = []
lenList = []
avgList = []
#inputFile = "1010824.ouput.pdbqt"
#cmd.load(pc.vinaOutputDir+inputFile)
pseudoAtomCoord = cmd.get_coords("phem")
processcount = 0
totalcount = len(os.listdir(pc.vinaOutputDir))
for inputFile in os.listdir(pc.vinaOutputDir):
    processMolecules(os, pc, centerpos, np, normalvector, cmd, superListAtomwise, superDistList, lenList, avgList, pseudoAtomCoord, inputFile)
    processcount = processcount + 1
    print processcount
#print superListAtomwise
explicitCountList, percDict = getCountAndPerc(superListAtomwise) #Read from that earlier list and calculate fractions of molecules INSIDE, averaged over their poses.
cmd.quit()
percList = []
for v in percDict.values():
    percList.append(v)
    
with open(subpath+'perclist_actives', 'wb') as fp:
    pickle.dump(percDict, fp)
with open(subpath+'distlist_actives', 'wb') as fp:
    pickle.dump(avgList, fp)
print 'done.'
#plt.hist(percList, bins = 100)
#plt.show()
# plt.hist(avgList, bins = 100)
# plt.show()

                    
                
