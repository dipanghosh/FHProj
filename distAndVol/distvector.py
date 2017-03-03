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
from dockingPipeline import pathCollections as pc
os.chdir(pc.basepath)
inputFile = "17509699.ouput.pdbqt"
centerpos = np.array((12.5, 36.7,8.3))
pointa = np.array([15.18700027,36.02099991,3.9849999 ])
pointb = np.array([17.23699951,37.56800079,8.26000023])
pointc = np.array([9.17000008,34.95100021,9.55500031])
normalvector = np.cross(pointa-pointb, pointa-pointc)
pymol.finish_launching()

dotlist2 = []
cmd.load("dist_det.pse")
cmd.load(pc.vinaOutputDir+inputFile)
ringcoords = cmd.get_coords("ring")
for i in range(1,10):
    ligcoords = cmd.get_coords(inputFile.split(".")[0], i)
    dotList = []
    for coord1 in ligcoords:
       dotList.append(np.dot(coord1-centerpos, normalvector))
    dotlist2.append(dotList)
# for wehf in dotlist2: print wehf
# #print(dotList.pop())
# pymol.cmd.quit()
