'''
Created on 2 Feb 2017

@author: dghosh
'''
import os
from shutil import copyfile
pdbDir = '/Users/dghosh/Desktop/1006Active3D_minBabel'
os.chdir(pdbDir)
copyfile('/Users/dghosh/Documents/workspace/FSH/chimera_run.py','chimera_run.py')
os.system('/Applications/Chimera.app/Contents/MacOS/chimera --nogui chimera_run.py')