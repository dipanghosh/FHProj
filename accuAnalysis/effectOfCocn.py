'''
Created on 3 Jul 2017

@author: dghosh
'''
from accuAnalysis import loadfiles as ld
from accuAnalysis import determine_expt_inacc as dt
import pprint
set3active50inactive11_5 = set.intersection(dt.inactiveSet[2], set(ld.list588342_50))
activesIncorr50 = set(ld.set3Incorr50)
print (len(set.intersection(set3active50inactive11_5, activesIncorr50))/float(len(activesIncorr50)))