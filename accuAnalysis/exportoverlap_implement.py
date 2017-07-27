import exportOverlaps as ex
import loadfiles as ld
from dipan_utilities import utilities

overlaps = ex.exportOverlaps(1, 2)
switchFile = open(ld.desktopDir + 'set2to3SwitchedMID.csv', 'w')
notSwitchFile = open(ld.desktopDir + 'set2to3NotSwitchedMID.csv', 'w')
utilities.pullFromDictAndWriteToFIle(ld.set2dict, overlaps[0], switchFile)
utilities.pullFromDictAndWriteToFIle(ld.set2dict, overlaps[1], notSwitchFile)