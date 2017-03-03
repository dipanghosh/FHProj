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
from dockingPipeline import pathCollections as pc


def determineSide(inputFile, centerpos, normalvector):
    dot2Dlist = []
    for i in range(1, cmd.count_states(inputFile.split(".")[0])):
        ligcoords = cmd.get_coords(inputFile.split(".")[0], i)
        dotList = []
        for coord1 in ligcoords:
            dotList.append(np.dot(coord1 - centerpos, normalvector))
        dot2Dlist.append(dotList)
    print dot2Dlist


os.chdir(pc.basepath)
#inputFile = "17509699.ouput.pdbqt"
centerpos = np.array((12.5, 36.7,8.3))
pointa = np.array([15.18700027,36.02099991,3.9849999 ])
pointb = np.array([17.23699951,37.56800079,8.26000023])
pointc = np.array([9.17000008,34.95100021,9.55500031])
normalvector = np.cross(pointa-pointb, pointa-pointc)
pymol.finish_launching()
cmd.load("dist_det.pse")
for inputFile in os.listdir(pc.vinaOutputDir):
    if inputFile.endswith(".pdbqt"):
        cmd.load(pc.vinaOutputDir+inputFile)
        determineSide(inputFile, centerpos, normalvector)
        cmd.delete(inputFile.split(".")[0]+"*")

