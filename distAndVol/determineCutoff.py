'''
Created on 16 Mar 2017

@author: dghosh



'''
from dockingPipeline import pathCollections as pc
import os, pickle
import numpy as np

def dictTolist(dict):
    mylist = []
    for i in dict.values():
        mylist.append(i)
    return mylist
os.chdir(pc.basepath)

def calcAccuracy(list, list_actives, cutoff):
    #print "The current cutoff is     "+ str(cutoff)
    falseInactives = sum(x <= cutoff for x in list)
    trueInactives = len(list) - falseInactives
    trueActives = sum(x <= cutoff for x in list_actives)
    falseActives = len(list_actives) - trueActives
    balacc = 0.5*((float(trueInactives) / len(list))+(float(trueActives) / len(list_actives)))
    return (cutoff, falseInactives, trueInactives, falseActives, trueActives, balacc)

os.chdir(pc.basepath+pc.subpath)
perccutoffList = np.arange(0.3500, 0.4500, 0.01)

with open (pc.basepath+'/actives/perclist_actives', 'rb') as fp:
    percList = dictTolist(pickle.load(fp))

with open (pc.basepath+'/inactives/perclist_inactives', 'rb') as fp:
    percList_active = dictTolist(pickle.load(fp))


if __name__ == "__main__":
    for perccutoff in perccutoffList:
        print calcAccuracy(percList, percList_active, perccutoff)
