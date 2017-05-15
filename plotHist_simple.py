'''
Created on 12 May 2017

@author: dghosh
'''
import matplotlib.pyplot as plt
with open('/Users/dghosh/Desktop/inactive_uploaded') as f:
    strList = f.read().splitlines()
floatList = []
for item in strList:
    floatList.append(float(item))
print floatList
plt.hist(floatList, bins = 100)
plt.show()