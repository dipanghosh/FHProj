#from accuAnalysis import loadfiles as ld
from dipan_utilities import utilities
import random

with open('/Users/dghosh/Downloads/combined_inactive.csv') as f:
    mylist = f.read().splitlines()
randlist = random.sample(list(mylist), 10000)
utilities.listToFile('/Users/dghosh/Desktop/randListInactive', randlist)