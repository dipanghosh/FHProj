'''
Created on 23 Feb 2017

@author: dghosh
'''
import shutil,os,sys
from dockingPipeline import pathCollections as pc
os.chdir(pc.vinaOutputDir)
for filename in os.listdir("."):
    filenameNew = filename[:-11]+"pdb"
    print(pc.pdbDir+filenameNew)
    try:
        os.rename(pc.prepDoneDir+filenameNew, pc.vinaDoneDir+filenameNew)
    except:
        pass