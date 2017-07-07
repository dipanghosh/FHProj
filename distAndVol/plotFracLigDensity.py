'''
Created on 18 May 2017

@author: dghosh
'''
import os, pickle
from dockingPipeline import pathCollections as pc
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
def dictTolist(dict):
    mylist = []
    for i in dict.values():
        mylist.append(i)
    return mylist
os.chdir(pc.basepath)


with open ('./actives/vinaScore.pkl', 'rb') as fp:
    activeScoreList = pickle.load(fp)


with open ('./inactives/vinaScore.pkl', 'rb') as fp:
    inactiveScoreList = pickle.load(fp)

#print inactiveScoreList
with open ('./inactives/vinaScore_custom.pkl', 'rb') as fp:
    inactiveScoreCustomList = pickle.load(fp)


#y,binEdges=np.histogram(activeScoreList,bins=100)

sb.set(font_scale = 2)
sb.set_style('whitegrid')
#sb.set_context("paper", rc={"font.size":18,"axes.titlesize":18,"axes.labelsize":15, "font_scale": 20})
plot = sb.kdeplot(np.array(activeScoreList), bw=0.05, label = 'Actives')
plot = sb.kdeplot(np.array(inactiveScoreList), bw=0.01, label = 'Inactives')
#plot = sb.kdeplot(np.array(inactiveScoreCustomList), bw=0.05, label = 'False Positives')
plot.set(xlim=(-11, -3))

plt.show()

# ax = plt.subplot()
# #ax.set_xlim(-10, -4)
# actives = plt.hist(activeScoreList, bins = 100, normed=True, label = 'Actives', histtype='stepfilled' )
# inactives = plt.hist(inactiveScoreList, bins = 100, normed=True, label = 'Inactives', histtype='stepfilled')
# fp = plt.hist(inactiveScoreCustomList, bins = 100, normed=True, label = 'False Positives', histtype='stepfilled')
# plt.legend(loc='upper right')
# plt.show()
