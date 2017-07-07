'''
Created on 27 Jun 2017
@author: dghosh
Loads and manages all files for accuracy analysis
'''
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/AID411/411_11.5um_actives') as f:
    list411 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/411ActiveSIDList') as f:
    list411_50 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/1006ActiveSIDList') as f:
    list1006 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/AID588342/588342_11.5um_actives') as f:
    list588342 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342ActiveSIDList') as f:
    list588342_50 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/411SIDList') as f:
    listAll411 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/1006SIDList') as f:
    listAll1006 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342SIDList') as f:
    listAll588342 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/AID588342/actives_incorrect_50') as f:
    set3Incorr50 = f.read().splitlines()
