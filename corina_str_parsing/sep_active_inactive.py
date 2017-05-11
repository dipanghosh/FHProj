'''
Created on 5 May 2017

@author: dghosh
'''
import shutil,os,sys
from string import rstrip
activeList = open('/Users/dghosh/Desktop/1006_actives.txt').readlines()
for activeFile in activeList:
    activeFile = rstrip(activeFile)
    try:
        os.rename('/Users/dghosh/Desktop/Str/'+activeFile+'.sdf', '/Users/dghosh/Desktop/Str/actives/'+activeFile+'.sdf')
    except:
        print(activeFile+" not found")