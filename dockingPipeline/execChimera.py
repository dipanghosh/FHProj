'''
Created on 2 Feb 2017

@author: dghosh
'''
import os
from shutil import copyfile
from dockingPipeline import pathCollections as pc
pdbDir = pc.pdbDir

os.chdir(pdbDir)
copyfile('/Users/dghosh/Documents/workspace/FSH/dockingPipeline/chimera_run.py','chimera_run.py')
os.system('/Applications/Chimera.app/Contents/MacOS/chimera --nogui chimera_run.py')