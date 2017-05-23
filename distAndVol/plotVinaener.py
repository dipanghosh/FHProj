'''
Created on 18 May 2017

@author: dghosh
'''
import os, pickle
from dockingPipeline import pathCollections as pc
import matplotlib.pyplot as plt
os.chdir(pc.basepath)
with open ('./actives/vinaScore.pkl', 'rb') as fp:
    activeScoreList = pickle.load(fp)
with open ('./inactives/vinaScore.pkl', 'rb') as fp:
    inactiveScoreList = pickle.load(fp)
plt.hist(activeScoreList, bins = 200, normed=True)
plt.hist(inactiveScoreList, bins = 200, normed=True)
plt.show()
