'''
Created on 8 May 2017

@author: dghosh
'''
from dockingPipeline import pathCollections as pc
import os
from shutil import copyfile
#print(len(os.listdir(pc.pdbDir)))

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]
for i in range(20):
    print("Starting to fill bin"+str(i))
    pc.createFolder(pc.pdbDir+"bin"+str(i))
    pc.createFolder(pc.pdbDir+"bin"+str(i)+"/pdbqt")
    for filename in split_list(os.listdir(pc.pdbDir), wanted_parts=20)[i]:
            copyfile(pc.pdbDir+filename, pc.pdbDir+'bin'+str(i)+"/"+filename)
        
#print len(split_list(os.listdir(pc.pdbDir), wanted_parts=20)[1])
