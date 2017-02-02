'''
Created on 1 Feb 2017

@author: dghosh
'''
import os
import csv
from numpy.lib.utils import _dictlist
csvfile =  open('/Users/dghosh/Desktop/1006OChem.csv', 'rU')
reader = csv.DictReader(csvfile)   # The reader object is a python generator, so for iterating over many times, it must be locally cached
with open('/Users/dghosh/Desktop/exclusion') as f:
    targetList = f.read().splitlines()
dictList = []
for row in reader:
    dictList.append(row)  #Caching reader object to a list
#print targetList
for target in targetList:
    #print target
    for row in dictList:
        #print row
        if row['EXTERNALID'] == target:
            print row['RECORDID']
    #print 'not found'