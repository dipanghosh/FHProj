'''
Created on 3 Feb 2017

@author: dghosh
'''
import time
start_time = time.time()
import os
import csv
from numpy.lib.utils import _dictlist
csvfile =  open('/Users/dghosh/Desktop/1006OChem.csv', 'rU')
reader = csv.reader(csvfile)  # The reader object is a python generator, so for iterating over many times, it must be locally cached
with open('/Users/dghosh/Desktop/exclusion') as f:
    targetList = f.read().splitlines()
dictList = {}
for row in reader:
    dictList[row[1]] = row[0]  #Caching reader object to a dictionary
#print dictList
for target in targetList:
    print dictList[target]
print("--- %s seconds ---" % (time.time() - start_time))