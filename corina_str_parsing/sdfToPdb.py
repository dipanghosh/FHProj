'''
Created on 5 May 2017

@author: dghosh
'''
from dockingPipeline import pathCollections as pc
import os
from multiprocessing import Pool
def convertToPdb(infile):
    outfile = pc.pdbDir+infile[:-4]+".pdb"
    os.system('/opt/local/bin/babel '+pc.sdfdir+infile+" "+outfile)
# for file in os.listdir(pc.sdfdir):
#     convertToPdb(pc.sdfdir+file,pc.pdbDir+file[:-4]+".pdb")
pool = Pool(processes=8)
#os.chdir(pc.sdfdir)
pool.map(convertToPdb, os.listdir(pc.sdfdir))