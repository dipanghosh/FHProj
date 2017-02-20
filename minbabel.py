'''
Created on 20 Feb 2017

@author: dghosh
'''
import os
outputdir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/output/'
os.chdir(outputdir)
for filename in os.listdir(outputdir):
    #print filename[-4:]
    if filename[-4:]=='.pdb':
        os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 '+filename+' > ../3D_minBabel/'+filename)