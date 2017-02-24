'''
Created on 23 Feb 2017

@author: dghosh
'''
import os
basepath = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/'
subpath = 'actives/'
pdbOutputDir = basepath+subpath+'output/'
pdbDir = basepath+ subpath+'3D_minBabel/'
dockPrepOutputdir = basepath+ subpath+'vinaDockPrep/'
prepDoneDir = basepath+ subpath+'vinaprepDonePdb/'
prepErrorDir = basepath+ subpath+'vinaprepErrorPdb/'
randomSelDir = basepath+ subpath+'randomSelection/'
vinaOutputDir = basepath+ subpath+'finalVinaOutput/'
vinaDoneDir = basepath+ subpath+'vinaDoneDir/'
def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)