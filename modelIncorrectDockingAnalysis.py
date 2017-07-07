'''
Created on 31 May 2017

@author: dghosh
'''
from accuAnalysis import vennDiag_ncorr_Analysis as vd
import os, shutil
from matplotlib import pyplot as plt
from dockingPipeline import pathCollections as pc

pc.createFolder(pc.basepath+'incorrInactives/')
for externalID in vd.atleastTwice:
    try:
        shutil.copy(pc.vinaOutputDir+externalID+'.pdbqt', pc.basepath+'incorrInactives/'+externalID+'.pdbqt')
    except:
        print externalID+' Failed!'