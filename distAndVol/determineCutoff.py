'''
Created on 16 Mar 2017

@author: dghosh



'''
from dockingPipeline import pathCollections as pc
import os
import pickle

def dictTolist(dict):
    mylist = []
    for i in dict.values():
        mylist.append(i)
    return mylist
os.chdir(pc.basepath)

def calcAccuracy(list, list_actives, cutoff):
    falseInactives = sum(x >= cutoff for x in list)
    trueInactives = sum(x < cutoff for x in list)
    trueActives = sum(x >= cutoff for x in list_actives)
    falseActives = sum(x < cutoff for x in list_actives)
    #print falseInactives, trueInactives
    BalAcc = 0.5 * (float(trueActives) / (trueActives + falseActives) + float(trueInactives) / (trueInactives + falseInactives))
    print BalAcc
    #print 'For cutoff %f balanced accuracy %f' %(cutoff, BalAcc)
    print 'Accuracy of Inactives',
    print float(trueInactives) / len(percList)
    print 'Accuracy of Actives',
    print float(trueActives) / len(percList_active)
    #print 0.5*((float(trueInactives) / len(percList))+(float(trueActives) / len(percList_active)))
os.chdir(pc.basepath+pc.subpath)
perccutoffList = [x * 0.01 for x in range(10, 100)]
#distcutoffList = [x * 0.01 for x in range(400, 800)]
with open (pc.basepath+pc.subpath+'perclist_inactives', 'rb') as fp:
    percList = dictTolist(pickle.load(fp))
#with open ('distlist', 'rb') as fp:
    #distlist = pickle.load(fp)
with open (pc.basepath+pc.subpath+'perclist_actives', 'rb') as fp:
    percList_active = dictTolist(pickle.load(fp))
#with open ('distlist_actives', 'rb') as fp:
    #distlist_actives = pickle.load(fp)
for perccutoff in perccutoffList:
    calcAccuracy(percList, percList_active, perccutoff)
#for distcutoff in distcutoffList:
    #calcAccuracy(distlist, distlist_actives, distcutoff)
