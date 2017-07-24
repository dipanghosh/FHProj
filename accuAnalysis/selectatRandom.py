from accuAnalysis import loadfiles as ld
from dipan_utilities import utilities
import random

set3_50Inactives = set(ld.listAll588342) - set(ld.list588342_50)
randlist = random.sample(list(set3_50Inactives), 25000)
utilities.listToFile('/Users/dghosh/Desktop/randListInactive', randlist)