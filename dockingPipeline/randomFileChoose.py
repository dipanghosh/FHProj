'''
Created on 21 Feb 2017

@author: dghosh
'''
import os,random
from shutil import copyfile
from dockingPipeline import pathCollections as pc
targetDir = pc.pdbDir
randomSelDir = pc.randomSelDir
pc.createFolder(randomSelDir)
if __name__ == "__main__":
    sourceSet = set(os.listdir(targetDir))
    excludeSet = set(os.listdir(pc.vinaDoneDir))
    sampleSet = sourceSet-excludeSet
    filenames = random.sample(sampleSet, 5000)
    #print filenames
    #print len(sourceSet)
    for fname in filenames:
        srcpath = os.path.join(randomSelDir, fname)
        copyfile(targetDir+fname, randomSelDir+fname)
        #print fname