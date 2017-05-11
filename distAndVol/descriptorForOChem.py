'''
Created on 10 May 2017

@author: dghosh
'''
import pickle, os
from dockingPipeline import pathCollections as pc
fracDict = pickle.load( open( pc.basepath+"perclist_actives" ) )
file = open(pc.basepath+pc.subpath+'ochemDesc.csv', 'w')
for k,v in fracDict.items():
    file.write("M"+str(k)+","+str(v)+"\n")
file.close()
