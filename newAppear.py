'''
Created on 10 Feb 2017

@author: dghosh
'''
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn._venn2 import venn2

with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/411ActiveSIDList') as f:
    set411 = set(f.read().splitlines())
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/1006ActiveSIDList') as f:
    set1006 = set(f.read().splitlines())
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342ActiveSIDList') as f:
    set588342 = set(f.read().splitlines())
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/411SIDList') as f:
    setAll411 = set(f.read().splitlines())
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/1006SIDList') as f:
    setAll1006 = set(f.read().splitlines())
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342SIDList') as f:
    setAll588342 = set(f.read().splitlines())
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342_inconclusive') as f:
    setinconc588342 = set(f.read().splitlines())
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342_activeAt11_5um_SID') as f:
    set588342Activeat11um = set(f.read().splitlines())
    
inactive1006 = setAll1006 - set1006
inactive588342 = setAll588342 - (set588342Activeat11um|setinconc588342)
set588342Activeat11um = set588342Activeat11um - setinconc588342
#newin588342 = inactive1006 & set588342
#print len(newin588342)
venn3([inactive588342, inactive1006, set588342Activeat11um], ('Inactive in 588342', 'Inactive in 1006', 'Active in 588342'))
plt.show()
venn2([set1006, set588342Activeat11um], ('active in 1006', 'Active in 588342'))
plt.show()
plt.savefig('/Users/dghosh/Desktop/gained.png')

