'''
Created on 10 May 2017

@author: dghosh
'''
import pickle, os
import matplotlib.pyplot as plt
from dockingPipeline import pathCollections as pc
fracDict = pickle.load( open( pc.basepath+pc.subpath+"perclist_actives" ) )
#file = open(pc.basepath+pc.subpath+'ochemDesc.csv', 'w')
percList = []
for v in fracDict.values():
    percList.append(v)
plt.hist(percList, bins = 100)
plt.show()
# plt.hist(avgList, bins = 100)
# plt.show()

# for k,v in fracDict.items():
#     file.write("M"+str(k)+","+str(v)+"\n")
# file.close()
