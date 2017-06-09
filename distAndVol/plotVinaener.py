'''
Created on 18 May 2017

@author: dghosh
'''
import os, pickle
from dockingPipeline import pathCollections as pc
import matplotlib
import matplotlib.pyplot as plt
os.chdir(pc.basepath)
with open ('./actives/vinaScore.pkl', 'rb') as fp:
    activeScoreList = pickle.load(fp)
with open ('./inactives/vinaScore.pkl', 'rb') as fp:
    inactiveScoreList = pickle.load(fp)
with open ('./inactives/vinaScore_custom.pkl', 'rb') as fp:
    inactiveScoreCustomList = pickle.load(fp)

ax = plt.subplot()
ax.set_xlim(-10, -4)
actives = plt.hist(activeScoreList, bins = 100, normed=True, label = 'Actives')
inactives = plt.hist(inactiveScoreList, bins = 100, normed=True, label = 'Inactives')
fp = plt.hist(inactiveScoreCustomList, bins = 100, normed=True, label = 'False Positives')
plt.legend(loc='upper right')
plt.show()
