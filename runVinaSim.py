'''
Created on 30 Jan 2017

@author: dghosh
'''
import os
resultDir = "/Users/dghosh/Desktop/1006ActiveVinaOutput/"
inputdir = '/Users/dghosh/Desktop/1006ActiveDockPrep/'
pdbDir = '/Users/dghosh/Desktop/1006_activePrepDone'
for filename in os.listdir(pdbDir):
    #print filename[:-4]
    os.system('~/Desktop/Tools/vina --receptor '+inputdir+filename[:-4]+'.receptor.pdbqt --ligand '+inputdir+filename[:-4]+'.ligand.pdbqt --out '+resultDir+filename[:-4]+'.ouput.pdbqt --config '+inputdir+filename[:-4]+'.conf')