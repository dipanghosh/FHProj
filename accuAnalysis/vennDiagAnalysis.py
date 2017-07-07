from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles, venn2

with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/411ActiveSIDList') as f:
    list411 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/1006ActiveSIDList') as f:
    list1006 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342ActiveSIDList') as f:
    list588342 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/411SIDList') as f:
    listAll411 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/1006SIDList') as f:
    listAll1006 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342SIDList') as f:
    listAll588342 = f.read().splitlines()


# print list588342
def printcount(o):
    print len(o)


set1006 = set(list1006)
set588342 = set(list588342)
set411 = set(list411)
hitForThree = set.intersection(set1006, set588342, set411)
uniquein588342 = set588342 - (set1006 | set411)
onlyin1006 = (set1006 - (set588342 | set411))
onlyin411 = (set411 - (set588342 | set1006))
bothin1006and588342 = (set1006 - (hitForThree | onlyin1006))
bothin411and588342 = (set411 - (hitForThree | onlyin411))
notin588342 = (set1006 & set411) - set588342  #12 members belonging here both tested positive in 411 and 1006, not in 588342, False Negetives of 588342?
twiceHitNotin411 = bothin1006and588342 - set(listAll411)
twiceHitNotin1006 = bothin411and588342 - set(listAll1006)
falsePosin1006 = onlyin1006 & set(listAll411)

# Shall we consider the ones in only 1006 to be a false positive??, in that case::
# falsePosin1006 = onlyin1006

inactivein1006 = set(listAll1006) - set1006
inactivein411 = set(listAll411) - set411
active588342Inactive1006 = inactivein1006 & set588342
active588342Inactive1006Inactive411 = active588342Inactive1006 & inactivein411

allTwiceHits = twiceHitNotin1006 | twiceHitNotin411 | notin588342  # including the 12 members that tested negetive in 588342, because most likely they are false negetives.
reproducibleMembers = allTwiceHits | hitForThree  # These are having 2/2 or 3/3 hits, 12 of them have 2/3, but counting them as false negetives.
# printcount(reproducibleMembers)
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# printcount(set.union(set(listAll1006),set(listAll411),set(listAll588342)))
# print(len(hitForThree))
# print(len(uniquein588342))
# print(len(onlyin1006))

if __name__ == "__main__":
    pass
    # venn2([active588342Inactive1006, inactivein411])
    # venn3([set(list1006), set(list588342), set(list411)], ('AID1006', 'AID588342', 'AID411'))
    # plt.show()
