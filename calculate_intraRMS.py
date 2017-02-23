'''
Created on 23 Feb 2017
@author: dghosh
'''

def getRmsdAvg(filename):
    cmd.load(filename)
    rmsdarray = cmd.intra_rms_cur(filename[:-6], 1)
    rmsdAvg = (sum(rmsdarray) + 1.0) / len(rmsdarray)
    cmd.delete(filename[:-6])
    return rmsdAvg
# import __main__
# __main__.pymol_argv = [ 'pymol', '-qc']
import os
import pymol
from pymol import cmd
import runVinaSim
targetDir = runVinaSim.resultDir
os.chdir(targetDir)
pymol.finish_launching()
for filename in os.listdir("."):
#filename = "14718841.ouput.pdbqt"
    rmsdAvg = getRmsdAvg(filename)
    print rmsdAvg