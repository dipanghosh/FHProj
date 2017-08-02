import loadfiles as ld
from dipan_utilities import utilities

with open('/Users/dghosh/Desktop/set3_aggregators') as f:
    set3Aggre = f.read().splitlines()
with open('/Users/dghosh/Desktop/set3-nonAggregators') as f:
    set3NonAggre = f.read().splitlines()

switchFile = open(ld.desktopDir + 'set3AggreRID.csv', 'w')
notSwitchFile = open(ld.desktopDir + 'set3nonAggreRID.csv', 'w')

utilities.pullFromDictAndWriteToFIle(ld.set3dict, set3Aggre, switchFile)
utilities.pullFromDictAndWriteToFIle(ld.set3dict, set3NonAggre, notSwitchFile)