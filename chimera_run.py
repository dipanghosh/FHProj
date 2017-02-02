'''
Created on 2 Feb 2017

@author: dghosh
'''
import os
import chimera
from chimera import runCommand
#inputdir = ''
model = chimera.openModels.open('/Users/dghosh/Desktop/luciferaseForDocking.pdb')
for filename in os.listdir('.'):
    if filename.endswith(".pdb"):
        ligand = chimera.openModels.open(filename)
        receptorid = str(model[0].id)
        ligandid = str(ligand[0].id)
        ligandName = ligand[0].name
        commandString = 'vina docking receptor #'+receptorid+' ligand #'+ligandid+' output /Users/dghosh/Desktop/1006ActiveDockPrep/'+ligandName+' search_center 12.3515,36.5391,11.7799 search_size 14.113,16.9851,17.0 backend local location /Users/dghosh/Desktop/Tools/vina'
        runCommand(commandString)
        runCommand('close #'+ligandid)
        os.rename(filename, '../1006_activePrepDone/'+filename)