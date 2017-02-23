'''
Created on 23 Feb 2017

@author: dghosh
'''
import os
pdbOutputDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/output/'
pdbDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/3D_minBabel/'
dockPrepOutputdir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/vinaDockPrep/'
prepDoneDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/vinaprepDonePdb/'
prepErrorDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/vinaprepErrorPdb/'
randomSelDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/randomSelection/'
def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)