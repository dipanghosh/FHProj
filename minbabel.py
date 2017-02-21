'''
Created on 20 Feb 2017

@author: dghosh
'''
import os
#import threading
from subprocess import Popen
#from itertools import islice
from multiprocessing import Pool

outputdir = '/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/Docking/inactives/output/'
os.chdir(outputdir)
def minBabel(filename):
    os.system('/usr/local/bin/obminimize -ff -ff Ghemical -cg -n 2500 -c 1.0E-5 -cut -rvdw6.0 -rele 10.0 -pf 10 ' + filename + ' > ../3D_minBabel/' + filename)
    #print filename[-4:]
#     if filename[-4:]=='.pdb':
#         th = threading.Thread(target=minBabel, args = (filename,) )
#         th.start()
pool = Pool(processes=8)
pool.map(minBabel, os.listdir(outputdir))
#for command in processes:
    #myprocessess = (Popen(command, shell=True))
    