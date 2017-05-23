'''
Created on 12 May 2017

@author: dghosh
'''



import matplotlib.pyplot as plt
def lineToFloat(strList):
    floatList = []
    for item in strList:
        floatList.append(float(item))
    return floatList
    return floatList
with open('/Users/dghosh/Desktop/inactive_uploaded') as f:
    inactiveList = f.read().splitlines()
with open('/Users/dghosh/Desktop/actives_uploaded') as f:
    activeList = f.read().splitlines()
inactivefloatList = lineToFloat(inactiveList)
activefloatList = lineToFloat(activeList)
#print floatList
plt.hist(inactivefloatList, bins = 250, normed=True)
plt.hist(activefloatList, bins = 250, normed=True)
plt.show()