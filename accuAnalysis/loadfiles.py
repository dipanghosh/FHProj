'''
Created on 27 Jun 2017
@author: dghosh
Loads and manages all files for accuracy analysis
'''
desktopDir = '/Users/dghosh/Desktop/'

from dipan_utilities import utilities
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
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/SIDLists/588342_inconclusive') as f:
    listInconAll588342 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/DataMining/PubChem/AID588342/actives_incorrect_50') as f:
    set3Incorr50 = f.read().splitlines()
with open('/Users/dghosh/Desktop/FreqHitterProject/Luciferase/Analysis/MachineLearning/aggregation/set3_50_aggre_SID') as f:
    set3Aggre50 = f.read().splitlines()


set1dict = utilities.csvToDict('/Users/dghosh/Downloads/411_unique_1006.csv')
set2dict = utilities.csvToDict('/Users/dghosh/Downloads/1006_fluc_activity.csv')
set3dict = utilities.csvToDict('/Users/dghosh/Downloads/set3.csv')