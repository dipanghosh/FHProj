'''
Created on 14 Jun 2017

@author: dghosh
'''
import os
import re
import shutil
from dockingPipeline import pathCollections as pc
path = '/Volumes/01748907668/Pictures/Photography/EOS6D/Rome/2017-05-26/'
newpath = '/Volumes/01748907668/Pictures/Photography/EOS6D/Rome/2017-05-26/dups/'
pc.createFolder(newpath)
for filename in os.listdir(path):
    if filename.endswith(".CR2"):
        #print filename
        regex = r'romeTripDay3-(.+)\.CR2'
        match = re.search(regex, filename)
        if match:
            if int(match.group(1))%2 == 0:
                print filename
                shutil.move(path+filename, newpath+filename)