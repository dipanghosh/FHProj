import loadfiles as ld
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn2
import getUnique
from dipan_utilities import utilities

myfile = open('/Users/dghosh/Desktop/set2inconcset3.csv', 'w')
interestSet = set.intersection(set(ld.listAll1006), set(ld.listInconAll588342))

utilities.pullFromDictAndWriteToFIle(getUnique.set2dict, interestSet, myfile)