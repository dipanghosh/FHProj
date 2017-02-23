'''
Created on 2 Feb 2017
This file is not supposed to be run from within Eclipse. It is to be called with chimera. Please use execChimera.py for this.
@author: dghosh
22Feb: Included error checking
'''
print 'This file is not supposed to be run from within Eclipse. It is to be called with chimera. Please use execChimera.py for this.'

import os, sys
import chimera
from chimera import runCommand
sys.path.append("/Users/dghosh/Documents/workspace/FSH")
from dockingPipeline import pathCollections as pc
#inputdir = ''
outputdir = pc.dockPrepOutputdir
doneDir = pc.prepDoneDir
errorDir = pc.prepErrorDir
pc.createFolder(outputdir)
pc.createFolder(doneDir)
pc.createFolder(errorDir)
model = chimera.openModels.open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/luciferaseForDocking.pdb')
for filename in os.listdir('.'):
    if filename.endswith(".pdb"):
        ligand = chimera.openModels.open(filename)
        receptorid = str(model[0].id)
        ligandid = str(ligand[0].id)
        ligandName = ligand[0].name
        try:
            commandString = 'vina docking receptor #'+receptorid+' ligand #'+ligandid+' output '+outputdir+ligandName+' search_center 12.3515,36.5391,11.7799 search_size 14.113,16.9851,17.0 backend local location /Users/dghosh/Desktop/Tools/vina'
            runCommand(commandString)
        except:
            os.rename(filename, errorDir+filename)
            print "Error!"  
        runCommand('close #'+ligandid)
        try:
            os.rename(filename, doneDir+filename)            
        except:
            print "No File to move! Moving on..."
            pass