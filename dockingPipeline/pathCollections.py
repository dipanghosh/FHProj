'''
Created on 23 Feb 2017

@author: dghosh
'''
import os
basepath = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/strFromCorina/'
subpath = 'inactives/'
pdbOutputDir = basepath+subpath+'output/'
sdfdir = basepath+ subpath +"sdf/"
pdbDir = basepath+subpath+"pdb/"
dockPrepOutputdir = basepath+ subpath+'vinaDockPrep/'
prepDoneDir = basepath+ subpath+'vinaprepDonePdb/'
prepErrorDir = basepath+ subpath+'vinaprepErrorPdb/'
randomSelDir = basepath+ subpath+'randomSelection/'
vinaOutputDir = basepath+ subpath+'vinaoutput/'
vinaDoneDir = basepath+ subpath+'vinaDoneDir/'
processErrorDir = basepath+ subpath+ 'processError/'
customDir = basepath+'incorrInactives/'
def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        
        