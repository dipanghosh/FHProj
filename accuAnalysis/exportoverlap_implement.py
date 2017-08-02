import exportOverlaps as ex
import loadfiles as ld
from dipan_utilities import utilities

overlaps12 = ex.exportOverlaps(0, 1)
switchFile = open(ld.desktopDir + 'set1to2Switched.csv', 'w')
NotswitchFile = open(ld.desktopDir + 'set1to2NotSwitched.csv', 'w')
utilities.pullFromDictAndWriteToFIle(ld.set2dict, overlaps12[0], switchFile)
utilities.pullFromDictAndWriteToFIle(ld.set2dict, overlaps12[1], NotswitchFile)

