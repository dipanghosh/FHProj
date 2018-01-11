from matplotlib import pyplot as plt
import numpy as np
import pickle
import getActives as gt
import bootstrap
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from dipan_utilities import utilities

majorLocator = MultipleLocator(0.1)
majorFormatter = FormatStrFormatter('%.2f')
minorLocator = MultipleLocator(0.01)


#timesTested = [gt.determineFreq(compound)[1] for compound in gt.dictofallCompounds.keys()]
#timetimesTested
#timesPositive = [gt.determineFreq(compound)[2] for compound in gt.dictofallCompounds.keys()]

#print len(gt.listofallCompounds)

freq = gt.freq

freqboot = bootstrap.navgFreqList

#utilities.dumpToPickle("freq.p", freq)


#plot = sb.kdeplot(np.array(timesTested), bw=0.5, label = 'Times Tested')
#plot = sb.kdeplot(np.array(timesActive), bw=0.5, label = 'Times Active')
#plot = sb.kdeplot(np.array(freq), bw=0.0005, label = 'Frequency')

fig, ax = plt.subplots()

plt.hist(freq, bins = 20, log=True,  alpha=0.5)
plt.hist(freqboot, bins = 20, log=True,  alpha=0.5)


ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)

# for the minor ticks, use no labels; default NullFormatter
ax.xaxis.set_minor_locator(minorLocator)
plt.show()
#plt.hist(timesTested, bins = 100, log=True)
#plt.hist(timesPositive, bins = 50, log=True)
#plt.show()

