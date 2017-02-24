'''
Created on 23 Feb 2017

@author: dghosh
'''
import os
pdbOutputDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/output/'
pdbDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/3D_minBabel/'
dockPrepOutputdir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/vinaDockPrep/'
prepDoneDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/vinaprepDonePdb/'
prepErrorDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/vinaprepErrorPdb/'
randomSelDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/randomSelection/'
vinaOutputDir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/finalVinaOutput/'
vinaDoneDir = "/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/actives/vinaDoneDir/"
def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)