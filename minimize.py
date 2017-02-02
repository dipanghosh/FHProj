'''
Created on 30 Jan 2017

@author: dghosh
'''
import os
resultDir = "/Users/dghosh/Desktop/activeVinaOutput/"
inputdir = '/Users/dghosh/Desktop/output/'
outputDir = '/Users/dghosh/Desktop/1006Active3D_minBabel/'
for filename in os.listdir(inputdir):
    #print(inputdir+filename[:-4]+'.pdb')
    os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 '+inputdir+filename+' > '+outputDir+filename[:-4]+'.pdb')
    os.remove(inputdir+filename)