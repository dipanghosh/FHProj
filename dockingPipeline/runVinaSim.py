'''
Created on 30 Jan 2017

@author: dghosh
'''
import os
from dockingPipeline import pathCollections as pc
#import chimera_run
resultDir = pc.vinaOutputDir
pc.createFolder(resultDir)
inputdir = pc.dockPrepOutputdir
pdbDir = pc.prepDoneDir
vinaDoneDir = pc.vinaDoneDir
pc.createFolder(vinaDoneDir)
if __name__ == "__main__":
    for filename in os.listdir(pdbDir):
        #print filename[:-4]
        os.system('~/Desktop/Tools/vina --cpu 8 --receptor '+inputdir+filename[:-4]+'.receptor.pdbqt --ligand '+inputdir+filename[:-4]+'.ligand.pdbqt --out '+resultDir+filename[:-4]+'.ouput.pdbqt --config '+inputdir+filename[:-4]+'.conf')
        os.rename(pdbDir+filename, vinaDoneDir+filename)
        print ("\n\n\n"+pdbDir+filename+" moved to "+vinaDoneDir+filename+"\n\n\n")