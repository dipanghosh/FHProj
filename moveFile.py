'''
Created on 23 Feb 2017

@author: dghosh
'''
import shutil,os,sys
import runVinaSim
os.chdir(runVinaSim.resultDir)
for filename in os.listdir("."):
    filenameNew = filename[:-11]+"pdb"
    print(runVinaSim.pdbDir+filenameNew)
    #os.rename(runVinaSim.pdbDir+filenameNew, "/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/vinaDoneDir/"+filenameNew)