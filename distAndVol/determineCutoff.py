'''
Created on 16 Mar 2017

@author: dghosh



'''
from dockingPipeline import pathCollections as pc
import os
import pickle

def calcAccuracy(list, list_actives, cutoff):
    falseInactives = sum(x >= cutoff for x in list)
    trueInactives = sum(x < cutoff for x in list)
    trueActives = sum(x >= cutoff for x in list_actives)
    falseActives = sum(x < cutoff for x in list_actives)
    print 'For cutoff %f' % cutoff
    print 'Accuracy of Inactives',
    print float(trueInactives) / len(percList)
    print 'Accuracy of Actives',
    print float(trueActives) / len(percList_active)
os.chdir(pc.basepath)
perccutoffList = [x * 0.01 for x in range(10, 70)]
distcutoffList = [x * 0.01 for x in range(400, 800)]
with open ('perclist', 'rb') as fp:
    percList = pickle.load(fp)
with open ('distlist', 'rb') as fp:
    distlist = pickle.load(fp)
with open ('perclist_actives', 'rb') as fp:
    percList_active = pickle.load(fp)
with open ('distlist_actives', 'rb') as fp:
    distlist_actives = pickle.load(fp)
for perccutoff in perccutoffList:
    calcAccuracy(percList, percList_active, perccutoff)
for distcutoff in distcutoffList:
    calcAccuracy(distlist, distlist_actives, distcutoff)
